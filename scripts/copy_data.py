# Copy for the Tokeniser A/B ad packs. Edit here, then run scripts/fill_copy.py.
CTA = "Request demo → info-redbelly.zohobookings.com.au/demo"

A = {
  "The thesis": ("The risk was never the technology. It was the delay.", {
    "01_investors_ryoji.png": (
      "Give your investors 24/7 liquidity before someone else does.",
      "Investors now expect 24/7 liquidity and T+0 settlement. 160+ funds and companies already offer it on Tokeniser. See what it takes for yours."),
    "01b_get_ahead.png": (
      "Offer 24/7 liquidity and T+0 settlement before they ask for it.",
      "Investor expectations are moving fast. Funds on Tokeniser already offer 24/7 liquidity and T+0 settlement. Get yours ahead of the curve."),
  }),
  "The proof — they waited": ("Every industry has one. Finance’s is now.", {
    "02_kodak_moment.png": (
      "160+ funds and companies have already tokenised. Yours can too.",
      "Tokenisation is inevitable. Global funds are moving fast with investor expectations moving faster. Tokeniser can get your fund ready."),
    "03_kodak_waiting.png": (
      "The technology is proven. The only variable left is when you move.",
      "Tokeniser is proven and ready: 160+ funds and companies, A$2B+ transacted, T+0 settlement, 24/7 liquidity, locally compliant. It’s your move."),
    "04_blackberry_waiting.png": (
      "Your investors are moving to funds that settle in minutes, not days.",
      "The fund next door already offers T+0 settlement and 24/7 liquidity. See what tokenising yours involves."),
    "04b_blackberry_chose.png": (
      "Waiting felt safe right up until it wasn’t.",
      "Tokeniser is proven and ready: 160+ funds and companies, A$2B+ transacted. It’s your move."),
    "05_blackberry_stood.png": (
      "Learn from history and tokenise today.",
      "You don’t need to rebuild anything. Tokeniser runs alongside your existing infrastructure, under your existing licence. Book a demo."),
  }),
  "The proof — they moved": ("First movers don’t compete. They set the terms.", {
    "11_uber_replaced.png": (
      "Tokenised funds are replacing the T+2 model. 160+ have already moved.",
      "Instant settlement. 24/7 secondary liquidity. Investors who can borrow against holdings. This is the fund yours will be compared to. Book a demo."),
    "12_airbnb_replaced.png": (
      "Reach investors beyond your channels, without leaving your stack.",
      "Airbnb won on access. Tokenisation gives your fund the same edge: a global investor base, local compliance, T+0 settlement. See it in a demo."),
    "12b_airbnb_new_offering.png": (
      "Give investors a new way in: tokenised units, 24/7 liquidity, T+0.",
      "Airbnb didn’t take rooms from hotels. It offered what they couldn’t. Tokenisation does the same for your fund: new investors, new liquidity."),
  }),
  "Variations": ("Be the case study they copy, not the one they cite.", {
    "06_next_kodak.png": (
      "Equip your fund with the modern solution.",
      "The funds that tokenised early now offer T+0 settlement and 24/7 liquidity as standard. Find out what the move looks like for yours. Book a demo."),
    "07_case_study.png": (
      "Tokenisation is finance’s Kodak moment. Be on the winning side.",
      "Every industry gets one moment where the winners are decided. 160+ funds and companies have already made their move with Tokeniser. Make yours."),
    "08_chose_film.png": (
      "Your fund can tokenise at its own pace, under its own licence.",
      "Onboarding happens in stages, at your pace. No rip-and-replace, no new licence. Choose the future without betting the fund on it. Book a demo."),
    "09_first_movers.png": (
      "Tokenisation takes your fund to the frontier.",
      "The rules are being written now: T+0 settlement, 24/7 liquidity, global investors, local compliance. 160+ funds and companies are there. Join them."),
    "10_dont_develop.png": (
      "See what tokenising your fund actually involves.",
      "One platform from issuance to settlement. Your team keeps familiar registry operations. A$2B+ transacted already. Book a demo and see it live."),
  }),
}

B = {
  "Instant settlement": ("Settle the moment the trade is struck.", {
    "capability_tile_01.png": (
      "T+0 settlement for your fund, on infrastructure 160+ already use.",
      "Two days of settlement risk, gone. Tokenised units settle atomically, the moment a trade is struck. See T+0 on your asset class. Book a demo."),
    "capability_tile_02.png": (
      "Free two days of capital on every trade. Investors notice.",
      "Every T+2 trade parks investor capital for two days. On Tokeniser it works from minute one. A$2B+ transacted this way. Request a demo."),
  }),
  "Collateral mobility": ("Holdings that work as collateral, in minutes.", {
    "capability_tile_03.png": (
      "Let investors borrow against their fund units without redeeming.",
      "Collateralised lending, built into the platform. Investors unlock liquidity while staying invested. New revenue for the fund. Book a demo."),
    "capability_tile_04.png": (
      "Post fund holdings as collateral in minutes, not settlement cycles.",
      "Tokenised units move and settle instantly, so collateral moves too. Give investors and counterparties the speed they expect. See it in a demo."),
  }),
  "Secondary transfer": ("Liquidity without waiting for the redemption window.", {
    "capability_tile_05.png": (
      "24/7 secondary liquidity for a private fund. Compliant, on-platform.",
      "Positions transfer between eligible holders any day, not just at the window. Compliance rules run on every trade. Book a demo to see it."),
    "capability_tile_06.png": (
      "Give investors an exit without touching the fund’s capital.",
      "Redemptions drain the fund. Secondary transfers don’t. Let eligible investors trade positions between themselves, with a full audit trail."),
  }),
  "Real-time transparency": ("The register is the source of truth, live.", {
    "capability_tile_07.png": (
      "One investor portal: live holdings, statements and tax reports.",
      "Your investors see holdings, statements and tax reports the moment they change, in your branded portal. Fewer calls, more trust. Book a demo."),
    "capability_tile_08.png": (
      "Retire the spreadsheet. The register updates itself, every trade.",
      "Registry, cap table, distributions and corporate actions on one platform, updated as trades settle. 23% lower operating costs. Book a demo."),
  }),
  "Automated compliance": ("Compliance you don’t have to remember.", {
    "capability_tile_09.png": (
      "Eligibility and transfer rules enforced on every trade, automatically.",
      "Whitelisting, holder limits and transfer restrictions live in the token. Every trade checks itself. Built for AFSL and MAS frameworks. Book a demo."),
    "capability_tile_10.png": (
      "Locally compliant, programmed into the asset. Not bolted on.",
      "Built for Australia’s digital asset laws, with compliance programmed into the protocol. Your licence, your rules, enforced every time. Book a demo."),
  }),
  "Always-on": ("No market hours. No cut-offs. No waiting.", {
    "capability_tile_11.png": (
      "Investors view, transfer and settle any hour, from any device.",
      "No cut-off times, no waiting for Monday. Your fund runs on infrastructure that never closes, with compliance on every trade. Book a demo."),
    "capability_tile_12.png": (
      "Give your Australian fund a global edge: open when your investors are.",
      "Investors in other time zones shouldn’t wait for Sydney to open. 24/7 settlement and liquidity, locally compliant. See it in a demo."),
  }),
}
