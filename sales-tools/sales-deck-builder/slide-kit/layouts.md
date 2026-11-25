# Slide kit: layouts

The Seekridge sales deck slide kit. Every slide is a 1920 × 1080 HTML canvas, styled by [`slides.css`](./slides.css), which reads the brand tokens from [`../../../knowledge-base/design-system/tokens.css`](../../../knowledge-base/design-system/tokens.css) and loads Archivo, IBM Plex Sans and IBM Plex Mono from the repo's own font files. That way a PDF export renders the same offline.

The reference deck, [`../deck-retail-banks.html`](../deck-retail-banks.html), uses every layout below. Copy a slide's `<section>` from it, then change the words.

## Rules every slide keeps

- **One idea per slide,** and the headline says it as a full sentence ending in a full stop. Sentence case. 76 px Archivo ExtraBold (104 px on statement slides).
- **A mono eyebrow above every headline** names the section ("The challenge", "How it works"). It acts as the deck's chapter marker, so there's no separate agenda slide.
- **Two grounds only: navy and paper.** Alternate them to pace the story. Put the big emotional beats on navy and the dense proof on paper.
- **One gold element per slide:** the summit point, one card, one label or one highlighted row. Gold *text* only appears on navy.
- **Benefit before feature.** The headline says what the lender gets. Feature names (Evidence Trail) go in the eyebrow or the body.
- **Every figure keeps its source line** (`.source`), or the word "illustrative".
- **Speaker notes** go in `<aside class="notes">` on each slide. They're hidden when you view or print the deck.
- **Footer** on every slide except the cover and the close: the lockup on the left, the page number on the right.

## Layouts

| # | Layout | Ground | Use it for | You provide |
|---|---|---|---|---|
| L1 | **Cover** | Navy | The opening promise | Eyebrow (who it's for), headline with a gold accent on the last words, one-line lead, meeting line in the footer |
| L2 | **Quiet book** | Navy | The challenge: the opportunity exists but nobody sees it | Headline, a two-line lead, 3–5 muted moment labels with question marks on a low ridge |
| L3 | **Four cards** | Paper | What the buyer gets: levers, use cases, benefits | Four short verb tags (Keep, Win, Lend, Insure), a headline per card, one sentence each. The first card is navy with the one gold icon |
| L4 | **Statement** | Paper or navy | A single line to say slowly: why now, a point of view | One headline at 104 px, one lead, a ridge band along the bottom |
| L5 | **Moments on the ridge** | Navy (paper variant) | The hero: moments rising out of the customer base | 3–5 peaks. Each label has a pill (what happens in the customer's life) and a line under it (the conversation it opens). The most urgent one is gold |
| L6 | **Data layers** | Navy | How it works: three data sources converge into one moment | Three layer rows (icon, name, what's in it) and one moment card with one evidence point per layer |
| L7 | **Split with product** | Paper with a navy panel | A differentiator shown in the product | Headline, lead, a one-line kicker, a product card on the navy panel (Evidence Trail with weights, a moment card) |
| L8 | **Moment → product → owner** | Paper | How moments turn into sales | 3–5 rows: moment, product with its "Why:", and who acts (advisor, digital campaign, partner). One gold owner cell |
| L9 | **Steps and product** | Navy | Implementation or workflow | Three numbered steps (a verb-first title and one line each) and a product list card |
| L10 | **Benefits with outcome** | Navy | What changes, in three steps and the result | Three cards with a step label and one gold outcome card |
| L11 | **Figure and plan** | Paper | Proof: one number and how to prove it on their data | One figure with what it measures and its source, and three pilot steps with timing |
| L12 | **Three trust cards** | Paper | Security, compliance, data handling | Three navy cards, each an icon, a claim and one line of mechanism. No invented certifications |
| L13 | **Logo wall** | Paper | Social proof | Up to eight customer names. Use real logos only with approval. In this repo, all names are fictional |
| L14 | **Close** | Navy | The next step, as an action | Headline with a gold accent, what the next step is (length, data, outcome), who joins from their side, and the rep's contact |
| L15 | **Divider** | Navy | Section breaks and the appendix | Eyebrow, headline, one line on what follows |

## Appendix variants

Keep two or three versions of the key visual slides in the appendix, so the rep can swap one in for the room in front of them:

| Variant | Replaces | Choose it when |
|---|---|---|
| **Ranked statement** ("212 customers to call. Not 40,000.") | L5 | The room thinks in numbers: a CFO or a head of distribution |
| **Moments on the ridge, paper ground** | L5 | Printed handouts or a bright room |
| **Moments forming** (dashed markers, early signs) | Follows L5 | A planning-minded audience. It shows the pipeline before the moments peak |
| **Three layers, one moment** (light, vertical) | L6 | A shorter or simpler pitch |

## The ridge illustrations

The dot-map mountains come from [`ridge.py`](./ridge.py). [`build-assets.py`](./build-assets.py) lists every ridge the deck uses: size, ground, and each peak's position, height and marker (`gold`, `dot`, `ring` for a moment still forming, or none). Run `python3 build-assets.py` to redraw them. It prints each summit's position, which the slide uses to place the moment labels.

Keep the ridge abstract: no map of a real place, no house icons, no heat-map colours, and at most one gold point.

## Export

Open the deck in a browser to present it; every slide scales to the window. To make the PDF, print to PDF (the page size is set to 1920 × 1080) or run headless Chromium with `page.pdf(width="1920px", height="1080px", print_background=True)`.
