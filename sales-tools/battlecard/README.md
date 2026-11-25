# Battlecard

## The problem

[`competitive-landscape.md`](../../knowledge-base/competitive-landscape.md) is the deep, analyst-maintained reference — the right format for someone building or auditing the competitive picture. It's the wrong format for a rep about to get on a call, who needs something they can skim in under a minute, not read as a document. Someone has to translate the reference doc into a field-ready card, and that translation is real work: deciding which 3-5 differentiators actually matter, phrasing objection handlers the way a person would say them out loud, being explicit about what not to claim.

This is distinct from [`competitor-monitoring`](../competitor-monitoring), which tracks what *changed this week*, and from `competitive-landscape.md` itself, which is the deep reference. This folder is the rep-facing output built from that reference.

## The approach

A skill that takes the data already in `competitive-landscape.md`, the win/loss CRM export, the latest [competitor analyses](../competitor-monitoring/competitor-analyses.html) edition and the sales-call transcripts and produces two things: a full rep-facing HTML battlecard per competitor, and, when new research warrants it, a targeted update to `competitive-landscape.md`'s own entry. Every battlecard follows the same structure so a rep who's used one can navigate any of them cold:

At a glance (head-to-head record and price first) → what changed → their pitch and the quick dismiss → where they're strong and what to say, where they're weak and how to use it → where we're weaker and how to handle it → landmines to lay → what buyers told us, quoted from real calls → don't say. Shorter than a classic battlecard on purpose: everything on it is something a rep would say, ask or avoid.

Card depth matches actual threat level — the High-threat Ledgerline card is not the same length as the Low-threat Pocketlens card, on purpose.

## Files

- [`skill.md`](./skill.md) — the Claude Skill definition
- [`example.md`](./example.md) — the targeted-update mode: a battlecard section updated from new raw notes, output as a diff against the existing entry rather than a full regeneration
- [`ledgerline.html`](./ledgerline.html) — 🔴 High threat; we won 6 of 14 ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/battlecard/ledgerline.html))
- [`conturo.html`](./conturo.html) — 🟠 Medium-high threat; we won 3 of 11 ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/battlecard/conturo.html))
- [`nexascore.html`](./nexascore.html) — 🟠 Medium-high threat ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/battlecard/nexascore.html)) — we won 1 of 8; refreshed for NexaScore's July 2026 moment-explanation launch (see the Jul–Aug 2026 edition of [`competitor-analyses.html`](../competitor-monitoring/competitor-analyses.html))
- [`pocketlens.html`](./pocketlens.html) — ⚪ Low threat ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/battlecard/pocketlens.html)) — brokerage only, deliberately short

## Current limitations

Right now this runs as a manual pass per competitor. Automatically cross-referencing new input against the existing card and flagging contradictions (e.g. new win/loss data suggesting a differentiator no longer holds) is next — see [`outdated-checker`](../../knowledge-base/outdated-checker), which already flags exactly this kind of drift in `competitive-landscape.md`.
