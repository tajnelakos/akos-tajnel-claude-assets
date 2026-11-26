# MomentExplainer

Shows how one moment is built: a question cover, the tension, the three data layers, the evidence trail, and what the advisor does with it.

**Use it for** the brand's core story, told through one concrete moment: money starting to leave, a salary landing at another bank, a customer ready for a mortgage. It's the format that proves the promise (*opportunities you can act on — and explain*) rather than stating it. 6 slides.

**You provide**
- One segment and persona (see [`../../../personas.md`](../../../personas.md)) and one moment type.
- A cover question that names the customer situation: `title-cover`, about 8 words ("Which customers are moving money out?"), plus one `body-lead` line in `paper-72`.
- The tension in one statement: why a score or a list isn't enough for this reader.
- One line per data layer, in this order: transaction data, customer data, market data.
- Three to five evidence rows for one illustrative customer: the data point in words, its layer and its weight (two decimals; the weights shown add up to 1.00).
- Two or three actions for the advisor, each a full sentence.
- A close with one action ("See a moment built on your own data.").

**Build rules**
- Cover: lockup top-left, `layer-stack` motif on the right (top ≈ 200px, bleeding off the right edge), title block anchored 240px from the bottom and kept 200px clear of the right edge, arrow at the margin. The motif's gold point is the cover's gold, so no highlighted words.
- Tension: eyebrow "Moment explainer", `title-statement` at top ≈ 300px with up to 3 words in `gold-light`, one `body-lead` line in `paper-72`.
- Layers: eyebrow "Three data layers", `heading`, then three layer rows (64px icon, mono layer name, `body` line), 32px apart.
- Evidence: a paper slide. `heading` at top 192px, then the screenshot frame (left and right at the margin, top 392px, about 690px tall) showing the customer ID, the moment and its evidence rows. The top weight's bar is the slide's gold; every other bar is navy. A mono source line under the frame ("Illustrative customer and weights").
- Action: `title-statement` plus a checklist (56px squares with a check, `body` lines, 40px apart).
- Close: `title-cover` and one `body-lead` line at top ≈ 380px, lockup centred at the bottom. No arrow, no counter.

**Don't**
- Don't show a moment without its evidence rows, even on the cover or the close.
- Don't use real customer data or a real customer's name. IDs only, and say "illustrative".
- Don't explain the model with "AI". Name what it combines (the transfers, the income, outside savings rates) and that each weight is shown.
- Don't add a fourth layer or rename the three. Transaction, customer, market, in that order.

Reference: `assets/References/moment-explainer.jpg`.
