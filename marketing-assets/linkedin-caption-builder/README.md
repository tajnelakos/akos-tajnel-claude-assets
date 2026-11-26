# LinkedIn Caption Builder

## The problem

A social post built with no real finding behind it is an ad wearing a hashtag — engagement-bait hooks that could apply to any company in any category. The fix is the same one this repo applies everywhere else: require a real, cited data point before drafting, not a generic prompt.

## The approach

Takes a real, sourced finding — from [`win-loss-analysis`](../../knowledge-base/win-loss-analysis), [`competitor-monitoring`](../../sales-tools/competitor-monitoring), [`sales-call-analysis`](../../knowledge-base/sales-call-analysis), or a [`positioning.md`](../../knowledge-base/positioning.md) point of view — and compresses it to a LinkedIn caption, following the caption rules in the carousel system's [`captions.md`](../../knowledge-base/linkedin-carousels/captions.md). Shares [`blog-post-builder`](../blog-post-builder)'s rule that competitive intelligence named freely internally has to be generalized before it's public, and adds a caution specific to this format: short-form copy is exactly where a small-sample caveat tends to get cut for a punchier hook, so the skill checks explicitly that it survives.

## Files

- [`skill.md`](./skill.md) — the Claude Skill definition
- [`example.md`](./example.md) — a post built from the win-loss deep dive's Conturo/NexaScore win-rate finding, the same data [`outdated-checker`](../../knowledge-base/outdated-checker) used to update `competitive-landscape.md` and `positioning.md`

## Current limitations

Only LinkedIn is covered, on purpose: it is where this ICP's buyers spend time per `personas.md`. Another platform would need its own worked example with different mechanics, not just a shorter version of this one.
