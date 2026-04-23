---
headline: "Apple's ParaRNN Achieves 665x Speedup for Nonlinear RNN Training, Accepted as ICLR Oral"
slug: apple-pararnn-665x-rnn-speedup
category: research
story_number: 13
date: 2026-04-22
author: The Vault AI Edition
tags: [apple, rnn, pararnn, iclr-2026, deep-learning, manzano, multimodal]
---

# Apple's ParaRNN Achieves 665x Speedup for Nonlinear RNN Training, Accepted as ICLR Oral

**Cupertino's researchers crack the parallelization problem that has limited recurrent neural networks for decades, enabling the first 7-billion-parameter classical RNNs competitive with transformers.**

As the International Conference on Learning Representations (ICLR) kicks off this week in Rio de Janeiro, Apple is making a bold statement: the era of nonlinear recurrent neural networks being confined to sequential, painfully slow training may be over. The company's ParaRNN framework, accepted as an Oral presentation at ICLR 2026 -- a distinction reserved for roughly the top 1-2% of submissions -- achieves a staggering 665x speedup over traditional sequential training for nonlinear RNNs, a result that could reshape the competitive landscape between RNNs and the transformer architectures that have dominated AI for the past several years.

## Breaking the Sequential Bottleneck

The fundamental challenge with recurrent neural networks has always been their sequential nature. Each hidden state depends on the previous one, creating a chain of dependencies that resists parallelization. While State Space Models (SSMs) like Mamba have sidestepped this problem by constraining themselves to linear recurrences, that linearity comes at a cost: reduced expressive power compared to their nonlinear cousins, which include the venerable LSTM and GRU architectures.

ParaRNN, developed by Apple researchers Federico Danieli, Pau Rodriguez, Miguel Sarabia, Xavier Suau, and Luca Zappella, takes an entirely different approach. Rather than simplifying the recurrence to make it parallelizable, the team reframes the entire sequence of nonlinear recurrence relationships as a single unified system of equations. That system is then solved in parallel using Newton's iterations combined with custom parallel reductions -- a mathematical reformulation that preserves the full nonlinear expressiveness of classical RNNs while unlocking massive computational speedups.

"ParaRNN breaks the sequence-parallelization barrier for nonlinear RNNs," the researchers write in their paper, describing how the framework enables "training at unprecedented scales while maintaining expressiveness advantages over linear alternatives like SSMs."

## 7 Billion Parameters and Counting

The numbers tell a compelling story. The 665x speedup over naive sequential processing is not merely a theoretical benchmark -- the team used it to train adapted LSTM and GRU architectures at a scale of 7 billion parameters, marking what Apple claims are the first classical RNNs of that size. These models achieved perplexity comparable to similarly-sized Transformers and Mamba2 architectures on language modeling tasks, demonstrating that nonlinear RNNs can compete at the frontier when freed from their computational shackles.

Apple has released the ParaRNN codebase as an open-source PyTorch+CUDA library on GitHub, offering three solver implementations: a pure PyTorch reference implementation for accessibility, a CUDA-accelerated version for production use, and a fully-fused CUDA implementation for maximum performance. The open-source release signals Apple's intent to seed a broader research ecosystem around parallelized nonlinear RNNs, rather than keeping the advantage proprietary.

## MANZANO: A Multimodal Companion

ParaRNN is not Apple's only headline at ICLR 2026. The company is also presenting MANZANO, a unified multimodal model built around a hybrid vision tokenizer that bridges image understanding and image generation within a single architecture. Led by a team of over 30 researchers including Yanghao Li, Rui Qian, and Bowen Pan, MANZANO tackles a persistent challenge in multimodal AI: the performance trade-off between understanding images and generating them.

MANZANO's architecture routes a shared vision encoder through two lightweight adapters -- one producing continuous embeddings for image-to-text understanding, the other generating discrete tokens for text-to-image generation. A unified autoregressive LLM handles high-level semantic prediction, while an auxiliary diffusion decoder translates image tokens into pixels. The researchers report that this design exhibits "minimal task conflicts and consistent gains from scaling model size," achieving state-of-the-art results among unified models and competitive performance with specialist systems, particularly on text-rich evaluations.

## Analysis: Why This Matters

ParaRNN's significance extends beyond the immediate speedup numbers. For years, the AI research community has operated under an implicit assumption that transformers won the architecture war -- and that any alternative would need to accept significant compromises. SSMs like Mamba offered efficient inference but traded away nonlinear expressiveness. Classical RNNs retained that expressiveness but could not scale.

ParaRNN challenges that calculus. If nonlinear RNNs can now train at transformer-competitive speeds and scales, the architectural design space for large language models just got substantially wider. RNNs offer inherent advantages for certain workloads: constant memory during inference regardless of sequence length, natural handling of streaming data, and a fundamentally different inductive bias that could prove valuable for tasks where transformers struggle.

The open-source release amplifies the potential impact. By providing production-ready CUDA implementations alongside accessible PyTorch reference code, Apple is lowering the barrier for the broader research community to explore nonlinear RNNs at scale -- something that was simply not feasible before.

## The Bigger Picture

Apple's ICLR 2026 showing -- which also includes Oral presentations on length generalization in SSMs, 3D scene generation with SHARP, and protein folding with SimpleFold -- reflects a research organization that is increasingly willing to publish foundational work and release code. Conference attendees can experience some of this research firsthand at booth #204, where Apple is demonstrating SHARP running on iPad Pro with M5 and local LLM inference on MacBook Pro with M5 Max using the MLX framework.

For the AI research community gathering in Rio this week, the message from Cupertino is clear: the architectural frontier is far from settled, and Apple intends to help redraw the map.

---

*Sources: [Apple Machine Learning Research](https://machinelearning.apple.com/research/pararnn), [arXiv:2510.21450](https://arxiv.org/abs/2510.21450), [Apple ICLR 2026 Overview](https://machinelearning.apple.com/research/iclr-2026), [Apple MANZANO Research](https://machinelearning.apple.com/research/manzano)*
