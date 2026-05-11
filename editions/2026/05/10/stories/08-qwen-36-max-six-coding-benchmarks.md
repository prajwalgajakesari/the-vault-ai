---
headline: "Alibaba Qwen 3.6 Max Preview Tops Six Major Coding Benchmarks Unseating Claude and GLM From Leaderboards"
slug: qwen-36-max-six-coding-benchmarks
category: llms-genai
story_number: "08"
date: 2026-05-10
author: The Vault AI
tags: [alibaba, qwen, coding-benchmarks, swe-bench, closed-weights, agentic-ai, chinese-ai, llm-leaderboards]
---

# Alibaba Qwen 3.6 Max Preview Tops Six Major Coding Benchmarks Unseating Claude and GLM From Leaderboards

Alibaba has fired a shot across the bow of the global AI leaderboard. On April 20, the Chinese tech giant released Qwen3.6-Max-Preview, a proprietary flagship language model that claimed the top score on six of the most closely watched coding benchmarks in the industry, unseating Anthropic's Claude and Zhipu's GLM from positions they had held for weeks. For an AI community accustomed to Western labs dominating the coding frontier, the result marks a notable inflection point.

The six benchmarks where Qwen3.6-Max-Preview now sits at number one are SWE-Bench Pro, Terminal-Bench 2.0, SkillsBench, QwenClawBench, QwenWebBench, and SciCode. Together, they span the full arc of what matters to developers building AI-assisted software: real-world bug fixing across multi-file repositories, terminal command chaining under hardware constraints, general problem-solving, tool use, web development, and scientific programming. GLM-5.1, which had held the top spot on SWE-Bench Pro since earlier in April, and Claude Opus 4.7, which led Terminal-Bench 2.0 at 69.4 percent, were both displaced.

## The Numbers Behind the Headline

The improvements over Alibaba's own Qwen3.6-Plus, released just three weeks earlier, are not incremental. SkillsBench jumped by 9.9 points. SciCode improved by 10.8 points. NL2Repo, which tests the ability to navigate and contribute to real codebases, gained 5.0 points. Terminal-Bench 2.0, a grueling benchmark that simulates actual terminal-based engineering tasks under real hardware constraints with a three-hour timeout, improved by 3.8 points.

On the Artificial Analysis Intelligence Index, Qwen3.6-Max-Preview scored 52, the highest of any Chinese-origin model and above DeepSeek V4 Pro at 49. The model runs a Mixture-of-Experts architecture with 35 billion total parameters but only 3 billion active at inference time, keeping latency low while pushing benchmark scores past the competition.

Where the model dominates most convincingly is QwenWebBench, Alibaba's internal front-end code generation benchmark, where it posted an ELO of 1,558 compared to 1,182 for Claude Opus 4.5. For teams building UI-heavy products, that 376-point gap is the most actionable number in the entire release.

## A Strategic Pivot to Closed Weights

Perhaps more consequential than any benchmark is what Qwen3.6-Max-Preview signals about Alibaba's strategy. Historically, Alibaba published Qwen model weights under Apache 2.0 or similar permissive licenses, building a massive open-source ecosystem. This time, the flagship ships closed-weights only, available exclusively through Alibaba Cloud's API.

The shift mirrors the playbook that OpenAI and Anthropic established years ago: release capable open models to build community adoption, but keep the crown jewels behind an API paywall. Analysts point to three drivers behind the decision: a desire to monetize through API-first revenue, reducing distillation risk following the US-China AI intellectual property tensions that escalated in April 2026, and protecting the compute and data moat that makes the model possible.

Alibaba has not abandoned open weights entirely. Qwen3.5-Plus, Qwen3-Coder-Plus, and the Qwen3-VL series remain open, and the open-weight Qwen3.6-35B-A3B variant, which shares the same MoE skeleton, scored 73.4 percent on SWE-Bench Verified under Apache 2.0. But the message is clear: the best Qwen model will no longer be free to download.

## The preserve_thinking Innovation

One feature distinguishes Qwen3.6-Max-Preview from most competitors. Called preserve_thinking, it retains the model's chain-of-thought reasoning across multiple conversation turns rather than discarding it after each response. For agentic coding workflows where a model needs to analyze a codebase, propose a fix, refine based on test output, and handle edge cases across a dozen turns, this continuity is transformative.

Satvik Paramkusam, writing for Build Fast with AI, called the 10.8-point gain on SciCode the standout number. He noted that SciCode tests the ability to write working code that solves real scientific problems, and that kind of improvement signals the model genuinely understands complex domains rather than pattern-matching on training data.

## Reality Checks and Caveats

The benchmark results, while genuine, come with important caveats. Alibaba's comparison tables used Claude Opus 4.5, not the newer 4.7, as the baseline for most metrics. On SWE-Bench Verified, the gold standard for production software engineering, Claude Opus 4.7 still leads at 87.6 percent compared to an estimated 82 to 85 percent for Qwen. Independent testers at Towards AI flagged that the model underperformed on real-world coding tasks that fell outside benchmark patterns, a reminder that leaderboard supremacy does not automatically translate to production reliability.

The model also has no production SLA as of publication and is text-only, lacking the vision capabilities that Claude Opus 4.7 offers. Its pricing has not been finalized, though OpenRouter lists the model at 1.30 dollars per million input tokens, well below Anthropic's pricing.

## What This Means for the AI Landscape

Qwen3.6-Max-Preview's sweep of six coding benchmarks crystallizes a reality that has been building for months: the gap between Chinese and Western AI labs on code-centric tasks has effectively closed. The competition is now a three-way race between Alibaba, Anthropic, and OpenAI, with Zhipu's GLM and Google's Gemini pressing close behind.

For developers, the practical implication is straightforward. The model is available now through Alibaba Cloud and third-party routers like OpenRouter and TokenMix, with OpenAI and Anthropic API compatibility baked in. Whether the preview label gives way to a stable release with full SLAs remains the key question for enterprise adoption. Until then, Qwen3.6-Max-Preview is the model to benchmark against, even if it is not yet the model to bet a production system on.
