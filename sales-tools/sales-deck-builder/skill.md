---
name: sales-deck-builder
description: Builds a Seekridge sales deck for a specific buyer persona and deal stage. First a slide-by-slide outline to review, then designed 16:9 slides from the Seekridge slide kit (HTML, exported to PDF), with speaker notes and an appendix of alternative slides. Use when the user gives deal context and wants a tailored deck, not a generic one.
---

# Sales Deck Builder

## Purpose

Turn a few lines of deal context into a deck that fits the people in the room. The skill works in two stages:

1. **Outline:** headline, purpose and key point per slide, fast to sanity-check.
2. **Build:** once the outline is agreed, designed slides from the [slide kit](./slide-kit/layouts.md), in Seekridge's design system.

Stop after the outline if the user only asks for one.

## Stage 1: the outline

1. **Ask for, or infer from the context given, three things** before outlining: who's in the room (role and persona from [`personas.md`](../../knowledge-base/personas.md)), the deal stage (first meeting or late-stage/procurement), and any objection or theme already known from earlier calls. If the stage isn't given, assume "first substantive meeting".
2. **Match the structure to the persona, not just the content.** A risk or compliance buyer's deck leads with credibility and explainability before growth. A lending or distribution buyer's deck leads with the growth lever and the moment, and keeps method for later. Don't give both the same slide order just because the product is the same.
3. **Every slide gets three lines:** a headline (a full sentence, as the audience will read it, not an internal label), a purpose (why this slide is in this deck) and a key point (the one thing the rep must land). Name the kit layout it will use (L1–L15).
4. **Cap the main flow at 10–14 slides** for a first meeting, and up to 16 for late-stage decks that need more proof. Put everything else in the appendix. A long first-meeting deck is padded, not thorough.
5. **If the deal has a known objection or competitor, give it its own slide.** Don't leave it to come up out loud.
6. **End on one specific next step,** stated as an action with its length, its input and who joins ("A five-week backtest on a sample of your customers. Lending, risk and IT join"). Never end on "Thank you".

### The story shape that works for a first meeting

This is the arc both reference decks follow. Reorder it for the persona, but keep the logic:

1. **Promise** (cover): what the buyer gets, in their words. For example: "Find the peaks in your mortgage book."
2. **Challenge:** the opportunity already exists in their book, but their systems can't see it.
3. **What you get:** the business levers a head of lending recognises, before any mechanism.
4. **Why now:** a statement slide, one line to say slowly.
5. **The hero visual:** moments rising out of the customer base. Each label pairs *what happens in the customer's life* with *the conversation it opens for the bank*.
6. **How it works:** three data layers combining into one moment.
7. **The differentiator, shown in the product:** Evidence Trail.
8. **From moment to sale:** moment → product and why → who acts (advisor, digital campaign, partner).
9. **Workflow:** how it lands in the CRM they already use.
10. **Benefits:** three steps and the outcome they add up to.
11. **Proof:** one figure with its source, plus how to prove it on their own data.
12. **Trust:** security and compliance, as mechanisms, not badges.
13. **Customers like them.**
14. **Next step.**
15. **Appendix:** alternative versions of the key visuals.

## Stage 2: build the slides

1. **Read [`slide-kit/layouts.md`](./slide-kit/layouts.md)** and start from [`deck-retail-banks.html`](./deck-retail-banks.html). Copy the `<section>` for each layout in the outline, then rewrite the words. Don't invent new layouts while a kit layout fits.
2. **Use the design system as it is:** navy and paper grounds, Archivo headlines, IBM Plex Sans body, IBM Plex Mono eyebrows and source lines, the design-system icons, and one gold element per slide. Never paste hex values that aren't already in the kit.
3. **The illustration is the ridge** (the dot-map mountains), not stock imagery or icons of houses and people. To change the peaks, edit [`slide-kit/build-assets.py`](./slide-kit/build-assets.py) and place labels at the summit positions it prints.
4. **Write to [`writing.md`](../../knowledge-base/design-system/writing.md):**
   - "moment" every time, never "lead", "signal" or "alert"
   - Seekridge without an article
   - currency code before the number
   - benefit before feature
   - every AI claim explained.
5. **Every figure carries its source or "illustrative".** Every customer and person in a product mock-up is fictional and labelled as such.
6. **Write speaker notes for every slide** in `<aside class="notes">`: what to say, and what to ask the room.
7. **Add an appendix of 2–4 variants** of the hero and how-it-works slides (see the variants table in `layouts.md`), so the rep can swap one in for the room.
8. **Check before handing over:**
   - render every slide and look at it
   - make sure no text overflows or collides with the ridge
   - make sure there's one gold element per slide
   - export the PDF.

## What to avoid

- Don't add an "About us" slide unless the buyer needs the company's credibility established (an unfamiliar or skeptical buyer). Most decks don't, and it wastes an early slide.
- Don't pad the slide count to reach a "standard" deck length.
- Don't use bullet lists of features or data points. One idea per slide, shown, not listed.
- Don't put logos of real companies, real customer names or certifications Seekridge can't back up on a slide.
- Don't use the prohibited terms in the [`branding-guideline`](../../knowledge-base/branding-guideline/skill.md).

## Output format

Stage 1:

```
## Deck Outline — [deal context, one line]
Persona: [role] · Stage: [stage]

1. [Headline]   (L#)
   Purpose: ...
   Key point: ...

(repeat per slide)

Appendix: [variants to include]
```

Stage 2: `deck-[account-or-segment].html` built from the kit, its PDF export, and a one-line note of anything the rep must fill in (bracketed placeholders such as `[Bank]`).
