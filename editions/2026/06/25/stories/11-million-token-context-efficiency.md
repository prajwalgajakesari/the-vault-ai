---
headline: "New Architectures Push Million-Token Context Toward Near-32K Compute Cost"
slug: million-token-context-efficiency
category: research
story_number: 11
date: 2026-06-25
---

# New Architectures Push Million-Token Context Toward Near-32K Compute Cost

The defining bottleneck of the transformer era is the attention mechanism's quadratic cost: double the context, quadruple the compute. In 2026, a cluster of new architectures is attacking that wall directly, and the early reporting suggests the economics of long context are starting to bend. The shorthand circulating among researchers is striking — a mid-sized model processing roughly a million tokens at something close to the compute a 32K window used to demand. The figure is approximate and, in the cleanest cases, industry-reported rather than peer-reviewed. But the underlying shift is real, and it is showing up across state-space models, linear attention, and learned-sparse attention at once.

## The transformer bottleneck, restated

Standard dense attention compares every token with every other token. For a sequence of length *n*, that is roughly *n²* operations and *n²* memory pressure. At 32K tokens it is tolerable. At a million it is brutal, which is why most frontier models that advertise million-token windows degrade badly when asked to actually use them. On MRCR v2, the multi-reference retrieval benchmark labs report, even the strongest models leave large gaps, and several score far below their headline context claims.

The newest architectures share a single insight, framed bluntly by Subquadratic CTO Alex Whedon: "Sparse attention basically means instead of doing what transformers do, which is if you have 1,000 words, you look at every possible relationship between all 1,000 words, which is 1,000 squared combinations. You realize that only a portion of those actually matter and you only process the portion that matter." (The New Stack, May 2026)

## Three lines of attack

**Learned-sparse attention.** Miami-based startup Subquadratic launched its first model in May 2026 on an architecture it calls Subquadratic Selective Attention (SSA), which the company says scales linearly in both compute and memory with context length. Its reported benchmarks are aggressive: a 52x speedup over dense attention at one million tokens (7.2x already at 128K), 92.1% needle-in-a-haystack retrieval at a 12-million-token window, and 83 on MRCR v2 — nine points above the best score the company attributes to OpenAI. These numbers are vendor-reported and not independently reproduced; the weights are not open. But the direction matters: SSA's selection is content-dependent, choosing which positions matter per query without the selection step itself going quadratic — the trap that, the company argues, snares predecessors like DeepSeek's Sparse Attention, whose lightning indexer still scores every query against every key.

**State-space models.** The Mamba lineage took a different route, replacing all-pairs comparison with a recurrent state that compresses everything seen so far. Mamba-3, detailed in March 2026 by the Goomba Lab (Princeton/Cartesia/Together collaborators), is pitched as "inference-first." Its authors report matching strong transformer-baseline perplexity at roughly half the decoding cost, and beating Mamba-2, Gated DeltaNet, and a Llama-3.2-1B transformer on combined prefill-plus-decode latency across sequence lengths at the 1.5B scale. State-space recurrence is linear in sequence length by construction — its cost grows with *n*, not *n²* — which is what makes million-token serving plausible.

**Linear attention and hybrids.** Gated DeltaNet (NVIDIA) combines Mamba-2-style gating with a DeltaNet fast-weight memory update, and now anchors hybrid stacks in shipping models — Qwen3-Next mixes Gated DeltaNet blocks with periodic gated-attention layers, and NVIDIA's Nemotron 3 alternates regular attention with Mamba-2 layers.

## Why the "32K-cost" framing needs an asterisk

The pure efficiency story has a real caveat, and the most honest version comes from the skeptics. The New Stack notes that hybrid architectures — the pragmatic, widely deployed answer — retain a handful of dense attention layers for retrieval quality, and "a hybrid that is three times cheaper at 32K tokens remains three times cheaper at 10M tokens, because the dense layers it retains still do O(n²) work." A constant-factor discount is not the same as changing the scaling law. That distinction is exactly what the new architectures are fighting over: Whedon frames hybrids as delivering "a scalar benefit," while a fully subquadratic mechanism delivers "a scaling-law advantage." Whose claim survives independent replication is the open question.

There is also an accuracy ledger. NVIDIA's own study at 8B scale found pure Mamba-2 lagged transformers on MMLU and phonebook-style lookup, with the gap closing only when attention layers were added back. Compression is lossy; learned sparsity can miss the token that mattered. The benchmarks that look best — needle-in-a-haystack, RULER — are not the same as messy real-world long-context reasoning.

## Why it matters for RAG, agents, and cost

If long context gets genuinely cheap, the architecture of AI systems shifts. Retrieval-augmented generation exists partly as a workaround for short, expensive context; a model that holds millions of tokens affordably can ingest whole codebases, case files, or document corpora directly. Agent harnesses, which accumulate long tool-call histories, are the clearest beneficiary — Sebastian Raschka's 2026 research roundup frames long-context efficiency as a central theme precisely because "more LLMs are integrated into agent harnesses, requiring work with longer and longer contexts." Serving cost is the lever underneath all of it: prefill and decode latency at length is what determines whether a million-token agent loop is a demo or a product. Subquadratic's CEO Justin Dangel notes the company runs on "neoclouds rather than the major hyperscalers" because the hyperscalers are "very expensive" — a reminder that efficiency claims live or die on real serving infrastructure.

## What to watch

Three things. First, independent reproduction — the boldest numbers (12M-token retrieval, 52x speedups) are vendor-reported, and the category, as The New Stack put it, has a "track record" of approaches that "traded one necessary property to gain another." Second, whether hybrids or pure subquadratic mechanisms win at frontier scale, since that decides if the gain is a constant factor or a new scaling law. Third, downstream quality on hard reasoning, not just retrieval. If even one of these architectures holds up under scrutiny at frontier scale, the million-token context window stops being a marketing number and starts being an economic default — and the transformer's quadratic tax, the tax that has shaped LLM design since 2017, finally starts to come down.

---

*Reporting grounded in: Frederic Lardinois / The New Stack (May 5, 2026); the Goomba Lab, Princeton Language and Intelligence, and Cartesia Mamba-3 posts (March 2026); NVIDIA's Gated Delta Networks paper; and Sebastian Raschka's 2026 LLM research survey. Specific multi-million-token figures are company-reported and not independently verified.*
