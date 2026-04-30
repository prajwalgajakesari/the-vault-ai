# Cloudflare Builds Foundation for Running Extra-Large Language Models at the Edge

Cloudflare is laying the technical groundwork to run the largest open-source language models directly on its global edge network, unveiling a suite of infrastructure optimizations during Agents Week 2026 that collectively represent the company's most aggressive push yet into AI inference. The announcements, spanning a custom Rust-based inference engine, a novel model compression system, and support for frontier-scale models like Moonshot's Kimi K2.5, signal that the race to host large language models is no longer confined to centralized cloud data centers.

The centerpiece of Cloudflare's technical strategy is Infire, a proprietary LLM inference engine written in Rust and purpose-built for the unique constraints of distributed edge computing. Unlike centralized inference platforms that can rely on massive GPU clusters in a handful of data centers, Cloudflare must serve AI workloads across more than 200 cities worldwide, which means every watt of GPU power and every megabyte of memory bandwidth matters. According to the company's engineering team, Infire uses Granular CUDA Graphs to reduce CPU overhead by 82 percent and achieves GPU utilization rates above 80 percent under production loads. On unloaded machines equipped with H100 NVL GPUs, Infire completes inference tasks up to 7 percent faster than vLLM 0.10.0, the widely used open-source serving framework.

"We are entering a world where agents are the ones writing and executing code," CEO Matthew Prince said during Agents Week, framing the LLM infrastructure push as inseparable from the broader rise of autonomous AI agents. "Agents need a home that is secure by default, scales to millions instantly, and persists across long-running tasks."

## The Three Pillars of Edge-Scale Inference

Cloudflare's approach rests on three interlocking technical innovations that address the fundamental bottlenecks of running large models far from centralized GPU farms.

First, the Infire engine handles the core challenge of maximizing throughput on limited hardware. By implementing disaggregated prefill, which separates the compute-intensive prompt processing stage from the latency-sensitive token generation stage, Infire can pipeline work more efficiently across available GPUs. For the largest models, such as Kimi K2.5, the engine can begin serving requests in under 20 seconds and supports multi-GPU configurations necessary for models that exceed a single GPU's memory capacity.

Second, Cloudflare developed Unweight, a lossless inference-time compression system that reduces model weight footprints by 15 to 22 percent without sacrificing bit-exact output quality. For a model like Kimi K2.5, that translates to roughly 3 GB of VRAM savings per GPU, a meaningful margin on hardware where every gigabyte determines whether a model fits in memory or requires an additional card. Critically, Unweight operates without specialized hardware, meaning it can be deployed across Cloudflare's heterogeneous GPU fleet.

Third, speculative decoding accelerates token generation by pairing a smaller draft model with the target model. The draft model generates candidate tokens cheaply, and the larger model validates them in a single forward pass rather than generating each token sequentially. The Cloudflare engineering team noted that this technique is "particularly effective in agentic use cases because of the volume of tool calls and structured outputs" that agents must produce, where predictable patterns in function signatures and JSON schemas give the draft model high acceptance rates.

## Prefix Caching and the Economics of Agents

Beyond raw speed, Cloudflare is optimizing for the distinct economics of agentic workloads. In multi-turn agent conversations, the same system prompt and tool definitions are sent with every request, creating enormous redundancy in computation. Workers AI now implements prefix caching, storing computed input tensors from the prefill stage so that subsequent requests sharing the same prefix skip recomputation entirely.

The company has surfaced prefix cache hit rates as a usage metric and introduced discounted pricing for cached tokens, a pricing model that directly incentivizes developers to structure their agent architectures for cache efficiency. For agents making thousands of sequential API calls, the compound savings on both latency and cost could be substantial.

Workers AI now supports over 70 models spanning 12 providers through a unified inference layer, with Kimi K2.5 as the headline addition. Cloudflare reports making the model 3x faster than baseline through the combined application of Infire, Unweight, and speculative decoding. The platform maintains an OpenAI-compatible API, lowering the barrier for developers already building on the dominant inference interface.

## The Broader Edge AI Race

Cloudflare's infrastructure play arrives as the edge AI inference market enters a pivotal phase. Traditional cloud providers, including AWS, Google Cloud, and Azure, have invested heavily in centralized GPU capacity, but face inherent latency penalties for globally distributed workloads. Cloudflare's bet is that as AI agents proliferate and make orders of magnitude more requests than human users, the latency and cost advantages of edge inference will become decisive.

Prince has championed the narrative of the "Agentic Internet," arguing that while a human might visit five websites to complete a task, an autonomous AI agent might make 5,000 requests to perform the same function. If that prediction holds, the infrastructure layer that can handle massive request volumes with minimal latency will capture an outsized share of the emerging agent economy.

The competitive landscape is intensifying. Fastly, Vercel, and Deno have all expanded their edge AI capabilities in recent months, though none match Cloudflare's scale of 200-plus cities. Meanwhile, dedicated inference providers like Fireworks AI, Together AI, and Groq continue to push the frontier on raw throughput, albeit from centralized locations.

## What to Watch

The critical question is whether Cloudflare can expand its large model catalog fast enough to matter. Running Kimi K2.5 is a proof of concept; running a half-dozen frontier models with consistent performance across a global network is an engineering challenge of a different order. Watch for announcements on additional large model support, multi-modal inference capabilities, and enterprise pricing tiers that could signal Cloudflare's transition from infrastructure experiment to production-grade AI platform.
