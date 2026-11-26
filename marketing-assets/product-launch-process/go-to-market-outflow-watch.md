# Go-to-market plan: Seekridge Outflow Watch

The newest Seekridge product, run through the five-stage [launch process](./README.md) (define, prove, enable, launch, learn). Built with the [launch-plan skill](./skill.md) from the launch brief below, then filled in by hand where the skill leaves gaps for a person to decide.

Seekridge and every bank named here are fictional. Targets are plan targets, not results; there is no launch data yet.

---

## The launch brief

Filled in from the [launch brief template](./launch-brief-template.md) before the plan below was made. It stays a draft until the product lead decides it is ready.

**1. What changes, for whom**
- **In one sentence:** a bank's savings team sees which customers are starting to move money to another provider, with the reason, weeks before the balance falls.
- **Who notices first:** the Head of Deposits & Savings and their savings team.
- **Existing customers:** yes. A new moment family arrives in the same CRM queue; no new integration. Customer success briefs current customers before the announcement.

**2. Launch size:** Launch — a new product that brings in a second buyer.

**3. Who it's for**
- **Buyer:** Head of Deposits & Savings (Head of Retail Banking where one person owns both).
- **Segments, best fit first:** regional retail banks and savings banks · mutual and cooperative banks with a large saver base · credit unions on the web app (Ridge and Summit).
- **Markets, best fit first:** DACH · Benelux · Nordics.

**4. The story**
- **Before:** "We see the money leave when the balance is already gone, and raising the rate for everyone is ruinous."
- **After:** the savings team calls the customers whose money has started to move, with the reason in front of them. Proof number: share of last year's outflows flagged before the balance fell.
- **Proof we can show:** backtest on the customer's own 2025 data; the first pilot bank's results once it agrees to be named.
- **First objection:** "We already have a churn model." Answer: put the two side by side on last year's outflows and compare how early each flagged them.
- **Against the competition:** NexaScore scores customers without saying why; every Outflow Watch moment shows the transactions behind it.

**5. Name and words:** Seekridge Outflow Watch. Moments: *Money starting to leave*, *Balance drifting down*, *Card going quiet*. Avoid "churn score" and "primacy".

**6. Commercials and timing**
- **How it's sold:** paid add-on for platform customers · new subscription for new logos · inside Ridge and Summit for credit unions.
- **Price:** open (pricing owner).
- **Rollout:** pilot with two banks → early access → available to everyone; target months open.
- **Available through:** CRM integration · API · Seekridge web app.

**7. Launch kit and decision**
- **Kit:** the Launch kit, minus the press release until a pilot customer agrees to be named.
- **Decision:** product lead (open) decides; heads of sales and marketing agree; customer success and support informed. Date: open.

## Market and why now

- **The problem, in the buyer's words:** *"We see the money leave when the balance is already gone. It's never one big transfer. It's EUR 300 a month to someone paying a point more."* (from the [Head of Deposits & Savings persona](../../knowledge-base/personas.md#head-of-deposits--savings-buyer-deposits-and-savings)).
- **Why now:** digital banks and savings marketplaces make it a two-minute job to open an account elsewhere, and customers now spread their money across several providers. Raising the savings rate for everyone is the expensive answer; knowing whom to call is the cheap one.
- **Where it fits:** Outflow Watch is the fourth moment family alongside main-bank, growth and new-customer moments (see [`knowledge-base.md`](../../knowledge-base/knowledge-base.md)). It uses data the bank already shares with Seekridge, so for existing customers there is no new integration.

## Who it's for

| | Primary | Secondary |
|---|---|---|
| **Segment** | Regional retail banks and savings banks (Tier 1, see [`icp.md`](../../knowledge-base/icp.md)) | Mutual and cooperative banks with a large saver base (Tier 1–2) |
| **Buyer** | Head of Deposits & Savings | Head of Retail Banking |
| **Reviewers** (via the review pack) | Head of Model Risk, data protection officer | Vendor risk and compliance |
| **Users** | Savings team, relationship managers | Branch advisors |
| **Fit signals** | Visible deposit-rate fight in the bank's market; a churn model the team doesn't trust; savings growth targets | A new Head of Deposits hire; a CRM migration underway |

Not for: banks that want a customer-facing savings widget (that's Pocketlens' job, see [`competitive-landscape.md`](../../knowledge-base/competitive-landscape.md)), or banks with a hard on-prem requirement.

## Positioning

Built on the [message house](../../knowledge-base/positioning.md#message-house), in value → benefit → feature order:

- **Value:** keep the savings your customers already have with you.
- **Benefit:** call the customers who are starting to move money out, weeks before the balance falls, with a reason they recognise.
- **Feature:** outflow moments read from the bank's own transactions (new recurring transfers out, balance trends, card spend moving elsewhere), compared with what other banks pay on savings, each with its evidence trail and logged for review.

**One line:** *See who's moving money out, and why, before the balance shows it.*

**Against the alternatives:**

| Alternative | What we say |
|---|---|
| The bank's own churn model | It flags a closed account. Outflow Watch flags the first transfer, with the reason attached, and backtests on the bank's own past outflows. |
| Raising the savings rate for everyone | Expensive and blunt. Outflow Watch tells you which customers to call, so the offer goes where the money is actually moving. |
| NexaScore's next-best-action scores | Ask both vendors to show which named transactions drove one real moment, on a customer your team picks. |
| Ledgerline's Flow Alerts beta | A transfer alert without a ranking, an explanation or an audit log; the bank still builds and defends the logic. |

**Naming check:** "Outflow Watch" follows the brand rule of literal, descriptive feature names ([`brand-guidelines.md`](../../knowledge-base/branding-guideline/brand-guidelines.md)) and avoids any name already used for a comparable product in the market.

## 1. Define

- **Shape the product:** with product, test three use cases against real customer data: a new monthly transfer to an outside savings account, a balance drifting down over eight weeks, and a card going quiet while transfers out rise. Drop any moment type a banker can't explain to a customer in one sentence.
- **Messaging master:** tagline *See who's moving money out, and why.* · premise: outflows start small and early, and the evidence is already in the transactions · stage headlines: *It starts with one transfer.* → *Here's why this customer.* → *On the savings team's list, with the reasons.* · outcomes: deposits kept, cost of retention offers, customers who stay · illustration: the dot-map ridge with one gold point sliding away from the base.
- **Names:** product *Seekridge Outflow Watch*; moments *Money starting to leave*, *Balance drifting down*, *Card going quiet*. Copy follows [`writing.md`](../../knowledge-base/design-system/writing.md).
- **Package and price:**
  - Existing platform customers: add-on priced by the number of savers analysed.
  - New logos: Outflow Watch on its own, with an upgrade path to the full platform.
  - Credit unions on the web app: included in the Ridge and Summit tiers, not in Base.
  - Upsell path: banks live on main-bank moments add Outflow Watch first, since the data is already connected.

## 2. Prove

- **Pilot:** two existing customers, [Alpenkreis Bank](../case-study-builder/case-study-alpenkreis-bank.html) (DACH) and [Nordkredit](../case-study-builder/case-study-nordkredit.html) (Nordics), for eight weeks. The pilot tests three things: whether moments appear early enough to act on (weeks before the balance falls), whether bankers can say the reason out loud, and whether risk accepts the evidence trail for savings offers. It is a test, not a source of quotes.
- **Backtest offer for new logos:** a five-week backtest on a sample of the bank's own past outflows, the same motion that won the first Outflow Watch deal ([Thornfield Mutual](../../knowledge-base/sales-call-analysis/call-14-thornfield-mutual.md)).
- **Launch KPIs:**

| KPI | Target | Early or business result | Where measured |
|---|---|---|---|
| Pilot moments acted on by bankers | 60% within two weeks | Early (90 days) | Audit log, CRM |
| Existing customers adding Outflow Watch | 5 of the live base | Early (90 days) | CRM |
| Backtests started with new logos | 8 | Early (90 days) | CRM |
| Demo requests from Outflow Watch pages and campaigns | 40 | Early (90 days) | Website, CRM |
| Qualified pipeline | EUR 1.2M | Business result (6 months) | CRM |
| Win rate where Outflow Watch is in the deal | Above the platform average | Business result (6 months) | [`win-loss-analysis`](../../knowledge-base/win-loss-analysis) |

- **Demo readiness** (to check once each demo is built on local data):

| Market | Segment | Rating | Missing |
|---|---|---|---|
| DACH | Retail banks | To check | — |
| DACH | Savings banks | To check | Sparkasse-group product names in the demo data |
| Benelux | Savings banks | To check | Dutch merchant categories for local savings apps |
| Nordics | Retail banks | To check | Mobile-payment transfers labelled correctly |
| DACH, Benelux | Credit unions (web app) | To check | Seat-based demo workspace |

## 3. Enable

- **Sales:** a one-page quick reference, an Outflow Watch section in the [retail banks deck](../../sales-tools/sales-deck-builder/deck-retail-banks.html), a demo playbook built around one outflow moment, market training per region, and updated [battlecards](../../sales-tools/battlecard) with the NexaScore and Ledgerline lines above.
- **CSMs and support:** what changes for existing customers (no new integration, a new moment family in the same CRM queue), a product FAQ (how outflow moments differ from the bank's churn model, how purpose limits on transaction data apply), and how to handle first questions from savings teams.

## 4. Launch

- **Website:** an Outflow Watch solution page with a 30-second film; the [moment story film](../../knowledge-base/video-design-system/assets/Films/story-outflow-dach-16x9.mp4) is the reference cut, mocked up then built in Framer.
- **Press and partners:** an announcement timed to the pilot's end; co-marketing with one CRM partner on "outflow moments inside your CRM."
- **Users:** an in-app note for existing customers; a Head of Deposits & Savings email sequence ([`persona-email-sequence`](../persona-email-sequence)); a blog post on why outflows start with one transfer ([`blog-post-builder`](../blog-post-builder)); a LinkedIn carousel in the moment-explainer format ([`linkedin-carousels`](../../knowledge-base/linkedin-carousels)).
- **Events:** a deposits and treasury event in DACH with a flyer ([`flyer-design-system`](../../knowledge-base/flyer-design-system)), a roll-up and the film on loop.

## 5. Learn

| Feedback source | KPI it feeds |
|---|---|
| Pilot audit log: moments viewed, acted on, dismissed (with reasons) | Pilot moments acted on |
| Sales calls and objections ([`sales-call-analysis`](../../knowledge-base/sales-call-analysis)) | Backtests started, pipeline |
| Win/loss with Outflow Watch in the deal ([`win-loss-analysis`](../../knowledge-base/win-loss-analysis)) | Win rate |
| Campaign and web performance ([example analysis](../persona-email-sequence/campaign-performance-analysis.html)) | Demo requests |
| CSM and customer feedback on moment quality | Add-on adoption |

What comes back feeds the next round of shaping the product: moment types bankers dismiss most often are the first to be reworked or dropped.

---

**Open gaps for the user:** who decides the brief is ready, and when; price; pilot start dates; price points for the add-on and the stand-alone product; which CRM partner to approach; KPI baselines once the pilot runs.
