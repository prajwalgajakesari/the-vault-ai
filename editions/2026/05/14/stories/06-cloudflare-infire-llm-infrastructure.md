---
headline: "Cloudflare Builds Custom Infire Engine for Running LLMs Across Its Global Network"
slug: cloudflare-infire-llm-infrastructure
category: llms-genai
story_number: "06"
date: 2026-05-14
author: The Vault AI
tags: [cloudflare, infire, inference-engine, llm-infrastructure, workers-ai, gpu, rust]
---
# Cloudflare Builds Custom Infire Engine for Running LLMs Across Its Global Network

When you operate one of the largest edge networks on the planet and decide to run trillion-parameter language models on it, off-the-shelf inference software will not cut it.

Cloudflare has unveiled a sweeping set of infrastructure upgrades designed to host large open-source AI models across its global network, anchored by Infire, a proprietary inference engine written in Rust that the company says delivers up to 20 percent higher throughput than existing open-source alternatives. The announcement arrives at a pivotal moment for the San Francisco-based internet infrastructure giant, which just weeks ago cut 1,100 jobs, roughly 20 percent of its workforce, as CEO Matthew Prince declared that AI had "fundamentally changed" how the company operates.

The core technical insight behind Cloudflare's approach is a concept called disaggregated prefill. Every large language model request involves two distinct computational stages: prefill, which processes all incoming tokens and populates a key-value cache, and decode, which generates output tokens one at a time. Prefill is compute-bound, meaning it benefits from raw processing power. Decode is memory-bound, meaning it depends on how fast the system can shuttle data in and out of GPU memory. By routing each stage to hardware optimized for that specific workload, Cloudflare can extract significantly more performance from the same silicon.

"One hardware configuration that we use to improve performance and efficiency is disaggregated prefill," wrote Michelle Chen, principal product manager, Kevin Flansburg, senior engineering manager, and Vlad Krasnov, principal systems engineer, in a Cloudflare engineering blog post. "Prefill is usually compute bound, while decode is memory bound."

## Infire: A Rust-Powered Inference Engine

At the heart of the infrastructure push is Infire, first announced during Cloudflare Birthday Week in late 2025. Unlike widely used open-source inference engines such as vLLM, Infire was purpose-built for Cloudflare's unusual constraint: running AI models not in a centralized data center but across a distributed network spanning more than 330 cities worldwide.

Early benchmarks show Infire completing inference tasks up to 7 percent faster than vLLM 0.10.0 on unloaded machines equipped with an H100 NVL GPU. That margin may sound modest, but at Cloudflare's scale, where millions of requests flow through the network daily, even single-digit efficiency gains translate into substantial hardware cost savings. The company says the engine can begin serving requests for even the largest models in under 20 seconds, a critical metric for a platform that needs to spin up model instances dynamically in response to fluctuating demand.

Infire supports multi-GPU configurations in both pipeline-parallel and tensor-parallel modes, with expert-parallelism for mixture-of-experts architectures. The team described their optimization strategy in detail: "For pipeline parallelism, Infire attempts to properly load balance all stages of the pipeline, in order to prevent the GPUs of one stage from starving while other stages are executing," the engineers wrote. "For tensor parallelism, Infire optimizes for reducing cross-GPU communication, making it as fast as possible."

## Running Trillion-Parameter Models at the Edge

The stakes become concrete when looking at what Cloudflare is actually trying to run. Moonshot AI's Kimi K2.5, one of the first large models hosted on Workers AI, contains over one trillion parameters and weighs roughly 560 gigabytes. Loading it requires a minimum of eight Nvidia H100 GPUs just for the model weights, before accounting for the additional VRAM consumed by the KV cache during inference. Cloudflare has already tripled the speed of Kimi K2.5 since its initial deployment, and the model now supports a full 256,000-token context window with multi-turn tool calling, vision inputs, and structured outputs.

Memory optimization has been another focus area. The team reduced Infire's internal GPU memory overhead enough to run Meta's Llama 4 Scout on just two H200 GPUs while preserving substantial capacity for context tokens. That kind of memory efficiency determines how many concurrent users a single GPU cluster can serve, directly impacting unit economics.

Cloudflare also recently introduced Unweight, a lossless compression system that shrinks LLM weights by 15 to 22 percent without sacrificing accuracy. By reducing the volume of data GPUs need to load and transfer during inference, Unweight effectively lets the same hardware serve models faster.

## The Bigger Picture: Infrastructure Under Pressure

Cloudflare's infrastructure push comes against a backdrop of industry-wide growing pains. A recent Cockroach Labs report on the state of AI infrastructure found that many organizations are discovering their existing systems cannot handle the scale and reliability demands of production AI workloads. As the report noted, the challenge requires "a fundamental shift in how systems are architected," not just incremental performance upgrades.

For Cloudflare, the bet is that its globally distributed network, combined with custom inference technology, can offer something hyperscale cloud providers cannot: low-latency AI inference at the edge, close to end users rather than concentrated in a handful of massive data centers. The company's willingness to build Infire from scratch in Rust, rather than relying on community-maintained alternatives, signals the depth of that commitment.

The layoffs cast a long shadow over the announcement. Cloudflare reported record quarterly revenue of $639.8 million, up 34 percent year over year, but shares still plunged 24 percent after the workforce reduction was disclosed. The juxtaposition is stark: record revenue, aggressive AI investment, and mass layoffs all arriving in the same earnings cycle. It is a pattern becoming distressingly familiar across the tech industry, where AI-driven productivity gains and AI-driven job elimination are two sides of the same coin.

Whether Infire and disaggregated prefill can transform Cloudflare into a serious AI inference platform alongside the likes of AWS, Google Cloud, and Azure remains an open question. But the technical foundation is now in place, and with over a trillion parameters already running across its network, the company is no longer merely talking about its AI ambitions.
