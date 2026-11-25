---
name: battlecard-generator
description: Produces a rep-facing HTML battlecard for one named competitor (at a glance, their pitch and the quick dismiss, strengths and weaknesses with what to say, where we're weaker, landmines, buyer quotes, don't-say), sourced from competitive-landscape.md, the win/loss CRM export, the competitor analyses site and sales-call transcripts. Can also update just the changed sections of competitive-landscape.md's own deeper reference entry when new raw research comes in. Use for the field-ready, printable/openable card a rep skims before or during a call — not the analyst-maintained reference doc itself.
---

# Battlecard Generator

## Purpose

Turn the deep, analyst-maintained competitor data in `competitive-landscape.md` into a battlecard a rep can actually use live: scannable in under a minute, structured the way a real sales-enablement battlecard is structured, not a research summary reformatted with headers.

## Two outputs, two audiences

1. **The rep-facing battlecard** (primary output, HTML) — for someone about to get on a call. Dense, visual, skimmable, no analysis-speak.
2. **An update to `competitive-landscape.md`'s own entry** (Markdown, targeted) — for whoever maintains the deeper reference doc. Only when new raw research comes in; output only the changed sections, not a full regeneration (see [`example.md`](./example.md) for this mode).

## Instructions — rep-facing battlecard

Shorter beats complete. A rep should get the whole card in a minute; every line must be something they would say, ask or avoid on a call.

1. **Header.** Competitor name, a one-sentence lede on how they compete right now, and three fact pills: threat level, last updated, and the head-to-head record. The pill that matters most for this competitor gets the highlight.
2. **At a glance.** Eight facts in a grid. Lead with the two a rep needs most: the head-to-head record and their price against ours, both computed from the win/loss CRM export (`Competitor Faced`, `Outcome`, `Deal Size`, `Competitor Quoted Price`). Then founded, size or funding, who they target, how they sell, which buyer they reach, and reviews or recent moves.
3. **What changed.** One line on the latest move from the competitor analyses site that changes what a rep can say. If a claim on an older card has become false, say so here.
4. **Their pitch, and the quick dismiss.** Their actual public message, quoted, beside a two-sentence reality check that is sourced, not invented. Then one line on how we differ, written as a contrast a rep can repeat.
5. **Where they're strong, and what to say. Where they're weak, and how to use it.** Three of each at most. Every point is paired with a line the rep can act on. Concede real strengths; don't argue with them.
6. **Where we're weaker, and how to handle it.** The honest gaps (deployment, size, price), each with how to raise or answer it. A card without this section isn't trusted.
7. **Landmines to lay.** Three questions a rep can ask before the competitor comes up, each with a short note on why it works. A real question invites the buyer to say something; it never leads the witness.
8. **What buyers told us.** Up to three short quotes from the sales-call transcripts, each linked to its file. Only verbatim quotes, trimmed, never paraphrased into quotation marks.
9. **Don't say.** Two or three lines a rep would be tempted to use, and why each would backfire. Update this list when a competitor ships something: an old "they don't have X" becomes a don't-say.
10. **Match depth to threat.** A low-threat competitor gets fewer pairs and gaps, not padding.

## What to avoid

- Don't invent a proof point, a stat, or a quote that isn't backed by `competitive-landscape.md` or the raw research provided.
- Don't write a discovery question that's really just an assertion in question form ("Isn't it true that X is slow?") — a real discovery question invites the prospect to say something, it doesn't lead the witness.
- Don't let the do-not-say list quietly disappear when a claim becomes true (e.g. a competitor ships a feature that used to be fair game to question) — check `competitive-landscape.md`'s "Last verified" date and `outdated-checker` before reusing an old card unchanged.

## Output format — rep-facing battlecard

```
[Header] lede · threat · updated · head-to-head
[At a glance] 8 facts; head-to-head and price first
[What changed] one line, from the latest competitor analyses edition
[Pitch and quick dismiss] they say (quoted) | reality (sourced) + one-line contrast
[Strong / weak] up to 3 each, every point paired with what to say or do
[Where we're weaker] honest gaps, each with how to handle it
[Landmines] 3 spoken questions, each with why it works
[What buyers told us] up to 3 verbatim quotes, linked to transcripts
[Don't say] 2–3 tempting lines, and why not
```

See [`ledgerline.html`](./ledgerline.html), [`conturo.html`](./conturo.html), [`nexascore.html`](./nexascore.html), and [`pocketlens.html`](./pocketlens.html) for this format applied to each tracked competitor.
