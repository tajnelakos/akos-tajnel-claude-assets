# Deep-Dive Campaign — Head of Deposits & Savings

The [`example.md`](./example.md) quick-mode sequence for this persona, extended into a full 5-email, A/B-tested campaign — same trigger context, same decision-criteria backbone, run for real against a 240-contact segment. Results: [`campaign-metrics.csv`](./campaign-metrics.csv) (raw sends) and [`campaign-performance-analysis.html`](./campaign-performance-analysis.html) (what the data actually says). See [`personas.md`](../../knowledge-base/personas.md#head-of-deposits--savings-buyer-deposits-and-savings) for the persona this is built from. The product behind it is [Seekridge Outflow Watch](../product-launch-process/go-to-market-outflow-watch.md).

**Trigger:** downloaded the "Where Savings Go: Small Monthly Outflows in Retail Banking" guide.

**A/B design note:** every email tests two subject-line framings against the same body copy — Variant A states the point directly (declarative, matches this persona's preference for evidence per customer over a portfolio average); Variant B names their specific worry as a direct question. Body copy is held constant across variants on purpose — varying both subject and body at once would make it impossible to attribute a performance difference to either one. **Variant B won on every tracked metric for this persona** (see the analysis) — naming the outflow they can't see yet outperformed stating the same fact declaratively, even for a numbers-led buyer who is wary of anything that reads as a hook.

---

### Email 1 — Day 0

**Variant A:** "Outflows start small, and early"
**Variant B:** "Who started moving savings out this month?"

You downloaded our guide on small monthly outflows, so you already know the pattern: it's rarely one big transfer. It's EUR 300 a month to a provider paying a point more, and the balance only looks wrong months later.

If you want to see which of your own customers started that pattern recently — with the transactions behind each one, not a churn score — it takes about 15 minutes on a sample of your data.

**Decision criterion advanced:** evidence on their own data (ranked #1) — moves from the guide's general argument to their own customers.

---

### Email 2 — Day 4

**Variant A:** "Weeks before the balance falls"
**Variant B:** "How late does your churn model see it?"

Following up on outflows — the other question worth asking any vendor is how early a moment appears. A model that flags the customer once the balance has dropped is a report, not a warning.

We backtest on your own past outflows and show how many weeks ahead each one was flagged, with the method documented.

**Decision criterion advanced:** how early a moment appears (ranked #2) — distinct from Email 1's evidence focus.

---

### Email 3 — Day 9

**Variant A:** "From moment to the right call"
**Variant B:** "Does your savings team ever see the list?"

Last thing worth covering before this starts feeling like too many emails: who acts on an outflow moment. A list that stays at head office changes nothing.

Each moment lands in the banker's CRM queue with its evidence, or in the savings team's retention queue — whichever owns that customer. Happy to walk through how that would work with your setup.

**Decision criterion advanced:** how moments reach bankers and the savings team (ranked #3).

---

### Email 4 — Day 15

**Variant A:** "A mutual savings bank kept its savers without raising rates"
**Variant B:** "What a peer did instead of matching every rate"

A mutual savings bank on Outflow Watch stopped raising its savings rate for everyone. Its savings team called only the customers whose money had started to leave, with the reason in front of them, and offered the right product to each.

That's a peer reference you can actually check, not a case study with the names filed off — happy to connect you directly.

**Decision criterion advanced:** evidence on their own data, re-approached through a peer — this persona's pain is explicit that "matching every rate is ruinous", and this email is built around that rather than another angle on the same claim.

---

### Email 5 — Day 22

**Variant A:** "Worth 15 minutes on your own data?"
**Variant B:** "Which of your savers would we have flagged last year?"

This is the last email in this sequence — not because the conversation has to end here, but because a fifth follow-up on the same topic stops being useful and starts being noise.

If it'd help, we'll run a backtest on a sample of your customers from last year and show you the outflows we would have flagged, and when. The data-protection terms come with it, so your risk team gets the same pack you do. If the timing genuinely isn't right, that's a fine answer too.

**Decision criterion advanced:** closes on the persona's strongest trust trigger — transaction evidence shown per customer — and on the data-handling fit (ranked #4), with the review pack for risk handed to the buyer rather than sent to risk directly.

---

## Reply handling for this campaign

See [`reply-handling-playbook.md`](./reply-handling-playbook.md)'s Head of Deposits & Savings section for response templates by reply type ("we already have a churn model", "isn't this just a rate problem?", "forwarded to risk", hard no).
