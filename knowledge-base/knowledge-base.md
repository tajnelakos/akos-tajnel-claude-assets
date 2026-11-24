# Knowledge Base — Parcelwise

Master source of truth for every prompt, skill, and example in this repo. Every other knowledge-base file alongside this one is a derived, deeper view of one section of this doc — kept separate so a skill can reference just the piece it needs (voice rules, competitor detail, persona psychology) instead of the whole thing.

## Company

**Parcelwise** — B2B SaaS. An AI data platform that finds new business inside a client's existing customer base. It combines three data layers:

1. **Property data** — property attributes, automated valuations, energy ratings, renovation potential
2. **Market data** — prices, listings, interest rates, local market trends
3. **The client's own customer data** — shared securely from their CRM or core systems

The platform turns these into **signals**: ranked, explained opportunities in customers the client already has. Delivered via API, CRM integration, and a web app, to banks and mortgage lenders, insurers, and real estate brokerages across Europe (core markets: DACH, Benelux, Nordics).

What a signal looks like, by segment:

- **Banks & mortgage lenders** — a customer whose fixed rate resets soon and is likely to refinance elsewhere; a homeowner with enough equity for a top-up or renovation loan; a customer likely to move and need a new mortgage.
- **Insurers** — a home whose rebuild value has outgrown its sum insured; a policyholder with no contents cover; a policy at high risk of not renewing.
- **Real estate brokerages** — a homeowner in the brokerage's own contact database who is likely to sell in the next 12 months.

- **ICP**: mid-size regional banks and mortgage lenders with a large existing customer base and a growth or retention target on it; insurers with a home/property book; secondary ICP is real estate brokerages wanting listing leads from contacts they already have.
- **Pricing**: platform subscription priced by the size of the customer base analysed, for banks and insurers; seat-based for the brokerage web app.
- **Positioning**: "opportunities you can act on — and explain," i.e. every signal shows the property, market, and customer data behind it, so advisors trust it and risk and compliance can sign off on it.

## Competitors

| Competitor | Angle |
|---|---|
| **Bricklane Data** | Cheaper, faster property data and valuation API; no customer-data layer and no explanations — sells on speed and price, leaves the signal-building to the buyer |
| **Estemate** | Legacy property-data incumbent, strong in France/Benelux, deep historical data, dated UI, slow release cycle |
| **ValuAI** | Well-funded new entrant, leads with "AI-native" propensity scoring, thin on property data depth and regulatory controls |
| **PropIQ** | Brokerage-focused seller-lead tool, doesn't really compete for bank/insurer deals but comes up in brokerage deals |

Derived: full battlecards, positioning gaps, and objection handling → [`competitive-landscape.md`](./competitive-landscape.md)

## Buyer personas

- **Head of Credit Risk** (bank risk and model-governance owner) — signs off any model that decides which customers get an offer. Cares about explainability, fair treatment, and audit trail. Skeptical of "black box AI" claims.
- **VP of Mortgage Lending** (bank economic buyer) — cares about growing and retaining the mortgage book, and about integration effort.
- **Head of Home Insurance** (insurer economic buyer) — cares about premium growth, renewal retention, and underinsurance in the book.
- **Broker Team Lead** (brokerage buyer) — cares about agent adoption and how signals turn into listings.

Derived: full buying psychology, objections, content preferences → [`personas.md`](./personas.md)

## Derived reference files

This doc is the quick summary. Everything below expands one section of it into the depth an actual skill needs:

- [`icp.md`](./icp.md) — firmographics, tiering, buying committee, in-market signals
- [`personas.md`](./personas.md) — per-persona psychology, objections, content preferences
- [`positioning.md`](./positioning.md) — narrative, differentiators, value props by segment
- [`branding-guideline/skill.md`](./branding-guideline/skill.md) — tone, style rules, anti-patterns, prohibited terms (and the rewrite skill that applies them)
- [`competitive-landscape.md`](./competitive-landscape.md) — full battlecards and positioning gaps
- [`design-system/`](./design-system) — the brand made build-ready: tokens, components, icons, motifs, and the rules for writing, LinkedIn, and video

Use this file and the ones above as the reference for names, roles, and competitive angles across every skill in this repo.
