---
name: linkedin-caption-builder
description: Writes a Seekridge LinkedIn caption, for a carousel or a standalone post, built on one real, sourced finding (a win-loss stat, a competitor-monitoring finding, a case-study result or a positioning point of view) and following the carousel design system's caption rules. Use when the user wants LinkedIn copy and can point to, or accept, a specific finding as its angle.
---

# LinkedIn Caption Builder

## Purpose

A post with no real finding behind it is just an ad. This skill needs the same real angle as [`blog-post-builder`](../blog-post-builder), and writes it to the caption rules in [`../../knowledge-base/linkedin-carousels/captions.md`](../../knowledge-base/linkedin-carousels/captions.md), the same rules the carousels use, so a standalone post and a carousel caption read as one brand.

## Instructions

1. **Require a specific angle.** Use a real, sourced stat or finding from this repo's data ([`win-loss-analysis`](../../knowledge-base/win-loss-analysis), [`competitor-monitoring`](../../sales-tools/competitor-monitoring), [`sales-call-analysis`](../../knowledge-base/sales-call-analysis), a [`case-study-builder`](../case-study-builder) result) or one of [`positioning.md`](../../knowledge-base/positioning.md)'s points of view. If asked to "write a post about our product" with nothing to hook it to, ask for a finding, or suggest one from recent data.
2. **Read [`captions.md`](../../knowledge-base/linkedin-carousels/captions.md) and write its four blocks, 50–110 words in total:**
   1. Hook: a situation or a sourced fact, never a rhetorical question
   2. What changes, as a benefit: the feature named once
   3. Proof or detail: the figure with its source, or the method
   4. A plain-verb CTA with one link
3. **For a carousel caption,** read the slides first. The hook must add the fact or the stake to the cover, never repeat it, and an illustrative figure on a slide is called "illustrative" in the caption too.
4. **Keep the hook and block 2 inside the first ~210 characters** before "…see more", and the whole caption under 1,300 characters.
5. **Apply the caption rules exactly:**
   - no hashtags (tag people and organisations instead, with their agreement)
   - at most one emoji, never in the hook
   - no exclamation marks
   - one link, with UTM tags
   - "we" and "our" are fine
6. **Generalise competitive intelligence before it goes public.** This is the same rule as `blog-post-builder`. A competitor or named prospect account used freely internally (`competitive-landscape.md`, battlecards) is anonymised in public copy. Any draft that still names one is flagged for review before it posts.
7. **Every stat stays traceable to this repo's data,** with its sample and caveat. Short-form copy is exactly where "small sample" or "illustrative" gets cut for a punchier hook, and it never does.
8. **Run the "Before you post the caption" checklist** at the end of `captions.md`, then proofread against the [`branding-guideline`](../../knowledge-base/branding-guideline).

## What to avoid

- Don't open with "We're excited to announce" or "Introducing". The situation comes first and the product second.
- Don't end with an engagement-bait question in place of a CTA.
- Don't name a real competitor or prospect account without flagging it for review.

## Output format

```
## LinkedIn caption — [carousel name or "standalone"] — [starting finding, one line]

[Hook]

[What changes, as a benefit]

[Proof or detail]

[CTA]: [link with UTM tags]

---
Words: [n] · Characters: [n] (first ~210: hook + block 2)
Sourced from: [internal citation]
Competitor or account named: yes/no — [if yes, flagged for review]
Checklist (captions.md): passed / [what failed]
```
