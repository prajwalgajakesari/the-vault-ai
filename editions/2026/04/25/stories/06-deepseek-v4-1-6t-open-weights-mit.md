# DeepSeek Ships V4 With 1.6 Trillion Parameters and Open Weights Under MIT License

The largest open-weight language model ever released is now available for anyone to download, modify, and deploy commercially -- and it costs almost nothing to run. On April 24, 2026, Chinese AI lab DeepSeek published preview versions of DeepSeek-V4-Pro and DeepSeek-V4-Flash, a pair of mixture-of-experts models that land within striking distance of the world's most capable closed-source systems at a fraction of their price. Both ship under the MIT License.

## The Models

V4-Pro is the flagship: 1.6 trillion total parameters with 49 billion activated per token, pre-trained on 33 trillion tokens, and supporting a 1-million-token context window with up to 384,000 tokens of output. V4-Flash is the lightweight sibling at 284 billion total parameters and 13 billion active, sharing the same context length and feature set. Both models offer three reasoning effort modes (standard, think, and think-max), JSON output, tool calls, and fill-in-the-middle completion.

The architectural headline is a hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Hybrid Chunked Attention (HCA), which dramatically reduces memory consumption for long-context workloads. In the 1-million-token scenario, V4-Pro consumes only 27 percent of the single-token FLOPs and just 10 percent of the KV cache relative to the previous-generation V3.2. V4-Flash pushes those numbers down further to 10 percent of FLOPs and 7 percent of KV cache.

"DeepSeek's V4 preview is a serious flex," said Neil Shah, vice president of research at Counterpoint Research, in comments to CNBC. The efficiency gains are not merely academic -- they translate directly into the most aggressive API pricing in the industry.

## Benchmark Performance

DeepSeek's self-reported benchmarks place V4-Pro in direct competition with frontier closed-source models. On SWE-bench Verified, V4-Pro scores 80.6 percent -- within 0.2 percentage points of Anthropic's Claude Opus 4.6 and above every other publicly reported result. On Terminal-Bench 2.0, it takes the lead outright with 67.9 percent versus Claude Opus 4.6's 65.4 percent. In mathematics, V4-Pro achieves a perfect 120 out of 120 on Putnam-2025. On broader reasoning benchmarks, it posts 87.5 percent on MMLU-Pro, 90.1 percent on GPQA Diamond, and 92.6 percent on GSM8K.

V4-Flash is no slouch either, scoring 79.0 percent on SWE-bench Verified -- a 1.6-point gap behind its larger sibling, but competitive with models several times its active parameter count.

DeepSeek itself offers a frank self-assessment in the accompanying technical paper: "Through the expansion of reasoning tokens, DeepSeek-V4-Pro-Max demonstrates superior performance relative to GPT-5.2 and Gemini-3.0-Pro on standard reasoning benchmarks. Nevertheless, its performance falls marginally short of GPT-5.4 and Gemini-3.1-Pro, suggesting a developmental trajectory that trails state-of-the-art frontier models by approximately 3 to 6 months."

## The Price War

The pricing is where V4 threatens to reshape the competitive landscape. V4-Flash costs $0.14 per million input tokens and $0.28 per million output tokens -- cheaper than OpenAI's GPT-5.4 Nano. V4-Pro comes in at $1.74 input and $3.48 output, undercutting Gemini 3.1 Pro ($2/$12), GPT-5.4 ($2.50/$15), Claude Sonnet 4.6 ($3/$15), and Claude Opus 4.7 ($5/$25) by substantial margins. For organizations running large-scale inference workloads, the cost difference is not marginal -- it is transformational.

As Simon Willison noted on his blog: "DeepSeek-V4-Flash is the cheapest of the small models, beating even OpenAI's GPT-5.4 Nano. DeepSeek-V4-Pro is the cheapest of the larger frontier models."

## What This Means for Open-Source AI

V4-Pro is now the largest open-weight model available, surpassing Kimi K2.6 (1.1 trillion parameters), GLM-5.1 (754 billion), and more than doubling the size of DeepSeek's own V3.2 (685 billion). The MIT license imposes virtually no restrictions: anyone can download, fine-tune, and deploy these models commercially without seeking DeepSeek's permission.

The model weights are already available on Hugging Face -- Pro at 865GB, Flash at 160GB. The quantization community is expected to produce smaller versions rapidly. Willison noted he is "hoping that a lightly quantized Flash will run on my 128GB M5 MacBook Pro," suggesting that near-frontier performance may soon be accessible on consumer hardware.

The release arrives at a moment when Western AI labs are moving in the opposite direction on pricing. As The Decoder observed, agentic AI is pushing rivals to raise prices and cap usage, while DeepSeek ships a competitive model for almost nothing. That dynamic -- open weights, aggressive pricing, and near-frontier performance -- puts sustained pressure on the business models of OpenAI, Google, and Anthropic, all of which charge multiples of DeepSeek's rates for comparable capability.

## What to Watch

The V4 models are marked as previews, with a full release expected in the coming weeks. Independent benchmark verification will be critical -- DeepSeek's self-reported numbers are impressive but await third-party confirmation. The training infrastructure is also notable: reports indicate V4 was developed with support from Huawei's Ascend chips, potentially demonstrating a viable alternative to Nvidia hardware for frontier model training amid ongoing U.S. export controls. If confirmed, that development may prove as consequential as the model itself.
