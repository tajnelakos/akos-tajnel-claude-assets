# Films (sources)

The HTML compositions of the reference films and the script that renders them. Each composition is a single 1920 × 1080 `.pwv-stage` holding one `<section data-scene>` per beat, built only from `../tokens.css`, `../components/bundle.css` and `../components/film-engine.js`. Open one in a browser to watch it loop at screen size.

| File | Renders to |
|---|---|
| `story-outflow-dach-16x9.html` | `../assets/Films/story-outflow-dach-16x9.mp4` |
| `walkthrough-evidence-trail-16x9.html` | `../assets/Films/walkthrough-evidence-trail-16x9.mp4` |
| `segment-retail-lending-16x9.html` | `../assets/Films/segment-retail-lending-16x9.mp4` |
| `statement-evidence-16x9.html` | `../assets/Films/statement-evidence-16x9.mp4` |
| `render-film.py` | Stills contact sheet or full MP4 from any composition |

## Render

```bash
pip install playwright pillow && playwright install chromium   # once; ffmpeg must be on PATH
# 1. check the busiest frame of each scene first
python render-film.py story-outflow-dach-16x9.html --stills 4.5,9.6,15.6,21.2,30.6,36.6,41.6,46.5 --out check.jpg
# 2. then render once
python render-film.py story-outflow-dach-16x9.html --out ../assets/Films/story-outflow-dach-16x9.mp4
```

Fonts are bundled in `../fonts/` and loaded by `../tokens.css`, so rendering works offline; `--font-css` is only needed to override them.

## Building a new film

Copy the composition closest to the format you need and change the scenes. Each scene sets its ground (`data-ground="paper|navy"`) and its start and end in seconds; every element inside it says when it starts (`data-at`, seconds from the scene's start) and what it does (`data-fx`). Captions are `<p data-cap data-in data-out>` in the stage's `.pwv-captions`, and the `.srt` sidecar carries the same lines. The engine's header comment lists every effect. The full method, from brief to render, is [`../skill.md`](../skill.md).
