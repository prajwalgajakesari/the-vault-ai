---
title: Vector Core Compute Emerges With Disaggregated Architecture for Enterprise AI Inference
slug: vector-core-compute-disaggregated-inference
category: research
story_number: 13
date: 2026-06-02
---

# Vector Core Compute Emerges With Disaggregated Architecture for Enterprise AI Inference

A new inference cloud backed by Vista Equity Partners and Cambium Capital debuted at Computex 2026 with what its founders call the first commercially deployed disaggregated inference system -- splitting prefill, decode, and orchestration across three different processor architectures simultaneously.

## The Big Picture

The AI industry has spent billions optimizing model training. Now, as production inference workloads explode alongside the rise of agentic AI, a consortium of private equity, chip vendors, and cloud upstarts is betting that the next frontier is not faster GPUs but smarter system architecture.

Vector Core Compute, unveiled on stage at Computex 2026 in Taipei, demonstrated a fully disaggregated inference stack running live from its data center in Los Angeles, California. The system uses Intel Xeon 6 processors for orchestration and execution, SambaNova SN40 Reconfigurable Dataflow Units for bandwidth-intensive decode operations, and NVIDIA Blackwell GPUs for compute-heavy prefill -- all working in concert on a single inference request.

The result, according to third-party benchmarking by Artificial Analysis, is the fastest enterprise inference on the MiniMax 2.5 model of any architecture tested to date.

## Why Disaggregation Matters

Traditional inference deployments treat the GPU as a monolithic resource: a model is loaded into GPU memory and the accelerator handles every phase of token generation. This approach leaves expensive silicon idle during phases it was not optimized for.

Disaggregated inference breaks this paradigm by routing each phase of the inference pipeline to the hardware best suited for it. Prefill -- the initial processing of a prompt -- is compute-bound and maps well to NVIDIA Blackwell GPUs. Decode -- generating tokens one at a time -- is memory-bandwidth-bound and runs efficiently on SambaNova's dataflow architecture. Orchestration and tool execution for agentic workloads remain on general-purpose Intel Xeon CPUs.

According to The Register's analysis, this architecture boosts per-user token output by 2-3x compared to monolithic GPU deployments.

"For more than five decades, Intel, its ecosystem partners, and Taiwan have brought the world the foundational technologies for the PC, Internet, and now AI eras," said Lip-Bu Tan, CEO of Intel. "Today, with the rise of inference, agentic, and physical AI, Intel is poised to bring the world new innovations from the chip to systems level that promise to transform industry and society for the better."

## The Business Model

Vector Core Compute is structured as a purpose-built enterprise inference cloud -- a so-called "agentic neocloud" -- rather than a general-purpose cloud provider. The company is backed by Vista Equity Partners and Cambium Capital, with Vista securing early access to Vector Core Compute's inference solutions for its 90-plus portfolio companies, which collectively serve more than 2.5 million enterprise customers and 750 million users worldwide.

Together.ai has signed on as the first commercial customer, running production workloads on the platform. The choice of Together.ai -- itself a well-known inference optimization company -- lends credibility to the architecture's performance claims.

Creative Strategies CEO and principal analyst Ben Bajarin framed the shift in infrastructure terms: while "the training-era world looked closer to a one-CPU-per-four-GPU relation in AI deployments, agentic inference changes that relationship to roughly a one-CPU-to-one-GPU (or less) ratio."

## Competitive Landscape

Vector Core Compute enters a rapidly evolving inference market. NVIDIA itself has partnered with Groq to create disaggregated rack systems using Groq's Language Processing Units. AWS is exploring similar splits with Trainium and Cerebras waferscale accelerators. Intel, SambaNova, and Foxconn also announced separate rackscale AI infrastructure blueprints at the same event, supporting up to 36,864 CPU cores in a single 100-kilowatt rack.

The differentiator for Vector Core Compute is its private-equity-backed go-to-market strategy. Rather than selling raw compute, the company is positioning as an inference utility for enterprise software portfolios -- a model that could scale rapidly if Vista's portfolio companies adopt the platform as their default inference backend.

## What to Watch

The disaggregated inference model is still early. Key questions remain: How does the system handle latency across physically separated accelerators? What happens to efficiency at lower utilization rates? And can a multi-vendor hardware stack deliver the reliability enterprises demand?

But the signal from Computex is clear. As inference costs dominate AI budgets and agentic workloads demand more CPU-side orchestration, the era of one-size-fits-all GPU clusters may be giving way to purpose-built, heterogeneous inference infrastructure.

---

*Sources: Intel Newsroom, Data Center Dynamics, The Register, BusinessWire*
