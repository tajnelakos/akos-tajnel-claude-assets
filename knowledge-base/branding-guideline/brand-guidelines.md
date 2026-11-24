# Brand Guidelines — Parcelwise

The full brand system: who we are, how we sound, and how we look. For the detailed voice/tone rules a rewrite skill actually applies, see [`skill.md`](./skill.md) — this document covers the fuller identity those rules serve, plus everything visual. See [`positioning.md`](../positioning.md) for the strategic narrative these guidelines express, and [`../design-system/`](../design-system) for the build-ready version of everything below: tokens, components, icons, motifs, and the full rules for writing, LinkedIn, and video.

---

## Core Identity

### Mission

Show banks, insurers, and brokerages the opportunities already inside their customer base — with the evidence to act on them.

### Vision

A market where every automated customer decision — not just Parcelwise's — can withstand scrutiny, so "the model said so" stops being an acceptable answer anywhere in banking and insurance.

### Brand values

1. **Defensible over impressive.** A claim that survives being questioned beats a claim that only sounds good in a demo.
2. **Precision, not hype.** Say exactly what the product does. If we can't name the specific mechanism, we don't make the claim.
3. **Transparency by default.** Show the work — the data points behind each moment, how much each counted, the method — rather than asking for trust.
4. **Respect the skeptic.** Our best-fit buyer is trained to distrust vendor claims. That skepticism is correct more often than not, and we build and write for it rather than around it.
5. **Substance before speed.** Volume and speed are real value, but never the whole pitch — see [`positioning.md`](../positioning.md)'s "what this is not."

### Brand voice and tone

Full rules (style standards, anti-patterns, prohibited terms, approved substitutions) live in [`skill.md`](./skill.md) — summarized here: confident and specific, never hyped, written for a technically skeptical, regulator-adjacent reader who trusts precision over enthusiasm.

Tone shifts by channel, but the underlying values above never do:

| Channel | Tone | What changes |
|---|---|---|
| Marketing pages | Confident, declarative | Leads with the claim; still no hype language or unexplained AI claims |
| Sales decks | Persona-adapted | Structure and emphasis change by buyer (see [`personas.md`](../personas.md)); the voice rules don't |
| Support / product emails | Direct, plain, helpful | Shorter sentences, no persuasion register at all — a support email that sounds like marketing copy erodes trust fast with this audience |
| Sales conversation / call | Consultative, willing to say "I don't know, let me find out" | The one channel where admitting a limitation live is a trust *builder*, not a liability — see the sales-call-analysis examples in [`../sales-call-analysis`](../sales-call-analysis) |
| Internal docs (this repo included) | Direct, reasoned, can be more casual | Precision matters as much as externally; hype matters less |
| Social / conference presence | Minimal, factual | We don't chase attention with urgency language — see the Anti-patterns in [`skill.md`](./skill.md) |
| Product UI | Neutral, exact | Labels name the object ("Moments", "Evidence trail", never "Insights"); errors say what happened and what to do next — see [`writing.md`](../design-system/writing.md)'s Product copy |
| Video | Calm, declarative | One claim per scene, readable in three seconds, captions always on — see [`video-and-motion.md`](../design-system/video-and-motion.md) |

---

## Visual Identity

### Logo

- [`logo.svg`](./logo.svg) — primary lockup (mark + wordmark), for light backgrounds
- [`logo-reversed.svg`](./logo-reversed.svg) — white version, for dark/navy backgrounds
- [`logo-mark.svg`](./logo-mark.svg) — icon alone, for favicons, social avatars, and spaces too small for the wordmark
- [`logo-usage.svg`](./logo-usage.svg) — clear space, minimum size, and misuse reference sheet

**Clear space:** minimum clear space on every side equals the height of the mark itself. Nothing — text, edges, other logos — enters that space.

**Minimum size:** 24px height (digital) / 10mm (print) for the mark alone; below that, use the mark only, never the full lockup with the wordmark.

**On dark surfaces:** always use `logo-reversed.svg`. Never place the primary (navy) mark on a dark background at reduced opacity as a substitute.

**Don't** (see [`logo-usage.svg`](./logo-usage.svg) for each of these rendered):
- Stretch or distort the proportions
- Recolor outside the palette below
- Place it on a busy or low-contrast background
- Add a drop shadow, outline, or other effect
- Rebuild the wordmark in a different typeface
- Separate the mark from the wordmark arbitrarily (the icon alone is fine — see `logo-mark.svg` — but don't split the primary lockup and space its pieces independently)

**On slides and video frames:** one logo per slide or frame. Covers and title cards use the lockup, top-left inside the 96px safe margin; every other slide or frame uses the mark alone (56px on carousels, 48px on video), bottom-right inside the same margin. End cards use the reversed lockup, centred.

### Color palette

See [`color-palette.svg`](./color-palette.svg) for the swatch reference. CMYK values are the standard mathematical conversion — verify against your actual print profile before a physical print run.

| Role | Name | HEX | RGB | CMYK |
|---|---|---|---|---|
| Primary | Parcelwise Navy | `#1A3A5C` | 26, 58, 92 | 72, 37, 0, 64 |
| Secondary | Meridian Gold | `#C1892E` | 193, 137, 46 | 0, 29, 76, 24 |
| Neutral | Ink | `#1C1C1A` | 28, 28, 26 | 0, 0, 7, 89 |
| Neutral | Slate | `#8A8782` | 138, 135, 130 | 0, 2, 6, 46 |
| Neutral | Paper | `#F4F3EF` | 244, 243, 239 | 0, 0, 2, 4 |
| Status — good | — | `#0CA30C` | 12, 163, 12 | reserved for success states only |
| Status — warning | — | `#D68A1F` | 214, 138, 31 | distinct from Secondary on purpose — a status color should never double as the brand accent |
| Status — critical | — | `#D03B3B` | 208, 59, 59 | reserved for error/critical states only |

Primary and Secondary are for brand and marketing use. Status colors are reserved for product UI state (success/warning/error) and never repurposed as decoration — status color and brand accent stay visually distinct on purpose, so one never impersonates the other.

**Using the palette:**

- **Gold is a highlight, not a color scheme.** At most one gold element per view: the highlighted lot, the top data point in an evidence trail, an eyebrow rule, or up to three highlighted words. Gold is never body text on light backgrounds (3.05:1 on white); on navy, gold text uses the lighter `#D9A54B` from the reversed logo (5.2:1).
- **No gradients, glows, or tints of navy as decoration.** Flat fields only.
- **Status text uses darker ink values.** Good (`#0CA30C`) and warning (`#D68A1F`) fall below 4.5:1 as small text on white, so they stay as icons, dots, and chart marks; text and badges use the ink/background pairs below.

| State | Mark (icons, dots) | Text | Background |
|---|---|---|---|
| Good | `#0CA30C` | `#1F7A4D` | `#E9F5EE` |
| Warning | `#D68A1F` | `#9A6212` | `#FCF3E3` |
| Critical | `#D03B3B` | `#B33A2E` | `#FBEAE8` |

**UI support colors:** secondary text `#5B6470` (6.0:1 on white), hairline `#E1E0D9`, control borders Slate `#8A8782` (3.58:1, the minimum for an input's edge).

**Dark theme:** page `#0F1E2C`, surfaces `#16324A`, text Paper, secondary text `#AEB8C3`, hairlines `#2C4C6B`, and `#D9A54B` as the primary action — a navy button disappears on a navy background. Always the reversed logo. Full light/dark values with usage notes: [`tokens.json`](../design-system/tokens.json).

### Typography

- **Display / headings:** Archivo (weights 600–800). Used for logo wordmark, page titles, section headers.
- **Body:** IBM Plex Sans (weights 400–600). Used for all running text, UI labels, and email copy.
- **Data / mono:** IBM Plex Mono (weights 400–500). Reserved for dates, source citations, tabular figures, and code — never for prose.

| Use | Face | Weight | Notes |
|---|---|---|---|
| H1 / page title | Archivo | 700–800 | `text-wrap: balance`; never all-caps |
| H2 / section header | Archivo | 600–700 | |
| Body copy | IBM Plex Sans | 400 | ~65-character line length target |
| UI labels, buttons | IBM Plex Sans | 500–600 | Sentence case, never all-caps except small eyebrow labels |
| Eyebrow / small label | IBM Plex Mono | 500 | Uppercase with letter-spacing is the one place all-caps is correct |
| Data, dates, citations | IBM Plex Mono | 400 | `font-variant-numeric: tabular-nums` where digits line up in columns |

**Type scale** (size / line height, px):

| Style | Face and weight | Size | Use |
|---|---|---|---|
| Display | Archivo 800 | 56 / 60 | Marketing hero only, one per page |
| H1 | Archivo 700 | 40 / 46 | Page title |
| H2 | Archivo 700 | 28 / 34 | Section header |
| H3 | Archivo 600 | 20 / 26 | Card titles, sub-sections |
| Body large | IBM Plex Sans 400 | 18 / 28 | Lead paragraph |
| Body | IBM Plex Sans 400 | 16 / 24 | Running text, emails |
| Body small | IBM Plex Sans 400 | 14 / 20 | Dense UI, table cells, helper text |
| Label / button | IBM Plex Sans 500–600 | 14–15 / 20 | Form labels, buttons |
| Eyebrow | IBM Plex Mono 500 | 12 / 16, +0.08em | Uppercase label above a heading |
| Data / caption | IBM Plex Mono 400 | 14 / 20 · 12 / 16 | Figures, dates, source lines |

LinkedIn and video use larger, canvas-specific sizes — see [`social-and-carousels.md`](../design-system/social-and-carousels.md) and [`video-and-motion.md`](../design-system/video-and-motion.md). All three faces are free on Google Fonts.

This is the same type system already used across this repo's designed artifacts ([`competitor-monitoring`](../../sales-tools/competitor-monitoring)'s report, [`battlecard`](../../sales-tools/battlecard)'s cards, [`sales-call-analysis`](../sales-call-analysis)'s rollup) — those weren't a one-off design choice each time, they were this brand system applied consistently.

### UI/UX visual styles

So the product and marketing site read as one brand, not two:

- **Buttons:** square or minimally rounded corners (2–4px), never full pill-shaped by default. Primary action in Parcelwise Navy with white text; secondary action outlined, not filled. No gradient fills.
- **Forms:** labels above fields, not placeholder-only. Error state uses Status — critical with a text explanation, never color alone.
- **Cards:** hairline border (`#E1E0D9`-equivalent) over drop shadows — shadows read as decorative, not this brand's register. Flat, bordered panels over "floating" elevated cards.
- **Icons:** see Image and Icon Style below — the same line-weight rule applies inside the product UI, not just marketing.
- **Moments always carry their evidence.** Wherever the product shows a moment, the data points behind it and their weights are visible with it, not behind a click — the brand promise in UI form. See `MomentCard` in [`components.md`](../design-system/components.md).

### Spacing, radius, and lines

- **4px grid:** 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64. Card padding 24, gaps between cards 32, page sections 48.
- **Corners:** 2px (badges, checkboxes), 4px (buttons, inputs, cards — the maximum for anything clickable), 6px (large panels and image frames only, matching the logomark's corner). Never pill-shaped.
- **One line language:** 1px hairlines for borders and dividers, 1.75px strokes for icons, 2px for focus rings and active underlines — the same stroked construction as the logomark.
- **Shadows:** none on cards, panels, or buttons. One soft shadow exists for floating layers only (menus, dialogs), and they keep their hairline border too.

### Layout

- **Product UI:** 12-column grid, 24px gutters, content up to 1200px wide. Dense tables are fine; decoration isn't.
- **Documents and one-pagers:** a single ~680px text column, sections 48px apart, a source line under every figure.
- **Lead with the claim:** the first thing on any page, slide, or card is the point, not the setup.

### Motifs

The parcel map is the brand's one graphic idea: land divided by straight lines, one lot highlighted in gold, top-right — as in the logomark. Three cuts live in [`../design-system/`](../design-system):

- `motif-parcel-grid.svg` — navy field, Paper lines at 35%, one gold lot. Carousel covers, video title cards, slide backgrounds.
- `motif-plot-strip.svg` — a horizontal band of lots. Document headers, email banners, the top of a one-pager.
- `motif-lot-outline.svg` — navy outline with one gold lot. Section dividers, empty states.

One motif per surface, anchored to an edge and allowed to bleed off it, never behind running text.

### Data visualization

- Default series in Navy; the one series or bar the chart is about in Gold; everything else in Slate or tints of Navy. Status colors are never categories.
- Hairline gridlines, axis labels in IBM Plex Mono, a one-line takeaway as the title, and a source line under every chart.
- When a chart supports a moment, label each data point with its layer — property, market, or customer.

### Accessibility

- Text meets 4.5:1 against its background in both themes (3:1 for text 24px and above, control borders, focus rings, and icons).
- Never color alone: errors carry text, status badges carry a word, charts carry labels.
- Every focusable element shows a 2px focus ring with a 2px offset.
- Videos always carry burnt-in captions — most are watched muted.

---

## Content and Assets

### Naming conventions

- **Pricing tiers** (brokerage/seat-based product): **Plot** (entry), **Block** (mid), **Estate** (enterprise): a land-scale theme that grows with the customer, used consistently and only for this purpose (not reused as a generic naming device elsewhere).
- **Feature names:** literal and descriptive, never invented proper nouns or trademarked-sounding names. "Evidence Trail," not "TraceIQ™." "Coverage Map," not "SmartArea." This follows directly from the "precision, not hype" brand value — a cute feature name reads as marketing packaging on something that should read as infrastructure.
- **Product terminology (use consistently):**

| Use this | Not this |
|---|---|
| Moment | Lead, insight, alert |
| Evidence trail (the data points behind a moment) | Explainability report, transparency log |
| Audit log (the record of what was done with a moment) | Activity feed, history |
| Customer base | Database, leads |
| Property data · market data · customer data (the three data layers) | Big data, data lake |
| Valuation (as one data point inside a moment) | Appraisal, estimate |
| Bank / lender / insurer / brokerage | Client (in product copy — "client" is fine in casual internal use) |
| CRM | Sales tool, customer system |

### Image and icon style

- **No stock photography.** Especially no generic finance-stock clichés (handshakes, skyline photos, people pointing at monitors). This audience recognizes stock photography instantly and it reads as substance-free.
- **Prefer real product surfaces and data visualization** — an actual (or realistic mock) evidence-trail screenshot, a real moment-weighting chart — over any illustration standing in for the product.
- **Where illustration is needed** (e.g. a concept with no literal screenshot, like "data residency"), use abstract geometric illustration consistent with the logomark's style — flat shapes, no gradients, no 3D renders, no isometric-office-life scenes.
- **Icon style:** line icons only, 1.5–2px stroke weight, no fills, consistent corner radius. No skeuomorphic, glossy, or 3D icon sets. This matches the logomark's own construction (a stroked parcel map plus one solid highlighted lot) — the icon system and the logo should look like they were drawn by the same hand. A starter set of 15 icons drawn to this rule (1.75px on a 24px grid) lives in [`../design-system/`](../design-system) as `icon-*.svg`: moment, evidence-trail, customer, parcel, valuation, market, coverage-map, lender, policy, crm-sync, data-residency, check, alert, arrow-right, search.
- **Mock-ups:** realistic but clearly illustrative data. Customers appear by ID, never by a real name or address.

---

## Writing Mechanics

The voice rules live in [`skill.md`](./skill.md). The mechanics that sit underneath them — the same in every channel — are summarized here; the full rules, with examples and market-by-market tables, are in [`writing.md`](../design-system/writing.md).

- **Names:** Parcelwise is one word, capital P only, no article. Feature names are literal and capitalized as names (Evidence Trail, Coverage Map), with no article in English.
- **Case:** sentence case for every title, heading, button, label, cover, and caption. The mono eyebrow is the one all-caps element, set in CSS rather than typed in capitals.
- **Numbers:** every figure says what it measures and where it came from ("68% of flagged customers refinanced within 6 months — backtest on the client's 2025 book"). Illustrative figures are labelled as illustrative.
- **Currency:** the three-letter code before the number (EUR 412,500 · CHF 1.2m · SEK 3.4m), because the core markets use several currencies. Older files in this repo still use €; update them when they're next edited.
- **Dates:** 24 November 2026 in prose; 2026-11-24 in tables, exports, and the audit log.
- **Markets:** UK English (Oxford spelling). German uses „…“ and 412.500; Swiss German «…» and 412’500; the Nordics 412 500. German *Sie*, Dutch *u*, Nordic *du*.
- **Inclusive language:** *they / their* for generic people in English; neutral forms first in German (*Kundschaft*, *Mitarbeitende*). Never gender a generic advisor, customer, or policyholder.

---

## Channels

### LinkedIn posts and carousels

Full system: [`../linkedin-carousels/`](../linkedin-carousels) (formats, slide CSS, assets, wording, captions, and a skill that builds a finished carousel); one-page summary: [`social-and-carousels.md`](../design-system/social-and-carousels.md).

- **Canvas:** 1080 × 1350 px (4:5), 96px safe margin, 4–8 slides (cover, 2–6 middle slides, one close). Minimum type on the canvas is 28px.
- **Grounds:** flat Navy for covers, statements, and closes; flat Paper for proof slides with screenshots, tables, and charts. No gradients or glows.
- **Furniture:** lockup on the cover and the close, the mark bottom-right on every other slide, a swipe arrow on every slide but the last, a mono eyebrow and a slide counter on middle slides. One parcel-map motif at most per slide: the parcel grid on covers, the plot strip or layer stack on data and explainer slides.
- **Story shape:** question → tension → method → proof → action. One gold element per slide: up to three highlighted words in `#D9A54B` on Navy, or a motif's lot, or the top weight in an evidence trail.
- **Formats:** moment explainer, myth vs method, proof in numbers, feature launch, regulation brief, event invite, field guide, plus a slide kit for mixing them.
- **Caption:** 50–110 words in four blocks — hook, what changes (as a benefit), proof or detail, one CTA with one link. No hashtags; at most one emoji, never on slides.

### Video and motion

Summary rules: [`video-and-motion.md`](../design-system/video-and-motion.md). The full system for film (formats, beat structures, components, reference films and the skill that builds them): [`../video-design-system/`](../video-design-system).

- **Formats:** 1920 × 1080 master (45–75 s), 1080 × 1350 social cut (30–45 s), 1080 × 1920 vertical (15–30 s); 30 fps; one video per segment and persona.
- **Structure:** hook (the customer situation) → tension (what goes wrong today) → method (product panels rebuilt in code from the real screens, through the three data layers, ending on a moment with its evidence trail) → proof (one backtest figure with its source) → end card (lockup, "Opportunities you can act on — and explain.", one action, held three seconds).
- **Captions:** always burnt in, IBM Plex Sans 500 at 44px on a Navy band (a Paper band on Navy frames), left-aligned, two lines maximum, at least 160px above the bottom edge.
- **Motion language:** straight, exact, no bounce — like a surveyor drawing a plan. Signature move: parcel lines draw in, then the gold lot fills. One easing curve (`cubic-bezier(0.2, 0, 0, 1)`); 150ms for UI feedback, 250ms for panels, 500ms for video text, 800ms for line draws. No spins, 3D flips, glitch effects, or stock footage. UI motion respects `prefers-reduced-motion`.

---

## Before You Publish

1. Does the first line name the reader's situation or the opportunity, for the right persona, in plain words?
2. Is every claim specific — the mechanism, the data behind it, or the figure? Does every moment shown carry its evidence? No prohibited terms from [`skill.md`](./skill.md)?
3. Navy, Gold, and the three neutrals only (status colors in product UI only)? One gold highlight per view?
4. Archivo, IBM Plex Sans, and IBM Plex Mono only? Sentence case? Mono only for data?
5. Square corners, hairlines, no shadows, gradients, or stock photos?
6. One logo, the right file for the background, with its clear space?
7. Figures real or labelled illustrative, formatted for the market, with a source? No real customer names or data?
8. Proofread against these rules (or run the [`skill.md`](./skill.md) rewrite pass), then a second pair of eyes — and [`positioning-compliance`](../../marketing-assets/positioning-compliance) as the final check before anything external ships.
