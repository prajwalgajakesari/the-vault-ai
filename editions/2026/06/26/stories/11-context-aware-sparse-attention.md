A note on this story: The Vault set out to verify a 2026 method described to us as "Context-Aware Sparse Attention" (CASA), said to cut transformer compute roughly tenfold by adjusting its sparsity pattern to the content of the input. We could not confirm a paper by that exact name and description. But the underlying idea — attention that decides, on the fly, which tokens are worth computing — is very real and is arguably the hottest thread in efficiency research this year. So we anchor this story on two verifiable results that deliver precisely what CASA promised.

## The idea: stop paying for tokens you don't need

The attention mechanism at the heart of every large language model has a stubborn problem: its cost grows with the square of the sequence length. Double the context, quadruple the compute. As models stretch toward million-token windows for agentic workflows, repository-scale code reasoning, and persistent memory, that quadratic wall becomes, in the words of one June 2026 paper, "untenable at deployment scale."

Sparse attention is the escape hatch. The insight is that most attention weight, in practice, lands on a small subset of tokens — so why compute the rest? The hard part is doing this *adaptively*: picking the right tokens based on what the input actually contains, rather than a fixed, hand-drawn pattern. Two recent papers crack that in different ways.

## MiniMax Sparse Attention: shipped, not just published

The most consequential is **MiniMax Sparse Attention (MSA)**, posted to arXiv on June 11, 2026 by Xunhao Lai, Pengyu Zhao and colleagues. Unlike most efficiency papers, this one comes attached to a production model: MiniMax's M3, a 109-billion-parameter natively multimodal system, already released publicly.

MSA splits attention into two branches. "A lightweight Index Branch scores key-value blocks and independently selects a Top-k subset for each [grouped-query] group," the authors write, "while the Main Branch then performs exact block-sparse attention over only the selected blocks." In plain terms: a cheap scout first decides which chunks of context matter for each query, and the expensive computation runs only on those.

The payoff is large and specific. "On a 109B-parameter model with native multimodal training, MSA performs on par with GQA while reducing per-token attention compute by 28.4x at 1M context," the authors report. Paired with a custom GPU kernel, that translates to "14.2x prefill and 7.6x decoding wall-clock speedups" on an H800. The inference kernel is open-sourced on GitHub.

## DHSA: tenfold faster without retraining

The second result, **Dynamic Hierarchical Sparse Attention (DHSA)** from Siheng Xiong and co-authors, was accepted as an ICML 2026 Spotlight. Its pitch is complementary: rather than baking sparsity into training, DHSA "predicts attention sparsity online while keeping the LLM backbone frozen" — bolting onto existing open-weight models. It estimates importance at the chunk level, then propagates it down to individual tokens.

The numbers track the original tenfold claim closely. DHSA "delivers up to 10x prefill speedup at 128K context length" and posts "12-20% relative accuracy gains over Block Sparse Attention at comparable prefill cost." Tellingly, it ran a 100K-token context on a single 24GB GPU "where dense attention fails" — a vivid illustration of why this matters beyond the data center.

## Why efficiency is the whole ballgame

Three forces make adaptive sparsity strategic rather than incremental. **Cost:** attention dominates the bill for long prompts, so a 10x-to-28x reduction reshapes the economics of agents that re-read large contexts thousands of times. **Long context:** these methods don't just make existing windows cheaper, they make previously impossible windows feasible — the difference between a model that can hold an entire codebase in view and one that can't. **On-device AI:** DHSA squeezing 100K tokens onto a consumer-grade 24GB card hints at a near future where capable long-context models run on laptops and phones, not just rented H800s.

This is also where these methods sit relative to their predecessors. FlashAttention made dense attention faster without changing what it computes; linear attention changed the math but often sacrificed quality; content-adaptive sparse attention tries to keep exact attention over the tokens that matter and skip the rest. A large 2026 survey, *The Sparse Frontier*, counted more than 150 sparse-attention papers in a single year — the field is crowded, and not every claim survives scrutiny.

## What to watch

Two cautions. First, these are early-stage results: DHSA is peer-reviewed (ICML Spotlight), but MSA's headline figures, while backed by a shipped model and open code, are a single-team preprint awaiting independent replication. Second, "near-lossless" is workload-dependent — needle-in-a-haystack retrieval is not the same as multi-hop reasoning, and aggressive sparsity can quietly drop the token a hard question hinges on. The signal worth tracking through late 2026: whether content-adaptive sparsity holds up on reasoning-heavy benchmarks, and whether it becomes the default in frontier training runs rather than an inference-time retrofit. MiniMax shipping it in production suggests the answer is already tilting toward yes.