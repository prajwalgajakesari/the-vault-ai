---
headline: "Cloudflare Builds Split-Architecture Infrastructure for Running LLMs at Global Scale"
slug: cloudflare-split-architecture-llm-inference
category: llms-genai
story_number: "13"
date: 2026-05-30
author: The Vault AI Edition
---

# Cloudflare Builds Split-Architecture Infrastructure for Running LLMs at Global Scale

When you ask a large language model to summarize a document or write a function, two very different computational tasks happen in sequence: first the model reads and digests every token you sent it, then it generates a response one token at a time. Most AI providers run both stages on the same hardware. Cloudflare has decided that is a waste of expensive silicon -- and has rebuilt its inference stack from the ground up to treat them as separate problems.

In an engineering deep-dive published during Agents Week 2026, Cloudflare detailed how its Workers AI platform now splits LLM processing into two disaggregated stages -- prefill and decode -- each handled by a different machine optimized for its specific workload. The result is a 3x improvement in inter-token latency and dramatically lower tail latency, achieved without adding a single GPU.

## Two Stages, Two Machines

The core insight is straightforward. Prefill -- the stage that ingests input tokens and populates the key-value (KV) cache -- is compute-bound, hammering the GPU's arithmetic units. Decode -- the stage that generates output tokens one by one -- is memory-bound, limited by how fast weights and cache entries can be shuttled to the processor. Running both on the same server means one stage always leaves hardware underutilized while the other runs.

Michelle Chen, principal product manager at Cloudflare, Kevin Flansburg, senior engineering manager, and Vlad Krasnov, principal systems engineer, explained the rationale in their blog post: "There are two stages to processing an LLM request: prefill, which processes the input tokens and populates the KV cache, and decode, which generates output tokens. Prefill is usually compute bound, while decode is memory bound."

By routing each stage to a dedicated server pool, Cloudflare can tune hardware configurations independently, scale prefill and decode capacity to match actual traffic patterns, and even run the two stages on entirely different GPU types. The company built a custom load balancer that estimates in-flight prefill and decode tokens across endpoint pools, rewrites streaming server-sent event responses to stitch cache metadata between stages, and spreads load evenly across heterogeneous hardware.

## Infire: A Rust-Based Inference Engine

Powering this split architecture is Infire, a proprietary inference engine Cloudflare first announced during Birthday Week 2025. Written in Rust rather than Python, Infire was built specifically for the constraints of Cloudflare's distributed global network -- thousands of locations, each sharing GPUs among multiple services, with strict security requirements that previously forced the company to run the open-source vLLM engine inside a gvisor sandbox at significant performance cost.

The engineering team described Infire's approach to multi-GPU coordination: "For pipeline parallelism, Infire attempts to properly load balance all stages of the pipeline, in order to prevent the GPUs of one stage from starving while other stages are executing. On the other hand, for tensor parallelism, Infire optimizes for reducing cross-GPU communication, making it as fast as possible."

The numbers tell the story. Infire can boot Kimi K2.5 -- a model with over one trillion parameters requiring roughly 560 GB of weight storage -- on eight H100 GPUs with more than 30 GB still available for KV cache. It runs Llama 4 Scout on just two H200 GPUs with capacity for over 1.2 million context tokens. Cold-start times for even the largest models clock in under 20 seconds. Under synthetic benchmarks, Infire delivers up to 7 percent faster inference than vLLM on unloaded machines while consuming roughly one-sixth the CPU resources -- a critical advantage on edge nodes where GPU servers share silicon with Cloudflare's other services.

## Compressing What Cannot Be Cut

Alongside the architectural changes, Cloudflare introduced Unweight, a tensor compression system that shrinks model weights by 15 to 22 percent without measurable accuracy loss. By reducing the sheer volume of data GPUs need to load and move during inference, Unweight lets models run faster on hardware that would otherwise be too constrained. Combined with speculative decoding -- where a smaller draft model proposes candidate tokens that the full model validates in a single forward pass -- the stack squeezes throughput from every available cycle.

## Security at Scale: The Glasswing Connection

Cloudflare's infrastructure ambitions extend beyond performance. As one of approximately 50 partners in Anthropic's Project Glasswing -- a collaborative effort to harden critical software using Claude Mythos Preview -- Cloudflare turned the model loose on its own critical-path systems. The results were striking: 2,000 bugs discovered, 400 of which were rated high- or critical-severity, with a false-positive rate that Cloudflare's security team assessed as better than human testers. The findings underscore a broader theme: the same companies building infrastructure to serve AI models are simultaneously using those models to secure the infrastructure itself.

## The Edge Advantage

What distinguishes Cloudflare's approach from hyperscaler GPU farms is geographic distribution. Workers AI runs on a network that operates within 50 milliseconds of 95 percent of the world's internet-connected population. For agentic AI workloads -- where a single user interaction may trigger dozens of sequential model calls, tool invocations, and MCP requests -- that proximity translates directly into user-perceived speed. The company reports that Workers AI saw 4,000 percent year-over-year growth in inference requests as of early 2026, driven largely by developers building latency-sensitive agent applications that cannot tolerate round trips to centralized data centers.

## What to Watch

Cloudflare is betting that the future of AI inference looks less like renting time on a massive GPU cluster and more like running models at the same network edge where web traffic already terminates. The split-architecture approach, purpose-built inference engine, and weight compression represent a coherent technical thesis: that software engineering discipline can substitute for brute-force hardware spending. Whether that thesis holds as models continue to grow -- and as competitors like AWS, Google Cloud, and a fleet of specialized inference startups pursue their own optimizations -- will determine whether Cloudflare's connectivity cloud becomes a serious contender in the rapidly consolidating AI infrastructure market. For now, the engineering is compelling, and the growth curve suggests developers are paying attention.
