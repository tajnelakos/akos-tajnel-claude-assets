# Positioning — Seekridge

Used by prompts/skills that generate customer-facing content — see [`sales-deck-builder`](../sales-tools/sales-deck-builder), [`branding-guideline`](./branding-guideline), [`one-pager-builder`](../marketing-assets/one-pager-builder) and [`persona-email-sequence`](../marketing-assets/persona-email-sequence), which pick the specific angle below that fits a given reader rather than the general pitch.

## Market category

Seekridge doesn't try to create a new category. "Customer intelligence," "next-best-action" and "personalisation" are established, understood terms in retail banking, and fighting that understanding would cost more than it earns. The positioning instead claims a **sub-category within it**: not "another propensity score" and not "insights in the banking app," but **"the bank-facing moment you can explain"** — an opportunity sent to the bank's own people, with the evidence behind it treated as core infrastructure rather than a bolt-on feature. This is a deliberate choice — category creation is expensive and slow, and the market is already primed to ask the right question (see [`competitive-landscape.md`](./competitive-landscape.md)'s Market Patterns, where two competitors independently started reaching for the same "explainable" language this period — the sub-category is becoming contested, not proprietary).

## Competitive alternatives

What a prospect does instead of buying Seekridge, in rough order of how often it's the actual alternative:

1. **Another data or scoring vendor** (Ledgerline, Conturo, NexaScore, or occasionally Pocketlens when the bank's digital team leads) — the most common alternative, see [`competitive-landscape.md`](./competitive-landscape.md) for the full battlecard set.
2. **Campaigns built by hand from the CRM** — a marketing team pulling lists by simple rules (balance above a threshold, product anniversary, age band). More common at smaller Tier 2 accounts or ones without a data team (see [`icp.md`](./icp.md)'s Anti-ICP section); the pitch here is about the moments those rules miss — the salary that never arrived, the transfer that started last month — and the lack of any record of why a customer was chosen, not a better list.
3. **An in-house-built model** — the hardest alternative to displace, since the buyer isn't evaluating a product, they're defending a prior internal decision. Positioning here has to avoid sounding like an attack on the team that built it — see [`icp.md`](./icp.md)'s note on this as a near-Anti-ICP case.
4. **Doing nothing / deferring the decision** — the real competitor in a large share of stalled deals (see the Delta Direct Bank pattern in [`sales-call-analysis`](./sales-call-analysis/call-07-delta-direct-bank.md)), where the honest positioning response is patience, not more pressure.

## Strategic narrative

Retail banks already hold the richest data about their customers' financial lives: every salary, every card payment, every transfer out. Most of it goes unread. Customers now spread their money across several providers, so a bank can look like a customer's main bank while their salary, savings and investments quietly sit elsewhere — and the bank finds out when the balance is gone. Over the last decade, "AI-powered" tools promised to fix that — and delivered scores nobody could explain, or insights pushed into the banking app that the bank's own people never see. Regulators, risk and data-protection teams, and front-line bankers are now asking a harder question: *why this customer, and why now?* Most tools can't answer beyond "the model said so."

Seekridge's narrative is not "we find more leads" (most credible vendors can produce a long list) — it's **"we find the opportunities your bankers can actually act on, and show you why."**

## Message house

One primary message, three pillars that support it, each with its own proof point — the structure every other positioning artifact in this repo should trace back to.

**Primary message:** *Opportunities you can act on — and explain.*

| Pillar | Claim | Proof point |
|---|---|---|
| Built on data you already own | Moments read your own transaction, customer and AI-agent data alongside market data, so they point at real customers, not cold leads | Every moment links to a named customer record in your CRM — see [`competitive-landscape.md`](./competitive-landscape.md)'s capability comparison |
| Explainable by design | Every moment shows the specific transaction, customer and market data points behind it, and how much each counted | Inspectable evidence trail per moment, not a single score — available to technical evaluators on request, see the [Data & CRM Lead persona](./personas.md#data--crm-lead-technical-evaluator) |
| Built for regulated banking, not retrofitted | Purpose limits on transaction data, consent rules, and the audit log were designed around banking compliance and data protection from inception | Distinct from a general marketing-AI product with a compliance feature added later |

## Points of view that ladder to this

1. **"A lead you can't explain is a liability, not an opportunity."** An offer only has value if the banker believes it and the decision to make it survives review later. A list that's twice as long but can't be explained to a risk committee or a data protection officer creates risk it doesn't remove.
2. **"Your bank may be a customer's second bank, and you'd be the last to know."** Account ownership isn't the relationship. Where the salary lands, which card pays for groceries and where the savings go decide it — and all of that is already in the transaction data.
3. **"Explainability" needs a definition or it's marketing, not a capability.** Seekridge defines it concretely: the named data points behind each moment, how much each counted, and a reproducible record of what the moment said and what was done with it — not a general claim.

## Differentiators, with proof points

| Differentiator | Proof point (fictional, for illustration) |
|---|---|
| Per-moment evidence trail | Every moment shows the transaction, customer and market data points behind it and their weighting — inspectable, not just a score |
| Moment quality validated on the bank's own data | Before go-live, moments are backtested against the bank's own past outcomes (who actually moved money out, switched their salary in, or took a mortgage), and the method is documented for technical evaluators to scrutinize, not just a headline hit rate |
| Bank-facing by design | Moments land in the CRM and in front of the banker who owns the relationship, with the next best conversation attached — not a customer-facing feed the bank's people never see |
| Built for regulated banking workflows, not adapted from a marketing tool | Integration points, purpose limits on transaction data, consent handling, and audit-log format were designed around banking compliance and data-protection requirements from the start |

## Positioning by persona and tier

Value proposition changes by who's buying; tier (see [`icp.md`](./icp.md)) changes how much proof the pitch needs to carry before it lands.

| Buyer | Pain | Value proposition | Tier-specific note |
|---|---|---|---|
| Risk, compliance & data protection | Can't explain why a customer was targeted with an offer, or show that transaction data was used within its purpose | Moments your risk team can sign off, because every one shows its evidence | Tier 1: the pain is often anticipatory (a coming review). Tier 2: frequently a *lived* pain — a specific past finding, which makes the pitch easier to land but the sales cycle longer regardless (more procurement layers) |
| Retail banking | Looks like the main bank, isn't; growth targets on the existing base with no idea which customers to call | Know which customers to call this month, and why — main-bank and growth moments — mortgage-ready, car purchase goal, family growing — before a competitor sees them | Matters most at Tier 1, where retail and risk are both active, present stakeholders — see the [persona interaction map](./personas.md#persona-interaction-map) |
| Deposits & savings | Money leaves in small monthly transfers; the bank notices when the balance is gone | See which customers are starting to move money out, with the evidence to call them first — **Seekridge Outflow Watch** | The newest product — fewer reference customers, so the pitch leans on a backtest on the bank's own past outflows |
| Relationship managers (credit unions, small cooperative banks) | Bankers work from gut feel and old lists; a new tool nobody opens after month one | Moments that tell each banker which members to call this week, in a web app with no integration project | This is Tier 3's entire positioning — adoption and conversation value are the whole pitch; the risk conversation is lighter |

## Positioning against specific competitors — strategic framing

This is the strategic posture behind each competitor's tactical talk track in [`competitive-landscape.md`](./competitive-landscape.md) and its [battlecards](../sales-tools/battlecard) — the "why we lead with this" behind the "what to say."

- **Against Ledgerline:** Don't compete on their terms (price, speed of categorised data). Reframe the axis of comparison entirely, to the cost of building and defending moments yourself — competing on their chosen metric is a losing position even when the product argument is sound.
- **Against Conturo:** Don't position as "the disruptor" — this reads as a risk to a buyer who's already risk-averse by function. Position as "the modernization that doesn't require you to bet on an unproven vendor," which lets a switching decision feel safe rather than bold.
- **Against NexaScore:** The strategic ground has shifted, not disappeared. Before their July 2026 launch of "action explanations," the position was "they don't have this." Now it has to be "having it and proving it at scale are different claims" — see [`battlecard/nexascore.html`](../sales-tools/battlecard/nexascore.html) for how the tactical talk track already reflects this shift.
- **Against Pocketlens:** Don't compete directly — different job, usually a different buyer (the digital channel team). The only strategic posture needed is "insights for your customers and opportunities for your bankers are different jobs; we do the second," and only when both come up inside one account.

## Elevator pitches

- **One sentence:** "Seekridge reads the transaction data your bank already has and shows your bankers which customers to talk to next, and why — with evidence your risk team can sign off."
- **One paragraph (customer-facing):** "Your customers' salaries, card payments and transfers tell you when your bank is about to become their main bank — or stop being it. Most tools give you a list and a score. If a banker or a risk committee asks why a customer is on that list, 'the model said so' isn't an answer — and increasingly, regulators are asking. Seekridge reads your transaction and customer data alongside market data, and every moment shows the specific data points behind it, so your team can act on an opportunity as confidently as it found it."
- **Internal onboarding version:** "We don't win on producing the longest lead list — most credible vendors can generate volume. We win by being the one whose moments survive being questioned, by bankers who have to make the call and by the risk and data-protection teams that have to sign off, which matters more every year as scrutiny of automated customer decisions increases."

## Objections to the positioning itself

The positioning has to survive skepticism aimed at the positioning, not just the product:

- **"Every vendor now claims some version of 'explainable.'"** True, and increasingly so (see [`competitive-landscape.md`](./competitive-landscape.md)'s Market Patterns). The response isn't to abandon the claim, it's to make it concrete and provable rather than asserted — see "How this positioning needs to evolve" below.
- **"This sounds like it's just about compliance, not growth."** Fair challenge — the value proposition table above exists specifically to connect the same underlying capability to a growth pain for the Head of Retail Banking and Head of Deposits & Savings personas.
- **"Isn't using transaction data for offers exactly what regulators worry about?"** Yes — which is why the evidence trail and purpose limits exist. A bank that can't show why it used a customer's transactions to make an offer has a problem with or without Seekridge; with it, the answer is on record.
- **"If most vendors can find opportunities, why does this matter at all?"** Because the cost of an unexplainable moment shows up later — in bankers who ignore the list, in a campaign that has to be paused after review, in an audit finding. This is the single hardest part of the pitch to make concrete, and the reason [`sales-deck-builder`](../sales-tools/sales-deck-builder) leads with the buyer's pain before the product.

## How this positioning needs to evolve

This narrative was built on a real, durable gap — but that gap is not static, and the positioning has to be honest about that rather than defend a fixed claim indefinitely. The bi-monthly [competitor analyses](../sales-tools/competitor-monitoring/competitor-analyses.html) (Jul–Aug 2026 edition) flagged this directly: two of four tracked competitors shifted toward "explainable" language in the same period, and NexaScore shipped a real (if unproven-at-scale) action-explanation feature. The wedge is narrowing faster than expected.

The adaptation already reflected in [`battlecard/nexascore.html`](../sales-tools/battlecard/nexascore.html) is the right direction for the whole narrative, not just that one battlecard: as competitors close the *capability* gap, the positioning needs to shift its center of gravity from "we have explainability" toward **proof at scale** — named reference customers speaking specifically to the evidence trail, a published backtest, a track record measured in years of production use rather than a launch announcement. Capability claims are becoming table stakes; production-proven trust is not yet.

*(Updated via `outdated-checker` sweep, September 2026 — see [`sweep-2026-09.md`](./outdated-checker/sweep-2026-09.md): the [win-loss deep dive](./win-loss-analysis/win-loss-detailed-analysis.html) now gives this argument a concrete, uncomfortable number — we won only 1 of 8 head-to-head deals against NexaScore — which is why the "proof at scale" argument has to be made live, on the buyer's own data, rather than asserted. 8 deals is a small, recent sample, and the same sweep also found we're losing nearly three-quarters of deals against Conturo, the least "exciting" competitor in this book — a reminder that this narrative's real test is the boring incumbent as much as the flashy new entrant.)*

## What this is not

Not a claim that Seekridge finds more opportunities than every competitor in every scenario — that claim is not reliably defensible and erodes credibility with a technically skeptical buyer (see the [Head of Model Risk persona](./personas.md#head-of-model-risk-risk-and-model-governance-owner)). Not a customer-facing money-management app either. The narrative wins on explainability, trust, and moments that reach the banker — not a race to the longest lead list.
