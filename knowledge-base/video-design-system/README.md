# Seekridge Video Design System

How Seekridge shows its moments in motion: product walkthroughs, persona films for retail, savings and cooperative banks, and statements for launches and events. Use it to brief a motion designer, to build a film in code, or to check a cut before it ships.

It sits on top of the brand. Identity, palette, type and voice come from [`../branding-guideline/brand-guidelines.md`](../branding-guideline/brand-guidelines.md); the build-ready web system is [`../design-system/`](../design-system). This folder adds what film needs and the brand file only covers in a paragraph: formats, beat structures, on-screen copy, frame layouts, a motion grammar, cast and sample data per market, sound, production specs and a component set, all drawn for the 1920 × 1080 master. [`../design-system/video-and-motion.md`](../design-system/video-and-motion.md) is the one-page summary of these rules.

**Decisions locked on 24 November 2026:** Meridian Gold is the only accent, one gold per frame · flat grounds only, Paper or Navy, no gradients, glows, blur or shadows · rounded corners and hairlines, as in the product (16px on panels, 10px on buttons and bands, pills for badges and tags; updated 25 November 2026) · every moment on screen carries its evidence · customers appear by ID, never by name · captions burnt into every cut · 16:9 is the master, 4:5 and 9:16 are cut from it · 30 fps · films are built in code from this system, never screen-recorded · no stock footage, no live action, no illustration of people.

**The idea in one line:** draw the ridge, then mark the point. Every beat starts from straight lines on a flat ground and ends with one thing marked in gold: the customer, the evidence, the figure, the action.

---

## Contents

0. [The first rule: situation, moment, evidence, action](#0-the-first-rule-situation-moment-evidence-action)
1. [Three formats, one language](#1-three-formats-one-language)
2. [Beat structures](#2-beat-structures)
3. [Copy](#3-copy)
4. [Visual foundations](#4-visual-foundations)
5. [Motion grammar](#5-motion-grammar)
6. [Markets, cast and sample data](#6-markets-cast-and-sample-data)
7. [Sound, voice-over and captions](#7-sound-voice-over-and-captions)
8. [Formats and aspect ratios](#8-formats-and-aspect-ratios)
9. [Template: Moment story (45–60 s)](#9-template-moment-story-4560-s)
10. [Production specs](#10-production-specs)
11. [Product interface reference](#11-product-interface-reference)
12. [Do and don't](#12-do-and-dont)
13. [Still open](#13-still-open)
14. [Files in this folder](#14-files-in-this-folder)

---

## 0. The first rule: situation, moment, evidence, action

Every film, script and beat sheet runs in this order. It is the brand promise (*opportunities you can act on — and explain*) turned into a running order, and it comes before every other section.

| Order | Question it answers | Example (Head of Retail Banking, DACH) | Share of a Moment story |
|---|---|---|---|
| **1. Situation** | What is happening to one customer the bank already has? | *Customer 40-1187 just started sending EUR 400 a month to another bank.* | Opens the film |
| **2. Moment** | What does Seekridge flag, and how high does it rank? | *Money starting to leave. Ranked 3rd of 212 this week.* | Short, and always named in the product's word: *moment* |
| **3. Evidence** | Which data points made the moment, and how much did each count? | *New transfer out 38%, income up 27%, savings-rate gap 21%, products held 14%.* | The body of the film. The beat that makes this brand different |
| **4. Action** | What does the banker do now, and where is it recorded? | *On the banker's list in the CRM, with the reasons. Logged.* | Closes the method, before the proof |

- **Never show a moment without its evidence.** A frame with a moment and no evidence trail is a frame the Head of Model Risk will stop the film on. If time is short, cut the action beat, never the evidence.
- **Never lead with the model.** "AI-powered propensity scoring" is a mechanism in the situation slot. Rewrite it as what is happening to the customer.
- **Evidence is data, not adjectives.** Each evidence row names its layer (transaction, customer, market) and the data point, in plain words. Evidence rows list the data points in plain words. Don't show weights or percentages. "Strong moments from multiple sources" is not evidence.
- **Walkthroughs** are feature-led by design, but open on the job (situation) before the first control: *A banker needs to know why a customer was flagged.*
- **Check it first:** read the voice-over aloud. If a viewer would learn what Seekridge *is* before they see one customer's situation, the order is wrong. If they could repeat the moment but not one reason behind it, the evidence beat is too thin.

---

## 1. Three formats, one language

Every film shares the same type, grounds, panels and motion grammar. What changes is the job, the ground and how much of the product is on screen.

| | **Walkthrough** | **Moment story** | **Statement** |
|---|---|---|---|
| Job | Show how one feature works | Show what one moment does for one persona, end to end | Announce, open an event, state one finding |
| Emphasis | Product-heavy | Customer situation and evidence | One idea and one figure |
| Reference film | `walkthrough-evidence-trail-16x9` | `story-outflow-dach-16x9`; segment version `segment-retail-lending-16x9` | `statement-evidence-16x9` |
| Length | 20–45 s | 45–60 s | 20–35 s |
| Ground | Paper, map grid on | Navy open and close, Paper body | Navy throughout |
| Framing | One panel, cropped to the control the beat is about | Split beats: headline left (5 columns), panel right (7 columns) | Type, the dot map and figures; at most one panel |
| Headline | `headline-compact`, no full stop | `headline`, full stop | `title`, full stop |
| Navigation aid | Step counter in the eyebrow (`STEP 2 / 5`) | ChapterRail: Situation · Moment · Evidence · Action | None |
| Opens on | The first headline, straight on Paper | TitleCard: the situation as the hook | The dot map moving in, then the statement |
| Closes on | Two-line lockup on Paper, mark only | EndCard: lockup, the line, one action | EndCard |
| Where it lives | Help centre, in-app onboarding, feature pages, sales follow-ups | Segment and persona pages, sales follow-ups, LinkedIn, event screens | Launch posts, conference openers, the top of a sales deck |

**Choosing:** if the viewer already has Seekridge and needs to *use* a feature, make a Walkthrough. If the viewer needs to *trust a moment enough to act on it*, make a Moment story. If the viewer needs to *notice one finding*, make a Statement.

**One persona per film.** A Moment story is made for one of the four personas in [`../personas.md`](../personas.md) (Head of Retail Banking, Head of Model Risk, Head of Deposits & Savings, Relationship Manager Lead) and one segment. Never one film for everybody.

---

## 2. Beat structures

A beat is one headline plus one change on screen. Default length 5 s (`beat`), range 3–8 s. Evidence beats run longest because they are the reading.

### Walkthrough (5–8 beats)

1. **Frame the job** in the user's words. *An advisor needs to know why.*
2. **3–5 action beats**, one control each, in the order a user would do them. *Open the moment. Every data point is listed. Every reason in plain words. Sort by layer. Export the trail.*
3. **Reassure** where governance matters. *Every view is in the audit log*
4. **Lockup**, two lines, Paper ground, the mark bottom-right. *Every moment. / Its reasons, on screen.*

### Moment story (9–12 beats, follows Situation → Moment → Evidence → Action)

1. **TitleCard**, Navy, 0–5 s. The situation as a one-line hook over the dot map rising. *They just started sending money to another bank.*
2. **Tension**, 1 beat. What happens today without the moment, on a Timeline. *By the time anyone notices, the savings have gone.*
3. **Situation into data**, 1 beat. The LayerStack builds: transaction, customer, market. *Three layers, one customer.*
4. **Moment**, 1 beat. The MomentCard lands with the rank. *One moment, ranked third this week.*
5. **Evidence**, 2–3 beats. The EvidenceTrail populates; FocusMarks close on the lead row, marked gold. *Here's why it ranks third. / The new transfer comes first.*
6. **Action**, 1–2 beats. The moment arrives in the CRM; the AuditLog writes the line. *On the banker's list, with the reasons. / And on the record.*
7. **Scale**, optional, 1 beat. RidgeField: the whole customer base as a moving dot map, the week's moments rising as peaks. *212 customers to call this week. Not 40,000.*
8. **Proof**, 1 beat, Navy. FigureCard with its source line. *68% moved money out within six months.*
9. **EndCard**, Navy. Lockup, the line, one action, 3 s hold.

### Segment story (45–60 s, a Moment story for a whole segment page)

A product or segment page (retail banking, deposits and savings, retail lending) gets one Moment story built around **two customers with two different moments**, so the page shows range without becoming a feature tour.

1. **TitleCard**: the customer base in the reader's own word (*customers*, *savers*, *members*). *Your customers' transactions already hold next quarter's business.*
2. **Customer one**: situation → moment → evidence (2 rows only) → action.
3. **Customer two**, a different moment type: same order, faster (the viewer has learned the grammar).
4. **Governance beat**: AuditLog plus one line for risk and compliance. *Every moment, explained and logged.*
5. **Scale**: RidgeField.
6. **Proof** and **EndCard**.

**Short cut (35–45 s), value → benefit → feature.** When the page needs a punchier film, drop the governance and proof beats and run: the customer base as a RidgeField with its moments rising and tagged → the three layers (*your transactions, your customers, the market*) → customer one with the evidence trail → customers two and three, faster, each with the offer the moment opens → the week's moments settling into a ranked CRM queue → a closing title that turns the opening hook into the action (EndCard, *Closing claim* variant). No ChapterRail. Headlines are bolder here: short, declarative, a claim per scene. Reference: [`assets/Films/segment-retail-lending-16x9.mp4`](./assets/Films/segment-retail-lending-16x9.mp4) (50.2 s, silent with captions until the voice is re-recorded), with its ElevenLabs-ready voice-over script beside it.

### Statement (5–7 beats)

1. **RidgeField** draws in on Navy, no words for 1.5 s.
2. **The claim** as a `title`, up to three words in gold-light. *Most moments can't explain themselves.*
3. **The turn**. *Ours show their evidence.*
4. **One figure** with its source. *68% of flagged customers moved money out within six months.*
5. **SegmentTriptych**: the same evidence grammar for main-bank, outflow and growth moments (optional).
6. **EndCard**.

---

## 3. Copy

Headlines carry the film. Write them first, read them aloud, then design. Voice rules are the brand's ([`../branding-guideline/skill.md`](../branding-guideline/skill.md)); these are the film-specific ones.

| Rule | Do | Don't |
|---|---|---|
| Length | 3–8 words a line, max two lines | A sentence that needs a comma to breathe |
| Case | Sentence case. Feature names keep capitals (Evidence Trail, Coverage Map) | Title Case Headlines; all caps outside the mono eyebrow |
| Highlight | Up to three words, the payoff, usually at the end. Gold-light text on Navy; a gold underline bar on Paper | Highlighting a verb mid-line, more than half a line, or two highlights in one frame |
| Two-liners | Situation in ink, consequence or answer highlighted. *Their salary went up in March. / **So did their transfers out.*** | Two lines of equal weight |
| Punctuation | Moment stories and Statements end in a full stop. Walkthroughs don't | Exclamation marks, question marks as hooks ("Ready to grow?"), ellipses |
| Voice | Second person to the professional (*your customers*, *your bankers*). Customers by ID on screen, *this customer* in the voice-over | *Users*, *leads*, *prospects*. Customer first names |
| Precision | Name the data point. *Income up 16% in three months.* | *Rich customer insights.* *Powerful data.* |
| Mechanism | Name it when the persona asks for it (Head of Model Risk films), always as plain data points | *Proprietary AI*, *black box*, *magic*, *revolutionary* (all prohibited terms) |
| Product words | Moment · evidence trail · audit log · customer base · transaction data, customer data, market data · CRM | Lead, insight, alert · explainability report · database · data lake |
| Figures | One figure per beat, with what it measures and where it came from. Illustrative figures labelled *Illustrative* on screen | A figure without a source line; demo data presented as a result |
| Currency | Code before the number: EUR 412,500 · CHF 1.2m · SEK 3.4m | € 412.5k; mixing formats in one film |
| Spelling | UK English (Oxford) for international films | Mixing US and UK spelling |
| Economy | Cut a clause the picture already says | *…as you can see on the screen.* |
| Calm | Let the evidence do the persuading | Urgency (*Don't miss out*, *before it's too late*) |

**Highlight pattern library**

- **Consequence:** Their salary went up in March. **So did their transfers out.**
- **Reason:** Ranked third. **Here's why.**
- **Evidence:** The new transfer counts **most.**
- **Record:** On the advisor's list. **With the reasons.**
- **Scale:** 212 customers to call. Not 40,000. (No highlight: the RidgeField's gold point is the frame's gold.)
- **Contrast:** Most moments can't explain themselves. **Ours show their evidence.**
- **Governance:** Every moment, **explained and logged.**
- **Lockup:** Every moment. / **Its reasons, on screen.**

**Per persona, what the hook names**

| Persona | Hook names | Evidence beat leads with | Action beat shows |
|---|---|---|---|
| Head of Retail Banking | A customer banking mainly elsewhere, or ready for a mortgage | The salary and card-spend rows | The banker's CRM list |
| Head of Model Risk | A decision someone will have to defend | Every data point in plain words, the method line | The audit log and export |
| Head of Deposits & Savings | A saver starting to move money out | The transfer-out and savings-rate rows | The savings team's call list |
| Relationship Manager Lead | A member worth a call this week | The change that triggered it (income, transfers) | The banker's weekly list |

---

## 4. Visual foundations

### Grounds

- **Paper** (`#F4F3EF`) for everything with product on it. Never white: panels are white so they read against it.
- **Navy** (`#1A3A5C`) for title cards, statements, figures and end cards.
- **Flat, always.** No gradients, glows, vignettes, blur, grain or depth of field. Depth comes from crop and dimming, never from light.
- **Map grid** (optional, Walkthroughs only): 1px `grid` hairlines every 96px on Paper. It is the drafting table the panel sits on. Never behind running text.
- **Changing ground** happens by a straight vertical wipe (`wipe`) or a cut, never a dissolve between grounds.

### Layout (1920 × 1080 master)

- 12 columns of 122px with 24px gutters inside a 96px margin.
- **Left-aligned, always.** Headlines sit at the left margin, eyebrow above, the panel to the right. The only centred frames are the EndCard and the Walkthrough lockup.
- **Split beat:** text block across columns 1–5, panel across columns 6–12. The panel may run off the right margin when the camera has pushed in, never off the top or bottom.
- **Full beat:** one panel across columns 2–11, headline above it at `headline-compact`.
- Eyebrow top at `headline-top` (144px); headline under it; one optional lead line under that.
- **Bottom zone:** the caption band's bottom edge sits at `caption-bottom` (160px above the frame bottom). The ChapterRail sits under it, baseline at `rail-bottom` (72px). Keep panels clear of the lowest 260px while a caption is on screen.
- **Logo:** the lockup top-left inside the margin on TitleCards; the reversed lockup centred on EndCards; the mark at 48px bottom-right on Paper frames; nothing on Navy statement frames between the title and the end.

### Type

- **Archivo** for anything on the ground: titles 800, headlines 700, figures 800.
- **IBM Plex Sans** for panels, captions and lower thirds: values 500, titles 600.
- **IBM Plex Mono** for every eyebrow, ID, date, source line and the ChapterRail. If it is data, it is mono.
- Headlines track tight (−0.025em); mono eyebrows track open (+0.08em) and are the only all-caps.
- The smallest size a viewer must read is `panel-value` (26px). Anything smaller (column labels at 18px) is texture: it can be in shot but must never carry the message.

### The highlight

There is one gold per frame. It marks the thing the beat is about:

| Ground | Highlighted words | Elsewhere in the frame |
|---|---|---|
| Navy | Text in gold-light `#D9A54B` (5.2:1) | Nothing else gold |
| Paper | Words stay ink; a 6px gold bar draws under them | Nothing else gold, so the top evidence bar goes navy until the headline highlight has left |

When a beat's point is a data point rather than a phrase, the gold moves into the panel instead: the gold edge on the lead evidence row, the gold point in the RidgeField, the bar in the chart. Then the headline carries no highlight.

### Product UI in film

- **Recreate, don't record.** Every panel is a cleaned rebuild of a real Seekridge screen (section 11), drawn in code from these tokens.
- **Flat panels.** White surface, 1px `panel-line` border, 16px corners (`radius`), no shadow. The border traces in before the content appears.
- **Crop to the component.** A panel fills 50–60% of the frame width in split beats, up to 85% in full beats. Never a whole app window with its navigation.
- **Film density.** Rows are 72px, values 26px: twice the web app's size. Keep 4–6 rows per panel.
- **Simplify.** One primary action visible at most, in navy, 10px corners (`radius-control`). Remove nav, avatars, filters and secondary buttons that don't move the story.
- **Evidence is always visible.** A MomentCard on screen shows at least its top two evidence rows. The full trail is its own beat.
- **Status colours only inside panels**, with their ink and background pairs: *Synced to CRM* in good-ink on good-bg. Never on the ground, never for drama.
- **Cursor** only when a click is the point (exporting the trail, opening the moment). One straight eased move, one click, no ripple.
- **Focus by FocusMarks and dimming.** Four corner brackets close on the element; everything else in the panel dims to 35%. No blur, no zoom bubble, no glow.

### The three layers, without colour coding

The brand palette has no categorical hues, so films never colour-code the data layers. A layer is shown by its **mono label and line icon**, always in this order:

| Layer | Label | Icon | Typical evidence rows |
|---|---|---|---|
| Transaction data | `TRANSACTIONS` | `icon-transaction` | Salary and income change, transfers out, card spend at other banks, saving habit, bills paid from elsewhere |
| Customer data | `CUSTOMER` | `icon-customer` | Products held, tenure, contact history, questions to the bank's AI agent (`icon-agent`) |
| Market data | `MARKET` | `icon-market` | What other banks pay on savings, rate changes, local wage and price trends |

Evidence rows list the data points in plain words. Don't show weights or percentages. The lead row gets a gold edge (`.is-lead`); the other rows stay ink on Paper.

### Drawings

- The **ridge field** is the only illustration: a dot map of the client base that is always gently moving, where only a few areas rise into peaks (the moments) and one summit is marked with a gold point, as in the logomark. Dots are Paper on Navy and Navy on Paper, brightest at the peaks.
- **Plan drawings** for concepts with no screen (money flowing between two accounts, a month of payments, a customer base as a field): 3px strokes, square ends, straight lines and right angles only. Dashed means *expected* (a projected balance, a likely transfer); solid means *now*.
- Icons are the 16 line icons in [`../design-system/`](../design-system), scaled to 48px with the stroke at 2.5px.
- **No people.** No illustrated advisors, hands, phones held in hands, faces, offices or city skylines. The customer is an ID and a point.

---

## 5. Motion grammar

Motion is calm and continuous: the dot map always moves gently, everything else is exact, no bounce. Everything moves on one curve, `cubic-bezier(0.2, 0, 0, 1)`. Nothing spins, flips, pops, blurs, glows or slides in from off-screen.

| Move | How | Token |
|---|---|---|
| Line in | Each headline line rises 24px out of a mask on its own baseline; lines, not words | `line-in`, `line-stagger` |
| Highlight | On Paper, the gold bar draws under the highlighted words left to right as their line lands; on Navy, the gold words simply arrive with their line | `highlight-in` |
| Draw | Plan drawings, chart lines and the timeline track draw their stroke, consecutive lines staggered | `draw`, `draw-stagger` |
| Point fill | After its lines, the one gold point fills from the bottom edge up: the signature move | `lot-fill` |
| Frame trace | A panel's hairline border traces clockwise from the top-left; then its content fades in | `frame-trace`, `content-in` |
| Populate | Rows appear top to bottom, each fading in and settling 8px | `row-stagger` |
| Count | Figures count up and land on the exact value, tabular numerals so nothing jitters | `count` |
| Focus | FocusMarks close in from 40px outside the element; the rest of the panel dims | `focus-in`, `dim` |
| Type | A mono log line types in, character by character, then its status badge appears | `type` |
| Mark | A point in the RidgeField fills gold, or a row gets the gold bar: the moment a thing is chosen | `lot-fill` |
| Wipe | Ground changes Paper ↔ Navy as a hard vertical edge moving left to right | `wipe` |
| Camera | One straight move per beat at most: a push-in to `drift` (1.03) on a panel, linear. Never on type-only frames | `drift` |
| Out | A beat's content fades out; the ground stays; the next beat draws in on it | `fade-out` |
| Hold | The finished frame stays still long enough to read | `hold` |

**Cadence.** Something resolves every 2–3 seconds in evidence beats (a row lands, a bar grows, the marks close), timed to the voice-over sentence it illustrates. Title and end cards are allowed to be still.

**Reading-time rule:** a beat lasts at least `words × 0.3 s + 1.5 s` after its last line lands. A 7-word headline needs 3.6 s.

**Reduced motion** (web embeds): replace every draw, rise and count with a 250ms fade; keep the order.

---

## 6. Markets, cast and sample data

The market is chosen per film and sets language, number format, currency, voice and sample data at once. Core markets: DACH, Benelux, Nordics; UK English for international masters.

| | **International (UK English)** | **DACH** | **Benelux** | **Nordics** |
|---|---|---|---|---|
| On-screen language | UK English | German (*Sie*); Swiss films: no ß, «…» | Dutch (*u*); French for Wallonia | Swedish, Danish or Norwegian (*du*) |
| Voice-over | Neutral UK English | Hochdeutsch (Swiss Standard German for CH) | Netherlands Dutch; Belgian French | One language per film |
| Demo bank | Northmere Bank | Alpenkreis Bank | Havenstad Bank | Fjordvik Sparebank |
| Demo savings bank | Ashcombe Mutual | Lindwurm Sparkasse | Dijkhuis Spaarbank | Ørsund Sparekasse |
| Demo credit union | Kestrel Credit Union | Brandauer Raiffeisen | Kade Coöperatieve Bank | Strand Andelsbank |
| Customer IDs | 40-1187, 40-2210, 52-0093 | same format | same format | same format |
| Monthly transfer | EUR 400 | EUR 400 (CH: CHF 400) | EUR 400 | SEK 4 500 |
| Balance | EUR 48,200 | EUR 48.200 (CH: CHF 48’200) | EUR 48.200 | SEK 482 000 |
| Percentages | +11.2% | +11,2 % | +11,2% | +11,2 % |
| Dates (on screen) | 31 March 2027 | 31. März 2027 | 31 maart 2027 | 31 mars 2027 |
| Dates (in panels and logs) | 2027-03-31 | 2027-03-31 | 2027-03-31 | 2027-03-31 |

- **All brands and customers are fictional** and labelled *Demo* in the panel header. No real customer, bank or address ever appears, not even a street name.
- **Customers are IDs.** In the voice-over: *this customer*, *one customer*, *a saver*. Never a first name, never an age, never a photo.
- **Bankers** are roles (*your banker*, *the Hamburg branch team*), never people.
- **Moment names** are the product's own (section 11): Salary landing elsewhere, Salary just switched in, Money starting to leave, Balance drifting down, Card going quiet, Income rising, Investing elsewhere, Mortgage-ready, Car purchase goal, Family growing, Renovating, New customer not yet active.

---

## 7. Sound, voice-over and captions

A Seekridge film must work fully muted: most are watched that way in a feed or on a stand screen. Sound adds calm, never energy.

**Voice-over**

| Rule | Detail |
|---|---|
| Role | The voice-over tells the customer's situation and reads the evidence in plain words; the headline names the point. They agree in meaning, never word for word |
| Pace | Calm: about 2.4 words a second in English (2.1 in German and Dutch, 2.3 in the Nordic languages), with pauses. A 50-second Moment story holds 95–110 English words |
| Shape | Short declarative sentences, one or two a beat, landing on the change they describe. 0.3 s between sentences, 0.5 s before the evidence and before the figure |
| Silence | No speech over the first 1.5 s of the TitleCard or the last 2 s of the EndCard |
| Voice | One approved voice per language, the same in every film, so Seekridge always sounds like one person: a measured, precise peer. No announcer lift, no sales energy, no smile in the voice on figures |
| Engine | Synthetic voice allowed (one licensed voice per language); a recorded read for flagship films. Generate the voice first, measure every sentence, then time scenes and captions from those measurements |
| Persona | Address the professional (*your customers*, *your advisors*), never the customer |

**Mix**

| Layer | Level |
|---|---|
| Voice-over | Leads; full mix at −16 LUFS integrated, −1 dBTP true peak |
| Music | Optional. Sparse and even (piano, soft pulse), ducked 10–12 dB under the voice, no build-ups, no drops |
| Sound design | One soft tick when the gold point fills or a point is marked. Nothing on cuts, wipes or row reveals. No whooshes |

**Captions, always.** Every cut of every film carries burnt-in captions of the voice-over, or of the on-screen story where there is no voice-over.

| Rule | Detail |
|---|---|
| Style | `caption` type (IBM Plex Sans 500, 44px at 1080p) in `caption-ink` on the `caption-band`, 10px corners, 32px horizontal padding. On Paper frames the band is navy with Paper text; on Navy frames it inverts to a Paper band with ink text, so it never disappears into the ground |
| Position | Bottom centre, text centred, band bottom edge at `caption-bottom`; above the ChapterRail. Keep panels and headlines out of the band's area (about 780–920px down the frame) while a caption is on |
| Length | Max 2 lines, max 42 characters a line; break at a phrase, never inside an ID, a figure or a currency amount |
| Timing | Matches the spoken line; on screen 1.2 s minimum, 6 s maximum; fades in and out over 150ms, no movement |
| Silence | No caption over the TitleCard's first 1.5 s or the last 2 s of the EndCard |
| Sidecar | An `.srt` with the same text ships with every render |
| No voice-over | Where a film runs silent, captions carry what the picture doesn't say (the situation, the reason), never a transcript of the headlines |
| Overlap | A caption never repeats the headline word for word; if the voice-over restates the headline, rewrite the voice-over |
| Language | Same language as the voice-over; German and Dutch run longer, so re-time the beat rather than shrink the type |

---

## 8. Formats and aspect ratios

| Ratio | Size | Length | Use | Adaptation |
|---|---|---|---|---|
| **16:9 (master)** | 1920 × 1080 | 45–60 s story, 20–45 s walkthrough | Website, sales follow-ups, events, YouTube | As designed |
| 4:5 | 1080 × 1350 | 30–45 s | LinkedIn feed | Split beats stack: headline top (rows 1–3), panel under it at full width; captions keep 160px from the bottom; ChapterRail dropped, chapter named in the eyebrow |
| 9:16 | 1080 × 1920 | 15–30 s | Stories, event screens | Headline in the top third, panel in the middle third, bottom 280px clear for platform UI; one evidence beat only |

Design and time the 16:9 master first; cut the others from the same beats and voice-over. The 4:5 cut drops the scale beat; the 9:16 cut also drops tension and keeps situation → moment → evidence → end card.

---

## 9. Template: Moment story (45–60 s)

The default persona film. Reference: [`assets/Films/story-outflow-dach-16x9.mp4`](./assets/Films/story-outflow-dach-16x9.mp4) (Head of Deposits & Savings, DACH savings bank, 48 s, UK English master); the full brief → beat sheet → voice-over → captions run is [`example.md`](./example.md).

| Time | Beat | Headline | On screen | Chapter |
|---|---|---|---|---|
| 0.0–5.0 s | TitleCard | Their savings just started to leave. | Navy; the dot map moves in from the right, peaks rise, the gold point lands; lockup top-left; hook as `title` | — |
| 5.0–10.0 s | Tension | By the time anyone notices, **it's gone.** | Wipe to Paper; Timeline: First transfer out 2026-06-02 → Today → Balance moved elsewhere (dashed, marked) | Situation |
| 10.0–16.0 s | Layers | Three layers. **One customer.** | LayerStack: transaction, customer, market rows draw in and resolve into one line | Situation |
| 16.0–21.5 s | Moment | One moment, **ranked third.** | MomentCard: Money starting to leave · Customer 40-1187 · Rank 3 of 212 | Moment |
| 21.5–31.0 s | Evidence | Here's why it **ranks third.** | EvidenceTrail: four rows with layer, data point and value; FocusMarks close on the lead row; gold edge on it | Evidence |
| 31.0–37.0 s | Action | On the banker's list. **With the reasons.** | CRM panel: task row lands with *Synced to CRM*; AuditLog line types in | Action |
| 37.0–42.0 s | Proof | (the figure is the headline) | Wipe to Navy; FigureCard counts to 68%; source line: *Backtest, demo bank's 2025 data. Illustrative.* | — |
| 42.0–48.0 s | EndCard | Opportunities you can act on — and explain. | Reversed lockup centred, the line, the action *Run a backtest on your own data*; 3 s hold, silent last 2 s | — |

A 30-second cut drops the layers beat and shortens the evidence to two rows.

**Moment lines by family (starting point, refine per page)**

| Family | Situation | Moment | Top evidence rows | Action |
|---|---|---|---|---|
| Main bank | Salary paid in at another bank for two years | Salary landing elsewhere | Salary payer · card spend at another bank · bills paid from elsewhere | Main-bank conversation and a salary-switch offer |
| Outflow | A new monthly transfer to an outside savings account | Money starting to leave | Transfer out · savings-rate gap · balance trend | Savings call before the habit settles |
| Growth | Income up, money starting to go to an investment app | Investing elsewhere | Income change · transfers to a broker · products held | The bank's own investment conversation |
| Growth | Income up, savings building, questions to the AI agent about borrowing | Mortgage-ready | Income trend · savings towards a deposit · AI-agent questions · rate change | Mortgage advisor call |
| Growth | Savings pot growing towards a round target, questions to the AI agent about car financing | Car purchase goal | Savings towards a target · car loan elsewhere ending · AI-agent questions | Car loan offer before the dealer's finance |
| Growth | Child benefit arriving, new children's spend, the customer mentions parental leave to the AI agent | Family growing | Child benefit in · childcare fees · children's spend · AI-agent questions | One ranked next step: mortgage for a bigger home, car loan or renovation loan |
| Growth | Builder and DIY payments, money set aside in savings, energy prices rising | Renovating | Builder payments · savings set aside · energy prices | Green loan or renovation loan, timed to the work |
| New customer | Account opened six weeks ago, salary not switched | New customer not yet active | No salary in · card unused · no bills set up | Onboarding call from the branch |

Moments are always shown as the result of named data, and the voice-over leads with the customer's situation, never the detection method.

---

## 10. Production specs

| | Master | Web |
|---|---|---|
| Size | 1920 × 1080 (16:9); 1080 × 1350 and 1080 × 1920 cut from it | 1280 × 720 |
| Frame rate | 30 fps | 30 fps |
| Video | H.264 MP4, CRF 18, yuv420p | H.264 MP4, ≤ 4 MB per 30 s where possible |
| Audio | AAC 48 kHz stereo, −16 LUFS, −1 dBTP | same |
| Captions | Burnt in on every version, plus a `.srt` sidecar | same |
| Build | Scenes built in HTML and CSS from `tokens.css` and `components/bundle.css`, driven frame by frame by `components/film-engine.js`, captured headless, one MP4 per scene, joined with ffmpeg's concat demuxer without re-encoding; sound added last with `-c:v copy` | — |
| Check | A contact sheet of the busiest frame of every scene, taken before its fade-out, at full size, before the full render | — |
| File name | `<format>-<topic>-<market>-<ratio>.mp4`, e.g. `story-outflow-dach-16x9.mp4` | `…-web.mp4` |

How to build one is in [`skill.md`](./skill.md); the reference films' sources are in [`films/`](./films).

---

## 11. Product interface reference

The Seekridge web app, screen by screen, and what each gives a film. The screens are in [`assets/Product UI/`](./assets/Product%20UI) (recreated November 2026, demo data). Rebuild from them; never screen-record.

| Area | Screen | What it proves | Film use |
|---|---|---|---|
| Moments | 01 Moments this week | Moments ranked for one bank's customer base, with moment type, customer ID, rank and top reason | Moment beat; scale beat |
| Moments | 02 Moment detail | One moment with its full evidence trail: layer, data point and value in plain words (no weights) | MomentCard, EvidenceTrail |
| Customer | 03 Customer record | The three layers for one customer side by side | LayerStack |
| Coverage | 04 Coverage Map | Where in the customer base moments cluster, by branch region | RidgeField, Statement |
| Action | 05 CRM sync | Which moments went to which team's CRM queue, and when | Action beat |
| Governance | 06 Audit log | Every view, export and action on a moment, timestamped | AuditLog |
| Proof | 07 Backtest report | How past moments performed on the client's own data, with method and period | FigureCard, BacktestChart |
| Setup | 08 Data layers | Which transaction, customer, AI-agent and market sources are connected, and how fresh each is | Walkthrough openers, governance beats |

**Product vocabulary on screen and in the voice-over:** moment · evidence trail (Evidence Trail as the feature name) · data point · audit log · customer base · transaction data, customer data, market data · main bank · Coverage Map · backtest · CRM sync · rank.

**Numbers.** The product shows demo data. In an external film every figure is either from an approved client case, with its source on screen, or labelled *Illustrative*. Backtest figures always carry the period and the data they ran on.

---

## 12. Do and don't

| Do | Don't |
|---|---|
| One customer, one moment, one point per beat | Two panels changing at once |
| Show the evidence trail every time a moment is on screen | A moment badge with nothing behind it |
| Draw lines, then fill the one gold point | Gold on more than one thing in a frame |
| Keep grounds flat, panels white and hairlined | Gradients, glows, blur, drop shadows, glassy cards |
| Rounded corners from the scale: 16px panels, 10px controls and bands, 6px chips, pills for badges and tags | Sharp 0px panels, mixed radii in one panel, bubbly shapes beyond the scale |
| Left-align headlines at the margin | Centred headlines over centred cards (except end cards) |
| Dim to focus | Blur to focus |
| Mono for every ID, date and source | Data in the display face |
| Customers as IDs, advisors as roles | Names, faces, illustrated people, hands holding phones |
| Label illustrative figures on screen, with a source line | Demo figures presented as results |
| Cut a beat to fit; keep the evidence | Speeding up the evidence beat to fit a slot |
| Check six full-size stills in a contact sheet before the full render | Rendering blind, or checking frames mid-transition |
| Let the end card breathe for 3 s, silent for the last 2 | Cutting the moment the action appears |
| Straight wipes and cuts | Spins, 3D flips, zoom bursts, glitch, particle fields, stock footage |

---

## 13. Still open

1. **Approved voices.** Choose and record the one synthetic voice per language (EN-GB, DE, NL, SV) and its licence, so every film uses the same voice. The final English voice will come from ElevenLabs. Until then, `segment-retail-lending-16x9` carries a draft voice made offline with Kokoro (voice *bf_emma*), and the other reference films ship silent with captions.
2. **Music.** No bed is cleared yet. Films ship voice-only (or silent) until one is licensed for commercial use.
3. **Logo files.** The wordmark is live text in the SVGs; films embed Archivo so it renders, but outlined logo files are the next step (see [`../branding-guideline/README.md`](../branding-guideline/README.md)).
4. **Localised references.** Only the UK English master of the reference films exists. A German cut of `story-outflow-dach` is the next one to build, to test the re-timing rule.

---

## 14. Files in this folder

| Path | What it holds |
|---|---|
| `README.md` | This book |
| [`tokens.json`](./tokens.json) | Every film token (colour by ground, type, layout, motion) with a usage note |
| [`tokens.css`](./tokens.css) | The same as CSS custom properties (`--pwv-*`) and ground themes, with `@font-face` rules for the bundled fonts. Generated from `tokens.json` |
| [`fonts/`](./fonts) | Archivo, IBM Plex Sans and IBM Plex Mono as WOFF2 (SIL Open Font License), the same files the carousel and flyer systems bundle, so films render offline |
| [`manifest.json`](./manifest.json) | Component and asset index, in the shape a Claude design system reads |
| [`components/`](./components) | `bundle.css` (all component styles), `film-engine.js` (frame-exact timeline), and one folder per component with a `README.md` and a live `preview.html` |
| [`preview.html`](./preview.html) | Every component on one page, playing, with Paper and Navy grounds |
| [`films/`](./films) | The HTML sources of the three reference films and the render script |
| [`assets/Films/`](./assets/Films) | The rendered reference films (MP4) and their caption sidecars (SRT) |
| [`assets/Stills/`](./assets/Stills) | One reference frame per pattern, and the contact sheet |
| [`assets/Product UI/`](./assets/Product%20UI) | The eight Seekridge screens films rebuild from |
| [`assets/Logos/`](./assets/Logos) | The lockup, reversed lockup and mark used in films |
| [`skill.md`](./skill.md) | The Claude skill that writes a beat sheet and builds a film from this system |
| [`example.md`](./example.md) | A worked brief → beat sheet → voice-over → captions → render, for the reference Moment story |
