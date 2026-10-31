# Style discovery

Goal: turn the creator's taste into a `STYLE.md` that another editor could follow without asking a single question. Taste is vague; rules must be numbers.

## 1. Collect taste (one round of questions)

- 3–5 creators or specific videos they love, and *what exactly* they love (pace? captions? colour? humour?).
- 2–3 they dislike and why. Dislikes are often sharper than likes.
- Three personality words for the channel (e.g. "calm, sharp, premium").
- Any fixed assets: name, logo, a colour they already use, a font they like.

If they share links, look at them (titles, thumbnails, descriptions, any transcripts you can reach). Don't claim to have watched what you couldn't open.

## 2. Translate words into rules

For each personality word, write 2–4 measurable rules. Examples:

| Word | Rules |
|---|---|
| Sharp | cut or punch-in at least every 4 s of talking head; transitions ≤ 200 ms; no cross-dissolves |
| Calm | music −24 LUFS under voice; captions fade, never bounce; holds of 1.5 s on key lines |
| Premium | one accent colour only; generous margins (title-safe 80%); no stock-looking emoji or stickers |
| Energetic | word-by-word captions with an active-word highlight; whoosh SFX on graphics in; 2–3 s B-roll |

Pick three directions that interpret the words differently (e.g. "editorial minimal", "bold creator", "documentary warm"). HyperFrames ships ready `frame.md` design templates (see the HyperFrames README's Frame.md section and https://www.hyperframes.dev/design/) — starting one direction from a template is fine.

## 3. Render three style tests

Use `/hyperframes` (and `/hyperframes-registry` for captions, lower-thirds, transitions). Use the **same** 10–15 s clip for all three — the creator's own talking-head footage if available, otherwise a stand-in — so only the style differs. Each test shows: the hook title card, captions, a lower-third, one B-roll cut-in, one emphasis zoom, and the music bed. Render to `style-tests/<direction>.mp4` (16:9) plus one 9:16 frame grab for each, so the vertical version is judged too.

## 4. Write STYLE.md

Fill `style-template.md` for the chosen direction (or mix). Every field gets a value; write "n/a" deliberately rather than leaving blanks. Then build the reusable pieces it names under `compositions/components/` (both 16:9 and 9:16 variants), and render a 30 s **style reel** that uses each piece once: it becomes the visual reference that later edits are compared against (`style-tests/style-reel.mp4`).

## 5. Evolve deliberately

The style should improve from evidence (retention graphs, comments, the creator's own taste shifting), not drift by accident. Each change: bump `Version`, add a changelog line with the reason, re-render the style reel.
