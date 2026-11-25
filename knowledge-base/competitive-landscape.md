# Competitive Landscape — Seekridge

Full battlecard reference. The summary table in [`knowledge-base.md`](./knowledge-base.md) is the quick version; this is what [`competitor-monitoring`](../sales-tools/competitor-monitoring), [`battlecard`](../sales-tools/battlecard), and [`win-loss-analysis`](./win-loss-analysis) draw on for deeper context.

**Last full refresh:** September 2026, following a [`outdated-checker`](./outdated-checker) sweep against the July–August bi-monthly competitor report and the trailing-12-month win-loss deep dive — see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md) for exactly what changed and why. Per-competitor "Last verified" dates below track individual sections.

## Executive summary

Three real competitors in the bank/lender and insurer segments, none with a decisive product edge — deals are won or lost in the risk conversation, not the demo. Bricklane is the highest-frequency threat (price-led raw property data, no explanations, leaves moment-building to the buyer); ValuAI is the fastest-moving one — its moment-explanation feature shipped in July 2026 and it's now competing on price too, though we're 8-for-8 against it this period (small sample, closing gap, not a reason for confidence); Estemate is fading but still wins on relationship tenure and on-prem support — and still beats us more often than any other named competitor (72.7% win rate for them when faced, per the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)), which is worth remembering before assuming the flashier competitor is the bigger threat. Our two live vulnerabilities are price and the on-prem gap — see [Known gap working against us](#known-gap-working-against-us).

## Company profiles

| Competitor | Founded | Size | Funding | Target market | Core value prop |
|---|---|---|---|---|---|
| Bricklane Data | 2021 | ~80 employees | Series A (~$15M) | Mid-market lenders, EU-wide | Fastest, cheapest property data and valuations via API |
| Estemate | 2005 | ~450 employees | Private, no disclosed VC | Large + regional banks and insurers, France/Benelux | Two decades of trusted property data, now with a "portfolio insights" add-on |
| ValuAI | 2022 | ~120 employees | Series B (~$60M) | Forward-leaning banks and insurers, EU-wide | AI-native propensity scoring built for what's next |
| PropIQ | 2019 | ~40 employees | Bootstrapped/seed | Independent brokerages | Seller leads that help agents win listings |

*(Source: general market knowledge, not independently verified — reconfirm before citing a specific figure to a prospect.)*

## Quick reference — read this before a call

| Competitor | Threat level | Segment | Win angle | Landmine — don't say |
|---|---|---|---|---|
| [Bricklane Data](#bricklane-data) | 🔴 High — most frequent competitor in losses (13 of 35 lost deals, Q1) | Bank/lender | Reframe price → the cost of building and defending moments yourself | Don't price-match — it concedes the frame that this is commodity data |
| [ValuAI](#valuai) | 🟠 Medium-High — shipped moment explanations in Jul 2026; 0-for-8 against us since, but that's a small sample and the gap is closing, not a reason for confidence | Bank/lender, insurer | Ask for proof at scale (named reference, live test on the buyer's own customers) — existence of the feature is no longer the wedge | Don't call it "still in beta" — it shipped; don't assume our current win rate against them will hold |
| [Estemate](#estemate) | 🟠 Medium-High — revised up: wins 72.7% of deals it contests (n=11), despite the least exciting product story of the three | Bank/lender, insurer (Benelux-heavy) | Modern CRM integration + faster implementation, once a frustrated stakeholder is in the room | Don't attack the relationship tenure — it's their strongest card, and it's working better than this document previously credited |
| [PropIQ](#propiq) | ⚪ Low — different segment | Brokerage | N/A — rarely a head-to-head bank/insurer deal | N/A |

## Capability comparison

Illustrative — not a substitute for a live demo comparison.

| | Seekridge | Bricklane Data | Estemate | ValuAI |
|---|---|---|---|---|
| Per-moment evidence trail (property, market and customer data points) | ✅ Yes | ❌ No moments — raw data and a valuation confidence score only | ⚠️ Partial, portfolio-level reports in a dated format | ⚠️ Shipped Jul 2026, but a feature-importance chart rather than named data points, and reportedly weaker where property data matters most (commercial/mixed-use, see [`call-09-ironbridge-bank.md`](./sales-call-analysis/call-09-ironbridge-bank.md)) |
| Combines the client's own CRM data | ✅ Yes | ❌ No — property data only | ⚠️ Batch file upload, no live CRM integration | ✅ Yes |
| Moment-quality method disclosed (backtest on client data) | ✅ Yes | ❌ Not applicable / not published | ✅ Yes, established track record on property data | ❌ Claimed, not disclosed |
| On-prem deployment | ❌ No — current gap, see [win-loss data](./win-loss-analysis/win-loss-infographic.svg) | ❌ Cloud only | ✅ Yes (legacy architecture) | ❌ Cloud only |
| Implementation timeline | Weeks | Fastest — self-serve API (but the buyer builds the moments) | Slowest — legacy integration | Medium |
| Pricing model | Subscription by customer-base size | Usage-based per API call, ~15% below Seekridge on comparable volume | Enterprise/negotiated, typically higher | Not publicly disclosed; averaged ~9% below our deal size in Q3 head-to-heads (n=8, see [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)) |

The on-prem gap is real, not a competitor's weakness — flag it early with a prospect that requires it rather than letting it surface late in the deal.

## Pricing & packaging

| Competitor | Model | Notes |
|---|---|---|
| Seekridge | Subscription priced by customer-base size, seat-based for brokerage app | No self-serve tier for the bank/insurer product — sales-assisted only |
| Bricklane Data | Usage-based per API call, ~15% below Seekridge | Self-serve signup, no enterprise tier disclosed — built for fast adoption without procurement |
| Estemate | Enterprise/negotiated only | Multi-year contracts typical, no self-serve option |
| ValuAI | Not publicly disclosed | Sales-assisted only. The "premium-priced" assumption didn't hold up in Q3 head-to-heads — their average quote came in below our average deal size (see [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)); price is now part of their play, not just capability |
| PropIQ | Seat-based, tiered by team size | Freemium single-seat trial available |

## Marketing & positioning

| Competitor | Primary channel | Core message | Persona emphasis |
|---|---|---|---|
| Bricklane Data | Paid search, self-serve signup funnel | Speed + price | Procurement and data-team buyers |
| Estemate | Direct sales, industry conferences | Trust and tenure | Risk-averse senior stakeholders |
| ValuAI | Content marketing, conference sponsorships, aggressive LinkedIn presence | "AI-native," technology leadership | Innovation-minded growth buyers — sometimes reaches the buyer before the risk function does |
| PropIQ | Real estate industry communities, webinars | Agent productivity, seller leads | Broker team leads |

## Customer sentiment

| Competitor | Rating | Praise | Complaint |
|---|---|---|---|
| Bricklane Data | ~4.3/5 (G2, ~40 reviews) | Speed, easy self-serve setup | Support "felt automated"; data quality questioned in edge cases |
| Estemate | ~3.6/5 (G2, ~90 reviews) | Data depth, reliability | Slow support response, dated UI *(confirmed — see [competitor-monitoring/example](../sales-tools/competitor-monitoring/weekly-brief-example.md))* |
| ValuAI | ~4.1/5 (G2, ~25 reviews — newer product) | Modern UI, strong demo experience | A few reviews mention promised features not yet available |
| PropIQ | ~4.5/5 (Capterra) | Easy agent adoption | Limited to brokerage use case, not built for banks or insurers |

*(Source: illustrative review patterns, not pulled from a live G2/Capterra feed — treat ratings as directional, not exact.)*

---

## Bricklane Data

**Quick facts:** Threat level 🔴 High · Bank/lender segment · 13 of 35 Q1 losses · Last verified: March 2026 (per [win-loss-analysis](./win-loss-analysis/win-loss-infographic.svg))

**Positioning:** Speed and price. Their pitch is "property data and valuations in seconds, at the lowest per-call cost in the market."

**Strengths:** Genuinely fast, aggressive pricing, easy self-serve API onboarding — appeals to buyers with a strong in-house data team who plan to build their own targeting models and haven't yet been asked to explain them. *(Source: 3 lost-deal notes, Q1)*

**Weaknesses:** No customer-data layer and no moments — the buyer has to build and govern the targeting logic themselves. Valuations come with a confidence score only. No compliance/audit-log feature. *(Source: product comparison, unconfirmed independently — worth a live demo comparison before repeating as certain)*

**How we win:** Reframe the conversation from price-per-call to the cost of building, running, and defending moments in-house. Works best once the Head of Credit Risk (not just procurement or the data team) is in the room — see [`personas.md`](./personas.md).

**How we lose:** Deals that stay procurement- or data-team-led and never reach a real risk conversation; deals where price sensitivity dominates because the institution hasn't yet had a review of how it targets customers.

**Objection handling:** "Bricklane is 15% cheaper" → don't price-match; quantify the build-and-govern cost of turning raw data into moments someone can explain, and offer a side-by-side on one real customer segment.

**Landmines — don't say:** Don't claim Bricklane's data is "inaccurate" — no evidence supports that, and an overclaim here is the kind of thing that gets fact-checked and costs credibility. The honest gap is that they sell data, not explained moments.

**Trigger moments it's in the deal:** Prospect asks about per-call pricing early, before asking about method; the data team is leading the evaluation alone.

---

## Estemate

**Quick facts:** Threat level 🟠 **Medium-High (revised up from Medium)** · Bank/lender and insurer segments, Benelux-heavy · Last verified: September 2026, via [`outdated-checker`](./outdated-checker) sweep (see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md))

**Why the threat level moved:** Win-loss data shows a 27.3% win rate *for us* when Estemate is the named competitor (n=11) — meaning Estemate wins nearly three-quarters of the deals it contests, the worst of any named competitor in this book, despite being the one with the least exciting product story. See the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html). The lesson isn't that Estemate got stronger this period — it's that this document was previously rating threat by how compelling a competitor's pitch sounds, not by how often they actually win.

**Positioning:** Legacy property-data incumbent, especially entrenched in France/Benelux. Sells on relationship tenure and breadth of historical data, with a newer "portfolio insights" report bolted on.

**Strengths:** Long-standing customer relationships, large historical property dataset, strong brand recognition in Benelux specifically. On-prem deployment available, which we currently can't match. *(Source: general market knowledge — worth reconfirming against a specific deal)*

**Weaknesses:** Dated UI, slow release cadence, no live CRM integration (customer data goes in by batch file), publicly documented support responsiveness issues. *(Source: 2 public G2 reviews, confirmed — see [competitor-monitoring/example](../sales-tools/competitor-monitoring/weekly-brief-example.md))*

**How we win:** Modern CRM integration and faster implementation timeline; strongest against Estemate when the buying committee includes someone frustrated with the current tool's UX or support, or a lending/insurance lead who wants moments in the advisors' CRM rather than a quarterly report.

**How we lose:** Deeply entrenched relationships where switching cost (real or perceived) outweighs product gaps; risk-averse buyers who default to "nobody gets fired for choosing the incumbent"; any deal requiring on-prem deployment.

**Objection handling:** "We've used Estemate for 10 years" → don't attack the relationship; focus on a specific, current pain point (support responsiveness, release velocity, no CRM integration) rather than a general pitch to switch.

**Landmines — don't say:** Don't lead with "Estemate is outdated" as a blanket claim — it reads as disrespecting the buyer's own long-standing choice. Let a specific, named pain point (support ticket age, missing feature) do the work instead.

**Trigger moments it's in the deal:** Prospect is Benelux-based; prospect mentions a slow support ticket or a feature request that's been open a long time; prospect states an on-prem requirement.

---

## ValuAI

**Quick facts:** Threat level 🟠 Medium-High · Bank/lender and insurer segments · Last verified: **September 2026**, via [`outdated-checker`](./outdated-checker) sweep (see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md)) — next recheck due October 2026, since this is still the fastest-moving section in this document.

**Positioning:** "AI-native" propensity-scoring challenger, well-funded, leads with technology-forward messaging — as of this period, also reaching for "regulatory-ready" language (see [`competitor-monitoring`](../sales-tools/competitor-monitoring)'s bi-monthly report).

**Strengths:** Strong initial sales narrative, modern-feeling product demo, live CRM integration, aggressive marketing presence, and — as of July 2026 — a shipped, generally available moment-explanation feature. *(Source: market observation; [competitor analyses, Jul–Aug 2026 edition](../sales-tools/competitor-monitoring/competitor-analyses.html))*

**Weaknesses:** No longer "the feature doesn't exist" — it shipped. The current, more precise weakness: adoption evidence is thin (one named enterprise reference customer, no independent validation at scale), the explanation is a feature-importance chart rather than named data points, and property-data depth is thinner, so moments reportedly perform worse on commercial/mixed-use properties than residential. *(Source: [`call-09-ironbridge-bank.md`](./sales-call-analysis/call-09-ironbridge-bank.md); see [`battlecard/valuai.html`](../sales-tools/battlecard/valuai.html) for the fully updated talk track)*

**How we win:** Our clearest differentiation lane has moved from *existence* to *proof at scale* — offer a live evidence trail on the buyer's own customers, and ask ValuAI to do the same. This is working: **0 of 8 head-to-head deals against ValuAI were won by them this period** (see [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)). Don't read that as settled, though — 8 deals is a small sample, and their capability gap is closing, not widening.

**How we lose:** Early-stage deals where the buyer hasn't yet pressure-tested ValuAI's claims and is still impressed by the demo — and, newly, deals where their now-lower quoted price is the deciding factor rather than capability at all.

**Objection handling:** "ValuAI says they're explainable too" → don't dispute it, it's true now. Invite direct comparison instead ("ask them to show which named data points drove one real moment on one of your customers, then ask us the same") and, if the book has a lot of commercial or mixed-use property, that comparison favors us more specifically than it used to.

**Landmines — don't say:** Don't say the explanation feature "doesn't exist" or is "still in beta" — it shipped in July 2026, and repeating the old claim is exactly the kind of thing that gets fact-checked and costs credibility. Don't over-rely on the current 0-for-8 win-loss record either — it's real, but it's recent and small, not a permanent advantage.

**Trigger moments it's in the deal:** Buyer uses the word "AI-native," references a recent ValuAI demo, or brings up their explanation feature by name — worth asking directly whether they've seen it live on their own customers or only in a demo.

---

## PropIQ

**Quick facts:** Threat level ⚪ Low · Brokerage segment · Last verified: March 2026

**Positioning:** Brokerage-focused seller-lead tool, doesn't meaningfully compete in the bank/lender or insurer segments.

**Relevance:** Comes up mainly in brokerage deals or occasionally when a bank buyer also has a brokerage arm evaluating tools separately. Not a primary battlecard priority outside the brokerage segment — deprioritize deepening this section unless brokerage-segment deal volume increases.

---

## Positioning gaps to exploit

1. **No competitor has a credible, specific answer to "show me why this customer was flagged, on our data, not a demo"** — this is the single highest-leverage moment in a competitive deal (see [`positioning.md`](./positioning.md)).
2. **Support responsiveness is a live, public weakness for Estemate** — usable in Benelux-specific battlecards without needing to fabricate anything, since it's evidenced in public reviews.
3. **Bricklane's price-led positioning has no answer to a risk-framed objection** — reframing the conversation away from price is more effective than matching it.

## Known gap working against us

**On-prem deployment** is not currently offered and was the #2 reason for lost deals in Q1 (24% of losses, up from #4 the prior quarter — see [win-loss-analysis](./win-loss-analysis/win-loss-infographic.svg)). Because Seekridge works with the client's own customer data, data-residency questions come up in nearly every bank and insurer deal. Estemate can meet this requirement; Bricklane and ValuAI likely can't either, but that hasn't been confirmed. Surface this limitation proactively with any prospect with a known on-prem requirement rather than letting it surface late — it's a case for product, not something a battlecard talk track can talk around.
