# Buyer Personas — Seekridge

Expands the persona list in [`knowledge-base.md`](./knowledge-base.md). Where [`icp.md`](./icp.md) names *which roles* sit on a buying committee and what's generally at stake for each, this document is what those roles actually think, say, and respond to — used by prompts/skills that need to tailor tone, structure, or emphasis to who's actually reading, not just confirm they exist. See [`sales-deck-builder`](../sales-tools/sales-deck-builder), [`persona-email-sequence`](../marketing-assets/persona-email-sequence), [`one-pager-builder`](../marketing-assets/one-pager-builder), and [`sales-call-analysis`](./sales-call-analysis) for where this gets applied.

## How this maps to the buying committee

[`icp.md`](./icp.md)'s buying committee table names the roles. The ones with the deepest, most decision-shaping psychology get full persona treatment; the procurement role gets a shorter entry, since its behavior is more procedural than psychological — the content that would actually change a rep's approach is thinner.

| Buying committee role (per `icp.md`) | Persona below | Depth |
|---|---|---|
| Risk & model-governance owner | [Head of Model Risk](#head-of-model-risk-risk-and-model-governance-owner) | Full |
| Economic buyer (growth on the base) | [Head of Retail Banking](#head-of-retail-banking-economic-buyer) | Full |
| Economic buyer (Outflow Watch) | [Head of Deposits & Savings](#head-of-deposits--savings-economic-buyer-outflow-watch) | Full |
| End user / Tier 3 buyer | [Relationship Manager Lead](#relationship-manager-lead-end-user-lead-tier-3-buyer) | Full |
| Technical evaluator | [Data & CRM Lead](#data--crm-lead-technical-evaluator) | Full |
| IT/security reviewer | [IT Security Lead](#it-security-lead-infrastructure-gatekeeper) | Full |
| Procurement / compliance | [Vendor Risk & Compliance Reviewer](#vendor-risk--compliance-reviewer) | Shorter — mostly procedural |

## Persona interaction map

A deal rarely has one persona in the room — it has several, often with real tension between them, not just different priorities in parallel:

- **Head of Model Risk vs. Head of Retail Banking** is the most common live tension: retail wants more opportunities worked faster, risk wants to know why each customer was chosen and whether their transactions may be used that way, and neither will say the other's priority doesn't matter. The rep's job is to show the two aren't actually in conflict (a moment that shows its evidence *is* a moment bankers act on faster, and one risk can approve once instead of campaign by campaign), not to pick a side. See the [Meridian Savings call](../knowledge-base/sales-call-analysis/call-02-meridian-savings.md) for this playing out directly.
- **Data & CRM Lead is usually an ally, not a gatekeeper**, if engaged early — they want to be the one who validated the tool properly, and a rep who treats them as a rubber stamp loses that alliance. See the [Meadowbrook Financial call](../knowledge-base/sales-call-analysis/call-13-meadowbrook-financial.md), where the data team's own evaluation rigor became the rep's strongest lever.
- **IT Security Lead answers to a different, often invisible-until-late master**: a specific regulator or internal data-governance policy, not the deal's momentum. Because Seekridge works with the bank's own transaction data, they are the one persona here who can end a deal that every other stakeholder wants to close — see the [Solvane Bank Group call](../knowledge-base/sales-call-analysis/call-10-solvane-bank-group.md).
- **Vendor Risk & Compliance moves on its own clock**, largely deaf to sales urgency, and reacts badly to being chased directly rather than through the internal champion — see the [Thornfield Mutual call](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md).

---

## Head of Model Risk (risk and model-governance owner)

**Buying psychology:** Risk-averse by function, not by personality — their job is to be the person in the room who asks "how do we defend this to a regulator." Any model that decides which customers get an offer lands on their desk for sign-off, and so does any new use of customers' transaction data. Enthusiasm from other stakeholders makes them more skeptical, not less; they see their role as the check on that enthusiasm.

**Measured on:** Audit outcomes, exam findings (or absence of them), and — increasingly — how defensible the bank's automated customer decisions are under regulatory scrutiny: fair treatment, purpose limitation on transaction data, profiling rules, model governance. Not measured on sales volume; a campaign that grows deposits but can't be explained is a mark against them, not a win.

**Pain, in their language:** *"I can't tell the auditor 'the model picked them' — I need to be able to show why we contacted each customer, and which of their transactions we used."* *"Every vendor claims their AI is explainable. I've been burned by that claim before."* *"I don't need the cleverest model. I need the one I can defend two years from now, after whoever ran the campaign has left."*

**Decision criteria, ranked:**
1. Explainability of individual moments — which data points drove each one
2. Moment quality, validated against a method they can scrutinize (not just a headline hit rate)
3. Vendor stability and transaction-data handling practices
4. Integration effort (real, but secondary to the above)

**Common objections:** "Are you inferring anything sensitive from spending — a pregnancy, a health condition?" (No: moments only describe what has already happened, such as child benefit arriving or the customer telling the AI agent; see the family-growing moment in [`knowledge-base.md`](./knowledge-base.md)) · "How is this different from [prior vendor]'s explainability claim that didn't hold up?" · "What happens to our customers' transaction data if we leave you?" · "Show me a moment that turned out wrong and how the evidence trail explained it."

**Trust triggers:** A vendor who volunteers a live run on the bank's own data, unprompted. A vendor who says "we don't know, let me find out" rather than an immediate confident answer. A specific, named method detail rather than a general claim.

**Trust breakers:** Any claim that sounds identical to a prior vendor's claim that didn't hold up — this persona has usually been burned once already and pattern-matches hard against repeat offenses. Overclaiming moment accuracy without a disclosed method. Being asked to just "trust the model."

**Content preferences:** Method whitepapers, live runs on their own data over slides, peer references from similarly-regulated banks. Actively distrusts case studies without a named, checkable source.

**Where they spend time:** Risk/compliance-focused LinkedIn groups, industry risk conferences, trade publications — not general SaaS/martech content channels.

**Seen in this repo:** [Nordkredit](../knowledge-base/sales-call-analysis/call-01-nordkredit.md) (Lena Virtanen — the clean, textbook version of this persona's mandate), [Court Street Bank](../knowledge-base/sales-call-analysis/call-03-court-street-bank.md) (David Okafor — the same psychology under a formal competitive bake-off), [Crestview Capital Bank](../knowledge-base/sales-call-analysis/call-11-crestview-capital-bank.md) (Ingrid Solberg — a regulatory-certification variant of the same core need for defensibility).

---

## Head of Retail Banking (economic buyer)

**Buying psychology:** Measured against growth on the existing customer base, not risk metrics — success looks like "more customers who use us as their main bank, more products per customer, more lending to customers we already have," not "audits passed." Will defer to the Head of Model Risk on explainability but owns the growth and workflow conversation, and usually the budget.

**Measured on:** Main-bank customers (salary credited here), products per customer, lending and investment sales to existing customers — mortgages, car loans and renovation loans included — and banker productivity. A tool that's more defensible but produces fewer usable opportunities is, from this persona's KPIs alone, a regression — which is exactly why the tension with Head of Model Risk (see the interaction map above) is real, not manufactured.

**Pain, in their language:** *"Half our 'customers' get their salary somewhere else — we're the account they keep for the mortgage."* *"We find out a customer took a mortgage elsewhere when the rent payments stop."* *"A family has a baby, buys a bigger car on the dealer's finance, and we never knew."* *"My bankers get lists every month and ignore half of them because nobody can say why a name is on there."* *"I need my risk team on board, but I'm not going to sell this internally for them."*

**Decision criteria, ranked:**
1. Business impact — main-bank conversions, products per customer or new lending, ideally with a specific number from their own data
2. Fit with the bankers' existing CRM workflow (minimal new steps)
3. Whether bankers will actually believe and act on the moments
4. Alignment with what Model Risk has already approved (won't fight that battle themselves)

**Common objections:** "Will my bankers need retraining, and how long does that take?" · "What's the actual uplift on our customers, not the theoretical one?"

**Trust triggers:** A specific, credible implementation timeline broken into real steps, not a marketing "instant" claim. A rep who separates "the tool goes live" from "my bankers actually use it" — this persona has been burned by vendors conflating the two.

**Trust breakers:** Being told competitor timelines are "instant" or "seamless" without qualification — this persona knows enough about their own workflow to smell an oversimplified claim. Being asked to advocate internally for the risk/compliance case themselves.

**Content preferences:** Uplift and ROI calculators, workflow diagrams, short case studies focused on main-bank and cross-sell metrics.

**Where they spend time:** Retail-banking trade publications, LinkedIn, regional and savings-bank associations.

**Seen in this repo:** [Meridian Savings](../knowledge-base/sales-call-analysis/call-02-meridian-savings.md) (Julia Hoffmann — the split-committee dynamic with Model Risk, explicitly acknowledged mid-call), [Delta Direct Bank](../knowledge-base/sales-call-analysis/call-07-delta-direct-bank.md) (Sophie Larsen — the "instant vs. actually adopted" distinction surfacing directly against a Ledgerline claim).

---

## Head of Deposits & Savings (economic buyer, Outflow Watch)

**Buying psychology:** Owns deposit balances and savings growth, and knows the money is quietly drifting: customers keep their checking account here but send a monthly amount to a better-paying savings account or an investment app elsewhere, and nobody calls. Pragmatic, numbers-led, and wary of "AI" pitches that ignore how small and gradual outflows really are.

**Measured on:** Deposit balances and their cost, savings product growth, outflows to other providers, and retention of high-balance customers.

**Pain, in their language:** *"We see the money leave when the balance is already gone."* *"It's never one big transfer. It's EUR 300 a month to someone paying a point more."* *"Matching every rate is ruinous — I need to know who to call, not raise the rate for everyone."*

**Decision criteria, ranked:**
1. Evidence on their own data — a backtest showing outflows the bank didn't see coming
2. How early a moment appears — weeks before the balance falls, not after
3. How moments reach bankers and the savings team, not just head office
4. Data-handling and purpose-limit fit with data-protection rules

**Common objections:** "We already have a churn model." · "Isn't this just a rate problem?"

**Trust triggers:** A rep who asks how the bank prices savings and who decides retention offers before pitching. Transaction evidence shown per customer, not as a portfolio average.

**Trust breakers:** Lending-only language ("loans," "origination") — it signals the vendor doesn't know the deposit side. A pitch that implies matching every competitor rate.

**Content preferences:** A backtest on a sample of their own past outflows, short case studies with deposit and retention numbers, one-pagers for savings and treasury leaders.

**Where they spend time:** Banking trade publications, treasury and ALM events, LinkedIn.

**Seen in this repo:** [Thornfield Mutual](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md) (Grace Almeida — product case won, deal waiting on the vendor-risk queue).

---

## Relationship Manager Lead (end-user lead, Tier 3 buyer)

**Buying psychology:** Adoption-driven — at a credit union or small cooperative bank they hold the budget and the team that has to use the tool, so they weigh "will my bankers bother opening this" as heavily as feature fit.

**Measured on:** Conversations that turn into products, member or customer retention, banker productivity, and — quietly — whether their last few tool purchases actually got used. A Relationship Manager Lead who's been burned by low adoption before will interrogate onboarding harder than price.

**Pain, in their language:** *"I've bought tools before that nobody used after month one."* *"I need something that tells my bankers who to call this week, not another dashboard to check."* *"Half my team barely uses the advanced features of what we already have."*

**Decision criteria, ranked:**
1. Banker adoption / ease of use (low friction to get value in the first session)
2. Direct tie to real conversations (does a moment turn into a meeting and a product)
3. Price relative to per-seat value
4. Onboarding/support quality

**Common objections:** "How is this different from what's built into our core system already?" · "What's the learning curve for a banker who isn't technical?"

**Trust triggers:** A rep who asks about the team's actual tech-comfort spread rather than assuming uniform ease of adoption. A referral from another credit union with a specific, credible outcome (not a generic testimonial).

**Trust breakers:** A rep pushing a full-team rollout before adoption risk has been addressed. Feature-first pitches that don't address who on the team will actually open the tool.

**Content preferences:** Short demo videos, banker testimonials, simple one-pagers — not whitepapers.

**Where they spend time:** Credit-union and cooperative-bank associations, regional meetups, LinkedIn.

**Seen in this repo:** [Riverton Credit Union](../knowledge-base/sales-call-analysis/call-04-riverton-credit-union.md) (Tomas Reyes — adoption risk correctly identified as the real question, not the mobile feature gap itself), [Harborlight Credit Union](../knowledge-base/sales-call-analysis/call-12-harborlight-credit-union.md) (Dana Whitfield — a case where the rep correctly talked *out of* a low-value deal), [Copperfield Cooperative Bank](../knowledge-base/sales-call-analysis/call-15-copperfield-cooperative-bank.md) (Owen Marsh — a warm-referral case where adoption risk was already resolved by someone else's track record).

---

## Data & CRM Lead (technical evaluator)

**Buying psychology:** Wants to be the one who validated the tool properly — treating this persona as a rubber-stamp step rather than a real technical reviewer is the single most common way a rep loses their support. They are usually not the final decision-maker, but a deal without their early buy-in tends to stall later at the procurement gate even if the economic buyer is enthusiastic (see [`icp.md`](./icp.md)).

**Pain, in their language:** *"I don't want to be the person who signed off on a model that fell apart in front of an examiner."* *"Every vendor's demo looks clean. I want to run it on our own customers and see where it breaks."* *"Our transaction categorisation is messy — show me what you do with it, not a clean sample."*

**Decision criteria, ranked:**
1. Whether the evidence trail holds up under a live test on customer records they select, not a prepared demo
2. A backtest on their own past data, with a method they can actually scrutinize
3. Integration feasibility with the CRM, core system and transaction feed they maintain
4. Whether the vendor treats their scrutiny as legitimate rather than an obstacle

**Common objections:** "Can we run this on customers we pick, not ones you've prepared?" · "What's the actual method, not the score?"

**Trust triggers:** A rep who invites a harder test than the one being requested. Being asked what evidence bar *they* think is fair, rather than being told what the evidence is.

**Trust breakers:** A rep who only offers prepared demo material when asked for something live. Any hint that their technical questions are an inconvenience.

**Seen in this repo:** [Meadowbrook Financial](../knowledge-base/sales-call-analysis/call-13-meadowbrook-financial.md) — the data team whose own evaluation rigor (noting they hadn't tested any vendor's evidence trail live yet) became the strongest argument in the room, once invited rather than resisted.

---

## IT Security Lead (infrastructure gatekeeper)

**Buying psychology:** Not swayed by product enthusiasm from other stakeholders — answers to a data-governance policy or regulator, not the deal's momentum. Genuinely willing to end a deal everyone else wants, and doesn't experience that as a loss. Sharing transaction data with a vendor puts this persona at the center of every Seekridge deal.

**Pain, in their language:** *"That's not a small gap for us — it's a hard requirement, not a nice-to-have."* *"I've had vendors dodge this question before, so directness helps."*

**Decision criteria, ranked:**
1. Where customer and transaction data is processed and stored, against a specific regulatory requirement
2. Access control, pseudonymization, and audit-logging architecture
3. Whether the vendor gives a direct yes/no rather than a deflection

**Common objections:** "Does this support on-premises deployment?" · "Where specifically is our transaction data processed and stored?"

**Trust triggers:** An immediate, honest "no, we don't have that" when true, followed by a concrete next step (e.g. a compliance/infrastructure technical call) rather than a soft pivot.

**Trust breakers:** Any vendor response that reframes a hard requirement as a soft preference. A generic "we take security seriously" non-answer.

**Seen in this repo:** [Solvane Bank Group](../knowledge-base/sales-call-analysis/call-10-solvane-bank-group.md) (Erik Voss — a hard on-prem requirement stated plainly, handled honestly by the rep rather than talked around; see [`competitive-landscape.md`](./competitive-landscape.md)'s "Known gap working against us").

---

## Vendor Risk & Compliance Reviewer

**Buying psychology:** Operates on an internal review clock that has nothing to do with sales urgency — typically a queue-based process with its own timeline, largely independent of how convinced the economic buyer already is. Often includes the data protection officer, who reviews the purpose and legal basis for using transaction data.

**Pain, in their language:** *"New vendor approvals move slowly here — I don't have much ability to expedite it."*

**Decision criteria, ranked:**
1. Standard security/compliance documentation completeness, including a data-processing agreement and a data-protection impact assessment
2. Precedent — has a similar vendor been approved before
3. Absence of direct pressure from the vendor (a vendor reaching out directly can read as pressure, not helpfulness)

**Common objections:** Rarely objects directly — more often simply doesn't move, which reads as an objection if misdiagnosed as one.

**What actually helps:** Pre-prepared standard documentation handed to the internal champion, not this reviewer directly. Patience calibrated to their actual stated timeline, not repeated check-ins.

**Seen in this repo:** [Thornfield Mutual](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md) — the champion (Grace Almeida) explicitly asked the rep not to contact compliance directly, and the deal's only open variable was this internal queue, not a product objection.

---

## Using personas together on one deal

Most real deals engage two or three of these personas at once, not one at a time — the practical skill is knowing which one is actually blocking progress at a given moment, since the answer changes across a deal's lifecycle: Data & CRM Lead early (technical validation), Head of Model Risk and Head of Retail Banking (or Head of Deposits & Savings) in the middle (the substantive decision, often in tension with each other), then IT Security and Vendor Risk & Compliance late (gates that can kill an otherwise-won deal). Treating a late-stage IT Security objection as if it were a Head of Model Risk objection — i.e., trying to win it on explainability — is a common, avoidable mismatch.
