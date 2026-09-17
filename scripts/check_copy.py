#!/usr/bin/env python3
"""Validate copy in index.html against the LinkedIn limits in COPY-BRIEF.md."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
LIM = {"headline": 70, "primary_text": 150, "theme_line": 60}
problems = []; heads = {}; rows = []
for m in re.finditer(r'\{ label: ("[^"]*"), theme_line: ("[^"]*")', html):
    label, theme = json.loads(m.group(1)), json.loads(m.group(2))
    rows.append(("THEME", label, len(theme), theme))
    if not theme: problems.append(f"empty theme_line: {label}")
    elif len(theme) > LIM["theme_line"]: problems.append(f"theme_line over {LIM['theme_line']}: {label} ({len(theme)})")
for m in re.finditer(r'\{ file: ("[^"]*"), on_tile: "[^"]*", support: "[^"]*", headline: ("[^"]*"), primary_text: ("[^"]*"), cta: ("[^"]*")', html):
    f, h, p, c = (json.loads(g) for g in m.groups())
    rows.append((f, "headline", len(h), h)); rows.append((f, "primary", len(p), p))
    for k, v in (("headline", h), ("primary_text", p), ("cta", c)):
        if not v: problems.append(f"empty {k}: {f}")
        elif k in LIM and len(v) > LIM[k]: problems.append(f"{k} over {LIM[k]}: {f} ({len(v)})")
    if h in heads: problems.append(f"duplicate headline: {f} == {heads[h]}")
    heads[h] = f
for r in rows: print(f"{r[0]:<28} {r[1]:<28} {r[2]:>3}  {r[3]}")
print(f"\n{len(rows)} fields checked, {len(problems)} problems")
for p in problems: print(" -", p)
sys.exit(1 if problems else 0)
