# EvidenceTrail

The signature component, and the brand promise on screen: every data point behind a moment, in plain words, with the layer it came from and its value.

**Evidence rows list the data points in plain words. Don't show weights or percentages.** Viewers read weights as probabilities or as shares of income, so there are no weight bars, no "38%", no decimals and no "adds up to 100". Percentages that are facts about the customer or the market stay (*income up 16%*, *market rates +1.7 pts*).

**Anatomy**
- Header: `DEMO · <CLIENT>`, *Evidence trail*, and the customer and moment on the right in mono.
- Column labels (mono 18px, texture): Layer · Data point · Value. Optional: drop them when the panel needs the height.
- One row per data point, 72px: the layer as icon + mono label (`CRM`, `TRANSACTIONS`, `MARKET`), the data point in Plex Sans, the value in mono, right-aligned.
- **The first data point is the lead**: a 6px gold edge on its left and the data point in 600 weight (`.is-lead`). That edge is the frame's one gold, so the headline carries no highlight while it is on. The other rows have no marker.
- Optional footer in mono: *Model v4.2, validated 2026-09-30*.

**Motion** (the longest beat in a film, 7–10 s)
1. Frame traces in, content fades in.
2. Rows populate every 450ms, top to bottom.
3. FocusMarks close on the lead row; the other rows dim to 35%.
4. Hold. The voice-over says what the data shows, in plain words.

**Copy.** Data points name the measure, not an adjective: *Fixed rate ends in 7 months*, *Salary split with another bank*, *Competitor offers nearby, 6 in 30 days*, *Baby-related purchases, 9 in 60 days*. The voice-over never talks about how much a data point counted.

**Provide.** 3–5 rows (layer, data point, value), with the lead first; the model version line if the film needs it.

**Avoid.** Weights, scores, bars or percentages next to a data point; colour per layer; an evidence trail behind a click or a tooltip.
