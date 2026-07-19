---
headline: "MiniMax M3 Tops the Open-Weight Leaderboard as the Gap to Closed Models Narrows"
slug: minimax-m3-open-weight-leader
category: llms-genai
story_number: "07"
date: 2026-07-18
---

# MiniMax M3 Tops the Open-Weight Leaderboard as the Gap to Closed Models Narrows

For most of this decade, the answer to "what is the best model you can actually download?" came with an apology attached. As of mid-July 2026, it comes with a leaderboard citation instead. MiniMax M3 sits at the top of BenchLM's open-weight ranking with an overall score of roughly 69.8, and on the benchmark that buyers argue about most — hard, agentic coding — the distance between the best open model and the best closed one has quietly compressed from "several generations" to single digits.

That reframing is the story. It is bigger than any one release, and MiniMax M3 is its clearest exhibit.

## What M3 is, and where it stands

MiniMax M3 shipped on May 31, 2026 as an open-weight model with a 1-million-token context window. Its defining design choice is what it leaves out: M3 answers without an explicit chain-of-thought reasoning pass, trading visible deliberation for faster responses and lower token consumption — a deliberately different bet from the "maximum thinking effort" flagships it competes against.

On BenchLM, that bet is paying off on the board that matters to the open-source crowd. M3 is the top-ranked open-weight model at about 69.8, and it places #15 of roughly 200 models on the public leaderboard overall (and #13 of 99 on BenchLM's stricter verified lane) — meaning a downloadable model is now mixing into the lower reaches of the closed-frontier pack, not sitting a tier below it. Its strongest published category is instruction following; its weakest, tellingly, is agentic tasks, where it ranks near the bottom of the field.

The coding numbers are where the "narrowing gap" thesis gets its receipts. MiniMax reports M3 at 59.0% on SWE-Bench Pro, the harder software-engineering benchmark, edging past Kimi K2.6's 58.6% to lead open weights on that measure. As BenchLM's editors framed the field, the best open-weight LLM "right now is MiniMax M3" — followed by Z.ai's GLM-5.1 and GLM-5. On other vendor-reported benchmarks, M3 posts 78.1% on MMMU-Pro, 91.6% on OmniDocBench, and 84.6% on Video-MMMU. Those are vendor figures, and worth reading as direction rather than settled fact until independent evaluations catch up.

## How narrow is "narrow"?

Narrow is not the same as closed, and the honest version of this story keeps the seams showing. On SWE-Bench Pro, open leaders like M3 and GLM-5.1 land around 58-59% — roughly level with a mid-tier closed model such as GPT-5.5. But on SWE-bench Verified, the closed frontier still runs well ahead: GPT-5.5 is reported near 88.7%, and the strongest open coder, DeepSeek V4 Pro, around 80.6%. On Moonshot's own launch chart for Kimi K3, the freshly shipped open flagship trails Anthropic's Claude Fable 5 by 5.4 points on FrontierSWE and by just 0.5 points on Terminal Bench 2.1 — inside a single point on some agentic rows.

The nuance analysts keep stressing: the gap is no longer one number. Frontier-adjacent open models are within a generation of the closed leaders on hard coding; generalist, customization-first open models still trail by double digits and say so plainly. As one widely cited July tracker put it, the gap now "reads as one generation, not several" — a smaller claim than the hype, and a much bigger one than last year's.

## The July offensive

M3's leadership landed inside an unusually crowded two-week window. Between July 4 and July 17, five open-weight moves clustered: Moonshot shipped Kimi K3 (a 2.8-trillion-parameter model, weights promised by July 27); Thinking Machines Lab — Mira Murati's startup — shipped Inkling under Apache 2.0, the first credible US-built open model at frontier-adjacent scale; DeepSeek scheduled the official graduation of V4 from preview; Mistral teased a new sparse mixture-of-experts family; and MiniMax's own 2.7-trillion-parameter "M3 Pro" plan surfaced in press reports (single-sourced, and unconfirmed by MiniMax).

Thinking Machines was refreshingly blunt that Inkling "is not the strongest overall model available today, open or closed," pitching customization over raw capability. Mistral CEO Arthur Mensch, confirming his lab's entry, said the company had "a very exciting model to come this summer — it will be open-weight, and we're opening early access to it in July." The through-line: open weights stopped being a China-only phenomenon this month, even as Chinese labs still hold most of the top positions.

## Analysis: why the momentum reshapes pricing

The competitive pressure is showing up in dollars, not just benchmarks. DeepSeek rolled out its first time-of-day API pricing — surcharges that double rates during daily peak windows, off-peak unchanged — while Kimi K3 listed at $3 per million input tokens (30 cents on a cache hit) and $15 per million output, flat across its full context. On OpenRouter's early-July snapshot, Chinese open-weight labs dominated token volume, with DeepSeek alone moving roughly 5.4 trillion tokens a week.

That is the real leverage of an open-weight leader like M3: it does not have to beat GPT-5.5 to matter. It only has to be close enough that weights access, deployment control, and a fraction of the price tip specific workloads open. When the capability gap was multi-generational, closed vendors could price to their moat. At single digits on the benchmarks buyers actually run, that moat is a line item to defend.

## What to watch next

Three near-term markers will test whether M3's perch holds. First, Kimi K3's open weights, promised by July 27 — if they ship at listed benchmarks, M3's overall lead could be short-lived. Second, DeepSeek V4's official launch and whether its peak/off-peak pricing becomes the template others copy. Third, and most consequential, the next closed-frontier release (a rumored Gemini 3.5 Pro chief among them), which would reset the reference line every "narrowing gap" number is measured against. Until then, the leaderboard says something it never used to: the model on top of the open pile is close enough to the top of the whole pile to change the math.

---

*Figures are as reported by BenchLM and vendor materials as of mid-July 2026; vendor-reported benchmarks await independent verification.*

**Sources:** [BenchLM](https://benchlm.ai/), [Digital Applied — July 2026 Open-Weight Wave](https://www.digitalapplied.com/blog/open-weight-model-wave-july-2026-momentum-tracker)