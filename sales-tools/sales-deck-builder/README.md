# Sales Deck Builder

## The problem

Reps customize decks for big deals by copy-pasting slides from old decks and hoping the story still holds together. The result is usually a Frankenstein deck: right individual slides, wrong order, no throughline for who's actually in the room, and three visual styles fighting each other.

## The approach

A skill that works in two stages:

1. **Outline.** From a few lines of deal context (who's buying, what they care about, the deal stage), it writes a slide-by-slide outline: headline, purpose and key point per slide. The outline is quick to sanity-check, so the story gets fixed before anyone designs anything.
2. **Build.** Once the outline is agreed, it builds the slides from a **Seekridge slide kit**: 15 layouts on a 1920 × 1080 canvas in the brand's design system, with the dot-map ridge as the one illustration. Every slide gets speaker notes, and the deck gets an appendix of alternative slides for different rooms.

The core judgment call it makes every time: **order and emphasis change with the buyer persona**, even when the product facts don't. A model-risk buyer and a retail-banking buyer don't get the same structure just because they're buying the same product.

The kit's story shape and slide patterns come from two decks Akos built in a previous role: a solution deck and a segment deck. They were rebuilt here for Seekridge's own design, words, bank-transaction story and fictional customers.

## Files

- [`skill.md`](./skill.md): the Claude Skill definition
- [`gpt.md`](./gpt.md): ChatGPT custom GPT version (outline stage only)
- [`slide-kit/`](./slide-kit): the slide kit
  - [`layouts.md`](./slide-kit/layouts.md): the 15 layouts, the appendix variants and the rules every slide keeps
  - [`slides.css`](./slide-kit/slides.css): the kit's styles, built on the design-system tokens and fonts
  - [`ridge.py`](./slide-kit/ridge.py) and [`build-assets.py`](./slide-kit/build-assets.py): draw the ridge illustrations
- [`deck-retail-banks.html`](./deck-retail-banks.html) ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/sales-deck-builder/deck-retail-banks.html)) and [`deck-retail-banks.pdf`](./deck-retail-banks.pdf): the reference deck, a first meeting with a bank's Head of Retail Banking, 14 slides plus a 5-slide appendix
- [`example-retail-banks.md`](./example-retail-banks.md): the input and outline behind that deck
- [`sample-deck-outline.md`](./sample-deck-outline.md): an outline-only example for a Head of Model Risk, showing how the order changes by persona

## Current limitations

- The kit outputs HTML and PDF, not PowerPoint, so a rep who edits slides in PowerPoint has to rebuild them there.
- The outline is written from scratch every time. Pulling approved slides from a shared deck library is next.
