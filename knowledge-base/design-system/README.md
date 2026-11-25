# Design System

## The problem

A brand guideline says what the brand *is*: values, colours, a logo, a type pairing. It rarely says how to *build* with it: what a moment looks like on screen next to its evidence, how big a headline is on a LinkedIn slide, how a currency is written in Swiss German, how a product video opens, or what colour a warning badge is when the brand's gold already means "look here". Without those answers, every new asset re-decides them, and the brand drifts one deadline at a time.

## The approach

The [`branding-guideline/`](../branding-guideline) folder stays the source of truth for identity and voice. This folder turns it into something an agent or a designer can build from directly:

- **Tokens** with exact values and a usage note on each, in light and dark themes, with every text pairing checked for contrast.
- **Components** as plain HTML and CSS, each with what the author provides and the rules that don't change. The signature one is `MomentCard`: a moment, the customer it points at, and the transaction, customer and market data behind it, so the brand promise (*opportunities you can act on — and explain*) is visible in the UI itself.
- **Channel rules** for the places the original guideline only covered in a line: LinkedIn carousels and captions, product video and motion, and product UI copy.
- **Assets** drawn to the guideline's own rules: a line-icon set at the specified stroke weight, and graphic motifs built from the logomark's idea (a moving dot map with a few peaks and one gold summit point).

The same system is published as a Claude design system, so Claude builds Seekridge slides, pages and mock-ups from it without being re-briefed.

## Files

| File | What it holds |
|---|---|
| [`tokens.json`](./tokens.json) | Every token: colour (light and dark), type scale, spacing, radius, shadow, line weights, social and video canvases. Each has a usage note. |
| [`report-theme.css`](./report-theme.css) | The shared look for every outward-facing page: Navy masthead with lockup, nav pills, bold hero, fact pills and the dot map in its own column, then 16px cards lifted over the band. |
| [`tokens.css`](./tokens.css) | The same tokens as CSS custom properties, plus a class per type style. Generated from `tokens.json`. |
| [`components.css`](./components.css) | Styles for all components (`pw-` classes), reading the tokens. Imports the three Google Fonts. |
| [`components.md`](./components.md) | Guidelines for each component: Button, FormField, Card, StatusBadge, Alert, DataTable, StatTile, MomentCard, PricingTier, CarouselSlide, VideoFrame. |
| [`components.html`](./components.html) | A live page rendering every component and colour token, with a light/dark switch. |
| [`writing.md`](./writing.md) | Full wording rules: golden rules, names and terms, case, numbers and currency, market typography (DACH, Benelux, Nordics), inclusive language, product copy. |
| [`social-and-carousels.md`](./social-and-carousels.md) | LinkedIn in one page; the full carousel system (formats, slide CSS, assets, wording, captions, skill) is [`../linkedin-carousels/`](../linkedin-carousels). Canvas, grounds, type sizes, logo and swipe furniture, seven carousel formats, story shape, caption anatomy, pre-post check. |
| [`video-and-motion.md`](./video-and-motion.md) | Video formats and story structure, key frames, captions, motion tokens and easing, sound, production rules: the one-page summary of [`../video-design-system/`](../video-design-system), which holds the full film book, components and reference films. |
| `icon-*.svg` | 16 line icons (moment, evidence-trail, customer, transaction, savings, market, coverage-map, bank, agent, compliance, crm-sync, data-residency, check, alert, arrow-right, search): 24px grid, 1.75px stroke, no fills, navy. |
| `motif-*.svg` | 3 dot-map motifs: `ridge-lines` (covers, title cards), `ridge-strip` (headers), `ridge-frame` (dividers). |

Logos and the palette and logo-usage reference sheets stay in [`branding-guideline/`](../branding-guideline). Print pieces (trifolds, postcards, one-pagers) have their own system in [`flyer-design-system/`](../flyer-design-system).

## How to use it

1. Read [`../branding-guideline/brand-guidelines.md`](../branding-guideline/brand-guidelines.md) for identity, voice and the visual rules.
2. Load `tokens.css` and `components.css`, then build with the `pw-` classes. Never paste hex values: use the variables.
3. For a LinkedIn post or a video, follow the channel file before designing anything.
4. Run the "Before you publish" checklist in the brand guideline.

## Decisions worth knowing

- **Status text uses darker `-ink` tokens.** The guideline's status hues are kept for icons and marks, because good (#0CA30C) and warning (#D68A1F) fall below 4.5:1 for small text on white.
- **Dark theme primary action is `gold-light`**, because a navy button disappears on a navy ground.
- **Currency codes before the number** (EUR 412,500), because the core markets mix EUR, CHF, SEK, NOK and DKK. Older files in this repo still use €.

## Current limitations

- Components are HTML and CSS only, not a React library.
- Fonts load from Google Fonts; there are no self-hosted font files.
- The logo SVGs still set the wordmark as live text, and the reversed logo carries its own navy background box. Outlined, transparent versions are the next step before print or app-store use.
