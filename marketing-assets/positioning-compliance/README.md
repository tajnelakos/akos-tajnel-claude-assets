# Positioning Compliance Checker

## The problem

[`branding-guideline`](../../knowledge-base/branding-guideline) rewrites a draft to fix voice issues. That's the right tool when one person owns the draft and wants it improved. It's the wrong tool for a pre-publish gate, where what's needed is a fast yes/no on whether a piece is safe to ship — flagging problems for the actual owner to fix, not silently rewriting someone else's copy before it goes out.

## The approach

A skill that checks a draft against [`branding-guideline`](../../knowledge-base/branding-guideline/skill.md)'s voice rules (prohibited terms, anti-patterns), [`positioning.md`](../../knowledge-base/positioning.md) (claims that overstate or contradict our actual positioning), and [`competitive-landscape.md`](../../knowledge-base/competitive-landscape.md) (named-competitor claims that have gone stale since they were written) — and returns a pass/fail with specific citations, never a rewrite. The distinction from the brand-voice skill is deliberate: a compliance check that also rewrites invites skipping the review, since the "fixed" version just gets shipped without anyone looking at why it was flagged.

## Files

- [`skill.md`](./skill.md) — the Claude Skill definition
- [`example.md`](./example.md) — a worked check: a claim that was accurate when written and is false now, because a named competitor (ValuAI) shipped the feature the claim said they lacked

## Current limitations

Right now this is a standalone check run by hand. Wiring it in as a required step before publishing (and in the [`battlecard`](../../sales-tools/battlecard) refresh cycle, where stale competitor claims do the most damage) is next.
