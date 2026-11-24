/*
 * Seekridge film engine: a frame-exact timeline for films built from this design system.
 *
 * Every animated element says when it starts (data-at, seconds from the start of its scene)
 * and what it does (data-fx). The engine turns the current time into one eased progress value
 * per element and writes it to the CSS variable --p (0 to 1). components/bundle.css does the
 * drawing from --p, so a page without this script shows every element in its finished state.
 *
 *   PWV.seek(t)            draw every timeline on the page at time t (seconds). Used by the renderer.
 *   PWV.play()             play every timeline in real time, looping (previews).
 *   PWV.duration           length of the page's main timeline, from [data-film-duration].
 *
 * Effects (data-fx), default length from tokens.json:
 *   lines   headline: each .pwv-line rises out of its mask (line-in, line-stagger); <mark> bars draw (highlight-in)
 *   rise    one block rises 24px and fades in (line-in)
 *   fade    opacity only (content-in)
 *   row     a panel row fades in and settles 8px (row-stagger applies via data-stagger on the parent)
 *   draw    an SVG stroke with pathLength="1" draws in (draw)
 *   fill    the gold point fills from its bottom edge (lot-fill)
 *   grow    a bar grows from the left to its width (bar-grow)
 *   trace   a panel's hairline frame traces clockwise, then its content fades in (frame-trace + content-in)
 *   count   a number counts up to data-to (count); data-dec, data-pre, data-suf, data-locale
 *   type    mono text types in at 28ms a character (type)
 *   focus   FocusMarks close in (focus-in); data-dim on the container dims everything not .is-focus
 *   wipe    a full-frame ground wipe, left to right (wipe)
 *   cue     no drawing; sets --p for custom CSS
 *
 * Scenes: <section data-scene data-start="5" data-end="10">. Hidden outside [start, end);
 * content fades out over the last 250ms unless data-no-out. data-drift="1.03" on an element
 * inside a scene pushes it in linearly over the scene.
 * data-until="4.5" on a wrapper fades it out over 250ms from that time (scene-relative): one headline
 * replacing another inside a scene. The wrapper must not carry a data-fx of its own.
 * Captions: <p data-cap data-in="5.2" data-out="8.4">, faded over 150ms, absolute times.
 */
(function () {
  "use strict";

  // cubic-bezier(0.2, 0, 0, 1): the brand's only curve.
  function bezier(x1, y1, x2, y2) {
    function a(p1, p2) { return 1 - 3 * p2 + 3 * p1; }
    function b(p1, p2) { return 3 * p2 - 6 * p1; }
    function c(p1) { return 3 * p1; }
    function calc(t, p1, p2) { return ((a(p1, p2) * t + b(p1, p2)) * t + c(p1)) * t; }
    function slope(t, p1, p2) { return 3 * a(p1, p2) * t * t + 2 * b(p1, p2) * t + c(p1); }
    return function (x) {
      if (x <= 0) return 0;
      if (x >= 1) return 1;
      var t = x;
      for (var i = 0; i < 8; i++) {
        var s = slope(t, x1, x2);
        if (Math.abs(s) < 1e-6) break;
        t -= (calc(t, x1, x2) - x) / s;
      }
      var lo = 0, hi = 1;
      for (var j = 0; j < 20 && Math.abs(calc(t, x1, x2) - x) > 1e-5; j++) {
        if (calc(t, x1, x2) < x) lo = t; else hi = t;
        t = (lo + hi) / 2;
      }
      return calc(t, y1, y2);
    };
  }
  var ease = bezier(0.2, 0, 0, 1);
  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }

  var DUR = { lines: 0.5, rise: 0.5, fade: 0.25, row: 0.4, draw: 0.8, fill: 0.3, grow: 0.5,
              trace: 0.6, count: 0.8, focus: 0.4, wipe: 0.5, cue: 0.5, type: 0 };
  var LINE_STAGGER = 0.12, HIGHLIGHT = 0.4, CONTENT_IN = 0.25, CHAR = 0.028, OUT = 0.25, CAP_FADE = 0.15;

  function num(el, name, dflt) {
    var v = el.getAttribute(name);
    return v === null || v === "" ? dflt : parseFloat(v);
  }

  function sceneOf(el) { return el.closest("[data-scene]"); }

  function Timeline(root) {
    this.root = root;
    this.loop = num(root, "data-loop", 0) || num(root, "data-film-duration", 0);
    this.items = [];
    this.scenes = [].slice.call(root.querySelectorAll("[data-scene]"));
    this.caps = [].slice.call(root.querySelectorAll("[data-cap]"));
    this.capBoxes = [].slice.call(root.querySelectorAll(".pwv-captions"));
    this.drifts = [].slice.call(root.querySelectorAll("[data-drift]"));
    this.untils = [].slice.call(root.querySelectorAll("[data-until]"));
    var self = this;

    // Expand headlines into per-line and per-mark items.
    [].slice.call(root.querySelectorAll('[data-fx="lines"]')).forEach(function (h) {
      var at = num(h, "data-at", 0);
      [].slice.call(h.querySelectorAll(".pwv-line > span")).forEach(function (span, i) {
        var start = at + i * LINE_STAGGER;
        self.add(span, "rise", start, DUR.lines);
        [].slice.call(span.querySelectorAll("mark")).forEach(function (m) {
          self.add(m, "grow", start + DUR.lines * 0.8, HIGHLIGHT);
        });
      });
    });

    // Staggered children: data-stagger="0.12" on a parent gives its [data-fx] children consecutive starts.
    [].slice.call(root.querySelectorAll("[data-stagger]")).forEach(function (parent) {
      var at = num(parent, "data-at", 0), step = num(parent, "data-stagger", 0.12);
      [].slice.call(parent.children).forEach(function (child, i) {
        if (!child.hasAttribute("data-at")) child.setAttribute("data-at", String(at + i * step));
      });
    });

    [].slice.call(root.querySelectorAll("[data-fx]")).forEach(function (el) {
      var fx = el.getAttribute("data-fx");
      if (fx === "lines") return;
      var at = num(el, "data-at", 0);
      var dur = num(el, "data-dur", DUR[fx] !== undefined ? DUR[fx] : 0.5);
      if (fx === "type") {
        el._full = el._full || el.textContent;
        dur = num(el, "data-dur", el._full.length * CHAR);
      }
      if (fx === "count") {
        el._to = num(el, "data-to", 0);
      }
      if (fx === "trace" && !el.querySelector(":scope > .pwv-trace")) {
        var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("class", "pwv-trace");
        svg.setAttribute("aria-hidden", "true");
        var r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        // Size comes from bundle.css (.pwv-trace rect), so the frame follows the panel.
        r.setAttribute("x", "0.5"); r.setAttribute("y", "0.5");
        r.setAttribute("pathLength", "1");
        svg.appendChild(r);
        el.insertBefore(svg, el.firstChild);
      }
      self.add(el, fx, at, dur);
    });
  }

  Timeline.prototype.add = function (el, fx, at, dur) {
    var sc = sceneOf(el);
    var base = sc ? num(sc, "data-start", 0) : 0;
    // A timeline nested inside another (a preview card) counts from its own root.
    if (sc && !this.root.contains(sc)) base = 0;
    this.items.push({ el: el, fx: fx, start: base + at, dur: Math.max(dur, 0.0001) });
  };

  Timeline.prototype.seek = function (t) {
    var i, it, p, e;
    for (i = 0; i < this.scenes.length; i++) {
      var sc = this.scenes[i];
      var s = num(sc, "data-start", 0), en = num(sc, "data-end", Infinity);
      var on = t >= s && t < en;
      sc.style.visibility = on ? "visible" : "hidden";
      // Captions sit above the scenes; they take the ground of the scene on screen.
      if (on && sc.hasAttribute("data-ground")) {
        for (var q = 0; q < this.capBoxes.length; q++) this.capBoxes[q].setAttribute("data-ground", sc.getAttribute("data-ground"));
      }
      var out = sc.hasAttribute("data-no-out") ? 0 : clamp((t - (en - OUT)) / OUT);
      sc.style.setProperty("--out", String(1 - ease(out)));
    }
    for (i = 0; i < this.drifts.length; i++) {
      var d = this.drifts[i], dsc = sceneOf(d);
      var ds = dsc ? num(dsc, "data-start", 0) : 0, de = dsc ? num(dsc, "data-end", ds + 5) : ds + 5;
      var k = clamp((t - ds) / (de - ds));
      d.style.transform = "scale(" + (1 + (num(d, "data-drift", 1.03) - 1) * k).toFixed(5) + ")";
    }
    for (i = 0; i < this.items.length; i++) {
      it = this.items[i];
      p = clamp((t - it.start) / it.dur);
      if (it.fx === "trace") {
        it.el.style.setProperty("--p", ease(p).toFixed(4));
        var c = clamp((t - it.start - it.dur) / CONTENT_IN);
        it.el.style.setProperty("--c", ease(c).toFixed(4));
        continue;
      }
      if (it.fx === "type") {
        var n = Math.floor(p * it.el._full.length + 1e-6);
        it.el.textContent = it.el._full.slice(0, n);
        it.el.style.setProperty("--p", p >= 1 ? "1" : "0");
        continue;
      }
      e = ease(p);
      it.el.style.setProperty("--p", e.toFixed(4));
      if (it.fx === "count") {
        var dec = num(it.el, "data-dec", 0);
        var loc = it.el.getAttribute("data-locale") || "en-GB";
        var v = p >= 1 ? it.el._to : it.el._to * e;
        var txt = new Intl.NumberFormat(loc, { minimumFractionDigits: dec, maximumFractionDigits: dec }).format(v);
        it.el.textContent = (it.el.getAttribute("data-pre") || "") + txt + (it.el.getAttribute("data-suf") || "");
      }
      if (it.fx === "focus") {
        var box = it.el.closest("[data-dim]");
        if (box) box.style.setProperty("--dim", (1 - e * (1 - num(box, "data-dim", 0.35))).toFixed(4));
      }
    }
    for (i = 0; i < this.untils.length; i++) {
      var u = this.untils[i], usc = sceneOf(u);
      var ub = (usc ? num(usc, "data-start", 0) : 0) + num(u, "data-until", Infinity);
      u.style.setProperty("--o", (1 - ease(clamp((t - ub) / OUT))).toFixed(4));
      u.style.visibility = t >= ub + OUT ? "hidden" : "visible";
    }
    for (i = 0; i < this.caps.length; i++) {
      var cp = this.caps[i], a = num(cp, "data-in", 0), b = num(cp, "data-out", 0);
      var o = Math.min(clamp((t - a) / CAP_FADE), clamp((b - t) / CAP_FADE));
      cp.style.opacity = o.toFixed(3);
      cp.style.visibility = o > 0 ? "visible" : "hidden";
    }
  };

  var timelines = [];
  function mountAll() {
    timelines = [];
    var roots = [].slice.call(document.querySelectorAll("[data-timeline]"));
    roots.forEach(function (r) { timelines.push(new Timeline(r)); });
  }

  var PWV = {
    ease: ease,
    mount: mountAll,
    seek: function (t) { timelines.forEach(function (tl) { tl.seek(t); }); },
    play: function () {
      var t0 = performance.now();
      function frame(now) {
        var t = (now - t0) / 1000;
        timelines.forEach(function (tl) { tl.seek(tl.loop ? t % tl.loop : t); });
        requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }
  };
  Object.defineProperty(PWV, "duration", {
    get: function () {
      var r = document.querySelector("[data-film-duration]");
      return r ? num(r, "data-film-duration", 0) : 0;
    }
  });
  window.PWV = PWV;

  function ready() {
    mountAll();
    if (window.PWV_RENDER || document.documentElement.hasAttribute("data-render")) PWV.seek(0);
    else if (!window.matchMedia || !window.matchMedia("(prefers-reduced-motion: reduce)").matches) PWV.play();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", ready);
  else ready();
})();
