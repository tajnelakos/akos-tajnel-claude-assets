# RidgeField

The brand's one graphic idea, at the scale of a whole customer base: a range of ridgelines drawn in straight segments, the week's moments marked as points on them, the one the film follows in gold.

**Anatomy**
- An SVG field of ridgelines: one mountain profile per row, built from straight segments only (no curves), each row lower than the one above so they never cross.
- Lines: `survey-line` at `survey-line-opacity` (Navy at 18% on Paper, Paper at 35% on Navy), 2px, mitred joins.
- Marked moments: small points on the ridgelines, filled navy at 90% on Paper (Paper at 75% on Navy).
- One gold point: the customer the film follows, sitting on a summit, as in the logomark.

**Variants.** Full field (scale beat), right-edge field (TitleCard), bottom band (StatementStage), small field inside a Walkthrough frame.

**Motion.** The ridgelines draw left to right, top row first (`draw`, staggered); marked points fill one after another (60ms apart); the gold point fills last (`lot-fill`). A slow straight push-in (`drift`) is allowed on the scale beat.

**Copy.** The headline gives the count: *212 customers to call this week. Not 40,000.* The field is never labelled point by point.

**Provide.** Size, seed, how many points to mark, where the gold point goes.

**Avoid.** A map of a real place, house icons, people, curves or contour blobs, heat-map colour, more than one gold point.
