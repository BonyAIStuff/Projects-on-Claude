#!/usr/bin/env python3
"""Measure a rendered video against a platform profile (youtube | instagram).

Usage: python3 measure.py <video.mp4> <youtube|instagram> <out_dir>

Writes <out_dir>/format-report.json and <out_dir>/safe-zones.png (contact sheet with the
platform's safe zones drawn on), and prints a short summary. Needs ffmpeg and ffprobe.
Everything here is measured from the render itself; the composition-level checks
(text sizes, elements off canvas, highlight density) are done by the skill with
`npx hyperframes check --json` and by looking at the contact sheet.
"""
import json, re, subprocess, sys
from pathlib import Path

PROFILES = {
    "youtube": {
        "size": (1920, 1080), "fps": 30,
        "max_static_s": 10.0,          # longest stretch without a cut / punch-in / B-roll
        "lufs": (-15.0, -13.0), "true_peak_max": -1.0,
        "max_hard_cuts_between_scenes": 0,
        # action-safe 5% margin for logos/graphics, title-safe 10% for text
        "zones": [("action-safe", 0.05, 0.05, 0.05, 0.05), ("title-safe", 0.10, 0.10, 0.10, 0.10)],
    },
    "instagram": {
        "size": (1080, 1920), "fps": 30,
        "max_static_s": 3.0,
        "lufs": (-15.0, -13.0), "true_peak_max": -1.0,
        "max_hard_cuts_between_scenes": None,   # hard cuts are fine on Reels
        # (name, top, right, bottom, left) as fractions: Reels UI covers the top bar,
        # the caption/username area at the bottom and the action column on the right
        "zones": [("reels-ui-safe", 0.12, 0.13, 0.22, 0.05)],
    },
}

CHANGE_PEAK = 0.06      # scene score that counts as a visual change (calibrated on whips/punch-ins)
CHANGE_FLOOR = 0.03     # frames above this join the surrounding change event
DETECT_REGION = 0.55    # analyse only the top 55% of the frame so caption pop-ins don't count as cuts


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(path):
    out = run(["ffprobe", "-v", "error", "-show_entries",
               "stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels:format=duration",
               "-of", "json", str(path)]).stdout
    d = json.loads(out)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), {})
    a = next((s for s in d["streams"] if s["codec_type"] == "audio"), None)
    num, den = (v.get("r_frame_rate", "0/1").split("/") + ["1"])[:2]
    return {
        "width": v.get("width"), "height": v.get("height"),
        "fps": round(int(num) / max(int(den), 1), 2), "video_codec": v.get("codec_name"),
        "audio": bool(a), "audio_codec": a and a.get("codec_name"),
        "duration_s": round(float(d["format"]["duration"]), 2),
    }


def scene_events(path):
    vf = "crop=iw:ih*%s:0:0,scale=320:-2,select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file=-" % DETECT_REGION
    out = run(["ffmpeg", "-loglevel", "error", "-i", str(path), "-vf", vf, "-f", "null", "-"]).stdout
    frames, t = [], None
    for line in out.splitlines():
        m = re.search(r"pts_time:([\d.]+)", line)
        if m:
            t = float(m.group(1))
        m = re.search(r"scene_score=([\d.]+)", line)
        if m and t is not None:
            frames.append((t, float(m.group(1))))
    events, cur = [], None
    for t, s in frames:
        if s >= CHANGE_FLOOR:
            if cur and t - cur["end"] <= 0.12:
                cur["end"] = t; cur["peak"] = max(cur["peak"], s); cur["frames"] += 1
            else:
                if cur:
                    events.append(cur)
                cur = {"start": t, "end": t, "peak": s, "frames": 1}
    if cur:
        events.append(cur)
    events = [e for e in events if e["peak"] >= CHANGE_PEAK]
    for e in events:
        # a whip/push/wipe smears across several frames; a raw cut is a one-frame spike
        e["kind"] = "animated" if e["frames"] >= 3 else "hard cut"
        e["start"], e["end"], e["peak"] = round(e["start"], 2), round(e["end"], 2), round(e["peak"], 3)
    return events


def static_stretches(events, duration, limit):
    marks = [0.0] + [e["start"] for e in events] + [duration]
    gaps = [(round(a, 2), round(b, 2), round(b - a, 2)) for a, b in zip(marks, marks[1:])]
    return max((g[2] for g in gaps), default=0), [g for g in gaps if g[2] > limit]


def loudness(path):
    err = run(["ffmpeg", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    summary = err[err.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[\d.]+) LUFS", summary)
    lra = re.search(r"LRA:\s+(-?[\d.]+) LU", summary)
    tp = re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary)
    return {"integrated_lufs": i and float(i.group(1)), "lra_lu": lra and float(lra.group(1)),
            "true_peak_dbtp": tp and float(tp.group(1))}


def contact_sheet(path, duration, w, h, zones, out_png):
    n = 12
    step = max(duration / n, 0.5)
    boxes = []
    for name, top, right, bottom, left in zones:
        color = "red" if "ui" in name else ("yellow" if name == "title-safe" else "cyan")
        x, y = int(w * left), int(h * top)
        bw, bh = int(w * (1 - left - right)), int(h * (1 - top - bottom))
        boxes.append("drawbox=x=%d:y=%d:w=%d:h=%d:color=%s@0.9:t=%d" % (x, y, bw, bh, color, max(4, w // 240)))
    tile = "4x3"
    scale = "scale=480:-2" if w >= h else "scale=270:-2"
    vf = "fps=1/%.3f,%s,%s,drawtext=text='%%{pts\\:hms}':x=10:y=10:fontsize=%d:fontcolor=white:box=1:boxcolor=black@0.6,tile=%s" % (
        step, ",".join(boxes), scale, 22 if w >= h else 16, tile)
    r = run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(path), "-vf", vf, "-frames:v", "1", str(out_png)])
    if r.returncode != 0:  # drawtext may be missing a font; retry without timestamps
        vf = "fps=1/%.3f,%s,%s,tile=%s" % (step, ",".join(boxes), scale, tile)
        run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(path), "-vf", vf, "-frames:v", "1", str(out_png)])
    return round(step, 2)


def main():
    video, platform, out_dir = Path(sys.argv[1]), sys.argv[2].lower(), Path(sys.argv[3])
    p = PROFILES[platform]
    out_dir.mkdir(parents=True, exist_ok=True)
    info = probe(video)
    events = scene_events(video)
    longest, too_long = static_stretches(events, info["duration_s"], p["max_static_s"])
    loud = loudness(video)
    sheet_step = contact_sheet(video, info["duration_s"], info["width"], info["height"], p["zones"], out_dir / "safe-zones.png")

    checks = []
    def add(name, ok, detail):
        checks.append({"check": name, "pass": None if ok is None else bool(ok), "detail": detail})

    W, H = p["size"]
    add("frame size", (info["width"], info["height"]) == (W, H), "%sx%s (want %sx%s)" % (info["width"], info["height"], W, H))
    add("frame rate", abs(info["fps"] - p["fps"]) < 0.1, "%s fps (want %s)" % (info["fps"], p["fps"]))
    add("codecs", info["video_codec"] == "h264" and info["audio_codec"] == "aac", "%s / %s (want h264 / aac)" % (info["video_codec"], info["audio_codec"]))
    add("visual change pace", not too_long,
        "longest stretch without a cut/punch-in/B-roll: %.1f s (max %.0f s)%s" % (
            longest, p["max_static_s"], "; too long: " + ", ".join("%s–%s s" % (a, b) for a, b, _ in too_long) if too_long else ""))
    if p["max_hard_cuts_between_scenes"] is not None:
        hard = [e for e in events if e["kind"] == "hard cut"]
        add("transitions smoothed", True if not hard else None,
            "%d one-frame hard cuts at %s s — confirm each is an intended punch-in on the same shot; a cut between different scenes needs a whip/push" % (
                len(hard), ", ".join(str(e["start"]) for e in hard)) if hard else "all scene changes are animated")
    lo, hi = p["lufs"]
    il, tp = loud["integrated_lufs"], loud["true_peak_dbtp"]
    add("loudness", il is not None and lo <= il <= hi, "%s LUFS integrated (want %s to %s)" % (il, lo, hi))
    add("true peak", tp is not None and tp <= p["true_peak_max"], "%s dBTP (max %s)" % (tp, p["true_peak_max"]))

    report = {"video": str(video), "platform": platform, "info": info, "loudness": loud,
              "change_events": events, "checks": checks,
              "contact_sheet": str(out_dir / "safe-zones.png"), "contact_sheet_step_s": sheet_step}
    (out_dir / "format-report.json").write_text(json.dumps(report, indent=2))
    for c in checks:
        mark = "PASS" if c["pass"] is True else ("REVIEW" if c["pass"] is None else "FAIL")
        print("%-6s %-22s %s" % (mark, c["check"], c["detail"]))
    print("contact sheet:", out_dir / "safe-zones.png")


if __name__ == "__main__":
    main()
