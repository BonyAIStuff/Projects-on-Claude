# Fixes

Fix in the composition, then re-render. Load `/hyperframes` first for the render contract.

## Wrong size / aspect
- Wrong project: the render came from the wrong scaffold. Make the 9:16 version with `/video-edit` Step 5 (portrait project, speaker-centred crop), never by letterboxing or stretching.
- Wrong fps: re-render with `--fps 30`.

## Something outside the frame or safe box
- Move or resize it inside the box (graphics: action-safe; text: title-safe / Reels safe).
- Push-ins: lower the end scale or move `transform-origin` toward the part that must stay visible; check the last frame of the push.
- Whips: only the landed position counts; the slide-in/out may cross the edge.

## Hard cut between scenes (YouTube)
Add the STYLE whip: outgoing `xPercent: -100, skewX: 8` (0.3 s, power3.in); incoming from `xPercent: 100, skewX: 8` to `0` (0.35 s, power3.out); a `whoosh-short` or `whoosh` at the cut − 0.1 s, volume 0.35–0.45. Overlap the two scene clips by the transition length.

## Too long without a visual change
In order of preference:
1. B-roll or a graphic for the line being spoken (it adds information).
2. A punch-in on the talking head: `tl.set("#thwrap", { scale: 1.14 }, t)` at a sentence boundary, back to 1.03 at the next one.
3. A text card for a key phrase (Reels).
Place changes on sentence or phrase boundaries from the transcript, never mid-word.

## Loudness
Preferred: fix the mix (raise the A-roll or VO `data-volume`, lower the music). If the overall level is just low, normalise the final file without touching the picture (two-pass loudnorm):

```bash
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2> pass1.txt
# read measured_I, measured_TP, measured_LRA, measured_thresh, target_offset from pass1.txt
ffmpeg -i in.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=<..>:measured_TP=<..>:measured_LRA=<..>:measured_thresh=<..>:offset=<..>:linear=true" -c:a aac -b:a 192k out.mp4
```

## Reels captions too small / too plain
Bump the caption size to ≥ 96 px, split lines to 2–4 words, move the block to the middle third, add a highlighter sweep to the key word of each line, and shorten the pop-in to 0.12 s with a 0.92→1 scale.
