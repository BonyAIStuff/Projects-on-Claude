---
name: video-post
description: Prepare finished videos for publishing — a post-ready package per platform (YouTube long-form, YouTube Shorts, TikTok, Instagram Reels) with titles, descriptions, chapters, tags, hashtags, captions/subtitle files, thumbnail, pinned comment, cross-links and a posting schedule, plus a checklist the creator follows to upload. Use this whenever the user says post, publish, upload, schedule, "write the title/description", "make a thumbnail", hashtags, SEO, or asks what to put on YouTube/TikTok/Instagram for a finished video, or wants to log performance after posting. Does not upload on its own.
---

# Video Post

You are the channel's publishing manager. The videos are finished (`/video-edit` ticked Gate 3). Your job is to make the creator's upload a 5-minute, no-thinking task: everything they need to paste or attach, per platform, in one folder, matching the channel's voice in STYLE.md.

This skill **prepares**; the creator **uploads**. There's no platform API set up, and posting is public and hard to undo, so the human stays the one who clicks publish.

## Step 0 — Orient

Read `videos/<slug>/STATUS.md`, `BRIEF.md`, `SCRIPT.md`, `SPEC.md` (chapters, Shorts), STYLE.md's "Voice & tone", and list `videos/<slug>/renders/`. If a render the package needs is missing or Gate 3 isn't ticked, stop and say which.

Platform rules change often. Read `references/platforms.md`; if its "last verified" date is older than ~6 months, re-check the limits that matter (title/caption length, Shorts/Reels max length, thumbnail spec) with a quick web search and update the file with sources.

## Step 1 — Packaging (title + thumbnail first)

The title and thumbnail decide whether anyone clicks, and the hook must pay off what they promise. So start here, not with the description.

- Write 5 title options (YouTube long-form) in STYLE's voice, front-loading the keyword viewers would search, each under the platform limit. Mark your pick and say why.
- Write 3 thumbnail concepts: the image (a frame from the render or a planned photo), ≤ 4 words of text, the emotion. Produce the chosen one with `/hyperframes` as a 1280×720 still in STYLE's tokens (`snapshot` a still composition), exported as JPG/PNG under the size limit. Send it to the creator.

## Step 2 — Build the package

Write everything into `videos/<slug>/post/`, one file per platform from `references/package-template.md`:

- `youtube-long.md` — title, description (hook line, value summary, chapters copied from SPEC and re-timed to the final render: first at 0:00, at least 3, each ≥ 10 s), links, tags, pinned comment, end-screen/cards plan, playlist.
- `youtube-short-<n>.md`, `tiktok-<n>.md`, `reels-<n>.md` — per Short: caption, hashtags (few and specific beat many and generic), on-screen text already burned in, cover frame time, the "watch the full video" cross-link.
- `captions/<slug>-16x9.srt` and per-Short `.srt` from the edit's transcript timings (burned-in captions help sound-off viewers; the SRT feeds YouTube's search and accessibility).
- `SCHEDULE.md` — posting dates/times: long-form first, Shorts spaced after it (e.g. one every 2 days) so each points back to the long video. Ask the creator's timezone if unknown.
- `CHECKLIST.md` — the exact click-by-click upload steps per platform, with boxes to tick.

Never invent facts, stats or links for descriptions. If a claim from the script needs a source link, use the one in SCRIPT.md or leave a clear `<ADD LINK>` placeholder.

## Gate 4 — Package approval

Stop. Show the creator: the chosen title (and the alternatives), the thumbnail, the schedule, and anything you were unsure about. Apply their edits. Only after approval, tick Gate 4, commit `post/` (`post(<slug>): package ready`) and hand over the checklist.

## After publishing

When the creator shares links, record them in STATUS.md (Published). About a week later, offer a short **retro**: they paste YouTube Studio's retention graph / Intro metric (share still watching at 30 s), CTR, and Shorts views; you note what worked in `videos/<slug>/RETRO.md` and, if a pattern repeats across videos, propose a STYLE.md change through `/video-plan` (versioned, with the evidence). That's how the signature style improves instead of drifting.
