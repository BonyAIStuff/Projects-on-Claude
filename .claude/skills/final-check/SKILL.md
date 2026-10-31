---
name: final-check
description: The last gate before a video is posted — a scored review (out of 100) of facts and sources, on-screen text and spelling, hook and CTA, technical glitches, copyright, claims about companies, and platform policy, ending in READY TO POST or NOT YET. NOT YET blocks /video-post until fixed or the creator explicitly overrides. Use this whenever a video is finished or about to be posted, or the user says final check, "is it ready to post", "check facts", "check spelling", "any copyright issues", "can I say this about <company>" — even if they don't name the skill. Run it after /format-check and before /video-post.
---

# Final check

The creator explains business and marketing strategy using real companies, real numbers and real news articles. That's what makes the videos credible, and it's also where a single wrong number, a misquoted headline or an unlicensed track can cost trust, a strike or a legal letter. This check is the editor-in-chief's read before publishing: slow, sceptical, and honest about what it couldn't verify.

Scoring and verdict rules: `references/scorecard.md`. Copyright, company claims and platform policy: `references/risk-guide.md`. Read both every time.

## Step 1 — Gather

In `video-channel/videos/<slug>/`: the renders, the project(s) (`edit/`, `shorts/*/`), `SCRIPT.md` / `SPEC.md` if they exist, any transcript, the article screenshots and source links the creator supplied, `checks/FORMAT-CHECK.md`. If the format check hasn't been run on these renders, run `/format-check` first; a final check on a video that may still change is wasted.

## Step 2 — Run the scripts

From the repo root:

```bash
python3 .claude/skills/final-check/scripts/glitches.py <render.mp4> --speech-until <seconds where speech ends>
python3 .claude/skills/final-check/scripts/onscreen_text.py <project_dir>
```

`glitches.py`: black frames, frozen picture, audio gaps during speech, clipping, audio/video length mismatch. A frozen stretch on a deliberate graphic hold is fine; on the talking head it's a fault.
`onscreen_text.py`: every on-screen text block in order, placeholder text ("sample", "placeholder", "TODO", "<ADD LINK>"…), and every audio file with whether a CREDITS file sits beside it.

## Step 3 — Review each area

Work through the seven areas in `references/scorecard.md`. For each, list findings with the timestamp (snapshot with `npx hyperframes snapshot --at <s>` to confirm) and a concrete fix.

**Facts & sources.** Build a claims table from everything said and shown: every number, date, percentage, quote, headline and statement about what a company did. For each claim record the source the creator gave (publication, date, link) and whether the video matches it exactly. Verify against the source itself when you can reach it; when you can't, mark it **UNVERIFIED** and ask the creator for the link or screenshot. Never fill a gap with a number from memory, and never mark something verified that you didn't check. Article screenshots must show the publication name and date somewhere in the shot or in an on-screen credit.

**Text & spelling.** Spelling and grammar of every block from `onscreen_text.py`; consistent names and terms (UPI, MDR, company names exactly as the company writes them); number formats (₹ before the number, Indian or international digit grouping used consistently, % with no space); captions match the words actually spoken (compare to the transcript when there is one, otherwise listen at the snapshot times).

**Hook & CTA.** Within the first 3 seconds there's a spoken hook and a matching on-screen line that states the tension or payoff. The video ends with a clear CTA (poll, comment, subscribe or follow) that's on screen long enough to read. The YouTube title/thumbnail promise (if already drafted) is paid off in the first 30 seconds.

**Technical.** Script findings, plus: lip-sync looks right at 3–4 spot checks, no leftover placeholders, no element visibly popping or flickering.

**Copyright, claims about companies, platform policy.** Follow `references/risk-guide.md`.

## Step 4 — Score and verdict

Write `videos/<slug>/checks/FINAL-CHECK.md` with the template in `references/scorecard.md`: the verdict line first, the scorecard table, then findings by area with fixes, then the claims table. Show the creator the verdict, the score and the blocking issues in plain words.

## Step 5 — Fix with approval

Ask which fixes to apply. Wording and on-screen changes go in the composition (re-run `/format-check` if layout changed), then re-render and re-run this check. A claim the creator can't source gets reworded to what the source supports, attributed ("according to <publication>"), or cut; that choice is theirs.

## Blocking

Set the gate in `STATUS.md`: `- [x] Final check — READY (score N, <date>)` or `- [ ] Final check — NOT YET (score N): <blocking items>`. `/video-post` won't build a package while it says NOT YET. The creator can override by saying so explicitly ("override final check, post anyway"). Record that in STATUS.md with the date and the unresolved items, and repeat the unresolved risks to them once.
