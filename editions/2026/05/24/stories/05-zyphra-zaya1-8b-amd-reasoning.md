---
title: "Zyphra Releases ZAYA1-8B Open Source Reasoning Model Trained on AMD Hardware"
slug: zyphra-zaya1-8b-amd-reasoning
category: llms-genai
date: 2026-05-24
story_number: "05"
sources:
  - name: "Zyphra Official Blog"
    url: "https://www.zyphra.com/post/zaya1-8b"
    domain: "zyphra.com"
  - name: "PR Newswire Press Release"
    url: "https://www.prnewswire.com/news-releases/zyphra-releases-zaya1-8b-a-reasoning-model-trained-on-amd-and-optimized-for-maximum-intelligence-density-per-parameter-302764700.html"
    domain: "prnewswire.com"
  - name: "MarkTechPost"
    url: "https://www.marktechpost.com/2026/05/06/zyphra-releases-zaya1-8b-a-reasoning-moe-trained-on-amd-hardware-that-punches-far-above-its-weight-class/"
    domain: "marktechpost.com"
  - name: "VentureBeat"
    url: "https://venturebeat.com/technology/meet-zaya1-8b-a-super-efficient-open-reasoning-model-trained-on-amd-instinct-mi300-gpus"
    domain: "venturebeat.com"
---

# Zyphra Releases ZAYA1-8B Open Source Reasoning Model Trained on AMD Hardware

A small AI lab just cracked one of the field's most stubborn assumptions: that frontier-grade reasoning performance requires frontier-scale compute. On May 6, 2026, San Francisco-based Zyphra released ZAYA1-8B, a Mixture-of-Experts language model with only 760 million active parameters that matches or outperforms models many times its size on mathematics and coding benchmarks — and did it without touching a single NVIDIA GPU.

The release marks a significant milestone in two parallel competitions reshaping the AI industry: the race to squeeze maximum intelligence out of minimum compute, and the growing challenge to NVIDIA's near-monopoly on AI training infrastructure. ZAYA1-8B was pretrained, midtrained, and fine-tuned entirely on a cluster of 1,024 AMD Instinct MI300X GPUs interconnected via AMD Pensando Pollara networking, built in collaboration with IBM Cloud — making it the first MoE model to complete its entire training lifecycle on AMD hardware at scale.

## Small Parameter Count, Outsized Results

The numbers are striking. On AIME '26, the prestigious math olympiad benchmark that separates capable reasoning models from genuinely capable ones, ZAYA1-8B scored 89.1 — edging past Qwen3-4B-Thinking-2507's 77.5 and beating Mistral-Small-4-119B's 86.4, a model with 119 billion total parameters and 6 billion active ones. On LiveCodeBench-v6, a rigorous coding evaluation, ZAYA1-8B scored 65.8 against Mistral-Small-4's 57.9.

What makes those numbers remarkable is the denominator. ZAYA1-8B has 8.4 billion total parameters but activates only around 760 million per forward pass — fewer than one billion active parameters at inference time. In a Mixture-of-Experts architecture, only a selected subset of the network's "experts" fires for any given input token. The result is a model that carries the representational capacity of a much larger system while running at a fraction of the memory and compute cost.

Zyphra describes the design philosophy as "maximizing intelligence density per active parameter and per FLOP," and ZAYA1-8B is the clearest proof of that objective to date.

## Three Architectural Innovations

The model's efficiency stems from three distinct innovations baked into Zyphra's MoE++ architecture.

The first is Compressed Convolutional Attention (CCA), a sequence-mixing mechanism that operates in a compressed latent space and delivers an 8x reduction in KV-cache size compared to standard multi-head attention. KV-cache is the memory used to store intermediate attention states during inference — cutting it by 8x directly translates to lower hardware requirements and the ability to handle longer contexts within the same memory budget.

The second is an MLP-based router with PID-controller bias balancing. Standard MoE routers use linear projections to decide which experts handle each token. Zyphra replaces this with a multi-layer perceptron router, adding a proportional-integral-derivative style balancing mechanism to prevent load imbalance across experts — a known failure mode that can destabilize MoE training at scale.

The third is learned residual scaling, a lightweight technique that controls how norms grow as activations pass through successive layers. In deep networks, unchecked residual-norm growth can cause instability. Learned scaling addresses this at negligible parameter and FLOP cost.

## Going All-In on AMD

Beyond the model architecture itself, the AMD story is arguably the more strategically significant headline. Zyphra's full training pipeline — from pretraining on the base model through supervised fine-tuning of the reasoning variant — ran exclusively on AMD silicon. The 1,024-node MI300X cluster, connected via Pensando Pollara networking on IBM Cloud infrastructure, represents the largest-scale demonstration to date that frontier AI workloads can be executed outside NVIDIA's ecosystem.

"ZAYA1-8B is the first MoE model pretrained, midtrained, and supervised fine-tuned on an AMD Instinct MI300 stack," the company stated in its official release announcement. Zyphra added that ZAYA1-8B's "strength demonstrates the power of our post-training stack and we are excited to continue to scale our efforts here both in terms of model size and the breadth and diversity of domains."

The collaboration with AMD and IBM was not incidental. Zyphra co-designed its training infrastructure around AMD silicon, building custom tooling on the ROCm software stack to achieve training throughput competitive with NVIDIA-based alternatives. That co-design effort matters because it signals not just a one-time demonstration but an ongoing commitment to a non-NVIDIA supply chain — and gives enterprise buyers concrete evidence that the MI300X platform is ready for serious workloads.

## A Novel Inference Method Raises the Ceiling Further

Alongside the model weights, Zyphra published details of a new test-time compute scheme called Markovian RSA, which pushes ZAYA1-8B's performance ceiling significantly higher when additional inference budget is available.

The method combines two existing ideas in a novel configuration. Recursive Self-Aggregation (RSA) generates multiple reasoning traces in parallel and merges them iteratively. The Markovian thinker approach breaks reasoning into fixed-length chunks, passing only the tail end of each chunk forward so the context window stays bounded regardless of total reasoning time. Markovian RSA fuses these: multiple parallel traces generate, their tail segments are extracted and sub-sampled into new aggregation prompts, and the cycle repeats.

The practical result is parallelizable inference with bounded context windows — a combination that scales with additional compute without requiring exponentially growing memory. With an extra-high compute budget of 5.5 million tokens per problem, ZAYA1-8B surpasses DeepSeek-V3.2 and GPT-OSS-High on the APEX-shortlist mathematics benchmark. At standard compute settings, ZAYA1-8B already exceeded Claude 4.5 Sonnet and GPT-5-High on HMMT '25, scoring 89.6 versus their 88.3.

Crucially, Zyphra trained ZAYA1-8B specifically to respond to Markovian RSA prompts, starting in supervised fine-tuning and continuing through reinforcement learning. When researchers applied the same inference harness to Qwen3-4B-Thinking without that co-design, the performance uplift was substantially smaller. This finding underlines a principle that will likely define the next phase of reasoning model development: inference-time compute methods only pay off when the training pipeline is built around them from the start.

## Five-Stage Post-Training Pipeline

The model's performance also reflects a carefully staged post-training methodology. Zyphra's pipeline runs through five sequential phases: a foundational supervised fine-tuning stage covering chat, instruction following, code, and math; a reasoning warmup phase mixing mathematical tasks with logic and puzzle solving; a large reinforcement learning phase using an environment Zyphra calls RLVE-Gym with dynamically adjusted puzzle difficulty; a dedicated math and code RL stage; and a final alignment pass using RLHF and RLAIF to improve chat behavior and writing quality.

The reinforcement learning phases produced the most significant capability gains in mathematics and coding, with smaller but meaningful improvements in knowledge retrieval and instruction following — a distribution of outcomes consistent with what other labs have reported when applying RL to reasoning-focused models.

## Open and Available Now

ZAYA1-8B is released under an Apache 2.0 license — the most permissive tier in open-source AI, allowing commercial use without restriction. Model weights are available on Hugging Face. The model is also live as a serverless endpoint on Zyphra Cloud at cloud.zyphra.com, allowing developers to test it immediately without local infrastructure. A full technical report is available on arXiv at arxiv.org/abs/2605.05365.

## The Bigger Picture

The release lands at an inflection point for the industry. The past eighteen months have seen model performance curves steepen through scale, but that phase is increasingly constrained by hardware availability and energy costs. ZAYA1-8B's approach — architectural efficiency, RL-driven capability extraction, and inference-time compute scaling — points toward a different path: extracting more from less, rather than simply adding more of the same.

For AMD, the significance goes beyond one model release. Zyphra's end-to-end training proof-of-concept demonstrates that the MI300X platform can handle the full complexity of a frontier reasoning model's lifecycle, from large-scale pretraining through iterative RL. Each successful demonstration of this kind erodes the narrative that serious AI work requires NVIDIA hardware — and gives the broader ecosystem concrete evidence that alternatives are production-ready.

Whether ZAYA1-8B represents a one-off efficiency breakthrough or the opening chapter of a new architecture paradigm remains to be seen. But the model has already established a data point the field will have difficulty ignoring: under one billion active parameters, trained on AMD, competing with models more than a hundred times its active size. The weight class just changed.
