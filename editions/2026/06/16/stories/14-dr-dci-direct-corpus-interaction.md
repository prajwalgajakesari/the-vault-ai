---
headline: "Dr-DCI Lets Search Agents Talk Directly to a Corpus, Expanding Their Workspace on the Fly"
slug: dr-dci-direct-corpus-interaction
category: research
story_number: 14
date: 2026-06-16
source: "arXiv:2606.14885"
---

# Dr-DCI Lets Search Agents Talk Directly to a Corpus, Expanding Their Workspace on the Fly

For all the excitement around AI agents that "do research," most of them are still peering at the world through a very narrow window. When an agent searches a large document collection, it almost never touches the collection itself. Instead, it hands a query to a retriever — a system like BM25 or ColBERT — and gets back a ranked list of candidates. The retriever is good at one job: deciding which documents look most relevant to a string of words. But it only ever shows the agent the top of a list, or a bounded slice of a document. The agent cannot reorganize the material, cross-check a claim across ten sources at once, or verify a constraint that spans the whole corpus. It can only ask for more list.

A paper announced June 16, 2026 argues this is the wrong interface for an agent that has to reason over many steps. Titled "Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion" (arXiv:2606.14885), the work — from Yi Lu, Zhuofeng Li, Wenhu Chen, Jimmy Lin, Dongfu Jiang, Yu Zhang and colleagues — proposes letting agents interact with a corpus far more directly, and then makes that direct interaction scale to collections too large to fit in any context window.

## What "direct corpus interaction" means

The core idea, which the authors call Direct Corpus Interaction (DCI), is to stop treating the corpus as a black box behind a ranking function. Per the paper, a retriever-mediated interface "exposes evidence only as ranked results or bounded document views," which limits an agent's ability to reorganize material and verify constraints across documents. DCI instead exposes the corpus through shell-executable operations — the kind of search, filter, compare and verify primitives a human analyst would reach for at a command line.

That distinction matters. A ranked list answers "what looks similar to my query?" A shell-style interface answers richer questions: count how many documents satisfy a condition, pull every passage that mentions two entities together, diff two reports, or filter down a set and then operate on the survivors. The agent is no longer limited to semantic similarity as the only lens. It can express logic, structure and verification directly against the data, which is exactly what long, multi-step investigations demand.

The framing builds on a line of recent work — including papers like "Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction" — that questions whether similarity-ranking is the right contract between an agent and its evidence at all.

## The scaling problem, and dynamic workspace expansion

Direct interaction sounds liberating until you remember how big real corpora are. You cannot simply dump a multi-gigabyte collection into a context window so the agent can grep it. The contribution Dr-DCI is named for is its answer to this: dynamic workspace expansion.

Rather than fixing the agent's view in advance, the system grows the agent's working surface on the fly as the task demands. The "workspace" is the set of corpus material the agent can directly manipulate, and it expands dynamically — bringing more of the corpus into reach when the agent's operations call for it, instead of pre-committing to a single retrieved slice. This is what turns DCI from a neat idea on a toy collection into something that can, in principle, run against corpora far larger than the model could ever hold at once.

The paper is a substantial one — 25 pages, with four figures and 22 tables — suggesting the authors put real weight on empirical evaluation across many settings rather than a single benchmark headline. (We are not reproducing those numbers here, since the abstract alone does not state them.)

## Why this matters for long-horizon agents

The timing is not accidental. The hardest open problem in agentic search right now is the long horizon: tasks that need dozens of retrieval steps and reasoning that stitches together sources the agent saw at different moments. Recent benchmarks have shown how easily agents get "lost in the maze" of such tasks, and how a retriever's narrow window forces an agent to spend turns re-querying for context it should already be able to hold and inspect.

A direct, expandable interface attacks that failure mode at its root. If an agent can filter, recombine and verify against the corpus itself — and if its workspace can grow as the investigation deepens — then constraint-checking and cross-document synthesis become operations the agent performs, not approximations it pieces together from ranked snippets. That is the difference between an agent that browses and an agent that genuinely works over a body of evidence.

## The bigger shift

Dr-DCI fits a broader rethinking of how agents should meet their data. The first generation of retrieval-augmented systems treated retrieval as a fixed, one-shot step before generation. The second made it agentic — letting the model decide when and what to fetch. Dr-DCI pushes on the third axis: not just *when* an agent retrieves, but *what kind of contact* it gets with the corpus, and how much of that corpus it can hold in view at once. By making direct interaction scalable, the authors are betting that the most capable research agents will be the ones that stop asking a middleman for a list and start talking to the data directly.

---

*Source: [arXiv:2606.14885](https://arxiv.org/abs/2606.14885), "Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion."*
