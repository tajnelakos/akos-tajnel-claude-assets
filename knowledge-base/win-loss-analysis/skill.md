---
name: win-loss-infographic
description: Analyzes a batch of closed-deal notes (close reasons, rep summaries, call excerpts) and produces a quantified win/loss breakdown rendered as a single-page infographic with concrete next actions. Use when the user has a batch of closed deals from one quarter/segment and wants patterns, not a deal-by-deal summary. Also supports a deep-dive mode against a structured CRM export — see below.
---

# Win/Loss Infographic

## Purpose

Turn a pile of closed-deal notes into one page an exec will read: what we actually win and lose on, quantified, with a mandatory "what to do about it" section.

## Instructions

1. **Read every deal note before classifying anything.** Don't classify off the CRM close-reason field alone — it's frequently a rep's shorthand, not the real reason. If the notes suggest a different or additional reason than the logged one, use what the notes actually support.
2. **Build two ranked lists**: top reasons deals were won, top reasons deals were lost. Each reason should be specific enough to act on ("no on-prem deployment option") not generic ("product gap").
3. **Cap each list at 4-5 reasons.** Group anything smaller into "Other" rather than listing every one-off reason — a list of 12 reasons is not a pattern, it's a data dump.
4. **Compute percentages against total won / total lost**, not total deals — win reasons should sum to ~100% of wins, loss reasons to ~100% of losses.
   - **Win rate** = wins ÷ total decisions × 100. 25 won out of 100 decided deals is a 25% win rate.
   - **Win/loss ratio** = wins ÷ losses. 25 won and 75 lost is 0.33.
   - Say how "no decision" deals are counted. If they sit in the losses, also show the win rate without them, because a stalled deal isn't a deal a competitor won.
5. **Note competitor concentration**: if losses cluster against one competitor, call that out explicitly — a 38% loss-to-price rate means something different if it's all against one aggressively-priced competitor vs. spread evenly.
6. **Compare to the prior period if data is available.** A reason that jumped in rank (e.g. "missing on-prem" moving from #4 to #2) is often more actionable than the current #1, because it moments a new or growing blocker.
7. **End with 2-3 concrete next actions**, each tied to a specific finding, addressed to a specific function (sales enablement, product, content). Never end on the chart alone — an unquantified "so what" is a required section, not optional color commentary.
8. **Render as a single infographic**: header stat row (win rate, deals analyzed, top competitor), two horizontal bar sections (won / lost reasons), and a takeaway panel. Use one hue for the "won" bars and a different single hue for "lost" bars — this is categorical-by-section, not a multi-series legend.

## What to avoid

- Don't editorialize about individual reps or deals — this is a pattern-level analysis, not a performance review.
- Don't present a reason as quantified if fewer than ~5 deals support it — note it as anecdotal instead, or omit it.
- Don't recommend pricing changes directly — flag pricing pressure as a finding for the pricing/product team to act on, not a decision this skill makes.

## Deep-dive mode — structured CRM export

The infographic above is built for a quarterly, exec-facing cadence. This mode is for a deeper, less frequent pass against an actual CRM export (deal size, sales cycle, lead source, assigned rep, and outcome per opportunity) — a richer input deserves a richer output, not the same one-page infographic with more rows squeezed in.

1. **Compute every statistic from the export, never estimate it.** If a number appears in the output (a win rate, an average deal size, a percentage), it must trace to a real aggregation over real rows — this mode's entire value is that its numbers are computed, not asserted.
2. **Structure the analysis around five core components**, each a real section, not a paragraph: **Buyer Demographics** (company size, industry/segment, current tech stack), **Decision Drivers** (why the buyer chose us or a competitor), **Competitor Data** (who we faced, their quoted price if known, their perceived strength), **Product Feedback** (missing features or bugs behind losses, standout features behind wins), and **Sales Process Insights** (rep performance, response time, demo quality).
3. **Pull in [`sales-call-analysis`](../sales-call-analysis) as a second data source where it exists.** A CRM export tells you *that* a deal was lost to price; a call transcript tells you *how* that conversation actually went. Cite the transcript directly rather than re-deriving what it already shows.
4. **Add buyer interviews as the third data source.** CRM fields capture what reps think happened; interviews tell you what buyers actually experienced. Build the interview pipeline below and run each interview with the [interview guide](./interview-guide.md). Join each summary to the export by Opportunity ID.
5. **Compare the rep's reason with the buyer's reason, deal by deal.** Mark each one Agrees, Partly or Differs, and count them. Where they differ, the buyer's reason wins in the analysis, and the gap itself is a finding (for example, losses logged as price that buyers put down to a missing reference). Below 15 interviews, say the sample size plainly and treat the pattern as a hint, not a rate.
6. **Look for findings that cut across components**, not just within one — e.g. whether the deals we lose tend to be larger than the ones we win, or whether response time (a process metric) predicts outcome better than demo quality (also a process metric) does. These cross-cutting findings are usually more useful than any single component's breakdown.
7. **Flag a 0%-win-rate segment as urgent, not as a footnote.** A competitor or condition with an extreme result on a small sample is still worth surfacing prominently — just say the sample size plainly rather than either hiding it or overstating its certainty.
8. **Never let a rep-performance finding read as a performance review of a named individual.** Report the aggregate pattern (e.g. response time correlating with win rate across the team) and, if a specific rep's documented work elsewhere contradicts a shallow read of their aggregate numbers, say so explicitly rather than leaving the contradiction for the reader to notice.
9. **Route every finding to one of four outputs**, and name the owner:
   - **Battlecards** (sales enablement): buyer language about competitor strengths and weaknesses.
   - **Product roadmap** (product): feature gaps from lost deals, with the ACV lost against each gap.
   - **Sales training** (sales enablement): the objections that tripped reps up, as coaching scenarios.
   - **Positioning** (product marketing): how buyers compare us with competitors, in their words, so messaging rests on evidence.
10. **Render as a full analysis page**, not a single infographic — this mode has too much real structure (five components, cross-cutting findings, source citations) to compress into one exec-glance visual. See [`win-loss-detailed-analysis.html`](./win-loss-detailed-analysis.html).

## Build the interview pipeline

Win/loss is an interview program, not a report on CRM fields. The most common mistake is to analyse the dropdowns and never talk to a buyer.

**Get the CRO or Head of Sales to own the discipline, before anything else.** Product marketing can run the interviews, but it can't make reps log real close reasons, pass on the decision-maker's contact, or make the intro. When sales leadership treats win/loss as optional, reps drop it, the pipeline dries up and the CRM fields stay shorthand. Ask the sales leader to make it part of how a deal is closed: close-reason fields required before a deal can be marked won or lost, the buyer contact handed over within a week, and win/loss findings on the agenda of their regular pipeline or forecast meeting. If that sponsor isn't there, say so at the top of the analysis as a limitation.

1. **Sample wins and losses.** Losses alone give a skewed picture. Wins show what's working, what buyers respond to, and which differentiators actually land.
2. **Size the sample.** At least 15–20 completed interviews a quarter for patterns you can trust, with roughly 10 wins and 10 losses. Cutting by competitor, deal size or persona needs 30–40 a quarter.
3. **Time it.** Interview within 2–4 weeks of the close, while it's fresh. After about 30 days buyers start rationalising the decision; after 60 they struggle to remember who else they looked at.
4. **Talk to the decision-maker**, not the champion or an end user. For a loss, the person who chose the competitor. For a win, the person who signed off the purchase.
5. **Ask in the right way.** Frame the request as "help us improve", never "tell us what went wrong". Offer something back: anonymised industry benchmarks, a short summary of market trends, or a gift card where the buyer's policy allows it.
6. **Fill the top of the pipeline.** Expect 10–30% of buyers to say yes, so invite 50–60 closed deals a quarter to complete 15–20 interviews. Track invited, agreed and completed each quarter so the response rate is visible.
7. **Keep the interviewer neutral.** Product marketing runs the interview, not the rep who worked the deal, and the rep gets the summary afterwards.
