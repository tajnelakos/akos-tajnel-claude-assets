# Sample output

The rendered film: [`assets/Films/story-fixed-rate-dach-16x9.mp4`](./assets/Films/story-fixed-rate-dach-16x9.mp4) (48 s, silent, captions burnt in) · source: [`films/story-fixed-rate-dach-16x9.html`](./films/story-fixed-rate-dach-16x9.html) · check sheet: [`assets/Stills/contact-sheet-story.jpg`](./assets/Stills/contact-sheet-story.jpg)

---

## Input

> We need a short film for the mortgage lending page, aimed at VPs of Mortgage Lending at regional banks in DACH. It should show what happens with a customer whose fixed rate is about to end. English master first, German later.

## Output

```
## Film — Moment story · Head of Mortgage Lending · DACH (UK English master)

**Format and why:** Moment story. The viewer doesn't have Seekridge yet and needs to trust one
moment enough to act on it, so not a Walkthrough; one persona and one situation, so not a Statement.
**Length:** 48 s · 16:9 master. 4:5 (36 s, drops the layers beat) and the German cut follow.

| Time        | Beat      | Headline                                      | On screen                                                                 | Chapter   |
|-------------|-----------|-----------------------------------------------|---------------------------------------------------------------------------|-----------|
| 0.0–5.0 s   | TitleCard | Their fixed rate ends in four months.         | Navy; the dot map moves in, peaks rise, gold point lands; lockup; eyebrow MORTGAGE LENDING · DACH | —   |
| 5.0–10.0 s  | Tension   | By the time anyone notices, **they've moved.** | Wipe to Paper; Timeline: Today → Fixed rate ends 2027-03-31 → Refinanced elsewhere (marked) | Situation |
| 10.0–16.0 s | Layers    | Three layers. **One customer.**               | LayerStack: customer, transactions, market chips → node "Refinance risk"      | Situation |
| 16.0–21.5 s | Moment    | One moment, ranked **third.**                 | MomentCard: Refinance risk · 40-1187 · rank counts to 3 / 212 · two evidence rows | Moment |
| 21.5–31.0 s | Evidence  | Here's why it ranks third.                    | EvidenceTrail, 4 rows in plain words; FocusMarks on the lead row, rest dims; gold edge on the lead; lead line "The rate gap comes first." | Evidence |
| 31.0–37.0 s | Action    | On the advisor's list. **With the reasons.**  | CRM queue panel; synced row in focus; log line types: crm.synced …        | Action    |
| 37.0–42.0 s | Proof     | (figure)                                      | Wipe to Navy; 68% counts up; measure; source: backtest, demo lender's 2025 book (n = 1,940). Illustrative. | — |
| 42.0–48.0 s | EndCard   | Opportunities you can act on — and explain.   | Reversed lockup, line, action "Run a backtest on your own book"; 3 s hold  | —         |

**Voice-over** (96 words, ~2.3 words/s over 42 s of speech)
1. This customer's fixed rate ends in March.
2. Without a moment, the first anyone hears is the redemption notice.
3. Seekridge reads their customer data, their transactions and the market together.
4. Out of 40,000 customers, they're third on this week's list.
5. The biggest reason: the market rate is 1.7 points above their contract.
6. The salary split, local offers and the reset date make up the rest, adding up to 100.
7. The advisor gets the call in the CRM, with every reason attached.
8. Tested on a past book first, so you know what the ranking is worth.
9. See what your own book holds.

**Captions** → assets/Films/story-fixed-rate-dach-16x9.srt
 1.6–4.8   This customer's fixed rate ends in March.
 5.4–9.6   Without a moment, the first anyone hears / is the redemption notice.
10.4–15.6  Seekridge reads their customer data, / their transactions and the market together.
16.4–21.0  Out of 40,000 customers, they're third / on this week's list.
21.8–26.0  The biggest reason: the market rate / is 1.7 points above their contract.
26.2–30.6  The salary split, local offers and the reset date / make up the rest, adding up to 100.
31.4–36.6  The advisor gets the call in the CRM, / with every reason attached.
37.6–41.6  Tested on a past book first, / so you know what the ranking is worth.
42.4–45.8  See what your own book holds.

**Files:** films/story-fixed-rate-dach-16x9.html · assets/Films/story-fixed-rate-dach-16x9.mp4 ·
assets/Films/story-fixed-rate-dach-16x9.srt · assets/Stills/contact-sheet-story.jpg

**Checks:**
- First rule ✓ — the customer's situation (0–10 s) comes before the product (10 s); a viewer can
  repeat the top reason ("the market rate is 1.7 points above their contract").
- One gold per frame ✓ — the gold point (title), highlight bars (Paper beats), the top evidence bar with
  no headline highlight (evidence beat), gold-light words only on Navy.
- Figures ✓ — 68% carries its source and *Illustrative*; evidence rows are plain data points, with no weights or percentages.
- Captions ✓ — max 2 × 42 characters, none over the first 1.5 s or the last 2 s, never the
  headline word for word; inverted to a Paper band on Navy frames.
- No names ✓ — customer 40-1187, *the advisor*, demo lender Alpenkreis Bank.
- Still open: no cleared voice or music, so the master ships silent with captions.

---
Sourced from: personas.md (Head of Mortgage Lending: book growth and retention, integration effort) ·
knowledge-base.md (bank moment: fixed rate resets soon, likely to refinance elsewhere) ·
positioning.md (the end-card line) · this system's section 9 template and section 6 sample data
```

## Why this shape

- **The situation gets two beats before Seekridge is named.** The Head of Mortgage Lending cares about the book leaking; the timeline makes the cost concrete without a single feature.
- **The evidence beat is the longest (9.5 s).** It is what separates Seekridge from a score: if the film had to lose 10 seconds, the layers beat would go, not this one.
- **The proof is a backtest, not a customer quote**, and is labelled illustrative because the lender is a demo. A real cut needs an approved case and its source line.
- **The German cut is re-timed, not shrunk**: German runs about 20% longer, so the evidence and action beats each gain a second and the layers beat loses two.
