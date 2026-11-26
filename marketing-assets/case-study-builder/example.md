# Sample output

Nordkredit — the account that runs through the rest of this repo. This case study is that thread's actual ending: [`sales-call-analysis/call-01-nordkredit.md`](../../knowledge-base/sales-call-analysis/call-01-nordkredit.md) is the resulting discovery call, and the deal closed won per [`win-loss-analysis/win-loss-crm-export.csv`](../../knowledge-base/win-loss-analysis/win-loss-crm-export.csv) (OPP-1001).

---

## Input

> Account: Nordkredit. Source: `win-loss-crm-export.csv` row OPP-1001 (Won, closed 2026-09-08, 65-day cycle, €56,924 ACV, competitor Conturo quoted €57,313, decision driver "Explainability / evidence trail", product feedback "Standout: customer-level evidence trail") + `sales-call-analysis/call-01-nordkredit.md` (discovery call with Lena Virtanen, Head of Model Risk).

## Output

```
## Case Study — Nordkredit

**Status:** Draft — pending Nordkredit's explicit sign-off before publishing named or quoting Lena Virtanen publicly

**Title:** Nordkredit replaces a "score only" targeting tool ahead of a board audit
**Snapshot:** Retail bank · Tier 1 · Nordics · ~900,000 retail customers · Displaced: Conturo (incumbent) · Deal size: €56,924 ACV · Sales cycle: 65 days

### Challenge
Nordkredit's newly hired Head of Model Risk inherited an internal audit finding on her first day: a savings-and-investment campaign had been run off a customer score from the bank's existing data provider — a score and a generic methodology document, not the specific data points that put an individual customer on the list. When an auditor or internal risk committee asked "why this customer," the only honest answer was "the model said so" — not something the team wanted to repeat at an upcoming board audit.

### Solution
Rather than a prepared demo, Seekridge ran moments live on a pseudonymized sample of Nordkredit's own customers, at the prospect's request — showing the actual transaction, market, and CRM data points behind each moment and their weighting, not a templated walkthrough. Nordkredit had already used this same standard (push past the first demo, ask for a real breakdown) to evaluate and rule out another vendor earlier in its process.

### Results
- Closed in 65 days — inside Nordkredit's own Tier 1 typical sales-cycle range (per `icp.md`: 2-4 months)
- Logged decision driver: "Explainability / evidence trail" (win-loss-crm-export.csv, OPP-1001)
- Logged product feedback: "Standout: customer-level evidence trail" (same record)
- Won at effective price parity, not on discount — Seekridge's ACV (€56,924) closely tracked the competitor's own quoted price (€57,313) for the same deal

### Quote
No public-use quote available yet. Lena Virtanen's discovery-call comments about the "the model said so" problem are exactly the kind of language a real testimonial should use — but they were said on a sales call, not given as a public statement, so using them here requires her explicit sign-off first, not just because they exist in our call notes.

---
Positioning tie-in: "Bankers act on it" (positioning.md's message house) — the specific proof point this account decided on (named data points and weighting per customer, not a score) is exactly this pillar, not a generic lead-volume claim.
Sourced from: win-loss-crm-export.csv (OPP-1001) · sales-call-analysis/call-01-nordkredit.md
What's not confirmed: whether Nordkredit's implementation was completed before their stated board-audit date (tentatively the second week of September, per the call transcript) — the CRM close date (2026-09-08) falls right around that window, but "deal closed" isn't the same claim as "audit passed," and the source material doesn't confirm the latter. This case study should not assert it did.
```

Note what this example deliberately does *not* do: it doesn't smooth over the audit-timing question just because it would make a cleaner ending — the "what's not confirmed" line exists specifically so a genuinely unverified detail doesn't get published as fact.
