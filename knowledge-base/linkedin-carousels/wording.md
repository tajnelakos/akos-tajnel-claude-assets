# Writing for carousels

Seekridge's wording rules ([`../design-system/writing.md`](../design-system/writing.md) and the voice in [`../branding-guideline/skill.md`](../branding-guideline/skill.md)) applied to a slide that is read in two seconds on a phone. Where a carousel needs something those files don't cover, these rules win.

## The golden rules on a slide

| Rule | On a carousel | Do | Don't |
|---|---|---|---|
| Name one reader's situation | One persona per carousel; the cover names their situation or a fact | "Which customers will refinance elsewhere?" | "Discover the Seekridge platform" |
| Mechanism, not adjective | Each slide names what the product does, checks or shows | "Shows the rate reset, the salary moving and the market behind each moment" | "Transparent, AI-powered insights" |
| Explain any AI claim | Say what the model combines and that each weight is shown, or leave AI out | "Combines the rate end date, the salary moving elsewhere and local rates, and shows each weight" | "Powered by advanced AI" |
| Benefit, then feature | The heading says what the reader can now do; the feature name goes in the eyebrow or the caption | Heading: "The reason, written from the evidence" · eyebrow: "Evidence Trail" | Heading: "Evidence Trail now has reason lines" |
| One idea per slide | One claim, one figure or one screenshot | "One lender, one year, one product." | A claim, a figure and a screenshot on one slide |
| Lead with the claim | The first words on a slide carry the point | "Credit scoring is high-risk AI." | "In today's regulatory landscape…" |
| Numbers carry their source | Every figure has a mono source line under it, or "illustrative" | "68%" + "Backtest on a lender's 2025 book · illustrative" | "68%" alone, or "up to 70%" |
| Admit the limit | Proof carousels end on what the figure doesn't show | "The only figure that should convince you is a backtest on your own book." | Implying a result transfers to any bank |
| One term per idea | Same word on every slide and in the caption | "moment" throughout | "moment", then "lead", then "alert" |
| Precise CTAs | The close says what to do and what they get | "Run the same backtest on your book." | "Learn more" |
| Check it twice | Review against these rules, then a colleague | | Publishing unchecked |

## Banned on slides

- **The "it's not X, it's Y" construction.** State the point directly. A plain contrast that adds information ("a list, not a reason") is fine once per carousel; a slogan built on one isn't.
- **Rhetorical-question openers** ("Tired of leads nobody can explain?"). A *direct* question that names a real situation is the one allowed question, and only on a cover or an event invite ("Which customers will refinance elsewhere?").
- **Manufactured urgency**: "don't miss", "act now", "the future is here", countdowns.
- **Prohibited terms**: `seamless` · `revolutionary` · `cutting-edge` · `game-changing` · `next-generation` · `unlock` · `robust` (with nothing specific attached) · `powered by advanced AI` · `disrupt` / `disruptive`.
- Emoji, hashtags, links, @-mentions and exclamation marks.
- Real customer names, addresses or data. Customers appear by ID ("Customer 40-1187").
- Competitor names. They belong in battlecards, never in public content.

## Lengths

| Style | About | Lines |
|---|---|---|
| `title-cover` | 8 words | 3, at most 4 |
| `title-question` | 12 words | 4 |
| `title-statement` | 20 words | 5 |
| `title-long` | 30 words | 6 |
| `heading` | 8 words | 2 |
| `title-step` | 7 words | 3 |
| `body-lead` | 30 words | 3 |
| `card-body` / `body` | 40 words | 5 |
| Checklist row | 10 words | 2 |
| Eyebrow | 3 words | 1 |

When a line doesn't fit, cut words before you change the style. Step down a style (statement → long) only for German, Dutch or a quotation.

## Names

- **Seekridge**: one word, capital P only, never with an article ("Seekridge backtests every moment model").
- **Feature names** are literal and capitalised as names: Evidence Trail, Coverage Map. No article in English; German and Dutch use one ("der Evidence Trail", "de Coverage Map").
- **Tiers** (Base, Ridge, Summit) appear only on pricing posts.
- **The three data layers** are always named in this order and these words: transaction data, customer data, market data. The icons follow the same order: transaction, customer, market.
- **Terms**: moment (not lead, insight or alert) · evidence trail (not explainability report) · audit log (not activity feed) · customer base (not database) · name the transaction data point ("salary now split with another bank", not "spending behaviour") · bank or lender (not client).

## Case

Sentence case, always, with no exceptions for covers, eyebrows or buttons: "New in Evidence Trail", "Three data layers", "Book a slot". Feature names keep their capitals inside a sentence-case line. The eyebrow is typed in sentence case and set uppercase in CSS, so a screen reader and a copy-paste get normal text.

## Numbers, currency and dates

- **Currency code before the number**, never a symbol: EUR 412,500 · CHF 1.2m · SEK 3.4m. On a slide, "m" and "bn" with a space after the code and none before the unit ("EUR 2.4m").
- **Figures** in `figure-hero` are short: a percentage, a count or an amount, 6 characters at most ("68%", "18,400", "EUR 2.4m" drops to `figure`). What it measures goes underneath, in words.
- **Source line**, in mono, under every figure, chart and table: what the data is, its period and its size where you have it ("Backtest on 18,400 mortgage customers, 2025"). Add "· illustrative" for anything that isn't a real, approved result.
- **Dates**: "12–13 March 2027" on slides (en dash, no spaces); 2027-03-12 only in tables and screenshots.
- **Weights** in an evidence trail are two decimals in mono (0.41), and the weights shown on one moment add up to 1.00.

## Market typography

| | EN (UK) | DE / AT | CH-DE | NL / BE-NL | SV | DA | NO |
|---|---|---|---|---|---|---|---|
| Quotation marks | "…" | „…“ | «…» | "…" | ”…” | »…« | «…» |
| 10000 and above | 10,000 | 10.000 | 10’000 | 10.000 | 10 000 | 10.000 | 10 000 |
| Decimals | 6.1% | 6,1 % | 6.1% | 6,1% | 6,1 % | 6,1 % | 6,1 % |
| Currency | EUR 412,500 | EUR 412.500 | CHF 412’500 | EUR 412.500 | SEK 4 125 000 | DKK 4.125.000 | NOK 4 125 000 |
| Address form | you | Sie | Sie | u | du | du | du |
| Spelling | Oxford | Duden | Duden (ss for ß) | Groene Boekje | SAOL | Retskrivningsordbogen | Bokmålsordboka |

- Use typographic apostrophes and quotes (’ “ ” „ «), the en dash for ranges and the ellipsis character (…). Non-breaking spaces before % in German and the Nordics, and inside Nordic thousands.
- German and Dutch run 20–30% longer: step down from `title-statement` to `title-long`, or split the slide in two. Never narrow the margins or drop below 28px.
- Abbreviations never start a line ("For example", not "E.g."). Mid-line they're fine (e.g., etc.).

## Inclusive language

- English: *they / their* for generic people ("If an advisor needs the evidence, they can open it from the moment").
- German: neutral forms first (*Kundschaft*, *Mitarbeitende*, *Beratende*), otherwise *Kund:innen*. Never plain *Kunden* for a generic group.
- Dutch: *klanten* and *adviseurs* are already neutral; avoid *hij* for a generic advisor.
- Nordic languages: neutral nouns (*kund*, *kunde*), *hen* in Swedish only where the post's voice allows it.
- A named speaker or a story character may have a gender. A generic advisor, customer or account holder may not.

## Common corrections

| As drafted | Corrected |
|---|---|
| "Unlock hidden opportunities in your database" | "See which customers in your customer base are likely to refinance" |
| "€412,500" | "EUR 412,500" |
| "The Evidence Trail shows…" | "Evidence Trail shows…" |
| "Leads your advisors will love" | "Moments your advisors can explain" |
| "5 Checks Before You Trust A Score" | "5 checks before you trust a score" |
| "Up to 70% accuracy!" | "68% of flagged customers refinanced within six months" + source line |
| "Kunden mit auslaufender Zinsbindung" | "Kundschaft mit auslaufender Zinsbindung" |
| "It's not a score, it's a story" | "Each moment shows the three data points behind it" |
