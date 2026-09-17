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

## Copy
- `COPY-BRIEF.md` — grounding brief: product, ICP, approved proof points with sources, CTA, LinkedIn limits, voice. Mirrored at `.claude/product-marketing.md` for the marketing skills.
- `scripts/copy_data.py` — the copy itself (theme line per sub-theme; headline + intro text per card). Edit here.
- `scripts/fill_copy.py` — writes `copy_data.py` into the `PACKS` array in `index.html`.
- `scripts/check_copy.py` — validates limits (headline ≤70, intro ≤150, theme ≤60), empties and duplicate headlines.
- Copy written with the `ad-creative`, `copywriting` and `ads` skills from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), installed under `.agents/skills/`.
