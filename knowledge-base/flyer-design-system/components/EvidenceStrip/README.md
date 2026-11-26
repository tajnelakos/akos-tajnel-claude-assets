# EvidenceStrip

The brand promise on paper: one moment, the customer it points at (by ID), and the data points behind it, in plain words. Every piece that shows a moment shows this.

**Markup:** `.pwf-panel.pwf-evidence` › meta line (`data`), title (`tri-panel-title`), `.pwf-evidence__rows` of `.pwf-ev` (icon and `label`, the data point in plain words), then a `source` line. No weights, percentages or bars: the first row is the lead, marked with a gold left edge (an ink edge on `--plain`). On navy the panel turns `navy-deep`.

**The consumer provides:** a customer ID, the moment, two to four evidence rows with their layer icon, in plain words, and the source.

- Do put the lead data point first; its gold edge is the panel's one gold mark. Use `.pwf-evidence--plain` (ink edge) when the panel or page already has its gold.
- Do show customers by ID only, never a name or an address, and label the data illustrative.
- Don't show weights, percentages or bars for how much a data point counted, or drop the source line. Percentages that are facts (*income up 16%*) are fine.
