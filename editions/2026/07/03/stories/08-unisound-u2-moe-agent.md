Chinese AI firm Unisound has released U2, a 266-billion-parameter mixture-of-experts model that activates just 10 billion parameters per token and is designed, from the ground up, to do work rather than merely answer questions. The company frames it as a "native agentic large model built for execution" that can autonomously decompose and complete workflows spanning 100 or more steps.

Announced in early June 2026 and now live on the company's Token Hub, U2 lands squarely in the year's dominant AI storyline: a wave of Chinese labs shipping cost-efficient, agent-focused models that undercut Western frontier systems on price while chasing them on capability.

## A sparse model built to act

U2's headline architecture is its sparsity. Of its 266 billion total parameters, only about 10 billion — roughly 3.8% — fire on any given token. That is the same MoE playbook that DeepSeek, MiniMax, and Zhipu have ridden to prominence, and it is the reason Unisound can price the model aggressively: **$0.15 per million input tokens and $0.30 per million output tokens**, according to both Unisound and the tracking site LLM Stats.

The company says U2 was trained on 15 trillion tokens with a knowledge cutoff of January 2026, and it is released under a proprietary, non-commercial license rather than as open weights.

What distinguishes U2's pitch is less the parameter count than the design philosophy Unisound attaches to it. The company describes the model as guided by "high intelligence density × high Token value" — using fewer activated resources to carry stronger capabilities, and making every call move closer to a deliverable result. In plain terms, Unisound is arguing that raw output length and parameter scale are the wrong yardsticks once AI enters real workflows. What matters, the company says, is whether the model can actually finish the task.

To get there, U2 leans on a "Hybrid Thinking" mechanism that switches between explicit chain-of-thought reasoning and faster latent-space reasoning depending on a task's stage and uncertainty. Early exploration and planning happen internally, without decoding every intermediate thought into visible tokens; at critical junctures — constraint checking, result convergence — the model reverts to readable, verifiable reasoning. Unisound pairs this with an "Agent-Harness" co-training paradigm, in which the execution scaffolding around the model evolves in the same training loop as the model itself, feeding real task trajectories back into training.

## The benchmark case

Unisound's own release positions U2 in the top tier of mainstream models across several evaluations. On **GPQA Diamond**, which tests hard knowledge and reasoning, the company reports a score of **87.9**, claiming it outperforms GLM-5.1, a Hy3 preview, DeepSeek-V4-Flash (High), and MiniMax M2.7. On **SWE-Bench Verified**, the real-world software-engineering benchmark, Unisound reports a score of **75**.

Independent aggregation has landed in a similar band, with slightly different figures. Reporting drawn from benchmark trackers cites roughly **86.9% on GPQA Diamond, 85.8% on MATH-500, and 72.2% on SWE-bench Verified** — close enough to Unisound's numbers to corroborate the broad claim, but a reminder that vendor-reported and third-party scores rarely match to the decimal.

Crucially, Unisound leans hardest on the agentic benchmarks that map to its "get work done" thesis. It reports **76.9 on Claw-Eval (pass@3)**, an end-to-end test of autonomous agent execution, and **72.9 on GDPval**, which measures real office and knowledge-work delivery — document analysis, report writing, spreadsheet processing, chart and slide generation. "U2 does not win through a single isolated capability," the company said, arguing that the model delivers "systematic performance across reasoning, coding, Agent execution, and office delivery."

The demos Unisound highlights are similarly execution-flavored: generating structured research reports as Word documents, PowerPoint decks, and interactive HTML pages; building playable HTML5 games such as Tetris end to end; and producing competitive-landscape matrices and data visualizations.

## Why It Matters

U2 is another data point in the defining trend of 2026: China's labs are competing not by matching the largest Western models parameter for parameter, but by shipping sparse MoE systems that are cheap to run and tuned for agents. At $0.15 in and $0.30 out per million tokens, U2 is priced to be embedded in high-volume automation pipelines, where inference cost — not benchmark bragging rights — decides what actually gets deployed.

The framing matters, too. By anchoring the launch to agentic benchmarks like Claw-Eval and GDPval rather than trivia-style leaderboards, Unisound is betting that the market's attention is shifting from "can it answer?" to "can it complete a multi-step job?" That is the same wager DeepSeek, MiniMax, Zhipu, and others are making, and it turns evaluation itself into a competitive front. For Unisound — a speech-AI company that only recently listed publicly and reported narrowing losses — U2 is also a strategic pivot, a move to plant a flag in the native-agent era rather than remain a voice-tech specialist.

## What to Watch

Three things will determine whether U2 is more than a well-timed press release. First, independent verification: the gap between Unisound's reported scores and third-party figures is modest, but agentic benchmarks are young and easy to game, so watch for reproductions on neutral harnesses. Second, availability beyond Unisound's own Token Hub — the model is proprietary and, for now, served by a single provider, which limits how far developers can pressure-test it. And third, whether "100+ step" autonomy holds up outside curated demos. Long-horizon agentic reliability is exactly where today's models tend to break, and it is the claim on which U2's entire pitch rests.
