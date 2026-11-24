Parcelwise in print: claims in Paper on flat Navy, the evidence on Paper, and one gold lot that marks the thing that matters. Use this system for the A4 trifold, A5 postcards and recto flyers, the A4 one-pager leave-behind, and any event handout that has to sit beside them.

It applies the Parcelwise brand guideline ([`../branding-guideline/`](../branding-guideline)) and design system ([`../design-system/`](../design-system)) to print. Where those files and this one disagree, the brand guideline wins.

## Why a flyer system

Print is where the brand promise is hardest to keep. A flyer has a few seconds and no click-through, so the easy move is a glowing hero image and a big unsourced number. Parcelwise sells to risk-minded buyers who distrust exactly that. This system makes the defensible version the easy one: every signal on paper shows its evidence, every figure carries its source, and the layouts are already measured for trim, folds and bleed.

The formats and their logic were modelled on the PriceHubble Flyer Design System (A4 trifold, A5 cards, panel-based insides). The look, the components and the rules are Parcelwise's own.

## Files

| File | What it holds |
|---|---|
| `tokens.json` · `tokens.css` | Colour (Paper and Navy ground themes), type for three formats, spacing, radius, line weights and print production values. Sizes are stored in px at 96 dpi so the CSS and the Claude design-system page read them; each usage note opens with the print value in pt or mm. Each token has a usage note; contrast ratios are in `meta.contrast`. |
| `components/bundle.css` | The `pwf-` print primitives, with logos, icons, motifs and the sample QR inlined. |
| `components/*/` | A README and a live preview for each component: 3 formats (Trifold, Postcard, OnePager), 2 surfaces (NavyGround, Logo), 7 content blocks (FeaturePanel, Benefit, FigurePanel, Step, LayerDiagram, EvidenceStrip, ContactBlock). |
| `wording.md` | How flyer copy is written: claims, CTAs, figures, market formats, words to avoid. |
| `production.md` | Trim, bleed, safe zones, folds, colour, paper, PDF export and the pre-press checklist. |
| `examples/` | Three finished pieces as HTML that prints at true size, plus PDFs and JPG renders in `assets/Examples/`. |
| `assets/` | Logos (outlined, transparent), line icons, motifs, arrows, the sample QR and the example renders. |
| `fonts/` | Archivo, IBM Plex Sans and IBM Plex Mono (SIL Open Font License, `fonts/OFL.txt`). |

## Content fundamentals

- **One reader per piece.** Name them in the eyebrow ("For mortgage lenders", "For risk and compliance teams") and write everything else to them.
- **Lead with the reader's situation or the opportunity, then the proof.** The front states the outcome; the inside shows how it works and proves it with one signal and its evidence.
- **Sentence case everywhere**, covers included. The mono eyebrow is the one all-caps element, set in CSS.
- **Short, declarative claims.** One idea per line on the navy ground, up to 12 words on a trifold front and 8 on a postcard. No exclamation marks, no emoji.
- **Every figure says what it measures and where it came from**, in a source line under it. Illustrative figures say "illustrative".
- **Customers appear by ID** ("Customer 40-1187"), never by a name or an address.
- **Close with one action** that says what happens next ("Scan to book a backtest"), never "Learn more".
- The full rules, prohibited words and market formats are in [`wording.md`](./wording.md).

## Visual foundations

**Two grounds, never mixed in one panel.**
- *Navy ground* (`.pwf-navy`, `data-theme="dark"`): flat `navy`, Paper type, `navy-text` for supporting lines, the reversed logo. Trifold front and back, postcard fronts, recto flyers.
- *Paper* (default): `paper` ground with white panels and a 0.5pt hairline. Navy headings and figures, Ink body, `grey-text` for secondary text. The inside of every piece, card backs, the one-pager.

**Colour.** Navy and Paper do the work. Gold is a highlight, not a colour scheme: **one gold element per trifold panel, per card side, or per one-pager**. It is the motif's lot, the signal box's lot, the top evidence bar, one figure's rule, or up to three words of a claim on navy (`gold-light`). The logo's own lot doesn't count. Status colours never appear in print.

**No gradients, glows, tints or shadows.** The PriceHubble pieces use a blue gradient and a cyan halo behind a hero object; Parcelwise uses flat grounds and the parcel-grid motif instead, and a square diagram of its method in place of the glowing object.

**Contrast.** Every text pairing passes WCAG AA: Ink on Paper 15.4:1, Navy on Paper 10.5:1, `grey-text` on Paper 5.4:1, Paper on Navy 10.5:1, `navy-text` on Navy 5.8:1, `gold-light` on Navy 5.2:1. Gold on Paper is 2.7:1, so it is marks only, never text.

**Type.** Archivo for claims, headings and figures (600–800); IBM Plex Sans for copy and labels (400–600); IBM Plex Mono for eyebrows, weights, IDs and source lines only. Sizes are set per format (in pt for print, stored as px): `tri-*` for the trifold, `card-*` for A5, `page-*` for the one-pager, and shared small styles. Floors: 8pt for sans text, 7pt for mono source lines.

**Layout.**
- Trifold: panels of 100, 100 and 97 mm (the flap folds in); text 8 mm (`space-4`) from every fold and trim; lower blocks anchored to the panel foot so the three inside panels share a top and bottom line.
- A5 and one-pager: 12 mm (`space-5`) margins; lockup top-left; statement in the lower half of a front.
- Back panels and card backs end with the `ContactBlock`.

**Shape.** Square. Panels and image frames take `radius-sm` (0.5 mm), everything else `radius-none`. No pills, no circles, no discs: numbers sit in square tiles, the URL sits on a line with an arrow.

**Motifs.** One per side, anchored to an edge and bleeding off it, never behind text: `parcel-grid` top-right on navy fronts, `plot-strip` along the top of a one-pager, `layer-stack` where the three data layers need a picture rather than a diagram.

**Imagery.** Real product screens printed at 300 ppi in a hairline frame, the LayerDiagram and the EvidenceStrip. No stock photography, no 3D renders, no illustration of people at screens.

## Iconography

- The Parcelwise line icons: 24 grid, 1.75 stroke, square caps, no fills. Navy on paper (`-navy` files), Paper on navy (`-paper` files). `.pwf-icon` picks the right one from the ground.
- Sizes: 6 mm beside a panel title, 9 mm above a benefit, 4 mm in evidence rows and chips.
- The three data layers always use `customer`, `market` and `parcel`.
- Never fill, recolour, put an icon in a disc, or mix in another set.

## Logo

- The lockup goes top-left on fronts and on the one-pager (40 mm, or 32 mm on a trifold panel); the mark (10 mm) only on a side that carries no lockup, such as a postcard back.
- One logo per side. Clear space equals the mark's height. Outlined files only in print.

## How to build a piece

1. Pick the format and the one reader. Copy the closest file in `examples/`.
2. Write the copy first, to [`wording.md`](./wording.md): eyebrow, claim, problem, three pillars, one signal with evidence, up to three sourced figures, one action.
3. Build from the components; never paste hex values or px sizes.
4. Print to PDF from Chrome (margins none, background graphics on), or rebuild in InDesign from the tokens, then follow [`production.md`](./production.md).
5. Run the "Before you publish" checklist in the brand guideline and the pre-press checklist in `production.md`.

## Examples

| Piece | HTML | PDF | Render |
|---|---|---|---|
| A4 trifold for mortgage lenders | `examples/trifold-mortgage-lenders.html` | `assets/Examples/trifold-mortgage-lenders.pdf` | `assets/Examples/trifold-outside.jpg`, `trifold-inside.jpg` |
| A5 postcard on explainable signals | `examples/postcard-explainable-signals.html` | `assets/Examples/postcard-explainable-signals.pdf` | `assets/Examples/postcard-front.jpg`, `postcard-back.jpg` |
| A4 one-pager for risk teams | `examples/one-pager-risk-teams.html` | `assets/Examples/one-pager-risk-teams.pdf` | `assets/Examples/one-pager.jpg` |

Parcelwise is a fictional company and `parcelwise.example` is a reserved example domain. Every figure, customer ID and weight in this folder is illustrative.

## Current limitations

- The PDFs are trim-size RGB proofs from Chrome. A printer needs a PDF/X-4 with 3 mm bleed in their CMYK profile; `production.md` says how to get one.
- CMYK values are the standard conversion from the brand guideline, not a measured match. Ask for a proof on the chosen stock.
- The sample QR encodes `https://parcelwise.example/demo`; replace it per campaign.
