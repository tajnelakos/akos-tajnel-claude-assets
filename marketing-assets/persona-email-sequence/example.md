# Sample output

Sequence for the Head of Deposits & Savings persona ([`personas.md`](../../knowledge-base/personas.md)).

---

## Input

> Persona: Head of Deposits & Savings. Trigger: downloaded our "Where Savings Go: Small Monthly Outflows in Retail Banking" guide from the site.

## Output

```
## Email Sequence — Head of Deposits & Savings — Trigger: guide download

### Email 1 — "Outflows start small, and early" — Day 0
You downloaded our guide on small monthly outflows, so you already know the pattern: it's rarely one big transfer. It's EUR 300 a month to a provider paying a point more, and the balance only looks wrong months later.
If you want to see which of your own customers started that pattern recently — with the transactions behind each one, not a churn score — it takes about 15 minutes on a sample of your data.
Decision criterion this advances: evidence on their own data (top-ranked criterion) — moves from the guide's general argument to their own customers.

### Email 2 — "Weeks before the balance falls" — Day 4
Following up on outflows — the other question worth asking any vendor is how early a moment appears. A model that flags the customer once the balance has dropped is a report, not a warning.
We backtest on your own past outflows and show how many weeks ahead each one was flagged, with the method documented.
Decision criterion this advances: how early a moment appears (2nd-ranked criterion) — distinct from email 1's evidence focus.

### Email 3 — "From moment to the right call" — Day 9
Last thing worth covering before I stop filling your inbox: who acts on an outflow moment. A list that stays at head office changes nothing.
Each moment lands in the banker's CRM queue with its evidence, or in the savings team's retention queue — whichever owns that customer. Happy to walk through how that would work with your setup, no pressure if the timing isn't right.
Decision criterion this advances: how moments reach bankers and the savings team (3rd-ranked criterion) — closes the loop without urgency tactics.
```

Note: no 4th email pushing "last chance" urgency, and no rate-matching hook — this persona's `personas.md` entry flags a pitch that implies matching every competitor rate as a trust breaker, so the sequence ends on a low-pressure, real-effort answer instead.
