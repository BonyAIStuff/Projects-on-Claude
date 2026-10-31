#!/usr/bin/env python3
"""Find technical glitches in a rendered video.

Usage: python3 glitches.py <video.mp4> [--speech-until SECONDS]

Prints JSON: black frames, frozen stretches, silent gaps, clipping, audio/video length
mismatch. --speech-until limits the silence check to the part with speech, since a
music-only tail may legitimately be quiet. Needs ffmpeg and ffprobe.
"""
import json, re, subprocess, sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def stream_durations(path):
    d = json.loads(run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,duration",
                        "-of", "json", path]).stdout)
    out = {}
    for s in d["streams"]:
        if "duration" in s:
            out[s["codec_type"]] = round(float(s["duration"]), 2)
    return out


def intervals(text, start_key, end_key):
    starts = [float(x) for x in re.findall(start_key + r":\s*(-?[\d.]+)", text)]
    ends = [float(x) for x in re.findall(end_key + r":\s*(-?[\d.]+)", text)]
    return [(round(a, 2), round(b, 2)) for a, b in zip(starts, ends)]


def main():
    path = sys.argv[1]
    speech_until = None
    if "--speech-until" in sys.argv:
        speech_until = float(sys.argv[sys.argv.index("--speech-until") + 1])

    vf = run(["ffmpeg", "-nostats", "-i", path, "-vf", "blackdetect=d=0.1:pix_th=0.08,freezedetect=n=0.001:d=1.5",
              "-an", "-f", "null", "-"]).stderr
    black = [(round(float(a), 2), round(float(b), 2)) for a, b in
             re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", vf)]
    freeze = intervals(vf, "freeze_start", "freeze_end")

    af = run(["ffmpeg", "-nostats", "-i", path, "-af", "silencedetect=n=-45dB:d=0.6,astats=metadata=0",
              "-vn", "-f", "null", "-"]).stderr
    silence = intervals(af, "silence_start", "silence_end")
    if speech_until is not None:
        silence = [s for s in silence if s[0] < speech_until]
    peak = re.findall(r"Peak level dB:\s*(-?[\d.inf]+)", af)
    peak_db = max((float(p) for p in peak if p not in ("-inf", "inf")), default=None)

    durs = stream_durations(path)
    av_gap = round(abs(durs.get("video", 0) - durs.get("audio", 0)), 2) if "audio" in durs else None

    issues = []
    if black:
        issues.append({"type": "black frames", "where": black})
    if freeze:
        issues.append({"type": "frozen picture (>1.5 s without any change)", "where": freeze,
                       "note": "fine if it's a deliberate hold on a graphic; a frozen talking head is a fault"})
    if silence:
        issues.append({"type": "audio gap (>0.6 s below -45 dB)", "where": silence})
    if peak_db is not None and peak_db > -0.5:
        issues.append({"type": "audio clipping", "where": "peak %.1f dBFS" % peak_db})
    if av_gap is not None and av_gap > 0.1:
        issues.append({"type": "audio and video lengths differ", "where": "%s s apart (%s)" % (av_gap, durs)})
    if "audio" not in durs:
        issues.append({"type": "no audio track", "where": "whole file"})

    print(json.dumps({"video": path, "durations": durs, "peak_db": peak_db, "issues": issues}, indent=2))


if __name__ == "__main__":
    main()
