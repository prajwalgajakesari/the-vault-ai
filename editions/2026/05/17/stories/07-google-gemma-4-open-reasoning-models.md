---
title: "Google Releases Gemma 4 Open Models for Advanced Reasoning and Agentic Workflows"
slug: google-gemma-4-open-reasoning-models
category: llms-genai
story_number: "07"
date: 2026-05-17
---

# Google Releases Gemma 4 Open Models for Advanced Reasoning and Agentic Workflows

Google has released Gemma 4, its most capable family of open-weight models yet, engineered from the ground up for multi-step reasoning, autonomous agent behavior, and deployment across a spectrum of hardware — from a smartphone to a workstation GPU. Launched on March 31 and publicly announced on April 2, 2026, the release lands under a clean Apache 2.0 license with no usage thresholds, no enterprise carve-outs, and no revenue caps. For the open-model community, that licensing choice may prove just as consequential as the benchmark numbers.

## Four Models, One Coherent Strategy

Gemma 4 ships in four variants designed around specific deployment contexts. The E2B (2B parameters) and E4B (4B parameters) edge models are built for on-device inference on phones and low-power hardware, each offering a 128K context window and — notably — native audio input for speech recognition. The 26B Mixture-of-Experts model activates only 3.8B parameters at inference time, making it tractable on a single consumer GPU while punching well above its active parameter weight. At the top sits the 31B Dense model, aimed at workstations and cloud deployments, with a 256K context window and the highest performance ceiling in the family.

The naming strategy underscores Google DeepMind's explicit goal: "byte for byte, the most capable open models." The claim is that capability-per-parameter, not raw scale, is the axis on which Gemma 4 competes.

## Benchmark Numbers That Demand Attention

The 31B Dense model posts scores that would have seemed implausible for a sub-40B open model even eighteen months ago. On MMLU Pro it reaches 85.2%; on AIME 2026 (a demanding mathematical reasoning benchmark) it scores 89.2%; on GPQA Diamond — a measure of graduate-level scientific reasoning — it hits 84.3%, outperforming Meta's Llama 4 Scout, which has a 109B total parameter count, by a full ten percentage points on that task.

Coding performance is equally striking. Gemma 4 31B logs a Codeforces ELO of 2150, placing it at an expert competitive-programmer level, while LiveCodeBench v6 returns an 80% score. The model also ranks third overall on LMSYS Arena AI, a human-preference leaderboard, placing it ahead of most models several times its size.

For agentic tasks specifically, the improvement over its predecessor is dramatic. On τ2-bench, a benchmark designed to test real-world agentic tool use, Gemma 3 27B scored 6.6%. Gemma 4 31B scores 86.4% — a jump of nearly 80 percentage points. That number is not a typo, and it is the one that has developers most animated about what Gemma 4 can actually do in production.

## Built for Agents, Not Just Completions

Agentic capability is not an afterthought in Gemma 4's design. Every model in the family ships with native function-calling, structured JSON output, and configurable system prompts. The models can produce more than 4,000 tokens of chain-of-thought reasoning before committing to an answer — a configurable "thinking mode" that allows developers to trade latency against depth of reasoning depending on the task.

Google has also invested in long-context retrieval. The 31B model improved from 13.5% to 66.4% on multi-needle retrieval tests — a benchmark that measures whether a model can locate and synthesize multiple pieces of relevant information buried across a very long context. For RAG pipelines, document-level reasoning, and long-horizon planning tasks, that improvement matters considerably.

All four models are natively multimodal, processing images and video with variable-resolution support and excelling at tasks like OCR and chart understanding. The E2B and E4B edge variants extend this to audio, enabling speech-grounded reasoning on-device.

## The Apache 2.0 Bet

Technically, Gemma 4 is impressive. Strategically, the licensing decision may be the longer-term story.

Developer Sam Witteveen put it plainly: "This is an actual real Apache 2 license, which means for the first time, you can take Google's best open model, modify it, fine tune it, deploy it commercially, do whatever you want with it."

Earlier Gemma releases carried custom licenses with constraints that made corporate legal teams nervous. Apache 2.0 changes that calculus entirely. For solo developers and startups shipping products, there is no threshold to monitor, no clause to negotiate, no moment when Google could demand an enterprise agreement. Researcher and analyst Nathan Lambert framed it succinctly: "Gemma 4's success is going to be entirely determined by ease of use. It's strong enough, small enough, with the right license, and from the U.S., so many companies are going to slot it in."

As of May 2026, no competitor of comparable capability matches the combination of benchmark performance, model size, and fully permissive licensing that Gemma 4 offers.

## One Practical Catch

The community has noted at least one friction point: inference speed on the 26B MoE variant. On the same GPU where Alibaba's Qwen 3.5 delivers more than 60 tokens per second, Gemma 4's 26B MoE tops out around 11 tokens per second. For interactive applications where latency is felt by end users, that gap is significant. Google has not publicly addressed the issue, and it is likely to shape which use cases the MoE variant fits and which it does not.

The 31B Dense model and the edge variants do not appear to share this problem to the same degree, and the edge models in particular are designed for the latency-sensitive scenarios where tokens-per-second matters most.

## What It Means

Gemma 4 is the clearest signal yet that Google DeepMind is competing seriously in the open-weights tier — not as a public relations exercise, but as a deliberate platform play. By combining state-of-the-art reasoning scores with a genuinely permissive license and a hardware-spanning model family, Google is positioning Gemma 4 as infrastructure: the kind of model that disappears into products rather than being celebrated on a benchmark leaderboard.

Whether that strategy succeeds will depend partly on the inference efficiency improvements that need to come, and partly on the ecosystem tooling that builds around it. But the release itself sets a new bar for what an openly licensed model can deliver in 2026.
