# Positioning — Seekridge

Used by prompts/skills that generate customer-facing content — see [`sales-deck-builder`](../sales-tools/sales-deck-builder), [`branding-guideline`](./branding-guideline), and [`abm-account-brief`](../sales-tools/abm-account-brief) (which picks the specific angle below that fits a named account, rather than the general pitch).

## Market category

Seekridge doesn't try to create a new category. "Customer intelligence" and "next-best-offer" are established, understood terms in banking and insurance, and fighting that understanding would cost more than it earns. The positioning instead claims a **sub-category within it**: not "another propensity score," but "the moment you can explain," treating the evidence behind each opportunity as core infrastructure rather than a bolt-on feature. This is a deliberate choice — category creation is expensive and slow, and the market is already primed to ask the right question (see [`competitive-landscape.md`](./competitive-landscape.md)'s Market Patterns, where two competitors independently started reaching for the same "explainable" language this period — the sub-category is becoming contested, not proprietary).

## Competitive alternatives

What a prospect does instead of buying Seekridge, in rough order of how often it's the actual alternative:

1. **Another data or scoring vendor** (Bricklane Data, Estemate, ValuAI, or occasionally PropIQ in brokerage deals) — the most common alternative, see [`competitive-landscape.md`](./competitive-landscape.md) for the full battlecard set.
2. **Campaigns built by hand from the CRM** — a marketing or sales team pulling lists by simple rules (rate-reset date, policy anniversary, postcode). More common at smaller Tier 2 accounts or ones without a data team (see [`icp.md`](./icp.md)'s Anti-ICP section); the pitch here is about the opportunities those rules miss and the lack of any record of why a customer was chosen, not a better list.
3. **An in-house-built model** — the hardest alternative to displace, since the buyer isn't evaluating a product, they're defending a prior internal decision. Positioning here has to avoid sounding like an attack on the team that built it — see [`icp.md`](./icp.md)'s note on this as a near-Anti-ICP case.
4. **Doing nothing / deferring the decision** — the real competitor in a large share of stalled deals (see the Delta Mortgage Partners pattern in [`sales-call-analysis`](./sales-call-analysis/call-07-delta-mortgage-partners.md)), where the honest positioning response is patience, not more pressure.

## Strategic narrative

Banks, insurers, and brokerages already hold most of the data they need to grow: who their customers are, what they own, and when their contracts end. What they lack is a way to combine that with what's happening to the property and the market, and to act on it before a competitor does. Over the last decade, "AI-powered" tools promised exactly that — and delivered scores nobody could explain. Regulators, risk teams, and front-line advisors are now asking a harder question: *why this customer, and why now?* Most tools can't answer beyond "the model said so."

Seekridge's narrative is not "we find more leads" (most credible vendors can produce a long list) — it's **"we find the opportunities you can actually act on, and show you why."**

## Message house

One primary message, three pillars that support it, each with its own proof point — the structure every other positioning artifact in this repo should trace back to.

**Primary message:** *Opportunities you can act on — and explain.*

| Pillar | Claim | Proof point |
|---|---|---|
| Built on data you already own | Moments combine your own customer data with external market data, so they point at real customers, not cold leads | Every moment links to a named customer record in your CRM — see [`competitive-landscape.md`](./competitive-landscape.md)'s capability comparison |
| Explainable by design | Every moment shows the specific customer and market data points behind it, and how much each counted | Inspectable evidence trail per moment, not a single score — available to technical evaluators on request, see the [Data & CRM Lead persona](./personas.md#data--crm-lead-technical-evaluator) |
| Built for regulated industries, not retrofitted | Data handling, consent rules, and the audit log were designed around banking and insurance compliance from inception | Distinct from a general marketing-AI product with a compliance feature added later |

## Points of view that ladder to this

1. **"A lead you can't explain is a liability, not an opportunity."** An offer only has value if the advisor believes it and the decision to make it survives review later. A list that's twice as long but can't be explained to a risk committee creates risk it doesn't remove.
2. **"AI-powered" is not a differentiator anymore — everyone claims it.** The differentiator is what happens when an advisor, a risk team, or a regulator asks *why* a specific customer was flagged. Most vendors' answer degrades under that question; this is where the real gap is.
3. **"Explainability" needs a definition or it's marketing, not a capability.** Seekridge defines it concretely: the named data points behind each moment, how much each counted, and a reproducible record of what the moment said and what was done with it — not a general claim.

## Differentiators, with proof points

| Differentiator | Proof point (fictional, for illustration) |
|---|---|
| Per-moment evidence trail | Every moment shows the customer and market data points behind it and their weighting — inspectable, not just a score |
| Moment quality validated on the client's own data | Before go-live, moments are backtested against the client's own past outcomes (who actually refinanced, renewed, or sold), and the method is documented for technical evaluators to scrutinize, not just a headline hit rate |
| Built for regulated banking and insurance workflows, not adapted from a marketing tool | Integration points, consent handling, and audit-log format were designed around banking and insurance compliance requirements from the start |

## Positioning by segment and tier

Value proposition changes by who's buying; tier (see [`icp.md`](./icp.md)) changes how much proof the pitch needs to carry before it lands.

| Segment | Pain | Value proposition | Tier-specific note |
|---|---|---|---|
| Risk & compliance (bank/lender) | Can't explain why a customer was targeted with an offer | Moments your risk team can sign off, because every one shows its evidence | Tier 1: the pain is often anticipatory (a coming audit). Tier 2: frequently a *lived* pain — a specific past finding, which makes the pitch easier to land but the sales cycle longer regardless (more procurement layers) |
| Mortgage lending (bank/lender) | Customers refinance elsewhere before anyone notices; top-up and renovation demand goes unseen | Know which customers to call this month, and why, before a competitor does | Matters most at Tier 1, where lending and risk are both active, present stakeholders — see the [persona interaction map](./personas.md#persona-interaction-map) |
| Home insurance | Underinsured homes and quiet non-renewals erode the book | See which policies are underinsured or likely to lapse, with the property evidence to start the conversation | A newer segment for Seekridge — fewer reference customers, so the pitch leans on a backtest on the insurer's own book |
| Brokerage | Agents chase cold leads while likely sellers sit in their own contact list | Moments that tell agents which past clients and contacts are likely to sell, not another dashboard | This is Tier 3's entire positioning — regulatory explainability is largely irrelevant here; adoption and listing value are the whole pitch |

## Positioning against specific competitors — strategic framing

This is the strategic posture behind each competitor's tactical talk track in [`competitive-landscape.md`](./competitive-landscape.md) and its [battlecards](../sales-tools/battlecard) — the "why we lead with this" behind the "what to say."

- **Against Bricklane Data:** Don't compete on their terms (price, speed of raw data). Reframe the axis of comparison entirely, to the cost of building and defending moments yourself — competing on their chosen metric is a losing position even when the product argument is sound.
- **Against Estemate:** Don't position as "the disruptor" — this reads as a risk to a buyer who's already risk-averse by function. Position as "the modernization that doesn't require you to bet on an unproven vendor," which lets a switching decision feel safe rather than bold.
- **Against ValuAI:** The strategic ground has shifted, not disappeared. Before their July 2026 launch of "moment explanations," the position was "they don't have this." Now it has to be "having it and proving it at scale are different claims" — see [`battlecard/valuai.html`](../sales-tools/battlecard/valuai.html) for how the tactical talk track already reflects this shift.
- **Against PropIQ:** Don't compete directly — different buying committee, different job to be done. The only strategic posture needed is "one platform covers your lending, insurance, and brokerage arms," and only when more than one actually exists inside one prospective account.

## Elevator pitches

- **One sentence:** "Seekridge shows banks, insurers, and brokerages which of their existing customers to talk to next, and why — with evidence their risk team can sign off."
- **One paragraph (customer-facing):** "Most customer-scoring tools give you a list and a score. If an advisor or a risk committee asks why a customer is on that list, 'the model said so' isn't an answer — and increasingly, regulators are asking. Seekridge combines your own customer data with external market data, and every moment shows the specific data points behind it, so your team can act on an opportunity as confidently as it found it."
- **Internal onboarding version:** "We don't win on producing the longest lead list — most credible vendors can generate volume. We win by being the one whose moments survive being questioned, by advisors who have to make the call and by the risk team that has to sign off, which matters more every year as scrutiny of automated customer decisions increases."

## Objections to the positioning itself

The positioning has to survive skepticism aimed at the positioning, not just the product:

- **"Every vendor now claims some version of 'explainable.'"** True, and increasingly so (see [`competitive-landscape.md`](./competitive-landscape.md)'s Market Patterns). The response isn't to abandon the claim, it's to make it concrete and provable rather than asserted — see "How this positioning needs to evolve" below.
- **"This sounds like it's just about compliance, not growth."** Fair challenge — the value proposition table above exists specifically to connect the same underlying capability to a growth pain for the VP of Mortgage Lending and Head of Home Insurance personas.
- **"If most vendors can find opportunities, why does this matter at all?"** Because the cost of an unexplainable moment shows up later — in advisors who ignore the list, in a campaign that has to be paused after review, in an audit finding. This is the single hardest part of the pitch to make concrete, and the reason [`sales-deck-builder`](../sales-tools/sales-deck-builder) leads with the buyer's pain before the product.

## How this positioning needs to evolve

This narrative was built on a real, durable gap — but that gap is not static, and the positioning has to be honest about that rather than defend a fixed claim indefinitely. The bi-monthly competitive report ([`competitor-monitoring/bi-monthly-report-2026-07-08.md`](../sales-tools/competitor-monitoring/bi-monthly-report-2026-07-08.md)) flagged this directly: two of four tracked competitors shifted toward "explainable" language in the same period, and ValuAI shipped a real (if unproven-at-scale) moment-explanation feature. The wedge is narrowing faster than expected.

The adaptation already reflected in [`battlecard/valuai.html`](../sales-tools/battlecard/valuai.html) is the right direction for the whole narrative, not just that one battlecard: as competitors close the *capability* gap, the positioning needs to shift its center of gravity from "we have explainability" toward **proof at scale** — named reference customers speaking specifically to the evidence trail, a published backtest, a track record measured in years of production use rather than a launch announcement. Capability claims are becoming table stakes; production-proven trust is not yet.

*(Updated via `staleness-detection` sweep, September 2026 — see [`sweep-2026-09.md`](./staleness-detection/sweep-2026-09.md): the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html) now gives this argument a concrete number — 0 wins for ValuAI across 8 head-to-head deals since their launch — which is the strongest "proof at scale" evidence we currently have for our own side of the claim. Cite it, but don't lean on it as settled: 8 deals is a small, recent sample, and the same sweep also found we're losing nearly three-quarters of deals against Estemate, the least "exciting" competitor in this book — a reminder that this narrative's real test is the boring incumbent as much as the flashy new entrant.)*

## What this is not

Not a claim that Seekridge finds more opportunities than every competitor in every scenario — that claim is not reliably defensible and erodes credibility with a technically skeptical buyer (see the [Head of Credit Risk persona](./personas.md#head-of-credit-risk-risk-and-model-governance-owner-banklender-segment)). The narrative wins on explainability and trust, not a race to the longest lead list.
