# Cloudflare Builds High Performance Multi-GPU LLM Infrastructure With Custom Infire Engine

When Cloudflare's engineers looked at the numbers, the math was unambiguous: running Python-based inference at the network edge was burning CPU cycles they could not afford to waste. The answer was Infire — a Rust-written LLM inference engine purpose-built for a company that operates within 50 milliseconds of 95% of the world's internet-connected population and cannot simply throw more GPUs at the problem.

Infire is now powering some of the largest open-weight models available on Cloudflare's Workers AI platform, including Moonshot AI's one-trillion-parameter Kimi K2.5 and Meta's Llama 4 Scout, after the company extended the engine with full multi-GPU support in April 2026. The move marks a significant step in Cloudflare's push to compete with hyperscalers on AI inference — and to do it from the edge rather than a centralized data center.

## The Case Against vLLM at the Edge

Cloudflare had been running most of its models on vLLM, the widely used open-source inference engine. On paper, vLLM is excellent: battle-tested, broadly compatible, and continuously improving. In practice, it was a poor fit for Cloudflare's operating model.

The core issue was security. Cloudflare could not trust a third-party Python process to run alongside other services without strong sandboxing, which meant routing vLLM through gVisor. The overhead compounded quickly: under full production load, vLLM through gVisor consumed as much as 2.5 CPU cores, competing directly with latency-sensitive services on the same machine. When CPU resources were constrained to simulate realistic edge conditions, throughput dropped sharply.

"Although it can run on a very wide range of hardware, from personal devices to data centers, it is best optimized for large data centers," the Cloudflare engineering team wrote of vLLM. "It is much less optimized for dynamic workloads, distributed networks, and for the unique security constraints of running inference at the edge."

The team also needed features vLLM did not support: co-hosting multiple models on the same GPU, dynamic model scheduling, and tight integration with proprietary in-house research.

## What Infire Does Differently

Infire is written in Rust — Cloudflare's preferred language for new infrastructure — and designed to run as a trusted bare-metal process rather than inside a sandbox. The engine is composed of three major components: an OpenAI-compatible HTTP server built on the high-performance Hyper crate, a batcher, and the core inference engine.

Against vLLM 0.10.0 on an unloaded H100 NVL, Infire is 7% faster end-to-end — 40.91 versus 38.38 requests per second, 17,224 versus 16,164 tokens per second. CPU load tells the more dramatic story: vLLM bare metal drew 140% of a CPU core; Infire drew 25%. Under the gVisor-plus-CPU-constraint scenario approximating real production conditions, vLLM managed only 9,279 tokens per second — less than half of Infire's output.

The efficiency gains come from several design choices. Infire just-in-time compiles CUDA kernels for the specific model it is running, optimizing for that model's hidden state size, dictionary size, and target GPU architecture. It creates a dedicated CUDA graph for every possible batch size, cutting CPU overhead by 82% compared to standard sequential kernel launches. Startup time for Llama 3.1 8B from disk is under four seconds.

## Scaling to Multi-GPU: Pipeline, Tensor, and Expert Parallelism

When Cloudflare expanded Workers AI to include frontier-scale models, Infire had to grow. Kimi K2.5 has over one trillion parameters and approximately 560 GB of model weights — requiring at least eight H100 GPUs just to load into memory, before any KV cache or context window overhead is accounted for.

The team added three forms of parallelism. Pipeline parallelism splits the model across GPUs sequentially and load-balances stages. Tensor parallelism splits layer computations across GPUs while minimizing cross-GPU communication. Expert parallelism handles mixture-of-experts architectures. For most large models, Cloudflare runs pipeline and tensor parallelism together.

"For pipeline parallelism, Infire attempts to properly load balance all stages of the pipeline, in order to prevent the GPUs of one stage from starving while other stages are executing," wrote principal product manager Michelle Chen, senior engineering manager Kevin Flansburg, and principal systems engineer Vlad Krasnov. "For tensor parallelism, Infire optimizes for reducing cross-GPU communication, making it as fast as possible."

The memory efficiency gains are striking. Infire runs Llama 4 Scout on just two H200 GPUs with more than 56 GiB remaining for KV cache — sufficient for over 1.2 million context tokens. Kimi K2.5 runs on eight H100 GPUs with more than 30 GiB still available. Cloudflare's engineers note vLLM would struggle to boot in either configuration. On unconstrained systems, multi-GPU Infire delivers up to 20% higher tokens-per-second throughput, and cold-starts for even the largest models complete in under 20 seconds.

## Prefill-Decode Disaggregation: Splitting the Pipeline

Alongside Infire, Cloudflare built an infrastructure layer that splits LLM processing into two stages on separate machines. The prefill stage handles input tokens and KV cache population — compute-bound work. The decode stage generates output tokens and is memory-bound. A token-aware load balancer routes traffic across a pool of prefill and decode endpoints and rewrites streaming responses on the fly.

The impact was measurable: p90 inter-token latency dropped from roughly 100 milliseconds with high variance to a stable 20 to 30 milliseconds — a threefold gain while request volume was simultaneously rising, using the same GPU count. Kimi K2.5 is now 3x faster than at its initial launch.

## Why This Matters

The broader implication is that edge-native LLM inference at frontier scale is now technically feasible. The assumption across most of the industry has been that running trillion-parameter models requires centralized, purpose-built data center clusters. Cloudflare is doing it on eight H100 GPUs distributed across its network.

The cost stakes are real. Cloudflare's internal security review agent processes more than seven billion tokens per day using Kimi K2.5. Running the same workload on a mid-tier proprietary model would cost an estimated $2.4 million annually; Kimi K2.5 on Workers AI cuts that figure by 77%.

Cloudflare describes the current Infire deployment as a first iteration. Flash Attention 3 integration is pending and most kernels do not yet use fusion — both will unlock further speed. Quantization and true multi-tenancy are on the roadmap. The engine already powers Llama 3.1 8B on Workers AI today, with larger model support expanding.

The Rust-based stack is a direct challenge to the assumption that production AI inference must be built on Python. Cloudflare is betting it does not — and the early benchmark numbers suggest that bet is paying off.
