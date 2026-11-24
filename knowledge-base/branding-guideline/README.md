# Branding Guideline

## The problem

Brand guidelines are usually a PDF nobody rereads after onboarding — and most of them only cover half the picture: voice rules with no visual identity, or a logo file with no naming conventions, split across whatever tool made them easiest to produce at the time. In practice, brand consistency breaks down in the small, high-volume stuff — a support-team blog post, a sales one-pager written under deadline, a button component built without checking the type scale — not the flagship campaign that gets three rounds of review.

## The approach

Two things live here, deliberately not merged: a **skill** that applies the voice rules as an active rewrite pass (below), and the **fuller brand system** those rules are one part of — mission, values, tone by channel, logo, color, typography, and naming conventions, with the actual visual assets alongside it, not described in prose only.

## Files — the rewrite skill

- [`skill.md`](./skill.md) — the Claude Skill definition, including the voice rules it applies (tone, style standards, anti-patterns, prohibited terms, substitutions)

## Files — the full brand system

- [`brand-guidelines.md`](./brand-guidelines.md) — mission, vision, brand values, tone-by-channel, logo rules, full color palette (HEX/RGB/CMYK) with text-safe status colors and a dark theme, type scale, UI/UX visual styles, spacing and radius, layout, motifs, data visualization, accessibility, naming conventions, image and icon style, writing mechanics, LinkedIn and video rules, and a pre-publish checklist
- [`logo.svg`](./logo.svg) — primary logo, for light backgrounds
- [`logo-reversed.svg`](./logo-reversed.svg) — white version, for dark backgrounds
- [`logo-mark.svg`](./logo-mark.svg) — icon alone
- [`logo-usage.svg`](./logo-usage.svg) — clear space, minimum size, and misuse reference sheet
- [`color-palette.svg`](./color-palette.svg) — the palette swatch reference

## Files — the design system

The build-ready version of this brand lives next door in [`../design-system/`](../design-system): tokens (light and dark), component CSS and a live [components page](../design-system/components.html), 15 line icons, 3 ridge-line motifs, and the full rules for writing, LinkedIn carousels, and video. `brand-guidelines.md` summarizes each of those and links to the detail.

## Current limitations

The rule set in `skill.md` is condensed to what generalizes across content types; a fuller internal terminology doc and a running library of examples pulled from top-performing published content are next to fold in. The logo files are hand-authored SVG with system-font fallbacks rather than production-ready files with text converted to outlines — the right next step before these ever left this repo for real print or app-icon use.
