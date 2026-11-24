# Video and motion

Rules for Parcelwise product videos and UI motion: formats, story structure, key frames, captions, the motion language and production. Component: `VideoFrame` in [`components.md`](./components.md).

## Formats

| Cut | Size | Length | Use |
|---|---|---|---|
| Master | 1920 × 1080, 16:9 | 45–75 s | Website, sales follow-ups, events |
| Social | 1080 × 1350, 4:5 | 30–45 s | LinkedIn feed |
| Vertical | 1080 × 1920, 9:16 | 15–30 s | Stories, event screens |

30 fps, H.264, captions burnt in on every cut. One video per segment and persona (mortgage lending, home insurance, brokerage, risk and compliance): never one video for everybody.

## Structure

1. **Hook (0–5 s):** the persona's situation on a navy title card. "Your customer's fixed rate resets in four months."
2. **Tension (5–15 s):** what goes wrong today. "By the time anyone notices, they've refinanced elsewhere."
3. **Method (15–40 s):** the product, as real screen recordings, following the three layers: the customer record, then the property and its value, then the market and rates. The signal appears with its evidence trail and is pushed to the CRM.
4. **Proof (40–55 s):** one backtest figure with its source line, or one customer outcome (approved, or labelled illustrative).
5. **Close (last 4–5 s):** end card with the lockup, one line ("Opportunities you can act on — and explain.") and one action ("Run a backtest on your own book").

## Frames

- **Title card:** navy ground, `parcel-grid` motif bleeding off the right, Archivo 800 at 96–120px in Paper, lockup top-left.
- **Screen recording:** on Paper, the product in a `surface` frame with a hairline border, cropped to the panel that matters; zoom in on the detail being described.
- **Lower third:** navy band, 2px gold rule above it, Plex Sans 600 at 40px; at least `canvas-margin-caption` (160px) above the bottom edge.
- **Captions:** Plex Sans 500 at 44px (master), Paper on a navy band at 90% opacity, 2 lines max, 42 characters a line, sentence case.
- **Figure card:** one number in Archivo 800 at 240px, the measure under it in Plex Sans, the source in Plex Mono.
- **End card:** reversed lockup centred on navy, the line, the action, held 3 seconds.

Logo: lockup on the title and end cards; the mark at 48px bottom-right on screen-recording frames, nowhere else.

## Motion language

Motion should feel like a surveyor drawing a plan: straight lines, exact, no bounce.

| Token (in CSS) | Value | Use |
|---|---|---|
| `--motion-fast` | 150ms | Hover, press, focus |
| `--motion-base` | 250ms | Menus, tabs, panels in UI |
| `--motion-slow` | 500ms | Video text in and out |
| `--motion-draw` | 800ms | Parcel lines drawing in on video |
| `--ease-standard` | cubic-bezier(0.2, 0, 0, 1) | Everything that moves |

- **Signature move:** parcel lines draw in, then the one gold lot fills. Use it on the title card and when a signal appears.
- **Allowed:** cuts, fades, straight wipes, line draws, number count-ups (ending on the exact value), slow zooms into screenshots.
- **Not allowed:** bounces, spins, 3D flips, glitch effects, particle fields, stock footage.
- **UI motion:** only to show cause and effect (a row expanding, a panel opening). Respect `prefers-reduced-motion`: replace movement with a fade.

## Sound

Restrained music under a calm voice-over, or music only with captions carrying the story. No whooshes on every cut. The video must work fully muted.

## Production

- Draw every frame at the output size and 30 fps.
- Render one file per scene with the same size, frame rate and encoder settings, join them without re-encoding, and add sound last. Crossfades go inside a scene file.
- Before the full render, check stills of the busiest moments at full size.
- Subtitles in the market's language; German and Dutch captions run longer, so re-time rather than shrink.

## Before you export

1. One persona, one claim per scene, readable in 3 seconds?
2. Real product footage, with no real customer names, addresses or data on screen?
3. Captions burnt in, inside the caption margin?
4. Figures real or labelled illustrative, with a source?
5. No bounce, spin, stock footage or gradient?
6. End card: lockup, one line, one action, 3-second hold?
