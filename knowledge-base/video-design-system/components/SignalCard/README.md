# SignalCard

One signal for one customer, as the product shows it in *Signals this week*: what was flagged, for whom, how high it ranks, and the start of why.

**Anatomy**
- Header: mono label `SIGNAL · DEMO · <CLIENT>`, the signal name in Plex Sans 600 (*Refinance risk*), a neutral badge (*New this week*).
- Meta row: the customer ID in Plex Mono 500 34px, one muted line of product facts (*Mortgage · EUR 312.000 · fixed until 2027-03-31*), the rank on the right in Archivo 800 88px with `/ 212` in mono.
- **At least two evidence rows**: layer, data point, weight. A SignalCard never appears without them.

**Signal names** (the product's own; never invent new ones):

| Segment | Signals |
|---|---|
| Bank / mortgage lender | Refinance risk · Top-up potential · Likely to move · Rate reset ahead |
| Insurer | Underinsured home · No contents cover · Renewal risk |
| Brokerage | Likely to sell · Ready to upsize |

**Motion.** Frame traces in, content fades in, the rank counts up to its value (`count`), then the evidence rows populate. In the next beat the card can grow into a full EvidenceTrail (cut, not morph).

**Provide.** Signal name, customer ID, product line, rank and total, the top two evidence rows.

**Avoid.** A score out of 100 (*92% likely*): Seekridge ranks, and shows why; a customer name; a red or green colour for the signal itself.
