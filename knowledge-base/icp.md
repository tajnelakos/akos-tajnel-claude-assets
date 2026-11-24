# Ideal Customer Profile — Parcelwise

Used by prompts/skills that need to reason about fit or in-market signals rather than have it re-explained inline every time. See [`knowledge-base.md`](./knowledge-base.md) for the company overview. Consumed most directly by [`icp-buying-signal-monitor`](../sales-tools/icp-buying-signal-monitor) (scoring incoming signals) and [`abm-account-brief`](../sales-tools/abm-account-brief) (placing a named account in the tiering below).

## Firmographic & technographic criteria

The tiering below is the quick reference. These are the underlying dimensions it's built from — useful when a real account doesn't cleanly match one tier's row and needs to be reasoned about directly.

| Dimension | What we're actually checking | Why it matters |
|---|---|---|
| Size of the existing book | Mortgage book (banks/lenders), number of home policies (insurers) — a proxy for how many opportunities sit in the customer base and for subscription size | Below ~€200M annual mortgage origination or ~50,000 home policies, procurement overhead usually exceeds the deal's value to us |
| Ownership structure | Public bank, private bank, mutual/cooperative, non-bank lender, or insurer | Mutuals and cooperatives often have slower, consensus-driven procurement — factor into sales cycle estimates, not a disqualifier |
| Dedicated risk / model-governance function | Does a named person or team own model risk and data-use sign-off, separate from sales and lending ops | No dedicated risk function usually means no one is asking "why was this customer chosen" — the explainability wedge doesn't land |
| CRM / core system openness | Modern CRM with documented APIs (e.g. Salesforce, Dynamics) vs. legacy core system with batch-only exports | Drives implementation timeline more than company size does — signals have to land where advisors already work |
| Data residency posture | Cloud-accepting vs. hard on-prem/data-residency requirement for customer data | See [`competitive-landscape.md`](./competitive-landscape.md)'s "Known gap working against us" — this alone can end an otherwise well-fit deal, and sharing customer data makes it come up more often than it did for property data alone |
| Existing approach to finding opportunities in the base | Another data/scoring vendor, rule-based CRM campaigns, or an in-house model | In-house-built is a longer, more skeptical sales cycle — see Anti-ICP below |

## Tiered customer profiles

| | Tier 1 (best fit) | Tier 2 | Tier 3 (opportunistic) |
|---|---|---|---|
| **Segment** | Regional banks & mortgage lenders; regional and mutual home insurers | National/multi-region lenders and insurers | Real estate brokerages |
| **Book size** | €200M–€2B annual mortgage origination; 50,000–500,000 home policies | €2B+ origination or 500,000+ policies (longer sales cycle, more procurement layers) | N/A — seat-based, not book-based |
| **Geography** | DACH, Benelux | Nordics, wider EU | DACH, Benelux |
| **CRM / core system** | Modern CRM with open APIs | Legacy core systems, heavier integration lift | Any CRM (Parcelwise's brokerage product is standalone) |
| **Regulatory posture** | Subject to periodic reviews of how customer data and models are used, actively modernizing | Subject to reviews, slower to change vendors | Not regulator-facing |
| **Sales cycle** | 2–4 months | 6–12 months | 3–6 weeks |
| **Typical buying committee size** | 3–4 people | 5–8 people, often with a separate vendor-risk gate | 1–2 people |
| **Expected first-year contract value** | Mid five figures to low six figures (subscription) | Low-to-mid six figures | Low five figures (seat-based) |

Tier 1 is the focus for outbound and content strategy — best combination of pain intensity (a growth target on the existing base, plus a risk team asking how customers are chosen) and reachable buying committee size. Tier 2 converts at a similar rate but takes roughly 3x longer, so it's worth pursuing opportunistically (inbound, warm signal) rather than as the primary outbound target. Tier 3 is a different motion entirely — see [`positioning.md`](./positioning.md)'s segment-specific value propositions.

Insurers are a newer segment: the fit criteria are the same, but there are fewer live reference customers, so expect a backtest on the insurer's own book to carry more of the proof.

## Regional nuances

Firmographic fit doesn't travel evenly across our three core regions — worth checking before assuming a Tier 1 account behaves like another Tier 1 account just because the numbers match.

| Region | Regulatory environment | Typical incumbent | Notes |
|---|---|---|---|
| **DACH** | Multiple national regulators, rigorous data-protection and model-governance expectations | Mixed — no single dominant incumbent | Our strongest region; most Tier 1 pattern-matches come from here |
| **Benelux** | Similar rigor to DACH, smaller total addressable market | Estemate has the deepest incumbency (see [`competitive-landscape.md`](./competitive-landscape.md)) | Switching-cost objections are more common here than elsewhere — see the Estemate battlecard |
| **Nordics** | Strong digital-infrastructure baseline, generally cloud-accepting | More fragmented, no entrenched incumbent | Property-data coverage depth is a genuine open question in smaller Nordic-adjacent markets — see the note in the Anti-ICP section below |

## Buying committee (Tier 1, bank/lender deals)

| Role | Typical title | Stake |
|---|---|---|
| Economic buyer | VP of Mortgage Lending / Head of Retail Banking | Owns the growth and retention target on the existing base, and usually the budget |
| Risk & model-governance owner | Chief Risk Officer / Head of Credit Risk | Signs off any model that decides which customers get an offer; often holds a veto and sometimes co-owns budget |
| Technical evaluator | Data & CRM Lead / data team | Backtests signal quality on the bank's own data and validates CRM integration |
| End user | Mortgage advisor / relationship manager | Works the signals daily, cares about whether they're believable and fit the workflow |
| IT/security reviewer | IT Security Lead / Infrastructure | Gates on data residency, customer-data sharing, access controls — usually only blocks, rarely champions (see [`competitive-landscape.md`](./competitive-landscape.md)'s on-prem gap) |
| Procurement / compliance | Vendor risk / Compliance / Data protection officer | Gates the deal on data handling, SLAs, certifications — usually enters late |
| Economic sponsor (Tier 2 only) | CFO or COO | At larger accounts, a second budget-holder above the lending or risk lead — usually silent unless contract value crosses an internal threshold |

At insurers, the Head of Home Insurance (or Head of Distribution) takes the economic-buyer seat, and the risk seat is usually held by a Chief Risk Officer or actuarial lead — the rest of the committee looks the same.

A deal without early technical evaluator buy-in tends to stall at the procurement gate later, even if the economic buyer is enthusiastic — worth surfacing this in deck/outline prompts (see [`sales-deck-builder`](../sales-tools/sales-deck-builder)). At Tier 2 specifically, the IT/security reviewer and procurement stage are where deals actually die or stall — the product conversation is rarely the blocker once the economic buyer is convinced (see [`staleness-detection`](../knowledge-base/staleness-detection)'s general pattern of process gates outlasting product objections).

## Anti-ICP: who this isn't for

Fit criteria work better with explicit disqualifiers alongside them — a lead that superficially matches the tiering table but fails one of these is a poor use of a rep's time regardless of firmographic score.

- **No dedicated risk or model-governance function.** If nobody owns the question "why was this customer chosen," there's no one to champion explainability internally — the core wedge has no owner on the buyer's side.
- **Hard, non-negotiable on-prem requirement with no cloud-acceptance path.** Not every on-prem requirement is equally hard (see [`competitive-landscape.md`](./competitive-landscape.md) — some regulators accept a well-documented cloud architecture); but where it's genuinely non-negotiable, this is disqualifying today, not a longer sales cycle.
- **Deep in-house build with organizational investment in it.** A bank that built its own propensity models in-house isn't buying better models — they're defending a decision. This is a different (and usually much longer, politically harder) sale than displacing a third-party vendor.
- **Recently signed a multi-year contract with a competitor, with no trigger event.** Worth staying in [`competitor-monitoring`](../sales-tools/competitor-monitoring)'s peripheral vision, but not worth active pursuit until something changes — see the nurture pattern in the [sales-call-analysis rollup](../knowledge-base/sales-call-analysis/call-analysis-summary.html)'s Ironbridge Bank example.
- **Markets where our property-data coverage is genuinely thin.** Smaller or newer regional markets should be confirmed, not assumed — see the Baltic Home Finance example in [`sales-call-analysis`](../knowledge-base/sales-call-analysis/call-05-baltic-home-finance.md), where this was correctly treated as a hard blocking question rather than smoothed over.
- **Brokerages wanting general agent productivity or CRM features, not seller signals.** That's a different product (and largely PropIQ's actual turf, not ours) — see [`positioning.md`](./positioning.md) on where the brokerage value proposition does and doesn't extend.

## Fit scoring (for prioritization, not a hard gate)

A simple way to translate the above into a single ranking when several accounts are competing for attention:

| Factor | Strong (+2) | Medium (+1) | Weak (0) |
|---|---|---|---|
| Tier | Tier 1 | Tier 2 | Tier 3 without a specific trigger |
| Dedicated risk / model-governance function | Confirmed, named owner | Implied, not confirmed | Absent |
| Data residency | Cloud-accepting, confirmed | Unconfirmed | Hard on-prem, confirmed |
| In-market signal (see below) | Strong | Medium | None yet |

Anything scoring 0 on data residency is a hold regardless of the total score — see Anti-ICP above. This isn't a formula to automate a decision, just a way to compare two live opportunities quickly when time is the constraint, not judgment.

## External signals that indicate a company is in-market

Signal strength here matches the taxonomy [`icp-buying-signal-monitor`](../sales-tools/icp-buying-signal-monitor) uses, so scoring stays consistent between this reference doc and the tool that operationalizes it.

**Strong signals**
- New Head of Credit Risk, Chief Risk Officer, or Head of Home Insurance hire within the last 2 quarters (frequently a mandate-holder for modernization)
- A recent adverse audit or compliance finding about how customer data or models were used in campaigns, or a public statement about an upcoming regulatory review
- A job posting for a CRM analytics, customer-data, or model-governance role that names a specific legacy tool (signals dissatisfaction or planned migration)

**Medium signals**
- CRM or core-system migration announced or underway — data and signal tooling often gets revisited alongside it
- Executive turnover at a company using a known competitor (new leadership frequently re-evaluates inherited vendor choices)
- Public growth or retention targets on the existing customer base ("grow share of wallet," "reduce churn at renewal"), without a specific tooling reference

**Weak / not yet actionable**
- Generic hiring growth with no risk- or data-function specificity
- A company simply existing within Tier 1/2 firmographics with no dated trigger at all

**Negative signals worth noting explicitly**
- A recently completed (not just started) implementation of a competitor's tool — the account is likely to be an Anti-ICP "recently signed" case for the next 12–18 months regardless of how well it otherwise fits
- Public statements emphasizing cost-cutting or vendor-consolidation initiatives, without an accompanying growth or risk driver — these tend to favor Bricklane's price-led pitch over an explainability-led one (see [`competitive-landscape.md`](./competitive-landscape.md))

These signals feed the [`competitor-monitoring`](../sales-tools/competitor-monitoring) brief and outbound targeting — not a hard qualification checklist, but a prioritization signal.

## Expansion motion: once an account is live

The ICP for expanding within an existing customer is different from the new-logo ICP above — the account has already cleared procurement and technical validation, so the relevant signals are usage-based, not firmographic.

- **New business line or geography added by the customer** — a bank entering a new lending product or region, or adding its insurance arm, is a natural trigger to add signal types, not a new sale.
- **A brokerage or insurance arm evaluating tools separately from the lending side** — see the recurring pattern in [`competitive-landscape.md`](./competitive-landscape.md) of a bank customer's other arms being distinct, separately-sold opportunities.
- **Advisor headcount or customer-base growth within a live account** — subscription pricing by base size means this is a natural, low-friction expansion conversation rather than a renegotiation.
- **A near-miss on-prem or coverage objection that's since been resolved** (e.g. a new market's property-data coverage was confirmed after initially being a blocker) — worth a proactive follow-up rather than waiting for the customer to notice.

## Worked examples

Accounts already documented elsewhere in this repo, shown against the tiering above:

- **[Nordkredit](../knowledge-base/sales-call-analysis/call-01-nordkredit.md)** — Tier 1: regional Nordic lender, ~€600M annual origination, a new Head of Credit Risk hire and a real audit finding driving urgency. A clean pattern match, which is why it's used as the primary example throughout this repo's [`icp-buying-signal-monitor`](../sales-tools/icp-buying-signal-monitor) → [`abm-account-brief`](../sales-tools/abm-account-brief) → [`personalized-outbound`](../marketing-assets/personalized-outbound) pipeline.
- **[Court Street Lending](../knowledge-base/sales-call-analysis/call-03-court-street-lending.md)** — Tier 2: €5B+ national lender. Longer cycle, more procurement layers, and a vendor-stability objection that doesn't come up at Tier 1 — consistent with the buying-committee table above.
- **[Solvane Lending Group](../knowledge-base/sales-call-analysis/call-10-solvane-lending-group.md)** — a Tier 2 firmographic fit that hit the Anti-ICP on-prem disqualifier directly, mid-deal. A real instance of a fit score being overridden by a hard gate, not a hypothetical.
- **[Thornfield Mutual](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md)** — Tier 2 insurer (~620,000 home policies): a mutual home insurer where the product case was already won and the only open variable was the vendor-risk queue.
