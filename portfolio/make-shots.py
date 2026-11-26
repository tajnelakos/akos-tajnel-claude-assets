"""Capture the screenshots shown inside the portfolio dropdowns.
Each shot scrolls a page so an anchor text sits near the top, then captures the viewport.
Run from the repo root: python portfolio/make-shots.py"""
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "portfolio" / "shots"
# name: (page, anchor text or None for the top, viewport width, viewport height)
SHOTS = {
  "launch-1": ("marketing-assets/product-launch-process/launch-process.html", None, 1280, 820),
  "launch-2": ("marketing-assets/product-launch-process/launch-process.html", "Each stage produces what the next one needs", 1280, 820),
  "launch-3": ("marketing-assets/product-launch-process/launch-process.html", "Demo readiness, by market and use case", 1280, 820),
  "launch-4": ("marketing-assets/product-launch-process/launch-process.html", "Feedback, measured against the launch KPIs", 1280, 820),
  "winloss-1": ("knowledge-base/win-loss-analysis/win-loss-detailed-analysis.html", None, 1280, 820),
  "winloss-2": ("knowledge-base/win-loss-analysis/win-loss-detailed-analysis.html", "Key findings", 1280, 820),
  "winloss-3": ("knowledge-base/win-loss-analysis/win-loss-detailed-analysis.html", "Buyer Demographics", 1280, 820),
  "calls-1": ("knowledge-base/sales-call-analysis/call-analysis-summary.html", None, 1280, 820),
  "calls-2": ("knowledge-base/sales-call-analysis/call-analysis-summary.html", "Buying moment distribution", 1280, 820),
  "campaigns-1": ("marketing-assets/persona-email-sequence/campaign-performance-analysis.html", None, 1280, 820),
  "campaigns-2": ("marketing-assets/persona-email-sequence/campaign-performance-analysis.html", "Key findings", 1280, 820),
  "competitors-1": ("sales-tools/competitor-monitoring/competitor-analyses.html", None, 1280, 820),
  "competitors-2": ("sales-tools/competitor-monitoring/competitor-analyses.html", "Germany, Austria and Switzerland", 1280, 820),
  "bc-1": ("sales-tools/battlecard/nexascore.html", None, 1280, 900),
  "bc-2": ("sales-tools/battlecard/ledgerline.html", None, 1280, 900),
  "bc-3": ("sales-tools/battlecard/conturo.html", None, 1280, 900),
  "bc-4": ("sales-tools/battlecard/pocketlens.html", None, 1280, 900),
  "bc-detail": ("sales-tools/battlecard/nexascore.html", "Where they", 1280, 900),
  "case-1": ("marketing-assets/case-study-builder/case-study-alpenkreis-bank.html", None, 1100, 1000),
  "case-2": ("marketing-assets/case-study-builder/case-study-alpenkreis-bank.html", "New opportunities by type", 1100, 1000),
  "case-3": ("marketing-assets/case-study-builder/case-study-alpenkreis-bank.html", "From moment to closed business", 1100, 1000),
  "onepager-1": ("marketing-assets/one-pager-builder/one-pager-retail-banking.html", None, 1000, 1300),
  "onepager-2": ("marketing-assets/one-pager-builder/one-pager-retail-banking.html", "Call before", 1000, 1300),
  "trifold-1": ("knowledge-base/flyer-design-system/examples/trifold-retail-banks.html", None, 1280, 900),
  "review-1": ("knowledge-base/flyer-design-system/examples/one-pager-review-pack.html", None, 1000, 1300),
  "carousel-1": ("knowledge-base/linkedin-carousels/gallery.html", "Moment explainer", 1280, 640),
  "carousel-2": ("knowledge-base/linkedin-carousels/gallery.html", "Proof in numbers", 1280, 640),
  "carousel-3": ("knowledge-base/linkedin-carousels/gallery.html", "Feature launch", 1280, 640),
  "ds-web": ("knowledge-base/design-system/components.html", None, 1280, 820),
  "ds-video": ("knowledge-base/video-design-system/preview.html", None, 1280, 820),
}
FIND = """(t) => { const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n; while ((n = w.nextNode())) { if (n.textContent.includes(t) && n.parentElement.offsetParent !== null) {
    const r = n.parentElement.getBoundingClientRect(); return r.top + window.scrollY; } } return null; }"""
with sync_playwright() as p:
    kw = {"executable_path": "/usr/bin/google-chrome"} if pathlib.Path("/usr/bin/google-chrome").exists() else {}
    b = p.chromium.launch(**kw)
    for name, (rel, anchor, w, h) in SHOTS.items():
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto((ROOT / rel).as_uri()); pg.wait_for_timeout(1500)
        y = 0
        if anchor:
            y = pg.evaluate(FIND, anchor)
            if y is None: print("ANCHOR NOT FOUND", name); pg.close(); continue
            y = max(0, y - 40)
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(400)
        tmp = OUT / f"{name}.png"; pg.screenshot(path=str(tmp))
        im = Image.open(tmp).convert("RGB"); im.thumbnail((1200, 1400))
        im.save(OUT / f"{name}.jpg", quality=72, optimize=True); tmp.unlink(); pg.close()
        print("ok", name)
    # Sales deck: screenshot individual slides
    DECK = [1, 3, 5, 6, 7, 11]
    pg = b.new_page(viewport={"width": 1400, "height": 900})
    pg.goto((ROOT / "sales-tools/sales-deck-builder/deck-retail-banks.html").as_uri()); pg.wait_for_timeout(1500)
    for k, n in enumerate(DECK, 1):
        tmp = OUT / f"deck-{k}.png"; pg.locator(".slide").nth(n - 1).screenshot(path=str(tmp))
        im = Image.open(tmp).convert("RGB"); im.thumbnail((1200, 1200)); im.save(OUT / f"deck-{k}.jpg", quality=72, optimize=True); tmp.unlink()
        print("ok", f"deck-{k}")
    pg.close()
    b.close()
