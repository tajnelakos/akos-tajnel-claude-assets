# Deep-Dive Campaign — Head of Retail Banking

A full 5-email, A/B-tested campaign for the bank's economic buyer, run against a 260-contact segment. Results: [`campaign-metrics.csv`](./campaign-metrics.csv) (raw sends) and [`campaign-performance-analysis.html`](./campaign-performance-analysis.html) (what the data actually says). See [`personas.md`](../../knowledge-base/personas.md#head-of-retail-banking-buyer-main-bank-and-lending) for the persona this is built from.

**Trigger:** used the main-bank calculator on the site.

**A/B design note:** same structure as the [Head of Deposits & Savings campaign](./campaign-head-of-deposits-and-savings.md) — Variant A states the point declaratively with a specific number where one exists, Variant B leads with a direct question naming the cost of inaction. **Variant A won on every tracked metric for this persona** — the opposite result from the Head of Deposits & Savings campaign, where the question framing won. Don't read "provocative questions win" or "declarative numbers win" as a universal rule from either result in isolation — see the analysis for why the same technique cuts opposite ways for these two personas.

---

### Email 1 — Day 0

**Variant A:** "The main-bank number banks like yours actually hit"
**Variant B:** "How many customers moved their savings out last quarter?"

You ran the numbers on our calculator, so you've already seen the theoretical gain in main-bank customers — this is the actual figure banks your size see in production, not the calculator's best case.

If you want to see where that gain actually comes from (it's mostly one moment — customers whose salary lands at another bank — not a dozen small ones), a 15-minute walkthrough is enough to show it.

**Decision criterion advanced:** business impact with a specific number (ranked #1) — moves from the calculator's projection to a real, sourced figure.

---

### Email 2 — Day 3

**Variant A:** "Where this actually plugs into your bankers' day"
**Variant B:** "No new steps for your bankers (really)"

The main-bank number only means something if your bankers don't have to change how they work to get it — so here's specifically where moments land in the CRM they already use, not a new tool they have to remember to open.

Happy to map it against your specific CRM setup if that'd save you a step later in this evaluation.

**Decision criterion advanced:** fit with the bankers' existing CRM workflow (ranked #2) — addresses this persona's stated concern about retraining time directly, rather than asserting "easy" without specifics.

---

### Email 3 — Day 7

**Variant A:** "What customers notice when you call first"
**Variant B:** "The outflow number nobody tracks until it's too late"

Main-bank customers matter, but the number that tends to get missed until a QBR is how many bankers actually act on a list — this is what changes once every moment comes with the reason behind it, so the customer conversation starts with something specific.

If savings moving to other banks is something you're already tracking, this is worth five minutes even if the rest of this evaluation is still early.

**Decision criterion advanced:** whether bankers will believe and act on the moments (ranked #3) — a different angle from the internal-workflow focus of Email 2, not a restatement of it.

---

### Email 4 — Day 12

**Variant A:** "A real rollout timeline, not a 'go-live in a day' claim"
**Variant B:** "What week one, four, and twelve actually look like"

You've probably had a vendor tell you this goes live "instantly" — that's rarely the useful number, since going live and your team actually working differently are two different milestones.

Here's the real week-by-week: data connection and backtest, a pilot cohort of bankers, then full rollout. Worth comparing against whatever timeline you're being told elsewhere.

**Decision criterion advanced:** re-approaches integration effort through this persona's specific trust trigger — "a rep who separates 'the tool goes live' from 'my team actually adopts it'" — rather than a general reassurance.

---

### Email 5 — Day 18

**Variant A:** "You don't have to sell this to your risk team"
**Variant B:** "The one slide that gets Risk and Retail on the same page"

Last email in this sequence. One thing worth naming directly: this persona's `personas.md` entry is explicit that this buyer won't advocate internally for the risk/compliance case themselves, and being asked to is a stated trust breaker — so this email doesn't ask that.

If it'd help, we'll give you a short review pack to forward to whoever owns the risk and data-protection side — the method, a real evidence trail, the data-processing terms — and join a call with them if they want one, so the review doesn't become a second sales cycle you have to run yourself.

**Decision criterion advanced:** a clear path through risk and data protection that doesn't depend on them arguing it (ranked #4) — closes the sequence by removing the one friction point this persona's own profile flags as most likely to stall the deal, without asking them to do the risk team's job.

---

## Reply handling for this campaign

See [`reply-handling-playbook.md`](./reply-handling-playbook.md)'s Head of Retail Banking section for response templates by reply type (timeline pushback, "send this to my risk lead," retraining concern, hard no).
