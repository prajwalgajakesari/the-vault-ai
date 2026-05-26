---
headline: "Penn Researchers Introduce Mollifier Layers to Solve Inverse PDEs With Neural Networks"
slug: penn-mollifier-layers-inverse-pdes
category: research
story_number: 12
date: 2026-05-25
author: The Vault AI
sources:
  - https://www.seas.upenn.edu/stories/ai-method-tackles-one-of-sciences-hardest-math-problems/
  - https://www.eurekalert.org/news-releases/1126149
  - https://openreview.net/forum?id=6mFVZSzyev
  - https://phys.org/news/2026-05-ai-tackles-math-brutal-problems.html
---

# Penn Researchers Introduce Mollifier Layers to Solve Inverse PDEs With Neural Networks

Sometimes the biggest breakthroughs in artificial intelligence come not from building bigger models, but from reaching back into the history of mathematics for a forgotten idea. That is exactly what a team of engineers at the University of Pennsylvania has done, reviving a smoothing technique from the 1940s and embedding it inside neural networks to crack one of the most stubborn problems in scientific computing: inverse partial differential equations.

The result is a new module the researchers call Mollifier Layers -- a lightweight, architecture-agnostic addition to neural networks that replaces the standard method of computing derivatives with a more stable alternative based on classical mollifier functions. Published in Transactions on Machine Learning Research and accepted for presentation at NeurIPS 2026, the work addresses a longstanding bottleneck that has limited AI-driven scientific discovery across physics, biology, and materials science.

## The Inverse Problem, Explained

Partial differential equations, or PDEs, are the mathematical backbone of modern science. They describe how quantities like heat, pressure, and concentration change across space and time. Forward PDEs are hard enough -- given a set of rules, predict how a system evolves. Inverse PDEs are far harder: given only observations of a system, work backward to infer the hidden forces and parameters that produced them.

"Solving an inverse problem is like looking at ripples in a pond and working backward to figure out where the pebble fell," said Vivek Shenoy, the Eduardo D. Glandt President's Distinguished Professor in Materials Science and Engineering at Penn and senior author of the study. "You can see the effects clearly, but the real challenge is inferring the hidden cause."

Inverse PDEs matter enormously in practice -- from reconstructing subsurface geology from seismic waves to modeling climate systems from atmospheric observations. But solving them with neural networks has been plagued by instability, particularly when higher-order derivatives are involved.

## Why Existing Methods Broke Down

The standard approach relies on recursive automatic differentiation -- the same backpropagation engine that powers all deep learning -- to compute the derivatives that PDEs require. For first-order equations, this works reasonably well. But for second- and fourth-order PDEs, each additional round of differentiation amplifies noise in the data, producing wildly unreliable results and consuming enormous amounts of memory.

The Penn team initially suspected the problem lay in their neural network architecture. After methodical experimentation, they discovered the real culprit was the differentiation process itself. "We initially assumed the issue had to do with the neural network's architecture," said Ananyae Kumar Bhartari, a co-first author and graduate of Penn Engineering's Scientific Computing master's program. "But, after carefully adjusting the network, we eventually realized the bottleneck was recursive automatic differentiation itself."

## An 80-Year-Old Idea, Reimagined

The fix came from an unlikely source: the work of Kurt Otto Friedrichs, a German-American mathematician who in 1944 described "mollifiers" -- mathematical functions designed to smooth out rough or noisy signals. The Penn team built these mollifiers directly into a neural network layer that replaces recursive autodiff with convolutional operations using analytically defined smoothing kernels.

The effect was dramatic. Mollifier Layers reduced noise amplification, cut memory usage, and accelerated training times across benchmarks spanning first-, second-, and fourth-order PDEs, including Langevin dynamics, heat diffusion, and reaction-diffusion systems. Crucially, the module is architecture-agnostic: it can be dropped into any existing neural network without redesigning the model.

"Modern AI often advances by scaling up computation," said Vinayak Vinayak, a doctoral candidate in Materials Science and Engineering and co-first author. "But some scientific challenges require better mathematics, not just more compute."

## From DNA to Drug Discovery

The team's immediate application is in genomics. The Shenoy Lab studies chromatin -- the tightly bundled form DNA takes inside the cell nucleus -- and how its organization governs which genes are switched on or off. These epigenetic processes are governed by reaction-diffusion equations that are, by nature, inverse problems: scientists can observe the chromatin structures under a microscope, but must infer the chemical reaction rates that produced them.

With Mollifier Layers, the researchers can now estimate those hidden reaction rates with far greater reliability. Chromatin domains are just 100 nanometers in size, but because they determine gene expression -- and gene expression governs cell identity, function, aging, and disease -- understanding their dynamics is critical for biology and medicine.

"If we can track how these reaction rates evolve during aging, cancer or development," Vinayak said, "this creates the potential for new therapies: If reaction rates control chromatin organization and cell fate, then altering those rates could redirect cells to desired states."

## Analysis: Why This Matters for AI

The Mollifier Layers paper arrives at an inflection point for scientific AI. The field has spent several years scaling physics-informed neural networks and neural operators with ever-larger models and datasets, yet many inverse problems have remained stubbornly out of reach. The Penn result suggests that for an important class of scientific problems, the path forward is not more parameters but better mathematical primitives.

The architecture-agnostic design is particularly significant. Rather than proposing yet another specialized model, the team offers a modular component that existing research groups can integrate immediately. That kind of composability is what turns a research paper into infrastructure.

The broader implication is a growing recognition that scientific machine learning cannot succeed by importing techniques wholesale from language modeling or computer vision. These problems are governed by known physical laws and sensitive to derivative fidelity in ways that token prediction never is. Mollifier Layers represent exactly the kind of domain-aware engineering that scientific AI needs more of.

"Ultimately, the goal is to move from observing complex patterns to quantitatively uncovering the rules that generate them," Shenoy said. "If you understand the rules that govern a system, you now have the possibility of changing it."

*The study was supported by the National Cancer Institute, the National Science Foundation, the National Institute of Biomedical Imaging and Bioengineering, and the National Institute of General Medical Sciences.*
