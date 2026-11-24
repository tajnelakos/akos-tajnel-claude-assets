# EvidenceStrip

The brand promise on paper: one signal, the customer it points at (by ID), and the data points behind it with how much each counted. Every piece that shows a signal shows this.

**Markup:** `.pwf-panel.pwf-evidence` › meta line (`data`), title (`tri-panel-title`), `.pwf-evidence__rows` of `.pwf-ev` (icon, `label`, weight in `data`, a bar with `--w` set to the weight's share), then a `source` line. On navy the panel turns `navy-deep`.

**The consumer provides:** a customer or policy ID, the signal, two to four evidence rows with their layer icon and weight, and the source.

- Do order rows by weight, highest first; the top bar is gold, the panel's one gold mark. Use `.pwf-evidence--plain` (all navy) when the panel or page already has its gold.
- Do show customers by ID only, never a name or an address, and label the weights illustrative.
- Don't round the weights so they no longer add up, or drop the source line.
