#!/usr/bin/env python3
"""List every piece of on-screen text in a HyperFrames project, and flag placeholders.

Usage: python3 onscreen_text.py <project_dir>

Reads index.html and compositions/**/*.html, drops <script>/<style>, and prints JSON:
the visible text blocks per file (in document order, caption words joined into lines)
and any placeholder-looking text. Also lists audio files in assets/ so licences can be
checked against CREDITS files.
"""
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path

PLACEHOLDER = re.compile(r"\b(sample|placeholder|lorem|ipsum|todo|tbd|xxx|your (talking head|name|logo) here)\b|<add|\[add", re.I)
BLOCK_TAGS = {"div", "p", "h1", "h2", "h3", "h4", "li", "section", "td", "th", "figcaption", "br"}


class TextGrab(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.blocks, self.cur = [], []

    def flush(self):
        text = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        if text:
            self.blocks.append(text)
        self.cur = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in BLOCK_TAGS:
            self.flush()
        else:
            self.cur.append(" ")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        elif tag in BLOCK_TAGS:
            self.flush()
        else:
            self.cur.append(" ")

    def handle_data(self, data):
        if not self.skip:
            self.cur.append(data)


def main():
    root = Path(sys.argv[1])
    files = [root / "index.html"] + sorted((root / "compositions").rglob("*.html")) if (root / "compositions").exists() else [root / "index.html"]
    out = {"files": {}, "placeholders": [], "audio_assets": []}
    for f in files:
        if not f.exists():
            continue
        g = TextGrab()
        g.feed(f.read_text(encoding="utf-8"))
        g.flush()
        rel = str(f.relative_to(root))
        out["files"][rel] = g.blocks
        for b in g.blocks:
            if PLACEHOLDER.search(b):
                out["placeholders"].append({"file": rel, "text": b})
    for a in sorted((root / "assets").rglob("*")) if (root / "assets").exists() else []:
        if a.suffix.lower() in (".mp3", ".wav", ".m4a", ".aac", ".ogg"):
            credits = [c.name for c in a.parent.glob("CREDITS*")]
            out["audio_assets"].append({"file": str(a.relative_to(root)), "credits_file_beside_it": credits})
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
