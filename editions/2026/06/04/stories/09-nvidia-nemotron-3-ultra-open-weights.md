---
headline: "Nvidia Debuts Nemotron 3 Ultra as Largest US Open-Weight Model With 550 Billion Parameters"
slug: nvidia-nemotron-3-ultra-open-weights
category: llms-genai
story_number: 9
date: 2026-06-04
---

# Nvidia Debuts Nemotron 3 Ultra as Largest US Open-Weight Model With 550 Billion Parameters

Jensen Huang walked onto the Computex stage in Taipei on June 1, leather jacket and all, and unveiled the biggest open-weight AI model ever produced by an American company. Nemotron 3 Ultra, a 550-billion-parameter reasoning engine built on a hybrid Mamba-Transformer mixture-of-experts architecture, is now the top-scoring US open-weight model on independent benchmarks -- and it is not close. But in the intensifying transatlantic and transpacific race for AI supremacy, being the best in America is no longer enough to be the best in the world.

The model activates only 55 billion of its 550 billion total parameters on any given token -- a 90 percent sparsity rate that keeps inference costs far below what the headline parameter count would suggest. Think of it like a hospital with hundreds of specialists: when a patient arrives, only the relevant doctors show up. That design, combined with a million-token context window and multi-token prediction, lets Nemotron 3 Ultra generate more than 300 output tokens per second on a pre-release DeepInfra endpoint -- three to six times faster than Chinese rivals in the same intelligence class.

"Open innovation is the foundation of AI progress," Huang said during the keynote. "With Nemotron, we are transforming advanced AI into an open platform that gives developers the transparency and efficiency they need to build agentic systems at scale."

## The Numbers Tell Two Stories

Independent evaluator Artificial Analysis, which partnered with Nvidia on the pre-release assessment, scored Nemotron 3 Ultra at 48 on its Intelligence Index -- a composite benchmark aggregating ten evaluations spanning reasoning, coding, general knowledge, and agentic performance. That puts it comfortably ahead of every other US open-weight model: Google's Gemma 4 31B scored 39, Nvidia's own Nemotron 3 Super hit 36, and OpenAI's gpt-oss-120b managed 33.

But the leaderboard does not end at the American border. China's Kimi K2.6, released in April by Moonshot AI, sits at 54 on the same index -- six points above Nemotron 3 Ultra and only three points behind the proprietary flagships from Anthropic, Google, and OpenAI, all tied at 57. The gap illustrates a persistent pattern: Chinese labs have been flooding the open-weight ecosystem with strong models while their American counterparts keep their best systems behind APIs.

The speed story is where Nvidia genuinely differentiates. Artificial Analysis recorded median output speeds of 420.2 tokens per second across providers, with a time-to-first-token of just 0.91 seconds. Peer models from DeepSeek and Moonshot typically serve at 50 to 100 tokens per second through their commercial APIs. For autonomous agents executing long, multi-step tasks where latency compounds at every turn, that throughput advantage translates directly into faster and cheaper task completion -- Nvidia claims up to 30 percent lower cost to complete agentic benchmarks like SWE-Bench Verified and Terminal Bench.

## Architecture Built for Agents

Nemotron 3 Ultra is not a standard transformer. Its hybrid stack interleaves Mamba-2 layers, which process long sequences at sub-quadratic cost, with traditional attention layers that preserve precise recall over large contexts. The model uses 108 layers with 512 experts per MoE layer, activating the top 22 per token. A technique called LatentMoE routes experts more efficiently by trading hidden-dimension width for additional routed experts at fixed inference cost.

The model was pre-trained on 20 trillion text tokens in two phases -- 15 trillion biased for diversity, then 5 trillion biased for quality -- before its context window was extended to one million tokens. Post-training involved supervised fine-tuning, reinforcement learning across 15 environments, and a novel technique called Multi-teacher On-Policy Distillation, where more than ten domain-specialized teacher models provide dense, token-level guidance to the student model across its own generated rollouts.

On the non-hallucination front, Nemotron 3 Ultra recorded 78.7 on the AA-Omniscience benchmark -- the highest score in its comparison set -- suggesting a lower tendency to confabulate when uncertain. Its RULER score of 94.7 at one million tokens confirms that the long context window is not just theoretical.

## Enterprise Adoption Already Underway

Thirteen early adopters have signed on, including Accenture, CrowdStrike, Cursor, Deloitte, Palantir, Perplexity, ServiceNow, Siemens, and Zoom. Several are integrating Nemotron 3 Ultra into agentic workflows spanning cybersecurity, software development, and enterprise automation.

"Perplexity is built on the idea that human curiosity will be amplified by accurate AI built into exceptional tools," said Aravind Srinivas, CEO of Perplexity. "With our agent router, we can direct workloads to the best fine-tuned open models, like Nemotron 3 Ultra, or leverage leading proprietary models when tasks benefit from their unique capabilities -- ensuring our AI assistants operate with exceptional speed, efficiency and scale."

The model's weights shipped June 4 on Hugging Face, ModelScope, and OpenRouter, and are available as an Nvidia NIM microservice on build.nvidia.com. Nvidia released the weights under its Open Model License, which permits commercial use, along with training data and reinforcement learning recipes -- a level of openness that goes beyond what most frontier labs offer.

## The Bigger Picture

Nemotron 3 Ultra is the most visible output yet of Nvidia's publicly stated commitment to spend 26 billion dollars over five years on open-weight AI development. The company has also assembled the Nemotron Coalition -- eight AI labs including Mistral AI and Perplexity -- to co-develop the next generation, Nemotron 4, on DGX Cloud infrastructure.

The model arrives at a moment when the US open-weight ecosystem badly needs a credible contender. Chinese open-source models surged from roughly 1.2 percent of global open-model usage in late 2024 to around 30 percent by the end of 2025, according to Decrypt's reporting. Nemotron 3 Ultra narrows the gap but does not close it. At 48 versus Kimi K2.6's 54, the smartest American open model remains six index points behind the smartest Chinese one.

For enterprise developers evaluating their options, the calculus is nuanced. Nemotron 3 Ultra offers the best combination of intelligence and speed available in a US-origin open model, with the added assurance of Nvidia's enterprise support ecosystem. But teams that need absolute peak open-weight intelligence -- and can navigate the geopolitical considerations of Chinese-origin models -- still have reason to look east. The race, clearly, is far from over.
