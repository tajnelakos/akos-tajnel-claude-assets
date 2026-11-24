# Print production

Values a printer will ask for, and the checks to run before a file leaves the building. The tokens in the `print` group of `tokens.json` hold the same numbers.

## Formats

| Piece | Trim | Folded | Panels | Margin |
|---|---|---|---|---|
| Trifold (roll fold) | 297 × 210 mm | 100 × 210 mm | Outside: 97 · 100 · 100 mm. Inside: 100 · 100 · 97 mm | 8 mm from every fold and trim |
| Postcard / recto flyer | 210 × 148 mm (A5) | — | Front and back | 12 mm |
| One-pager | 210 × 297 mm (A4) | — | One or two sides | 12 mm sides and foot; 19 mm top for the motif band |

The trifold's inner flap is 3 mm narrower so it folds in without buckling. Check the printer's fold allowance: some ask for 98 mm on 170 gsm and heavier.

## Bleed and safe zones

- **Bleed: 3 mm** on every edge. Navy grounds and motifs run into it. Wrap a sheet in `.pwf-print` to add it in HTML; each ground and motif extends by 3 mm.
- **Safe zone: 5 mm** inside the trim is the hard limit for any text, logo or QR. The layouts keep 8 mm (trifold) and 12 mm (cards) for comfort.
- Nothing readable crosses a fold.

## Colour

| Token | HEX | CMYK (standard conversion) | Note |
|---|---|---|---|
| Navy | #1A3A5C | 72 · 37 · 0 · 64 | Large grounds: ask for a wet proof; navy shifts on uncoated stock |
| Gold | #C1892E | 0 · 29 · 76 · 24 | Marks only on paper |
| Gold light | #D9A54B | 0 · 24 · 65 · 15 | Gold on the navy ground |
| Ink | #1C1C1A | 0 · 0 · 7 · 89 | Body text. Do not build small text from four colours |
| Paper | #F4F3EF | 0 · 0 · 2 · 4 | Print as a tint, or use an off-white stock and leave it unprinted |
| Grey text | #5B6470 | 19 · 11 · 0 · 56 | Secondary text |

CMYK values are mathematical conversions. Before a run, ask the printer to convert from the RGB PDF with their profile (for example PSO Coated v3 or PSO Uncoated v3 in Europe) and send a proof.

- Total ink on the navy ground stays under 300%.
- Text under 12pt in one plate only (Ink as K-heavy black, Paper as knocked-out stock).
- Hairlines are 0.5pt; anything thinner breaks up in print.

## Paper

- Trifold: 170 gsm silk or uncoated, scored before folding.
- Postcards: 350 gsm uncoated or silk; matt laminate on the navy side if it will be posted.
- One-pager: 120–150 gsm uncoated, so it can be written on.

Navy on uncoated stock prints darker and duller; check the proof against the screen render.

## Images and QR codes

- Product screenshots at 300 ppi at final size: export the UI at 3× its screen size. Frame them with `.pwf-shot` (hairline, no shadow).
- QR codes at least 20 mm with a 4-module quiet zone, Ink on white, error correction M or higher. Scan the printed proof with two phones.
- Encode a short campaign URL with a tracking parameter (`?c=event-name`). Print the same URL without the parameter beside it.

## Exporting

**From the HTML (proofs and short digital runs):**
1. Open the example in Chrome. Print → Save as PDF, Margins: none, Background graphics: on. Each sheet sets its own `@page` size.
2. For bleed, wrap each sheet in `<div class="pwf-print">` and change `@page` to the trim plus 6 mm (303 × 216 mm for A4 landscape).
3. The result is an RGB PDF with fonts embedded; fine for proofs and most digital presses.

**For offset print:**
1. Rebuild the layout in InDesign (or Affinity Publisher) from the tokens: page size, columns and type styles map one to one.
2. Place the outlined logo SVGs and the icon SVGs; install the three font families from `fonts/`.
3. Export PDF/X-4 with 3 mm bleed and crop marks, the printer's output intent, fonts embedded.

## Pre-press checklist

1. Trim, bleed and fold positions match the printer's template?
2. All text, logos and QR codes inside the safe zone and off the folds?
3. One logo per side, outlined, with its clear space?
4. One gold element per panel, side or page?
5. No type below 8pt (sans) or 7pt (mono)?
6. Every figure with its source line; "illustrative" where it is?
7. QR scans from the proof and lands on the right page?
8. Spelling and number formats right for the market (see `wording.md`)?
9. Proof signed off on the actual stock?
