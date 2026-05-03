---
headline: "Xiaomi Open-Sources MiMo-V2.5-Pro With One Trillion Parameters and Million-Token Context"
slug: xiaomi-mimo-v25-pro-open-source
category: llms-genai
story_number: "07"
date: 2026-05-02
---

# Xiaomi Open-Sources MiMo-V2.5-Pro With One Trillion Parameters and Million-Token Context

The company best known for selling smartphones at razor-thin margins has just dropped a frontier-class AI model under the most permissive license in the industry -- and the benchmarks suggest it is not a vanity project. Xiaomi released MiMo-V2.5-Pro on April 22, 2026, a 1.02-trillion-parameter Mixture-of-Experts model with 42 billion active parameters, a one-million-token context window, and native multimodal capabilities spanning text, image, video, and audio. The weights are available on Hugging Face under an MIT license, meaning anyone can download, fine-tune, and commercially deploy the model without restriction.

The release cements a pattern that has been building for more than a year: Chinese technology companies are not just participating in the open-source AI race -- they are setting its pace.

## Two Models, One Architecture Philosophy

Xiaomi actually shipped two models as part of the V2.5 family. MiMo-V2.5-Pro is the flagship: 1.02 trillion total parameters with 42 billion active at inference time, trained on 27 trillion tokens using FP8 mixed precision. The smaller sibling, MiMo-V2.5, packs 310 billion total parameters with 15 billion active, trained on an even larger corpus of 48 trillion tokens -- a design choice that prioritizes efficiency and cost over raw scale.

Both models share a hybrid-attention architecture that interleaves Sliding Window Attention and Global Attention at a 6:1 ratio with a 128-token sliding window. The practical effect is significant: KV-cache storage drops by nearly seven times compared to standard full-attention designs, which is what enables the million-token context window without requiring a small data center to run inference. Xiaomi describes this as a learnable attention sink bias that preserves long-context performance while dramatically cutting memory overhead.

The multimodal capabilities are not bolted-on afterthoughts. MiMo-V2.5-Pro processes text, code, images, video, and audio within a single unified architecture. For developers building agentic applications, the model can sustain complex trajectories spanning thousands of tool calls while maintaining coherence across the full million-token context.

## Benchmark Performance That Demands Attention

The numbers are hard to dismiss. On SWE-bench Pro, a demanding benchmark for real-world software engineering tasks, MiMo-V2.5-Pro scores 57.2 percent -- ahead of Claude Opus 4.6 at 53.4 percent and within striking distance of GPT-5.4 at 57.7 percent and Kimi K2.6 at 58.6 percent. On agentic evaluations like Claw-Eval and GDPVal, the model matches or exceeds several closed-source competitors.

The cost structure is equally striking. MiMo-V2.5 is priced at $0.40 per million input tokens and $2.00 per million output tokens through Xiaomi Cloud -- roughly an order of magnitude cheaper than comparable frontier models. That is not a promotional gimmick. The efficient MoE architecture, where only a fraction of parameters activate per token, translates directly into lower serving costs.

## The Luo Fuli Factor

The MiMo division is led by Luo Fuli, a former core contributor at DeepSeek who worked on the R1 and V-series models before joining Xiaomi. Her fingerprints are visible in the architectural choices: the aggressive use of Mixture-of-Experts, the emphasis on training efficiency, and the decision to release under MIT rather than a more restrictive license all echo the playbook that made DeepSeek a credible open-source contender. According to reporting from 36Kr, Luo timed the V2.5 launch as a deliberate pre-emptive strike ahead of DeepSeek-V4, and Xiaomi claims the Pro model outperforms DeepSeek-V4-Pro across multiple evaluations.

## Hardware Agnosticism as Strategy

In a move that underscores the geopolitical dimensions of AI development, Xiaomi announced day-one compatibility with seven chip platforms: Alibaba T-Head, AWS Trainium2, AMD, Baidu Kunlun Core, Enflame Technology, Moore Threads, and Tianshu Zhixin. Five of those seven are Chinese-designed chips. The message is clear: MiMo is built to run on whatever silicon is available, including domestically produced alternatives to NVIDIA hardware that may be subject to export restrictions.

This hardware flexibility, combined with the MIT license, positions MiMo-V2.5-Pro as a strategically important model for organizations -- and nations -- seeking to reduce dependence on any single chip vendor or model provider.

## The Bigger Picture: China and the Open-Source AI Arms Race

Xiaomi joins DeepSeek, Alibaba (Qwen), and Baidu (ERNIE) in a growing cohort of Chinese companies releasing frontier-capable models under permissive licenses. The competitive dynamic is striking: while American labs like OpenAI and Anthropic have largely moved toward closed or semi-open release strategies, their Chinese counterparts are aggressively open-sourcing models that match or beat them on key benchmarks. The result is a two-track AI ecosystem where the most accessible frontier models increasingly originate from China.

For enterprise developers and startups, the practical implications are immediate. A model that matches GPT-5.4 on coding benchmarks, runs on diverse hardware, and costs a fraction of the price to serve is not just technically interesting -- it reshapes build-versus-buy calculations across the industry.

## What to Watch Next

The critical question is whether MiMo-V2.5-Pro can translate benchmark performance into real-world adoption at scale. Watch for ecosystem development: fine-tuned variants, integration into popular frameworks, and enterprise deployment case studies. Xiaomi has announced 100 trillion free tokens for developers through its cloud platform, a subsidy designed to seed adoption. If the developer community responds the way it did to DeepSeek-R1 and Qwen-3, Xiaomi could find itself operating one of the most widely deployed open-source model families within months. The smartphone company, it turns out, has ambitions well beyond your pocket.