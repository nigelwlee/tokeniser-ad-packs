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

## Rules for review edits
- **Changing text baked into an existing tile image** (on-tile headline, support line, kicker): set `on_tile` / `support` to the new wording **and** add `tile_fix: { field, from, to }` to that card in `PACKS`. The page shows an amber "IMAGE UPDATE NEEDED" badge on the tile and an "IMAGE FIX" row with old → new wording, so the designer can re-export the PNG. Remove `tile_fix` once the new image is in `tiles/` and `preview/` is regenerated.
- **New concept with no image yet**: add the card with `placeholder: true`; the page renders a slate frame with the intended on-tile lines and an "IMAGE TO COME" tag.
- **Headline / intro / CTA edits**: change `scripts/copy_data.py`, run `fill_copy.py` then `check_copy.py`, push.

## Ad layout guide
Lives on the site (collapsible section under the copy spec). Four elements, one left-aligned column, 8% safe margin: (1) short mint accent bar, (2) headline in sentence case with the closing phrase in mint, ≤8 words, (3) support line ≤6 words, (4) footer row with the sign-off left and the tokeniser wordmark right on one baseline. Nothing else on the tile. Pack A already follows it; every Pack B tile carries a `tile_fix` with a punchy support line and `layout: true`.
- **No blockchain or crypto concepts in any copy** (token as a noun, protocol, atomic, chain, ledger, smart contract, wallet, custody, digital asset, web3…). Tokenise/tokenisation is fine. `scripts/check_copy.py` fails on any hit.
