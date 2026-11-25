# Buyer Personas — Seekridge

Expands the persona list in [`knowledge-base.md`](./knowledge-base.md). Where [`icp.md`](./icp.md) names *which roles* sit on a buying committee and what's generally at stake for each, this document is what those roles actually think, say, and respond to — used by prompts/skills that need to tailor tone, structure, or emphasis to who's actually reading, not just confirm they exist. See [`sales-deck-builder`](../sales-tools/sales-deck-builder), [`persona-email-sequence`](../marketing-assets/persona-email-sequence), and [`sales-call-analysis`](./sales-call-analysis) for where this gets applied.

## Who we sell to, and who we meet later

Seekridge creates opportunities, so we sell to the two people who own a growth target on the bank's existing customers. Everyone else on the committee either uses the product or can stop the deal, but none of them has a reason to buy it. Marketing, outbound and content go to the two buyers only. The others get prepared material, handed over through the buyer, at the stage where they appear.

| Role | Persona below | Who reaches them |
|---|---|---|
| **Buyer:** mortgages and refinancing | [Head of Mortgage Lending](#head-of-mortgage-lending-buyer-mortgages-and-refinancing) | Marketing and outbound |
| **Buyer:** every other loan, cards and insurance | [Head of Retail Banking](#head-of-retail-banking-buyer-consumer-loans-cards-and-insurance) | Marketing and outbound |
| User | [Advisors and relationship managers](#advisors-and-relationship-managers-users) | Through the buyer, in the pilot |
| Technical evaluator | [Data & CRM Lead](#data--crm-lead-technical-evaluator) | The rep, early, once a buyer is engaged |
| Reviewer | [Risk, model governance and data protection](#risk-model-governance-and-data-protection-reviewers) | Prepared pack, through the buyer |
| Gatekeeper | [IT Security Lead](#it-security-lead-infrastructure-gatekeeper) | The rep, when residency comes up |
| Gatekeeper | [Vendor Risk & Compliance](#vendor-risk--compliance-reviewer) | Documentation, through the buyer |

**How the two buyers relate.** In most banks the Head of Mortgage Lending reports to the Head of Retail Banking. Mortgages carry the biggest moments (refinancing from another bank, buying a home), so the Head of Mortgage Lending is usually the way in and the strongest champion. The Head of Retail Banking owns the budget once Seekridge covers more than mortgages, and at smaller banks is often the only buyer. Land with mortgages, expand into retail.

## Persona interaction map

- **Head of Mortgage Lending and Head of Retail Banking want the same thing at different scope.** The mortgage head wants refinancings kept and purchases won; the retail head wants every product line growing from the same customer base. A pilot on mortgage moments with a clear number is what earns the wider retail rollout. See the [Meridian Savings call](./sales-call-analysis/call-02-meridian-savings.md).
- **Risk and data protection review, they don't buy.** A buyer who has to make the risk case alone stalls. The rep's job is to hand the buyer what reviewers need — the evidence trail, the method, the data-processing terms — so approval happens once, not campaign by campaign. Never reach out to a reviewer directly before the buyer is convinced.
- **The Data & CRM Lead is usually an ally**, if engaged early — they want to be the one who validated the tool properly. See the [Meadowbrook Financial call](./sales-call-analysis/call-13-meadowbrook-financial.md).
- **IT Security answers to a policy or regulator, not to the deal's momentum.** Because Seekridge works with the client's transaction data, this is the one role that can end a deal everyone else wants — see the [Solvane Lending Group call](./sales-call-analysis/call-10-solvane-lending-group.md).
- **Vendor Risk & Compliance moves on its own clock**, and reacts badly to being chased directly — see the [Thornfield Mutual call](./sales-call-analysis/call-14-thornfield-mutual.md).

---

## Head of Mortgage Lending (buyer: mortgages and refinancing)

**Buying psychology:** Measured against growth and retention of the mortgage book. Success looks like "more refinancings kept, more purchases financed by us," not "audits passed." Owns the growth and workflow conversation and usually the mortgage budget; wants the risk team on board but won't make the risk case for them.

**Measured on:** Retention at fixed-rate renewal, mortgages won from other banks, new mortgages to existing customers, advisor productivity.

**Pain, in their language:** *"We find out a customer refinanced elsewhere when the redemption request arrives."* *"Half our customers have their mortgage at another bank, and we only notice when they mention it."* *"My advisors get lists every month and ignore half of them because nobody can say why a name is on there."*

**Moments they own:** refinancing elsewhere (a mortgage at another bank nearing its fixed-rate end), buying a home, rate reset on their own book.

**Decision criteria, ranked:**
1. Business impact: retained and new mortgage volume, ideally a number from their own data
2. Fit with the advisors' existing CRM workflow (minimal new steps)
3. Whether advisors will believe and act on the moments
4. A clear path through risk and data protection that doesn't depend on them arguing it

**Common objections:** "Will my advisors need retraining, and how long does that take?" · "What's the actual uplift on our customers, not the theoretical one?"

**Trust triggers:** A specific implementation timeline broken into real steps. A rep who separates "the tool goes live" from "advisors actually use it." A backtest on last year's lost refinancings.

**Trust breakers:** "Instant" or "seamless" claims without qualification. Being asked to advocate internally for the risk case themselves.

**Content preferences:** Uplift and ROI calculators, workflow diagrams, short case studies with retention and conversion numbers.

**Where they spend time:** Mortgage and lending trade publications, LinkedIn, regional banking associations.

**Seen in this repo:** [Nordkredit](./sales-call-analysis/call-01-nordkredit.md) (Lena Virtanen — a refinancing campaign that failed an internal audit, and a board audit ahead), [Meridian Savings](./sales-call-analysis/call-02-meridian-savings.md) (Julia Hoffmann — a lower competing quote, answered with the bank's own numbers), [Delta Mortgage Partners](./sales-call-analysis/call-07-delta-mortgage-partners.md) (Sophie Larsen — "instant" versus actually adopted), [Baltic Home Finance](./sales-call-analysis/call-05-baltic-home-finance.md) (Rasa Petraityte — a long-time incumbent and a market-data coverage question), [Ironbridge Bank](./sales-call-analysis/call-09-ironbridge-bank.md) (Fredrik Nilsson — a competitor rollout that underdelivered), [Solvane Lending Group](./sales-call-analysis/call-10-solvane-lending-group.md) (Karin Lindqvist — a won product case stopped by an on-prem rule), [Meadowbrook Financial](./sales-call-analysis/call-13-meadowbrook-financial.md) (Robert Yankov — evaluating with his data team).

---

## Head of Retail Banking (buyer: consumer loans, cards and insurance)

**Buying psychology:** Owns growth across everything a retail customer holds besides the mortgage: car and consumer loans, green and renovation loans, cards and card upgrades, and the insurance the bank sells (home, contents, car, payment protection). Thinks in products per customer and share of wallet. Pragmatic and numbers-led, and wary of tools that turn advisors into product pushers. At smaller savings banks and credit unions, this is usually the only buyer, and adoption is the whole question.

**Measured on:** Products per customer, consumer-lending and card volume, insurance attach rate, advisor productivity, complaints.

**Pain, in their language:** *"We finance the car and the customer insures it somewhere else the same week."* *"We can see the premium leaving the account every month and do nothing with it."* *"I've bought advisor tools before that nobody used after month one."* *"Our advisors need a reason to call, not a quota."*

**Moments they own:** a car purchase coming up, renovation and green loans, card upgrades, insured elsewhere, a new property with no home cover, salary moving away.

**Decision criteria, ranked:**
1. Evidence on their own customers: a backtest showing which customers took a product when offered at the right moment
2. Advisor adoption: value in the first session, inside the tools advisors already use
3. Fit with how each product is sold (advisor, digital journey, partner insurer)
4. Fair-treatment and consent fit: offers made because they fit the customer, never because a score said so

**Common objections:** "How is this different from the campaign lists our CRM already makes?" · "We already send an insurance mailing with every new loan." · "Our partner insurer runs its own campaigns."

**Trust triggers:** A rep who asks how each product line is sold before pitching. Evidence shown per customer, not as a portfolio average. A referral from a similar bank with a specific outcome.

**Trust breakers:** Insurer-centric language ("underwriting," "loss ratio"). Pushing volume over fit. A network-wide rollout pitched before adoption risk is addressed.

**Content preferences:** A live test on a sample of their own customers, short case studies with attach-rate and products-per-customer numbers, short demo videos, one-pagers.

**Where they spend time:** Retail-banking and savings-bank association events, banking trade press, LinkedIn.

**Seen in this repo:** [Court Street Lending](./sales-call-analysis/call-03-court-street-lending.md) (David Okafor — a formal three-vendor bake-off at a national bank), [Riverton Savings Bank](./sales-call-analysis/call-04-riverton-savings-bank.md) (Tomas Reyes — adoption risk as the real question), [Alpine Credit Union](./sales-call-analysis/call-06-alpine-credit-union.md) (Heinrich Bauer — vendor stability), [Fenwick & Oak Bank](./sales-call-analysis/call-08-fenwick-oak-bank.md) (Priya Chandra), [Crestview Capital Bank](./sales-call-analysis/call-11-crestview-capital-bank.md) (Ingrid Solberg — a national certification requirement), [Harborlight Credit Union](./sales-call-analysis/call-12-harborlight-credit-union.md) (Dana Whitfield — talked out of a low-value deal), [Thornfield Mutual](./sales-call-analysis/call-14-thornfield-mutual.md) (Grace Almeida — insurance case won, waiting on vendor risk), [Copperfield Sparkasse](./sales-call-analysis/call-15-copperfield-sparkasse.md) (Owen Marsh — a warm referral).

---

## Advisors and relationship managers (users)

Not a buyer, but the people whose behavior decides whether the purchase pays off. They want a short list of customers worth calling this week, with a reason they can say out loud. They ignore lists without reasons, and they stop opening tools that add steps. Reach them through the buyer, in the pilot: measure who calls and what closes, and use their feedback as proof for the wider rollout.

---

## Data & CRM Lead (technical evaluator)

**Buying psychology:** Wants to be the one who validated the tool properly — treating this persona as a rubber stamp is the most common way a rep loses their support. Not the decision-maker, but a deal without their early buy-in tends to stall at the procurement gate (see [`icp.md`](./icp.md)).

**Pain, in their language:** *"Every vendor's demo looks clean. I want to run it on our own customers and see where it breaks."*

**Decision criteria, ranked:**
1. Whether the evidence trail holds up on customer records they select, not a prepared demo
2. A backtest on their own past data, with a method they can scrutinize
3. Integration feasibility with the CRM and core systems they maintain

**Trust triggers:** A rep who invites a harder test than the one being requested.

**Seen in this repo:** [Meadowbrook Financial](./sales-call-analysis/call-13-meadowbrook-financial.md).

---

## Risk, model governance and data protection (reviewers)

**Who:** The Head of Credit Risk or model-risk team (any moment that leads to a credit offer, and any scoring model), and the Data Protection Officer (any use of transaction data to target offers). Not buyers: they have no target Seekridge helps them hit, and a pitch aimed at them reads as pressure.

**What they need:** For data protection — the purpose and legal basis for using transaction data, consent handling, the data-processing agreement, retention and deletion. For model risk — the method, a backtest on the bank's own data, the evidence trail per moment (which data points, how much each counted), and the audit log. For credit offers — the lending criteria behind a moment, which credit risk signs off once.

**How we reach them:** A prepared review pack the buyer takes inside, then a technical session with the rep if they ask for one. This is where "why this customer" earns its keep: it is the reason approval happens once instead of campaign by campaign.

---

## IT Security Lead (infrastructure gatekeeper)

**Buying psychology:** Answers to a data-governance policy or regulator, not the deal's momentum. Willing to end a deal everyone else wants. Sharing transaction data with a vendor puts this role in every Seekridge deal.

**Common objections:** "Does this support on-premises deployment?" · "Where specifically is our customer data processed and stored?"

**Trust triggers:** An immediate, honest "no, we don't have that" when true, followed by a concrete next step.

**Seen in this repo:** [Solvane Lending Group](./sales-call-analysis/call-10-solvane-lending-group.md) (Erik Voss — a hard on-prem requirement, handled honestly; see [`competitive-landscape.md`](./competitive-landscape.md)'s "Known gap working against us").

---

## Vendor Risk & Compliance Reviewer

Operates on an internal review clock that has nothing to do with sales urgency. Rarely objects directly — more often simply doesn't move. What helps: standard security and compliance documentation, including a data-processing agreement, handed to the champion rather than this reviewer directly, and patience calibrated to their stated timeline.

**Seen in this repo:** [Thornfield Mutual](./sales-call-analysis/call-14-thornfield-mutual.md) — the champion asked the rep not to contact compliance directly.

---

## Using personas together on one deal

A deal moves through the roles in order: a buyer first (Head of Mortgage Lending or Head of Retail Banking — the substantive decision), the Data & CRM Lead early in evaluation, risk and data protection once the buyer wants it, then IT Security and Vendor Risk & Compliance late (gates that can stop an otherwise-won deal). Treating a late IT Security objection as a product objection, or pitching a reviewer as if they were a buyer, are the two most common, avoidable mismatches.
