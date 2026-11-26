# Knowledge Base — Seekridge

Master source of truth for every prompt, skill, and example in this repo. Every other knowledge-base file alongside this one is a derived, deeper view of one section of this doc — kept separate so a skill can reference just the piece it needs (voice rules, competitor detail, persona psychology) instead of the whole thing.

## Company

**Seekridge** — B2B SaaS. An AI data analytics company for retail banks, built around customer moments. It reads the data a bank already has, spots what is changing in each customer's financial life, and tells the bank's own teams where the next piece of business is. It combines three data layers:

1. **The bank's transaction data** — the customer's main checking account and payment activity: salary and other income, card spend, bills and direct debits, transfers in and out, savings
2. **Customer and interaction data** — the bank's CRM and product holdings, plus what customers ask the bank's AI agent (for example, a customer asking the assistant what mortgage they could afford)
3. **Market data** — interest rates, including what other banks pay on savings, inflation, and local wage and price trends

The platform turns these into **moments**: ranked, explained business opportunities in customers the bank already has. Moments are **bank-facing** — they go to relationship managers, advisors, and the marketing and CRM teams, through CRM integration, API, and a web app, not into a customer-facing app. Seekridge sells to retail banks across Europe (core markets: DACH, Benelux, Nordics).

The first question Seekridge answers about every customer is whether the bank is their **main bank or a secondary one**. Everything else builds on it. Moments fall into four families, each with an owner — one of the two people Seekridge sells to:

- **Main-bank moments** *(owner: Head of Retail Banking)* — the bank is a customer's secondary bank and could become the main one: salary landing at another bank, everyday card spend on another bank's card, bills paid from an account elsewhere; or a salary that has just switched in.
- **Outflow moments** *(owner: Head of Deposits & Savings)* — money starting to leave: a new monthly transfer to a savings or investment account at another provider, balances drifting down, standing orders moving, a card going quiet. Sold as **Seekridge Outflow Watch**, the newest product (see the [launch plan](../marketing-assets/product-launch-process/go-to-market-outflow-watch.md)).
- **Growth moments** *(owner: Head of Retail Banking)* — a customer ready for more: rising income, a steady saving habit, money starting to go to an outside investment account, a life event (a new job, a move), or one of three bigger ones:
  - **Mortgage-ready** — income up, savings building towards a deposit, rent paid on time, and questions to the bank's AI agent about what they could borrow.
  - **Car purchase goal** — a savings pot growing towards a round target, a car loan elsewhere about to end, and questions to the AI agent about car financing or trade-in. Next step: the bank's car loan before the dealer's finance offer.
  - **Family growing** — a child has arrived: child benefit landing in the account, new regular spend at baby and children's shops, nursery or childcare fees, and the customer telling the AI agent about parental leave or a new child. One moment, with one ranked next step: a **mortgage** for a bigger home (renting, rent taking a growing share of income, savings building), a **car loan** (car questions to the AI agent, an old car loan ending), or a **renovation loan** (already owns a home, spend at DIY and building suppliers).
- **New-customer moments** *(owner: Head of Retail Banking)* — the first 90 days: a new customer whose salary hasn't switched yet, whose card is unused, or who hasn't set up a single bill.

**Moments only describe what has already happened.** Seekridge never predicts a pregnancy, a health condition or any other sensitive fact from spending. The family-growing moment fires only on evidence after a child has arrived (child benefit, childcare fees, children's spend) or on what the customer has told the bank's AI agent themselves — and, like every moment, it shows that evidence, so risk, compliance and data protection can see exactly why it fired.

A typical moment in one line: *income up 16% over three months, and EUR 400 a month now going to an outside investment account* → the bank's investment advisor calls with the bank's own savings and investment offer before the habit settles elsewhere.

- **ICP**: mid-size regional retail banks, savings banks and cooperative banks with a large existing customer base and a growth, deposit or main-bank target on it; secondary ICP is credit unions and small cooperative banks using the Seekridge web app.
- **Pricing**: platform subscription priced by the number of retail customers analysed; seat-based for the web app used by smaller banks and credit unions.
- **Positioning**: "opportunities you can act on — and explain," i.e. every moment shows the transaction, customer and market data behind it, so bankers act on it, and risk, compliance and data protection can approve the method once, not campaign by campaign.

## Competitors

| Competitor | Angle |
|---|---|
| **Ledgerline** | Cheaper, faster transaction categorisation and enrichment API; no moments and no explanations — sells on speed and price, leaves the moment-building to the bank's own data team |
| **Conturo** | Legacy banking-analytics and campaign-management incumbent, strong in France/Benelux, on-prem, deep installed base, dated UI, slow release cycle |
| **NexaScore** | Well-funded new entrant, leads with "AI-native" next-best-action scoring, thin on regulatory controls and on data depth outside standard retail accounts |
| **Pocketlens** | Customer-facing money-insights widget for banking apps; a different job (insights for the customer, not opportunities for the bank), comes up in digital-channel deals |

Derived: full battlecards, positioning gaps, and objection handling → [`competitive-landscape.md`](./competitive-landscape.md)

## Buyer personas

Seekridge sells to two buyers; everyone else is reached through them.

- **Head of Retail Banking** (buyer) — owns growth on the existing base: main-bank customers, products per customer, and lending to existing customers (mortgages, car and renovation loans). Owns the main-bank, growth and new-customer moments. Cares about business impact and integration effort.
- **Head of Deposits & Savings** (buyer, Outflow Watch) — owns deposit balances and savings growth; owns the outflow moments. Cares about money leaving before anyone notices.
- **Relationship Manager Lead** (user; the buyer for the web app at credit unions and small cooperative banks) — cares about adoption and whether moments turn into real conversations.
- **Head of Model Risk** (reviewer, with data protection) — reviews any model that decides which customers get an offer, and how transaction data may be used for it. Gets a prepared review pack through the buyer, never marketing. Cares about explainability, fair treatment, purpose limitation and audit trail.

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
