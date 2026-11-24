# Sample output — same account, different persona

**Account:** Nordkredit (fictional) · **Persona:** VP of Mortgage Lending · **Signal strength:** Strong (same signal as [`example.md`](./example.md))

Holds the account and trigger fixed from [`example.md`](./example.md) and changes only the persona, to isolate what a persona swap alone changes. This is a real, common rep move — multi-threading an account by writing to a second stakeholder using the same known signal, read through that stakeholder's own priorities rather than restating the first email with a new name at the top.

---

## Input

> Same underlying signal as the [Nordkredit account brief](../../sales-tools/abm-account-brief/example.md): new Head of Credit Risk hired ~3 weeks ago; engineering job postings this month reference migrating customer-targeting workflows off legacy tooling.
>
> This message is not to that new Head of Credit Risk hire — it's a parallel outreach to Nordkredit's VP of Mortgage Lending, multi-threading the account. No new facts beyond what the original brief established; the persona reading it changes, not the underlying trigger.
>
> **Lead persona for this message:** VP of Mortgage Lending — per `personas.md`, this persona owns growth and retention of the mortgage book, will defer to Credit Risk on explainability, and won't advocate internally for the risk side of a purchase.
> **Positioning angle:** "Know which customers to call this month, and why, before a competitor does" (the Mortgage lending row in `positioning.md`'s segment table) — distinct from the Head of Credit Risk email's explainability-first framing.

## Output

```
## Outbound Draft — Nordkredit — Email

Subject: What the tooling migration means for retention

Hi [Name],

I saw your team's already in motion on migrating customer-targeting tooling off your current vendor — usually a risk-driven decision, but the impact lands on your lending numbers either way.

A change like this tends to go one of two ways for a quarter or two: your advisors get a sharper list of who's about to refinance elsewhere, or campaigns pause while everyone adjusts and those customers quietly leave. Worth 15 minutes on what the transition actually looks like week-to-week for your advisors — separate from whatever your risk team is evaluating on the explainability side?

[Rep name]

---
Personalization used: the same tooling-migration signal used in the Head of Credit Risk outreach to this account, re-read through the lending-growth lens instead — no new fact, a different persona's angle on it.
```

## Why this email is different from the Head of Credit Risk version, not just re-addressed

- **Opens on retention risk, not evidence trails** — this persona's top decision criterion (`personas.md`) is business impact on the mortgage book, not explainability.
- **The ask is about the transition itself**, not a conversation about methodology — matches what this persona actually owns.
- **Explicitly stays out of the risk/compliance conversation** ("separate from whatever your risk team is evaluating") — this persona's profile states plainly that being asked to carry the internal risk case is a trust breaker, so the email doesn't lean on them for that even implicitly.
- **No mention of evidence trails, auditors, or defensibility** — those words would be exactly right in the Head of Credit Risk email and exactly the wrong opener here; a persona-blind template would have included them by default.
