#!/usr/bin/env python3
"""Write copy from scripts/copy_data.py into the PACKS array in index.html (in place)."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import copy_data as cd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "index.html"); html = open(path, encoding="utf-8").read()
data = {"a": cd.A, "b": cd.B}
def js(s): return json.dumps(s, ensure_ascii=False)
def fill(m):
    pack = m.group(1); return m.group(0)  # unused
n = 0
# theme lines: match `{ label: "X", theme_line: "...", cards: [` inside each pack id
for pid, sections in data.items():
    for label, (theme, cards) in sections.items():
        pat = re.compile(r'(\{ label: ' + re.escape(js(label)) + r', theme_line: )"[^"]*"')
        html, k = pat.subn(lambda m: m.group(1) + js(theme), html); assert k == 1, (pid, label, k); n += k
        for file, (headline, primary) in cards.items():
            pat = re.compile(r'(\{ file: ' + re.escape(js(file)) + r', on_tile: "[^"]*", support: "[^"]*", headline: )"[^"]*"(, primary_text: )"[^"]*"(, cta: )"[^"]*"')
            html, k = pat.subn(lambda m: m.group(1) + js(headline) + m.group(2) + js(primary) + m.group(3) + js(cd.CTA), html)
            assert k == 1, (pid, file, k); n += k
open(path, "w", encoding="utf-8").write(html); print("filled", n, "entries")
