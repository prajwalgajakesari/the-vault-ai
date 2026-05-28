---
headline: "Google Launches Gemini 3.5 Flash and Gemini Omni Models at I/O 2026"
slug: google-gemini-35-flash-omni-io
category: llms-genai
story_number: "06"
date: 2026-05-27
---

# Google Launches Gemini 3.5 Flash and Gemini Omni Models at I/O 2026

Google used its annual I/O developer conference on May 19 to unveil two new model families that together represent the company's clearest declaration yet: the era of AI chatbots is over, and the era of AI agents has begun. Gemini 3.5 Flash, a frontier-grade model purpose-built for autonomous coding and long-horizon agentic tasks, shipped generally available on the same day it was announced. Alongside it, Google introduced Gemini Omni, a new multimodal model family capable of generating video output grounded in real-world physics -- a first for the Gemini lineup.

## Flash: Frontier Intelligence at Flash Speed

Gemini 3.5 Flash arrives as a model that defies the traditional trade-off between intelligence and latency. It outperforms Google's own Gemini 3.1 Pro -- a much larger flagship model -- across nearly every benchmark the company publishes, while running four times faster than comparable frontier models from competitors. On Terminal-Bench 2.1, the coding benchmark, Flash scores 76.2% compared to 3.1 Pro's 70.3%. On MCP Atlas, a measure of agentic tool use, it hits 83.6% versus 78.2%. The jump on GDPval-AA, which measures performance on economically valuable real-world tasks, is even more dramatic: an Elo rating of 1656 versus 1314.

The model accepts text, image, video, and audio input with a 1-million-token context window and supports up to 65,536 output tokens. API pricing lands at $1.50 per million input tokens and $9.00 per million output tokens, with cached inputs at $0.15 -- less than half the cost of comparable frontier models. Dynamic thinking is enabled by default, and the knowledge cutoff is January 2026.

"3.5 Flash offers an incredible combination of quality and low latency," Koray Kavukcuoglu, DeepMind's chief technologist, told reporters ahead of the launch. "It outperforms our latest frontier model, 3.1 Pro, on nearly all the benchmarks." He added that Google had developed an optimized version that is not just four times but twelve times faster than other frontier models, specifically tuned for agentic workloads inside Google's Antigravity development platform.

## Agents, Not Chatbots

The strategic framing around 3.5 Flash is unmistakable. Google is positioning the model not as a better conversation partner but as an autonomous worker capable of executing multi-step workflows over hours with minimal human oversight. At I/O, Google engineer Varun Mohan demonstrated agents spawning subagents to independently build components of an operating system inside Antigravity 2.0, the company's newly released standalone desktop application for agent-first development.

Tulsee Doshi, Google's senior director and head of product, explained the division of labor planned for the upcoming 3.5 Pro model. "3.5 Pro becomes your orchestrator, your planner, and then it actually can leverage Flash to be the various sub-agents," Doshi told TechCrunch. "It really comes down to where do you really want that reasoning power versus where do you have tasks that really do merit good brute force tool use capabilities."

Enterprise partners are already integrating the model. Shopify is using 3.5 Flash subagents running in parallel to analyze merchant growth data at global scale. Macquarie Bank is piloting it for customer onboarding, reasoning over 100-plus-page compliance documents. Salesforce is integrating it into Agentforce for multi-turn enterprise automation. Ramp is using its multimodal capabilities for invoice processing, and Xero has deployed agents to manage multi-week workflows like 1099 tax form preparation.

Google CEO Sundar Pichai provided context for the internal adoption velocity during his keynote. Internal AI developer tools were processing half a trillion tokens per day in March; that figure has since grown to over three trillion tokens per day, doubling every few weeks. Across all Google surfaces, monthly token processing has reached 3.2 quadrillion -- a sevenfold year-over-year increase.

## Gemini Omni: Video Generation Meets World Understanding

The second major model announcement was Gemini Omni, a new family designed to generate output in any modality from any input. The first release, Gemini Omni Flash, accepts text, image, audio, and video input and outputs video grounded in real-world knowledge. Google described it as combining Gemini's reasoning intelligence with its generative media models, resulting in outputs that demonstrate understanding of physics and motion.

Omni Flash is available immediately in the Gemini app, Google Flow, and YouTube Shorts, with developer and enterprise API access coming in the weeks ahead. Image and text output modalities will follow over time.

## Why This Matters

Google's I/O announcements land at a moment when every major AI lab is racing to prove that large language models can do more than talk -- they can act. OpenAI has its Codex agent and operator tools. Anthropic has Claude's computer use capabilities. Microsoft has Copilot agents embedded across its enterprise stack. But Google is making a distinct bet: that the winning formula is not just a smart model but a smart model running inside a purpose-built agentic runtime, at a price point that makes sustained autonomous operation economically viable.

The pricing is particularly significant. Pichai noted during his keynote that many companies are already exhausting their annual token budgets by May. He argued that if enterprises shifted 80 percent of their workloads from other frontier models to 3.5 Flash, they could save over one billion dollars annually. Whether or not that figure holds up to scrutiny, the signal is clear: Google wants to be the default infrastructure for agentic AI at scale, and it is willing to undercut competitors aggressively to get there.

The Gemini Omni launch, meanwhile, opens a new front in the multimodal arms race. Video generation grounded in world understanding is a capability that neither OpenAI nor Anthropic currently offers natively through their flagship model APIs. If Omni's quality holds up in real-world use, it could give Google a meaningful differentiation point for creative and media applications.

## What to Watch Next

The immediate question is how 3.5 Flash performs in sustained, unsupervised agentic workflows outside of controlled demos. Google's enterprise partners are providing early signals, but the real test will come as developers push the model's limits in production. Watch for the release of Gemini 3.5 Pro next month, which is designed to serve as the orchestration layer that directs Flash subagents -- that pairing could define whether Google's agent architecture actually scales. The rollout of Gemini Spark, the consumer-facing personal agent built on 3.5 Flash, to AI Ultra subscribers at $100 per month will test whether ordinary users are ready to hand sustained autonomous tasks to an AI. And as Omni Flash reaches developer APIs, the question will be whether video generation grounded in world models is a genuine product capability or still a research demo dressed up for a keynote stage.
