# Knowledge Base — Seekridge

Master source of truth for every prompt, skill, and example in this repo. Every other knowledge-base file alongside this one is a derived, deeper view of one section of this doc — kept separate so a skill can reference just the piece it needs (voice rules, competitor detail, persona psychology) instead of the whole thing.

## Company

**Seekridge** — B2B SaaS. An AI data analytics company for retail banks, built around customer moments: it finds new business and early churn inside a bank's existing customer base. It reads three data layers:

1. **The bank's transaction data** — current-account and card activity: salary and other income coming in, standing orders and direct debits going out, saving habits, payments to other banks and providers
2. **The bank's CRM and product data** — products held, loan and savings terms, contact history and consent
3. **Market data** — interest rates, competitor offers and price trends

The platform turns these into **moments**: ranked, explained opportunities in customers the bank already has. Delivered via API, CRM integration, and a web app, to retail banks and mortgage lenders across Europe (core markets: DACH, Benelux, Nordics).

What a moment looks like, grouped by the buyer who owns it:

**Mortgage lending (Head of Mortgage Lending)**
- **Refinancing elsewhere** — a mortgage payment going to another lender every month, or a fixed rate ending soon while market rates are lower, ready to be brought over or kept.
- **Buying a home** — deposits building up and rent payments that point to a first home purchase.
- **Growing family** — baby-related payments, and mentions in chats with the bank's AI assistant, pointing to a bigger home (mortgage), a bigger car or a renovation.

**Retail banking (Head of Retail Banking)**
- **Buying a car** — a car purchase coming up, ready for the bank's car loan before a dealer's finance offer.
- **Renovating** — payments to builders and hardware stores, and savings set aside, ready for a renovation or green loan.
- **Card upgrade** — income that has risen steadily, ready for a better card or credit line.
- **Insured elsewhere (bancassurance)** — premiums paid to another insurer every month, or a newly financed car or home with no cover, ready for the bank's own insurance offer.
- **Keep the relationship** — salary now partly paid into another bank, or cash building up with no savings product.
- **Care moments** — overdraft use rising month on month: a customer to help early, before arrears (fair treatment, and good risk practice).

- **ICP**: mid-size regional retail banks and mortgage lenders with a large existing customer base and a growth or retention target on it. Insurance is sold through the bank (bancassurance), not to insurers directly.
- **Pricing**: platform subscription priced by the number of customers analysed.
- **Positioning**: growth from customers the bank already has — every moment shows the transaction, CRM and market data behind it, so advisors act on it, and the method is approved by risk and compliance once, not campaign by campaign.
- **Buyers**: Head of Mortgage Lending (mortgages, refinancing) and Head of Retail Banking (car and green loans, card upgrades, insurance). Reviewers are reached through them — see [`personas.md`](./personas.md).

## Competitors

| Competitor | Angle |
|---|---|
| **Ledgerlight** | Cheaper, faster transaction-categorisation and enrichment API; no moments and no explanations — sells on speed and price, leaves the moment-building to the bank |
| **Kontora** | Legacy banking-analytics and campaign-management incumbent, strong in DACH and Benelux, deep core-banking integrations, dated UI, slow release cycle |
| **Propensa** | Well-funded new entrant, leads with "AI-native" next-best-offer propensity scoring, thin on explanations and regulatory controls |
| **Nudgely** | In-app money-insights widget sent straight to the bank's end customers; competes for the digital-banking budget rather than the advisor-led one, and comes up mainly in digital-first banks |

Derived: full battlecards, positioning gaps, and objection handling → [`competitive-landscape.md`](./competitive-landscape.md)

## Buyer personas

We sell to two buyers, both measured on growth from the bank's existing customers:

- **Head of Mortgage Lending** — owns mortgages and refinancing: retention at fixed-rate renewal, mortgages won from other banks, new mortgages to existing customers. Usually the entry point.
- **Head of Retail Banking** — owns every other product a retail customer holds: car and consumer loans, green and renovation loans, cards and card upgrades, and insurance sold through the bank. The budget owner once Seekridge covers more than mortgages, and often the only buyer at smaller banks.

Others we meet during a deal but don't market to: advisors (the users), the Data & CRM Lead (technical evaluator), risk and model governance and the Data Protection Officer (reviewers), IT Security and Vendor Risk (gatekeepers). They get prepared material through the buyer.

Derived: full buying psychology, objections, content preferences → [`personas.md`](./personas.md)

## Derived reference files

This doc is the quick summary. Everything below expands one section of it into the depth an actual skill needs:

- [`icp.md`](./icp.md) — firmographics, tiering, buying committee, in-market moments
- [`personas.md`](./personas.md) — per-persona psychology, objections, content preferences
- [`positioning.md`](./positioning.md) — narrative, differentiators, value props by segment
- [`branding-guideline/skill.md`](./branding-guideline/skill.md) — tone, style rules, anti-patterns, prohibited terms (and the rewrite skill that applies them)
- [`competitive-landscape.md`](./competitive-landscape.md) — full battlecards and positioning gaps
- [`design-system/`](./design-system) — the brand made build-ready: tokens, components, icons, motifs, and the rules for writing, LinkedIn, and video
- [`linkedin-carousels/`](./linkedin-carousels) — the LinkedIn carousel design system: seven formats and a slide kit, slide tokens and CSS, assets, fonts, wording and caption rules, and a carousel-building skill
- [`flyer-design-system/`](./flyer-design-system) — Seekridge in print: trifold (flyer) and one-pager system with print tokens, components, copy and pre-press rules, and print-ready examples
- [`video-design-system/`](./video-design-system) — the brand on film: the film book, film tokens and components, product UI references, reference films, and the film-builder skill

Use this file and the ones above as the reference for names, roles, and competitive angles across every skill in this repo.
