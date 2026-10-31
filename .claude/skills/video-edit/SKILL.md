---
name: video-edit
description: Edit the channel's footage into finished videos in the signature style — transcribe talking-head or voiceover footage, cut it from the transcript, build the HyperFrames edit from SPEC.md and the style kit (captions, lower-thirds, chapter cards, B-roll, zooms, music), check, preview, and render the 16:9 long-form plus 9:16 Shorts/Reels/TikTok cuts. Use this whenever the user uploads or mentions footage, raw clips, A-roll/B-roll, a recording, or asks to cut, trim, edit, caption, add B-roll or music, make Shorts from a video, fix or re-render a video for this channel — even if they don't say "edit". Use /video-plan first if there's no approved SPEC.
---

# Video Edit

You are the editor. `/video-plan` produced an approved `SPEC.md`; the channel's look lives in `STYLE.md` and its reusable pieces in `compositions/components/`. Your job is to turn raw footage into videos that match both — the SPEC decides *what* happens, STYLE decides *how it looks and moves*. When they seem to conflict, STYLE wins on look, SPEC wins on content, and you mention the conflict.

Load `/hyperframes` before writing any composition, `/hyperframes-registry` before hand-building a visual, and `/media-use` for music, SFX, grades and transcription. Those skills hold the render contract; this one holds the channel's workflow.

## Step 0 — Orient

1. Find the video folder `videos/<slug>/` and read `STATUS.md`, `SPEC.md`, `SCRIPT.md` and the repo-root `STYLE.md`.
   - No SPEC or Gate 2 unticked → say so and offer `/video-plan`. Small one-off edits ("trim this clip and caption it") can proceed without a SPEC, but still in STYLE.
   - No STYLE.md → offer `/video-plan` style discovery; if the creator wants to proceed anyway, say the result won't be on-style.
2. If a project in the folder was opened in the HyperFrames desktop app, run `npx hyperframes catch-up <dir>` first and build on the creator's changes.

## Step 1 — Footage intake

Raw footage stays out of Git (GitHub refuses files over 100 MB and talking-head files pass that fast). Put it in `videos/<slug>/footage/` (git-ignored). Write `videos/<slug>/footage/INDEX.md`, which *is* committed: file name, duration (`ffprobe`), resolution, fps, what it is (A-roll take 2, B-roll #7…), and which SPEC rows it covers. Flag missing B-roll against the SCRIPT shot list now, not mid-edit.

## Step 2 — Transcribe and paper-cut

1. Transcribe each A-roll / voiceover file: `npx hyperframes transcribe <file> --json` (word-level timestamps; see `/media-use` `references/local.md` for engines and languages).
2. Build the **paper cut** in `videos/<slug>/CUTS.md`: the kept lines in SPEC order, each with `source file · in · out`, cut at word boundaries with ~80–120 ms of handle so words don't clip. Remove what STYLE.md says to remove (silences over its threshold, false starts, repeated takes — keep the best take, usually the last full one). List removed bits at the bottom so the creator can rescue one.
3. Re-time SPEC rows to the real speech. Keep their order and components.

Reviewing a cut as text is far faster for the creator than scrubbing a timeline, so show the paper cut when it changes the story (a dropped section, a reordered point). Otherwise carry on.

## Step 3 — Build the long-form edit (16:9)

Scaffold `videos/<slug>/long/` with `npx hyperframes init videos/<slug>/long --non-interactive --skip-skills --resolution landscape`, then copy in the style kit (`compositions/components/`, `assets/fonts/`, `assets/vendor/`) from the repo root so the project renders offline and on-style.

Then follow the SPEC row by row:
- **A-roll**: one `<video>` clip per CUTS.md segment, same source, `data-media-start` = segment in, `data-duration` = out − in, laid end to end. Keep audio on these (`data-has-audio="true"`).
- **B-roll**: muted `<video>` over the A-roll for the rows that call for it, using the style kit's transition; voice keeps running underneath (that's what makes B-roll feel continuous).
- **Captions**: the style kit caption component fed from the transcript's words for the kept segments, re-timed to the edit timeline.
- **Graphics**: hook card, lower-third, chapter cards, emphasis zooms, end screen — only from `compositions/components/`. If the SPEC needs something the kit lacks, build it as a new kit component (16:9 + 9:16) in STYLE's tokens and add it to STYLE.md's kit table, rather than a one-off.
- **Sound**: music bed and SFX per STYLE (levels, SFX only on visible actions) via `/media-use`.

## Step 4 — Check and self-review

Run `npx hyperframes check --json` and fix every error; weigh every warning. Then `npx hyperframes snapshot --review` and compare the frames against the style reel (`style-tests/style-reel.mp4`) and STYLE.md's rules. Write `videos/<slug>/REVIEW.md` with: what you checked, anything off-style and fixed, anything you're unsure about. A passing check doesn't prove it looks right, so actually look at the frames.

Then run `/format-check` on a draft render for each platform you're delivering and fix what it reports before showing the creator.

## Gate 3 — Preview approval

Start the preview with `npx hyperframes preview --background` (verify with `--status`), tell the creator they can watch and tweak it there, or in the HyperFrames desktop app. In a cloud session where the creator can't reach a local preview, render a fast draft (`npx hyperframes render --quality draft -o renders/<slug>-draft.mp4`) and send it instead.

Ask for changes in plain language ("move the B-roll at 1:20 two seconds earlier"). Log each request in STATUS.md's change list, apply, re-check, re-preview. Render the final file only after explicit approval:

`npx hyperframes render -o videos/<slug>/renders/<slug>-16x9.mp4`

## Step 5 — Shorts (9:16)

For each Short in the SPEC: scaffold `videos/<slug>/shorts/short-<n>/` with `--resolution portrait`, reuse the CUTS.md segments for its in/out range, and use the **9:16 variants** of the kit (captions higher than the bottom ~20% where platform UI sits, bigger type, hook card in the first 1–2 s). Reframe 16:9 footage by cropping to the speaker, not letterboxing. Same check → review → preview loop; each Short gets its own Gate 3 tick. Render to `videos/<slug>/renders/<slug>-short-<n>-9x16.mp4`.

## Finish

Tick the gates in STATUS.md, commit everything except footage and renders (`edit(<slug>): long-form approved`), and send the final MP4s to the creator. Tell them `/video-post` is next.
