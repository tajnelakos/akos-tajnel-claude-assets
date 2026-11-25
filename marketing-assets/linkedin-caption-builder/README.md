# LinkedIn Caption Builder

## The problem

A LinkedIn post with no real finding behind it is an ad, built on an engagement-bait hook that could apply to any company in any category. When the standalone posts follow different rules from the carousel captions, the company page also reads like two brands.

## The approach

Takes a real, sourced finding — from [`win-loss-analysis`](../../knowledge-base/win-loss-analysis), [`competitor-monitoring`](../../sales-tools/competitor-monitoring), [`sales-call-analysis`](../../knowledge-base/sales-call-analysis), or a [`positioning.md`](../../knowledge-base/positioning.md) point of view — and writes it to the caption rules of the [LinkedIn carousel design system](../../knowledge-base/linkedin-carousels/captions.md): four short blocks (hook, benefit, proof, CTA with one link), 50–110 words, no hashtags, no rhetorical-question hooks. The same skill writes a carousel's caption or a standalone post.

It shares [`blog-post-builder`](../blog-post-builder)'s rule that competitive intelligence used freely internally is generalised before it's public. It also checks that a small-sample caveat survives, because short-form copy is exactly where one gets cut for a punchier hook.

## Files

- [`skill.md`](./skill.md) — the Claude Skill definition
- [`example.md`](./example.md) — a standalone post built from the win-loss deep dive's Kontora/Propensa win-rate finding, the same data [`outdated-checker`](../../knowledge-base/outdated-checker) used to update `competitive-landscape.md` and `positioning.md`

## Current limitations

LinkedIn only. Other channels would need their own rules, not a shorter version of these.
