# 'AgentIR' Rethinks Retrieval for Deep Research Agents, Making Search Reasoning-Aware

When a person searches the web, they type a few keywords and keep the rest in their head. When a deep research agent searches the web, it thinks out loud first, writing a paragraph of natural-language reasoning about what it is looking for and why, before it ever issues a query. For years, retrieval systems have thrown that paragraph away. A new paper argues that discarding it is one of the most expensive mistakes in agentic search.

In "AgentIR: Reasoning-Aware Retrieval for Deep Research Agents," a team of retrieval researchers introduces a method that reads the agent's reasoning trace as part of the search, not as throat-clearing before it. The result, a compact embedding model called AgentIR-4B, reaches 68% accuracy on the demanding BrowseComp-Plus benchmark when paired with the open-weight agent Tongyi-DeepResearch, compared with 50% for conventional embedding models twice its size and 37% for the venerable keyword baseline BM25.

## The problem: retrievers built for humans, used by machines

Deep research agents, the systems that autonomously plan, search, read, and synthesize across dozens of web pages to answer a hard question, have quietly become one of the biggest consumers of retrieval infrastructure. But that infrastructure was designed for humans.

The authors put the mismatch plainly. "Unlike human users who issue and refine queries without documenting their intermediate thought processes," they write, "Deep Research agents generate explicit natural language reasoning before each search call, revealing rich intent and contextual information that existing retrievers entirely ignore."

That is the crux. A human might type "1998 Nobel physics" and rely on their own memory to filter the results. An agent, by contrast, will have already written something like: "I need to identify the physicist who shared this prize for the fractional quantum Hall effect, then cross-reference their doctoral students." All of that context, the disambiguation, the multi-hop plan, the implicit constraints, is sitting right there in the reasoning trace. A standard retriever, tuned to match a short query string against a document, never sees it. It answers a thin question when a rich one was available.

## The method: embed the reasoning, not just the query

AgentIR's core idea is deceptively simple: jointly embed the agent's reasoning trace alongside its query, so the retriever can condition on intent rather than keywords alone. The authors call this paradigm Reasoning-Aware Retrieval. Instead of compressing an agent's rich internal state down to a search box, the retriever ingests the state directly and returns documents matched to what the agent is actually trying to accomplish.

The second piece of the paper addresses a practical obstacle: there is no large, ready-made corpus of agent reasoning traces paired with the right documents to retrieve. So the team built one synthetically. Their data synthesis method, DR-Synth, generates deep-research retriever training data from standard question-answering datasets, effectively manufacturing the reasoning-plus-query signal that reasoning-aware retrieval needs to learn from.

Crucially, the authors report that the two contributions stand on their own. They "demonstrate that both components are independently effective," and that combining them "yields a trained embedding model, AgentIR-4B, with substantial gains." In other words, reasoning-aware retrieval helps even without the synthetic data, the synthetic data helps even with off-the-shelf retrievers, and together they compound.

## The numbers that matter

The headline evaluation is on BrowseComp-Plus, a benchmark built to stress-test agents on genuinely hard, browse-heavy questions where a single lucky search will not do. Paired with Tongyi-DeepResearch, an open-weight deep research agent, AgentIR-4B hit 68% accuracy.

The comparisons are what make that figure land. Conventional embedding models, at roughly twice the parameter count of AgentIR-4B, managed 50%. BM25, the sparse keyword-matching workhorse that still anchors countless production search stacks, reached 37%. The gap is not a rounding error; it is an 18-point jump over a larger dense retriever and a near-doubling over the lexical baseline, achieved by a 4-billion-parameter model that gives up size for context-awareness.

Two details are worth flagging for readers weighing the claim. First, the wins are measured through the downstream agent's end-task accuracy, not just retrieval-quality proxies, which is the metric that actually matters for research agents. Second, the model is small by frontier standards, suggesting the gains come from the paradigm rather than raw scale.

## Why this matters for the deep-research-agent race

The past year has seen deep research agents move from demos to default features across the industry, and most of the engineering attention has gone to the agent's brain: better planning, longer context, more capable reasoning models. AgentIR points at a different bottleneck. If the retriever the agent calls is deaf to the agent's reasoning, then every planning improvement upstream gets throttled at the search boundary.

That reframes retrieval as a first-class citizen of the agent stack rather than a commodity API behind it. It also has an efficiency angle that will appeal to teams watching inference budgets: a reasoning-aware 4B model beating a conventional 8B-class retriever implies that architecture matched to the workload can substitute for scale. For anyone running agents at volume, a smaller retriever that returns better documents on the first call means fewer search iterations, fewer tokens, and shorter task latency.

The authors have released code and data at the project page, texttron.github.io/AgentIR, which lowers the bar for others to test whether reasoning-aware retrieval generalizes beyond BrowseComp-Plus and Tongyi-DeepResearch.

## What to watch

Three questions will decide whether AgentIR becomes a pattern or a paper. First, does the approach hold up with closed frontier agents and other benchmarks, or is the 68% partly a happy pairing with Tongyi-DeepResearch? Second, does DR-Synth's synthetic training data transfer to the messy, adversarial reasoning traces real agents produce in the wild, where thoughts wander and contradict themselves? Third, will retrieval vendors and open-source stacks adopt reasoning-aware embeddings, given that it requires the agent and the retriever to share a richer interface than today's query-string handoff?

If the answers trend positive, the "search box" abstraction that has defined information retrieval for decades may finally give way to something built for readers who think in paragraphs, even when those readers are machines.
