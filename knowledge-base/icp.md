# Ideal Customer Profile — Seekridge

Used by prompts/skills that need to reason about fit or in-market moments rather than have it re-explained inline every time. See [`knowledge-base.md`](./knowledge-base.md) for the company overview. Consumed most directly by [`sales-deck-builder`](../sales-tools/sales-deck-builder) (placing a deal in the tiering below), [`competitor-monitoring`](../sales-tools/competitor-monitoring) and [`win-loss-analysis`](./win-loss-analysis).

## Firmographic & technographic criteria

The tiering below is the quick reference. These are the underlying dimensions it's built from — useful when a real account doesn't cleanly match one tier's row and needs to be reasoned about directly.

| Dimension | What we're actually checking | Why it matters |
|---|---|---|
| Size of the retail customer base | Number of active retail customers with a checking account at the bank — a proxy for how many moments sit in the base and for subscription size | Below ~200,000 active retail customers, procurement overhead usually exceeds the deal's value to us — those banks fit the web app (Tier 3) instead |
| Ownership structure | Public bank, private bank, savings bank, cooperative bank, building society or credit union | Cooperatives, savings banks and mutuals often have slower, consensus-driven procurement — factor into sales cycle estimates, not a disqualifier |
| Dedicated risk / model-governance function | Does a named person or team own model risk and data-use sign-off, separate from retail and marketing | No dedicated risk function usually means no one is asking "why was this customer chosen" — the explainability wedge doesn't land |
| CRM / core system openness | Modern CRM with documented APIs (e.g. Salesforce, Dynamics) and a transaction feed vs. legacy core system with batch-only exports | Drives implementation timeline more than bank size does — moments have to land where bankers already work |
| Data residency posture | Cloud-accepting vs. hard on-prem/data-residency requirement for customer and transaction data | See [`competitive-landscape.md`](./competitive-landscape.md)'s "Known gap working against us" — this alone can end an otherwise well-fit deal, and sharing transaction data makes it come up in almost every deal |
| Existing approach to finding opportunities in the base | Another data/scoring vendor, rule-based CRM campaigns, or an in-house model | In-house-built is a longer, more skeptical sales cycle — see Anti-ICP below |

## Tiered customer profiles

| | Tier 1 (best fit) | Tier 2 | Tier 3 (opportunistic) |
|---|---|---|---|
| **Segment** | Regional retail banks, savings banks and cooperative banks | National/multi-region retail banks and digital banks | Credit unions and small cooperative banks |
| **Customer base** | 200,000–3M active retail customers | 3M+ active retail customers (longer sales cycle, more procurement layers) | Under 200,000 — seat-based web app, not base-based |
| **Geography** | DACH, Benelux | Nordics, wider EU | DACH, Benelux |
| **CRM / core system** | Modern CRM with open APIs and a daily transaction feed | Legacy core systems, heavier integration lift | Any — the web app works from a secure file feed, no CRM integration |
| **Regulatory posture** | Subject to periodic reviews of how customer data and models are used, actively modernizing | Subject to reviews, slower to change vendors | Lighter review, but still data-protection bound |
| **Sales cycle** | 2–4 months | 6–12 months | 3–6 weeks |
| **Typical buying committee size** | 3–4 people | 5–8 people, often with a separate vendor-risk gate | 1–2 people |
| **Expected first-year contract value** | Mid five figures to low six figures (subscription) | Low-to-mid six figures | Low five figures (seat-based) |

Tier 1 is the focus for outbound and content strategy — best combination of pain intensity (a growth, deposit or main-bank target on the existing base, plus a risk team asking how customers are chosen) and reachable buying committee size. Tier 2 converts at a similar rate but takes roughly 3x longer, so it's worth pursuing opportunistically (inbound, warm moment) rather than as the primary outbound target. Tier 3 is a different motion entirely — see [`positioning.md`](./positioning.md)'s persona-specific value propositions.

Seekridge Outflow Watch is the newest product: the fit criteria are the same, but there are fewer live reference customers, so expect a backtest on the bank's own past outflows to carry more of the proof.

## Regional nuances

Firmographic fit doesn't travel evenly across our three core regions — worth checking before assuming a Tier 1 account behaves like another Tier 1 account just because the numbers match.

| Region | Regulatory environment | Typical incumbent | Notes |
|---|---|---|---|
| **DACH** | Multiple national regulators, rigorous data-protection and model-governance expectations; strong savings-bank and cooperative-bank groups | Mixed — no single dominant incumbent | Our strongest region; most Tier 1 pattern-matches come from here |
| **Benelux** | Similar rigor to DACH, smaller total addressable market | Conturo has the deepest incumbency (see [`competitive-landscape.md`](./competitive-landscape.md)) | Switching-cost objections are more common here than elsewhere — see the Conturo battlecard |
| **Nordics** | Strong digital-infrastructure baseline, generally cloud-accepting, high card and mobile-payment use | More fragmented, no entrenched incumbent | Merchant-categorisation coverage for local payment schemes is a genuine open question in smaller Nordic-adjacent and Baltic markets — see the note in the Anti-ICP section below |

## Buying committee (Tier 1)

| Role | Typical title | Stake |
|---|---|---|
| Economic buyer | Head of Retail Banking (or Head of Deposits & Savings, for Outflow Watch) | Owns the growth, deposit or main-bank target on the existing base, and usually the budget |
| Risk & model-governance owner | Chief Risk Officer / Head of Model Risk | Signs off any model that decides which customers get an offer; often holds a veto and sometimes co-owns budget |
| Technical evaluator | Data & CRM Lead / data team | Backtests moment quality on the bank's own data and validates the CRM and transaction-feed integration |
| End user | Relationship manager / advisor | Works the moments daily, cares about whether they're believable and fit the workflow |
| IT/security reviewer | IT Security Lead / Infrastructure | Gates on data residency, transaction-data sharing, access controls — usually only blocks, rarely champions (see [`competitive-landscape.md`](./competitive-landscape.md)'s on-prem gap) |
| Procurement / compliance | Vendor risk / Compliance / Data protection officer | Gates the deal on data handling, purpose limits, SLAs, certifications — usually enters late |
| Economic sponsor (Tier 2 only) | CFO or COO | At larger accounts, a second budget-holder above the retail or risk lead — usually silent unless contract value crosses an internal threshold |

At Tier 3, the Relationship Manager Lead usually holds the budget and the end-user seat at once, with a compliance officer reviewing data handling.

A deal without early technical evaluator buy-in tends to stall at the procurement gate later, even if the economic buyer is enthusiastic — worth surfacing this in deck/outline prompts (see [`sales-deck-builder`](../sales-tools/sales-deck-builder)). At Tier 2 specifically, the IT/security reviewer and procurement stage are where deals actually die or stall — the product conversation is rarely the blocker once the economic buyer is convinced (see [`outdated-checker`](../knowledge-base/outdated-checker)'s general pattern of process gates outlasting product objections).

## Anti-ICP: who this isn't for

Fit criteria work better with explicit disqualifiers alongside them — a lead that superficially matches the tiering table but fails one of these is a poor use of a rep's time regardless of firmographic score.

- **No dedicated risk or model-governance function.** If nobody owns the question "why was this customer chosen," there's no one to champion explainability internally — the core wedge has no owner on the buyer's side.
- **Hard, non-negotiable on-prem requirement with no cloud-acceptance path.** Not every on-prem requirement is equally hard (see [`competitive-landscape.md`](./competitive-landscape.md) — some regulators accept a well-documented cloud architecture); but where it's genuinely non-negotiable, this is disqualifying today, not a longer sales cycle.
- **Deep in-house build with organizational investment in it.** A bank that built its own next-best-action models in-house isn't buying better models — they're defending a decision. This is a different (and usually much longer, politically harder) sale than displacing a third-party vendor.
- **Recently signed a multi-year contract with a competitor, with no trigger event.** Worth staying in [`competitor-monitoring`](../sales-tools/competitor-monitoring)'s peripheral vision, but not worth active pursuit until something changes — see the nurture pattern in the [sales-call-analysis rollup](../knowledge-base/sales-call-analysis/call-analysis-summary.html)'s Ironbridge Bank example.
- **Markets where our merchant-categorisation coverage is genuinely thin.** Smaller or newer regional markets, with local card schemes and merchants, should be confirmed, not assumed — see the Baltic Savings Bank example in [`sales-call-analysis`](../knowledge-base/sales-call-analysis/call-05-baltic-savings-bank.md), where this was correctly treated as a hard blocking question rather than smoothed over.
- **Banks wanting a customer-facing money-management app, not bank-facing moments.** That's a different product (and largely Pocketlens' actual turf, not ours) — see [`positioning.md`](./positioning.md) on where the value proposition does and doesn't extend.

## Fit scoring (for prioritization, not a hard gate)

A simple way to translate the above into a single ranking when several accounts are competing for attention:

| Factor | Strong (+2) | Medium (+1) | Weak (0) |
|---|---|---|---|
| Tier | Tier 1 | Tier 2 | Tier 3 without a specific trigger |
| Dedicated risk / model-governance function | Confirmed, named owner | Implied, not confirmed | Absent |
| Data residency | Cloud-accepting, confirmed | Unconfirmed | Hard on-prem, confirmed |
| In-market moment (see below) | Strong | Medium | None yet |

Anything scoring 0 on data residency is a hold regardless of the total score — see Anti-ICP above. This isn't a formula to automate a decision, just a way to compare two live opportunities quickly when time is the constraint, not judgment.

## External moments that indicate a bank is in-market

**Strong moments**
- New Head of Model Risk, Chief Risk Officer, Head of Retail Banking or Head of Deposits hire within the last 2 quarters (frequently a mandate-holder for modernization)
- A recent adverse audit or compliance finding about how customer or transaction data was used in campaigns, or a public statement about an upcoming regulatory review
- A job posting for a CRM analytics, customer-data, or model-governance role that names a specific legacy tool (dissatisfaction or planned migration)

**Medium moments**
- CRM or core-system migration announced or underway — data and moment tooling often gets revisited alongside it
- Executive turnover at a bank using a known competitor (new leadership frequently re-evaluates inherited vendor choices)
- Public growth, deposit or main-bank targets on the existing customer base ("grow main-bank customers," "defend deposits," "more products per customer"), without a specific tooling reference
- A visible deposit-rate fight in the bank's market — competitors or digital banks paying noticeably more on savings

**Weak / not yet actionable**
- Generic hiring growth with no risk- or data-function specificity
- A bank simply existing within Tier 1/2 firmographics with no dated trigger at all

**Negative moments worth noting explicitly**
- A recently completed (not just started) implementation of a competitor's tool — the account is likely to be an Anti-ICP "recently signed" case for the next 12–18 months regardless of how well it otherwise fits
- Public statements emphasizing cost-cutting or vendor-consolidation initiatives, without an accompanying growth or risk driver — these tend to favor Ledgerline's price-led pitch over an explainability-led one (see [`competitive-landscape.md`](./competitive-landscape.md))

These moments feed the [`competitor-monitoring`](../sales-tools/competitor-monitoring) brief and outbound targeting — not a hard qualification checklist, but a prioritization aid.

## Expansion motion: once an account is live

The ICP for expanding within an existing customer is different from the new-logo ICP above — the account has already cleared procurement and technical validation, so the relevant moments are usage-based, not firmographic.

- **A new moment family added** — a bank live on main-bank and growth moments adding Outflow Watch is the most natural expansion, not a new sale.
- **A new business line or geography added by the customer** — a bank adding small-business banking or a new region is a trigger to add moment types.
- **Banker headcount or customer-base growth within a live account** — subscription pricing by base size means this is a natural, low-friction expansion conversation rather than a renegotiation.
- **A near-miss on-prem or coverage objection that's since been resolved** (e.g. a new market's merchant-categorisation coverage was confirmed after initially being a blocker) — worth a proactive follow-up rather than waiting for the customer to notice.

## Worked examples

Accounts already documented elsewhere in this repo, shown against the tiering above:

- **[Nordkredit](../knowledge-base/sales-call-analysis/call-01-nordkredit.md)** — Tier 1: regional Nordic retail bank, ~900,000 retail customers, a new Head of Model Risk hire and a real audit finding driving urgency. A clean pattern match, which is why it's used as the primary example throughout this repo, ending as the [Nordkredit case study](../marketing-assets/case-study-builder/case-study-nordkredit.html).
- **[Court Street Bank](../knowledge-base/sales-call-analysis/call-03-court-street-bank.md)** — Tier 2: national bank, 5M+ retail customers. Longer cycle, more procurement layers, and a vendor-stability objection that doesn't come up at Tier 1 — consistent with the buying-committee table above.
- **[Solvane Bank Group](../knowledge-base/sales-call-analysis/call-10-solvane-bank-group.md)** — a Tier 2 firmographic fit that hit the Anti-ICP on-prem disqualifier directly, mid-deal. A real instance of a fit score being overridden by a hard gate, not a hypothetical.
- **[Thornfield Mutual](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md)** — Tier 2 mutual savings bank (~3.4M savers) and the first Outflow Watch deal: the product case was already won and the only open variable was the vendor-risk queue.
