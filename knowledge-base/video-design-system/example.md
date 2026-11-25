# Sample output

The rendered film: [`assets/Films/story-outflow-dach-16x9.mp4`](./assets/Films/story-outflow-dach-16x9.mp4) (48 s, silent, captions burnt in) · source: [`films/story-outflow-dach-16x9.html`](./films/story-outflow-dach-16x9.html) · check sheet: [`assets/Stills/contact-sheet-story.jpg`](./assets/Stills/contact-sheet-story.jpg)

---

## Input

> We need a short film for the Outflow Watch page, aimed at Heads of Deposits & Savings at savings banks in DACH. It should show what happens with a customer who has quietly started moving money to another bank. English master first, German later.

## Output

```
## Film — Moment story · Head of Deposits & Savings · DACH (UK English master)

**Format and why:** Moment story. The viewer doesn't have Seekridge yet and needs to trust one
moment enough to act on it, so not a Walkthrough; one persona and one situation, so not a Statement.
**Length:** 48 s · 16:9 master. 4:5 (36 s, drops the layers beat) and the German cut follow.

| Time        | Beat      | Headline                                          | On screen                                                                 | Chapter   |
|-------------|-----------|---------------------------------------------------|---------------------------------------------------------------------------|-----------|
| 0.0–5.0 s   | TitleCard | Their savings just started to leave.        | Navy; the dot map moves in, peaks rise, gold point lands; lockup; eyebrow DEPOSITS & SAVINGS · DACH | — |
| 5.0–10.0 s  | Tension   | By the time anyone notices, **it's gone.**        | Wipe to Paper; Timeline: First transfer out 2026-06-02 → Today → Balance moved elsewhere (marked) | Situation |
| 10.0–16.0 s | Layers    | Three layers. **One customer.**                   | LayerStack: transactions, customer, market chips → node "Money starting to leave" | Situation |
| 16.0–21.5 s | Moment    | One moment, ranked **third.**                     | MomentCard: Money starting to leave · 40-1187 · rank counts to 3 / 212 · two evidence rows | Moment |
| 21.5–31.0 s | Evidence  | Here's why it ranks third.                        | EvidenceTrail, 4 rows, bars grow; FocusMarks on the top row, rest dims; gold top bar; lead "The new transfer counts most." | Evidence |
| 31.0–37.0 s | Action    | On the banker's list. **With the reasons.**       | CRM queue panel; synced row in focus; log line types: crm.synced …        | Action    |
| 37.0–42.0 s | Proof     | (figure)                                          | Wipe to Navy; 68% counts up; measure; source: backtest, demo bank's 2025 data (n = 1,940). Illustrative. | — |
| 42.0–48.0 s | EndCard   | Opportunities you can act on — and explain.       | Reversed lockup, line, action "Run a backtest on your own data"; 3 s hold  | —         |

**Voice-over** (~95 words, ~2.3 words/s over 42 s of speech)
1. This customer just started sending money to another bank.
2. Without a moment, the first anyone sees is the balance falling.
3. Seekridge reads their transactions, their products and the market together.
4. Out of 40,000 customers, they're third on this week's list.
5. The biggest reason: a new transfer of EUR 400 a month, since June.
6. Income, savings rates and products held make up the rest, adding up to 100.
7. The banker gets the call in the CRM, with every reason attached.
8. Tested on your past data first, so you know what the ranking is worth.
9. See what your own data holds.

**Captions** → assets/Films/story-outflow-dach-16x9.srt
 1.6–4.8   This customer just started sending / money to another bank.
 5.4–9.6   Without a moment, the first anyone sees / is the balance falling.
10.4–15.6  Seekridge reads their transactions, / their products and the market together.
16.4–21.0  Out of 40,000 customers, they're third / on this week's list.
21.8–26.0  The biggest reason: a new transfer / of EUR 400 a month, since June.
26.2–30.6  Income, savings rates and products held / make up the rest, adding up to 100.
31.4–36.6  The banker gets the call in the CRM, / with every reason attached.
37.6–41.6  Tested on your past data first, / so you know what the ranking is worth.
42.4–45.8  See what your own data holds.

**Files:** films/story-outflow-dach-16x9.html · assets/Films/story-outflow-dach-16x9.mp4 ·
assets/Films/story-outflow-dach-16x9.srt · assets/Stills/contact-sheet-story.jpg

**Checks:**
- First rule ✓ — the customer's situation (0–10 s) comes before the product (10 s); a viewer can
  repeat the top reason ("a new transfer of EUR 400 a month").
- One gold per frame ✓ — the gold point (title), highlight bars (Paper beats), the top evidence bar with
  no headline highlight (evidence beat), gold-light words only on Navy.
- Figures ✓ — 68% carries its source and *Illustrative*; weights 38 + 27 + 21 + 14 = 100.
- Captions ✓ — max 2 × 42 characters, none over the first 1.5 s or the last 2 s, never the
  headline word for word; inverted to a Paper band on Navy frames.
- No names ✓ — customer 40-1187, *the banker*, demo bank Alpenkreis Bank.
- Still open: no cleared voice or music, so the master ships silent with captions.

---
Sourced from: personas.md (Head of Deposits & Savings: money leaving before anyone notices) ·
knowledge-base.md (outflow moment: a new monthly transfer to another provider) ·
positioning.md (the end-card line) · this system's section 9 template and section 6 sample data
```

## Why this shape

- **The situation gets two beats before Seekridge is named.** The persona cares about deposits leaking; the timeline makes the cost concrete without a single feature.
- **The evidence beat is the longest (9.5 s).** It is what separates Seekridge from a score: if the film had to lose 10 seconds, the layers beat would go, not this one.
- **The proof is a backtest, not a customer quote**, and is labelled illustrative because the bank is a demo. A real cut needs an approved case and its source line.
- **The German cut is re-timed, not shrunk**: German runs about 20% longer, so the evidence and action beats each gain a second and the layers beat loses two.
