# Deep-Dive Campaign — Head of Retail Banking

A full 5-email, A/B-tested campaign for the bank's economic buyer, run against a 260-contact segment. Results: [`campaign-metrics.csv`](./campaign-metrics.csv) (raw sends) and [`campaign-performance-analysis.html`](./campaign-performance-analysis.html) (what the data actually says). See [`personas.md`](../../knowledge-base/personas.md#head-of-retail-banking-economic-buyer) for the persona this is built from.

**Trigger:** used the retention-uplift calculator on the site.

**A/B design note:** same structure as the [Head of Model Risk campaign](./campaign-head-of-model-risk.md) — Variant A states the point declaratively with a specific number where one exists, Variant B leads with a direct question naming the cost of inaction. **Variant A won on every tracked metric for this persona** — the opposite result from the Head of Model Risk campaign, where the question framing won. Don't read "provocative questions win" or "declarative numbers win" as a universal rule from either result in isolation — see the analysis for why the same technique cuts opposite ways for these two personas.

---

### Email 1 — Day 0

**Variant A:** "The retention number lenders like you actually hit"
**Variant B:** "How many customers refinanced elsewhere last quarter?"

You ran the numbers on our calculator, so you've already seen the theoretical retention gain — this is the actual figure lenders your size see in production, not the calculator's best case.

If you want to see where that retained volume actually comes from (it's mostly one moment — customers approaching a rate reset — not a dozen small ones), a 15-minute walkthrough is enough to show it.

**Decision criterion advanced:** business impact with a specific number (ranked #1) — moves from the calculator's projection to a real, sourced figure.

---

### Email 2 — Day 3

**Variant A:** "Where this actually plugs into your advisors' day"
**Variant B:** "No new steps for your advisors (really)"

The retention number only means something if your advisors don't have to change how they work to get it — so here's specifically where moments land in the CRM they already use, not a new tool they have to remember to open.

Happy to map it against your specific CRM setup if that'd save you a step later in this evaluation.

**Decision criterion advanced:** fit with the advisors' existing CRM workflow (ranked #2) — addresses this persona's stated concern about retraining time directly, rather than asserting "easy" without specifics.

---

### Email 3 — Day 7

**Variant A:** "What customers notice when you call first"
**Variant B:** "The redemption number nobody tracks until it's too late"

Retention matters on the book, but the number that tends to get missed until a QBR is how many advisors actually act on a list — this is what changes once every moment comes with the reason behind it, so the customer conversation starts with something specific.

If redemptions to other lenders are something you're already tracking, this is worth five minutes even if the rest of this evaluation is still early.

**Decision criterion advanced:** whether advisors will believe and act on the moments (ranked #3) — a different angle from the internal-workflow focus of Email 2, not a restatement of it.

---

### Email 4 — Day 12

**Variant A:** "A real rollout timeline, not a 'go-live in a day' claim"
**Variant B:** "What week one, four, and twelve actually look like"

You've probably had a vendor tell you this goes live "instantly" — that's rarely the useful number, since going live and your team actually working differently are two different milestones.

Here's the real week-by-week: data connection and backtest, a pilot cohort of advisors, then full rollout. Worth comparing against whatever timeline you're being told elsewhere.

**Decision criterion advanced:** re-approaches integration effort through this persona's specific trust trigger — "a rep who separates 'the tool goes live' from 'my team actually adopts it'" — rather than a general reassurance.

---

### Email 5 — Day 18

**Variant A:** "You don't have to sell this to your risk team"
**Variant B:** "The one slide that gets Risk and Lending on the same page"

Last email in this sequence. One thing worth naming directly: this persona's `personas.md` entry is explicit that this buyer won't advocate internally for the risk/compliance case themselves, and being asked to is a stated trust breaker — so this email doesn't ask that.

If it'd help, we can put together a short, joint walkthrough for you and whoever owns the risk side, so the evidence-trail conversation happens in the room with both of you rather than becoming a second sales cycle you have to run yourself.

**Decision criterion advanced:** alignment with what Credit Risk has already approved (ranked #4) — closes the sequence by removing the one friction point this persona's own profile flags as most likely to stall the deal, without asking them to do the risk team's job.

---

## Reply handling for this campaign

See [`reply-handling-playbook.md`](./reply-handling-playbook.md)'s Head of Retail Banking section for response templates by reply type (timeline pushback, "send this to my risk lead," retraining concern, hard no).
