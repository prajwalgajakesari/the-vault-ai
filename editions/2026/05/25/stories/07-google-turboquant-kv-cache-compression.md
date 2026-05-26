---
headline: "Google TurboQuant Achieves 6x KV Cache Compression With Zero Accuracy Loss"
slug: google-turboquant-kv-cache-compression
category: llms-genai
story_number: "07"
date: 2025-05-25
author: The Vault AI Staff
sources:
  - https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
  - https://nerdleveltech.com/google-turboquant-kv-cache-compression-llm-inference
  - https://vast.ai/article/turboquant-explained-llm-memory-inference
  - https://www.starkinsider.com/2026/03/google-turboquant-llm-compression-less-memory.html
  - https://arxiv.org/abs/2504.19874
---

# Google TurboQuant Achieves 6x KV Cache Compression With Zero Accuracy Loss

**The training-free algorithm squeezes LLM key-value caches down to 3 bits per coordinate, delivering up to 8x faster attention on H100 GPUs -- and the open-source community is already running with it.**

The most expensive part of running a large language model is not always the model itself. It is often the memory consumed by the key-value cache -- the running ledger of every previous token the model must consult each time it generates a new one. As context windows push past 128,000 tokens, that cache can devour tens of gigabytes of GPU memory, forcing inference providers into brutal tradeoffs between serving more users and supporting longer conversations.

Google Research has now published a compression algorithm that attacks this bottleneck head-on. TurboQuant, presented at ICLR 2026 in Rio de Janeiro, compresses the KV cache from 16-bit precision down to roughly 3 bits per coordinate -- a 6x reduction in memory -- with zero measurable accuracy loss on standard benchmarks. On NVIDIA H100 GPUs, the 4-bit variant delivers up to 8x speedup in attention logit computation compared to 32-bit unquantized keys.

The results are not incremental. They represent a step change in what is possible at inference time.

## How It Works: Rotation, Then Correction

TurboQuant is built from two companion techniques, each peer-reviewed at a top venue. The first, PolarQuant (accepted at AISTATS 2026), applies a random orthogonal rotation to each KV vector. This seemingly simple step has a profound effect: it spreads the energy of each vector uniformly across all coordinates, eliminating the outlier channels that have historically plagued low-bit quantization. Once rotated, every coordinate follows a predictable near-Gaussian distribution, allowing mathematically optimal Lloyd-Max quantization buckets to be computed from probability theory alone -- no calibration data, no model-specific tuning.

The second technique, Quantized Johnson-Lindenstrauss (QJL, published at AAAI 2025), spends just one additional bit per coordinate to correct residual error from the first stage. QJL acts as a mathematical error-checker that preserves the inner-product relationships between vectors -- the exact relationships on which attention scores depend.

"TurboQuant is more than just a practical engineering solution; it is a fundamental algorithmic contribution backed by strong theoretical proofs," wrote Amir Zandieh, Research Scientist, and Vahab Mirrokni, VP and Google Fellow, in the official Google Research blog post announcing the work. The team also noted that the method operates within a factor of approximately 2.7 of the information-theoretic limit for compression -- close to the best any algorithm could theoretically achieve.

Critically, the entire pipeline is data-oblivious: compute the rotation matrix once via QR decomposition, and it works on any transformer model without retraining or fine-tuning.

## The Numbers That Matter

Google evaluated TurboQuant on Llama-3.1-8B-Instruct, Gemma, and Mistral across five standard long-context benchmarks including LongBench, Needle-in-a-Haystack, ZeroSCROLLS, RULER, and L-Eval. At 3.5 bits per value on LongBench, TurboQuant scored 50.06 -- identical to the full-precision FP16 baseline. Even at an aggressive 2.5 bits, the score dropped only marginally to 49.44.

On needle-in-a-haystack retrieval tasks with context lengths up to 104,000 tokens, TurboQuant scored 0.997 at 4x compression -- functionally perfect. The algorithm also outperformed KIVI, the previous standard baseline for KV cache quantization published at ICML 2024, while being simpler to implement.

For vector search workloads, TurboQuant achieved superior recall ratios compared to state-of-the-art methods that relied on larger codebooks and dataset-specific tuning, confirming its robustness beyond the LLM inference use case.

## Why This Changes the Inference Cost Equation

The economics of LLM inference are straightforward: GPU memory is the binding constraint. A 6x reduction in KV cache memory means either serving six times more concurrent users on the same hardware, or extending context windows six times longer at the same concurrency. For cloud inference providers spending millions on H100 clusters, the savings are immediate and material.

As Vast.ai noted in its analysis of the breakthrough: "TurboQuant matters because it attacks one of the fastest-growing costs in long-context inference: the KV cache." The GPU cloud provider pointed out that workloads previously requiring premium high-VRAM instances could potentially run on cheaper hardware, directly lowering per-token costs.

The implications extend beyond the data center. Community developers have already built working implementations for llama.cpp, vLLM, and Apple Silicon via MLX -- all from the paper alone, since Google has not yet released official code. One llama.cpp implementation demonstrated a 104-billion parameter model running at 128,000-token context on a MacBook with just 74 GB peak memory. An independent developer built a PyTorch version with custom Triton kernels, reporting character-identical output to the uncompressed baseline at 2-bit precision.

## Market Shock and the Bigger Picture

The market took notice before the research community finished digesting the paper. When Google published its blog post on March 25, SK Hynix shares fell 6.23% and Samsung Electronics dropped 4.8% on the Korea Exchange the following day. U.S. memory stocks including Micron and SanDisk also sold off sharply. Analysts largely called the reaction an overreaction, noting that TurboQuant compresses inference-stage working memory only and offers no reduction in the massive memory requirements of model training.

Still, the broader signal is clear. The AI efficiency race -- doing more with less -- may prove as consequential as the parameter race. TurboQuant stacks cleanly on top of existing optimizations like PagedAttention for memory management, speculative decoding for latency, and weight quantization techniques like AWQ and GPTQ. Each layer compounds the savings.

## What to Watch Next

Google is expected to release official TurboQuant code around Q2 2026. The real question is adoption: whether vLLM, llama.cpp, and Ollama merge the technique into their mainline releases. Feature requests and pull requests are already open in all three projects. If TurboQuant becomes a default option in the open-source inference stack, it will quietly reshape what hardware is needed to run long-context AI -- from cloud clusters down to a single workstation in a small office.

The parameter race makes headlines. Compression makes deployment possible.