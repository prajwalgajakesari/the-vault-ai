In 2013, GE threw a titanium jet-engine mounting bracket open to the internet. Nearly 700 entries arrived from 56 countries. GE Aviation printed the top ten in Cincinnati and load-tested them to failure at its Niskayuna research center, and a designer in Salatiga, Indonesia named M Arie Kurniawan won. That geometry has been the human high-water mark ever since.

On August 25, London-based PhysicsX published research claiming it beat that mark by 18.5%. Not with a topology optimizer. With a diffusion model originally built to turn photographs into video-game assets.

The result appears in a technical post, "Building Beyond CAD: On Generative Optimization for Engineering," by PhysicsX engineers Daniel Owen-Lloyd and Sanmitra Ghosh. It arrives ten weeks after the company closed a $300 million Series C at roughly a $2.4 billion valuation, led by Temasek with NVIDIA, Siemens and Applied Materials among existing backers.

## What the model actually did

The benchmark is SimJEB, the Simulated Jet Engine Bracket Dataset assembled in 2021 by MIT's Eamon Whalen, Azariah Beyene and Caitlin Mueller. It took the GrabCAD submissions, cleaned and meshed 381 of them, and ran finite element analysis under four load cases — every model solving the same function under identical loads and supports. In the authors' words, SimJEB models are "more complex, diverse, and realistic than the synthetically generated datasets commonly used in parametric surrogate model evaluation." PhysicsX puts the human labor embedded in it at roughly 14 person-years.

The pipeline starts with TRELLIS.2, a 3D generative foundation model presented at CVPR 2026, with its image conditioning stripped out. Because the model was trained with classifier-free guidance, it already knows how to generate from a "null" token — but it still routes that fixed token through more than 235 million cross-attention parameters per generative model, burning compute to compute a constant. The team proved algebraically that cross-attention under a zero null token collapses to a fixed bias, precomputed it, and deleted over 700 million parameters across TRELLIS.2's three generative models. Inference got roughly 60% faster per evaluation.

Then LoRA. Fine-tuning only about 1 to 10 million of each billion-parameter flow model's weights, on a single GPU, bent the prior away from creative assets and toward engineering parts. In the most extreme test, they fine-tuned on a single bolt with no augmentation and still recovered a distribution over length, width and number of sides — variation derived entirely from pretraining.

The optimization step is worth being precise about, because it is not what most coverage implies. PhysicsX uses differentiable learned surrogates as reward models for its aerodynamics work — steering generation toward a target lift-to-drag ratio, or editing an aircraft tail while holding the fuselage fixed. For the bracket, it did not. The team wired the generative model directly to an FEA worker and ran SDEdit, a diffusion editing technique repurposed as a genetic algorithm: mutate a candidate through a partial forward-and-reverse diffusion pass, keep it only if the solver says it improved. Seeded from the SimJEB competition winner and given a fixed simulation budget, the loop extended the Pareto front and produced a new lightest feasible design — 18.5% lighter, still under the yield stress of titanium, "using no surrogate model or CAD parameters at any stage."

The geometry it found uses a split support that does not exist anywhere in the dataset.

## The caveats that matter

Everything here is simulated. No part was printed, no part was pulled to failure — a direct contrast with the 2013 human winner, which GE physically built and broke. PhysicsX also could not reproduce SimJEB's original FEA solver, so it re-simulated the entire dataset with its own. The 18.5% is measured against that re-simulation, not against GE's 2013 test data.

The company is candid about the rest of the gap. Non-manifold meshes out of TRELLIS.2 need a post-processing pipeline before any production solver will touch them, and the blog states plainly that constrained optimization and manufacturability "remain important issues to address for broader practical adoption."

## Why this is different from twenty years of generative design

Generative design has been a CAD-vendor marketing slide since the mid-2000s and has produced remarkably few flight parts. The reason is structural: topology optimization and parametric search both operate inside a design space someone hand-built, and every candidate costs a solver run. You get organic-looking brackets that are hard to machine, hard to inspect, and hard to certify.

What changed is not the optimizer. It is that the design space itself is now learned rather than authored. A diffusion prior over shapes is not bounded by a parameter list, and PhysicsX's framing — optimization as sampling from a distribution tilted toward high performance, rather than hunting a single argmax — means the prior regularizes the search instead of the engineer doing it by hand.

The surrogate story is more nuanced than the headline suggests. Surrogates are the unlock for aerodynamics, where solver calls are ruinous. For a structural bracket, FEA is cheap enough to sit in the loop directly, sidestepping the failure mode PhysicsX names explicitly: model performance "degrades as it moves beyond its training distribution," precisely where novel designs live.

For Siemens, Ansys and Autodesk, the threat is not simulation speed. Siemens is a PhysicsX investor and already integrates its models into Simcenter X. The threat is that geometry authoring — the CAD kernel, the parametric feature tree, the licensing moat — becomes optional.

## What to watch

Three things. Whether anyone prints and load-tests a generatively designed bracket to failure. Whether a certification authority accepts a part whose provenance is a learned distribution rather than documented design intent. And whether PhysicsX delivers the roadmap it named: bespoke mesh representations for engineering, integrated back into CAD workflows.

Jacomo Corbo, PhysicsX co-founder and CEO, framed the Series C in terms of throughput: "We are giving engineers the ability to explore thousands of designs where they once managed a handful, in seconds rather than weeks." The bracket makes that claim legible. Whether it can fly is a separate question, and nobody has answered it.
