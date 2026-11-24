# LayerDiagram

The flyer version of how a moment is built: three square layer chips on the left, joined by hairlines into one moment box with the gold point in its corner. It replaces orbiting chips and glowing hero objects: the brand shows the method, not a halo.

**Markup:** `.pwf-layers` › `.pwf-layers__chips` (three `.pwf-chip.label`) · `.pwf-layers__join` · `.pwf-layers__moment`. Works on paper and on navy.

**The consumer provides:** the moment's name in plain words ("Likely to refinance within 6 months").

- Do list the layers in this order: customer data (`.pwf-chip--own`, the client's own data, outlined strong), market data, property data.
- Do use the layer icons only: `customer`, `market`, `property`.
- Don't add a fourth layer, arrows, glows or a chip per data point; the evidence belongs in `EvidenceStrip`.
- The moment box's gold square is the panel's one gold mark.
