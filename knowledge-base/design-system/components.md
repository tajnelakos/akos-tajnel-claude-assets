# Components

Guidelines for the Parcelwise components. Styles live in [`components.css`](./components.css) (classes prefixed `pw-`, reading the variables in [`tokens.css`](./tokens.css)); every component is rendered in [`components.html`](./components.html).

## Button

Square-cornered buttons for actions: one primary per view, outlined secondary, underlined text button.

**You provide:** a label written as verb + object in sentence case ("Push to CRM", "View evidence", "Export audit log"); optionally a trailing `arrow-right` icon for "go somewhere" actions.

**Variants:** `pw-btn--primary` (navy fill, white text; gold-light with dark text in the dark theme), `pw-btn--secondary` (1px `line-strong` outline, no fill), `pw-btn--text` (underlined, for low-priority links), `pw-btn--sm` for dense tables. `disabled` uses `surface-sunken` and `slate`.

**Rules**
- `radius-md` (4px) at most. Never pill-shaped, never a gradient, never a shadow.
- One primary button per view. Destructive actions are secondary buttons with an explicit label ("Dismiss signal"), followed by a confirmation.
- Never "Submit", "Click here" or "Learn more".

## FormField

A labelled text input with helper and error text: labels above fields, never placeholder-only.

**You provide:** a sentence-case label, an optional placeholder that shows the format, helper text that says what the field is used for, and for errors a message that says what happened and what to do.

**States:** default (1px `line-strong` border, 3:1 or more on surface), focus (2px `focus` ring), error (`pw-field--error`: 2px `critical` border, `critical-ink` message with the `alert` icon).

**Rules**
- An error is never colour alone: always a message, always an icon.
- Don't blame the user ("Invalid input"); explain and offer the next step.
- Field width matches the expected input; don't stretch an ID field across the page.

## Card

A flat, bordered panel for grouping content: hairline border, no shadow.

**You provide:** an optional mono eyebrow (feature or topic), a title in Archivo 600, a short body in `ink-muted`, and an optional footer with one action.

**Rules**
- 1px `line` border, `radius-md`, `space-5` padding, `shadow-none`. Cards never float.
- No coloured left borders, no icons in coloured circles, no emoji.
- One action per card at most. The whole card is not a link unless it has no other interactive elements.

## StatusBadge

A small label for the state of a signal, a sync or an integration, always with a word, never colour alone.

**You provide:** the state in one to three words, sentence case.

**Variants:** `pw-badge--good`, `--warning`, `--critical` use the `-ink` text on `-bg` grounds (all 4.5:1 or more); the default is neutral.

**Rules**
- Status colours mean state only: never use a badge as decoration or a segment colour.
- Warning is orange, not gold: gold is the brand accent and never signals state.

## Alert

An inline message about the current task: what happened and what to do next.

**You provide:** a bold lead of a few words, then one or two plain sentences; the matching icon (`alert`, `check`, or a topic icon such as `crm-sync` for neutral notes).

**Variants:** neutral (surface, hairline), `pw-alert--good`, `--warning`, `--critical`.

**Rules**
- State limits openly: a warning about thin evidence is part of the product's honesty, not a failure.
- No exclamation marks, no "Oops".
- Use `role="status"` for passive messages and `role="alert"` only for errors that block the task.

## DataTable

A dense, bordered table for signals, evidence and exports.

**You provide:** column headers (they render as mono eyebrows), rows, and a source line under the table in `caption` naming which data layers the rows come from.

**Rules**
- Numbers and dates right-aligned in Plex Mono with tabular figures; dates as 2026-11-24.
- Currency code before the number, formatted for the market (CHF 1’240’000; EUR 412.500 in German).
- Customers appear by ID in mock-ups and demos, never by a real name.
- Highlight at most one row (`is-highlight`: sunken ground and a 3px gold edge) for the row the view is about.
- Hairline row dividers, no zebra striping, no shadows.

## StatTile

One figure with what it measures and where it comes from.

**You provide:** a mono eyebrow naming the measure, the figure (Archivo 800, tabular), one line of context (scope, population, period), and a source line for any backtest or external figure.

**Rules**
- A number without its measure is not allowed: every tile says what it counts.
- Illustrative figures are labelled as such outside internal tools.
- No trend arrows in green and red; if direction matters, say it in words ("up 120 since October").

## SignalCard

The signature product surface: one signal, the customer it points at, and the evidence trail behind it.

**You provide:** the segment and customer (by ID in demos), the signal in plain words ("Likely to refinance elsewhere", "Rebuild value above sum insured", "Likely to sell within 12 months"), the timing and strength, the top data points with their weights and which layer each comes from (property, market, customer), the actions, and the model version and timestamp.

**Rules**
- The evidence is always visible with the signal, never behind a click. This is the brand promise in UI form: opportunities you can act on, and explain.
- Each data point is labelled with its layer in mono. The largest-weight data point is the one gold element; other bars are navy.
- Show limits next to the signal (a warning badge or Alert for thin evidence), not in a footnote.
- Model version and timestamp in mono on every card: they make the signal reproducible for the audit log.

## PricingTier

The three brokerage tiers, Plot, Block and Estate, side by side.

**You provide:** the tier name (only these three), who it's for and the billing basis in mono, 2–5 included items as literal feature names, and one action.

**Rules**
- Tier names are used only for brokerage pricing, never as a general naming device.
- The recommended tier gets a 2px navy border, not a "Most popular" ribbon or a colour fill.
- Banks and insurers pay a platform subscription priced by the size of the customer base analysed; it isn't shown as tiers.

## CarouselSlide

LinkedIn carousel slides on the 1080 × 1350 canvas: a navy cover and a paper proof slide. Full rules in [`social-and-carousels.md`](./social-and-carousels.md).

**You provide:** the segment and job of the post (explain a signal, prove with a backtest, launch, invite), a cover title of about 8 words that names the reader's situation, one idea per middle slide, real or clearly illustrative proof, and a close with one action.

**Build rules**
- Grounds: `navy` or `paper` only, flat. `canvas-margin` 96px on every side.
- Cover: lockup top-left, `parcel-grid` motif bleeding off the top-right, title in Archivo 800 at 104px, swipe arrow bottom-right.
- Middle slides: mono eyebrow top-left, heading Archivo 700 at 60px, body Plex Sans 40px, mark bottom-right, counter bottom-left.
- Highlight up to 3 words in `gold-light` on navy only.
- Product proof sits in a white frame with a hairline border and 6px corners; mock-ups use skeleton bars, not invented customer data.

**Don't:** gradients, glows, stock photos, emoji, hashtags or links on slides.

## VideoFrame

Key frames for product videos on the 1920 × 1080 master: the title card and a screen-recording frame with a burnt-in caption. Full rules in [`video-and-motion.md`](./video-and-motion.md).

**You provide:** one segment and persona, a hook line for the title card that names the customer situation, the product screens to rebuild (see [`../video-design-system/`](../video-design-system) for the full film components), caption text (2 lines max, 42 characters a line) and a closing action.

**Build rules**
- Title card: navy, `parcel-grid` motif bleeding off the right, lockup top-left, Archivo 800 at 112px.
- Recording frames: paper ground, product in a white hairline frame, the mark 48px bottom-right.
- Captions: Plex Sans 500 at 44px, Paper on navy at 90%, at least 160px above the bottom edge.
- Motion: lines draw in (800ms), then the gold lot fills; standard ease, no bounce.

**Don't:** stock footage, gradients, glitch or 3D transitions, real customer names or data on screen.
