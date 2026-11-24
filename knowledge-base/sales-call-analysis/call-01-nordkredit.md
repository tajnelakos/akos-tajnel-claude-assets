# Call Transcript — Nordkredit

**Date:** July 2026 · **Duration:** ~18 minutes · **Call type:** First discovery call, following outbound
**Rep:** Anna Kowalski (Seekridge) · **Prospect:** Lena Virtanen, Head of Credit Risk, Nordkredit (regional lender, Nordics, ~€600M annual origination)

*Context: Lena responded to an outbound email referencing her recent hire and Nordkredit's tooling migration (see [`personalized-outbound`](../../marketing-assets/personalized-outbound/example.md)).*

---

**Anna:** Lena, thanks for making time — I know you're still fairly new in the role, so I appreciate it. I'll keep this loose: I'd rather understand what you're actually dealing with than run you through slides. Sound okay?

**Lena:** That works. Honestly your email was the first one this month that didn't try to sell me something before asking a question, so — here we are.

**Anna:** Ha, good. So, high level — what pulled you into this migration? Was it something you inherited, or something you decided once you got in the seat?

**Lena:** Bit of both. Last year our lending team ran a refinancing campaign off a customer score from our current data provider — literally, it gives you a list of customers and a score, and that's it. We had an internal audit finding afterwards, nothing catastrophic, but the auditor's note was basically "you couldn't explain why three of these customers were contacted if asked." That report was sitting on my desk my first day, and now any model that decides who gets an offer comes through me.

**Anna:** That's about as clean a mandate as it gets. When you say "couldn't explain" — walk me through what happens today when someone does ask.

**Lena:** Our current provider — we use Estemate, have for years, mostly for property data — added a "portfolio insights" report a while back. It flags customers with a score and a short methodology PDF that's the same for every customer. It doesn't tell you which data points put *this specific customer* on the list, or how much each one counted. So if an auditor or our risk committee asks "why this customer," the honest answer is "the model said so," which is not an answer anyone wants to give twice.

**Anna:** Okay, that's useful, and it's exactly the gap we built around. Every moment we produce comes with the actual data points behind it — the property data, the market data, and the fields from your own CRM — and how much each one counted. Not a generic doc, the specific inputs for that specific customer. Would it help if I showed that live, on a sample of your own customers, rather than a canned demo?

**Lena:** Yes, actually — that would matter a lot more than slides. Can you genuinely do that with our real data, or does it need to be something already in your system somehow?

**Anna:** We'd need a pseudonymized extract of the customers you want to test, under a data-processing agreement, but yes — we can run it live and you can see the actual evidence trail it produces, not a mocked-up one.

**Lena:** Okay. I'll be honest, we also looked at ValuAI a few months back, before I started. I've heard from a colleague at another bank that ValuAI's sales team said something almost identical to what you just said.

**Anna:** That's a fair thing to bring up, and I'd rather you ask it directly than wonder. What did your colleague say happened?

**Lena:** She said when they pushed ValuAI in a follow-up technical call — not the first demo, the second one — the "explanation" turned out to be a chart of which feature categories mattered across the whole model, not the actual data points behind one customer. It looked good in the first meeting and then didn't hold up when their data team asked for specifics.

**Anna:** That matches what we've heard elsewhere too, for what it's worth — though I'd rather you verify it yourself than take our word for it, since obviously we have a horse in this race. What I'd suggest: when you evaluate us, do exactly what your colleague did with ValuAI — push past the first demo, ask us for a customer-level breakdown on records your own team picks, not ones we prepare. If we can't produce it, that tells you something. If we can, that also tells you something.

**Lena:** That's a reasonable way to structure it. Okay — separately, timeline. We have a board audit scheduled for Q3. I don't want to be mid-migration when that happens — that would be worse than not migrating at all.

**Anna:** Understood, and that's a real constraint, not a soft one. What's the actual date, if you know it?

**Lena:** Second week of September, tentatively.

**Anna:** Okay. Typical implementation for a bank your size is a few weeks, not months, assuming we're not waiting on your side for data access approvals — that's usually the longest pole. If we started in, say, early August, you'd have real runway before September, with buffer. I don't want to promise a date I can't back up, so let me confirm exact weeks with our implementation team rather than guess on this call.

**Lena:** Appreciate you not just saying "sure, no problem." One more thing — pricing. Your website says "custom," which usually means "we'll figure out how much you can pay."

**Anna:** Fair reaction, and no, that's not what it means here — it's a subscription that scales with the size of the customer base you want analysed, so I can actually give you a real range today rather than making you sit through two more calls to get a number. Given roughly what you described — €600M origination, and a mortgage book to match — you're likely in [a specific tier], which I can follow up with in writing so you have it in front of you rather than half-remembering a number from a call.

**Lena:** That's more than I expected to get today, honestly. Okay — what's the actual next step?

**Anna:** I'd suggest a technical validation call — bring whoever on your team would actually push on the evidence trail, and we run it live against customers your side selects. No slides. If that goes well, we can talk implementation timeline against your September date specifically.

**Lena:** That works. Let me check with our data lead on availability — I'll follow up this week.

**Anna:** Sounds good. I'll send the pricing tier detail in writing today so you have something concrete either way.

**Lena:** Appreciate it. Talk soon.

---

## Internal notes (rep-logged, not read aloud on the call)

- Strong, specific buying moment: real audit-finding trigger (a refinancing campaign nobody could explain), dated board deadline (Q3, tentatively second week of September).
- ValuAI explicitly in play, but via secondhand account, not confirmed head-to-head yet — worth revisiting if it resurfaces with more specifics.
- Estemate is the incumbent being displaced — confirms `competitive-landscape.md`'s Estemate entry (portfolio-level report, generic methodology doc, no customer-level detail).
- Next step: technical validation call with Nordkredit's data lead, live evidence trail on customers they select.
- Action: send pricing tier confirmation in writing today (open commitment made on the call — must follow through).
