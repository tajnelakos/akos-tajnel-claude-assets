# Knowledge Base — Seekridge

Master source of truth for every prompt, skill, and example in this repo. Every other knowledge-base file alongside this one is a derived, deeper view of one section of this doc — kept separate so a skill can reference just the piece it needs (voice rules, competitor detail, persona psychology) instead of the whole thing.

## Company

**Seekridge** — B2B SaaS. An AI data analytics company for retail banks, built around customer moments: it finds new business and early churn inside a bank's existing customer base. It reads three data layers:

1. **The bank's transaction data** — current-account and card activity: salary and other income coming in, standing orders and direct debits going out, saving habits, payments to other banks and providers
2. **The bank's CRM and product data** — products held, loan and savings terms, contact history and consent
3. **Market data** — interest rates, competitor offers and price trends

The platform turns these into **moments**: ranked, explained opportunities in customers the bank already has. Delivered via API, CRM integration, and a web app, to retail banks and mortgage lenders across Europe (core markets: DACH, Benelux, Nordics).

What a moment looks like:

- **Keep the relationship** — a customer whose salary is now partly paid into another bank, on the way to making you their secondary bank; a customer whose fixed rate ends soon while market rates are lower, likely to refinance elsewhere.
- **Win business held elsewhere** — a mortgage, savings or loan payment going to another provider every month, ready to be brought over.
- **Grow with the customer** — income that has risen steadily, ready for a better account, card or credit line; cash building up in the current account, ready for savings or investment; deposits and rent payments that point to a first home purchase; payments to builders and hardware stores that point to a renovation loan.
- **Insurance as a bank product (bancassurance)** — premiums paid to another insurer every month, or a newly financed car or home with no cover, ready for the bank's own insurance offer.
- **Care moments** — overdraft use rising month on month: a customer to help early, before arrears (fair treatment, and good risk practice).

- **ICP**: mid-size regional retail banks and mortgage lenders with a large existing customer base and a growth or retention target on it. Insurance is sold through the bank (bancassurance), not to insurers directly.
- **Pricing**: platform subscription priced by the number of customers analysed.
- **Positioning**: "opportunities you can act on — and explain," i.e. every moment shows the transaction, CRM and market data behind it, so advisors trust it and risk and compliance can sign off on it.

## Competitors

| Competitor | Angle |
|---|---|
| **Ledgerlight** | Cheaper, faster transaction-categorisation and enrichment API; no moments and no explanations — sells on speed and price, leaves the moment-building to the bank |
| **Kontora** | Legacy banking-analytics and campaign-management incumbent, strong in DACH and Benelux, deep core-banking integrations, dated UI, slow release cycle |
| **Propensa** | Well-funded new entrant, leads with "AI-native" next-best-offer propensity scoring, thin on explanations and regulatory controls |
| **Nudgely** | In-app money-insights widget sent straight to the bank's end customers; competes for the digital-banking budget rather than the advisor-led one, and comes up mainly in digital-first banks |

Derived: full battlecards, positioning gaps, and objection handling → [`competitive-landscape.md`](./competitive-landscape.md)

## Buyer personas

- **Head of Credit Risk** (bank risk and model-governance owner) — signs off any model that decides which customers get an offer. Cares about explainability, fair treatment, and audit trail. Skeptical of "black box AI" claims.
- **VP of Mortgage Lending** (bank economic buyer) — cares about growing and retaining the mortgage book, and about integration effort.
- **Head of Bancassurance** (bank economic buyer for insurance) — cares about insurance attach rates, premiums placed with other insurers, and advisor time.
- **Data & CRM Lead** (technical evaluator) — cares about data access, integration effort and whether the method holds up.
- **Head of Advisory Network** (buyer at smaller savings banks and credit unions) — cares about advisor adoption and whether moments turn into appointments.

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
- [`flyer-design-system/`](./flyer-design-system) — Seekridge in print: trifold, postcard and one-pager system with print tokens, components, copy and pre-press rules, and print-ready examples
- [`video-design-system/`](./video-design-system) — the brand on film: the film book, film tokens and components, product UI references, reference films, and the film-builder skill

Use this file and the ones above as the reference for names, roles, and competitive angles across every skill in this repo.
