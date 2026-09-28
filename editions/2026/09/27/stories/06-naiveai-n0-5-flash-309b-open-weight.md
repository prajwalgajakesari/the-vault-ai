# NaiveAI Open-Sources Naive-N0.5-Flash, a 309B MoE Built for Coding at 2,000 Tokens per Second

A week after reports that Tencent and a group of top Chinese investors had valued it at $1.42 billion before it shipped anything, Beijing startup NaiveAI has put its first real product on the table. On September 27 the lab released Naive-N0.5-Flash, an open-weight 309-billion-parameter mixture-of-experts model with 15.5 billion parameters active per token. It targets coding and AI research work, supports a native 1-million-token context window, and ships under the permissive MIT license. The release also answers the question the Vault raised last week: which open base model NaiveAI chose to build on. The answer is Xiaomi's MiMo-V2.5.

The company's pitch goes beyond the weights. NaiveAI says AI systems did much of the research and engineering behind the model, and its model card carries the tagline "Building Frontier AI with AI." According to the company's technical write-up, as summarized by RuntimeWire, models wrote code, ran experiments, monitored results and proposed iterations, while human researchers set objectives, constraints and evaluation standards and made the key decisions.

## A long-context model with no full attention

The most distinctive engineering choice is what the model leaves out. Naive-N0.5-Flash has no full-attention layers. Its 48 transformer layers are arranged as eight six-layer modules, each pairing five Sliding-Window Attention layers with one DeepSeek Sparse Attention layer, for a total of 39 SWA and 9 DSA layers. The sliding window covers just 128 tokens, while the sparse layers select the top 2,048 tokens from the full history for backbone attention. NaiveAI also replaced the multi-head latent attention used in DeepSeek's original sparse-attention design with grouped-query attention using four KV groups.

"The entire network remains local or sparse, with no full-attention layers," the model card states. The company explains that in the MiMo base, a small number of global-attention layers "account for much of the decoding overhead" at million-token lengths, which is why it swapped them for sparse attention. The card is candid about the limits of that trade: the sparse indexer still scans the full history, and the full key-value cache is still retained.

To adapt the base to the new structure, NaiveAI ran 3.25 trillion tokens of multi-stage training at native 1M context. That breaks down into a 50-billion-token indexer warmup, 3 trillion tokens of sparse-attention training and a 200-billion-token learning-rate decay. The acknowledgments credit Xiaomi's MiMo team, DeepSeek's sparse-attention work and the SGLang inference community.

## The 2,000 tokens-per-second claim

The speed headline comes from NaiveRT, an inference system the company says was "built and optimized through AI-centered R&D." It combines mega-kernel fusion, Programmatic Dependent Launch and speculative decoding. The model card promises 50 tokens per second per user in Standard mode and up to 2,000 tokens per second in Ultrafast mode.

The conditions behind that number deserve attention. RuntimeWire reported that the company's longer write-up cites a peak of 2,122 tokens per second on eight GPUs in a single-stream test, taken from the best one-second window across 41 HTML and SVG generation requests, and excluding prompt processing. "NaiveAI's headline speed figure needs its test conditions attached," wrote RuntimeWire's Ryan Merket. The company also reports a full speculative-decoding cycle of 3.4 milliseconds, against 12.3 milliseconds for SGLang on the same system.

Running the model yourself is not a hobbyist project. The weights occupy about 315 GB and require FP8-capable NVIDIA GPUs. For everyone else, NaiveAI lists API pricing of $0.10 per million input tokens, $0.40 per million output tokens and $0.01 per million cached reads. RuntimeWire noted that the Chinese write-up lists yuan prices of 0.60, 2.60 and 0.07 per million tokens.

On capability, the model card charts results across seven coding and agentic tasks, including SWE-Bench Pro, Terminal-Bench 2.1 and DeepSWE, and across AI R&D evaluations such as PostTrainBench, MLE-bench-30, PaperBench and NanoGPT SpeedRun. It compares the model with GLM-5.3, Kimi-K3, Qwen-3.8-Max, DeepSeek-V4.1-Flash and several closed frontier systems. All evaluations were run by NaiveAI in a Claude Code harness limited to basic file and Bash tools, and none have been independently reproduced.

## Why It Matters

Last week's coverage framed NaiveAI as the purest bet on the idea that the most valuable work in AI now happens after pretraining. Naive-N0.5-Flash is the first test of that thesis, and it is a more ambitious one than a simple fine-tune. NaiveAI did not just apply reinforcement learning to Xiaomi's base. It removed the base's global attention, grafted on DeepSeek's sparse mechanism and retrained on trillions of tokens. If the long-context quality holds up, that shows a lab with fewer than 100 people can do substantial architectural work on someone else's pretrained model and ship it back to the community under MIT terms.

The pricing matters as much as the architecture. At $0.40 per million output tokens, with 15.5 billion active parameters and a sparse attention stack designed to keep million-token decoding cheap, the model is aimed directly at agentic coding workloads, where long context and heavy output volume quickly drive up bills on closed models. The "AI built this" story is harder to judge. As RuntimeWire pointed out, NaiveAI has not said how it measured AI's contribution or whether the approach actually lowers development costs.

## What to Watch

Independent benchmarking comes first. Teams will want to know whether a stack with no full attention can really retrieve and reason across a million tokens, and whether the 2,000 tokens-per-second figure holds up on ordinary coding workloads rather than HTML and SVG generation. Watch for third-party inference providers adding the model; at release, Hugging Face listed none. Also watch whether NaiveAI publishes enough detail on its AI-driven research process for outsiders to evaluate it, and whether the unresolved MiroMind dispute over founder Dai Jifeng resurfaces now that the lab has a product in the market. With a $1.42 billion valuation to justify, the "N0.5" name makes clear that NaiveAI considers this a first step, not the finished product.
