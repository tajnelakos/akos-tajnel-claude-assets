# LinkedIn posts and carousels

How Seekridge shows up on LinkedIn, in one page. The full system (seven formats and a slide kit, slide tokens and CSS, outlined logos, motifs, fonts, wording and caption rules, rendered references and a carousel-building skill) is [`../linkedin-carousels/`](../linkedin-carousels); where this page and that folder differ, the folder wins. Component: `CarouselSlide` in [`components.md`](./components.md).

## The canvas

- **1080 × 1350 px** (`canvas-carousel-w` × `canvas-carousel-h`, 4:5 portrait). Carousels export as one PDF, a page per slide; single posts as PNG.
- **Safe margin `canvas-margin` 96px** on every side. Nothing but a bleeding motif crosses it.
- **Length:** 4–8 slides: a cover, 2–6 middle slides, one close.
- **Minimum type on canvas: 28px**, about 10pt on a phone.

## Grounds

Two grounds only, flat, no gradients or glows:

- **Navy** (`navy`): covers, statements, figures, closes. Text in `paper`; supporting lines in paper at 72%; highlights in `gold-light` (5.2:1).
- **Paper** (`paper`): proof slides with product screenshots, tables, charts and checklists. Headings in `navy`, text in `ink`; gold as *shapes* (a 6px underline, the focus bar, the top weight), never gold text.

A carousel usually runs navy cover → navy argument → paper proof → navy close.

## Type on the canvas

| Style | Face | Size / line | Use |
|---|---|---|---|
| Cover title | Archivo 800 | 104 / 108 | 3 lines max, about 8 words |
| Question | Archivo 700 | 88 / 96 | Centred question on a hook or event cover |
| Statement | Archivo 700 | 80 / 88 | One claim, about 20 words (64 / 72 for German and Dutch) |
| Slide heading | Archivo 700 | 60 / 68 | Proof and list slides |
| Figure | Archivo 800 | 200 / 200 | One number per slide, with tabular figures, never gold |
| Body | IBM Plex Sans 400 | 40 / 54 (lead 44 / 58) | Up to 40 words |
| Eyebrow | IBM Plex Mono 500 | 28, uppercase, 0.08em | Topic or series label above the title, with a rule to the margin |
| Source | IBM Plex Mono 400 | 28 / 36 | Source line under any figure, chart or screenshot |

The full scale (18 styles) is in [`../linkedin-carousels/tokens.json`](../linkedin-carousels/tokens.json).

## Furniture

- **Logo:** lockup top-left on the cover; the mark (56px) bottom-right on every middle slide; lockup centred at the bottom on the close. One per slide. Use the outlined, transparent carousel versions in [`../linkedin-carousels/assets/Logo/`](../linkedin-carousels/assets/Logo).
- **Swipe cue:** a 160 × 48px arrow (4px line, open head), 32px left of the mark on middle slides and at the margin on the cover. Never on the last slide.
- **Eyebrow:** the series or topic ("Evidence trail", "Outflow Watch") top-left on middle slides.
- **Slide counter** in mono, bottom-left, `02 / 06` beside a strip of squares, the current one filled.
- **Motif:** one per slide, anchored to an edge: `ridge-lines` on covers, `ridge-strip` along the top of a data slide, `layer-stack` on a Moment explainer cover. A motif's gold point is the slide's one gold element.

## Formats

| Format | Job | Slides |
|---|---|---|
| **Moment explainer** | Show how one moment is built | Question cover → tension → the three data layers → the evidence → what the banker does → close |
| **Myth vs method** | Correct a market belief | Correction → the belief → why it fails under scrutiny → what defensible looks like → close |
| **Proof in numbers** | One backtest or result | Figure cover → what it measures → chart → method → limits → close |
| **Feature launch** | A new capability | "New in Evidence Trail" cover → problem → screenshot proof ×1–2 → close |
| **Regulation brief** | What a rule change means for banks | Rule as a question → what it says → what it asks → what to prepare → where Seekridge fits → close |
| **Event invite** | Meet the team | Question cover → talk → speaker → date, place and one button |
| **Field guide** | Checks, steps or questions | Count cover → one item per slide → checklist → close |

Mix freely with the slide kit; keep one arrow style, one logo per slide and one gold element per slide. Each format's guidelines and preview: [`../linkedin-carousels/components/`](../linkedin-carousels/components).

## Story shape

**Question → tension → method → proof → action.** For example: "Which of your customers are moving money out this quarter?" → "Most scoring tools give you a list, not a reason." → "Seekridge shows the transfers, the income and the market behind each moment." → screenshot of a moment with its evidence → "Run a backtest on your own data."

## The caption (50–110 words)

1. **Hook (1–2 lines):** the situation or a sourced fact, never "We're excited to announce", and different from the cover.
2. **What changes, as a benefit (2–3 lines):** name the feature once.
3. **Proof or detail (1–2 lines):** the figure with its source, the method, or the logistics.
4. **CTA + one link:** a plain verb ("See a sample moment: [link]"), with UTM tags.

No hashtags; tag people and organisations instead. At most one emoji, only at the end of a line, and only in captions. Never on slides. Full rules: [`../linkedin-carousels/captions.md`](../linkedin-carousels/captions.md).

## Before you post

1. Does the cover name the reader's situation or the news in under 10 words?
2. One idea, one logo and (except the last) one swipe cue and counter per slide?
3. Every moment with its evidence, every figure with a source line or "illustrative"?
4. One gold element per slide, gold text on navy only, 3 words at most?
5. Caption hook different from the cover, one link, no hashtags?
