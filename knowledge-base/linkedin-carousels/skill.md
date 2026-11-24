---
name: seekridge-linkedin-carousel
description: Builds a finished Seekridge LinkedIn carousel (a PDF of 1080 × 1350 slides, PNGs of each slide, and the caption) from the Seekridge LinkedIn carousels design system in this folder. Use for any request to make, adapt or translate a Seekridge LinkedIn carousel or single image post. Requires a real angle (a sourced finding, a feature, a rule, an event or a positioning point of view), not a generic topic.
---

# Seekridge LinkedIn carousel

## Purpose

A carousel is the most designed thing Seekridge posts and the easiest place for the brand to drift: a gradient here, an unsourced number there, a cute feature name on the cover. This skill builds carousels from the system in this folder, so every slide uses the same grounds, type, furniture and wording rules, and every moment and figure carries its evidence.

## Before you start

Read, in this order: [`README.md`](./README.md) (the system), the chosen format's `components/<Format>/README.md`, [`wording.md`](./wording.md) and [`captions.md`](./captions.md). For the reader, use [`../personas.md`](../personas.md); for claims, [`../positioning.md`](../positioning.md).

## Instructions

1. **Require an angle and a reader.** A sourced finding (from [`win-loss-analysis`](../win-loss-analysis), [`sales-call-analysis`](../sales-call-analysis), a backtest), a feature that is live, a rule, an event, or a point of view from `positioning.md`; and one persona. "Make a carousel about our product" with nothing behind it is a prompt to ask for the angle, or to suggest one from recent repo data.
2. **Choose the format** by the job: explain → MomentExplainer; correct a belief → MythVsMethod; prove → ProofInNumbers; launch → FeatureLaunch; regulation → RegulationBrief; invite → EventInvite; checks or steps → FieldGuide. If none fits, compose from **SlideKit** and say which archetypes you used.
3. **Write the slides before designing anything**, as a table: slide number, archetype, ground (navy or paper), eyebrow, title, supporting line, proof element, gold element. Follow question → tension → method → proof → action, one idea per slide, the length limits in `wording.md`, and one gold element per slide.
4. **Check every claim** against its source. Every figure gets what it measures and a source line, or "illustrative". Every moment shown gets its evidence rows with weights. Remove any claim you can't trace; flag it for the user rather than softening it.
5. **Write the caption** to `captions.md`: hook (situation or sourced fact, different from the cover), what changes as a benefit, proof or detail, one CTA with one link placeholder. 50–110 words, no hashtags.
6. **Build the slides in HTML.** One file, one `.pwc-slide` per slide at 1080 × 1350, linking `tokens.css` and `components/bundle.css`. Start from the format's `preview.html` and keep its positions; change copy, not geometry. Add `pwc-slide--paper` for paper slides. Use only `pwc-` classes and the token type classes; never paste hex values or add new colours, fonts, radii or shadows.
7. **Render and export.** Render each slide at 1080 × 1350 with a headless browser (wait for the fonts to load), save a PNG per slide, and combine them into one PDF, one page per slide. A single post is one PNG.
8. **Look at every slide** at full size and at phone size (about 360px wide). Check: nothing outside the 96px margin except a motif; no text under 28px; no line too long for its style; the footer row (counter, arrow, mark) clear of content; one logo and one gold element per slide; no arrow or counter on the last slide.
9. **Run Before you publish** from the README, then [`positioning-compliance`](../../marketing-assets/positioning-compliance) on the slide copy and the caption together.
10. **For a translation**, localise rather than translate: follow the market table in `wording.md`, step down to `title-long` where German or Dutch runs long, and re-render and re-check every slide.

## What to avoid

- Gradients, glows, shadows, tints of navy, rounded pills or any colour outside the token list.
- A moment without its evidence, a figure without its source, or real customer data.
- Gold text on paper, more than one gold element on a slide, or a figure set in gold.
- Opening the cover or the caption with the product name, "We're excited", a rhetorical question or urgency.
- Inventing feature names, dates, prices or results.
- Naming a competitor or a prospect.

## Output format

```
## LinkedIn carousel — [format] — [angle, one line]

Reader: [persona] · Slides: [n] · Language: [EN-GB / DE / …]

| # | Archetype | Ground | Eyebrow | Title | Supporting line / proof | Gold |
|---|---|---|---|---|---|---|
| 1 | … | navy | — | … | … | motif lot |

Caption ([n] words):
[hook]

[what changes]

[proof or detail]

[CTA]: [link]

Files: carousel.pdf · slide-01.png … slide-0n.png · carousel.html
Sources: [each figure and where it came from]
Illustrative: [what is illustrative]
Compliance: positioning-compliance [pass / flags]
```
