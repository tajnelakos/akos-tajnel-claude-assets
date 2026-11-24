# Captions

Burnt-in captions of the voice-over, on every cut of every film, with or without sound. Most Parcelwise films are watched muted.

**Style.** `caption` (IBM Plex Sans 500, 44/56px at 1080p) in `caption-ink` on the `caption-band`, square corners, 32px horizontal padding. On Navy frames the band inverts: Paper at 96% with ink text, because a navy band disappears on the Navy ground.

**Position.** Left-aligned at the 96px margin (not centred: every Parcelwise frame reads from the left). The band's bottom edge sits at `caption-bottom`, 160px above the frame bottom; the ChapterRail sits underneath.

| Rule | Detail |
|---|---|
| Length | 2 lines, 42 characters a line; break at a phrase, never inside an ID, a figure or a currency amount |
| Timing | The spoken line; 1.2 s minimum, 6 s maximum; 150ms fade in and out, no movement |
| Silence | None over the TitleCard's first 1.5 s or the EndCard's last 2 s |
| Sidecar | `.srt` with the same text, same timings |
| Overlap | Never the headline word for word |

**Markup.** `<p data-cap data-in="5.2" data-out="8.6">…</p>` inside `.pwv-captions`; the engine fades each one at its times.

**Avoid.** Centred captions, captions in Archivo, white boxes, karaoke word highlighting, captions over the bottom 160px.
