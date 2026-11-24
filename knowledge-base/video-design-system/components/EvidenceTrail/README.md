# EvidenceTrail

The signature component, and the brand promise on screen: every data point behind a moment, which layer it came from, its value, and how much it counted. The weights sum to 100.

**Anatomy**
- Header: `DEMO · <CLIENT>`, *Evidence trail*, and the customer and moment on the right in mono.
- Column labels (mono 18px, texture): Layer · Data point · Value · Weight.
- One row per data point, 72px, sorted by weight: the layer as icon + mono label (`MARKET`, `PROPERTY`, `CUSTOMER`), the data point in Plex Sans, the value in mono, the weight as a bar on a track plus the figure.
- **The top row's bar is gold**; the others navy. That bar is the frame's one gold, so the headline carries no highlight while it is on.
- Footer in mono: *Weights sum to 100 · model v4.2, validated 2026-09-30*.

**Motion** (the longest beat in a film, 7–10 s)
1. Frame traces in, content fades in.
2. Rows populate every 450ms; each bar grows to its weight (`bar-grow`) while its figure counts.
3. FocusMarks close on the top row; the other rows dim to 35%.
4. Hold. The voice-over reads the top reason in plain words.

**Copy.** Data points name the measure, not an adjective: *Rate gap to market +1.7 pts*, *Equity position (LTV) 57%*, *Competitor offers nearby 6 in 30 days*, *Fixed rate ends 2027-03-31*.

**Provide.** 3–5 rows (layer, data point, value, weight), the model version line.

**Avoid.** Weights that don't add to 100, colour per layer, an evidence trail behind a click or a tooltip, rounding that hides the order.
