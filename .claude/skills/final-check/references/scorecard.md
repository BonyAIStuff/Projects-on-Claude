# Scorecard

## Areas and points (total 100)

| Area | Points | Full marks when |
|---|---|---|
| Facts & sources | 25 | Every claim matches a source the creator supplied or you verified; article shots show publication + date |
| Text & spelling | 15 | No spelling/grammar errors; consistent names, terms and number formats; captions match speech |
| Hook & CTA | 10 | Hook (spoken + on-screen) in the first 3 s; readable CTA at the end |
| Technical | 15 | No black/frozen frames, gaps, clipping, sync drift or placeholders |
| Copyright | 15 | Every music/SFX/footage/image asset has a known licence that allows commercial use; news used as commentary |
| Claims about companies | 15 | Statements are factual and attributed, opinions framed as opinions, no investment advice |
| Platform policy | 5 | Title/thumbnail honest; paid-promotion and AI disclosures where needed |

Deduct per finding: **critical** = the area scores 0; **major** = −50% of the area; **minor** = −2 points each (an area never goes below 0).

## What counts as critical (any one → NOT YET)
- A wrong or unsourced number, quote or headline presented as fact.
- A placeholder or "SAMPLE" label still in the video.
- Black/frozen frames or audio gaps on the talking head; audio out of sync.
- An asset with no licence, a licence that forbids commercial use, or copyrighted music.
- A statement that accuses a named company or person of wrongdoing without a source, or tells viewers to buy/sell a security.
- A paid promotion without disclosure.
- No CTA, or no hook in the first 3 s.

## Verdict
- **READY TO POST**: score ≥ 85 and no critical findings.
- **NOT YET**: any critical finding, or score < 85.
UNVERIFIED claims count as critical until the creator supplies the source.

## Report template (FINAL-CHECK.md)

```markdown
# Final check — <slug> — <date>

## Verdict: READY TO POST | NOT YET — <score>/100
Blocking: <one line per critical item, or "none">

| Area | Score | Notes |
|---|---|---|
| Facts & sources | 25/25 | |
| Text & spelling | 13/15 | 1 typo |
| Hook & CTA | 10/10 | |
| Technical | 15/15 | |
| Copyright | 15/15 | |
| Claims about companies | 15/15 | |
| Platform policy | 5/5 | |
| **Total** | **98/100** | |

## Findings
### <Area>
- [critical|major|minor] <what> — <where, timestamp> — Fix: <how>

## Claims table
| # | Claim (as said/shown) | Time | Source given | Verified? | Matches? |
|---|---|---|---|---|---|

## Overrides
<date — what the creator chose to post anyway, and why>
```
