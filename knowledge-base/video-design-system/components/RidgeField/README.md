# RidgeField

The brand's one graphic idea, at the scale of a whole customer base: a patch of the client map seen at an angle, drawn as a field of dots that is always gently moving. Only a few areas rise into peaks, the week's moments, and the one the film follows is marked in gold.

**Anatomy**
- A dot surface in perspective: a regular grid of dots, smaller and fainter towards the horizon, brightest where the surface rises.
- The surface keeps moving for the whole scene: a slow, low wave, so the database always looks alive.
- Peaks: two to five areas rise clearly out of the surface. Each summit gets a marker, filled navy at 90% on Paper (Paper at 75% on Navy).
- One gold point: the customer the film follows, on the highest summit, as in the logomark.

**Variants.** Full field (scale beat), right-edge field (TitleCard), bottom band with no gold (StatementStage).

**Motion.** `data-fx="terrain"`: the map fades in and starts moving; the peaks rise one after another at the times in `data-terrain`'s `rise` list; the summit markers land as each peak finishes, the gold one last. The film engine redraws the dots every frame, so the surface never stops moving.

**Copy.** The headline gives the count: *212 customers to call this week. Not 40,000.* The field is never labelled point by point.

**Provide.** Size, which peaks (position, height, width), when each rises, which one is gold.

**Avoid.** A map of a real place, house icons, people, bars or columns (it is terrain, not a city), heat-map colour, more than one gold point.
