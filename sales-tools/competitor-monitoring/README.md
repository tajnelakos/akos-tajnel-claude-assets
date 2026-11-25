# Competitor Monitoring

## The problem

Competitive intel usually shows up as noise: a pricing page change someone notices by accident, a G2 review a sales rep forwards, a changelog nobody reads end to end. Without a system, it either doesn't get synthesized at all, or it eats an afternoon every time someone asks "what's Bricklane doing lately?"

## The approach

A weekly-cadence skill that takes in raw, unstructured moments (pricing page snapshots, release notes, review site excerpts, sales call mentions) and produces one structured brief: what changed, why it matters for our positioning, and what — if anything — sales or product marketing should do about it. The goal is a brief a sales leader will actually read in three minutes, not a wall of bullet points.

Two constraints are built in on purpose:
- **No unverified claims.** If a moment is ambiguous (e.g. a pricing page number without context), the skill flags it as "needs confirmation" rather than asserting it.
- **"So what" is mandatory.** Every item must end with an implication, not just an observation — otherwise it's just news, not intelligence.

## Files — weekly brief

- [`weekly-brief-skill.md`](./weekly-brief-skill.md) — the Claude Skill definition
- [`weekly-brief-gpt.md`](./weekly-brief-gpt.md) — the same logic adapted as a ChatGPT custom GPT
- [`weekly-brief-example.md`](./weekly-brief-example.md) — a weekly brief run against [Seekridge](../../knowledge-base/knowledge-base.md)'s competitors

## Files — competitor analyses (bi-monthly, by region)

A slower, deeper cadence: a sourced, neutral record of what named competitors did in each core market (DACH, Benelux, Nordics), one edition per region every two months. Earlier editions stay one click away, and a year summary builds up as editions are added. What a move means for us is left to the [battlecards](../battlecard) and the weekly brief.

- [`competitor-analyses-skill.md`](./competitor-analyses-skill.md) — the skill that prepares one region's edition
- [`competitor-analyses.html`](./competitor-analyses.html) — the site: overview, a page per region, editions and a year summary ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/competitor-monitoring/competitor-analyses.html))

## Current limitations

Right now this takes plain pasted text. Pulling from the Slack channel where the team drops raw links/screenshots, and referencing the shared doc of past briefs for trend continuity week over week, is next.
