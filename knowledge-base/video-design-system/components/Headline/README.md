# Headline

The headline that carries every beat. Left-aligned at the margin, mono eyebrow above, one optional lead line below.

**Variants**

| Class | Type | Use | Full stop |
|---|---|---|---|
| `pwv-title` | Archivo 800, 120/120 | TitleCard hook, Statement claims, Navy only | Yes |
| `pwv-headline` | Archivo 700, 72/80 | Moment story beats, either ground | Yes |
| `pwv-headline-compact` | Archivo 700, 56/64 | Walkthroughs, beats sharing the frame with a large panel | No |

**The highlight.** Wrap up to three words in `<mark>`. On Paper they stay ink and a 6px gold bar draws under them as their line lands. On Navy they turn gold-light. One highlight per frame, and none if a gold element is already on screen (the gold point, the top evidence bar).

**Eyebrow.** IBM Plex Mono 500, 22px, +0.08em, uppercase in CSS, with a 48px 2px rule before it. It names the chapter or step: `EVIDENCE`, `STEP 2 / 5`, `DEPOSITS & SAVINGS · DACH`.

**Lead.** One line of Plex Sans 36px in `ink-muted`, under the headline. Optional; never repeats the headline.

**Motion.** Lines, not words: each line rises 24px out of a mask on its own baseline (`line-in` 500ms, `line-stagger` 120ms). The highlight bar draws as its line lands (`highlight-in` 400ms). Eyebrow fades in with the first line. The beat leaves with `fade-out`.

**Layout.** Split beats: 5 columns (706px) wide at the left margin, eyebrow top at 144px. Full beats: `is-wide` (1488px). Walkthrough lockup: `is-centre`.

**Provide.** The line(s), the highlighted words, the eyebrow, the variant.

**Avoid.** Centring over a centred panel, word-by-word animation, highlighting a mid-line verb, exclamation marks, question-mark hooks, Title Case.
