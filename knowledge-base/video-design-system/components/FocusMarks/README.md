# FocusMarks

How Seekridge points at something: four corner brackets close in on it from 40px outside, like the corner marks on a site plan, and everything else in the panel dims to 35%. It replaces blur, glows, zoom bubbles and halos.

**Anatomy.** Four 28px brackets, 3px navy strokes, square ends, 12px outside the element. On a Navy ground the brackets turn Paper.

**Motion.** `focus-in` (400ms): brackets travel 40px inwards and fade in; at the same time the container (`data-dim="0.35"`) dims every row that is not `.is-focus`. They stay until the beat ends.

**Markup.** Put `<span class="pwv-focus" data-fx="focus" data-at="…"><i></i><i></i><i></i><i></i></span>` inside the focused element and give it `.is-focus`; put `data-dim="0.35"` on its container.

**Use.** One focus per beat: the top evidence row, the moment in a list, the synced row in the CRM queue, a figure in a chart.

**Avoid.** Two focused things at once, focus on the headline, blur on the dimmed rows, animating the brackets more than once.
