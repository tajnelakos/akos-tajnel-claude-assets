# Reply-Handling Playbook

Nurture sequences generate replies that don't fit "book a meeting" or "unsubscribe" — a technical objection, a request to loop in someone else, a polite non-answer. This playbook maps reply types to response guidance, per persona, so a rep or SDR triaging a shared inbox doesn't have to improvise a tone match on every reply. Pairs with [`campaign-head-of-retail-banking.md`](./campaign-head-of-retail-banking.md) and [`campaign-head-of-mortgage-lending.md`](./campaign-head-of-mortgage-lending.md); the reply categories are the same across personas, the right response isn't.

## General rules, both personas

- **Reply within one business day.** A fast reply to an inbound response matters more than a polished one — see [`branding-guideline`](../../knowledge-base/branding-guideline/skill.md) for tone, but don't let voice-polishing delay the reply itself.
- **Never send a templated reply that ignores what they actually wrote.** Every template below is a starting point to personalize against their specific wording, not a copy-paste.
- **Stop the sequence the moment someone replies**, regardless of reply type — a scheduled Email 3 landing on top of an unresolved objection reply reads as not having read their message.
- **A reply that raises an objection is a better outcome than no reply.** Route it to the rep, don't try to fully resolve a substantive objection inside the automated sequence's reply-handling step.

---

## Head of Retail Banking

This persona's `personas.md` entry: owns growth across consumer loans, cards and insurance, thinks in products per customer, and is wary of anything that turns advisors into product pushers. Advisor adoption is their second-ranked criterion.

### "Can you show this on our customers, not a demo?"
**Read:** A genuine evaluation step, not stalling — matches the persona's stated content preference: a live test on a sample of their own customers.
**Response guidance:** Offer the backtest or a live sample run with a concrete date and what you need from them (an anonymised extract, a contact on the data side). Don't send a generic case study in its place.

### "We tried something like this — advisors stopped using it."
**Read:** Adoption is this persona's second-ranked criterion in `personas.md`, so expect this one often.
**Response guidance:** Ask what made advisors stop (too many leads, no reason given, a separate tool) and answer that specific failure mode: moments arrive in the CRM they already use, a short list, with the reason attached. A generic "ours is different" answer pattern-matches as exactly the claim they're sceptical of.

### "I've forwarded this to our data / CRM team to take a look."
**Read:** A good sign, not a brush-off — per `personas.md`'s persona interaction map, the Data & CRM Lead is usually an ally if engaged early.
**Response guidance:** Offer to loop in directly with the data contact rather than waiting, and treat their technical questions as legitimate scrutiny, not an obstacle.

### "Risk / the DPO will need to look at this first."
**Read:** Normal, not a stall. Reviewers are reached through the buyer, not marketed to.
**Response guidance:** Send the prepared review pack (data used, how moments are explained, model governance notes) to the buyer to forward, and offer a joint session with the reviewer. Don't start a separate sales sequence aimed at the reviewer.

### Hard no / unsubscribe
**Response guidance:** No reply needed beyond confirming the unsubscribe request is honored. Don't send a "sorry to see you go" retention email.

---

## Head of Mortgage Lending

This persona's `personas.md` entry: measured on growth and retention of the mortgage book, won't advocate internally for the risk/compliance case, wants a real implementation timeline rather than an "instant" claim.

### "What's the actual retraining time for my advisors?"
**Read:** A direct hit on this persona's stated common objection — answer with the real number, not a range that sounds better than it is.
**Response guidance:** Give the honest figure, broken down by what's genuinely new versus what stays the same in the existing workflow. If the honest answer is "more than a day," say that — this persona's trust trigger is explicitly "a rep who separates 'the tool goes live' from 'my team actually adopts it.'"

### "What's the real retention uplift, not the marketing number?"
**Response guidance:** Point to a sourced, specific figure (the same one used in Email 1) rather than restating the calculator's theoretical output — and offer a reference call with an existing lending customer if one exists, since this persona's content preferences skew toward operational-metric case studies over slides.

### "Can you send this to our risk lead / send a version for compliance?"
**Read:** This is the single most important reply type for this persona — `personas.md` states directly that this buyer "won't sell this internally for them" on the risk side, so a request to loop in risk is the sequence working as intended, not a detour.
**Response guidance:** Send the prepared review pack, offer the joint walkthrough described in [`campaign-head-of-mortgage-lending.md`](./campaign-head-of-mortgage-lending.md)'s Email 5, and reach out to the risk contact directly rather than routing everything back through the buyer — this removes exactly the internal-selling burden the persona profile flags as a trust breaker if left on them.

### "We're not prioritizing this right now — retention is fine."
**Read:** Possibly a genuine low-priority moment, but per `personas.md`'s pain language ("we find out a customer refinanced elsewhere when the redemption request arrives"), this can also mean the pain is real but not yet visible to this specific person.
**Response guidance:** One light follow-up offering the advisor-action data point (Email 3's angle) is reasonable if it wasn't already covered — a downstream metric this persona may not be tracking yet. Don't push past a second soft no.

### Hard no / unsubscribe
**Response guidance:** Same as Head of Retail Banking — honor immediately, no retention email.
