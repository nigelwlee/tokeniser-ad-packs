# Copy brief — Tokeniser tokenisation campaign (LinkedIn Sponsored Content)

Grounding document for the ad copy in `index.html`. Every claim in the copy must trace to a source listed here.

## Product
Tokeniser (a Redbelly Network project) is the digital asset platform for financial services: origination, administration and servicing infrastructure for tokenised equities, funds, loans and notes. Funds and companies tokenise their assets without a technology project; the team keeps familiar registry operations, one platform handles issuance to settlement. Built for Australia's digital asset laws; products run under the issuer's existing licensing (AFSL, MAS-ready). Non-disruptive: integrates alongside existing infrastructure, no rip-and-replace.
Sources: tokeniser.com homepage and FAQ (fetched 2026-09-17); `tokeniser-b2b-messaging.docx` (B2B Messaging V1).

## Audience (ICP)
Fund managers, fund administrators, company secretaries, heads of operations, COOs and CFOs at private funds, wealth managers and asset issuers. Australia primary; Singapore and Hong Kong secondary. Problem-aware to solution-aware. They live with T+2 settlement, quarterly redemption windows, quarter-end registry reconciliation, spreadsheets and manual compliance.
Source: `tokeniser_ads_to_test.docx` (Ad 1 ICP and targeting).

## Proof points (use only these)
| Claim | Source |
|---|---|
| 160+ companies and funds on the platform | tokeniser.com proof tiles; ads-to-test brief |
| A$2B+ transactions | tokeniser.com proof tiles; ads-to-test brief |
| A$1.2B issued equity and funds | tokeniser.com proof tiles |
| T+0 settlement | tokeniser.com proof tiles |
| −23% operating costs | tokeniser.com proof tiles |
| 24/7 secondary liquidity | tokeniser.com proof tiles and hero |
| Clients: IQ-EQ, JellyC, Holon, EnviroMission | tokeniser.com logo row; B2B messaging doc ("Trusted by IQ EQ") |
| A Redbelly Network project; born from research at the University of Sydney and CSIRO | ads-to-test brief trust signals |
| Locally compliant; eligibility and compliance programmed into the protocol | tokeniser.com hero and FAQ |

Do not use "200+ companies" (older B2B doc; superseded by the site's 160+). No invented statistics, quotes or client names.

## Campaign frame
A/B test of two packs, same audience, same CTA:
- **Pack A — Waiting Is the Risk** (emotional / consequences). Sign-off: "Finance is next. Tokenisation is how."
- **Pack B — Your fund with super powers** (functional / capabilities). Sign-off: "Your fund with super powers". Six capabilities: instant settlement, collateral mobility, secondary transfer, real-time transparency, automated compliance, always-on.
Site hero echoes Pack B: "Tokenising your asset gives investors superpowers: 24/7 liquidity, instant settlement, and more choice, while you stay locally compliant."

## CTA
LinkedIn CTA button: **Request demo**. Destination: https://info-redbelly.zohobookings.com.au/demo (also linked from tokeniser.com/demo). Decision by Nigel, 2026-09-17. The readiness quiz page from the older brief no longer exists.

## Platform spec (LinkedIn single-image Sponsored Content)
| Field | Limit used | Notes |
|---|---|---|
| Intro text (`primary_text`) | ≤150 characters | LinkedIn truncates around 150 in feed; hard cap 600. Hook first, one proof point where it fits, close with the ask. |
| Headline (`headline`) | ≤70 characters | Sits below the image. Must not repeat the headline baked into the tile. |
| CTA (`cta`) | fixed | Request demo → Zoho booking page |
| Theme line (`theme_line`) | ≤60 characters | One line per sub-theme: campaign-cell label, carousel cover or intro for the set. |

## Voice
Tokeniser brand as on the tiles: sentence case, short declaratives, one idea per line, mint-accent payoff. Australian English (tokenise, tokenisation). Professional, not boring; specific job outcomes; no consumer hype, no exclamation marks, **no blockchain or crypto concepts anywhere in the copy**: not "token" as a noun, protocol, atomic, chain, on-chain, ledger, smart contract, wallet, custody, digital asset, web3, decentralised, minting. "Tokenise / tokenisation / tokenised" is the product category and is fine. Say "asset", "transaction", "trade", "unit", "register" instead. Enforced by `scripts/check_copy.py`. Pack A copy stays consequence-led and never re-explains the Kodak/BlackBerry/Uber/Airbnb reference already on the tile. Pack B copy names one concrete capability and what it changes for the fund or its investors.
