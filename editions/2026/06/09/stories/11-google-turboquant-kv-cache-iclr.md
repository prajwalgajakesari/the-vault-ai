---
headline: "Google’s TurboQuant Slashes LLM Memory Overhead at ICLR 2026"
slug: google-turboquant-kv-cache-iclr
category: research
story_number: 11
date: 2026-06-09
---

# Google’s TurboQuant Slashes LLM Memory Overhead at ICLR 2026

Every time a large language model generates a token, it silently accumulates a bill. Not a dollar bill — a memory bill. Key-value pairs for every prior token, across every attention layer, pile up in GPU RAM at full 16-bit precision. At 128,000 tokens on a Llama 3 70B model, that bill comes to roughly 40 GB of high-bandwidth memory — the entire capacity of an NVIDIA A100 40GB — before a single model weight is even loaded. Google Research believes it has found a way to cut that bill by as much as six times, and the math is hard to argue with.

The algorithm is called TurboQuant. Presented as a poster at ICLR 2026 in Rio de Janeiro on April 25 and published in the conference proceedings under the title “TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate,” it compresses KV-cache entries from 16-bit floating-point precision down to as few as 3 bits per coordinate — with benchmark scores that are, in several cases, indistinguishable from the uncompressed baseline. The paper’s authors are Amir Zandieh and Vahab Mirrokni of Google Research, alongside Majid Daliri of New York University and Majid Hadian of Google DeepMind.

## The Two-Step Squeeze

TurboQuant’s compression pipeline has two named stages. The first is PolarQuant. Before any quantization happens, each KV vector is multiplied by a random orthogonal rotation matrix — generated once via QR decomposition of a random Gaussian matrix and reused across all vectors. The rotation does not change the vector’s mathematical meaning; it scrambles the coordinate representation so that energy, previously concentrated in a handful of “outlier” dimensions that confound simple quantizers, is spread uniformly across all coordinates. The resulting distribution is approximately Gaussian and analytically predictable.

Because the post-rotation distribution is known in advance, TurboQuant can apply Lloyd-Max quantization — a classical algorithm that places quantization buckets at information-theoretically optimal positions for a Gaussian input. The paper notes that TurboQuant operates within a factor of approximately 2.7 of the information-theoretic compression limit, a bound the authors describe as “near-optimal.” The method requires no calibration data, no model fine-tuning, and no per-layer profiling. It is, according to coverage of the paper, “data-oblivious” and “model-agnostic.”

The second stage is the Quantized Johnson-Lindenstrauss transform, or QJL. After PolarQuant compresses each vector, QJL adds a single corrective bit per coordinate derived from a random projection. This bit preserves inner-product relationships between keys and queries — the core operation of attention — ensuring that the attention pattern remains faithful to the original even at extreme compression ratios. The combination gives TurboQuant what the paper claims is an unbiased estimator of attention scores at 3-bit precision.

The “Polar” in PolarQuant, incidentally, refers to an internal coordinate conversion: the quantization stage represents each value in polar form (radius and angle) rather than Cartesian coordinates, eliminating the per-block normalization overhead that traditional quantizers require.

## What the Benchmarks Show

The numbers are striking. On LongBench, a long-document QA and summarization suite, Llama-3.1-8B-Instruct at 3.5 bits with TurboQuant scored 50.06 — identical to the FP16 baseline of 50.06. Even at an aggressive 2.5 bits, the score degraded only to 49.44. On Needle-in-a-Haystack, a test of verbatim recall across contexts up to 104,000 tokens, the algorithm scored 0.997 at 4x compression — functionally the same as full precision.

On NVIDIA H100 GPUs, 4-bit TurboQuant delivered up to 8x acceleration in attention logit computation compared to 32-bit unquantized keys — or roughly 4x versus the FP16 baseline used in most production deployments. That figure covers the attention kernel specifically, not end-to-end inference latency, so real-world wall-clock gains will be lower. According to reporting by Nerd Level Tech, the compression ratio at 3 bits (TQ3) reaches 4.9x versus FP16, with each 128-value vector shrinking from 256 bytes to 52 bytes, and a mean squared error of just 0.034.

Compared with KIVI — the 2-bit asymmetric quantization scheme presented at ICML 2024 that serves as the field’s standard baseline — TurboQuant matches or outperforms on LongBench at equivalent bit budgets while being simpler to implement: no per-channel or per-token calibration required.

The market noticed. When Google published the research blog on March 25, 2026, SK Hynix fell 6.23% and Samsung Electronics dropped 4.8% on the Korea Exchange the following session. U.S. memory stocks followed: Micron shed roughly 5%, SanDisk fell as much as 8%. The implicit investor thesis was that cheaper inference memory would dampen demand for high-bandwidth DRAM. Analysts largely pushed back. The selloff, Lynx Equity Strategies argued, conflated inference-time working memory — TurboQuant’s only target — with the far larger memory volumes consumed by model training, which TurboQuant does not touch.

## Why It Matters

KV-cache memory is the dominant bottleneck in long-context LLM inference, and the problem only worsens as context windows expand. At 128K tokens, KV storage already exceeds weight memory on many popular models; at 1 million tokens on Llama 70B, the KV cache alone can approach 135 GB at FP16. Inference providers today face a hard tradeoff: extend context length or serve more concurrent users, but not both. TurboQuant dissolves that tradeoff — at least in theory. A 6x reduction in KV memory translates directly into either 6x more concurrent sessions on the same cluster, or 6x longer effective context at constant cost.

The broader significance is what TurboQuant represents about the current direction of AI research. The era in which performance scaled reliably with parameter count and raw GPU hours has given way to an “efficiency-first” moment. Techniques like speculative decoding, PagedAttention, mixture-of-experts sparsity, and now TurboQuant-style KV compression are compounding to push inference costs toward commoditization. For on-device deployment, the gains are especially meaningful: early community implementations of TurboQuant for llama.cpp have already demonstrated a 104-billion-parameter model running at 128,000-token context on an Apple Silicon MacBook at 74 GB peak memory.

TurboQuant is also notable for what it does not require. No retraining. No calibration dataset. No gradient computation. The algorithm drops into any pre-trained transformer architecture unchanged. That universality matters: it means efficiency gains can propagate retroactively to already-deployed models without the cost and latency of retraining pipelines.

The paper frames its compression guarantee in information-theoretic terms: TurboQuant operates within a factor of approximately 2.7 of the Shannon limit for KV vectors with a Gaussian distribution. The authors describe the algorithm as achieving “near-optimal distortion rate” — meaning there is limited room for future work to close the gap further without fundamentally changing the problem formulation.

## What to Watch

Google had not released official TurboQuant code as of early April 2026, with the community moving faster than the lab; implementations in PyTorch, Rust, and llama.cpp are already available on GitHub. An official release was expected in Q2 2026. Integration into production inference stacks — vLLM, TensorRT-LLM, and Apple’s MLX — will determine how quickly the paper’s numbers translate into real-world serving costs. Watch also for whether TurboQuant’s principles extend to weight quantization or training-time compression, which would represent a substantially larger efficiency leap. And watch memory chip earnings: the next cycle of HBM procurement decisions, made with TurboQuant’s inference gains now priced into engineering roadmaps, will reveal how much of the market selloff was overreaction and how much was a genuine signal about long-run memory demand.

*Technical claims in this article are attributed to the TurboQuant paper (Zandieh et al., ICLR 2026), the Google Research blog, and reporting by Nerd Level Tech and Tom’s Hardware. Benchmark figures are as reported in those sources and should be treated as paper-reported results pending independent reproduction.*
