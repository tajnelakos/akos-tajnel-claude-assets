# Timeline

Shows time in a customer's situation: the tension beat (*the rate ends, then they leave*), a policy's renewal window, a signal's journey from created to acted on.

**Anatomy**
- A 3px `rule` track: **solid for the past and now, dashed for expected** (the plan-drawing convention).
- Ticks at each event, 32px tall.
- Events under the track: ISO date in mono 24px `ink-muted` (with *(expected)* where it is), the event in Plex Sans 600 32px.
- The event the beat is about is **marked**: navy fill, Paper text, 2px corners. One marked event per timeline.

**Motion.** The solid track draws left to right (`draw`), events rise in as the line reaches them, the dashed part fades in, the marked event arrives last.

**Provide.** 2–4 events with dates, which is expected, which is marked.

**Avoid.** Calendar graphics, clock icons, countdowns, curved paths, more than four events.
