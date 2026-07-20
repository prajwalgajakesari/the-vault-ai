# Borrowing From Distributed Databases, a New Paper Lets Agents Merge Their KV Caches Instead of Their Words

When two AI agents solve halves of the same problem and hand their thinking to a third, something absurdly fragile decides the answer: which one got listed first.

That is the finding of a preprint posted to arXiv on July 1, 2026, by Carlos Baquero of the University of Porto and Luis Brito of ESTG, Politecnico de Viana do Castelo. *Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning* argues that the way multi-agent systems fuse agents' internal state is order-sensitive in a way nobody has been measuring, and that the fix has sat in distributed systems for fifteen years. Baquero would know: he co-created conflict-free replicated data types (CRDTs), the convergence machinery underneath Riak and Akka distributed data.

*Corrected identifier: arXiv:2607.01308 (assigned as 2607.01367).*

## What a KV cache is, and why agents are trading them

When a transformer reads text, each token leaves behind a key and a value vector per layer. Together these form the KV cache, the model's compressed working memory - normally a private optimization.

Recent work repurposes it as a communication channel: instead of writing a paragraph for agent B, agent A hands over its raw cache. Agents, the paper notes, "pass intermediate KV-cache state directly, giving a downstream agent access to richer, higher-bandwidth representations than decoded text." The field calls this latent reasoning, and it is cheap: the Agent Primitives work this paper builds on reports roughly 3-4x reductions in token usage and inference latency versus text-based multi-agent systems.

The catch is the merge. To give a final agent both contributors' state, you concatenate the caches along the sequence axis and re-encode positions with RoPE, the rotary embedding most modern models use. Baquero and Brito name this operator BagMerge. Concatenation is ordered, and RoPE makes that order load-bearing: whichever agent occupies the privileged position-0 prefix slot gets a measurable advantage, and the decoded answer changes.

There is no safe default. On Qwen3-1.7B, swapping the agents was better when they could see the query (0.90 and 0.91 accuracy at 20 and 40 latent steps) and worse when they could not (0.83 and 0.77, against 0.90 and 0.85). On Qwen3-4B the inversion vanishes and swap wins both regimes. Across four model-by-regime cells the best ordering runs swap / default / swap / swap - six to fourteen points riding on a coin flip nobody can call in advance.

## The CRDT move

A CRDT is a data structure built so replicas receiving the same updates in any order, on any schedule, with arbitrary duplication, still converge to identical state. The guarantee is structural, proven about the merge itself rather than enforced by a coordinator.

First, CanonicalMerge fixes the layout by content rather than caller: it scores each cache by mean key-norm at a middle transformer layer and sorts on that. Because the score is symmetric in the content, the merged cache is byte-identical under any permutation of the inputs - verified across all permutations for two to five agents, and bit-for-bit on real Qwen3-1.7B (28 layers) and Qwen3-4B (36 layers) KV state.

Second, they separate durable state from decode-time layout. The state becomes LatentFragmentSet, a set of content-addressed fragments whose merge is plain set union - a state-based CvRDT that is "commutative, associative, idempotent, and absorbing by one-line proofs." CanonicalMerge is just its deterministic render.

The payoff appears under repeated delivery, the redundancy gossip and retry produce. Naive re-concatenation degrades from 0.93 accuracy at one copy to 0.45 at four, the cache growing linearly from 308 to 1,232 tokens. The CRDT policy absorbs byte-identical copies by content hash: accuracy holds at 0.93 and length at 308 tokens regardless.

## The honest accounting

CanonicalMerge does not win on accuracy, and the authors say so. It lands within 4 percentage points of the best BagMerge ordering in every cell, trading "a small, statistically insignificant accuracy margin for an unconditional structural guarantee." On 50 HotpotQA bridge questions it scores 0.605 F1 against a full-context baseline's 0.610, EM tied at 0.460, though BagMerge default edges both at 0.632.

The lopsided number is against output-level fusion: PackLLM, which blends output logits rather than caches, trails by 45 points at matched generation budget. By the output head each agent has compressed its reasoning into a sparse vocabulary distribution, and averaging two such vectors cannot synthesize content neither emits alone.

Limitations are front-loaded. Byte-identity assumes matched arithmetic and deterministic kernels; across heterogeneous accelerators, low-order bits may differ, breaking content-hash absorption. Convergence is syntactic - exact duplicates absorb, semantic near-duplicates do not. Both models are one family, and the benchmark is largely synthetic.

## Beyond two agents, it breaks

The negative result is most interesting. At three agents, a flat CanonicalMerge collapses to 0.07 and 0.03 accuracy on families whose full-text ceilings are 1.00 and 0.97; a pairwise merge tree does no better. Quality returns only when the model reprocesses a seam: one attention seam recovers 0.73 on chain-structured problems, a full sequential chain 0.97. The authors are blunt - "CRDT cache merge is a transport and colocation operator, not a composition operator."

## Why latent communication is an emerging direction

Text is the default agent interface because it is legible, but every handoff compresses continuous internal state into discrete tokens and re-expands it, paying in tokens, latency and fidelity. This paper's contribution may be less the algorithm than the framing. Once agents exchange state instead of messages, the hard problems stop being NLP ones and become distributed-systems ones: ordering, idempotence, convergence, provenance.

## What to watch

Whether anyone turns transport into composition beyond two agents without full sequential reprocessing - the problem the authors leave open. And the safety question: work like LCGuard is already asking what it means to accept a stranger's raw KV cache, unreadable by construction. This is a v1 preprint, not peer reviewed. Read the structural guarantees as proven and the accuracy story as preliminary.
