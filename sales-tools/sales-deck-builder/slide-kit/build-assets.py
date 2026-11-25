"""Generate the ridge illustrations used by the slide kit and the sample deck.

Run from this folder:  python3 build-assets.py
Writes assets/ridge-*.svg and prints each one's summit positions (SVG px),
which the slide HTML uses to place moment labels.
"""
import json
from ridge import ridge

SETS = {
    # name: (w, h, ground, peaks, extra kwargs)
    "ridge-cover":   (1040, 760, "navy", [(0.30, 0.55, 0.55, 0.055, "dot"), (0.55, 0.42, 1.05, 0.065, "gold"), (0.78, 0.6, 0.62, 0.055, "dot")], {}),
    "ridge-quiet":   (1700, 560, "navy", [(0.16, 0.55, 0.28, 0.05, "dot"), (0.40, 0.38, 0.30, 0.05, "dot"), (0.63, 0.62, 0.26, 0.05, "dot"), (0.85, 0.45, 0.30, 0.05, "dot")], {"base_opacity": 0.75}),
    "ridge-moments": (1700, 640, "navy", [(0.14, 0.62, 0.55, 0.05, "dot"), (0.36, 0.45, 0.70, 0.055, "dot"), (0.58, 0.38, 1.05, 0.06, "gold"), (0.84, 0.58, 0.62, 0.05, "dot")], {}),
    "ridge-moments-paper": (1700, 640, "paper", [(0.14, 0.62, 0.55, 0.05, "dot"), (0.36, 0.45, 0.70, 0.055, "dot"), (0.58, 0.38, 1.05, 0.06, "gold"), (0.84, 0.58, 0.62, 0.05, "dot")], {}),
    "ridge-forming": (1700, 600, "navy", [(0.14, 0.58, 0.20, 0.05, "ring"), (0.37, 0.42, 0.26, 0.05, "ring"), (0.60, 0.62, 0.22, 0.05, "ring"), (0.84, 0.46, 0.28, 0.05, "ring")], {}),
    "ridge-band-paper": (1920, 380, "paper", [(0.30, 0.5, 0.45, 0.06, "dot"), (0.62, 0.45, 0.7, 0.065, "dot"), (0.86, 0.55, 0.4, 0.06, None)], {"horizon": 0.12}),
    "ridge-band-navy": (1920, 380, "navy", [(0.22, 0.55, 0.35, 0.06, None), (0.55, 0.45, 0.55, 0.065, None), (0.82, 0.5, 0.4, 0.06, None)], {"horizon": 0.12, "base_opacity": 0.8}),
    "ridge-close":   (1040, 760, "navy", [(0.28, 0.6, 0.45, 0.05, "dot"), (0.52, 0.45, 0.62, 0.055, "dot"), (0.74, 0.40, 1.0, 0.06, "gold")], {}),
}

summits = {}
for name, (w, h, ground, peaks, kw) in SETS.items():
    svg, s = ridge(w, h, peaks, ground=ground, **kw)
    open(f"assets/{name}.svg", "w").write(svg)
    summits[name] = s
json.dump(summits, open("assets/summits.json", "w"), indent=1)
for k, v in summits.items():
    print(k, v)
