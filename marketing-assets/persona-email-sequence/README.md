# Persona Email Sequence

## The problem

Nurture sequences are usually written once for "the buyer" in general, then sent to everyone regardless of role — so an email about deposit outflows lands on someone who owns lending growth, and vice versa. The fix isn't more emails, it's sequences actually built around what a specific persona's decision-making process looks like, using [`personas.md`](../../knowledge-base/personas.md) instead of a single generic buyer.

This builds a reusable multi-email sequence for a persona segment — for marketing automation, not 1:1 sales outreach.

## The approach

A skill that takes a persona (from `personas.md`) and a starting context (e.g. "downloaded the explainable-moments whitepaper") and produces a short sequence — each email escalating naturally through that persona's actual decision criteria, not just increasing urgency. The sequence explicitly avoids restating the same value proposition three ways; each email should earn its place by advancing a different part of that persona's evaluation.

## Files — quick mode

- [`skill.md`](./skill.md) — the Claude Skill definition, covering both modes
- [`example.md`](./example.md) — a 3-email sequence for the Head of Deposits & Savings persona, content only

## Files — deep-dive campaign mode

For when the ask is a full, run-ready campaign rather than just sequence copy — see [`skill.md`](./skill.md)'s "Deep-dive campaign mode" section:

- [`campaign-head-of-deposits-and-savings.md`](./campaign-head-of-deposits-and-savings.md), [`campaign-head-of-retail-banking.md`](./campaign-head-of-retail-banking.md) — full 5-email, A/B-tested sequences for the two buyers we market to — the Head of Deposits & Savings and the Head of Retail Banking ([`personas.md`](../../knowledge-base/personas.md)); risk and data protection are reviewers, reached through the buyer with a prepared pack, not marketing targets, each extending its quick-mode equivalent with an extra decision-criterion email and a trust-trigger email
- [`campaign-metrics.csv`](./campaign-metrics.csv) — tracked sends for both campaigns, both A/B variants, all 5 emails: sent, delivered, opened, clicked, replied, meetings booked, unsubscribed (fictional, internally consistent — see the analysis for the rates computed from it)
- [`campaign-performance-analysis.html`](./campaign-performance-analysis.html) — the computed analysis, built from that CSV ([view live ↗](https://tajnelakos.github.io/akos-tajnel-claude-assets/marketing-assets/persona-email-sequence/campaign-performance-analysis.html)). The headline finding: the same two subject-line techniques produced the *opposite* winner for the two personas — evidence against generalizing one persona's A/B result to another.
- [`reply-handling-playbook.md`](./reply-handling-playbook.md) — reply types (technical objection, "forwarded to my analyst/risk lead," timing pushback, hard no) mapped to persona-specific response guidance
- [`deliverability-checklist.md`](./deliverability-checklist.md) — generic pre-send and during-send checklist (SPF/DKIM/DMARC, list hygiene, bounce/complaint thresholds); not persona-specific, run once per campaign regardless of which persona it targets

## Current limitations

Quick mode outputs email content only — no tracking or send infrastructure, by design, for when that's all that's needed. Deep-dive mode's tracking data is a one-time fictional snapshot rather than a live feed from an actual ESP/marketing automation platform, the same limitation [`win-loss-analysis`](../../knowledge-base/win-loss-analysis) has with its CRM export. Wiring either mode into the marketing automation platform's actual trigger/branch logic (e.g. stop the sequence if the contact books a call) is next.
