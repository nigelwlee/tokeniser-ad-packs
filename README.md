# Tokeniser ad packs — A/B test

Public review site for the tokenisation campaign ad tiles.

- **Pack A · Waiting Is the Risk** — emotional / consequences angle (12 tiles)
- **Pack B · Your fund with super powers** — functional / capabilities angle (12 tiles)

## Layout
- `index.html` — the whole site. All copy lives in the `PACKS` array at the bottom; edit `theme_line`, `headline`, `primary_text`, `cta` there and push.
- `tiles/a`, `tiles/b` — original full-resolution PNGs (download targets).
- `preview/` — 1080px WebP previews used on the page.
- `source/` — Alison's original single-file packs (base64 embedded).
- `scripts/extract_tiles.py` — regenerates `tiles/` and `preview/` from `source/`.

Static site, no build step. Deployed on Vercel from `main`.
