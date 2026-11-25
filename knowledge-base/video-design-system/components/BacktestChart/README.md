# BacktestChart

The proof behind a figure, for Head of Mortgage Lending and Head of Retail Banking films: how moments ranked in past periods performed on the client's own book.

**Anatomy**
- Bars by moment-rank decile (1 = highest ranked), navy on Paper (Paper at 55% on Navy); **decile 1 in gold**: the frame's gold.
- The book average as a 2px dashed `ink-muted` line with its label in mono.
- Hairline gridlines, axis labels and values in IBM Plex Mono, values above bars.
- A one-line takeaway as the headline (*The top tenth refinanced at 7× the book average.*) and a source line under the chart: method, period, n.

**Motion.** Baseline axis draws (`draw`), bars rise from it left to right 80ms apart (`fill`, 500ms), values fade in over them, the average line fades in last. Hold 2 s.

**Provide.** Ten values, the measure, the average, method and period.

**Avoid.** 3D bars, gradients, more than one gold bar, a y-axis that doesn't start at zero, smoothing lines, decile labels in Archivo.
