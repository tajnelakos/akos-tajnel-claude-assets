# ChapterRail

Tells the viewer where they are in a Moment story, in the order of the first rule: Situation · Moment · Evidence · Action.

**Anatomy.** IBM Plex Mono 500, 20px, +0.08em, uppercase, left-aligned at the margin under the caption band (baseline `rail-bottom`, 72px). Each item has a 14px square: outlined for upcoming, half-filled for done, filled for the current chapter. Squares, because they are lots.

**States.** `is-active` (ink, full opacity), `is-done` (80%), upcoming (55%).

**Motion.** The active square fills when a chapter starts (`lot-fill`); nothing else moves. The rail appears with the first Paper beat and leaves before the Proof beat; never on the TitleCard or EndCard.

**Use.** Moment stories and Segment stories only. Walkthroughs name the step in the eyebrow instead (`STEP 2 / 5`); Statements have no navigation.

**Avoid.** Gold on the rail, numbers instead of chapter words, a progress bar that fills with time.
