# Reply-Handling Playbook

Nurture sequences generate replies that don't fit "book a meeting" or "unsubscribe" — a technical objection, a request to loop in someone else, a polite non-answer. This playbook maps reply types to response guidance, per persona, so a rep or SDR triaging a shared inbox doesn't have to improvise a tone match on every reply. Pairs with [`campaign-head-of-deposits-and-savings.md`](./campaign-head-of-deposits-and-savings.md) and [`campaign-head-of-retail-banking.md`](./campaign-head-of-retail-banking.md); the reply categories are the same across personas, the right response isn't.

## General rules, both personas

- **Reply within one business day.** A fast reply to an inbound response matters more than a polished one — see [`branding-guideline`](../../knowledge-base/branding-guideline/skill.md) for tone, but don't let voice-polishing delay the reply itself.
- **Never send a templated reply that ignores what they actually wrote.** Every template below is a starting point to personalize against their specific wording, not a copy-paste.
- **Stop the sequence the moment someone replies**, regardless of reply type — a scheduled Email 3 landing on top of an unresolved objection reply reads as not having read their message.
- **A reply that raises an objection is a better outcome than no reply.** Route it to the rep, don't try to fully resolve a substantive objection inside the automated sequence's reply-handling step.

---

## Head of Deposits & Savings

This persona's `personas.md` entry: owns deposit balances and their cost, sees outflows only once the balance has gone, numbers-led, wary of pitches that imply matching every competitor rate.

### "We already have a churn model."
**Read:** The most predictable objection for this persona — `personas.md` names it directly. Usually true, and usually a model that flags customers after the balance has fallen.
**Response guidance:** Don't argue the model is bad. Ask how many weeks before the balance dropped it flagged last year's outflows, and offer a backtest that answers the same question for Seekridge on the same customers. Let the two numbers sit side by side.

### "Isn't this just a rate problem?"
**Read:** A real belief, and partly right — which is why it needs a straight answer, not a pivot.
**Response guidance:** Agree that rates matter, then point to what the persona already said: matching every rate is ruinous. The moment tells the savings team who to call and why, so a rate offer goes to the customers who are actually leaving, not to everyone.

### "I've forwarded this to our risk / data-protection team."
**Read:** The sequence working as intended — risk and data protection are reviewers, and the buyer routing them in is the right order.
**Response guidance:** Send the buyer the review pack (method note, a real evidence trail, the data-processing terms, the rule that moments only describe what has already happened) to pass on, and offer to join a call if the reviewers want one. Don't contact the reviewers directly before the buyer asks you to.

### "Not the right time — we're mid-budget / just repriced our savings range."
**Read:** Often a real, specific timing constraint, not a soft no.
**Response guidance:** Ask for a specific re-engagement point rather than a generic "circle back in Q_" — then actually wait for it.

### Hard no / unsubscribe
**Response guidance:** No reply needed beyond confirming the unsubscribe request is honored. Don't send a "sorry to see you go" retention email.

---

## Head of Retail Banking

This persona's `personas.md` entry: measured on main-bank customers, products per customer and lending to existing customers, won't advocate internally for the risk/compliance case, wants a real implementation timeline rather than an "instant" claim.

### "What's the actual retraining time for my bankers?"
**Read:** A direct hit on this persona's stated common objection — answer with the real number, not a range that sounds better than it is.
**Response guidance:** Give the honest figure, broken down by what's genuinely new versus what stays the same in the existing workflow. If the honest answer is "more than a day," say that — this persona's trust trigger is explicitly "a rep who separates 'the tool goes live' from 'my team actually adopts it.'"

### "What's the real main-bank uplift, not the marketing number?"
**Response guidance:** Point to a sourced, specific figure (the same one used in Email 1) rather than restating the calculator's theoretical output — and offer a reference call with an existing retail-bank customer if one exists, since this persona's content preferences skew toward operational-metric case studies over slides.

### "Can you send this to our risk lead / send a version for compliance?"
**Read:** This is the single most important reply type for this persona — `personas.md` states directly that this buyer "won't sell this internally for them" on the risk side, so a request to loop in risk is the sequence working as intended, not a detour.
**Response guidance:** Send the review pack described in [`campaign-head-of-retail-banking.md`](./campaign-head-of-retail-banking.md)'s Email 5 for the buyer to forward, and offer to join a call with the risk contact — this removes the internal-selling burden the persona profile flags as a trust breaker, without going around the buyer.

### "We're not prioritizing this right now — our main-bank share is fine."
**Read:** Possibly a genuine low-priority moment, but per `personas.md`'s pain language ("half our 'customers' get their salary somewhere else"), this can also mean the pain is real but not yet visible to this specific person.
**Response guidance:** One light follow-up offering the banker-action data point (Email 3's angle) is reasonable if it wasn't already covered — a downstream metric this persona may not be tracking yet. Don't push past a second soft no.

### Hard no / unsubscribe
**Response guidance:** Same as Head of Deposits & Savings — honor immediately, no retention email.
