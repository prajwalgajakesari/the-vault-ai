---
headline: "Penn Researchers Create Light-Matter Chip That Could Slash AI Computing Energy by Orders of Magnitude"
slug: penn-light-matter-chip-ai-computing
category: research
story_number: 10
date: 2026-05-21
author: The Vault — AI Edition
tags:
  - photonic computing
  - AI hardware
  - energy efficiency
  - exciton-polaritons
  - Penn
sources:
  - name: ScienceDaily
    url: https://www.sciencedaily.com/releases/2026/05/260518041341.htm
  - name: Penn Engineering Blog
    url: https://blog.seas.upenn.edu/new-chip-opens-door-to-ai-computing-at-light-speed/
  - name: Penn Today
    url: https://penntoday.upenn.edu/news/penn-engineering-new-chip-opens-door-ai-computing-light-speed
  - name: Interesting Engineering
    url: https://interestingengineering.com/innovation/a-way-to-use-photons-for-computing
  - name: Phys.org
    url: https://phys.org/news/2026-05-physicists-hybrid-particles-interact-strongly.html
  - name: Physical Review Letters (journal)
    url: https://link.aps.org/doi/10.1103/gc15-qsvf
---

# Penn Researchers Create Light-Matter Chip That Could Slash AI Computing Energy by Orders of Magnitude

Eighty years after the University of Pennsylvania gave the world ENIAC, the first general-purpose electronic computer, a team of Penn physicists is proposing a radical successor to the electron: a hybrid particle made of light and matter that can switch signals using almost no energy at all.

The research, published this month in *Physical Review Letters*, introduces a nanoscale device that generates quasiparticles called exciton-polaritons — strange entities that inherit the speed of photons and the interactive strength of electrons. Led by physicist Bo Zhen of Penn's School of Arts & Sciences, the team demonstrated all-optical signal switching at an energy cost of roughly 4 femtojoules, or four quadrillionths of a joule. That is an almost incomprehensibly small amount of energy, far below what it takes to briefly illuminate even the tiniest LED.

The implications for artificial intelligence infrastructure are significant. As AI models balloon in size and training runs consume electricity on an industrial scale, the search for computing substrates that sidestep the heat and resistance penalties of electronic circuits has become one of the most urgent problems in the field.

## The Photon Problem

Light has always been an appealing candidate for computing. Photons are charge-neutral, have zero rest mass, and can carry information over long distances with minimal loss — properties that already make them the backbone of global telecommunications through fiber-optic networks.

But photons have a critical flaw when it comes to computation. "They barely interact with their environment, making them bad at the sort of signal-switching logic that computers depend on," explained Li He, co-first author of the study and now an assistant professor at Montana State University. Carrying data is one thing; making decisions with it is another. Computation requires nonlinear operations — moments where one signal changes the behavior of another — and photons, left to their own devices, simply pass through each other without effect.

This limitation has haunted photonic computing for decades. Many experimental photonic AI chips already use light to accelerate certain calculations, particularly the matrix multiplications at the heart of neural networks. But when those systems reach a nonlinear activation step — the decision-making layer — they must convert optical signals back into electronic ones. That conversion erases much of the speed and efficiency advantage that light was supposed to provide.

## Building a Better Particle

Zhen's team attacked this problem by engineering a quasiparticle that does not exist in nature. They coupled photons with excitons — bound electron-hole pairs inside an atomically thin monolayer of molybdenum diselenide (MoSe2) — within a planar photonic crystal nanocavity. When the coupling becomes strong enough, the photons and excitons stop behaving as independent entities and merge into a new hybrid state: the exciton-polariton.

The result is a particle that moves at near-light speed while retaining the ability to interact strongly with other signals. The nanocavity's tight confinement amplifies these interactions dramatically, producing nonlinear optical responses that far exceed those of conventional materials.

The critical achievement was demonstrating that these interactions are powerful enough to switch optical signals at ultralow energies — roughly 4 femtojoules — on picosecond timescales. The researchers also showed that the device's properties can be tuned electrically through a gate voltage applied to the semiconductor, giving engineers an additional knob to control the system's behavior.

## Why It Matters for AI

The timing of this breakthrough aligns with a growing crisis in AI energy consumption. Training a single large language model can require megawatt-hours of electricity, and the proliferation of AI applications is driving an unprecedented buildout of data center capacity worldwide. Tech companies are now commissioning nuclear reactors and building elaborate liquid-cooling systems to manage the thermal output of dense GPU clusters.

Photonic systems based on exciton-polaritons could address this problem at a fundamental level. Because light generates far less waste heat than moving electrical charges through resistive materials, all-optical processing could dramatically reduce both the energy consumed by computation and the energy spent on cooling. The 4-femtojoule switching energy demonstrated by Zhen's team is orders of magnitude below what conventional electronic transistors require, suggesting that a mature version of this technology could reshape the energy economics of AI hardware.

Beyond efficiency, the platform opens a path toward processing optical data — such as images from cameras — directly in the light domain, without the repeated optical-to-electronic conversions that currently create bottlenecks in AI vision systems. The researchers also suggest their device could eventually support basic quantum computing functions on a chip.

## The Road Ahead

Important caveats remain. The current work is a proof-of-concept device, not a production-ready chip. Scaling the technology from a single nanocavity to the billions of switching elements needed for practical computing will require solving substantial engineering challenges. The device must also prove it can perform reliably outside controlled laboratory conditions and handle the complex, real-world computations that AI workloads demand.

Still, the research represents a meaningful step forward in a field that has long promised more than it has delivered. Previous photonic computing efforts from Penn — including a 2024 silicon-photonic chip from Nader Engheta and Firooz Aflatouni that performed vector-matrix multiplication using variations in silicon wafer height — have demonstrated that light-based math is feasible. Zhen's exciton-polariton work now addresses the missing piece: nonlinear switching without electronic conversion.

The study was supported by the U.S. Office of Naval Research and the Sloan Foundation. Co-authors include Zhi Wang and Bumho Kim of Penn's School of Arts & Sciences.

If these particles can be engineered into scalable systems, the institution that launched the electronic computing era may end up helping to define what comes after it.
