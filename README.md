# Seekridge — Marketing AI Systems

> **Portfolio note:** Seekridge is a fictional company, modelled on my real product-marketing work in B2B AI and data SaaS. All companies, people, deals, and figures are made up — no real employer's data appears here. Full context in [`ABOUT-THIS-REPO.md`](./ABOUT-THIS-REPO.md).

This repo holds the prompts, Claude Skills, and custom GPTs behind Seekridge's product marketing operations — competitive intelligence, account-based marketing, sales enablement, win/loss analysis, brand voice, and deck building.

**Start here if you're an AI assistant:** [`INSTRUCTIONS.md`](./INSTRUCTIONS.md) routes any given task to the right folder below and maps typical day/week/month/quarter marketing work to this repo's structure.

## What this covers

Product marketing runs on recurring problems, not one-off projects: tracking competitors, turning sales call transcripts into insight, explaining why deals are won or lost, keeping brand voice consistent across a growing content library, getting the right message to the right account at the right time. This repo is the set of small, repeatable systems built around those problems — the actual prompts and skill definitions, not just a description of the workflow.

## About the company

Everything here is built around **[Seekridge](./knowledge-base/knowledge-base.md)**, an AI data analytics company built around customer moments. It reads a bank's own transaction and CRM data alongside market data to flag new business opportunities, and early churn, inside the customer base the bank already has. It sells to retail banks and mortgage lenders across Europe. [`knowledge-base/`](./knowledge-base) describes the company, its market, and its customers in full.

## Three kinds of folder

- **[`knowledge-base/`](./knowledge-base)** — accumulated understanding: the core reference docs (company, ICP, personas, positioning, voice, competitive landscape), plus the analysis work that builds and maintains that understanding (call analysis, win/loss analysis, outdated checker).
- **[`sales-tools/`](./sales-tools)** — what a rep or sales-facing process actually uses: competitor monitoring, battlecards, deck building.
- **[`marketing-assets/`](./marketing-assets)** — content marketing produces and ships: nurture sequences, case studies, one-pagers, blog posts, LinkedIn captions, and the product launch process.

### `knowledge-base/`

| File | Contents |
|---|---|
| [`knowledge-base.md`](./knowledge-base/knowledge-base.md) | Master summary — company, competitors, personas at a glance |
| [`icp.md`](./knowledge-base/icp.md) | Firmographics, tiering, buying committee, in-market moments |
| [`personas.md`](./knowledge-base/personas.md) | Per-persona buying psychology, objections, content preferences |
| [`positioning.md`](./knowledge-base/positioning.md) | Strategic narrative, differentiators, value props by segment |
| [`branding-guideline/`](./knowledge-base/branding-guideline) | Full brand system — mission, values, tone-by-channel, logo files, color palette, typography, naming conventions — plus the rewrite skill that applies the voice rules |
| [`design-system/`](./knowledge-base/design-system) | The brand made build-ready: light and dark tokens, component CSS with a [live components page](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/design-system/components.html), 15 icons, ridge-line motifs, and the rules for writing, LinkedIn carousels, and video. Also published as a Claude design system |
| [`linkedin-carousels/`](./knowledge-base/linkedin-carousels) | A full LinkedIn carousel design system on top of the brand: seven formats and a slide kit, tokens, slide CSS, outlined logos, motifs, bundled fonts, wording and caption rules, a [live gallery of every format](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/linkedin-carousels/gallery.html), and a skill that builds a finished carousel |
| [`flyer-design-system/`](./knowledge-base/flyer-design-system) | Seekridge in print: an A4 trifold, A5 postcard and A4 one-pager system with print-sized tokens, 12 components (moment evidence strip, layer diagram, contact block…), copy and pre-press rules, and three finished example pieces as print-ready PDFs. Also published as a Claude design system |
| [`video-design-system/`](./knowledge-base/video-design-system) | How Seekridge looks and moves on film: a film book (formats, beat structures, copy, motion grammar, markets, sound, specs), film tokens, 18 components with [live previews](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/video-design-system/preview.html), eight product UI reference screens, and three reference films rendered in code from it, plus the skill that builds new ones |
| [`competitive-landscape.md`](./knowledge-base/competitive-landscape.md) | Full battlecards and positioning gaps |
| [`sales-call-analysis/`](./knowledge-base/sales-call-analysis) | 15 call transcripts plus a [designed rollup](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/sales-call-analysis/call-analysis-summary.html) of objections, competitors, and new findings across them |
| [`win-loss-analysis/`](./knowledge-base/win-loss-analysis) | Patterns from closed-won/closed-lost deals — a quarterly infographic, plus a [100-record CRM deep dive](https://tajnelakos.github.io/akos-tajnel-claude-assets/knowledge-base/win-loss-analysis/win-loss-detailed-analysis.html) |
| [`outdated-checker/`](./knowledge-base/outdated-checker) | Flags specific knowledge-base claims that newer evidence contradicts |

### `sales-tools/`

| Folder | What it does | Formats |
|---|---|---|
| [`competitor-monitoring/`](./sales-tools/competitor-monitoring) | A structured weekly brief, plus a sourced, region-by-region [competitor analyses site](https://tajnelakos.github.io/akos-tajnel-claude-assets/sales-tools/competitor-monitoring/competitor-analyses.html) (DACH, Benelux, Nordics) | Claude Skill, Custom GPT |
| [`battlecard/`](./sales-tools/battlecard) | A designed, rep-facing HTML battlecard per tracked competitor | Claude Skill |
| [`sales-deck-builder/`](./sales-tools/sales-deck-builder) | Turns deal context into a persona-tailored outline, then designed slides from a Seekridge slide kit (HTML and PDF), with a reference deck for mortgage lenders | Claude Skill, Custom GPT, slide kit |

### `marketing-assets/`

| Folder | What it does | Formats |
|---|---|---|
| [`persona-email-sequence/`](./marketing-assets/persona-email-sequence) | Builds a persona-specific nurture sequence where each email advances a different decision criterion | Claude Skill |
| [`case-study-builder/`](./marketing-assets/case-study-builder) | Builds a Challenge/Solution/Results case study from a real closed-won deal's CRM record and call transcript — never an invented result or quote, plus a finished, customer-facing [Alpenkreis Bank case study](https://tajnelakos.github.io/akos-tajnel-claude-assets/marketing-assets/case-study-builder/case-study-alpenkreis-bank.html) and the [designed Nordkredit case study](https://tajnelakos.github.io/akos-tajnel-claude-assets/marketing-assets/case-study-builder/case-study-nordkredit.html) | Claude Skill |
| [`one-pager-builder/`](./marketing-assets/one-pager-builder) | Builds a single-page, persona-specific leave-behind — one angle, sourced proof points, an actual designed HTML page | Claude Skill |
| [`blog-post-builder/`](./marketing-assets/blog-post-builder) | Drafts a blog post built around one real, sourced point of view or finding, not a generic SEO topic | Claude Skill |
| [`linkedin-caption-builder/`](./marketing-assets/linkedin-caption-builder) | Writes a LinkedIn caption, for a carousel or a standalone post, around one real, cited finding, using the carousel design system's caption rules | Claude Skill |
| [`product-launch-process/`](./marketing-assets/product-launch-process) | The five-stage launch process (define, prove, enable, launch, learn) with demo readiness per market and KPIs set before launch, as an [illustrated page](https://tajnelakos.github.io/akos-tajnel-claude-assets/marketing-assets/product-launch-process/launch-process.html), plus a skill that turns a launch brief into a launch plan | Claude Skill |

Each folder contains a `README.md` explaining the problem it solves, the actual prompt/skill definition, and a sample output. Several of them share one fictional account, Nordkredit, so they read as one account history: [`sales-call-analysis`](./knowledge-base/sales-call-analysis) has its discovery call and [`case-study-builder`](./marketing-assets/case-study-builder) its closed-won ending.

## About the formats

- **Claude Skill** — a `SKILL.md` file following [Claude's skill format](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) (YAML frontmatter + instructions), the same structure used in production.
- **Custom GPT** — the system instructions block as configured in ChatGPT's GPT builder.

Some prompts are shown partially or with details generalized rather than as a finished, ready-to-run internal playbook — see [`ABOUT-THIS-REPO.md`](./ABOUT-THIS-REPO.md) for why.
