---
headline: "MiniMax M3 Claims Frontier Coding Crown With Open-Weight Model and Million-Token Context"
slug: minimax-m3-open-weight-frontier-coding
category: llms-genai
story_number: 7
date: 2026-06-04
---

# MiniMax M3 Claims Frontier Coding Crown With Open-Weight Model and Million-Token Context

Shanghai-based AI lab MiniMax launched its M3 foundation model on June 1, making what may be the most ambitious claim in the open-weight AI race this year: that a single model can match proprietary giants on coding benchmarks, process one million tokens of context, and handle native multimodal input -- all while costing developers a fraction of what closed competitors charge.

The numbers, if they hold up under independent scrutiny, are striking. MiniMax reports that M3 scored 59.0% on SWE-Bench Pro, the demanding software engineering benchmark built around 1,865 real pull requests from 41 actively maintained open-source repositories. That edges past OpenAI's GPT-5.5 at 58.6% and Google's Gemini 3.1 Pro at 54.2%, though it trails Anthropic's Claude Opus 4.8, which posted 69.2% on the same benchmark. On BrowseComp, an autonomous web-search evaluation, M3 actually pulled ahead with 83.5 points.

## A New Architecture for an Old Problem

The technical engine behind M3's million-token ambitions is MiniMax Sparse Attention, or MSA -- a new attention mechanism that tackles the quadratic cost scaling that has long plagued transformer models at extreme context lengths. Rather than comparing every token against every other token, MSA splits the key-value cache into blocks, runs a lightweight filtering step to identify which blocks are relevant, and then computes full attention only on the selected segments.

The result is dramatic. At one million tokens of context, MiniMax reports a 20x reduction in per-token compute compared to its predecessor M2, with prefill processing running more than 9x faster and decoding more than 15x faster. Output speed hits roughly 100 tokens per second -- approximately 3x faster than Claude Opus, according to the company's benchmarks.

Independent researcher Elie Bakouch characterized the approach as doing "block level selection like in CSA but attention is done on the real KV, not in the compressed dimension" -- a distinction from DeepSeek's Multi-head Latent Attention that avoids precision loss at long contexts by operating on uncompressed key-value data.

## The Price War Intensifies

Perhaps the most disruptive element of the M3 launch is pricing. At $0.60 per million input tokens and $2.40 per million output tokens, M3 comes in at roughly one-tenth the cost of Claude Opus 4.7, which charges approximately $5 per million input and $25 per million output. A launch-week discount halves those figures further. For agentic coding workflows that can rack up thousands of model calls per session, the compounding savings are substantial.

MiniMax also introduced tiered subscription plans through MiniMax Code, its dedicated coding interface: $20 per month for approximately 1.7 billion tokens, scaling up to $120 per month for 9.8 billion tokens.

## Autonomy Demonstrations Raise the Bar

To showcase M3's sustained autonomous capabilities, MiniMax ran three internal demonstrations that push well beyond standard benchmark evaluations. In one test, M3 independently reproduced experiments from an ICLR 2025 Outstanding Paper on LLM fine-tuning, working autonomously for nearly 12 hours, producing 18 commits and 23 experimental figures. In another, the model optimized an FP8 matrix multiplication kernel on NVIDIA Hopper GPUs over 24 hours, completing 147 benchmark submissions and 1,959 tool calls to push hardware utilization from 7.6% to 71.3%.

"That's not an accusation of cheating, it's just how launch-day benchmarks work," noted independent reviewer Thomas Wiegold, pointing out that every benchmark figure in MiniMax's launch materials was produced on the company's own infrastructure with baselines it selected.

## The Caveats Are Real

The elephant in the room is verification. As of launch day, all benchmark scores are self-reported. Independent scores from Artificial Analysis and LMArena -- the two most widely cited third-party evaluation services -- were still pending. The promised open weights and technical report had not shipped either, with MiniMax committing to a roughly ten-day window for publication on Hugging Face and GitHub.

There are also geopolitical considerations that enterprise developers cannot ignore. Under China's 2017 National Intelligence Law, MiniMax is legally required to "support, assist, and cooperate with state intelligence work" -- an obligation that applies to every prompt processed through the company's API regardless of where the user is located. The American Enterprise Institute named MiniMax specifically in April 2026 analysis of the law's application to Chinese AI labs.

## What It Means for the AI Landscape

MiniMax M3 represents a significant inflection point in the open-weight model race. If the benchmarks survive independent validation and the weights ship on schedule, M3 would become the first open model to credibly challenge proprietary frontier systems across coding, long-context, and multimodal capabilities simultaneously -- and at a price point that could reshape how developers budget for AI infrastructure.

But the conditional matters. Until independent evaluations land and the weights are in researchers' hands, M3 remains a compelling promise rather than a confirmed reality. The roughly June 11 target date for the open-weight release is when the real assessment begins.