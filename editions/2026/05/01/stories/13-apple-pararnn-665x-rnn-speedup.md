---
headline: "Apple's ParaRNN Achieves 665x Speedup for Recurrent Neural Network Training at ICLR 2026"
slug: apple-pararnn-665x-rnn-speedup
category: research
story_number: "13"
date: 2026-05-01
---

# Apple's ParaRNN Achieves 665x Speedup for Recurrent Neural Network Training at ICLR 2026

Recurrent neural networks may have just gotten a second life. Apple researchers presented ParaRNN at the International Conference on Learning Representations (ICLR) in Rio de Janeiro last week, unveiling a framework that achieves a 665-fold speedup over traditional sequential RNN training -- and demonstrating, for the first time, that classical RNN architectures can be scaled to 7 billion parameters with language modeling performance competitive with transformers. The paper, accepted as an Oral presentation at ICLR 2026, could reshape the competitive landscape of sequence modeling architectures that has been dominated by transformers for nearly a decade.

## The Parallelization Breakthrough

The fundamental problem with RNNs has always been parallelization. Unlike transformers, which can process all tokens in a sequence simultaneously through their attention mechanism, RNNs must be unrolled step-by-step -- each hidden state depends on the one before it. This sequential bottleneck made it effectively impossible to train RNNs at the billion-parameter scales that have become standard for modern large language models.

State Space Models (SSMs) like Mamba partially addressed this by using structured linear recurrences that can be parallelized, but the linearity constraint limits their expressive power. As the Apple research team wrote in their paper: "Must we sacrifice expressivity for speed, or can we have both?"

ParaRNN answers that question by casting the entire sequence of nonlinear recurrence relationships as a single system of equations, then solving them in parallel using Newton's method combined with custom parallel reductions. The key insight is that each Newton iteration effectively reduces to computing a linear State Space Model, which can be solved efficiently via parallel scan. The researchers found that convergence is achieved consistently with just three iterations -- meaning three carefully designed parallel SSM applications can recover the same hidden state evolution as a full sequential nonlinear RNN pass.

"Scalability was the missing piece in the RNN puzzle all along," the research team wrote in their technical overview. "At billion scale, they perform as well as modern language models, and boast superior expressivity and faster throughput to boot."

## The Numbers

The results are striking. ParaRNN's implementation achieves speedups of up to 665x over naive sequential application of recurrent layers. The researchers applied their framework to adaptations of two classical RNN architectures -- the GRU (Gated Recurrent Unit) and LSTM (Long Short-Term Memory) -- training models ranging from 400 million to 7 billion parameters on language modeling tasks.

At the 7B scale, both ParaGRU and ParaLSTM achieved perplexity scores comparable to similarly-sized transformers and Mamba2 architectures. On downstream task performance, the parallelized RNNs matched or exceeded state-of-the-art SSMs, with notably superior performance on state tracking and recall tasks over purely linear RNNs like Mamba.

The real advantage emerges at inference time. Unlike transformers, whose computational cost grows quadratically with sequence length due to the attention mechanism, RNNs require constant compute per token regardless of context length. This means maintaining high throughput even as sequences grow longer -- a critical advantage for deployment scenarios where fast generation is paramount.

## Open Source and Implications

Apple has released the ParaRNN codebase as an open-source framework on GitHub, designed as a fully modular, PyTorch and CUDA-based software package. The framework is built to be extensible: researchers can define a custom RNN cell by implementing its recurrence step, and ParaRNN handles the parallelization automatically. The release includes multiple backend options, from a pure PyTorch mode for prototyping to optimized implementations for production scale.

Federico Danieli, the paper's lead author, delivered the Apple Expo Talk at ICLR 2026, presenting ParaRNN alongside other Apple research including SHARP and on-device AI demonstrations. The paper was co-authored by Pau Rodriguez, Miguel Sarabia, Xavier Suau, and Luca Zappella.

## Analysis: RNNs Are Back -- But It's Complicated

The implications of ParaRNN extend well beyond a single benchmark result. For years, the AI research community has treated the transformer's dominance as essentially settled. SSMs like Mamba opened a crack in that consensus by showing that recurrent-style architectures could compete at scale, but their reliance on linear recurrences was seen as a fundamental expressivity limitation.

ParaRNN removes that constraint entirely. By enabling nonlinear RNNs to train at transformer-competitive speeds, Apple has effectively reopened a question many researchers had closed: whether the transformer's architectural advantages are inherent, or simply a consequence of computational limitations that favored parallelizable designs.

The inference efficiency angle is particularly relevant for Apple's business. The company's AI strategy depends heavily on on-device deployment, where memory and compute budgets are tightly constrained. RNNs' constant-time token generation and lower memory footprint compared to attention-based models make them natural candidates for running language models on iPhones and other Apple hardware.

That said, competitive perplexity at 7B parameters is a necessary but not sufficient condition for displacing transformers. The real test will be whether parallelized nonlinear RNNs can match transformer performance on the full range of capabilities that matter for production LLMs -- instruction following, reasoning, long-context retrieval, and multimodal understanding. The ParaRNN paper focuses on language modeling perplexity and a limited set of downstream tasks, leaving these broader questions open.

## What to Watch

The open-source release is the most consequential near-term development. By lowering the barrier to experimenting with nonlinear RNNs at scale, Apple is effectively crowdsourcing the answer to whether these architectures can truly compete with transformers across the full spectrum of modern AI applications. Watch for independent reproductions and extensions in the coming months -- and for whether Apple integrates ParaRNN-trained models into its own on-device AI stack. The RNN may not be dead after all; it was just waiting for the right algorithm.
