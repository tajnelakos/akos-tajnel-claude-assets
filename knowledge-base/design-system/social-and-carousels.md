# LinkedIn posts and carousels

How Parcelwise shows up on LinkedIn: the canvas, grounds, type sizes, furniture, formats, story shape and caption, adapted to a phone screen and a two-second read. Component: `CarouselSlide` in [`components.md`](./components.md).

## The canvas

- **1080 × 1350 px** (`canvas-carousel-w` × `canvas-carousel-h`, 4:5 portrait). Carousels export as one PDF, a page per slide; single posts as PNG.
- **Safe margin `canvas-margin` 96px** on every side. Nothing but a bleeding motif crosses it.
- **Length:** 4–8 slides: a cover, 2–6 middle slides, one close.
- **Minimum type on canvas: 28px**, about 10pt on a phone.

## Grounds

Two grounds only, flat, no gradients or glows:

- **Navy** (`navy`): covers, statements, closes. Text in `paper`; highlights in `gold-light` (5.2:1).
- **Paper** (`paper`): proof slides with product screenshots, tables and charts. Text in `ink`; accents as gold *shapes* (a lot, a rule), never gold text.

A carousel alternates no more than it needs to: usually navy cover → paper proof → navy close.

## Type on the canvas

| Style | Face | Size / line | Use |
|---|---|---|---|
| Cover title | Archivo 800 | 104 / 108 | 3 lines max, about 8 words |
| Statement | Archivo 700 | 80 / 88 | One claim, about 20 words |
| Slide heading | Archivo 700 | 60 / 68 | Proof and list slides |
| Figure | Archivo 800 | 200 / 200 | One number per slide, with tabular figures |
| Body | IBM Plex Sans 400 | 40 / 54 | Up to 40 words |
| Eyebrow | IBM Plex Mono 500 | 28, uppercase, 0.08em | Topic or series label above the title |
| Source | IBM Plex Mono 400 | 28 / 36 | Source line under any figure or chart |

Emphasis: up to 3 words a slide in `gold-light` on navy, or a 6px gold underline on paper. Never a whole sentence.

## Furniture

- **Logo:** lockup top-left on the cover; the mark (56px) bottom-right on every other slide; lockup centred on the close. One per slide.
- **Swipe cue:** the `arrow-right` icon at 64px, bottom-right beside the mark position on narrative slides (mark moves top-right on those), never on the last slide.
- **Eyebrow:** the series or topic ("EVIDENCE TRAIL", "FOR INSURERS") top-left on middle slides.
- **Slide counter** in mono, bottom-left: `02 / 06`.
- **Motif:** `parcel-grid` on the cover only, bleeding off the top-right; the gold lot lands in the corner.

## Formats

| Format | Job | Slides |
|---|---|---|
| **Signal explainer** | Show how one signal is built | Question cover → the three data layers → the evidence → what the advisor does → close |
| **Myth vs method** | Correct a market belief | Claim → why it fails under scrutiny → what defensible looks like → close |
| **Proof in numbers** | One backtest or result | Figure cover → what it measures → how it's tested → limits → close |
| **Feature launch** | A new capability | "New in Evidence Trail" cover → problem → screenshot proof ×2 → close |
| **Regulation brief** | What a rule change means for banks and insurers | Rule → what it asks → what to prepare → how Parcelwise helps → close |
| **Event invite** | Meet the team | Question cover → topic → speaker or stand → date and place |

Mix freely; keep one arrow style, one logo per slide and one highlight colour.

## Story shape

**Question → tension → method → proof → action.** For example: "Which of your customers will refinance elsewhere this quarter?" → "Most scoring tools give you a list, not a reason." → "Parcelwise shows the rate reset, the equity and the market behind each signal." → screenshot of a signal with its evidence → "Run a backtest on your own book."

## The caption (50–110 words)

1. **Hook (1–2 lines):** the situation or a fact, never "We're excited to announce".
2. **What changes, as a benefit (2–3 lines):** name the feature once.
3. **Proof or detail (1–2 lines):** the figure with its source, or the logistics.
4. **CTA + one link:** a plain verb ("See a sample signal: [link]"), with UTM tags.

No hashtags; tag people and organisations instead. At most one emoji, only at the end of a line, and only in captions. Never on slides.

## Before you post

1. Does the cover name the reader's problem or the news in under 10 words?
2. One idea, one logo and (except the last) one swipe cue per slide?
3. Every figure real or labelled illustrative, with a source line?
4. Gold text only on navy, 3 words at most?
5. Caption hook different from the cover, one link, no hashtags?
