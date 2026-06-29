When MiniMax pushed M3 into public preview on June 1, it made a claim that the open-weight community has been circling for two years without quite landing: a single model that does frontier-grade coding, holds a million tokens of context, and reads images and video natively — all of it destined for free download. Independent benchmarking has since caught up with the marketing, and the early verdict is that the Shanghai lab is not bluffing.

MiniMax-M3 scores 55 on the Artificial Analysis Intelligence Index, the closely watched composite that blends reasoning, math, science and agentic evaluations. That places it a hair ahead of the strongest open-weight competitors Artificial Analysis has measured — Kimi K2.6 and MiMo-V2.5-Pro, both at 54 — and, as the firm put it, positions M3 to become "the leading open weights model" the moment its weights actually ship. (The lower ~44 figure circulating online refers to M3's non-reasoning variant; the 55 is the model running with reasoning enabled.)

## The architecture bet: sparse attention at a million tokens

M3 is a Mixture-of-Experts model, and the headline number that separates it from M-series predecessors is context. The window jumps to 1M tokens, up from the 200K of MiniMax-M2.7, the text-only model M3 supersedes. Holding that much context without melting a GPU cluster is the hard part, and MiniMax's answer is a new MiniMax Sparse Attention (MSA) design the company says delivers roughly 15.6x faster decoding and 9.7x faster prefill at 1M context compared with M2.

The other structural shift is multimodality. M3 is the first multimodal model in MiniMax's M line, adding image and video input, and the company emphasizes it was trained on mixed-modality data from the start rather than having a vision encoder grafted on afterward. On MMMU-Pro, the multimodal reasoning benchmark, M3 lands around 80% — statistically level with GPT-5.5 (79.9%) and Kimi K2.6 (79.4%), and trailing Gemini 3.5 Flash (84.3%). Native vision remains rare among open-weight releases, which is part of M3's pitch.

Parameter counts reported across secondary write-ups have varied — figures of 229.9 billion total with 9.8 billion active, and 428 billion total with 23 billion active, have both circulated — a reminder that until MiniMax publishes its technical report, the precise configuration is unconfirmed. What is consistent is the sparse-MoE design philosophy: a large pool of fine-grained experts, only a small fraction firing per token.

## Coding, the real battleground

The number generating the most noise is on software engineering. MiniMax reports 59.0% on SWE-Bench Pro, a result the company says edges past frontier closed models on that specific test. Artificial Analysis's own broader battery shows M3 improving on M2.7 nearly across the board: Humanity's Last Exam up nine points to 37%, GPQA Diamond up six to 93%, IFBench up seven to 83%, with a small regression on SciCode (47% to 45%). On GDPval-AA, which scores real-world tasks across 44 occupations, M3 hits roughly 1670 — behind Claude Opus 4.8 (1890) and GPT-5.5 (1769) but level with Claude Sonnet 4.6, and the top open-weight score once weights land.

Not every signal is flattering. On AA-Omniscience, M3 attempts only 30.9% of questions — the lowest among its peers — which buys a low hallucination rate (16.1%) at the cost of low raw accuracy (15.0%). Heavy abstention is a defensible design choice, but it is a choice, and one buyers should understand.

## Cheap, available, but not yet downloadable

Pricing is aggressive: $0.30 per million input tokens and $1.20 per million output up to 512K context, rising to $0.60/$2.40 in the 512K–1M band. That undercuts most closed rivals and several open-weight peers — a GLM-5.2-versus-M3 comparison making the rounds pegs M3 as roughly 3.7x cheaper while conceding GLM leads on several shared coding benchmarks. M3 is live now on MiniMax's first-party API and through SiliconFlow, GMI and Novita.

The asterisk is the one that matters most for an "open-weight" story: the weights are not out yet. MiniMax has stated they will follow within about ten days of launch, alongside a technical report. When the lab released M2.7's weights, it did so under a commercially restricted license — so whether M3 arrives under a permissive MIT or Apache terms, as DeepSeek, GLM and Qwen variants have, or under something more guarded, is an open and consequential question.

## What to watch

The open-weight coding race has tightened into a four-way scrum among MiniMax, DeepSeek, Zhipu's GLM and Alibaba's Qwen, with Moonshot's Kimi crowding the frontier. M3's distinct move is bundling capabilities — coding, ultra-long context, native multimodality — that competitors have so far shipped à la carte. If the weights land permissively and the technical report confirms the sparse-attention efficiency claims, M3 could become the default base model for self-hosted agentic coding overnight. If the license disappoints or the report never fully materializes, M3 risks being remembered as a strong API product that wore "open weight" as a marketing coat. The next ten days decide which.
