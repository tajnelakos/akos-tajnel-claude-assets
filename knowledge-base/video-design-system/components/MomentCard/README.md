# MomentCard

One moment for one customer, as the product shows it in *Moments this week*: what was flagged, for whom, how high it ranks, and the start of why.

**Anatomy**
- Header: mono label `MOMENT · DEMO · <CLIENT>`, the moment name in Plex Sans 600 (*Money starting to leave*), a neutral badge (*New this week*).
- Meta row: the customer ID in Plex Mono 500 34px, one muted line of product facts (*Mortgage · EUR 312.000 · fixed until 2027-03-31*), the rank on the right in Archivo 800 88px with `/ 212` in mono.
- **At least two evidence rows**: layer and data point, in plain words, with no weights or percentages. A MomentCard never appears without them.

**Moment names** (the product's own; never invent new ones):

| Family | Moments |
|---|---|
| Main bank | Salary landing elsewhere · Salary just switched in · Bills paid from elsewhere |
| Outflow | Money starting to leave · Balance drifting down · Card going quiet |
| Growth | Income rising · Investing elsewhere · Mortgage-ready · Saving for a home · Mortgage elsewhere · Car purchase goal · Family growing · Renovation planned |
| New customer | New customer not yet active · Salary not switched yet |

**Motion.** Frame traces in, content fades in, the rank counts up to its value (`count`), then the evidence rows populate. In the next beat the card can grow into a full EvidenceTrail (cut, not morph).

**Provide.** Moment name, customer ID, product line, rank and total, the top two evidence rows.

**Avoid.** A score out of 100 (*92% likely*): Seekridge ranks, and shows why; a customer name; a red or green colour for the moment itself.
