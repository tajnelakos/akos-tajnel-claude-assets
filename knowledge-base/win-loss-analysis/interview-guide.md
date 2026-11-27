# Buyer win/loss interview guide

CRM fields capture what reps think happened. Win/loss interviews tell you what buyers actually experienced. This guide is the third data source in the win/loss analysis, next to the [CRM export](./win-loss-crm-export.csv) and the [sales call analysis](../sales-call-analysis).

## Who runs it

Product marketing runs the interview, not the rep who worked the deal. Buyers are more open with someone who wasn't in the room. They won't defend the rep, and they won't soften the reason to be polite. The rep gets the summary afterwards.

## Who owns it

Product marketing runs the interviews, but the CRO or Head of Sales has to own the discipline. A request from product marketing or ops is easy for reps to ignore; a rule from their sales leader isn't. When leadership treats win/loss as optional, reps deprioritise it, and the pipeline dries up within a quarter.

What the sales leader enforces:

- Close-reason fields filled in properly before a deal can be marked won or lost.
- The decision-maker's contact handed to product marketing within a week of the close, with a warm intro from the rep.
- Win/loss findings reviewed in the regular pipeline or forecast meeting, so reps see the results of their effort.

## The pipeline

Win/loss is an interview program, not a report on CRM fields. You have to talk to buyers.

- **Wins and losses, both.** Losses alone skew the picture. Wins show what's working and which differentiators actually land with buyers.
- **Sample size.** At least 15–20 completed interviews a quarter, about 10 wins and 10 losses. For cuts by competitor, deal size or persona, 30–40 a quarter.
- **Fill the funnel.** Expect 10–30% of buyers to agree, so invite 50–60 closed deals a quarter. Track invited → agreed → completed.
- **Include "no decision" deals** when the buyer is willing. They are often the most honest conversations.

## Who to interview

The decision-maker, not the champion or an end user. For a loss, the person who chose the competitor. For a win, the person who signed off the purchase.

## When and how

- Within 2–4 weeks of the close. After about 30 days buyers start rationalising the decision; after 60 they can barely remember who they evaluated.
- 20 to 30 minutes, video or phone.
- Frame the invitation as "help us improve", not "tell us what went wrong". Offer something back: anonymised industry benchmarks, a short summary of market trends, or a gift card where their policy allows it.
- Ask for consent to record and take notes. Say the notes are for internal use and won't be quoted with their name outside the company. Under GDPR, record only with clear consent, keep the recording for a set time, and store the summary rather than the full transcript where you can.
- Send one short thank-you note after. No sales follow-up from the same call.

## The questions

Open with the decision, then go back to the start. Keep the order loose; follow what they bring up.

1. In a sentence, why did you choose the way you did?
2. What made you start looking in the first place? What was going on at the bank?
3. Who else was involved in the decision, and what did each of them care about most?
4. Which other options did you look at, and how did you narrow the list?
5. What did the other vendor do better than us? Where were we stronger?
6. Was there a moment when the decision was made, before the paperwork? What happened then?
7. How did price and contract terms weigh in, compared with everything else?
8. What was missing or worried you about our product? Was any of it a deal-breaker?
9. How was working with our team: speed of replies, the demo, the follow-up?
10. If you could change one thing about how we sold to you, what would it be?

For wins, add: *What almost made you go another way?*

## What to write up

One summary per interview, using the same fields every time so they can be counted:

| Field | What goes in it |
|---|---|
| Deal | Opportunity ID from the CRM, so it joins to the export |
| Rep-logged reason | The Decision Driver field as the rep logged it |
| Buyer's reason | The main reason in the buyer's words, one line |
| Match | Agrees / Partly / Differs |
| Competitor view | What the buyer said about the other vendor |
| Quote | One short line in their words (anonymised) |
| Goes to | Battlecards / Roadmap / Sales training / Positioning |

See [`buyer-interviews.md`](./buyer-interviews.md) for eight filled examples.

## Where the findings go

A win/loss program earns its keep through four outputs:

1. **Battlecards.** Buyer language about competitor strengths and weaknesses goes into the [battlecards](../../sales-tools/battlecard) reps use on calls.
2. **Product roadmap.** Feature gaps cited in lost deals reach product with the ACV lost against each one.
3. **Sales training.** The objections that tripped reps up become coaching scenarios.
4. **Positioning.** How buyers compare us with competitors adjusts messaging based on evidence, not guesswork.
