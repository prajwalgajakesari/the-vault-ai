---
headline: "The Other Diffusion Win at ICML Was Theoretical, and It Makes Every Sampler Cheaper"
slug: icml-high-accuracy-diffusion-sampling
category: research
story_number: 12
date: 2026-07-20
---

# The Other Diffusion Win at ICML Was Theoretical, and It Makes Every Sampler Cheaper

Every image a diffusion model generates is the end of a countdown. Twenty steps, fifty steps, a thousand steps — each one a full forward pass through a neural network, each one billed to somebody's GPU. That step count is the single dominant cost of generative media inference, and for four years the theory community has been unable to say whether it needed to be that high.

At ICML 2026 in Seoul, it answered. Alongside the conference's flashier diffusion win — a Tsinghua-led paper puncturing the arbitrary-order hype in diffusion language models — the Outstanding Paper Award also went to "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions," by Fan Chen, Constantinos Daskalakis and Alexander Rakhlin of MIT and Sinho Chewi of Yale. It contains no benchmarks, no model releases, and no code. What it contains is a proof that the denoising step count can, in principle, collapse from polynomial to polylogarithmic in the target error.

The authors do not hedge in the abstract. Their algorithm reaches δ-error in polylog(1/δ) steps given score estimates accurate to Õ(δ) in L2 — and, they write, "this is an exponential improvement over all previous results."

## What "high-accuracy" actually means

The jargon is unusually literal. A sampler's cost is measured in queries to the score function — the gradient of the log-density, which in a diffusion model is exactly what the denoising network computes. "Complexity bounds which scale as polylog(1/δ), indicating that algorithms converge exponentially fast, are known as 'high-accuracy' guarantees," the paper explains, "as they ensure that one can draw an extremely accurate sample without too many iterations."

The baseline is far worse. The foundational 2023 analysis of DDPMs by Chen, Chewi and coauthors established a query complexity of 1/δ² in total variation distance — halve your error, quadruple your steps. That penalty is not an artifact of loose analysis. It comes from discretization: diffusion samplers approximate a continuous reverse-time stochastic differential equation with finite steps, and, as the paper puts it, "the need to control the discretization error precludes high-accuracy guarantees." The authors flag the contrast with optimization, where gradient descent converges exponentially under strong convexity because discretization there does not bias the answer. In sampling, it biases the stationary distribution itself.

Classical MCMC has always had an escape hatch: Metropolis-Hastings, which corrects bias by accepting or rejecting proposals based on density ratios. But diffusion models never learn a density. They learn only its gradient. That is the trap the field has been stuck in — the correction mechanism requires information the architecture does not produce.

## The Bernoulli factory trick

The paper's answer is First-Order Rejection Sampling, or FORS: a training-free meta-algorithm that simulates an accept-reject test using score queries alone. The construction routes through a "Bernoulli factory," a device for flipping a coin with a probability you can only estimate, never evaluate. The unknown log-density ratio is written as a line integral along a randomized path between the candidate sample and a proximal base point; differences in the score function evaluated along that path give unbiased estimates of the integrand. Draw a Poisson number of independent paths, multiply the clipped estimates together, and the acceptance probability comes out exactly right — the Taylor series of the exponential does the work.

The resulting bounds are the headline. Under minimal data assumptions — essentially a finite second moment — the complexity is Õ(d⋆ polylog(1/δ)), where d⋆ is the *intrinsic* dimension of the data rather than the ambient pixel count. Under a non-uniform L-Lipschitz condition it falls further, to Õ(L polylog(1/δ)), which is effectively dimension-free. As a byproduct, the paper delivers the first polylog(1/δ) sampler for general log-concave distributions — the workhorse family in Bayesian inference, where "log-concave" simply means the log-density is concave, a single-peaked, no-hidden-valleys shape that makes sampling tractable — using only gradients.

## Analysis: what this is and is not worth

The ICML committee was careful with its verbs. The result "settles a long-standing question in the theory of score-based sampling," its citation reads, and "for diffusion models specifically, the result shows that the number of denoising steps (score-function evaluations) needed to reach a target sample accuracy can in principle drop from polynomial to polylogarithmic in 1/ε, suggesting that highly accurate diffusion sampling can be obtained with a smaller number of function evaluations."

*In principle* is load-bearing. Nobody has run FORS on a production image or video model. Rejection samplers degrade badly in high dimensions when the proposal drifts from the target — acceptance rates crater and wall-clock time becomes variable. The clipping parameter that keeps the estimator bounded introduces bias when the score fluctuates locally, and the analysis assumes L2-accurate scores everywhere, including the out-of-distribution regions where real denoisers are worst.

But the economics of the target are not in doubt. Inference for generative media is priced almost entirely in function evaluations, and every practical trick the field has adopted — distillation, consistency models, higher-order ODE solvers, learned schedules — is an empirical attack on the same quantity, usually trading fidelity for speed. This paper says the tradeoff is not fundamental: the poly(1/δ) wall was an artifact of how we discretize, not a law about what score functions can tell you.

## What to watch

The obvious next move is an implementation. FORS is training-free and architecture-agnostic by construction, which means a competent engineer can bolt it onto an existing sampler as a correction step and measure the acceptance rate empirically — the number that will decide whether the theory survives contact with a 1024×1024 latent space. Watch also for the concurrent line of work: Gatmiry et al. reached high-accuracy guarantees under a stronger sub-exponential score assumption, and Chewi's group published a companion COLT 2026 paper on high-accuracy log-concave sampling with stochastic queries. If the acceptance rates hold up in even a restricted regime, the cheapest inference optimization of 2027 may turn out to have been written in 2026 with no experiments at all.
