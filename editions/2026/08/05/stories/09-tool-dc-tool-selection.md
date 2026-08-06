# 'Tool-DC' Uses Divide-and-Conquer to Fix How LLMs Pick the Right Tool

*The Vault - AI Edition | Category: llms-genai | Story 09*

When an AI agent has three tools to choose from, picking the right one is trivial. Give it thirty, and something quietly breaks. A new framework out of Wuhan University and Nanyang Technological University argues that the fix is not a smarter retriever or a bigger model, but an old idea from algorithms class: divide and conquer.

## The problem hiding inside every agent

The paper, titled *Try, Check and Retry: A Divide-and-Conquer Framework for Boosting Long-context Tool-Calling Performance of LLMs* (arXiv:2603.11495), names a failure mode that anyone building AI agents has felt but rarely measured. Tool-calling lets a language model reach outside its frozen weights to hit an API, run a query, or trigger an action. But in the real world, models are not handed a tidy shortlist. They are handed dozens or hundreds of candidate tools, many with near-identical names and subtly different argument schemas.

The authors show, in preliminary experiments, that accuracy collapses as the catalog grows. Scaling candidate tools from fewer than ten to twenty causes every model they tested to degrade, with the smaller ones falling hardest. On the Berkeley Function-Calling Leaderboard (BFCL), Qwen2.5-1.5B loses more than 22 percentage points in the extended setting. The diagnosis is twofold: long context created by long tool lists overwhelms the model, and tools with similar semantics but different argument descriptions confuse the argument-filling step.

This matters because most benchmarks quietly understate the problem. Existing suites typically present fewer than ten candidate tools, which the authors call inconsistent with real-world scenarios. They introduce an Extended Setting that scales the tool count up to twenty to simulate production conditions - and it is precisely there that standard tool-calling falls apart.

## Try, Check, Retry

Tool-DC's response is structural. As the paper puts it, the core of the method is 'to reduce the reasoning difficulty and make full use of self-reflection ability of LLMs via a Try-Check-Retry paradigm.'

Concretely, the training-free variant, Tool-DC (TF), first splits the full pool of candidate tools into several smaller groups and runs tool-calling on each group in parallel. That is the *Try* step, and it is where the divide-and-conquer intuition pays off: each inference call sees a short, focused list instead of a sprawling one, cutting both context length and the odds of semantic confusion. The *Check* step then verifies each parallel result against strict schema constraints, filtering out malformed or invalid calls. Finally, *Retry* aggregates the validated candidates and refines a single global answer, effectively letting the model reflect across its own partial attempts.

Because running many parallel passes carries latency and cost, the authors also build a training-based variant, Tool-DC (TB). It internalizes the same decision behavior into the weights: they harvest the correct reasoning traces produced during Tool-DC (TF), assemble them into a high-quality chain-of-thought dataset, and fine-tune the model to perform the try-check-retry logic in a single, cheaper pass.

## The numbers

Across BFCL and ACEBench, the training-free version delivers up to a +25.10% average gain over the baseline, with the largest lifts concentrated exactly where standard methods suffer most - small models under the extended, many-tool setting.

The training-based result is the more provocative headline. With Tool-DC (TB), Qwen2.5-7B reaches an 83.16% overall score on BFCL, which the authors report as surpassing OpenAI's o3 and Claude Haiku 4.5. A seven-billion-parameter open model, in other words, is pulled up to and past proprietary-tier function-calling accuracy - not by scaling parameters, but by restructuring how it approaches the selection problem.

## Why tool selection is the agent bottleneck

The result lands on a sore spot. As agents move from demos to deployment, tool catalogs balloon. The Model Context Protocol has made it trivial to expose dozens or hundreds of tools to a single model, and marketplaces now offer many functionally overlapping options. The dominant workaround - bolt on a retriever to pre-select a small tool subset - has a brittle failure mode the paper flags directly: if the retriever drops the golden tool, the model cannot recover, because the right answer never enters the context.

Tool-DC sidesteps that dependency. Rather than betting everything on one retrieval pass, it keeps all tools in play but partitions them, then uses verification and self-reflection to converge. That reframes tool selection from a search problem into a reasoning-under-decomposition problem - which happens to be something LLMs, given short enough context, are already good at.

## What to watch

The open questions are practical. Parallel Try passes trade compute for accuracy, so the real economics depend on how far Tool-DC (TB) can compress that overhead without giving back the gains. It is also worth watching whether the approach holds as tool counts climb past twenty into the hundreds, and whether the fine-tuned try-check-retry behavior transfers across model families rather than the Qwen line the authors studied. If it does, the lesson for agent builders is clear: before reaching for a bigger model, try giving the one you have a smaller problem to solve at a time.

---

*Sources: arXiv:2603.11495; Berkeley Function-Calling Leaderboard (BFCL); ACEBench.*
