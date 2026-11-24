# Sample output

Moments scored against [`icp.md`](../../knowledge-base/icp.md). This example's flagged account, Nordkredit, is carried through to [`abm-account-brief`](../abm-account-brief) and [`personalized-outbound`](../../marketing-assets/personalized-outbound).

---

## Input (raw moments, pasted)

> - Nordkredit (regional lender, Nordics) posted a job for "Head of Credit Risk" three weeks ago; role has since been filled per their LinkedIn page.
> - Nordkredit's engineering job postings this month mention "migrating customer-targeting and data workflows off legacy vendor tooling."
> - Meridian Savings (regional bank, DACH) had a generic "we're growing!" LinkedIn post about hiring across departments.
> - Court Street Lending (large national lender, €5B+ origination) had a senior risk hire announced.

## Output

```
## Buying Moment Watch List — March 2026

1. Nordkredit — Tier 1 — Moment strength: Strong
   Evidence: New Head of Credit Risk hired ~3 weeks ago (role now filled); engineering job postings this month explicitly reference migrating off legacy customer-targeting tooling — this is a specific, corroborating second moment, not a standalone hire.
   Time sensitivity: High — new risk leadership typically re-evaluates vendor tooling within their first 1-2 quarters; the tooling-migration posting suggests this may already be underway.

2. Court Street Lending — Tier 2 — Moment strength: Medium
   Evidence: Senior risk hire announced, no corroborating second moment yet (no job postings or public statements about tooling).
   Time sensitivity: Medium — worth a watch, not urgent outreach; single-moment accounts should get a second data point before high-priority action.

Out-of-segment (moment present, doesn't fit ICP): Meridian Savings — moment is a generic hiring post with no risk/credit-specific hire or tooling mention; doesn't meet the Strong or Medium bar as defined, and general headcount growth isn't itself an ICP moment.
```

Note: Court Street Lending is Tier 2, not Tier 1 (per `icp.md`, €5B+ origination volume moves it into the longer-cycle, more-procurement-layers tier) — it's still worth tracking, just not with the same urgency as a Tier 1 account showing the same moment strength.
