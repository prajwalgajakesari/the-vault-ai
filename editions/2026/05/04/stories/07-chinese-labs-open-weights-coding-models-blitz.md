---
headline: "Four Chinese Labs Release Open-Weights Coding Models in 12-Day Blitz Undercutting Western Prices"
slug: chinese-labs-open-weights-coding-models-blitz
category: llms-genai
story_number: "07"
date: 2026-05-04
---

# Four Chinese Labs Release Open-Weights Coding Models in 12-Day Blitz Undercutting Western Prices

In the space of less than three weeks, four Chinese AI laboratories dropped open-weights coding models that collectively match or exceed the best Western frontier systems on agentic engineering benchmarks -- at a fraction of the cost. The sprint began on April 7 when Z.ai released GLM-5.1, continued with MiniMax open-sourcing M2.7 on April 12, accelerated when Moonshot AI shipped Kimi K2.6 on April 20, and culminated with DeepSeek unveiling V4 Pro and V4 Flash on April 24. None of the four costs more than a third of Anthropic's Claude Opus 4.7 on a per-token basis.

## The Models

The numbers tell a story of rapid convergence at the top. GLM-5.1, a 754-billion-parameter mixture-of-experts model released under the MIT license, scored 58.4 percent on SWE-Bench Pro on launch day -- briefly topping every model, open or closed, on the global leaderboard. Z.ai demonstrated the model by having it build a complete Linux desktop environment from scratch across 655 autonomous iterations, boosting vector database query throughput to 6.9 times the production baseline. It held the number-one spot for nine days before Claude Opus 4.7 reclaimed it.

Five days later, MiniMax published the weights for M2.7, a 229-billion-parameter MoE model notable for being the first to meaningfully participate in its own training loop. During development, an internal copy of M2.7 ran over 100 rounds optimizing its own scaffold. The model scored 56.22 percent on SWE-Bench Pro and 57.0 percent on Terminal Bench 2.

Moonshot AI's Kimi K2.6, a one-trillion-parameter vision-language model with 32 billion active parameters, arrived on April 20 with a 58.6 percent SWE-Bench Pro score, briefly retaking the open-source crown from GLM-5.1. The company demonstrated the model with a 12-hour continuous tool-use trace that ported an entire inference engine to Zig. Kimi K2.6 can instantiate hundreds of agents that collaborate on a single task, a capability Moonshot designed for day-long autonomous coding sessions.

DeepSeek's V4, released April 24, shipped in two variants: V4 Pro at 1.6 trillion total parameters with 49 billion active, and V4 Flash at 284 billion total with just 13 billion active. Both carry a native one-million-token context window and MIT licensing. Fortune reported that DeepSeek's pricing is "aimed at luring developers, startups, and enterprise users away from expensive U.S. models" from OpenAI, Anthropic, and Google.

## The Price Gap

The cost differential is stark. Claude Opus 4.7 runs at five dollars per million input tokens and 25 dollars per million output tokens. DeepSeek V4 Pro, its nearest Chinese competitor on benchmarks, lists at $0.435 input and $0.87 output per million tokens during its promotional period -- roughly one-twelfth the input cost and one-twenty-ninth the output cost. Even at full price after the promotion ends, V4 Pro would run at $1.74 and $3.48 respectively, still a fraction of Opus.

Kimi K2.6 comes in at $0.60 input and $2.50 output per million tokens. MiniMax M2.7 is the cheapest of the four at $0.30 input and $1.20 output. GLM-5.1 sits at $1.40 input and $4.40 output, making it the most expensive of the Chinese entrants but still less than a third of Opus on output pricing.

"Chinese-stack inference runs roughly five to 25 times cheaper at frontier capability tiers," noted the late-April Chinese LLM comparison on DEV Community. "You can get 80th-percentile SWE-Bench performance for $0.60 per million tokens, or 73rd-percentile performance for free on your own laptop."

## Strategic Context

The Air Street Press State of AI report for May 2026 described the releases as a coordinated "sprint" in which "four Chinese labs released open-weights coding models within a 12-day window" that "reached roughly the same capability ceiling on agentic engineering at meaningfully lower inference cost than the Western frontier." Zhipu's stock closed up 15.92 percent the day GLM-5.1 launched, a market signal of investor confidence in the open-weights strategy.

MIT Technology Review, in its April 21 analysis titled "China's open-source bet," called the wave part of a broader pattern in which Chinese companies have "repeatedly delivered AI models that match the performance of leading Western models at a fraction of the cost" since DeepSeek released its R1 reasoning model in January 2025.

The implications extend beyond pricing. All four models are released under permissive licenses -- primarily MIT -- meaning any developer or company can download, modify, and deploy them without restrictions. They are available through unified routing on platforms like Vercel AI Gateway and OpenRouter, lowering the integration barrier for teams already using Western APIs.

## What to Watch

The 12-day blitz raises uncomfortable questions for Western labs charging premium prices. If open-weights models from China can match 90-plus percent of frontier coding performance at one-fifth to one-twenty-fifth the cost, the value proposition of closed, expensive APIs narrows to the remaining margin of capability, brand trust, and compliance guarantees. For enterprise buyers evaluating their 2026 AI budgets, the calculus just shifted. The next test will be whether these models hold up under sustained production workloads -- and whether the Western labs respond with price cuts of their own.
