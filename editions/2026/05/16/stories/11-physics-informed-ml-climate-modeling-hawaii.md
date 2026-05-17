---
title: "University of Hawaii Unveils Physics-Informed ML Algorithm That Advances Climate and Fluid Dynamics Modeling"
slug: physics-informed-ml-climate-modeling-hawaii
category: research
story_number: "11"
date: "2026-05-16"
---

# University of Hawaii Unveils Physics-Informed ML Algorithm That Advances Climate and Fluid Dynamics Modeling

A new generation of machine learning models grounded in the laws of physics is reshaping how scientists simulate climate systems and fluid dynamics — and the University of Hawaiʻi is at the center of the breakthrough.

Researchers working at the confluence of artificial intelligence and atmospheric science have unveiled a physics-informed spatiotemporal deep learning framework capable of replicating the complex, turbulent behavior of convective fluid systems at a fraction of the computational cost of traditional numerical simulations. The advance, published in the *Journal of the American Statistical Association* in early 2026, could meaningfully accelerate climate projections, extreme weather risk modeling, and industrial fluid engineering.

## The Problem With Brute-Force Simulation

Understanding fluid dynamics — whether in ocean currents, thunderstorm cells, or industrial heat exchangers — has long demanded enormous computational resources. Direct numerical simulations (DNS) of turbulent systems must resolve every eddy, every temperature gradient, every chaotic fluctuation down to microscopic scales. For climate scientists studying decades-long trends, this approach is simply untenable. Even with modern supercomputers, running DNS for long-horizon atmospheric models can take weeks or months.

That computational barrier has driven growing interest in surrogate modeling: using machine learning to approximate the behavior of physical systems without solving the governing equations from scratch at every time step. The challenge, however, is that pure data-driven models tend to violate the basic conservation laws that real fluid systems must obey. They can hallucinate physically impossible states, drifting further from reality the longer they run.

Physics-informed machine learning resolves this tension by encoding the governing partial differential equations (PDEs) directly into the training objective. The model is not merely rewarded for matching observed data — it is explicitly penalized whenever its outputs contradict the physics.

## The New Framework: Convection Meets Transformers

The paper, authored by Luca Menicali, Andrew Grace, David H. Richter, and Stefano Castruccio, focuses on Rayleigh-Benard convection (RBC) — a canonical model system in which a fluid layer is heated from below, generating the kind of rolling, turbulent convection cells seen in the atmosphere, oceans, and planetary interiors.

Their architecture combines two powerful but previously separate ideas. Convolutional neural networks handle spatial dimension reduction, compressing the high-resolution field data into a latent representation that captures essential structure without retaining every detail of the simulation domain. Then, a novel recurrent architecture — explicitly inspired by the attention mechanisms underlying large language models — models how that compressed state evolves through time, capturing long-range temporal dependencies that simpler recurrent networks miss.

Crucially, the inference step is penalized with respect to the governing PDEs. If the model predicts a temperature field that violates energy conservation, that error is baked into the loss function. The physics is not just a prior assumption — it is an active training signal at every iteration.

To handle the inherent uncertainty of turbulent systems, the researchers applied a conformal prediction framework, providing statistically rigorous uncertainty bounds around each forecast rather than producing a single deterministic output. The result is a surrogate model that replicates key physical features of RBC dynamics — heat flux, velocity statistics, spatial correlations — while slashing computational cost compared to DNS.

The framework architecture is explicitly designed for generalizability. The authors emphasize that the convolutional structure, recurrent memory, and physics-based loss components are all transferable to other nonlinear systems in thermodynamics, climate, and geophysical flows — a design choice that positions the work as infrastructure for the field rather than a narrow, one-off result.

## UH Manoa's Broader AI Climate Push

The new framework arrives as the University of Hawaiʻi is scaling up its institutional investment in AI-driven climate science on multiple fronts.

Associate Professor Peter Sadowski of UH Manoa's Department of Information and Computer Sciences holds a five-year, $424,293 NSF CAREER grant for research titled "Score-Based Diffusion Models for Probabilistic Forecasting of Weather and Climate." The project applies generative AI techniques — the same class of models that produce realistic images from text — to produce location-specific probabilistic forecasts of extreme weather events, drawing on data from satellites, ground-based stations, and the NSF-funded CHANGE-HI climate simulation project.

"One of the risks of climate change for Hawaiʻi is extreme weather events, and current scientific models are poor at estimating these risks," Sadowski said. "This project will provide a completely new approach modeling these risks, using the latest advancements in AI."

The CHANGE-HI project itself represents a $20 million, five-year NSF award to develop actionable climate science for the Hawaiian Islands — a region particularly vulnerable to sea-level rise, intensifying rainfall events, and drought. Machine learning is central to that effort, with active work on high-resolution rainfall mapping, sea surface temperature forecasting from NOAA buoy data, and long-range climate projections tailored to the Pacific Island context.

In April 2026, UH also launched a new EPSCoR/IDeA Office specifically designed to expand research capacity statewide and amplify the visibility of Hawaii-based science nationally — a structural signal that physics-informed AI for climate is being treated as a long-term institutional priority, not a passing research trend.

## Why Physics-Informed ML Changes the Equation

What distinguishes the current wave of physics-informed models from earlier neural-network approaches to fluid simulation is the degree of integration between learned representations and physical constraints. Earlier hybrid methods often bolted physical corrections onto purely data-driven outputs as a post-processing step. The newer frameworks embed physics into every layer of the optimization process.

The payoff is significant: models trained this way generalize better to conditions outside their training distribution, remain stable over long simulation horizons, and produce outputs that scientists can interpret in terms of known physical mechanisms. For climate applications — where the goal is often to understand unprecedented future states, not merely interpolate within historical records — this physical grounding is not a luxury. It is a prerequisite for trustworthy prediction.

The conformal prediction layer addresses a separate but equally important gap: quantifying uncertainty in a statistically rigorous way. Climate policy decisions increasingly depend not just on best-guess projections but on credible probability ranges. A forecast that attaches a meaningful confidence interval to a rainfall estimate is more useful to a water utility or emergency manager than one that delivers only a single-point output.

## What Comes Next

The Rayleigh-Benard convection results are framed as a proof-of-concept for a broader class of geophysical applications. Potential extensions include ocean circulation modeling, atmospheric blocking events, and coupled climate system simulations — all domains where the cost of DNS makes conventional simulation impractical at the scales needed for policy-relevant projections.

With Hawaiʻi's unique position as a living laboratory for Pacific climate dynamics — sitting at the intersection of tropical convection, trade wind systems, and ocean-atmosphere coupling — the University's growing portfolio of physics-informed AI research carries stakes well beyond academic publication. It is aimed squarely at the question of how island communities across the Pacific will prepare for, and adapt to, a fundamentally altered climate in the decades ahead.
