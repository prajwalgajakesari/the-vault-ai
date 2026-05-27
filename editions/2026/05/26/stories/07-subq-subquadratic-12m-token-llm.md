---
headline: "SubQ Ships First Commercial Subquadratic LLM With 12 Million Token Context Window"
slug: subq-subquadratic-12m-token-llm
category: llms-genai
story_number: "07"
date: 2026-05-26
sources:
  - name: SiliconANGLE
    url: https://siliconangle.com/2026/05/05/subquadratic-launches-29m-bring-12m-token-context-windows-ai/
  - name: The New Stack
    url: https://thenewstack.io/subquadratic-12-million-context-window/
  - name: eWeek
    url: https://www.eweek.com/news/subquadratic-subq-12m-token-llm-neuron/
  - name: DataCamp
    url: https://www.datacamp.com/blog/subq-ai-explained
  - name: AlphaMatch
    url: https://www.alphamatch.ai/blog/subquadratic-subq-29m-12m-token-context-2026
  - name: Codersera
    url: https://codersera.com/blog/subq-12m-token-subquadratic-llm-2026/
---

# SubQ Ships First Commercial Subquadratic LLM With 12 Million Token Context Window

Every large language model shipped in the past decade has run on the same basic engine: the dense-attention transformer, where every token in a prompt is compared against every other token. Double the input and you quadruple the compute. That constraint has kept production context windows pinned at 128,000 tokens for most models and capped even frontier systems at one million. Now a Miami startup called Subquadratic claims it has shattered that ceiling -- shipping the first commercial LLM built on a fully subquadratic attention mechanism, with a context window stretching to 12 million tokens.

The company launched on May 5 with $29 million in seed funding and a flagship model called SubQ, built on a proprietary architecture it calls Subquadratic Sparse Attention, or SSA. Rather than forcing every token to attend to every other token, SSA uses content-dependent routing to identify which token relationships actually matter and computes attention only over those pairs. The result, Subquadratic claims, is a model that scales linearly -- not quadratically -- in both compute and memory as context length grows.

## How SSA Breaks the Quadratic Wall

The core problem is arithmetic. In standard dense attention, a prompt of n tokens generates n-squared comparisons. At one million tokens the figure balloons to one trillion. Every frontier model from OpenAI, Anthropic, and Google has engineered workarounds -- FlashAttention, sliding-window attention, RAG pipelines -- but none has replaced the underlying quadratic math.

SSA takes a different route. For each token the model computes a lightweight similarity score against all other tokens, then routes full attention only to the top-k most relevant positions. Crucially, the selection mechanism itself runs in linear time, avoiding a trap that caught earlier sparse-attention designs where the indexing step was still quadratic.

"We are very focused on the problem of how we transition from a dense attention, quadratic scaling architecture to a sparse attention linear architecture," CEO Justin Dangel told SiliconANGLE. "Sparse attention is an effort to say, hey, let us try to figure out how to not compare every token to every token to every token."

CTO Alexander Whedon, formerly head of generative AI at Meta, added context on why the routing must be dynamic: "For prompt A, words one and six are going to be important to each other. For prompt B, maybe it is words two and three. It is different for every prompt."

## The Benchmarks -- and the Fine Print

The numbers Subquadratic has published are eye-catching. On the RULER 128K long-context benchmark, SubQ scored 95 percent accuracy at a reported cost of roughly eight dollars, compared with 94 percent accuracy and approximately $2,600 for Claude Opus -- a 300-fold cost reduction. At one million tokens, the company says SubQ runs 52 times faster than FlashAttention-based models and costs about one-fifth of what comparable frontier systems charge. Extrapolated to the full 12-million-token window, Subquadratic claims a nearly 1,000-fold reduction in compute requirements versus dense-attention alternatives.

On coding benchmarks, SubQ scored 81.8 percent on SWE-Bench Verified, edging past Gemini 3.1 Pro at 80.6 percent but trailing Claude Opus 4.7 at 87.6 percent and GPT-5.5 at 88.7 percent. On the MRCR v2 eight-needle retrieval test at one million tokens, SubQ posted 65.9 percent in production -- competitive with GPT-5.5 at 74 percent and well ahead of Claude Opus 4.7 at 32.2 percent, though a notable 17-point gap between the company's internal research score of 83 percent and its deployed figure remains unexplained.

Independent verification is still pending. AI engineer Will Depue observed publicly that SubQ appears to be a sparse-attention fine-tune of an existing open-source base model and questioned whether the efficiency gains fully hold up. Subquadratic has acknowledged building on open-source foundations -- pragmatic for an 11-person team -- but maintains that the SSA layer and reinforcement-learning pipeline are the core innovations.

## Three Products, One Bet on Context

Subquadratic is shipping three products around the SubQ model. The SubQ API gives developers and enterprise teams access to the full 12-million-token window through OpenAI-compatible endpoints. SubQ Code is a command-line coding agent designed to ingest entire repositories into a single context window, eliminating multi-agent coordination overhead. SubQ Search is a free deep-research tool aimed at long-context knowledge work -- a land-and-expand play targeting enterprise analysts. The model will not be open-source in the near term but will support customer-specific fine-tuning. Pricing details have not been published.

## Why Subquadratic Attention Matters Beyond SubQ

Even skeptics acknowledge that the direction Subquadratic is pushing addresses one of the most consequential bottlenecks in modern AI. Today's production systems spend enormous engineering effort on RAG pipelines, chunking strategies, and agentic orchestration layers whose sole purpose is to work around limited context windows. Each layer adds latency, complexity, and potential for information loss.

If linear-scaling attention proves reliable at multi-million-token lengths, much of that infrastructure becomes optional. Entire codebases, legal archives, and research corpora could be processed in a single pass without brittle data curation. The economics shift too: tasks previously reserved for high-budget enterprise deployments become accessible to smaller teams.

The $29 million seed round reflects investor conviction in that thesis. Backers include Javier Villamizar, former partner at SoftBank Vision Fund; Justin Mateen, co-founder of Tinder; and early investors in Anthropic, OpenAI, Stripe, and Brex.

## What to Watch Next

Subquadratic has publicly targeted a 50-million-token context window by Q4 2026 -- a goal that, if the architecture truly scales linearly, is technically plausible but commercially uncharted territory. The more immediate test is whether third-party benchmarks and real-world developer adoption confirm the efficiency and accuracy claims the company has staked its reputation on. Until independent researchers reproduce the results and production pricing becomes transparent, SubQ remains a bold architectural bet with genuinely exciting -- but still unproven -- implications for the future of large language models.

"The fundamental scaling laws imposed by the transformer architecture and dense attention have been broken through," Dangel declared at launch. The AI industry is now watching to see if the math agrees.
