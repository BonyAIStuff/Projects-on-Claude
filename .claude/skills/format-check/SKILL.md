---
name: format-check
description: Check a finished video against the platform rules for this channel before it's posted — YouTube long-form (16:9, everything inside the frame, smooth animated transitions, varied angles, comfortable long-viewing sound) and Instagram Reels (9:16, a visual change at least every 3 seconds, bigger turned-up captions with highlights, Reels safe zones). Measures the render (size, cut pace, loudness, safe zones), reviews the composition, reports PASS/FAIL with timestamps, and fixes after the creator approves. Use this whenever a video has been rendered, or the user says format check, "is this ready for YouTube/Instagram", "check the video", aspect ratio, safe zones, loudness, too slow, cuts, or before /video-post — even if they don't name the skill.
---

# Format check

The creator makes business and marketing explainers in the style in `video-channel/STYLE.md`. A video can be on-style and still fail on a platform: a logo cut off by the frame edge, a stretch with no visual change that loses Reels viewers, a mix that's too quiet next to other YouTube videos. This skill catches those before posting.

It works like a pre-flight checklist: measure what a script can measure, look at what needs eyes, then report. Nothing gets changed until the creator says so, because some "failures" are deliberate choices.

Platform rules are in `references/platform-rules.md`; fixes in `references/fixes.md`. Read both before reporting.

## Step 1 — Find what to check

In `video-channel/videos/<slug>/`, find the renders (`renders/*16x9*.mp4` for YouTube, `renders/*9x16*.mp4` for Instagram) and the HyperFrames project each came from (`edit/`, `shorts/short-<n>/`). If the creator only has one platform's render, check that one and say the other is missing. If a 9:16 version doesn't exist yet and they want Instagram, that's `/video-edit`'s job: say so rather than cropping the 16:9 file.

## Step 2 — Measure the render

For each render, from the repo root:

```bash
python3 .claude/skills/format-check/scripts/measure.py video-channel/videos/<slug>/renders/<file>.mp4 <youtube|instagram> video-channel/videos/<slug>/checks/<platform>/
```

It prints PASS / FAIL / REVIEW lines and writes `format-report.json` plus `safe-zones.png`, a 12-frame contact sheet with the platform's safe zones drawn on: cyan = action-safe (logos, graphics), yellow = title-safe (text), red = the area Instagram's own buttons and captions cover.

How it measures cuts: it scores frame-to-frame change in the top 55% of the picture (so caption pop-ins don't count) and groups changes into events. A whip/push smears over several frames ("animated"); a raw cut is a one-frame spike ("hard cut"). A hard cut on the same shot is a punch-in and is fine; a hard cut between two different scenes breaks the "smooth transitions" rule. Hand gestures can register as a change: confirm REVIEW items against the timeline (`npx hyperframes timeline --json` in the project) rather than trusting the number.

## Step 3 — Check the composition

From inside the project directory:

1. `npx hyperframes check --json`: elements off the canvas (`panel_out_of_canvas`, `container_overflow`), text below the size floor, unreadable lines.
2. Read `index.html` (and scene files) for the rules a render can't show: caption sizes, words per caption line, which words are highlighted, the music and SFX volumes and how many SFX there are per minute.
3. **Look at `safe-zones.png`.** Anything that is a logo, graphic or text and touches or crosses its safe box is a FAIL. So is anything clipped at the frame edge (a push-in on an article can drift the masthead off the top). Snapshot the exact moment for any doubt: `npx hyperframes snapshot --at <s>`.

## Step 4 — Report

Write `videos/<slug>/checks/FORMAT-CHECK.md` using this template, and show the creator the summary:

```markdown
# Format check — <slug> — <date>

## YouTube (16:9) — PASS | NEEDS FIXES
| Check | Result | Where | Fix |
|---|---|---|---|
| Frame 1920×1080 · 30 fps | PASS | | |
| Inside the frame (logos, graphics, text) | FAIL | 9.5–13 s masthead off top edge | Reduce push-in to 1.2× or move origin lower |
...

## Instagram Reels (9:16) — …

## Deliberate exceptions (creator approved)
- <anything the creator chose to keep, with the reason>
```

Lead with the failures, in plain words, with the timestamp. Keep PASS rows short. Then stop and ask which fixes to apply (default: all).

## Step 5 — Fix, re-render, re-check

Apply the approved fixes from `references/fixes.md` in the composition (never paper over a composition problem with an ffmpeg crop), re-run `npx hyperframes check`, re-render, and run Step 2 again on the new file. Repeat until every row is PASS or a creator-approved exception. Then tick "Format check" in the video's `STATUS.md` and commit the project and `checks/` (renders and footage stay out of Git).

If a fix would change the creative intent (e.g. adding cuts to a moment the creator wanted to hold), propose it and let them decide.
