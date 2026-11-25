---
name: competitor-analyses-region
description: Prepares one region's bi-monthly edition of the Seekridge competitor analyses site (DACH, Benelux, Nordics): confirms scope, researches the named competitors for a fixed two-month window, verifies every item against a source, and writes the edition into that region's data block. Use for the deeper, sourced record of what competitors did — distinct from the weekly brief, which is faster and carries a "so what".
---

# Competitor Analyses — one region, one edition

## Purpose

Keep a sourced, comparable-over-time record of what named competitors are publicly doing in each core market. The output is one edition for one region, added to [`competitor-analyses.html`](./competitor-analyses.html), where every earlier edition stays one click away and a year summary builds up automatically.

## Why it's neutral

The site is a record, not a verdict. It never says what a move means for Seekridge, never compares, never rates threat. That keeps it trusted as an unbiased source across sales, product and leadership. What a development means for us is worked out downstream, in the [battlecards](../battlecard) and the [weekly brief](./weekly-brief-skill.md).

## Steps

1. **Confirm scope.** Region (DACH, Benelux or Nordics), the two-month window (e.g. 1 Sep – 31 Oct 2026), and the competitor list for that region. Each region tracks the competitors that matter there: the battlecard competitors that sell in it, plus local players (e.g. Sentiro in Switzerland, Norrvakt in Norway).
2. **Research the window only.** Company press releases, pricing pages, official blogs, commercial registers, LinkedIn announcements, industry news. Do not reach back before the window to fill a quiet company.
3. **Verify every item.** An item without a source is not an item. If two sources support one claim, cite both. State a competitor's own figures as their claims.
4. **Write each company in the same order:**
   - **Snapshot** — one sentence: who they are, where, how funded, who they sell to.
   - **Recent developments** — funding, launches, hires, expansion, pricing changes.
   - **Partnerships and ecosystem moves** — integrations, data partnerships, distribution.
   - **Messaging and positioning** — only if it visibly changed since the start of the half-year.
   - A company with nothing verifiable this period goes in the "analysed, no news" list. Say so plainly; don't pad.
5. **Write the summary.** One line per company with news, most significant first. This also feeds the region card on the overview page and the year summary.
6. **Write the edition into the region's data block only.** Each region is a JSON block between its `REGION <id> START / END` markers. Add the new period at the top of `periods`, set `published` and `nextUpdate`, and leave the other regions and the page code untouched.

## Rules

- No comparative or impact language ("better than", "a threat to", "an opportunity for us"). Don't mention Seekridge inside an edition.
- Company-level news only. Market price indices and thought-leadership posts are out unless they announce a real company change.
- Source labels say what kind of source it is ("Company press release", "Pricing page"), never a bare URL.
- Dates are exact where the source gives them.

## Output

One updated region block in [`competitor-analyses.html`](./competitor-analyses.html). The overview counts, region cards, edition switcher and year summary all update from the data, so nothing else needs editing.
