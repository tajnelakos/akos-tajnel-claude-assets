# LayerDiagram

The flyer version of how a signal is built: three square layer chips on the left, joined by hairlines into one signal box with the gold lot in its corner. It replaces orbiting chips and glowing hero objects: the brand shows the method, not a halo.

**Markup:** `.pwf-layers` › `.pwf-layers__chips` (three `.pwf-chip.label`) · `.pwf-layers__join` · `.pwf-layers__signal`. Works on paper and on navy.

**The consumer provides:** the signal's name in plain words ("Likely to refinance within 6 months").

- Do list the layers in this order: customer data (`.pwf-chip--own`, the client's own data, outlined strong), market data, property data.
- Do use the layer icons only: `customer`, `market`, `parcel`.
- Don't add a fourth layer, arrows, glows or a chip per data point; the evidence belongs in `EvidenceStrip`.
- The signal box's lot is the panel's one gold mark.
