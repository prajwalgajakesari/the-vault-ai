---
headline: "NVIDIA's Nemotron TwoTower Is a Diffusion Language Model That Claims Near-Lossless Quality at 2.4x Speed"
slug: nvidia-nemotron-twotower-diffusion
category: llms-genai
story_number: 09
date: 2026-07-02
---

# NVIDIA's Nemotron TwoTower Is a Diffusion Language Model That Claims Near-Lossless Quality at 2.4x Speed

For six years, nearly every large language model shipped has worked the same way: predict one token, append it, predict the next. That left-to-right march is elegant and provably reasonable, but it imposes a hard latency floor. No amount of GPU horsepower lets a model skip ahead. On July 1, NVIDIA published an open-weight attempt to break that floor without throwing away the models the industry has already spent billions training.

The release, **Nemotron-Labs-TwoTower**, is a diffusion language model that reports retaining **98.7% of its autoregressive baseline's benchmark quality while delivering 2.42x higher wall-clock generation throughput**. The weights are on Hugging Face in BF16 under NVIDIA's Nemotron Open Model License, and the accompanying paper lays out an architecture that is unusual even by the standards of a fast-moving subfield.

## What A Diffusion Language Model Actually Does

Autoregressive (AR) models generate text serially: each token must wait for the one before it. Diffusion language models take a different route borrowed from image generation. They start with a block of masked, placeholder tokens and refine them in parallel over several denoising steps, committing many tokens at once instead of one at a time. That is why a model can run multiple denoising passes and still finish faster than a serial decoder — early in refinement it commits several tokens per step.

The idea is not NVIDIA's alone. The startup Inception Labs, founded by Stanford researchers Stefano Ermon and Chenlin Meng, shipped Mercury in early 2025 as the first commercial diffusion LLM, reporting more than 1,000 tokens per second on a single H100. Google followed at I/O 2025 with Gemini Diffusion, and the open-source LLaDA project demonstrated an 8-billion-parameter mask-diffusion model trained from scratch that rivaled Llama 3 8B. The catch across the field has been quality: diffusion models trained from scratch tend to trail their AR peers, and retraining a frontier model from zero to get diffusion behavior is prohibitively expensive.

## The Two-Tower Trick

NVIDIA's contribution is a way to get diffusion speed on top of an existing autoregressive model without a full re-pretrain. As the paper frames it, TwoTower "decouples context representation and iterative denoising into two towers." One tower — a frozen AR "context" tower — reads the prompt and already-committed tokens causally, exactly as a normal LLM would. The second, trainable "denoiser" tower refines the noisy, masked blocks using bidirectional attention within each block, cross-attending layer-by-layer to the frozen context tower's representations.

Both towers begin as copies of the same backbone, **Nemotron-3-Nano-30B-A3B**, a hybrid model that interleaves Mamba-2, self-attention, and mixture-of-experts layers. Each tower carries 52 layers and roughly 30 billion parameters, of which only about **3 billion are active per token** thanks to the MoE routing (6 of 128 routable experts fire, plus 2 shared experts). Critically, only the denoiser is trained; the context tower stays frozen, preserving the capability the backbone learned during pretraining.

The economics are the point. According to the paper, the denoiser was trained on roughly **2.1 trillion tokens — a fraction of the 25 trillion** used to pretrain the backbone. NVIDIA describes the result as "converting token-by-token decoding into iterative block refinement" while reusing the structure learned during autoregressive pretraining. In other words, the company is trying to retrofit diffusion onto the enormous sunk cost of AR pretraining rather than starting over.

## The Numbers, And The Fine Print

At NVIDIA's default operating point (confidence threshold gamma=0.8, block size 16, running on two H100 GPUs), the diffusion model tracks its AR twin closely. MMLU slips from 78.56 to 78.24; WinoGrande and RACE are unchanged; ARC-Challenge actually improves. The degradation concentrates in code and math, where it hurts most: HumanEval drops from 79.27 to 75.58, and MATH-500 falls from 84.40 to 80.60. That 1.3% aggregate quality cost buys the 2.42x throughput gain. Push throughput past roughly 3x by lowering the threshold, and quality erodes further.

One checkpoint exposes three decoding modes — full mask diffusion, a "mock autoregressive" mode, and standard AR — letting teams run diffusion for bulk generation and fall back to exact AR scoring or speculative decoding from the same weights. The tradeoff is memory: full two-tower diffusion needs two GPUs at about 59 GB each, and the released checkpoint is a base model, not instruction-tuned or aligned.

## Why It Matters

The significance is less the raw speed and more the method. If diffusion behavior can be bolted onto a frozen AR backbone for under a tenth of the original pretraining budget, the quality gap that has kept diffusion LMs in the "promising but not quite" category becomes a tuning problem rather than a foundational one. That reframes diffusion from a competing paradigm you must commit to from scratch into an optional decoding mode you can add to models you already own.

It also fits NVIDIA's strategic posture. The company sells the GPUs everyone else's inference runs on, so anything that makes latency-sensitive workloads — real-time code completion, agentic loops, high-volume synthetic-data generation — more efficient on its hardware expands the addressable market rather than threatening it. Open-weighting the model under a commercial license seeds the ecosystem and pressures rivals whose diffusion efforts, like Gemini Diffusion, remain closed.

The honest caveat is that these are self-reported benchmarks on a base model, and the softest spots are exactly the reasoning-heavy tasks that agentic products lean on. A 4-point drop on MATH-500 matters more than a 0.3-point drop on MMLU.

## What To Watch

Three things will tell whether TwoTower is a milestone or a footnote. First, whether independent evaluations reproduce the 98.7% figure once the model is instruction-tuned and thrown at real workloads. Second, whether the two-tower recipe generalizes to larger backbones and to other labs' AR checkpoints — the architecture's whole promise is portability. And third, whether the throughput advantage survives contact with the serving stacks that matter, where batching and memory pressure often decide the winner. If it holds, the six-year reign of strictly serial decoding may finally have a credible, open, and cheap-to-adopt alternative.

---

**Sources:** [NVIDIA Nemotron-Labs-TwoTower on Hugging Face](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16), [Nemotron-TwoTower paper (arXiv:2606.26493)](https://arxiv.org/abs/2606.26493), [NVIDIA AI announcement on X](https://x.com/NVIDIAAI/status/2072394812301480067), [MarkTechPost coverage](https://www.marktechpost.com/2026/07/01/nvidia-releases-nemotron-labs-twotower/), [Mercury (Inception Labs, arXiv:2506.17298)](https://arxiv.org/abs/2506.17298), [LLaDA (arXiv:2502.09992)](https://arxiv.org/abs/2502.09992)
