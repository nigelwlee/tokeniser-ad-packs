#!/usr/bin/env python3
"""Extract the base64 PNG tiles from the two source pack HTML files into tiles/,
then build 1080px WebP previews in preview/ (needs cwebp on PATH)."""
import base64, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = {
    "a": "source/pack-a-tokenisation-campaign-visuals.html",
    "b": "source/pack-b-capabilities-campaign-refresh.html",
}
PAT = re.compile(r'download="([^"]+)"[^>]*href="data:image/png;base64,([^"]+)"|href="data:image/png;base64,([^"]+)"[^>]*download="([^"]+)"')
for pack, rel in SOURCES.items():
    html = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    n = 0
    for m in PAT.finditer(html):
        name = m.group(1) or m.group(4); data = m.group(2) or m.group(3)
        png = os.path.join(ROOT, "tiles", pack, name)
        open(png, "wb").write(base64.b64decode(data))
        webp = os.path.join(ROOT, "preview", pack, os.path.splitext(name)[0] + ".webp")
        subprocess.run(["cwebp", "-quiet", "-q", "82", "-resize", "1080", "1080", png, "-o", webp], check=True)
        n += 1
    print(f"pack {pack}: {n} tiles")
