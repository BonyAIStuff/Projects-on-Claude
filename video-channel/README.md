# my-videos — HyperFrames video editing workspace

Edit real footage (trim, captions, titles, lower-thirds, music, overlays) by describing the
video as HTML and rendering it to MP4 with [HyperFrames](https://github.com/heygen-com/hyperframes).

## Requirements
Node.js 22+ and FFmpeg.

## How to edit a video
1. Drop source clips in `footage/` (or `assets/`).
2. Ask Claude Code, e.g.:
   > Using /hyperframes, take footage/interview.mp4, cut 0:12–0:47, add burned-in captions,
   > a lower-third with my name, and background music. Make it vertical 9:16.
3. Claude edits `index.html`, runs `npm run check`, and renders to `renders/`.

## Commands
```bash
npm run dev       # live preview in the browser (Studio)
npm run check     # lint + runtime + layout checks
npm run render    # render to MP4  (or: npx hyperframes render -o renders/out.mp4)
```

Start a project from a clip, keeping its shape and auto-transcribing for captions:
```bash
npx hyperframes init my-edit --video path/to/clip.mp4 --non-interactive
```
Formats: `--resolution landscape | portrait | square` (16:9, 9:16, 1:1).

## Notes
- GSAP is vendored in `assets/vendor/gsap.min.js` so renders work offline/behind proxies.
- HyperFrames skills are checked into `.claude/skills/` so any Claude Code session in this repo
  has them. Refresh with `npx hyperframes skills update`.
- `index.html` is a smoke test: trims `assets/sample.mp4` (seconds 2–7) and adds a lower-third.
