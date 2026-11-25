---
name: personalized-outbound
description: Drafts one outbound email or LinkedIn message from an account brief, referencing the account's actual trigger moment and positioning angle, following the brand voice guide. Use when the user has an account brief (from abm-account-brief or similar) and wants an outreach draft — not a generic template with the account name inserted.
---

# Personalized Outbound

## Purpose

Turn an account-specific brief into one outbound message that could only have been sent to this account — not a template that happens to mention their name.

## Instructions

1. **Require the trigger/moment to be referenced specifically**, not generically. "I saw you're growing" is not this; "I saw you recently brought on a new Head of Credit Risk and are replacing your customer-targeting tooling" is.
2. **Lead with the account's situation, not our product.** The first line should establish that this message is about them specifically — the product enters after that, as the response to their situation, not the subject of the message.
3. **Use the positioning angle already selected in the brief** — don't default to a generic pitch if the brief specifies a particular angle (e.g. defensibility over speed).
4. **One clear, low-friction ask.** Not "let's set up a call to discuss our platform" — something specific and small enough to say yes to (e.g. "worth a 15-minute conversation about how you're thinking about explainability requirements for the new tooling?").
5. **Follow [`branding-guideline`](../../knowledge-base/branding-guideline/skill.md)'s voice rules** — no hype language, no banned terms, second person and direct.
6. **Keep it short.** Cold/warm outbound that requires scrolling doesn't get read; aim for under 120 words for email, shorter for LinkedIn.
7. **If the input brief doesn't contain a specific enough trigger to personalize against, say so** rather than producing generic outbound dressed up as personalized — a message with no real hook shouldn't ship under this skill's output.
8. **Match the confidence of the ask to the strength of the underlying moment.** A brief built on a single, uncorroborated moment (see [`icp-buying-moment-monitor`](../../sales-tools/icp-buying-moment-monitor)'s Strong/Medium distinction) should read as more exploratory than one built on multiple corroborating moments — don't borrow the confidence a stronger moment would have earned. See [`example-court-street-lending-head-of-credit-risk.md`](./example-court-street-lending-head-of-credit-risk.md) for a worked case.
9. **The same account can warrant more than one message if more than one persona is in play** — multi-threading with a second stakeholder means re-reading the *same* trigger through that persona's own decision criteria (`personas.md`), not repeating the first message with a new name. See [`example-nordkredit-vp-mortgage-lending.md`](./example-nordkredit-vp-mortgage-lending.md).

## Opening

The first two lines decide whether the rest gets read. Build them from [`openers.md`](./openers.md):

- **First line: their exact role and company, worded the way their title reads.** For example: "I noticed you oversee collateral management at [Bank]." If the brief says where the detail came from (an article, a post, an event, their website), say so.
- **Introduce yourself in one clause, in the reader's field's terms.** Don't describe the company. The same rep sounds different to a compliance head than to a lending head.
- **Then give the reason for writing,** picking the opener that fits the trigger: what peers are doing about a rule, a gap you keep seeing, or one real question about their setup. The product only comes in after this.
- **One recognisable connection at most** (a sister company or partner in their group), as a by-the-way line, and only if the brief supports it.
- **Make the ask answerable in one line,** and leave a referral route out when the brief doesn't confirm this person owns the topic: "If not, who on your team owns it?"

## What to avoid

- Don't invent a trigger or detail not present in the account brief.
- Don't lead with company boilerplate ("At Seekridge, we believe...") — this reads as a template regardless of what follows it.
- Don't ask for a demo in the first message unless the brief indicates the account is already late-stage aware of the product.
- Don't open with "I hope this message finds you well," "Forgive me if…," or any other line that delays the point.
- Don't list data points, features or products, and don't list client logos. Name the one thing that answers the trigger.
- Don't use "synergy," "in a nutshell, we specialise in…," "industry-leading" or "most comprehensive."
- Don't put a benefit in the subject line ("Boost your…"). The subject names their situation.

## Output format

```
## Outbound Draft — [Account name] — [channel: Email / LinkedIn]

Subject: [if email]

[message body]

---
Personalization used: [the specific trigger/detail this message depends on]
```
