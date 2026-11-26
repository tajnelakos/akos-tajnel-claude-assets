"""Build the portfolio front page (index.html) as one self-contained file:
theme CSS and page CSS inlined, photo embedded, all links absolute.
Run from the repo root: python portfolio/build-index.py"""
import base64, pathlib, html as h, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from work import GROUPS
ROOT = pathlib.Path(__file__).resolve().parent.parent
P = "https://akostajnel.com/"
G = "https://github.com/tajnelakos/akos-tajnel-claude-assets"
photo = "data:image/jpeg;base64," + base64.b64encode((ROOT / "portfolio/akos-tajnel.jpg").read_bytes()).decode()
poster = "data:image/jpeg;base64," + base64.b64encode((ROOT / "portfolio/film-poster.jpg").read_bytes()).decode()
theme = (ROOT / "knowledge-base/design-system/report-theme.css").read_text()
page = (ROOT / "portfolio/page.css").read_text()
def b64(path):
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()

def work_html():
    out = []
    for num, name, sub, rows in GROUPS:
        out.append(f'    <div class="group">\n      <div class="group__head"><span>{num}</span><h3>{name}</h3><p>{sub}</p></div>')
        for r in rows:
            o = " open" if r.get("open") else ""
            out.append(f'      <details class="item"{o}>')
            out.append(f'        <summary><span><span class="item__title">{h.escape(r["title"])}</span><span class="item__line">{h.escape(r["line"])}</span></span>'
                       f'<span class="item__stat">{h.escape(r["stat"])}' + (f'<small>{h.escape(r["stat_note"])}</small>' if r["stat_note"] else "") + '</span>'
                       f'<span class="item__more"><span class="c">Show</span><span class="o">Close</span></span></summary>')
            out.append('        <div class="item__body">')
            if r.get("video"):
                out.append('          <div class="item__video"><video src="{P}knowledge-base/video-design-system/assets/Films/segment-retail-lending-16x9.mp4" poster="{POSTER}" controls preload="none" playsinline aria-label="Seekridge mortgage lending film"></video></div>')
            if r["shots"]:
                cls = "gallery gallery--tall" if r.get("tall") else "gallery"
                imgs = "".join(f'<img src="{b64(ROOT / "portfolio/shots" / (f + ".jpg"))}" alt="{h.escape(a)}" loading="lazy">' for f, a in r["shots"])
                out.append(f'          <div class="gallery-wrap"><button class="gallery__prev" type="button" aria-label="Previous screenshots">‹</button><div class="{cls}">{imgs}</div><button class="gallery__next" type="button" aria-label="More screenshots">›</button></div>')
            links = "".join(f'<a class="item__link" href="{u}">{h.escape(t)}</a>' for t, u in r["links"])
            out.append(f'          <div class="item__links">{links}</div>')
            out.append('        </div>\n      </details>')
        out.append('    </div>')
    return "\n".join(out)

body = (ROOT / "portfolio/page-body.html").read_text().replace("{WORK}", work_html()).replace("{PHOTO}", photo).replace("{POSTER}", poster).replace("{P}", P).replace("{G}", G)
html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Akos Tajnel — Product marketing</title>
<meta name="description" content="Akos Tajnel, product marketer in B2B SaaS since 2018: launch process, customer insight, competitive intelligence and sales enablement, with the AI workflows behind them.">
<link rel="icon" href="{photo}">
<style>
{theme}
{page}
</style>
</head>
<body>
{body}
</body>
</html>
"""
(ROOT / "index.html").write_text(html)
print("index.html", len(html) // 1024, "KB")
