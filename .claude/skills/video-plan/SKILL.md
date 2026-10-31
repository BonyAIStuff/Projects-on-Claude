---
name: video-plan
description: Plan a new video for this channel before anything is edited — define or apply the channel's signature style (STYLE.md), write the brief, propose three storylines, then the script, filming shot list and shot-by-shot SPEC. Use this whenever the user wants to start, plan, outline, script or brainstorm a video, YouTube episode, Short, Reel or TikTok, says "new video", "video idea", "help me script", "what should I film", or wants to create or change their signature/visual/editing style — even if they don't say "plan". Run it before /video-edit for any new video.
---

# Video Plan

You are the producer for a creator's channel: talking-head and B-roll + voiceover videos, published as YouTube long-form (16:9) with Shorts/Reels/TikTok (9:16) cut from them. Your job here is everything *before* the edit: the style, the idea, the story, the script and the blueprint the editor (`/video-edit`) will follow.

The creator wants a **recognisable, consistent signature style**. Consistency comes from writing decisions down once and reusing them, not from remembering. So everything you decide lands in files in the repo, and later stages read those files instead of re-deciding.

## Where things live

```
STYLE.md                         # the channel's style bible (repo root) — one for all videos
videos/<YYYY-MM-DD>-<slug>/
  STATUS.md                      # stage + gate checklist; read it first to resume
  BRIEF.md
  STORYLINES.md
  SCRIPT.md                      # script + filming shot list
  SPEC.md                        # shot-by-shot blueprint for /video-edit
```

Copy `references/status-template.md` to start `STATUS.md`. Update it at every gate so any future session can pick up where this one stopped.

## Step 0 — Orient

1. If the user named an existing video folder, or `videos/` has a folder whose `STATUS.md` isn't finished, read `STATUS.md` and continue from the first unchecked gate. Don't restart work the user already approved.
2. If `STYLE.md` does not exist at the repo root, run **Style discovery** first (below). Every video depends on it; planning a video without it produces a one-off look, the opposite of what the creator wants.
3. If `STYLE.md` exists, read it fully. Everything you write later must be consistent with it.

## Style discovery (first run, or when the user asks to change the style)

Read `references/style-discovery.md` and follow it. In short: collect references and dislikes, turn three personality words into numeric rules, render three short style tests with `/hyperframes` from the same clip so the creator compares looks side by side, then write `STYLE.md` from `references/style-template.md`.

**Gate S — style approval.** Stop and show the three tests (send the MP4s) and the draft `STYLE.md`. Only commit `STYLE.md` once the creator approves. Changing an approved style later is a deliberate act: bump its version line and note what changed and why, so old videos remain explainable.

## Step 1 — Brief

Ask only what you can't infer. A good brief has: topic, target viewer, the one takeaway, the call to action, target length (long-form) and how many Shorts are wanted, footage the creator already has, deadline. Write `BRIEF.md`. Short questions, one round; propose defaults for anything they skip.

## Steps 2–3 — Research, angles and script: use `/video-script`

The channel has a fixed video structure (cold open with the result → intriguing question → why it matters → analogy-led chapters with stats, objections and fun-fact re-hooks → impact → spot it yourself + debatable poll). `/video-script` owns research, hooks and the script, including Gate 1 (angle) and Gate 2 (script). Run it, then come back here for the SPEC.

## Step 4 — SPEC (the blueprint)

Read `references/spec-template.md` and write `SPEC.md`. Turn every adjective into a number and every scene into rows: timestamp, what's on screen (A-roll / B-roll / graphic), the spoken line, the style-kit component used (caption, lower-third, chapter card, zoom), and the sound. Copy the script's `[REEL n]` tags into a Reels table (in/out against the script, hook card text); Reels are cut from the finished YouTube edit, not planned as separate videos.

The SPEC is the contract `/video-edit` builds against. Anything vague here gets guessed in the edit, and guesses drift away from the signature style.

**SPEC approval.** Stop. Show a short summary (runtime, scene count, Shorts planned, anything that needs filming), and link the files. On approval, tick the gate, then tell the creator what to film or upload and that `/video-edit` is next.

## Commit as you go

After each gate is approved, commit the video folder (and STYLE.md when it changes) with a message like `plan(<slug>): storyline approved`. The plan only survives a session ending if it's committed and pushed.
