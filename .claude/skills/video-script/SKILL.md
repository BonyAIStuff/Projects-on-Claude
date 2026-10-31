---
name: video-script
description: Research a topic and write the channel's YouTube explainer script in its fixed six-part structure — cold open with the result, a specific intriguing question, why it matters to you, the concept in 3–4 analogy-led animated chapters (each with a sourced stat, a viewer objection answered and a fun-fact re-hook), impact on the viewer, "spot it yourself", and a debatable A/B poll question — with every visual cue marked (news article highlights, animations, B-roll, stat cards, annotations, SFX) and 3–5 moments tagged to cut as Reels later. Use this whenever the user has a topic, research, a news story or an idea and wants a script, hook lines, statistics, research, "what should I say", or says "new video" — even if they don't say "script".
---

# Video script

The creator explains business and marketing strategies in simple, animated explainers for YouTube; Reels are cut from the finished video later. Every video follows the same construct so the audience learns the rhythm and the creator never starts from a blank page, like a TV show whose segments viewers know by heart, while the content changes every episode.

The structure is in `references/structure.md`, the script template in `references/script-template.md`, hook and question formulas in `references/hooks.md`. Read all three before writing. The look and sound of every cue come from `video-channel/STYLE.md`.

## Why the structure is ordered this way

Viewers decide fast: YouTube tracks how many are still watching at 30 seconds, Instagram how many skip in the first 3. So the result and a specific question come first, and "why this matters to you" lands within 15 seconds. Long-form retention falls steadily with length, so nothing is a block of the same thing: stats sit inside the chapter they prove, viewer questions are answered as objections where they arise, and fun facts re-hook attention between chapters. The ending asks a question people want to argue about, because comments are the cheapest engagement there is.

## Step 1 — Brief (one round of questions)

Ask only what you can't infer from what the creator gave you:
- the topic and the one thing a viewer should understand by the end;
- the creator's own research, links, screenshots and opinion (their take is the point of the video);
- target length (default 8–10 minutes ≈ 1,200–1,500 spoken words at ~150 words a minute);
- the audience's country (default: India when the topic is Indian; use ₹ and Indian examples).

Create `video-channel/videos/<YYYY-MM-DD>-<slug>/` and its `STATUS.md` (template in `/video-plan`'s `references/status-template.md`) if they don't exist.

## Step 2 — Research

Build `RESEARCH.md` from `references/script-template.md` (research section):
- **The result**: the headline event or outcome that opens the video, with the real article(s) that report it (publication, date, headline, link). These become the `[NEWS]` shots, so note the exact lines worth highlighting.
- **Stats**: 6–10 candidates, each with value, what it measures, date, source name and link. Prefer primary sources (regulators and official bodies such as RBI or NPCI, company filings and annual reports, government data), then reputable outlets. Never write a number you didn't read in a source this session; if search isn't available or turns up nothing, list what's needed and ask the creator for sources.
- **Analogies**: 3–5 everyday comparisons for the core concept (a kirana store, a cricket match, a restaurant, a phone plan…). The best analogy maps the mechanism, not just the mood.
- **Viewer objections**: the 3–5 questions a smart sceptic would ask.
- **Fun facts**: 3–5 surprising, sourced facts.
- **Spot-it-yourself examples**: 3–5 other companies or everyday places using the same strategy.

Mark each item SOURCED or NEEDS SOURCE. `/final-check` later checks every claim against this file, so a clean RESEARCH.md now saves a NOT YET verdict later.

## Step 3 — Angles and hooks (Gate 1)

Propose **three angles** (the same topic, three different "why should I care" framings) and for each: 2 hook lines (cold-open line + intriguing question) from `references/hooks.md`, a working title, and 3 debatable closing questions with A/B poll options. Mark your pick and why.

Stop. The creator picks an angle (and may mix hooks). Record the choice in `STATUS.md`.

## Step 4 — Write the script (Gate 2)

Write `SCRIPT.md` from `references/script-template.md`, following `references/structure.md` beat by beat:
- Spoken lines in the creator's voice: short sentences, second person, one idea per line, plain words (explain jargon the first time: "MDR, the fee a shop pays on each payment").
- Under each line, the visual cue(s) in the notation from the template: `[NEWS]`, `[ANIM]`, `[B-ROLL]`, `[STAT]`, `[ANNOTATE]`, `[SLIDE]`, `[SFX]`, `[POLL]`. A cue at least every 10 seconds of speech, so the edit never sits on the talking head for long.
- Every number and quote carries its RESEARCH.md reference, e.g. `(R3)`.
- Tag 3–5 `[REEL n]` moments: 30–60 seconds that make sense alone, open strong and end on a point. Write each one's 2-second hook card text. These are what get cut into Reels after the YouTube edit.
- Finish with the summary block: runtime estimate, word count, chapter list with timestamps, assets the creator must supply (articles to screenshot, B-roll to shoot or find), and anything still NEEDS SOURCE.

Read the script aloud in your head at ~150 words a minute and trim anything that drags. Then stop and show the creator the hook, the chapter list, the Reel picks and the open items. On approval, tick Gate 2 and commit `RESEARCH.md` and `SCRIPT.md`.

## What happens next

`/video-plan` turns the approved script into the shot-by-shot `SPEC.md`; the creator records; `/video-edit` builds it; `/format-check` and `/final-check` gate it; `/video-post` packages it. Reels are cut from the finished YouTube video using the `[REEL n]` tags.
