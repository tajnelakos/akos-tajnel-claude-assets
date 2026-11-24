# LayerStack

How a customer's situation becomes data: three bands, one per layer, always in the order customer, property, market, each with two or three data chips; straight connectors meet in one navy node, the signal.

**Anatomy**
- Three flat white bands (980 × 132px), each a ProductPanel: layer icon + mono label, then data chips (mono 22px value, mono 18px uppercase key, sunken fill, 2px corners).
- Right-angled 2px connectors (never curves) from each band to one node.
- The node: navy fill, Paper text, `SIGNAL` label and the signal name. It is the only filled shape.

**Motion.** Bands trace in 600ms apart, chips fade in within each band; connectors draw (`draw`) once all three are in; the node fades in as they arrive. Total about 4 s; hold 1.5 s.

**Use.** The *Situation into data* beat of a Signal story; Walkthrough openers about connecting data; Head of Credit Risk films to show what goes in.

**Provide.** Two or three data points per layer with their values, the signal name.

**Avoid.** Colour per layer, arrows with heads, curved or diagonal connectors, more than three chips a band, sources the client hasn't connected.
