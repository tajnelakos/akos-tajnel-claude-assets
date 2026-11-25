# ProductPanel

The base of every product moment: a flat white panel rebuilt from a real Seekridge screen (see `assets/Product UI/`), cropped to the part the beat is about. MomentCard, EvidenceTrail and AuditLog are panels.

**Anatomy**
- White `surface`, 1px `panel-line` border, 16px corners (`radius`), **no shadow**: it lies on the ground like a sheet on a drafting table.
- Header row on `surface-sunken`: a mono label naming the demo client (`DEMO · ALPENKREIS BANK`), the screen title in Plex Sans 600 32px, an optional badge or one button on the right.
- Rows 72px high, Plex Sans 500 26px values, mono for IDs, dates and figures, hairlines between rows. 4–6 rows.
- Optional footer in mono 20px for the method or source line.

**Badges** (product UI only): `is-good` (*Synced to CRM*, green dot, good-ink on good-bg), `is-neutral` (*Queued*, *New this week*). Pill-shaped (`radius-pill`).

**Motion.** The hairline frame traces clockwise from the top-left in navy (`frame-trace` 600ms) and settles to the light hairline as the white fills and the content fades in (`content-in` 250ms). Rows then populate top to bottom (`row-stagger`). A push-in up to 1.03 across the beat is allowed (`drift`).

**Layout.** Split beats: columns 6–12 (from x 826, 998px wide). Full beats: columns 2–11.

**Provide.** Which screen, which rows, which row the beat is about.

**Avoid.** A whole app window with navigation, avatars, dark-mode panels, more than one primary button, drop shadows, 3D tilt, rounded cards.
