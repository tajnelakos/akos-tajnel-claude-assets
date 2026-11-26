# Competitive Landscape — Seekridge

Full battlecard reference. The summary table in [`knowledge-base.md`](./knowledge-base.md) is the quick version; this is what [`competitor-monitoring`](../sales-tools/competitor-monitoring), [`battlecard`](../sales-tools/battlecard), and [`win-loss-analysis`](./win-loss-analysis) draw on for deeper context.

**Last full refresh:** September 2026, following a [`outdated-checker`](./outdated-checker) sweep against the July–August bi-monthly competitor report and the trailing-12-month win-loss deep dive — see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md) for exactly what changed and why. Per-competitor "Last verified" dates below track individual sections.

## Executive summary

Three real competitors for retail-bank deals, none with a decisive product edge — deals are won or lost in the risk conversation, not the demo. Ledgerline is the highest-frequency threat (price-led categorised transaction data, no explanations, leaves moment-building to the bank); NexaScore is the fastest-moving one — its action-explanation feature shipped in July 2026 and it's now competing on price too, and it won 7 of our 8 head-to-heads this period (small sample, but the clearest warning in the book); Conturo is fading but still wins on relationship tenure and on-prem support — and beats us in nearly three deals out of four (72.7% win rate for them when faced, across a larger sample of 11, per the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)), which is worth remembering before assuming the flashier competitor is the bigger threat. Pocketlens solves a different, customer-facing job and rarely competes head-to-head. Our two live vulnerabilities are price and the on-prem gap — see [Known gap working against us](#known-gap-working-against-us).

## Company profiles

| Competitor | Founded | Size | Funding | Target market | Core value prop |
|---|---|---|---|---|---|
| Ledgerline | 2021 | ~80 employees | Series A (~$15M) | Mid-market banks, EU-wide | Fastest, cheapest transaction categorisation and enrichment via API |
| Conturo | 2005 | ~450 employees | Private, no disclosed VC | Large + regional banks, France/Benelux | Two decades of banking analytics and campaign management, now with a "customer insights" add-on |
| NexaScore | 2022 | ~120 employees | Series B (~$60M) | Forward-leaning retail and digital banks, EU-wide | AI-native next-best-action scoring built for what's next |
| Pocketlens | 2019 | ~40 employees | Seed | Banks' digital channel teams | Money insights for customers inside the banking app |

*(Source: general market knowledge, not independently verified — reconfirm before citing a specific figure to a prospect.)*

## Quick reference — read this before a call

| Competitor | Threat level | Segment | Win angle | Landmine — don't say |
|---|---|---|---|---|
| [Ledgerline](#ledgerline) | 🔴 High — most frequent competitor in losses (13 of 35 lost deals, Q1) | Retail banks | Reframe price → the cost of building and defending moments yourself | Don't price-match — it concedes the frame that this is commodity data |
| [NexaScore](#nexascore) | 🟠 Medium-High — shipped action explanations in Jul 2026; we won only 1 of 8 head-to-heads since; a small sample, but they are beating us | Retail and digital banks | Ask for proof at scale (named reference, live test on the buyer's own customers) — existence of the feature is no longer the wedge | Don't call it "still in beta" — it shipped; don't assume our current win rate against them will hold |
| [Conturo](#conturo) | 🟠 Medium-High — revised up: wins 72.7% of deals it contests (n=11), despite the least exciting product story of the three | Retail banks (Benelux-heavy) | Modern CRM integration + faster implementation, once a frustrated stakeholder is in the room | Don't attack the relationship tenure — it's their strongest card, and it's working better than this document previously credited |
| [Pocketlens](#pocketlens) | ⚪ Low — different job | Digital channel teams, credit unions | N/A — rarely a head-to-head deal | N/A |

## Capability comparison

Illustrative — not a substitute for a live demo comparison.

| | Seekridge | Ledgerline | Conturo | NexaScore |
|---|---|---|---|---|
| Per-moment evidence trail (transaction, customer and market data points) | ✅ Yes | ❌ No moments — categorised transactions and a confidence score only | ⚠️ Partial, segment-level reports in a dated format | ⚠️ Shipped Jul 2026, but a feature-importance chart rather than named data points, and reportedly weaker where personal and business spending mix (sole traders, small-business owners, see [`call-09-ironbridge-bank.md`](./sales-call-analysis/call-09-ironbridge-bank.md)) |
| Combines the bank's own CRM and product data | ✅ Yes | ❌ No — transaction enrichment only | ⚠️ Batch file upload, no live CRM integration | ✅ Yes |
| Main-bank vs. secondary-bank view per customer | ✅ Yes | ❌ No | ⚠️ Rule-based flag | ⚠️ Score only |
| Moment-quality method disclosed (backtest on client data) | ✅ Yes | ❌ Not applicable / not published | ✅ Yes, established track record | ❌ Claimed, not disclosed |
| On-prem deployment | ❌ No — current gap, see [win-loss data](./win-loss-analysis/win-loss-infographic.svg) | ❌ Cloud only | ✅ Yes (legacy architecture) | ❌ Cloud only |
| Implementation timeline | Weeks | Fastest — self-serve API (but the bank builds the moments) | Slowest — legacy integration | Medium |
| Pricing model | Subscription by number of retail customers analysed | Usage-based per API call, ~15% below Seekridge on comparable volume | Enterprise/negotiated, typically higher | Not publicly disclosed; averaged ~9% below our deal size in Q3 head-to-heads (n=8, see [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)) |

The on-prem gap is real, not a competitor's weakness — flag it early with a prospect that requires it rather than letting it surface late in the deal.

## Pricing & packaging

| Competitor | Model | Notes |
|---|---|---|
| Seekridge | Subscription priced by retail customers analysed, seat-based for the web app | No self-serve tier for the platform — sales-assisted only |
| Ledgerline | Usage-based per API call, ~15% below Seekridge | Self-serve signup, no enterprise tier disclosed — built for fast adoption without procurement |
| Conturo | Enterprise/negotiated only | Multi-year contracts typical, no self-serve option |
| NexaScore | Not publicly disclosed | Sales-assisted only. The "premium-priced" assumption didn't hold up in Q3 head-to-heads — their average quote came in below our average deal size (see [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)); price is now part of their play, not just capability |
| Pocketlens | Per active app user, tiered | Packaged widget, quick to switch on |

## Marketing & positioning

| Competitor | Primary channel | Core message | Persona emphasis |
|---|---|---|---|
| Ledgerline | Paid search, self-serve signup funnel | Speed + price | Procurement and data-team buyers |
| Conturo | Direct sales, industry conferences | Trust and tenure | Risk-averse senior stakeholders |
| NexaScore | Content marketing, conference sponsorships, aggressive LinkedIn presence | "AI-native," technology leadership | Innovation-minded growth buyers — sometimes reaches the buyer before the risk function does |
| Pocketlens | Fintech events, app-store-style demos | Engagement in the banking app | Digital channel leads |

## Customer sentiment

| Competitor | Rating | Praise | Complaint |
|---|---|---|---|
| Ledgerline | ~4.3/5 (G2, ~40 reviews) | Speed, easy self-serve setup | Support "felt automated"; categorisation questioned in edge cases |
| Conturo | ~3.6/5 (G2, ~90 reviews) | Depth, reliability | Slow support response, dated UI *(confirmed — see [competitor-monitoring/example](../sales-tools/competitor-monitoring/weekly-brief-example.md))* |
| NexaScore | ~4.1/5 (G2, ~25 reviews — newer product) | Modern UI, strong demo experience | A few reviews mention promised features not yet available |
| Pocketlens | ~4.5/5 (Capterra) | Easy to switch on, customers like it | Customer-facing only; bankers don't see it |

*(Source: illustrative review patterns, not pulled from a live G2/Capterra feed — treat ratings as directional, not exact.)*

---

## Ledgerline

**Quick facts:** Threat level 🔴 High · Retail banks · 13 of 35 Q1 losses · Last verified: March 2026 (per [win-loss-analysis](./win-loss-analysis/win-loss-infographic.svg))

**Positioning:** Speed and price. Their pitch is "every transaction categorised and enriched in milliseconds, at the lowest per-call cost in the market."

**Strengths:** Genuinely fast, aggressive pricing, easy self-serve API onboarding — appeals to banks with a strong in-house data team who plan to build their own targeting models and haven't yet been asked to explain them. *(Source: 3 lost-deal notes, Q1)*

**Weaknesses:** No customer-data layer and no moments — the bank has to build and govern the targeting logic itself. Categories come with a confidence score only. No compliance/audit-log feature. *(Source: product comparison, unconfirmed independently — worth a live demo comparison before repeating as certain)*

**How we win:** Reframe the conversation from price-per-call to the cost of building, running, and defending moments in-house. Works best once the buyer has forwarded the review pack, so model risk (not just procurement or the data team) has seen the method — see [`personas.md`](./personas.md).

**How we lose:** Deals that stay procurement- or data-team-led and never reach a real risk conversation; deals where price sensitivity dominates because the bank hasn't yet had a review of how it targets customers.

**Objection handling:** "Ledgerline is 15% cheaper" → don't price-match; quantify the build-and-govern cost of turning categorised transactions into moments someone can explain, and offer a side-by-side on one real customer segment.

**Landmines — don't say:** Don't claim Ledgerline's categorisation is "inaccurate" — no evidence supports that, and an overclaim here is the kind of thing that gets fact-checked and costs credibility. The honest gap is that they sell enriched data, not explained moments.

**Trigger moments it's in the deal:** Prospect asks about per-call pricing early, before asking about method; the data team is leading the evaluation alone.

---

## Conturo

**Quick facts:** Threat level 🟠 **Medium-High (revised up from Medium)** · Retail banks, Benelux-heavy · Last verified: September 2026, via [`outdated-checker`](./outdated-checker) sweep (see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md))

**Why the threat level moved:** Win-loss data shows a 27.3% win rate *for us* when Conturo is the named competitor (n=11) — meaning Conturo wins nearly three-quarters of the deals it contests, across the largest sample of any named competitor in this book, despite being the one with the least exciting product story. See the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html). The lesson isn't that Conturo got stronger this period — it's that this document was previously rating threat by how compelling a competitor's pitch sounds, not by how often they actually win.

**Positioning:** Legacy banking-analytics and campaign-management incumbent, especially entrenched in France/Benelux. Sells on relationship tenure and a large installed base, with a newer "customer insights" report bolted on.

**Strengths:** Long-standing customer relationships, deep integration into older core systems, strong brand recognition in Benelux specifically. On-prem deployment available, which we currently can't match. *(Source: general market knowledge — worth reconfirming against a specific deal)*

**Weaknesses:** Dated UI, slow release cadence, no live CRM integration (data goes in by batch file), publicly documented support responsiveness issues. *(Source: 2 public G2 reviews, confirmed — see [competitor-monitoring/example](../sales-tools/competitor-monitoring/weekly-brief-example.md))*

**How we win:** Modern CRM integration and faster implementation timeline; strongest against Conturo when the buying committee includes someone frustrated with the current tool's UX or support, or a retail lead who wants moments in the bankers' CRM rather than a quarterly report.

**How we lose:** Deeply entrenched relationships where switching cost (real or perceived) outweighs product gaps; risk-averse buyers who default to "nobody gets fired for choosing the incumbent"; any deal requiring on-prem deployment.

**Objection handling:** "We've used Conturo for 10 years" → don't attack the relationship; focus on a specific, current pain point (support responsiveness, release velocity, no CRM integration) rather than a general pitch to switch.

**Landmines — don't say:** Don't lead with "Conturo is outdated" as a blanket claim — it reads as disrespecting the buyer's own long-standing choice. Let a specific, named pain point (support ticket age, missing feature) do the work instead.

**Trigger moments it's in the deal:** Prospect is Benelux-based; prospect mentions a slow support ticket or a feature request that's been open a long time; prospect states an on-prem requirement.

---

## NexaScore

**Quick facts:** Threat level 🟠 Medium-High · Retail and digital banks · Last verified: **September 2026**, via [`outdated-checker`](./outdated-checker) sweep (see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md)) — next recheck due October 2026, since this is still the fastest-moving section in this document.

**Positioning:** "AI-native" next-best-action challenger, well-funded, leads with technology-forward messaging — as of this period, also reaching for "regulatory-ready" language (see [`competitor-monitoring`](../sales-tools/competitor-monitoring)'s bi-monthly report).

**Strengths:** Strong initial sales narrative, modern-feeling product demo, live CRM integration, aggressive marketing presence, and — as of July 2026 — a shipped, generally available action-explanation feature. *(Source: market observation; [competitor analyses, Jul–Aug 2026 edition](../sales-tools/competitor-monitoring/competitor-analyses.html))*

**Weaknesses:** No longer "the feature doesn't exist" — it shipped. The current, more precise weakness: adoption evidence is thin (one named enterprise reference customer, no independent validation at scale), the explanation is a feature-importance chart rather than named data points, and their models are trained on standard retail accounts, so moments reportedly perform worse where personal and business spending mix — sole traders and small-business owners. *(Source: [`call-09-ironbridge-bank.md`](./sales-call-analysis/call-09-ironbridge-bank.md); see [`battlecard/nexascore.html`](../sales-tools/battlecard/nexascore.html) for the fully updated talk track)*

**How we win:** Our clearest differentiation lane has moved from *existence* to *proof at scale* — offer a live evidence trail on the buyer's own customers, and ask NexaScore to do the same. It has to start working: **we won only 1 of 8 head-to-head deals against NexaScore** (see [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html)). 8 deals is a small sample, but the direction is clear: their capability gap is closing, and they now undercut us on price too.

**How we lose:** Early-stage deals where the buyer hasn't yet pressure-tested NexaScore's claims and is still impressed by the demo — and, newly, deals where their now-lower quoted price is the deciding factor rather than capability at all.

**Objection handling:** "NexaScore says they're explainable too" → don't dispute it, it's true now. Invite direct comparison instead ("ask them to show which named transactions drove one real moment on one of your customers, then ask us the same") and, if the bank has a lot of sole traders and small-business owners, that comparison favors us more specifically than it used to.

**Landmines — don't say:** Don't say the explanation feature "doesn't exist" or is "still in beta" — it shipped in July 2026, and repeating the old claim is exactly the kind of thing that gets fact-checked and costs credibility. Don't dismiss them as not ready either: they won 7 of our last 8 head-to-heads.

**Trigger moments it's in the deal:** Buyer uses the word "AI-native," references a recent NexaScore demo, or brings up their explanation feature by name — worth asking directly whether they've seen it live on their own customers or only in a demo.

---

## Pocketlens

**Quick facts:** Threat level ⚪ Low · Digital channel teams, credit unions · Last verified: March 2026

**Positioning:** Customer-facing money-insights widget for banking apps — spending summaries and tips shown to the customer. Doesn't meaningfully compete for bank-facing moments.

**Relevance:** Comes up mainly at credit unions and when a bank's digital channel team runs its own evaluation. The honest framing is that the two do different jobs: insights for customers versus opportunities for bankers. Not a primary battlecard priority — deprioritize deepening this section unless it starts appearing in Tier 1 deals.

---

## Positioning gaps to exploit

1. **No competitor has a credible, specific answer to "show me why this customer was flagged, on our data, not a demo"** — this is the single highest-leverage moment in a competitive deal (see [`positioning.md`](./positioning.md)).
2. **Support responsiveness is a live, public weakness for Conturo** — usable in Benelux-specific battlecards without needing to fabricate anything, since it's evidenced in public reviews.
3. **Ledgerline's price-led positioning has no answer to a risk-framed objection** — reframing the conversation away from price is more effective than matching it.
4. **Nobody else leads with the main-bank question** — whether the bank is a customer's main or secondary bank is the first thing Seekridge shows, and the question every Head of Retail Banking is already asking.

## Known gap working against us

**On-prem deployment** is not currently offered and was the #2 reason for lost deals in Q1 (24% of losses, up from #4 the prior quarter — see [win-loss-analysis](./win-loss-analysis/win-loss-infographic.svg)). Because Seekridge works with the bank's own transaction data, data-residency questions come up in nearly every deal. Conturo can meet this requirement; Ledgerline and NexaScore likely can't either, but that hasn't been confirmed. Surface this limitation proactively with any prospect with a known on-prem requirement rather than letting it surface late — it's a case for product, not something a battlecard talk track can talk around.
