# STYLE — Business & marketing explainers

Version: 1.0 — 2026-10-31
Personality: smart, premium, editorial (Vox / The Economist inspired)
One-line summary: Newsprint-calm explainers where a soft highlighter carries the words and a red pen appears only when something really matters.

Reference edit: `videos/2026-10-31-first-edit/` (render: `renders/first-edit-16x9.mp4`). When unsure how something should look, match that edit.

## Colour — "Broadsheet, minimal red"
| Token | Hex | Use |
|---|---|---|
| --ground | #f2eee6 | graphic backgrounds (newsprint white) |
| --ink | #121212 | all text on light backgrounds |
| --second | #55606b | kickers, labels, secondary text |
| --desk | #dcd6ca | surface behind article screenshots |
| --hl | #efe0a6 | highlighter sweep (soft newsprint yellow) |
| --annot | #d23a26 | hand-drawn annotations ONLY |

Red rule: red appears only as hand-drawn ink (circles, arrows, handwritten notes), at most once or twice per scene. Never as a background, caption fill or highlighter.
Footage look: natural (no grade).

## Type — Swiss grotesk
| Role | Font | 16:9 | 9:16 | Weight |
|---|---|---|---|---|
| Captions | Archivo | 78 px | 84 px | 800 |
| Graphic headlines | Archivo | 100–110 px | 96 px | 800 |
| Big numbers | Archivo | 260–300 px | 220 px | 800, tabular |
| Labels / kickers | Archivo | 28–34 px, +0.16em tracking, caps | 32 px | 500 |
| Article body text | Georgia (serif, so articles read as print) | 38 px | 40 px | 400 |

Font files: `assets/fonts/archivo-latin-{500,800}-normal.woff2`. Minimum text size 28 px.

## Captions — word-by-word + highlighter sweep
- Words appear as spoken (fade + 14 px rise, 0.18 s, power3.out).
- White text with soft shadow over footage.
- Highlighter sweep on 1–2 key words per line only (left→right, 0.26 s); the highlighted word turns ink-black.
- Max ~6 words per line, one line on screen; bottom of the title-safe area (bottom 150 px in 16:9; above the bottom 20% in 9:16).
- When a graphic shows the same words (e.g. a big "2020"), hide the caption.

## News articles — spotlight + push-in
- Article on a paper card (#fbfaf7, soft shadow) on the desk colour, masthead in tracked caps.
- Slow push-in toward the lines being read (scale ~1.0→1.3 over the section).
- Active line full opacity; others dimmed to 22%.
- Each line stays on screen ≥ 0.5 s + 0.3 s per word.
- Use real article screenshots/text with source visible; never invent a quote. Mock articles must say "SAMPLE ARTICLE".

## Motion & transitions
- Transition: hard cut + whip (outgoing slides left, incoming slides in from right with 8° skew settling to 0; 0.25–0.45 s, power3).
- Talking head: slow push-in (+5% over a shot); punch-in cut (+10–15%) on an emphasis line.
- Entrances: power3.out 0.18–0.35 s. No bounces, no spins, no glitch effects.

## Signature element — hand-drawn annotations
- Red pen circles, underlines and arrows drawn on (0.4–0.8 s), on numbers, key phrases and CTAs.
- Optional short handwritten-style note in Archivo 800, red.

## B-roll
- Prefer real footage when supplied; otherwise animated B-roll in the palette (phone UI, receipts, charts, big numbers), whipped in over the voice.

## Sound
- Voice: always on top, target −14 LUFS for YouTube.
- Music: pulse and pads (cinematic tension, 90–110 BPM, minor). ~0.28 volume under speech, ~0.6 without speech; fade out last 1.5 s. Real tracks to be chosen; current bed is a placeholder.
- SFX: Pixabay library (free, commercial use, no attribution needed), quiet and sparse, only on visible actions:
  - whip → `whoosh-short` / `whoosh` (0.3–0.45)
  - article lands → `impact-bass-2` (0.2) + soft `typing` under reading (0.18)
  - list / poll items in → `pop` (0.35)
  - annotation drawn → `ping` (0.25)
  - first caption → `click-soft` (0.25)

## Recurring CTA
- Poll card: "WHAT DO YOU THINK?" kicker, headline with one highlighted word, two options (A/B) in outlined boxes, red-pen arrow to "Vote A or B in the comments".

## Formats
- YouTube long-form: 1920×1080, 30 fps.
- Shorts / Reels: 1080×1920, crop to the speaker; same rules, larger captions.

## Don'ts
- No red fills, no extra accent colours, no emoji, no stock-looking stickers, no glitch/RGB effects, no bouncy captions.

## Changelog
- 1.0 — 2026-10-31 — initial style from the style menu picks and the first edit.
