---
headline: "Generative-Physics Hybrid Runs Climate Models About 25x Faster"
slug: generative-physics-climate-models-25x
category: research
story_number: 13
date: 2026-06-09
---

# Generative-Physics Hybrid Runs Climate Models About 25x Faster

A new model called Spherical DYffusion can project a century of climate patterns in a single day — work that once took supercomputers weeks to complete.

By the time a government climate assessment team finishes running a single 100-year scenario on a traditional physics simulator, the window to act on its findings has often narrowed. A research collaboration between UC San Diego and the Allen Institute for AI wants to change that arithmetic. Their model, Spherical DYffusion, completed the same simulation in roughly 25 hours — about 25 times faster than the state-of-the-art physics-based model it was benchmarked against. The work was presented at NeurIPS 2024 in December and has since drawn attention as one of the clearest demonstrations yet of generative AI reshaping the economics of climate science.

The approach fuses two powerful ideas. The team adapted diffusion-based generative architectures — the same class of algorithms behind image-generation tools like DALL-E — and combined them with a Spherical Fourier Neural Operator, a neural network designed to work natively with data distributed across a sphere. The result is a model that begins with established knowledge of atmospheric behavior and then applies learned transformations to project forward in time, without having to solve the full set of differential equations that make physics-based models so computationally expensive.

"Data-driven deep learning models are on the verge of transforming global weather and climate modeling," the researchers write in their NeurIPS paper.

## The Numbers Behind the Claim

The benchmark comparison is striking. A 10-year simulation with the physics-based FV3GFS model — the United States' primary operational global forecast model — takes approximately 78 hours and 4 minutes. Spherical DYffusion runs the same scenario in about 2 hours and 56 minutes, a speedup of roughly 26.6 times. At century scale, a simulation that demands weeks on a supercomputer collapses to about 25 hours on a GPU cluster that fits in a university research lab.

That accessibility shift matters as much as the raw speed. When simulation compute moves from national supercomputing centers to departmental hardware, more research groups, more scenarios, and more ensemble members become tractable. Ensemble forecasting — running dozens or hundreds of slightly varied simulations to characterize uncertainty — is particularly sensitive to cost, because the value of the approach scales directly with the number of members you can afford to run.

## Accuracy: How Much Is Traded Away

Speed is only compelling if the model does not sacrifice too much fidelity. Here, the researchers are candid about where Spherical DYffusion stands. The model reduces climate biases to within 50 percent of the reference physics model — a more than twofold improvement over previous deep-learning benchmarks. For total water path, a critical measure of atmospheric moisture and cloud formation, results fall within 20 percent of the physics-based standard, outperforming the next-best baseline by a factor of five.

"One of the main advantages over a conventional diffusion model is that our model is much more efficient. It may be possible to generate just as realistic and accurate predictions with conventional DMs but not with such speed," the team writes. The phrasing is telling: the researchers are explicit that they have traded some accuracy ceiling for dramatic efficiency gains, but argue the current accuracy level is already competitive with existing emulator approaches.

Rose Yu, a faculty member in the UC San Diego Department of Computer Science and Engineering and one of the paper's senior authors, framed the scope of what was achieved: "We emulated the atmosphere, which is one of the most important elements in a climate model."

The research grew out of an internship that Yu's PhD student Salva Rühling Cachay completed at the Allen Institute for AI. Co-authors Brian Henn, Oliver Watt-Meyer, and Christopher S. Bretherton contributed from the Allen Institute side.

## Why It Matters

Climate modeling sits at the intersection of three urgent pressures: the scientific need to characterize uncertainty across many scenarios, the policy demand for faster turnaround on decision-relevant projections, and the practical constraint that full physics simulations are extraordinarily expensive. Spherical DYffusion addresses all three simultaneously.

For extreme-weather analysis specifically, ensemble size is everything. When scientists want to estimate the probability of a once-in-a-century flood or heat event under a particular emissions trajectory, they need large ensembles to populate the tail of the distribution with enough samples to reason about reliably. A 25x speedup means a researcher can run 25 ensemble members for the price of one, or explore 25 different forcing scenarios in the time previously required for a single run.

The broader context is a fast-moving field. Emulator-based approaches — ML models trained to mimic the outputs of physics simulators — have proliferated since around 2022, with Google DeepMind's GraphCast and others demonstrating competitive skill on weather forecasting timescales. Spherical DYffusion extends that paradigm into multi-decadal climate projection and explicitly incorporates probabilistic ensemble generation, which most deterministic emulators do not attempt.

The remaining gap is significant, though. The current model emulates only the atmosphere. Coupling it to ocean, land-surface, and ice components — the full Earth system — remains future work. The researchers also note that evaluating climate change scenarios requires time-varying forcings such as greenhouse gas and aerosol concentrations that are not yet incorporated. In other words, Spherical DYffusion is a powerful proof of concept, not a ready replacement for the physics-based systems that underpin official IPCC-style assessments.

## What to Watch

The team's stated next step is simulating how the atmosphere responds to CO2 forcing — a prerequisite for producing the kind of scenario projections that feed into policy documents. If that extension holds up at similar accuracy levels, the combination of generative speed and physical plausibility could meaningfully change how frequently and how broadly climate agencies can update their projections.

Watch also for the emulator-versus-physics debate to intensify. Critics of purely data-driven models argue they can fail silently outside their training distribution — a serious concern in a domain where the whole point is to project into conditions humanity has never experienced. The physics-informed architecture of Spherical DYffusion is a partial answer to that critique, but the community will scrutinize how the model behaves under high-CO2 regimes it was not trained on.

The paper is available at NeurIPS 2024 proceedings and on arXiv (arXiv:2406.14798). Code is open-sourced at github.com/Rose-STL-Lab/spherical-dyffusion.
