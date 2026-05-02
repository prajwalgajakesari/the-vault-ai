---
headline: "Mistral Releases Medium 3.5, a 128B Dense Open-Weights Model With 256K Context Window"
slug: mistral-medium-3-5-open-weights
category: llms-genai
story_number: "06"
date: 2026-05-01
---

# Mistral Releases Medium 3.5, a 128B Dense Open-Weights Model With 256K Context Window

Mistral AI on Tuesday released Medium 3.5, a 128-billion-parameter dense language model with open weights, a 256K-token context window, and a single set of weights that handles chat, reasoning, and code -- a combination the Paris-based company is betting will redefine what mid-tier models can do in production. The release, accompanied by Mistral's tagline "medium is the new large," lands as the open-weights movement enters a new phase of direct competition with proprietary frontier systems from OpenAI, Anthropic, and Google.

Medium 3.5 is available immediately on Hugging Face under a modified MIT license, through the Mistral API, and as the default model in both Le Chat and Mistral Vibe, the company's coding assistant. API pricing is set at $1.50 per million input tokens and $7.50 per million output tokens.

## One Model, Three Jobs

The most significant architectural choice in Medium 3.5 is what Mistral calls a "merged model" approach. Rather than shipping separate fine-tuned checkpoints for instruction following, chain-of-thought reasoning, and code generation, the company collapsed all three capabilities into a single dense model with configurable reasoning effort per request.

"We believe that the future of AI deployment is a single model that can be configured at inference time, not a zoo of specialized checkpoints that operators have to route between," Mistral wrote in its technical announcement. The reasoning mode toggle lets developers choose between fast, low-latency replies and extended chain-of-thought processing without swapping models or endpoints -- a meaningful simplification for teams running production workloads.

The model also ships with native vision capabilities, function calling, and JSON-structured output, making it a multimodal workhorse out of the box. Multilingual support spans more than a dozen languages, including English, French, German, Spanish, Chinese, Japanese, Korean, and Arabic.

## Benchmark Performance

On SWE-Bench Verified, the standard benchmark for real-world coding tasks, Medium 3.5 scores 77.6% -- a result Mistral says places it ahead of both Devstral 2 and Qwen3.5 397B, a model more than three times its size. On the Tau3-Telecom agentic benchmark, it reaches 91.4%, underscoring the model's strength in tool use and multi-step task completion. Mistral has also claimed that Medium 3.5 surpasses Claude Sonnet 4.5 on several internal evaluations, though independent verification of those comparisons is still pending.

"Medium 3.5 is our first flagship merged model," the company stated in its Hugging Face release notes. "It handles instruction-following, reasoning, and coding in a single set of weights, with a 256K context window."

## Self-Hosting and the Open-Weights Play

The decision to release Medium 3.5 as open weights under a modified MIT license -- rather than restricting access to an API -- is Mistral's clearest signal yet that it sees self-hosted deployment as a primary go-to-market channel, not an afterthought. The dense 128B architecture can run on as few as four GPUs, a hardware requirement that puts it within reach of well-resourced enterprise teams and cloud deployments alike. An EAGLE speculative decoding variant has also been released on Hugging Face, designed to accelerate inference throughput.

The pricing at $1.50/$7.50 per million tokens for API access positions Medium 3.5 in a middle tier -- substantially cheaper than frontier models from Anthropic and OpenAI but more expensive than smaller open-source alternatives like Llama or Qwen. That pricing has already drawn scrutiny from developers on Hacker News and elsewhere, with some arguing that the cost is too high for a model that users can, in theory, host themselves for the price of GPU compute.

## Vibe Gets Remote Agents

Alongside Medium 3.5, Mistral announced that its Vibe coding assistant now supports remote agents -- cloud-based coding agents that can be spawned from the CLI or Le Chat and run asynchronously to produce finished pull requests on GitHub. The feature positions Vibe as a direct competitor to Cursor, Windsurf, and the growing field of AI-powered development environments, with Medium 3.5 serving as the backbone model.

## Analysis: Mistral's Enterprise Bet

Medium 3.5 represents a strategic clarification for Mistral. After a period in which the company shipped a rapid succession of models across multiple size classes -- Mistral Small, Medium 3, Devstral, Codestral -- this release consolidates the lineup around a single, versatile model that Mistral clearly wants enterprises to standardize on. The merged-model approach eliminates the operational complexity of managing multiple specialized endpoints, which has been a persistent pain point for teams deploying open-weights models in production.

The 256K context window is another enterprise-oriented feature, enabling use cases like full-codebase analysis, long-document summarization, and multi-turn agentic workflows that shorter-context models cannot support. Combined with native function calling and vision, Medium 3.5 is arguably the most complete single-model offering in the open-weights ecosystem today.

But Mistral's challenge remains distribution. Meta's Llama family dominates open-weights mindshare, and Chinese labs like Alibaba's Qwen team are shipping competitive models at breakneck speed. Medium 3.5's benchmark numbers are strong, but converting benchmark performance into enterprise adoption requires more than raw capability -- it requires ecosystem, support, and trust. Mistral's European roots and data sovereignty pitch give it an angle in regulated industries, but the company will need to prove that one merged model truly replaces the specialist zoo if it wants Medium 3.5 to become the default choice for teams that have the option to self-host.

The AI model market is fragmenting into two tiers: closed frontier systems sold as services, and open-weights models sold as infrastructure. With Medium 3.5, Mistral is making its most ambitious play yet for the latter category -- and betting that medium really is the new large.
