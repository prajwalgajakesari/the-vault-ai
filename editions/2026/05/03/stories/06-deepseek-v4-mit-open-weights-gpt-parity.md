---
headline: "DeepSeek V4 Ships MIT Licensed Open Weights With 1.6 Trillion Parameters at Near GPT-5.4 Parity"
slug: deepseek-v4-mit-open-weights-gpt-parity
category: llms-genai
story_number: "06"
date: 2026-05-03
---

# DeepSeek V4 Ships MIT Licensed Open Weights With 1.6 Trillion Parameters at Near GPT-5.4 Parity

On April 24 the Hangzhou-based AI lab DeepSeek dropped the preview release of its V4 model family -- two Mixture-of-Experts language models shipped under the MIT license with full open weights on Hugging Face. The larger variant, V4-Pro, packs 1.6 trillion total parameters with 49 billion active per forward pass, a one-million-token context window, and benchmark scores that place it within striking distance of the best American frontier models at a fraction of their price. Ten days later, the implications are still rippling through the industry.

## Two Models, One Message

DeepSeek V4 arrives in two configurations. V4-Pro is the flagship: 1.6 trillion parameters, 49 billion active, pre-trained on 33 trillion tokens. V4-Flash is the efficiency variant: 284 billion total parameters, 13 billion active, trained on 32 trillion tokens. Both share a hybrid attention architecture that combines Compressed Sparse Attention and Heavily Compressed Attention, cutting single-token inference FLOPs to 27 percent of the previous DeepSeek-V3.2 and shrinking the KV cache to just 10 percent of its predecessor at the full one-million-token context length.

The pricing underscores the competitive intent. V4-Pro lists at $1.74 per million input tokens and $3.48 per million output tokens. V4-Flash comes in at $0.14 per million input tokens. For comparison, OpenAI charges roughly $5.00 per million input tokens for GPT-5.5 and Anthropic charges $25 per million output tokens for Claude Opus. A promotional 75 percent discount on V4-Pro runs through May 31, making the already aggressive pricing temporarily absurd.

## Benchmarks: Close but Not Identical

The headline numbers are impressive. V4-Pro tops LiveCodeBench at 93.5 and reaches a Codeforces ELO of 3,206 -- ahead of GPT-5.5 at 3,168. On SWE-bench Verified, V4-Pro scores 80.6 percent, statistically tied with Claude Opus 4.7 at 80.8.

But the picture is more nuanced than DeepSeek's own marketing suggests. A NIST Center for AI Standards and Innovation evaluation published in early May concluded that V4-Pro's capabilities "lag behind the frontier by about eight months," placing it roughly on par with GPT-5 rather than GPT-5.5. On Terminal-Bench 2.0, which tests complex command-line workflows requiring planning and tool coordination, GPT-5.5 scores 82.7 percent versus V4-Pro's 67.9 -- a 14.8-point gap that is not a rounding error.

The NIST assessment did note, however, that compared to the most cost-competitive U.S. reference model, GPT-5.4 mini, DeepSeek V4 was more cost efficient on five out of seven benchmarks, ranging from 53 percent less expensive to 41 percent more expensive depending on the task. That cost-efficiency finding may matter more to enterprise buyers than raw leaderboard placement.

## The MIT License Changes the Calculus

What separates V4 from many previous frontier-adjacent releases is the license. MIT imposes no commercial-use restrictions, no acceptable-use clauses tied to user count, and no required attribution beyond the license text itself. Any company, research lab, or individual developer can download the weights, fine-tune them, and deploy them in production without negotiating an enterprise agreement or worrying about usage caps.

"The open strategy has been one key channel through which China aims to compete with the U.S., by rapidly scaling up adoptions and rolling out real-life applications in various sectors from e-commerce to robotics," CNN reported on the day of the release.

The permissive licensing also complicates the geopolitical picture. Anthropic and OpenAI have accused DeepSeek of illegally extracting capabilities from their models through distillation. On the eve of the V4 launch, Michael Kratsios, White House director of the Office of Science and Technology Policy, accused foreign entities "primarily based in China" of conducting "industrial-scale" campaigns to distill frontier AI models from U.S. companies. DeepSeek has not publicly responded to the allegations.

## Huawei Hardware, Not Nvidia

To fulfill V4's computing requirements, DeepSeek partnered with Huawei, which announced that it supports the AI startup with its Supernode technology by combining large clusters of its Ascend 950 chips. The integration is significant: it demonstrates that a competitive frontier model can be trained and served on non-Nvidia silicon, weakening one of the core assumptions behind U.S. export controls on advanced AI chips to China.

## What This Means for the Market

The market reaction to V4 has been notably more muted than the panic that followed DeepSeek R1 in January 2025, when the model briefly tanked U.S. tech stocks. Analysts attribute the calmer response to two factors: the frontier labs have widened their own leads since then, and the industry has internalized that Chinese open-source models will continue to close the gap on a recurring basis.

For enterprise AI teams, however, the practical implications are substantial. A mid-size SaaS company processing 100 million input tokens per day could save roughly $29,500 per month by switching from GPT-5.5 to V4-Flash, according to cost analyses published after the release. That savings grows when factoring in the ability to self-host the open weights, eliminating API dependency entirely.

The central question going forward is whether near-frontier performance at one-seventh the cost is good enough. For coding assistants, document processing, and high-volume classification tasks, the answer is almost certainly yes. For complex agentic workflows requiring deep planning and tool coordination -- where that 14.8-point Terminal-Bench gap lives -- frontier closed models still hold a meaningful edge. The market is splitting, and DeepSeek V4 just made the split wider.
