# Buyer Personas — Seekridge

Expands the persona list in [`knowledge-base.md`](./knowledge-base.md). Where [`icp.md`](./icp.md) names *which roles* sit on a buying committee and what's generally at stake for each, this document is what those roles actually think, say, and respond to — used by prompts/skills that need to tailor tone, structure, or emphasis to who's actually reading, not just confirm they exist. See [`sales-deck-builder`](../sales-tools/sales-deck-builder), [`persona-email-sequence`](../marketing-assets/persona-email-sequence), [`abm-account-brief`](../sales-tools/abm-account-brief), and [`sales-call-analysis`](./sales-call-analysis) for where this gets applied.

## How this maps to the buying committee

[`icp.md`](./icp.md)'s buying committee table names the roles. The ones with the deepest, most decision-shaping psychology get full persona treatment; the procurement role gets a shorter entry, since its behavior is more procedural than psychological — the content that would actually change a rep's approach is thinner.

| Buying committee role (per `icp.md`) | Persona below | Depth |
|---|---|---|
| Risk & model-governance owner | [Head of Credit Risk](#head-of-credit-risk-risk-and-model-governance-owner-banklender-segment) | Full |
| Economic buyer (bank/lender) | [VP of Mortgage Lending](#vp-of-mortgage-lending-economic-buyer-banklender-segment) | Full |
| Economic buyer (insurer) | [Head of Home Insurance](#head-of-home-insurance-economic-buyer-insurer-segment) | Full |
| End user / brokerage buyer | [Broker Team Lead](#broker-team-lead-brokerage-segment-seat-based-product) | Full |
| Technical evaluator | [Data & CRM Lead](#data--crm-lead-technical-evaluator) | Full |
| IT/security reviewer | [IT Security Lead](#it-security-lead-infrastructure-gatekeeper) | Full |
| Procurement / compliance | [Vendor Risk & Compliance Reviewer](#vendor-risk--compliance-reviewer) | Shorter — mostly procedural |

## Persona interaction map

A deal rarely has one persona in the room — it has several, often with real tension between them, not just different priorities in parallel:

- **Head of Credit Risk vs. VP of Mortgage Lending** is the most common live tension: lending wants more opportunities worked faster, risk wants to know why each customer was chosen, and neither will say the other's priority doesn't matter. The rep's job is to show the two aren't actually in conflict (a moment that shows its evidence *is* a moment advisors act on faster, and one risk can approve once instead of campaign by campaign), not to pick a side. See the [Meridian Savings call](../knowledge-base/sales-call-analysis/call-02-meridian-savings.md) for this playing out directly.
- **Data & CRM Lead is usually an ally, not a gatekeeper**, if engaged early — they want to be the one who validated the tool properly, and a rep who treats them as a rubber stamp loses that alliance. See the [Meadowbrook Financial call](../knowledge-base/sales-call-analysis/call-13-meadowbrook-financial.md), where the data team's own evaluation rigor became the rep's strongest lever.
- **IT Security Lead answers to a different, often invisible-until-late master**: a specific regulator or internal data-governance policy, not the deal's momentum. Because Seekridge works with the client's own customer data, they are the one persona here who can end a deal that every other stakeholder wants to close — see the [Solvane Lending Group call](../knowledge-base/sales-call-analysis/call-10-solvane-lending-group.md).
- **Vendor Risk & Compliance moves on its own clock**, largely deaf to sales urgency, and reacts badly to being chased directly rather than through the internal champion — see the [Thornfield Mutual call](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md).

---

## Head of Credit Risk (risk and model-governance owner, bank/lender segment)

**Buying psychology:** Risk-averse by function, not by personality — their job is to be the person in the room who asks "how do we defend this to a regulator." Any model that decides which customers get a lending offer lands on their desk for sign-off. Enthusiasm from other stakeholders makes them more skeptical, not less; they see their role as the check on that enthusiasm.

**Measured on:** Audit outcomes, exam findings (or absence of them), and — increasingly — how defensible the institution's automated customer decisions are under regulatory scrutiny: fair treatment, purpose limitation on customer data, model governance. Not measured on loan volume; a campaign that grows the book but can't be explained is a mark against them, not a win.

**Pain, in their language:** *"I can't tell the auditor 'the model picked them' — I need to be able to show why we contacted each customer."* *"Every vendor claims their AI is explainable. I've been burned by that claim before."* *"I don't need the cleverest model. I need the one I can defend two years from now, after whoever ran the campaign has left."*

**Decision criteria, ranked:**
1. Explainability of individual moments — which data points drove each one
2. Moment quality, validated against a method they can scrutinize (not just a headline hit rate)
3. Vendor stability and customer-data handling practices
4. Integration effort (real, but secondary to the above)

**Common objections:** "How is this different from [prior vendor]'s explainability claim that didn't hold up?" · "What happens to our customer data if we leave you?" · "Show me a moment that turned out wrong and how the evidence trail explained it."

**Trust triggers:** A vendor who volunteers a live run on the bank's own data, unprompted. A vendor who says "we don't know, let me find out" rather than an immediate confident answer. A specific, named method detail rather than a general claim.

**Trust breakers:** Any claim that sounds identical to a prior vendor's claim that didn't hold up — this persona has usually been burned once already and pattern-matches hard against repeat offenses. Overclaiming moment accuracy without a disclosed method. Being asked to just "trust the model."

**Content preferences:** Method whitepapers, live runs on their own data over slides, peer references from similarly-regulated institutions. Actively distrusts case studies without a named, checkable source.

**Where they spend time:** Risk/compliance-focused LinkedIn groups, industry risk conferences, trade publications — not general SaaS/martech content channels.

**Seen in this repo:** [Nordkredit](../knowledge-base/sales-call-analysis/call-01-nordkredit.md) (Lena Virtanen — the clean, textbook version of this persona's mandate), [Court Street Lending](../knowledge-base/sales-call-analysis/call-03-court-street-lending.md) (David Okafor — the same psychology under a formal competitive bake-off), [Crestview Capital Bank](../knowledge-base/sales-call-analysis/call-11-crestview-capital-bank.md) (Ingrid Solberg — a regulatory-certification variant of the same core need for defensibility).

---

## VP of Mortgage Lending (economic buyer, bank/lender segment)

**Buying psychology:** Measured against growth and retention of the mortgage book, not risk metrics — success looks like "more refinancings kept, more top-up loans written," not "audits passed." Will defer to the Head of Credit Risk on explainability but owns the growth and workflow conversation, and usually the budget.

**Measured on:** Retention at rate reset, new lending to existing customers, advisor productivity. A tool that's more defensible but produces fewer usable opportunities is, from this persona's KPIs alone, a regression — which is exactly why the tension with Head of Credit Risk (see the interaction map above) is real, not manufactured.

**Pain, in their language:** *"We find out a customer refinanced elsewhere when the redemption request arrives."* *"My advisors get lists every month and ignore half of them because nobody can say why a name is on there."* *"I need my risk team on board, but I'm not going to sell this internally for them."*

**Decision criteria, ranked:**
1. Business impact — retained volume or new lending, ideally with a specific number from their own data
2. Fit with the advisors' existing CRM workflow (minimal new steps)
3. Whether advisors will actually believe and act on the moments
4. Alignment with what Credit Risk has already approved (won't fight that battle themselves)

**Common objections:** "Will my advisors need retraining, and how long does that take?" · "What's the actual uplift on our customers, not the theoretical one?"

**Trust triggers:** A specific, credible implementation timeline broken into real steps, not a marketing "instant" claim. A rep who separates "the tool goes live" from "my advisors actually use it" — this persona has been burned by vendors conflating the two.

**Trust breakers:** Being told competitor timelines are "instant" or "seamless" without qualification — this persona knows enough about their own workflow to smell an oversimplified claim. Being asked to advocate internally for the risk/compliance case themselves.

**Content preferences:** Uplift and ROI calculators, workflow diagrams, short case studies focused on retention and conversion metrics.

**Where they spend time:** Mortgage/lending trade publications, LinkedIn, regional banking associations.

**Seen in this repo:** [Meridian Savings](../knowledge-base/sales-call-analysis/call-02-meridian-savings.md) (Julia Hoffmann — the split-committee dynamic with Credit Risk, explicitly acknowledged mid-call), [Delta Mortgage Partners](../knowledge-base/sales-call-analysis/call-07-delta-mortgage-partners.md) (Sophie Larsen — the "instant vs. actually adopted" distinction surfacing directly against a Bricklane claim).

---

## Head of Home Insurance (economic buyer, insurer segment)

**Buying psychology:** Owns premium growth and retention on the home book, and knows the book is quietly drifting: rebuild costs have risen faster than sums insured, and policies lapse at renewal without anyone calling. Pragmatic, numbers-led, and wary of "AI" pitches that ignore how insurance distribution actually works (brokers, tied agents, direct).

**Measured on:** Gross written premium, renewal retention, cross-sell rate (home + contents), and exposure from underinsured properties.

**Pain, in their language:** *"Half our book was priced on rebuild values from before construction costs jumped."* *"We only learn a policyholder was unhappy when they don't renew."* *"Our agents need a reason to call, not a list."*

**Decision criteria, ranked:**
1. Evidence on their own book — a backtest showing underinsurance and lapse risk the insurer didn't already know about
2. Property-data depth (rebuild value, construction type, energy rating) in their regions
3. How moments reach agents and brokers, not just the head-office team
4. Data-handling and consent fit with insurance regulation

**Common objections:** "We already have a renewal model." · "How do you know the rebuild value better than our underwriters?"

**Trust triggers:** A rep who asks how distribution works at this insurer before pitching. Property evidence shown per policy, not as a portfolio average.

**Trust breakers:** Bank-centric language ("loans," "origination") — it moments the vendor doesn't know insurance. Reference customers who are all banks.

**Content preferences:** A backtest on a sample of their own book, short case studies with premium and retention numbers, one-pagers for distribution leaders.

**Where they spend time:** Insurance trade publications, national insurance association events, LinkedIn.

**Seen in this repo:** [Thornfield Mutual](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md) (Grace Almeida — product case won, deal waiting on the vendor-risk queue).

---

## Broker Team Lead (brokerage segment, seat-based product)

**Buying psychology:** Adoption-driven — the purchase only succeeds if agents actually use it, so they weigh "will my team bother opening this" as heavily as feature fit.

**Measured on:** Listing win rate, agent productivity, and — quietly — whether their last few tool purchases actually got used. A Broker Team Lead who's been burned by low adoption before will interrogate onboarding harder than price.

**Pain, in their language:** *"I've bought agent tools before that nobody used after month one."* *"I need something that tells agents who's about to sell, not another dashboard to check."* *"Half my team barely uses the advanced features of what we already have."*

**Decision criteria, ranked:**
1. Agent adoption / ease of use (low friction to get value in first session)
2. Direct tie to winning listings (does a seller moment turn into a listing appointment)
3. Price relative to per-seat value
4. Onboarding/support quality

**Common objections:** "How is this different from what's built into our CRM already?" · "What's the learning curve for a non-technical agent?"

**Trust triggers:** A rep who asks about the team's actual tech-comfort spread rather than assuming uniform ease of adoption. A referral from another brokerage with a specific, credible outcome (not a generic testimonial).

**Trust breakers:** A rep pushing a full-team rollout before adoption risk has been addressed. Feature-first pitches that don't address who on the team will actually open the tool.

**Content preferences:** Short demo videos, agent testimonials, simple one-pagers — not whitepapers.

**Where they spend time:** Real estate industry Facebook/LinkedIn groups, brokerage conferences, YouTube (agent-focused channels).

**Seen in this repo:** [Riverton Brokers](../knowledge-base/sales-call-analysis/call-04-riverton-brokers.md) (Tomas Reyes — adoption risk correctly identified as the real question, not the mobile feature gap itself), [Harborlight Brokerages](../knowledge-base/sales-call-analysis/call-12-harborlight-brokerages.md) (Dana Whitfield — a case where the rep correctly talked *out of* a low-value deal), [Copperfield Estates](../knowledge-base/sales-call-analysis/call-15-copperfield-estates.md) (Owen Marsh — a warm-referral case where adoption risk was already resolved by someone else's track record).

---

## Data & CRM Lead (technical evaluator)

**Buying psychology:** Wants to be the one who validated the tool properly — treating this persona as a rubber-stamp step rather than a real technical reviewer is the single most common way a rep loses their support. They are usually not the final decision-maker, but a deal without their early buy-in tends to stall later at the procurement gate even if the economic buyer is enthusiastic (see [`icp.md`](./icp.md)).

**Pain, in their language:** *"I don't want to be the person who signed off on a model that fell apart in front of an examiner."* *"Every vendor's demo looks clean. I want to run it on our own customers and see where it breaks."*

**Decision criteria, ranked:**
1. Whether the evidence trail holds up under a live test on customer records they select, not a prepared demo
2. A backtest on their own past data, with a method they can actually scrutinize
3. Integration feasibility with the CRM and core systems they maintain
4. Whether the vendor treats their scrutiny as legitimate rather than an obstacle

**Common objections:** "Can we run this on customers we pick, not ones you've prepared?" · "What's the actual method, not the score?"

**Trust triggers:** A rep who invites a harder test than the one being requested. Being asked what evidence bar *they* think is fair, rather than being told what the evidence is.

**Trust breakers:** A rep who only offers prepared demo material when asked for something live. Any hint that their technical questions are an inconvenience.

**Seen in this repo:** [Meadowbrook Financial](../knowledge-base/sales-call-analysis/call-13-meadowbrook-financial.md) — the data team whose own evaluation rigor (noting they hadn't tested any vendor's evidence trail live yet) became the strongest argument in the room, once invited rather than resisted.

---

## IT Security Lead (infrastructure gatekeeper)

**Buying psychology:** Not swayed by product enthusiasm from other stakeholders — answers to a data-governance policy or regulator, not the deal's momentum. Genuinely willing to end a deal everyone else wants, and doesn't experience that as a loss. Sharing customer data with a vendor puts this persona at the center of every Seekridge deal.

**Pain, in their language:** *"That's not a small gap for us — it's a hard requirement, not a nice-to-have."* *"I've had vendors dodge this question before, so directness helps."*

**Decision criteria, ranked:**
1. Where customer data is processed and stored, against a specific regulatory requirement
2. Access control, pseudonymization, and audit-logging architecture
3. Whether the vendor gives a direct yes/no rather than a deflection

**Common objections:** "Does this support on-premises deployment?" · "Where specifically is our customer data processed and stored?"

**Trust triggers:** An immediate, honest "no, we don't have that" when true, followed by a concrete next step (e.g. a compliance/infrastructure technical call) rather than a soft pivot.

**Trust breakers:** Any vendor response that reframes a hard requirement as a soft preference. A generic "we take security seriously" non-answer.

**Seen in this repo:** [Solvane Lending Group](../knowledge-base/sales-call-analysis/call-10-solvane-lending-group.md) (Erik Voss — a hard on-prem requirement stated plainly, handled honestly by the rep rather than talked around; see [`competitive-landscape.md`](./competitive-landscape.md)'s "Known gap working against us").

---

## Vendor Risk & Compliance Reviewer

**Buying psychology:** Operates on an internal review clock that has nothing to do with sales urgency — typically a queue-based process with its own timeline, largely independent of how convinced the economic buyer already is.

**Pain, in their language:** *"New vendor approvals move slowly here — I don't have much ability to expedite it."*

**Decision criteria, ranked:**
1. Standard security/compliance documentation completeness, including a data-processing agreement
2. Precedent — has a similar vendor been approved before
3. Absence of direct pressure from the vendor (a vendor reaching out directly can read as pressure, not helpfulness)

**Common objections:** Rarely objects directly — more often simply doesn't move, which reads as an objection if misdiagnosed as one.

**What actually helps:** Pre-prepared standard documentation handed to the internal champion, not this reviewer directly. Patience calibrated to their actual stated timeline, not repeated check-ins.

**Seen in this repo:** [Thornfield Mutual](../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md) — the champion (Grace Almeida) explicitly asked the rep not to contact compliance directly, and the deal's only open variable was this internal queue, not a product objection.

---

## Using personas together on one deal

Most real deals engage two or three of these personas at once, not one at a time — the practical skill is knowing which one is actually blocking progress at a given moment, since the answer changes across a deal's lifecycle: Data & CRM Lead early (technical validation), Head of Credit Risk and VP of Mortgage Lending (or Head of Home Insurance) in the middle (the substantive decision, often in tension with each other), then IT Security and Vendor Risk & Compliance late (gates that can kill an otherwise-won deal). Treating a late-stage IT Security objection as if it were a Head of Credit Risk objection — i.e., trying to win it on explainability — is a common, avoidable mismatch.
