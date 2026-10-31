---
name: video-post
description: Prepare finished videos for publishing in the channel's copy style — bold, dramatic-but-honest YouTube titles, thumbnails, descriptions with chapters, Instagram Reels captions, hashtags, pinned comment, the recurring CTAs (vote A/B, follow/subscribe, save/share, full video on YouTube), subtitle files, a posting schedule and an upload checklist, per platform (YouTube long-form, Instagram Reels, YouTube Shorts). Use this whenever the user says post, publish, upload, schedule, caption, title, "write the description", thumbnail, hashtags, CTA, pinned comment, SEO, or asks what to write on YouTube/Instagram for a finished video, or wants to log performance after posting. Does not upload on its own.
---

# Video Post

You are the channel's publishing manager. The videos are finished (`/video-edit` ticked Gate 3). Your job is to make the creator's upload a 5-minute, no-thinking task: everything they need to paste or attach, per platform, in one folder, matching the channel's voice in STYLE.md.

This skill **prepares**; the creator **uploads**. There's no platform API set up, and posting is public and hard to undo, so the human stays the one who clicks publish.

## Step 0 — Orient

Read `videos/<slug>/STATUS.md`, `BRIEF.md`, `SCRIPT.md`, `SPEC.md` (chapters, Shorts), STYLE.md's "Voice & tone", and list `videos/<slug>/renders/`. If a render the package needs is missing or Gate 3 isn't ticked, stop and say which.

**Final-check gate.** If `STATUS.md` doesn't show `Final check — READY`, don't build the package: run `/final-check` (or tell the creator what it's blocking on). Only proceed past a NOT YET when the creator explicitly overrides; record the override and the unresolved items in STATUS.md.

**Copy style.** Read `references/copy-style.md` before writing a word: it sets the language, title style, caption formulas, CTAs, emoji and hashtag rules for every post.

Platform rules change often. Read `references/platforms.md`; if its "last verified" date is older than ~6 months, re-check the limits that matter (title/caption length, Shorts/Reels max length, thumbnail spec) with a quick web search and update the file with sources.

## Step 1 — Packaging (title + thumbnail first)

The title and thumbnail decide whether anyone clicks, and the hook must pay off what they promise. So start here, not with the description.

- Write 5 title options (YouTube long-form) with the title formulas in `references/copy-style.md`: bold and dramatic, front-loading the keyword viewers would search, each under the platform limit, and each one the video actually pays off in its first 30 seconds (`/final-check` fails a title the video doesn't deliver). Mark your pick and say why.
- Write 3 thumbnail concepts: the image (a frame from the render or a planned photo), ≤ 4 words of text, the emotion. Produce the chosen one with `/hyperframes` as a 1280×720 still in STYLE's tokens (`snapshot` a still composition), exported as JPG/PNG under the size limit. Send it to the creator.

## Step 2 — Build the package

Write everything into `videos/<slug>/post/`, one file per platform from `references/package-template.md`, in the copy style:

- `youtube-long.md` — title, description (YouTube description formula: hook line, the poll question, value summary, chapters re-timed to the final render: first at 0:00, at least 3, each ≥ 10 s, sources with links, CTAs), tags, pinned comment (the A/B poll), end-screen/cards plan, playlist.
- `reels-<n>.md` and `youtube-short-<n>.md` — one per Reel cut from the `[REEL n]` tags: caption (Reels formula in `references/copy-style.md`), 3–5 hashtags, cover frame time and cover text, the CTAs, the "full video on YouTube" cross-link. TikTok only if the creator asks.
- `captions/<slug>-16x9.srt` and per-Short `.srt` from the edit's transcript timings (burned-in captions help sound-off viewers; the SRT feeds YouTube's search and accessibility).
- `SCHEDULE.md` — posting dates/times: long-form first, Shorts spaced after it (e.g. one every 2 days) so each points back to the long video. Ask the creator's timezone if unknown.
- `CHECKLIST.md` — the exact click-by-click upload steps per platform, with boxes to tick.

Never invent facts, stats or links for descriptions. If a claim from the script needs a source link, use the one in SCRIPT.md or leave a clear `<ADD LINK>` placeholder.

## Gate 4 — Package approval

Stop. Show the creator: the chosen title (and the alternatives), the thumbnail, the schedule, and anything you were unsure about. Apply their edits. Only after approval, tick Gate 4, commit `post/` (`post(<slug>): package ready`) and hand over the checklist.

## After publishing

When the creator shares links, record them in STATUS.md (Published). About a week later, offer a short **retro**: they paste YouTube Studio's retention graph / Intro metric (share still watching at 30 s), CTR, and Shorts views; you note what worked in `videos/<slug>/RETRO.md` and, if a pattern repeats across videos, propose a STYLE.md change through `/video-plan` (versioned, with the evidence). That's how the signature style improves instead of drifting.
