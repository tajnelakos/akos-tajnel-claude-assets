"""Build portfolio version 2 (v2/index.html, served at akostajnel.com/v2/) as one self-contained file.
Uses the same projects and screenshots as v1 (portfolio/work.py, portfolio/shots), with its own look.
Run from the repo root: python portfolio/v2/build.py"""
import base64, html as h, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))
from work import GROUPS

P = "https://akostajnel.com/"
G = "https://github.com/tajnelakos/akos-tajnel-claude-assets"
TINTS = {"01": "#FDEBDD", "02": "#E3EEF8", "03": "#EDE7F6", "04": "#E4F2EA", "05": "#F6EEDC"}
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>'

def uri(path):
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()

img = {"poster": uri(ROOT / "portfolio/film-poster.jpg")}
projects, cards, filters = [], [], ['<button class="filter is-on" type="button" data-g="all" aria-pressed="true">All</button>']
for num, name, sub, rows in GROUPS:
    filters.append(f'<button class="filter" type="button" data-g="{num}" aria-pressed="false">{h.escape(name)}<small>{len(rows)}</small></button>')
    for r in rows:
        i = len(projects)
        for f, _ in r["shots"]:
            img[f] = uri(ROOT / "portfolio/shots" / (f + ".jpg"))
        projects.append(dict(cat=name, title=r["title"], line=r["line"], stat=r["stat"], note=r["stat_note"],
                             video=bool(r.get("video")), tall=bool(r.get("tall")), shots=r["shots"], links=r["links"]))
        cover = "poster" if r.get("video") else r["shots"][0][0]
        tall = " is-tall" if r.get("tall") else ""
        play = f'<span class="card__play">{PLAY}</span>' if r.get("video") else ""
        note = f'<span>{h.escape(r["stat_note"])}</span>' if r["stat_note"] else ""
        cards.append(
            f'<button class="card rv" type="button" data-i="{i}" data-g="{num}" aria-label="Open {h.escape(r["title"])}">'
            f'<span class="card__cover{tall}" style="--tint:{TINTS[num]}"><img data-k="{cover}" alt="">{play}</span>'
            f'<span class="card__cat">{h.escape(name)}</span>'
            f'<span class="card__title">{h.escape(r["title"])}</span>'
            f'<span class="card__line">{h.escape(r["line"])}</span>'
            f'<span class="card__stat"><b>{h.escape(r["stat"])}</b>{note}</span></button>')

photo = uri(ROOT / "portfolio/akos-tajnel.jpg")
css = (HERE / "v2.css").read_text()
safe = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
body = ((HERE / "body.html").read_text()
        .replace("{FILTERS}", "".join(filters)).replace("{CARDS}", "\n        ".join(cards))
        .replace("{IMG}", safe(img)).replace("{PROJECTS}", safe(projects))
        .replace("{PHOTO}", photo).replace("{P}", P).replace("{G}", G))
html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Akos Tajnel — Product marketing</title>
<meta name="description" content="Akos Tajnel, product marketer in B2B SaaS since 2018: launches, customer insight, competitive intelligence and sales enablement, with the AI workflows behind them.">
<meta name="robots" content="noindex">
<link rel="icon" href="{photo}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""
out = ROOT / "v2/index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html)
print(out.relative_to(ROOT), len(html) // 1024, "KB")
