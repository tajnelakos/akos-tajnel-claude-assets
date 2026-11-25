# Writing for Seekridge

The full wording rules for every Seekridge channel. The voice core (tone, style standards, anti-patterns, prohibited terms) matches [`../branding-guideline/skill.md`](../branding-guideline/skill.md), which the rewrite skill applies; this file adds names and terms, case, numbers, market typography, inclusive language and product copy.

## Tone

Confident and specific, never hyped. The audience is technically skeptical and regulator-adjacent. The tone that wins with them belongs to someone with nothing to overstate, because the real claim is already strong enough.

## Style standards

- **Lead with the claim, not the setup.** No scene-setting openers ("In today's fast-changing landscape…").
- **Numbers over adjectives.** Use the real figure or comparison. With no figure in the source, make a defensible qualitative claim; never invent a number.
- **Second person, active voice.** Contractions are fine: formality comes from precision, not stiffness.
- **One idea per paragraph.** This audience skims first and reads second.
- **State limitations plainly.** A claim that admits what the product doesn't do reads as more credible to this audience, not less.

## The golden rules

| Rule | Do | Don't |
|---|---|---|
| Name the persona's problem | "Which of your customers are moving money out this quarter?" | "Discover our new platform" |
| Mechanism, not adjective | "Every moment shows the 6 data points behind it and how much each counted" | "Robust, transparent insights" |
| Explain any AI claim | "The model combines the new transfer out, the income change and other banks' savings rates, and shows each weight" | "Powered by advanced AI" |
| Benefit, then feature | "Know which customers to call this month, and why" | "Moment scoring with Evidence Trail" |
| One term per idea | "moments" throughout | "moments", then "leads", then "alerts" |
| Precise CTAs | "Run a backtest on your own customer base" | "Learn more" |
| Admit the limit | "Moment quality depends on your CRM data, so we backtest it before go-live" | Implying moments work the same on any data |

## Anti-patterns

- **"It's not X, it's Y."** Banned. State the point directly.
- **Unexplained AI claims.** Never assert an AI capability without saying what it does or checks.
- **Rhetorical questions as openers** ("Tired of leads nobody can explain?"). Open on the point. A direct question that names a real situation is fine on social covers (see [`social-and-carousels.md`](./social-and-carousels.md)).
- **Manufactured urgency** ("Don't get left behind", "the future is now").
- **Predicting sensitive facts.** Moments describe what has already happened, never what the data might reveal: "child benefit started arriving in October", not "we can tell when a customer is expecting". The same goes for health, relationships and money trouble.

## Prohibited terms

`seamless` · `revolutionary` · `cutting-edge` · `game-changing` · `next-generation` · `unlock` (as in "unlock your potential") · `robust` (with nothing specific attached) · `powered by advanced AI` / `powered by cutting-edge algorithms` · `disrupt` / `disruptive`

| Instead of | Use |
|---|---|
| "seamless integration" | the integration point: "pushes moments into your existing CRM via API" |
| "powered by advanced AI" | what the system does or checks |
| "significantly faster" | the figure, or "faster than manual review" |
| "revolutionary approach" | the specific difference, without the adjective |

## Names and terms

- **Seekridge**: one word, capital P only, no article ("Seekridge backtests every moment model", not "The Seekridge…").
- **Feature names** are literal and capitalised as names: Evidence Trail, Coverage Map. In running text they take no article in English ("Evidence Trail shows…"); German and Dutch use articles.
- **Tiers:** Base, Ridge, Summit. Only for pricing.
- **Terminology:** moment (not lead, insight or alert) · evidence trail (the data points behind a moment; not explainability report) · audit log (the record of what was done with a moment; not activity feed) · customer base (not database or leads) · transaction data, customer data, market data (not big data or data lake) · main bank and secondary bank (not primacy or share of wallet, in customer-facing copy) · bank, savings bank, cooperative bank or credit union (not client, in product copy) · CRM · AI agent (the bank's own assistant; not chatbot).
- **Competitors** are named only in battlecards and internal material, never in public content.

## Case

Sentence case for every title, heading, button, label, cover and caption: "Evidence for every moment", "Run a backtest". Capitals only for the first word, Seekridge, feature names, tiers and proper nouns. The mono eyebrow label is the one all-caps element, and it's set in CSS (`text-transform`), not typed in capitals.

## Numbers, currency and dates

- **Currency code before the number**, never a symbol, because the markets use EUR, CHF, SEK, NOK and DKK side by side: EUR 412,500 · CHF 1.2m · SEK 3.4m. Large amounts: m and bn ("EUR 5 bn" in prose; "EUR 5bn" in tight UI). *Older repo examples use €; update them when they're next edited.*
- **Every figure says what it measures** and, if external, where it came from: "68% of flagged customers moved money out within 6 months (backtest on the client's 2025 data)".
- **Illustrative figures are labelled** as illustrative wherever they appear outside internal docs.
- **Dates:** 24 November 2026 in prose; 2026-11-24 in tables, exports and the audit log (mono).
- **Percentages:** 6.1%, no space in English.
- **Ranges:** en dash, no spaces: 2–4px, 2024–2026.

## Market typography

| | EN (UK) | DE / AT | CH-DE | NL / BE-NL | Nordics (SV, DA, NO) |
|---|---|---|---|---|---|
| Quotation marks | "…" | „…“ | «…» | "…" | ”…” (SV), »…« (DA), «…» (NO) |
| 10000 and above | 10,000 | 10.000 | 10’000 | 10.000 | 10 000 |
| Decimals | 6.1 | 6,1 | 6.1 | 6,1 | 6,1 |
| Currency | EUR 412,500 | EUR 412.500 | CHF 412’500 | EUR 412.500 | SEK 4 125 000 |
| Address form | you | Sie | Sie | u (formal) or je (digital banks) | du |

- English is **UK English** (Oxford spelling: "organisation", "analyse").
- Localise rather than translate: German and Dutch run 20–30% longer. On fixed canvases, step down a type size rather than tightening margins.

## Inclusive language

- English: *they / their* for generic people ("If an advisor needs the evidence, they can open it from the moment").
- German: neutral forms first (*Kundschaft*, *Mitarbeitende*), otherwise *Kund:innen*.
- Never gender a generic banker, advisor, member or customer.

## Product copy

- **Buttons:** verb + object, sentence case: "Push to CRM", "View evidence", "Export audit log". Never "Submit" or "Click here".
- **Errors:** what happened, then what to do: "We couldn't match 214 customer records to a checking account. Check the account IDs in your CRM export." Never blame the user; never only a colour.
- **Empty states:** say what will appear and how to get it: "No moments yet. Connect your CRM to analyse your customer base."
- **Confidence and limits are shown, not hidden:** "Limited evidence: only six weeks of transactions on this account."

## Rewriting a draft

1. Read the whole draft before editing anything.
2. Rewrite to these rules, keeping the author's structure where it doesn't conflict.
3. Note each substantive change and the rule behind it; skip trivial word swaps.
4. Flag any claim that can't be verified from context. The writer confirms it, not the rewrite.
5. Return the rewrite, then a short "Changes and why" list.
