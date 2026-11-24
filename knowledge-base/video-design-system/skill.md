---
name: seekridge-film-builder
description: Plans and builds a Seekridge product film (Walkthrough, Signal story or Statement) from the Seekridge Video Design System — picks the format, writes the beat sheet, headlines, voice-over and captions in situation → signal → evidence → action order, builds the scenes in code from the system's tokens and components, checks stills, then renders the MP4 and its .srt. Use when the user wants a Seekridge video, a script or beat sheet for one, or a check of a cut against the film rules.
---

# Seekridge Film Builder

## Purpose

A product film fails the moment it shows a signal and moves on. The skill isn't animation — it's holding every beat to the brand's running order (situation, signal, evidence, action), keeping the evidence on screen long enough to read, and building the film from one system, so the tenth film looks like the first without anyone re-deciding colours, type or motion.

## Instructions

1. **Pick the format** from the film book's section 1 ([`README.md`](./README.md)): a Walkthrough if the viewer already has Seekridge and needs to use a feature, a Signal story if they need to trust a signal enough to act, a Statement if they need to notice one finding. If the brief could be two, ask once; if no one can answer, take the Signal story and say so.
2. **Name one persona and one segment** from [`../personas.md`](../personas.md) and the market (section 6). A Signal story for "everyone" is refused politely and turned into two films. The persona sets what the hook names and which evidence rows lead (section 3, *Per persona*).
3. **Write the beat sheet first, as a table** (time, beat, headline, on screen, chapter), using the beat structure for the format (section 2) and the template (section 9) as the default timing. Check the first rule before going on: read the beats aloud — does the viewer meet one customer's situation before the product, and could they repeat one reason behind the signal?
4. **Write the headlines** to section 3: 3–8 words a line, two lines max, up to three highlighted words, the frame's one gold. Then **write the voice-over** to section 7 (calm, 2.4 words a second in English, landing on the change it describes, never the headline word for word) and cut it into **captions** of at most two lines of 42 characters.
5. **Use only real product words and demo data**: signal names from [`components/SignalCard/README.md`](./components/SignalCard/README.md), screens from [`assets/Product UI/`](./assets/Product%20UI), a demo client and customer IDs from section 6. Every figure gets a source line or *Illustrative*; weights in an evidence trail sum to 100.
6. **Build the scenes in code**: copy the closest composition in [`films/`](./films), one `<section data-scene>` per beat, built only from the components in [`components/`](./components) and the tokens in [`tokens.css`](./tokens.css). Never type a hex value or a font size: use the `pwv-` classes and `--pwv-` variables.
7. **Check stills before rendering**: `render-film.py <film>.html --stills <busiest moment of each scene> --out check.jpg`. Look at every frame at full size against section 12 (one gold, no overlap with the caption zone, evidence readable, nothing centred that should be left-aligned). Fix, re-check, then render once.
8. **Render** with `render-film.py` (one MP4 per scene, joined without re-encoding), write the `.srt` from the same caption list, and name the file `<format>-<topic>-<market>-<ratio>.mp4`.
9. **Cut-downs** (4:5, 9:16) come from the finished master's beats and timing (section 8), never designed first.
10. **Before anything external ships**, run the script through [`../../marketing-assets/positioning-compliance`](../../marketing-assets/positioning-compliance).

## What to avoid

- Don't show a signal without its evidence trail, or speed up the evidence beat to fit a slot: cut another beat instead.
- Don't import anything from outside this system for "polish": no glows, blur, gradients, shadows, rounded cards, bounce, stock footage, illustrated people.
- Don't present demo figures as results, or name a customer.
- Don't write the voice-over as a read-out of the headlines, or narrate what the interface does instead of what changes for the customer and the bank.

## Output format

```
## Film — [format] · [persona] · [market]

**Format and why:** ...
**Length:** ... s · 16:9 master (+ cut-downs if asked)

| Time | Beat | Headline | On screen | Chapter |
|---|---|---|---|---|
| ... |

**Voice-over** (n words, ~2.4 words/s)
1. ...

**Captions** (in, out, text) → .srt
**Files:** films/<slug>.html · assets/Films/<slug>.mp4 · assets/Films/<slug>.srt · stills contact sheet
**Checks:** first rule ✓ · one gold per frame ✓ · figures sourced or illustrative ✓ · captions ≤ 2 × 42 ✓
```

A complete run of this skill for the reference Signal story is in [`example.md`](./example.md).
