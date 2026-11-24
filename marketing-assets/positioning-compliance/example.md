# Sample output

A fictional draft going through the compliance checker — flags rather than fixes.

---

## Input

> In today's fast-changing banking landscape, financial institutions are increasingly turning to advanced technology solutions to find growth in their customer base. Our platform is powered by cutting-edge AI algorithms that deliver significantly more opportunities than traditional methods, helping users eliminate customer churn and transform their sales operations. Users receive a ranked list of opportunities within a short timeframe, backed by industry-leading accuracy.

## Output

```
## Compliance Check — Draft, untitled (signal platform intro paragraph)

**Result:** FAIL

### Hard fails (block publish)
- "cutting-edge AI algorithms" — violates: branding-guideline prohibited terms list ("cutting-edge," and this phrasing matches the explicitly banned "powered by advanced AI" / "powered by cutting-edge algorithms" pattern)
- "significantly more opportunities" — violates: branding-guideline style rule (numbers over adjectives) — no figure or comparison is given to support this, and none is traceable to positioning.md
- "helping users eliminate customer churn" — violates: positioning.md — this is a stronger claim than our positioning supports; the doc explicitly frames Parcelwise as showing which customers to talk to and why, not as eliminating churn
- "industry-leading accuracy" — violates: positioning.md "what this is not" — positioning deliberately avoids claiming to find more or better opportunities than every competitor; this is exactly the claim it warns against

### Soft flags (reviewer's call)
- "In today's fast-changing banking landscape..." — drifts from: branding-guideline style guidance to lead with the claim, not a scene-setting opener. Not a banned phrase outright, but reads as filler.
```
