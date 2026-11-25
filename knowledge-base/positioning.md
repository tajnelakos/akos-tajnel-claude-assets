# Positioning — Seekridge

Used by prompts/skills that generate customer-facing content — see [`sales-deck-builder`](../sales-tools/sales-deck-builder) and [`branding-guideline`](./branding-guideline).

## Market category

Seekridge doesn't try to create a new category. "Customer intelligence" and "next-best-offer" are established, understood terms in retail banking, and fighting that understanding would cost more than it earns. The positioning instead claims a **sub-category within it**: not "another propensity score," but "growth from your own customers, with the reason attached" — the opportunity is what the buyer pays for, and the evidence behind each one is what makes advisors act on it and lets the bank approve it once, rather than a bolt-on feature. This is a deliberate choice — category creation is expensive and slow, and the market is already primed to ask the right question (see [`competitive-landscape.md`](./competitive-landscape.md)'s Market Patterns, where two competitors independently started reaching for the same "explainable" language this period — the sub-category is becoming contested, not proprietary).

## Competitive alternatives

What a prospect does instead of buying Seekridge, in rough order of how often it's the actual alternative:

1. **Another data or scoring vendor** (Ledgerlight, Kontora, Propensa, or Nudgely in digital-first banks) — the most common alternative, see [`competitive-landscape.md`](./competitive-landscape.md) for the full battlecard set.
2. **Campaigns built by hand from the CRM** — a marketing or sales team pulling lists by simple rules (rate-reset date, salary above a threshold, balance above a threshold). More common at smaller Tier 2 accounts or ones without a data team (see [`icp.md`](./icp.md)'s Anti-ICP section); the pitch here is about the opportunities those rules miss and the lack of any record of why a customer was chosen, not a better list.
3. **An in-house-built model** — the hardest alternative to displace, since the buyer isn't evaluating a product, they're defending a prior internal decision. Positioning here has to avoid sounding like an attack on the team that built it — see [`icp.md`](./icp.md)'s note on this as a near-Anti-ICP case.
4. **Doing nothing / deferring the decision** — the real competitor in a large share of stalled deals (see the Delta Mortgage Partners pattern in [`sales-call-analysis`](./sales-call-analysis/call-07-delta-mortgage-partners.md)), where the honest positioning response is patience, not more pressure.

## Strategic narrative

Retail banks already hold most of the data they need to grow: every salary that comes in, every payment that goes out, and when each contract ends. Their customers refinance at other banks, finance cars elsewhere and insure their homes with someone else — all of it visible in their own transaction data, and almost none of it acted on. Over the last decade, "AI-powered" tools promised to fix that and delivered scores nobody could explain: advisors ignored the lists, and risk teams paused the campaigns. The question that decides whether an opportunity turns into business is *why this customer, and why now?* Most tools can't answer beyond "the model said so."

Seekridge's narrative is not "we find more leads" (most credible vendors can produce a long list) — it's **"we find the opportunities you can actually act on, and show you why."**

## Message house

One primary message, three pillars that support it, each with its own proof point — the structure every other positioning artifact in this repo should trace back to.

**Primary message:** *Opportunities you can act on — and explain.*

| Pillar | Claim | Proof point |
|---|---|---|
| Growth from customers you already have | Moments come from your own transaction and CRM data plus market data: mortgages held at other banks, purchases, car and renovation loans, card upgrades, insurance bought elsewhere | Every moment links to a named customer record in your CRM — see [`competitive-landscape.md`](./competitive-landscape.md)'s capability comparison |
| Advisors act on it | Every moment shows the specific data points behind it and how much each counted, so advisors know why they're calling | Inspectable evidence trail per moment, not a single score — testable on the bank's own records, see the [Data & CRM Lead persona](./personas.md#data--crm-lead-technical-evaluator) |
| Approved once, not campaign by campaign | The same evidence, the method and the consent handling go to risk and data protection as a ready review pack, so the buyer never has to make the risk case alone | Data handling, consent rules and the audit log were designed around banking compliance from inception, not added later |

## Points of view that ladder to this

1. **"A lead you can't explain is a lead nobody calls."** An opportunity only turns into business if the advisor believes it and the decision to make the offer survives review later. A list that's twice as long but comes without reasons gets ignored, then paused.
2. **"AI-powered" is not a differentiator anymore — everyone claims it.** The differentiator is what happens when an advisor, a risk team, or a regulator asks *why* a specific customer was flagged. Most vendors' answer degrades under that question; this is where the real gap is.
3. **"Explainability" needs a definition or it's marketing, not a capability.** Seekridge defines it concretely: the named data points behind each moment, how much each counted, and a reproducible record of what the moment said and what was done with it — not a general claim.

## Differentiators, with proof points

| Differentiator | Proof point (fictional, for illustration) |
|---|---|
| Per-moment evidence trail | Every moment shows the transaction, CRM and market data points behind it and their weighting — inspectable, not just a score |
| Moment quality validated on the client's own data | Before go-live, moments are backtested against the client's own past outcomes (who actually refinanced elsewhere, moved their salary, or took up an offer), and the method is documented for technical evaluators to scrutinize, not just a headline hit rate |
| Built for regulated banking workflows, not adapted from a marketing tool | Integration points, consent handling, and audit-log format were designed around banking compliance requirements from the start |

## Positioning by segment and tier

Value proposition changes by who's buying; tier (see [`icp.md`](./icp.md)) changes how much proof the pitch needs to carry before it lands.

| Segment | Pain | Value proposition | Tier-specific note |
|---|---|---|---|
| Mortgage lending — Head of Mortgage Lending | Customers refinance elsewhere before anyone notices; half the base holds a mortgage at another bank; purchase demand goes unseen | Know which customers to call this month, and why, before a competitor does: mortgages to win back at fixed-rate end, purchases to finance | The entry point at most Tier 1 banks — the biggest-ticket moments, and the fastest number to prove in a backtest |
| Retail banking — Head of Retail Banking | Customers finance cars, renovations and insurance elsewhere, and drift to another bank one salary at a time | See which customers are ready for a car or green loan, a card upgrade or insurance, and which are making you their secondary bank, while there's time to act | The budget owner once Seekridge covers more than mortgages, and the only buyer at most Tier 3 banks. Insurance is newer, with fewer references, so the pitch leans on a backtest on the bank's own customers |

Risk, model governance and data protection are not segments we market to. They review the deal, and the evidence trail is what we hand them, through the buyer — see [`personas.md`](./personas.md).

## Positioning against specific competitors — strategic framing

This is the strategic posture behind each competitor's tactical talk track in [`competitive-landscape.md`](./competitive-landscape.md) and its [battlecards](../sales-tools/battlecard) — the "why we lead with this" behind the "what to say."

- **Against Ledgerlight:** Don't compete on their terms (price, speed of raw data). Reframe the axis of comparison entirely, to the cost of building and defending moments yourself — competing on their chosen metric is a losing position even when the product argument is sound.
- **Against Kontora:** Don't position as "the disruptor" — this reads as a risk to a buyer who has relied on the incumbent for years. Position as "the modernization that doesn't require you to bet on an unproven vendor," which lets a switching decision feel safe rather than bold.
- **Against Propensa:** The strategic ground has shifted, not disappeared. Before their July 2026 launch of "moment explanations," the position was "they don't have this." Now it has to be "having it and proving it at scale are different claims" — see [`battlecard/propensa.html`](../sales-tools/battlecard/propensa.html) for how the tactical talk track already reflects this shift.
- **Against Nudgely:** Don't compete on the end-customer app experience — different buying committee (digital channels), different job to be done. The posture is "in-app insights reach customers who open the app; moments reach the customers your advisors should call", and the two can run side by side.

## Elevator pitches

- **One sentence:** "Seekridge shows retail banks which of their existing customers are about to refinance, buy, borrow or insure — read from their own transaction data, with the reason attached so advisors act on it."
- **One paragraph (customer-facing):** "Your customers refinance at other banks, finance cars elsewhere and insure their homes with someone else — and it's all visible in your own transaction data. Seekridge reads that data alongside the market, finds the customers about to make a move, and puts each one in your advisors' CRM with the data points behind it. Advisors know why they're calling, and your risk team approves the approach once instead of campaign by campaign."
- **Internal onboarding version:** "We don't win on producing the longest lead list — most credible vendors can generate volume. We win by being the one whose moments turn into business: advisors act on them because they show why, and they survive review, which matters more every year as scrutiny of automated customer decisions increases."

## Objections to the positioning itself

The positioning has to survive skepticism aimed at the positioning, not just the product:

- **"Every vendor now claims some version of 'explainable.'"** True, and increasingly so (see [`competitive-landscape.md`](./competitive-landscape.md)'s Market Patterns). The response isn't to abandon the claim, it's to make it concrete and provable rather than asserted — see "How this positioning needs to evolve" below.
- **"This sounds like it's just about compliance, not growth."** It was, in an earlier version of this narrative, and that was a mistake: compliance teams review, they don't buy. The positioning now leads with growth for the two buyers (Head of Mortgage Lending, Head of Retail Banking); explainability is why the growth actually happens, not the headline.
- **"If most vendors can find opportunities, why does this matter at all?"** Because the cost of an unexplainable moment shows up later — in advisors who ignore the list, in a campaign that has to be paused after review, in an audit finding. This is the single hardest part of the pitch to make concrete, and the reason [`sales-deck-builder`](../sales-tools/sales-deck-builder) leads with the buyer's pain before the product.

## How this positioning needs to evolve

This narrative was built on a real, durable gap — but that gap is not static, and the positioning has to be honest about that rather than defend a fixed claim indefinitely. The bi-monthly [competitor analyses](../sales-tools/competitor-monitoring/competitor-analyses.html) (Jul–Aug 2026 edition) flagged this directly: two of four tracked competitors shifted toward "explainable" language in the same period, and Propensa shipped a real (if unproven-at-scale) moment-explanation feature. The wedge is narrowing faster than expected.

The adaptation already reflected in [`battlecard/propensa.html`](../sales-tools/battlecard/propensa.html) is the right direction for the whole narrative, not just that one battlecard: as competitors close the *capability* gap, the positioning needs to shift its center of gravity from "we have explainability" toward **proof at scale** — named reference customers speaking specifically to the evidence trail, a published backtest, a track record measured in years of production use rather than a launch announcement. Capability claims are becoming table stakes; production-proven trust is not yet.

*(Updated via `outdated-checker` sweep, September 2026 — see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md): the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html) now gives this argument a concrete, uncomfortable number — we won only 1 of 8 head-to-head deals against Propensa — which is why the "proof at scale" argument has to be made live, on the buyer's own data, rather than asserted. 8 deals is a small, recent sample, and the same sweep also found we're losing nearly three-quarters of deals against Kontora, the least "exciting" competitor in this book — a reminder that this narrative's real test is the boring incumbent as much as the flashy new entrant.)*

## What this is not

Not a claim that Seekridge finds more opportunities than every competitor in every scenario — that claim is not reliably defensible and erodes credibility with buyers and their technical evaluators (see the [Data & CRM Lead persona](./personas.md#data--crm-lead-technical-evaluator)). The narrative wins on opportunities advisors actually act on, not a race to the longest lead list.
