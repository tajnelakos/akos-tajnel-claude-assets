# Sample output

The rendered one-pager: [`one-pager-head-of-credit-risk.html`](./one-pager-head-of-credit-risk.html) ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/marketing-assets/one-pager-builder/one-pager-head-of-credit-risk.html)).

---

## Input

> Build a one-pager for the Head of Credit Risk persona, Tier 1 bank/lender segment.

## Output

```
## One-Pager — Head of Credit Risk, Tier 1 Bank/Lender

**Positioning angle used:** "Opportunities you can act on — and explain" — positioning.md's primary message, not the Mortgage lending, Home insurance, or Brokerage segment rows.
**Format:** designed single-page HTML — see one-pager-head-of-credit-risk.html

**Headline:** Opportunities you can act on — and explain.
**Subhead:** Most customer-scoring tools give you a list and a score. If an auditor asks why a customer was on that list, "the model said so" isn't an answer — and increasingly, regulators are asking.
**Proof points:**
1. Per-signal evidence trail — every signal shows the property, market, and customer data points behind it and their weighting, inspectable, not just a score.
2. Backtested on your own data — signals tested against the bank's own past outcomes, method documented for technical evaluators to scrutinize.
3. Built for regulated banking from inception — audit-log format, consent handling, and CRM integration designed around banking compliance from the start.
4. A recent deal proof point (anonymized, pending sign-off) — a Nordics regional bank displaced its incumbent specifically over this gap.
**CTA:** See a live evidence trail on a sample of your own customers — real data, no prepared demo, about 15 minutes.

---
Sourced from: positioning.md (headline, subhead, proof points 1-3, exact wording) · win-loss-analysis/win-loss-crm-export.csv OPP-1001 + case-study-builder/example.md (proof point 4, anonymized until customer sign-off)
```

## Why this is a one-pager and not a mini pitch deck

- **One angle, not three.** This targets Head of Credit Risk specifically — it doesn't also try to land the Mortgage lending growth pitch or the Brokerage adoption pitch on the same page. A VP of Mortgage Lending version would need its own one-pager with a different headline and different proof points, not this one with a different logo.
- **Every proof point is checkable.** None of the four claims is an adjective — each traces to `positioning.md`'s differentiators table or a real, sourced deal, per this persona's own stated distrust of unsourced case studies (`personas.md`).
- **The CTA matches this persona's specific trust trigger** — "a vendor who volunteers a live run on the bank's own data, unprompted" (`personas.md`) — not a generic "book a demo" button.
- **The customer-proof-point strip is honest about consent status**, same discipline as [`case-study-builder`](../case-study-builder) — anonymized, with the real named version flagged as pending sign-off rather than presented as already available.
