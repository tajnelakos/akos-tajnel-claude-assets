# Trifold

The A4 roll-fold leaflet (297 × 210 mm, folded to 100 × 210 mm): the main piece for events, branch drops and the post-meeting leave-behind.

**Panel order.** Outside, left to right: flap back (97 mm), back (100 mm), front (100 mm). Inside: 100 mm, 100 mm, then the flap (97 mm), which folds in first. The flap is 3 mm narrower so it closes without buckling; set `.pwf-fold--flap` on it.

**Grounds.** Front and back on navy (`.pwf-navy`, `data-theme="dark"`), flap back and the whole inside on paper. Never mix grounds inside one panel.

**What goes where**

| Panel | Ground | Built from |
|---|---|---|
| Front | navy | `Logo` lockup top-left, parcel-grid motif top-right, eyebrow naming the reader, `tri-claim` (up to 12 words, up to three in gold), one `tri-body` line, web address at the foot |
| Back | navy | the next step: `tri-heading`, one line on what happens, `ContactBlock` at the foot. No logo: the front carries it |
| Flap back | paper | the three pillars as `FeaturePanel`s, the fictional-company line as a `source` at the foot |
| Inside 1 | paper | the problem in the reader's words, a pull line, then `Benefit` ×4 anchored to the foot |
| Inside 2 | paper | how it works: `LayerDiagram`, one caption, `Step` ×3 anchored to the foot |
| Inside 3 (flap) | paper | the proof: `EvidenceStrip`, then a `FigurePanel` anchored to the foot |

**The consumer provides:** the reader (one persona per piece), the claim, three pillars, the problem, the steps, one signal with its evidence and up to two sourced figures, and the one action with its URL.

- Do align the lower blocks across the inside spread (`margin-top:auto`), so the three panels share a top and a bottom line.
- Do keep one gold element per panel. The logo's lot does not count.
- Do keep every text block 8 mm (`space-4`) from folds and trim; the fold eats about 1 mm each side.
- Don't run a figure, sentence or diagram across a fold.
- Don't put the logo on more than one outside panel.
