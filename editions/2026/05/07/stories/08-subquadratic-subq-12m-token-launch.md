---
headline: "Subquadratic Exits Stealth With $29 Million and a 12 Million Token Context Window That Challenges Transformer Orthodoxy"
slug: subquadratic-subq-12m-token-launch
category: llms-genai
story_number: "08"
date: 2026-05-07
---

# Subquadratic Exits Stealth With $29 Million and a 12 Million Token Context Window That Challenges Transformer Orthodoxy

A four-person Miami startup called Subquadratic emerged from stealth on May 5 with a claim bold enough to divide the AI research community within hours: that it has built the first frontier large language model to fully escape the quadratic attention bottleneck that has constrained every major AI system since 2017. The company launched with $29 million in seed funding, a model called SubQ 1M-Preview, and a research configuration boasting a 12 million token context window -- roughly 9 million words, or the equivalent of 120 books processed in a single call.

The announcement drew more than 12 million views on X and over 30,000 waitlist signups in its first 24 hours, according to co-founder and CEO Justin Dangel. It also drew something less welcome: immediate and pointed skepticism from the AI research community, which has seen architectures promising to dethrone the transformer come and go with metronomic regularity.

## The Core Claim: Linear Scaling Where Everyone Else Pays Quadratic Costs

At the heart of Subquadratic"s pitch is a proprietary mechanism called Subquadratic Sparse Attention, or SSA. Traditional transformer models use dense attention, meaning every token in a prompt is compared against every other token. Double the input, and the compute roughly quadruples. That quadratic scaling is why the industry standard remains 128,000 tokens for most models, stretching to 1 million for frontier offerings like Claude Sonnet 4.7 and Gemini 3.1 Pro.

SSA takes a different approach. For each query token, the model dynamically selects a small subset of positions to attend to based on content rather than fixed patterns, then computes exact attention only over those selected positions. The result, the company claims, is a model that scales linearly with context length, cutting attention compute by approximately 1,000 times at 12 million tokens compared with standard architectures.

"We are very focused on the problem of how we transition from a dense attention, quadratic scaling architecture to a sparse attention linear architecture," Dangel told SiliconANGLE. "Sparse attention is an effort to say, hey, let"s try to figure out how to not compare every token to every token to every token."

CTO Alexander Whedon, formerly Head of Generative AI at TribeAI and a software engineer at Meta, framed the practical impact in terms of what developers currently endure. "I used to manually curate prompts and retrieval systems and evals and conditional logic to chain together the workflows," Whedon said. "And I think that that is kind of a waste of human intelligence and also limiting to the product quality."

## Strong Benchmarks, Narrow Selection

Subquadratic is backing its claims with performance numbers. On the RULER 128K benchmark, SubQ scored 95 percent accuracy at a reported cost of $8, compared with 94 percent accuracy and approximately $2,600 for Claude Opus. The company says SubQ outperforms GPT-5.5 on retrieval benchmarks at the 12 million token scale.

But the benchmark selection has drawn scrutiny. The company published results on exactly three tests, all emphasizing long-context retrieval and coding -- precisely the tasks SSA is designed to excel at. Broader evaluations covering general reasoning, mathematics, multilingual performance, and safety have not been released. A comprehensive model card is listed as "coming soon," and the company has not yet published a peer-reviewed technical paper.

## Skeptics Draw the Theranos Comparison

The AI research community"s response landed on a wide spectrum. Within hours of the launch, prominent AI engineer Will Depue noted that SubQ appeared to be built on open-source model weights, suggesting it was likely a sparse attention fine-tune of an existing model such as Kimi or DeepSeek. Depue later escalated his criticism, writing that the company"s O(n) scaling claims and speedup numbers "don"t seem to line up" and calling the communication "either incredibly poorly communicated or just not real."

Whedon confirmed on X that the company uses open-source model weights as a starting point, describing it as a practical function of funding and maturity. Still, the comparisons were unflattering. At least one widely circulated post declared that SubQ is "either the biggest breakthrough since the Transformer... or it"s AI Theranos."

The Magic.dev precedent looms especially large. That company announced a 100 million token context window model in August 2024, also claiming a 1,000 times efficiency advantage, and raised roughly $500 million on the strength of those claims. As of early 2026, there is no public evidence of its LTM-2-mini model being used outside the company.

## The Team and the Money

Dangel is a five-time founder with a track record across health tech, insurance technology, and consumer goods. The company"s research team includes 11 PhD researchers with backgrounds at Meta, Google, Oxford, Cambridge, ByteDance, Adobe, and Microsoft. The $29 million seed round, raised at a reported $500 million valuation, was backed by Tinder co-founder Justin Mateen, Miami tech investor Javier Villamizar, and investors with ties to Anthropic, OpenAI, Stripe, and Brex.

According to Dangel, the company has been developing the underlying technology for roughly five years. It is launching two products in beta: an API exposing a 1 million token production context window and SubQ Code, a CLI coding agent. The 12 million token window is available in a research configuration, with a 50 million token target set for the fourth quarter of 2026.

## Why This Matters

If Subquadratic"s claims survive independent evaluation, the implications extend well beyond one startup"s valuation. A genuinely linear-scaling attention mechanism at frontier quality would make retrieval-augmented generation pipelines, chunking strategies, and agentic retrieval systems partially or fully obsolete for many workloads. Entire enterprise codebases, months of pull request history, and full legal document sets could be processed in a single call without the latency and information loss that current workarounds introduce.

But the AI field has a pattern: architectures that claim to replace the transformer -- Mamba, RWKV, state space models -- have repeatedly underperformed at frontier scale when subjected to rigorous, independent evaluation. Dangel himself acknowledged the dynamic. "Extraordinary claims will often be greeted rightly with skepticism," he said. "The fact that our company has a potentially industry-disrupting innovation, I"m not surprised by the reaction."

## What to Watch Next

The company says it plans to release additional technical papers and products in the coming months. "We look forward to releasing products and papers," Dangel said. "I hope the community will be satisfied." The real verdict will come not from internal benchmarks or X engagement metrics, but from whether independent researchers can reproduce the efficiency claims and whether the architecture holds up across the broad battery of evaluations that frontier models are expected to pass. Until then, Subquadratic occupies a familiar but precarious position: a startup whose technology is either genuinely transformative or merely well-marketed, with $29 million and 11 PhDs to prove which it is.