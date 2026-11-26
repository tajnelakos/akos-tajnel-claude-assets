# Sales Call Analysis

## The problem

Discovery and demo calls generate the most honest competitive and product feedback a company gets — and most of it evaporates the moment the call ends, because nobody has time to relisten and extract it systematically. Call recording tools transcribe; they don't tell you which objection is becoming a pattern.

## The approach

A skill that takes a single call transcript and extracts four things, every time, in the same structure — so that running it across many calls produces comparable output instead of freeform notes:

1. **Objections raised**, verbatim where possible, tagged by type (price, product gap, timing, competitor, internal politics).
2. **Competitor mentions**, with the context they came up in (prospect brought it up unprompted vs. rep asked).
3. **Buying moments**, distinguished from politeness — "that's helpful" is not a buying moment; a question about implementation timeline is.
4. **One coachable moment** for the rep — something they could have handled better, framed constructively, not a performance score.

## Files — single-call analysis

- [`skill.md`](./skill.md) — the Claude Skill definition
- [`gpt.md`](./gpt.md) — ChatGPT custom GPT version
- [`example.md`](./example.md) — run against a discovery call transcript

## Files — aggregate rollup across many calls

Fifteen call transcripts (July–August 2026, a deliberate mix of retail-bank, savings-bank and credit-union deals, competitors named and unnamed, strong moments and stalled ones) with a designed HTML rollup that surfaces the patterns a single-call analysis can't: which objections recur, which competitors actually come up, and — the part that matters most — specific new findings that aren't yet reflected anywhere else in this repo's knowledge base.

- [`call-01-nordkredit.md`](./call-01-nordkredit.md) through [`call-15-copperfield-cooperative-bank.md`](./call-15-copperfield-cooperative-bank.md) — the 15 transcripts
- [`call-analysis-summary.html`](./call-analysis-summary.html) — the aggregate rollup ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/sales-call-analysis/call-analysis-summary.html))

Several of the fifteen deliberately connect to accounts used elsewhere in this repo — Nordkredit (which ends as the [designed case study](../../marketing-assets/case-study-builder/case-study-nordkredit.html)), Meridian Savings and Court Street Bank (both in the [win-loss data](../win-loss-analysis/win-loss-crm-export.csv)), Thornfield Mutual (the first Outflow Watch deal, see the [go-to-market plan](../../marketing-assets/product-launch-process/go-to-market-outflow-watch.md)) — so the calls read as one continuous account history rather than fifteen disconnected demos.

All fifteen also appear as closed opportunities in [`win-loss-analysis`](../win-loss-analysis)'s [CRM export](../win-loss-analysis/win-loss-crm-export.csv) and [deep-dive analysis](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/win-loss-analysis/win-loss-detailed-analysis.html) — the qualitative "how the call went" here and the quantitative "what closed" there describe the same deals, not two unrelated data sets.

## Current limitations

The single-call skill takes one pasted transcript and returns one analysis; feeding transcripts directly from a call recording tool's API is next. The aggregate rollup above is currently a one-time manual pass across a fixed batch of transcripts — running it incrementally as new calls come in, rather than regenerating the whole rollup each time, is the natural next step.
