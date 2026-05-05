---
headline: "Cloudflare Builds Infire Inference Engine to Run Large Language Models at the Edge"
slug: cloudflare-infire-inference-engine-edge-llm
category: llms-genai
story_number: "10"
date: 2026-05-04
---

# Cloudflare Builds Infire Inference Engine to Run Large Language Models at the Edge

Running a large language model is expensive. Running one across a globally distributed edge network -- where every millisecond of latency and every megabyte of memory matters -- is a different kind of engineering problem entirely. Cloudflare has spent the past year attacking it head-on, building a custom inference engine called Infire from the ground up in Rust and rearchitecting how its Workers AI platform processes requests at every layer of the stack. The results, disclosed in a pair of technical blog posts published in April 2026, reveal a company that has essentially rejected the standard open-source inference toolkit in favor of a purpose-built system tuned to the realities of serving AI at the network edge.

## Why Cloudflare Walked Away from vLLM

Most companies running LLM inference at scale rely on vLLM, the widely adopted open-source serving engine that has become something of an industry default. Cloudflare used it too -- until it became clear that the framework's general-purpose design was a poor fit for the company's highly distributed, security-constrained environment.

"Infire completes inference tasks faster and with a fraction of the CPU load of our previous vLLM-based setup, especially under the strict security constraints we require," the company wrote in its engineering blog. The decision to build from scratch was not taken lightly, but Cloudflare's requirements -- running models across hundreds of edge locations on heterogeneous hardware, maintaining strict tenant isolation, and minimizing cold-start times -- demanded it.

Infire is composed of three major components: an OpenAI-compatible HTTP server, a batcher that groups incoming requests for efficient GPU utilization, and the Infire engine itself. Written entirely in Rust, the system supports multi-GPU inference in pipeline-parallel, tensor-parallel, and expert-parallel modes -- the last of which is critical for efficiently serving Mixture-of-Experts architectures like DeepSeek and Kimi K2.5.

## Splitting the Brain: Prefill-Decode Disaggregation

Perhaps the most consequential architectural decision Cloudflare made was separating the two internal phases of LLM inference -- prefill and decode -- onto entirely different server clusters.

In a standard LLM serving setup, the same GPU handles both phases: first processing all input tokens to build a key-value (KV) cache (the prefill phase), then generating output tokens one at a time (the decode phase). The problem is that these two jobs have fundamentally different hardware profiles. Prefill is compute-bound, demanding raw floating-point throughput. Decode is memory-bound, limited by how fast the GPU can read from its KV cache.

By running separate, independently tuned server pools for each phase, Cloudflare achieved dramatic improvements. After shifting traffic to the disaggregated architecture, p90 time per token dropped from approximately 100 milliseconds with high variance to 20-30 milliseconds -- a 3x improvement in intertoken latency, achieved on the same quantity of GPUs.

"This architecture allows the servers to be tuned independently for the role they are performing, scaled to account for more input-heavy or output-heavy traffic, or even to run on heterogeneous hardware," Cloudflare explained. The company uses RDMA (Remote Direct Memory Access) to transfer KV cache data directly between GPUs over the network, bypassing the CPU entirely and eliminating a major bottleneck in cross-server inference.

## Smarter Caching, Faster Boot Times

Cloudflare also overhauled its input token caching strategy. By working with heavy internal users to adopt a header that signals how much of a prompt is reusable, the company increased its input token cache hit ratio from 60% to 80% during peak times -- a gain that translates directly into higher throughput and lower latency for interactive workloads like AI-assisted coding sessions.

Boot times received similar attention. Even for the largest models, such as the 236-billion-parameter Kimi K2.5, Infire can begin serving requests in under 20 seconds, with load times bounded only by drive speed. On unconstrained systems, the proprietary engine delivers up to 20% higher tokens-per-second throughput compared to the previous stack, and critically, it enables Cloudflare to run frontier-class models on lower-end hardware where inference was previously infeasible.

## Compressing Models Without Losing a Bit

Alongside Infire, Cloudflare published research on Unweight, a lossless compression system for LLM weight tensors. By separating each BF16 value into its sign-plus-mantissa and exponent components and applying Huffman coding, Unweight achieves 15-22% reductions in model size -- roughly 3 GB of VRAM savings on a model like Llama 3.1 8B -- without any loss of output quality.

The engineering challenge was making decompression fast enough to avoid slowing down inference. Unweight solves this by decompressing weights directly in fast on-chip shared memory and feeding results straight to the tensor cores, using an autotuner that optimizes the decompression pipeline for each model and hardware configuration. The system targets NVIDIA Hopper GPUs (H100, H200), with kernel source code released on GitHub.

## The Bigger Picture

Cloudflare's infrastructure push positions the company as one of the few non-hyperscaler platforms capable of serving frontier-class LLMs, and the only one attempting to do so across a globally distributed edge network. The combination of Infire, prefill-decode disaggregation, aggressive caching, and lossless weight compression represents a vertically integrated inference stack that rivals what companies like Google and Meta have built internally.

For developers building AI-powered applications on Workers AI, the implications are practical: access to models like Kimi K2.5 through a single API call, with latency and cost characteristics that were previously available only to teams running their own GPU clusters. For the broader industry, Cloudflare's work demonstrates that the gap between centralized cloud inference and distributed edge inference is closing faster than many expected -- and that the tools to close it may need to be built from scratch.
