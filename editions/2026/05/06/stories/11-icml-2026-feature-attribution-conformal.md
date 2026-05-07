---
title: "ICML 2026 Accepts Breakthrough Papers on Feature Attribution and Robust Prediction"
slug: icml-2026-feature-attribution-conformal
category: research
story_number: 11
date: 2026-05-06
author: The Vault AI Staff
tags: [icml, machine-learning, explainability, conformal-prediction, generative-ai, kaist]
---

# ICML 2026 Accepts Breakthrough Papers on Feature Attribution and Robust Prediction

As the machine learning community digests the results of ICML 2026's record-breaking review cycle, a trio of papers from KAIST's Statistical Artificial Intelligence Laboratory highlights an unmistakable trend: the field's center of gravity is shifting from raw performance toward trustworthiness, interpretability, and diversity in AI systems.

The International Conference on Machine Learning, which will convene this July at Seoul's COEX Convention Center, accepted 6,352 papers from a staggering 23,918 submissions this year — a 26.6 percent acceptance rate drawn from a pool that nearly doubled compared to 2025. Within that fiercely competitive landscape, KAIST's SAIL Lab, led by Professor Jaesik Choi, secured three acceptances that collectively address some of the most pressing open questions in deployed machine learning.

## Making Attribution Maps Trustworthy

The first paper, "Manifold-Aligned Guided Integrated Gradients for Reliable Feature Attribution," by Soyeon Kim, Seongwoo Lim, Kyowoon Lee, and Jaesik Choi, tackles a long-standing weakness in explainable AI. Integrated Gradients — one of the most widely used methods for explaining neural network decisions — works by tracing a path from a baseline input to the actual input and accumulating gradients along the way. The problem is that this straight-line path often passes through regions of the input space that are off the data manifold, producing attribution maps that highlight features no real-world example would ever contain.

The KAIST team's solution aligns the integration path with the underlying data manifold, ensuring that every intermediate point along the attribution path remains realistic. The result is feature importance maps that are not only mathematically principled but also correspond to meaningful variations a domain expert would recognize. For practitioners deploying models in healthcare, finance, or autonomous systems — where regulators increasingly demand explanations — this represents a significant step toward attribution methods that can withstand scrutiny.

## Robust Prediction Under Distribution Shift

The second acceptance, "DistMatch: Adaptive Binning via Distribution Matching for Robust Sequential Conformal Prediction," by Enver Menadjiev, Jihyeon Seong, Jisu Yeo, and Jaesik Choi, addresses the reliability of uncertainty quantification in streaming settings. Conformal prediction has emerged as a popular framework for wrapping any model's point predictions in statistically valid confidence intervals without distributional assumptions. However, most conformal methods assume exchangeability — a condition that breaks down the moment data arrives sequentially and distributions shift over time.

DistMatch introduces an adaptive binning strategy that matches the empirical distribution of conformity scores to a target distribution, preserving coverage guarantees even as the generating process evolves. For applications ranging from financial forecasting to clinical monitoring, where models must flag when they are uncertain rather than silently degrade, robust sequential conformal methods could become essential safety infrastructure.

## Breaking Generative Lock-In

The third paper, "Breaking the Lock-in: Diversifying Text-to-Image Generation via Representation Modulation," by Dahee Kwon, Haeun Lee, and Jaesik Choi, confronts a subtler failure mode of modern generative models. Large-scale text-to-image diffusion models tend to converge on a narrow set of visual stereotypes for any given prompt — a phenomenon researchers call mode lock-in. The same prompt repeatedly produces nearly identical compositions, lighting, and subject appearances.

The team's approach modulates internal representations during the generation process to encourage diversity without sacrificing quality or prompt fidelity. As generative AI moves from research demos into production creative tools, the ability to produce varied, non-repetitive outputs becomes a commercial requirement and a fairness concern alike.

## The Bigger Picture

Taken together, these three papers illustrate a maturation of the machine learning research agenda. The field spent the last decade demonstrating that deep networks can achieve superhuman accuracy on benchmarks; the next chapter is proving that these systems can be trusted, understood, and controlled in the wild.

ICML 2026's overall program reflects this shift. With nearly 24,000 submissions — up from roughly 12,000 last year — the conference has become the largest venue for peer-reviewed machine learning research. The organizers introduced new transparency policies this cycle, publishing anonymized reviews and rebuttals for all accepted papers, signaling that the community itself is embracing accountability.

For industry practitioners, the message is clear: interpretability, calibration, and output diversity are no longer niche academic concerns. They are table stakes for any organization shipping AI into high-consequence environments. The KAIST SAIL Lab's hat trick at ICML 2026 is one data point among many, but it points squarely in the direction the field is headed.

*ICML 2026 takes place July 6-11 at the COEX Convention & Exhibition Center in Seoul, South Korea.*
