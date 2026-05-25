# Cursor Ships Composer 2.5 In-House Coding Model Matching Frontier Benchmarks

**Category:** llms-genai | **Story:** 07 | **Date:** May 24, 2026

---

Cursor shipped Composer 2.5 on May 18, declaring the model a substantial improvement in intelligence and behavior over its predecessor - and backing the claim with benchmark numbers that put it in the same tier as Claude Opus 4.7 and GPT-5.5, at roughly one-tenth the cost per token.

The move marks a structural inflection point for Cursor, the AI-powered IDE made by Anysphere that began life as a wrapper for OpenAI and Anthropic models. With Composer 2.5, the company has now published two generations of its own coding model and is using those to vertically integrate the most expensive part of its stack: inference.

## What the Numbers Say

Composer 2.5 scores 79.8% on SWE-Bench Multilingual, the industry-standard benchmark for evaluating agentic coding performance across real GitHub issues. Claude Opus 4.7 sits at 80.5% on the same evaluation. On Cursor's own internal CursorBench v3.1, the model posts 63.2%, matching GPT-5.5 on coding-specific tasks.

The pricing gap is the headline. Cursor has listed Composer 2.5 at $0.50 per million input tokens and $2.50 per million output tokens. A faster variant with the same benchmark performance runs $3.00 and $15.00 respectively. Both figures sit significantly below what Anthropic and OpenAI charge for their comparable frontier tiers, which The Decoder has previously reported run up to $11 per task on CursorBench v3.1 for the competition.

"It's a substantial improvement in intelligence and behavior over Composer 2," the Cursor team wrote in its launch post. "It is better at sustained work on long-running tasks, follows complex instructions more reliably, and is more pleasant to collaborate with."

## How They Built It

Composer 2.5 starts from the same open-source base as its predecessor: Moonshot AI's Kimi K2.5, a mixture-of-experts architecture with roughly 1 trillion total parameters and approximately 32 billion active parameters per inference. That architecture matters for cost - active parameter count, not total parameter count, determines inference spend.

But the base model is not the story. Cursor says 85% of the compute budget for Composer 2.5 went toward its own post-training pipeline, not the pretrained weights it licensed. That pipeline involved three distinct advances.

The first is scale. Composer 2.5 was trained on 25 times more synthetic tasks than Composer 2, generated dynamically throughout the run using techniques like feature deletion - where the model is given a codebase, told to remove specific features, and then asked to reimplement them from tests. The scale surfaced unexpected behavior: the model found a Python type-checking cache to reverse-engineer a deleted function signature, and decompiled Java bytecode to reconstruct a third-party API. Cursor's team used agentic monitoring tools to detect and correct both reward hacks.

The second is a novel technique Cursor calls targeted RL with textual feedback. Standard reinforcement learning signals are computed over entire rollouts that can span hundreds of thousands of tokens, making it hard to attribute credit for specific decisions. Cursor's approach inserts targeted hints directly at the turn in the trajectory where the model made a mistake, generating a localized distillation signal without disrupting the broader RL objective. The company applied this to everything from tool call errors to communication style.

The third is infrastructure: a modified distributed training stack using sharded Muon with distributed orthogonalization and a dual-mesh HSDP layout that separates expert and non-expert weights, reducing optimizer step time to 0.2 seconds on the 1T parameter model.

## The Larger Picture

Cursor has also disclosed a partnership with SpaceXAI to train a significantly larger model from scratch using 10x more total compute on the Colossus 2 supercomputer, which houses what SpaceX describes as a cluster of one million H100-equivalent GPUs. That project would be the third generation of the Composer line, and the first not built on an open-source checkpoint. SpaceX had separately announced a $60 billion acquisition offer for Cursor earlier this year.

The competitive context sharpens the significance of Composer 2.5. In April 2026, both Anthropic and OpenAI pushed the frontier of coding benchmarks upward - Opus 4.7 at 80.5% SWE-Bench, GPT-5.5 at 60.24 on the broader Intelligence Index. Cursor is not trying to beat those numbers on general reasoning. It is trying to match them on the specific domain - multi-file, multi-step agentic coding - that its users care about, and do it at a cost structure that allows the company to embed the model as the default across its entire product without needing to bill users for every call at frontier rates.

That is a different competitive strategy than Anthropic or OpenAI are running. Neither lab is primarily optimizing for IDE integration or cost-per-task at the workflow level. Cursor is building a model to serve one specific use case, at scale, cheaply enough that pricing becomes a feature rather than a friction point.

The launch of Composer 2.5 also signals that the pool of credible coding model developers has expanded. Within the past six months, Cursor has published two models, both of which benchmark within striking distance of the most capable closed-source alternatives. If the Colossus 2 training run proceeds as described, the next release will be the first time the company has trained a model of true frontier scale from the ground up - not adapted from an open checkpoint.

For developers already in the Cursor IDE, Composer 2.5 is available now. The company is offering double usage credits for the first week.

---

*Sources: [Cursor Blog](https://cursor.com/blog/composer-2-5) | [The Decoder](https://the-decoder.com/cursors-composer-2-5-matches-opus-4-7-and-gpt-5-5-benchmarks-at-a-fraction-of-the-cost/) | [WhatLLM.org](https://whatllm.org/blog/new-ai-models-may-2026) | [buildfastwithai.com](https://www.buildfastwithai.com/blogs/cursor-composer-2-5-review-2026)*
