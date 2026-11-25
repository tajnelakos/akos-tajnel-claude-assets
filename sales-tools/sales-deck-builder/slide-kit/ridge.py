"""Draw a static Seekridge ridge field (the dot-map mountains) as an SVG.

The customer base is a field of dots seen at an angle; a few areas rise into
peaks (the week's moments), and one summit can carry the gold point.

Usage, from Python:
    from ridge import ridge
    svg, summits = ridge(1000, 520, peaks=[(0.5, 0.45, 1.0, 0.07, "gold")], ground="navy")
summits lists each peak's summit position in SVG pixels, for placing labels.

Each peak is (x, depth, height, width, marker): x and depth run 0..1
(depth 0 is the horizon, 1 the front edge), height ~0.3..1.2, width ~0.04..0.09,
marker is "gold", "dot", "ring" (an early sign, outlined) or None.
"""
import math

NAVY, PAPER, GOLD = "#1A3A5C", "#F4F3EF", "#C1892E"


def ridge(w, h, peaks, ground="navy", cols=96, rows=34, horizon=0.18,
          spread=1.35, lift=0.55, dot=2.6, wave=0.012, fade_edges=True,
          base_opacity=1.0):
    ink = PAPER if ground == "navy" else NAVY
    s_min = 0.34

    def height(u, v):
        z = wave * math.sin(u * 9.0 + v * 4.0) * math.cos(v * 7.0 - u * 3.0)
        for (pu, pv, a, s, *_rest) in peaks:
            d2 = ((u - pu) ** 2) / (s * s * 1.6) + ((v - pv) ** 2) / (s * s * 1.0)
            z += a * math.exp(-d2 / 2.0)
        return z

    def project(u, v, z):
        scale = s_min + (1 - s_min) * v          # far rows smaller
        x = w / 2 + (u - 0.5) * spread * w * scale
        yg = h * horizon + (h * 0.98 - h * horizon) * ((scale - s_min) / (1 - s_min)) ** 1.15
        y = yg - z * lift * h * scale
        return x, y, scale

    out = []
    for j in range(rows):
        v = j / (rows - 1)
        for i in range(cols):
            u = i / (cols - 1)
            z = height(u, v)
            x, y, scale = project(u, v, z)
            if x < -4 or x > w + 4 or y < -4 or y > h + 4:
                continue
            op = 0.10 + 0.26 * scale + min(z, 1.0) * 0.6
            if v > 0.8:                      # soften the front edge
                op *= 1 - (v - 0.8) / 0.2 * 0.65
            if fade_edges:
                edge = min(u, 1 - u) / 0.18
                op *= max(0.0, min(1.0, edge))
            op = max(0.0, min(0.95, op * base_opacity))
            if op < 0.03:
                continue
            r = dot * (0.55 + 0.45 * scale)
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill-opacity="{op:.2f}"/>')

    summits, marks = [], []
    for (pu, pv, a, s, *rest) in peaks:
        kind = rest[0] if rest else "dot"
        x, y, scale = project(pu, pv, height(pu, pv))
        y -= 6
        summits.append((round(x), round(y)))
        if kind == "gold":
            marks.append(f'<circle cx="{x:.1f}" cy="{y-6:.1f}" r="11" fill="{GOLD}"/>')
            summits[-1] = (round(x), round(y - 6))
        elif kind == "dot":
            marks.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="{ink}" fill-opacity="0.92"/>')
        elif kind == "ring":
            marks.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="none" stroke="{ink}" stroke-width="2" stroke-dasharray="3 3"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
           f'<g fill="{ink}">{"".join(out)}</g>{"".join(marks)}</svg>')
    return svg, summits


if __name__ == "__main__":
    svg, s = ridge(1000, 520, [(0.25, 0.55, 0.5, 0.06, "dot"), (0.55, 0.4, 1.0, 0.07, "gold"), (0.8, 0.6, 0.6, 0.06, "dot")])
    open("/tmp/ridge-test.svg", "w").write(f'<html><body style="margin:0;background:{NAVY}">{svg}</body></html>')
    print(s)
