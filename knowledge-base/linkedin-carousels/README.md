# Parcelwise LinkedIn carousels

A system for designing Parcelwise LinkedIn carousels: one canvas, two flat grounds, three typefaces, one gold lot, seven formats and a slide kit for mixing them into new ones.

It sits on top of the brand. [`../branding-guideline/brand-guidelines.md`](../branding-guideline/brand-guidelines.md) says who Parcelwise is and how it looks; [`../design-system/`](../design-system) makes that build-ready for pages and product UI. This folder does the same for one channel, a 1080 × 1350 slide that is read on a phone in about two seconds. Where the two disagree on a carousel, this folder wins.

The formats are examples of what works, not a rulebook. Every post is different, so combine slides across formats, reorder them, or invent a new archetype, as long as it's built from the tokens and rules below. Start with **SlideKit** when a post doesn't fit a format cleanly.

## The canvas

- Every slide is **1080 × 1350 px** (LinkedIn portrait, 4:5). All sizes in this system are canvas pixels; a phone shows the slide at about a third of that.
- Export each slide as a page of one PDF for a swipeable carousel. A single post (one slide, no swipe) exports as PNG.
- Keep everything inside the **96px safe margin** (`canvas-margin`) on every side. Only a motif crosses it, and only by bleeding off an edge.
- **Carousel length: 4–8 slides.** A cover, 2–6 middle slides, one close.
- **Minimum type on the canvas: 28px**, about 10pt on a phone. Nothing smaller, including source lines and the slide counter.

## Content fundamentals

**Voice.** Confident and specific, never hyped, written for a technically sceptical reader in banking or insurance who trusts precision over enthusiasm. UK English. The brand's voice rules are in [`../branding-guideline/skill.md`](../branding-guideline/skill.md); **Writing for carousels** ([`wording.md`](./wording.md)) applies them to a slide.

- Write to *you* and *your customers*. Parcelwise is *we* only on the close and in the caption. Parcelwise is one word, capital P only, and never takes an article.
- **Lead with the reader's situation, not the product.** The cover names a customer situation or a fact ("Which customers will refinance elsewhere?"). The product name arrives in the middle, once.
- **Every claim names its mechanism, its data or its figure.** "Shows the rate reset, the equity and the market behind each signal", not "AI-powered insights". If a slide can't name the mechanism, it doesn't make the claim.
- **Signals always carry their evidence.** Any slide that shows a signal shows the data points behind it and how much each counted. This is the brand promise in one picture; never show a signal without it.
- Build the story as a sequence: **question → tension → method → proof → action.** For example: *"Which of your customers will refinance elsewhere this quarter?"* → *"Most scoring tools give you a list, not a reason."* → *"Parcelwise shows the rate reset, the equity and the market behind each signal."* → a signal with its evidence → *"Run a backtest on your own book."*
- **One idea per slide.** About 8 words for `title-cover`, 20 for `title-statement`, 30 for `title-long`, 40 for body copy or a white card.
- **Emphasis carries meaning.** Up to 3 words a slide in `gold-light` on navy, or under a 6px gold rule on paper. Never a whole sentence.
- **Sentence case, always**: every title, cover, heading, eyebrow, button, label and caption. The mono eyebrow is the one all-caps element, and it's set uppercase in CSS, typed in sentence case.
- **Numbers are proof, so they carry their source.** Every figure says what it measures and where it came from, in a mono source line under it ("Backtest on a lender's 2025 book, n = 18,400"). Illustrative figures say "illustrative". Currencies are three-letter codes before the number (EUR 412,500 · CHF 1.2m · SEK 3.4m), never symbols.
- **Say what doesn't hold.** A Proof in numbers carousel has a *Limits* slide. Admitting the edge of a claim is what makes the rest of it believable to this reader.
- No emoji, no hashtags, no links and no exclamation marks on slides. No urgency language ("don't miss", "act now"), no prohibited terms from the voice rules.
- **Localise, don't translate.** German and Dutch run 20–30% longer: step down from `title-statement` to `title-long` rather than narrowing the margins. Market typography is in [`wording.md`](./wording.md).

## Visual foundations

### Colour

- **Two grounds, both flat.** `navy` (#1A3A5C) for covers, statements, figures and closes; `paper` (#F4F3EF) for proof: screenshots, charts, tables and checklists. No gradients, glows, blurs or tints of navy as decoration. A typical carousel runs navy → paper → navy.
- **On navy:** text in `paper`; the single supporting line under a title in `paper-72`; hairlines, motif lines and empty lots in `paper-35`; panels in `navy-deep`, always outlined in `paper-35` (navy-deep on navy is only 1.1:1).
- **On paper:** headings, figures and numerals in `navy`; body in `ink`; secondary text and source lines in `ink-muted`; frame and card borders in `line`; inactive lots and outlines in `slate`.
- **Gold is one element per slide.** On navy, `gold-light` (#D9A54B, 5.2:1): up to 3 highlighted words, *or* the lot in a motif, *or* the top weight in an evidence trail. On paper, `gold` (#C1892E) as a shape only: the 6px underline, the focus bar in a chart, the top weight bar or a reason rule. Never gold text on paper (2.75:1). The lot inside the logo doesn't count.
- **Status colours never appear on slides.** Good, warning and critical belong to product UI. A chart's categories are navy, slate and one gold, never green and red.

### Typography

Three families, strict roles, all bundled in [`fonts/`](./fonts) (SIL Open Font License):

| Role | Family | Styles |
|---|---|---|
| Titles | **Archivo**, Bold (700) or ExtraBold (800) | `title-cover` 104 · `title-question` 88 · `title-statement` 80 · `title-long` 64 · `heading` 60 · `title-step` 56 |
| Figures | **Archivo** ExtraBold, tabular figures | `figure-hero` 200 · `numeral` 160 · `figure` 128 |
| Body | **IBM Plex Sans**, Regular (400) and SemiBold (600) | `body-lead` 44 · `body` 40 · `card-body` 36 · `card-title` 36 · `button` 36 |
| Data and labels | **IBM Plex Mono**, Regular and Medium | `data-label` 32 · `eyebrow` 28 · `source` 28 · `counter` 28 |

- Covers and closes run in Archivo ExtraBold; statements, headings and step headlines in Bold. There is no Regular-with-Bold-emphasis pattern: emphasis is gold, not weight.
- Line height is about 104% of size for covers, 110% for statements and headings, and 135% for body. Never set titles tighter, and use `text-wrap: balance` on every title.
- Figures are tabular (`font-variant-numeric: tabular-nums`) and never gold: the number is the proof, so it stays in the plain text colour. One `figure-hero` per slide.
- Mono is for data only: eyebrows, source lines, weights, table headers, the counter and IDs. Never a sentence in mono.
- **Never use another face**, and never all-caps outside the eyebrow and mono labels.
- Minimum size on the canvas: 28px.

### Layout and furniture

- **One logo per slide.** Cover: the lockup top-left at the margin (320 × 80px), `pw-lockup-paper.svg` on navy, `pw-lockup-navy.svg` on paper. Close: the lockup centred at the bottom margin. Every other slide: the mark (56 × 56px) bottom-right at the margin.
- **The arrow means "swipe".** One style, a 160 × 48px line with an open head (`stroke-arrow` 4px), paper on navy and navy on paper. On middle slides it sits 32px left of the mark; on the cover, where there is no mark, it sits at the margin. Never on the last slide.
- **Eyebrow:** the series or topic in mono, top-left at the margin on every middle slide, followed by a 2px rule to the right margin (`paper-35` on navy, `line` on paper). Typed in sentence case, set uppercase.
- **Slide counter:** bottom-left, `02 / 06` in mono beside a strip of 16px lots, one per slide, the current one filled. It replaces any "swipe" text and tells the reader how long the carousel is.
- **Content area:** from about y 192 (below the eyebrow) to y 1150 (above the footer row). Titles start high, not centred, except on question covers and the event invite.
- **Cards and frames:** white card (`radius-frame` 6px, 2px `line` border, padding 48px, ink text); navy-deep panel on navy (6px, 2px `paper-35`); outlined card (2px `paper-35`, no fill) for a belief or a "before"; screenshot frame (white, 2px `line`, 6px corners, full width between the margins, about 690–760px tall).
- **Placement:** statements, headings and lists left-aligned; questions, event details and the close centred. Partner artwork (an event or award mark) sits bottom-centre above the footer and is never placed on a white box.
- **Square, not soft.** 2px for lots and tags, 4px for the button, 6px for everything else. Never more, never pill-shaped. No shadows anywhere.

### Motifs

The parcel map is the brand's one graphic idea: land divided by straight lines, one lot highlighted in gold, top-right as in the logomark. Four cuts are drawn for the canvas, each in a navy-ground and a paper-ground version ([`assets/Motifs/`](./assets/Motifs)):

- `parcel-grid` (640 × 640): covers only, anchored top-right, its gold lot in the corner.
- `plot-strip` (1080 × 144): the top edge of a data slide; the eyebrow moves down to y 192.
- `layer-stack` (560 × 440): the three data layers, property, market and customer, as three flat plans with the signal lot on top. The cover of a Signal explainer.
- `scale-bar` (402 × 24): a surveyor's scale, no gold, under a limits statement or beside a source line.

One motif per slide, anchored to an edge, never behind text. A motif's gold lot is that slide's gold element, so a slide with a motif has no highlighted words.

### Imagery

- Real product surfaces first: a signal with its evidence trail, a weighting chart, an audit log, cropped to the one panel that proves the point, in a white frame.
- Mock-ups use skeleton bars (`line`) and clearly illustrative data. Customers appear by ID ("Customer 40-1187"), never by a name or an address.
- Icons are the brand's line icons (1.75px on a 24px grid, scaled to 48–64px on the canvas), paper on navy and navy on paper or white. Property, market and customer always use the parcel, market and customer icons.
- Third-party marks (event organisers, award bodies, client logos) come from their official files and are never redrawn. Client logos need written approval.
- No stock photography, no illustrations of people at screens, no 3D or isometric scenes. A speaker appears only as a real square headshot with 6px corners.

## Logo

[`assets/Logo/`](./assets/Logo). The carousel versions are outlined (the wordmark is drawn as paths, not live text) and have transparent grounds, so they sit directly on either slide ground:

- `pw-lockup-paper.svg`: covers and closes on navy.
- `pw-lockup-navy.svg`: covers and closes on paper.
- `pw-mark-paper.svg` and `pw-mark-navy.svg`: the corner mark on every other slide.

Never recolour, outline, stretch or add effects to the logo. Keep clear space equal to the mark's height around the lockup: at 80px tall, nothing comes within 80px of it except the slide edge's margin.

## Formats

| Format | Job | Signature slides |
|---|---|---|
| **SignalExplainer** | Show how one signal is built | Question cover with the layer stack · three data layers · the evidence trail · what the advisor does |
| **MythVsMethod** | Correct a market belief | The correction as a cover · the belief in an outlined card · why it fails · what defensible looks like |
| **ProofInNumbers** | One backtest or result | Figure cover · what it measures · a one-gold-bar chart · method · limits |
| **FeatureLaunch** | A new capability | "New in Evidence Trail" cover · the problem · screenshot proof on paper |
| **RegulationBrief** | What a rule means for lenders and insurers | The rule as a question · what it asks · what to prepare · where Parcelwise fits |
| **EventInvite** | Meet the team or hear a talk | Centred question · the talk · the speaker · date, place and one button |
| **FieldGuide** | Checks, steps or questions | Count cover · numeral + white card per item · checklist on paper |
| **SlideKit** | Anything else | Mix-and-match archetypes: five covers, statements, beliefs, layers, figures, list items, evidence, screenshots, charts, tables, checklists, speaker, invite, closes |

Each format has a long README (what you provide, build rules, what not to do) and a preview in [`components/`](./components). Rendered examples are in [`assets/References/`](./assets/References).

Mixing is encouraged: a feature launch can open with a Myth vs method belief, a field guide can close on a figure, an event invite can borrow the evidence panel. Keep one arrow, one logo per slide and one gold element per slide.

## Files

| File | What it holds |
|---|---|
| `README.md` | This guide. |
| [`tokens.json`](./tokens.json) | Every token with a usage note: 12 colours, 18 type styles, spacing, radius, stroke. |
| [`tokens.css`](./tokens.css) | The same tokens as CSS variables, a class per type style, and the `@font-face` rules. Generated from `tokens.json`. |
| [`components/bundle.css`](./components/bundle.css) | The slide kit: grounds, furniture, cards, frames, evidence rows, checklists, charts (`pwc-` classes). Images inlined, so a slide draws without the asset folder. |
| `components/<Format>/` | A long README and a `preview.html` board per format, plus the system's cover card. |
| [`wording.md`](./wording.md) | Writing for carousels: golden rules, names and terms, case, numbers, market typography, inclusive language. |
| [`captions.md`](./captions.md) | Writing the LinkedIn caption that carries what the slides leave out. |
| [`skill.md`](./skill.md) | The Claude Skill that builds a finished carousel from this system. |
| [`example.md`](./example.md) | A worked Signal explainer carousel: slide-by-slide copy, layout choices and caption. |
| [`manifest.json`](./manifest.json) | The package manifest used to publish this folder as a Claude design system. |
| `assets/` | Logo, arrows, icons and motifs as SVG; rendered references as JPG. |
| `fonts/` | Archivo, IBM Plex Sans and IBM Plex Mono (latin subsets, WOFF2) with their licence. |

## How to use it

1. Pick the job of the post and its one reader (see [`../personas.md`](../personas.md)), then the format.
2. Write the slides first, against [`wording.md`](./wording.md), and the caption against [`captions.md`](./captions.md).
3. Build each slide in HTML with `tokens.css` and `components/bundle.css` (start from the format's `preview.html`), or ask Claude with [`skill.md`](./skill.md).
4. Render at 1080 × 1350 and export one PDF, or a PNG for a single post.
5. Run **Before you publish**, then [`positioning-compliance`](../../marketing-assets/positioning-compliance) as the final check.

## Before you publish

1. Does slide 1 name the reader's situation or the news in under 10 words, for one persona?
2. Does every slide carry exactly one idea, one logo and (except the last) the arrow and the counter?
3. Archivo, IBM Plex Sans and IBM Plex Mono only? Sentence case, Parcelwise without an article, literal feature names?
4. Navy and paper grounds only, flat? One gold element per slide, gold text on navy only?
5. Does every signal shown carry its evidence? Does every figure carry what it measures and a source line, or the word "illustrative"?
6. No real customer names or data, no stock photos, no partner logo without its official file and approval?
7. Is the German, Dutch or Nordic version rechecked for line length, typography and inclusive forms?
8. Does the caption carry the detail and the one link the slides leave out?
9. Proofread against **Writing for carousels**, then a colleague's second pair of eyes, then [`positioning-compliance`](../../marketing-assets/positioning-compliance).
