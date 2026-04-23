---
headline: "OpenAI Makes o3-mini the Default Reasoning Model and Introduces Flex Compute Pricing"
slug: openai-o3-mini-default-flex-compute
category: llms-genai
story_number: "08"
date: 2026-04-22
author: The Vault AI Edition
tags: [openai, o3-mini, reasoning-models, flex-compute, api-pricing]
---

# OpenAI Makes o3-mini the Default Reasoning Model and Introduces Flex Compute Pricing

**OpenAI has officially retired o1-mini from its ChatGPT model picker, installing o3-mini as the default reasoning model for Plus, Team, and Pro subscribers while simultaneously rolling out a new Flex compute pricing tier that slashes API costs for developers willing to trade latency for savings.**

The twin announcements mark a decisive acceleration in OpenAI's strategy to make advanced reasoning capabilities both faster and cheaper, a move that arrives as competition from Anthropic, Google DeepMind, and open-source challengers like DeepSeek continues to intensify.

## A Faster, Smarter Default

The o3-mini model replaces o1-mini directly in the ChatGPT model selector, meaning that millions of paying subscribers will now default into a meaningfully upgraded reasoning engine without lifting a finger. OpenAI says o3-mini delivers responses 24% faster on average than its predecessor, with response times clocking in at 7.7 seconds compared to o1-mini’s 10.16 seconds in internal A/B testing.

But speed is only part of the story. In blind evaluations, testers preferred o3-mini’s responses to o1-mini’s 56% of the time, while major errors on difficult real-world questions dropped by 39%. On PhD-level science questions, the new model outperforms o1-mini even at its lowest reasoning effort setting. On the Codeforces competitive programming benchmark, o3-mini achieves progressively higher Elo scores with increased reasoning effort, consistently outperforming its predecessor at every level.

"We view this as sort of the beginning of the next phase of AI, where you can use these models to do increasingly complex tasks that require a lot of reasoning," CEO Sam Altman said in a post on X announcing the rollout.

Perhaps most notably, OpenAI tripled the daily rate limit for Plus and Team users, jumping from 50 messages per day with o1-mini to 150 messages per day with o3-mini. That threefold increase in access, combined with the performance gains, makes the upgrade feel less like a model swap and more like a tier expansion bundled at the same $20-per-month price point.

## Flex Compute: Pay Less, Wait a Little Longer

Alongside the model change, OpenAI introduced Flex processing, a new API pricing tier currently in beta. Flex sits between the existing Batch API and Standard processing, offering tokens at Batch API rates while still allowing near-real-time interactions rather than the Batch API’s 24-hour completion window.

Under Flex processing, o3 API calls are priced at $5 per million input tokens and $20 per million output tokens. By comparison, Standard priority processing runs at $2 per million input tokens and $8 per million output tokens for the recently repriced o3, though Priority processing commands a premium for guaranteed low latency. Flex requests are automatically routed to lower-demand compute windows, and OpenAI warns that requests may occasionally return a "resource unavailable" response during peak periods.

"We're working on showing a bunch more than we show today," said Kevin Weil, OpenAI’s chief product officer, referencing broader efforts to make reasoning model behavior more transparent. The Flex tier fits into that philosophy: giving developers granular control over the cost-latency tradeoff rather than forcing a one-size-fits-all pricing structure.

The move also stacks with prompt caching, where cached inputs can cost as little as $0.035 per million tokens during off-peak windows, representing a discount of more than 90% compared to uncached, priority-tier pricing.

## Analysis: The Reasoning Race Gets Cheaper

OpenAI’s dual announcement reflects a market reality that would have seemed unlikely even 12 months ago: reasoning models are rapidly commoditizing. When o1 launched, it was positioned as a premium product with tight rate limits and steep API prices. Now, its miniaturized successor is the free default for paying ChatGPT users, and full-scale o3 is available at a fraction of its original cost.

The pricing pressure is coming from multiple directions. DeepSeek’s R1 demonstrated that competitive reasoning performance could be achieved at dramatically lower compute budgets. Google’s Gemini 2.5 Pro has pushed multi-step reasoning into its free tier. And Anthropic’s Claude models have steadily closed the gap on coding and analysis benchmarks.

For developers, Flex processing introduces a practical new option. Workloads like batch analysis, overnight report generation, and non-interactive data processing can now run on o3-class reasoning at costs that approach commodity LLM pricing. The tiered structure—spanning Batch, Flex, Standard, and Priority—gives teams a menu of price-performance options that did not exist a year ago.

The o3-mini model also arrives as the first small reasoning model to support function calling, Structured Outputs, and developer messages out of the box, features that make it production-ready for agentic workflows where previous reasoning models required workarounds.

## What Comes Next

OpenAI’s roadmap suggests this is a waypoint, not a destination. The company has already released o3 and o4-mini as successors, and CEO Altman has hinted at further unification of the model lineup. For now, the message to developers and subscribers is clear: reasoning just got faster, cheaper, and harder to ignore.

---

*Sources: [OpenAI](https://openai.com/index/openai-o3-mini/), [VentureBeat](https://venturebeat.com/ai/openai-announces-80-price-drop-for-o3-its-most-powerful-reasoning-model), [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing), [Tom's Guide](https://www.tomsguide.com/ai/openai-confirms-launch-of-o3-mini-ai-model-that-pauses-to-think-heres-how-it-works)*