---
headline: "UPenn Researchers Introduce Mollifier Layers to Solve Inverse Partial Differential Equations With Neural Networks"
slug: upenn-mollifier-layers-neural-pde
category: research
story_number: "14"
date: 2026-05-05
author: The Vault AI
sources:
  - name: Penn Engineering - AI Method Tackles One of Science's Hardest Math Problems
    url: https://www.seas.upenn.edu/stories/ai-method-tackles-one-of-sciences-hardest-math-problems/
    domain: seas.upenn.edu
  - name: "arXiv - Mollifier Layers: Enabling Efficient High-Order Derivatives in Inverse PDE Learning"
    url: https://arxiv.org/html/2505.11682
    domain: arxiv.org
  - name: Phys.org - AI Tackles One of Math's Most Brutal Problems
    url: https://phys.org/news/2026-05-ai-tackles-math-brutal-problems.html
    domain: phys.org
  - name: Mirage News - AI Breakthrough Solves Toughest Math Challenge
    url: https://www.miragenews.com/ai-breakthrough-solves-toughest-math-challenge-1666072/
    domain: miragenews.com
---

# UPenn Researchers Introduce Mollifier Layers to Solve Inverse Partial Differential Equations With Neural Networks

A team of researchers at the University of Pennsylvania has developed a deceptively elegant solution to one of scientific computing's most persistent headaches: getting neural networks to reliably compute high-order derivatives when solving inverse partial differential equations. Their method, called "Mollifier Layers," borrows an 80-year-old mathematical smoothing technique and weaves it directly into modern AI architectures, slashing memory usage and training time by 6 to 10 times while producing more stable results. The work, published in Transactions on Machine Learning Research, will be presented at the Conference on Neural Information Processing Systems (NeurIPS 2026).

## The Inverse PDE Problem

Partial differential equations describe how quantities change across both space and time. They underpin models of weather systems, heat dissipation, fluid mechanics, and -- in the case of the Penn team -- the organization of DNA inside cells. Solving a PDE forward, predicting future behavior from known rules, is hard enough. Solving one inversely, working backward from observed data to infer the hidden forces that produced it, is substantially harder.

"Solving an inverse problem is like looking at ripples in a pond and working backward to figure out where the pebble fell," the researchers explain. Scientists need this capability across disciplines: identifying tumor growth parameters from medical imaging, reconstructing subsurface geology from seismic readings, or inferring reaction rates from microscopy data.

For years, neural networks tackling these inverse problems have relied on recursive automatic differentiation to compute derivatives -- the mathematical measurements of change that PDEs require. For first- and second-order derivatives, this works tolerably well. But many real-world systems demand third-, fourth-, or even higher-order derivatives, and that is where the approach falls apart. Each recursive pass amplifies noise in the data, like repeatedly photocopying a photocopy until the text becomes illegible. The computational cost also scales explosively, consuming memory and processing power that quickly exceed practical limits.

## An 80-Year-Old Mathematical Idea, Reimagined

Rather than simply throwing more computing power at the problem, the Penn team looked to the past. In the 1940s, German-American mathematician Kurt Otto Friedrichs -- later a National Medal of Science recipient -- described "mollifiers," mathematical functions that smooth out the sharpest features of noisy or jagged signals while preserving their essential structure.

"Modern AI often advances by scaling up computation," said Vinayak Vinayak, a doctoral candidate in Materials Science and Engineering at Penn and co-first author of the study. "But some scientific challenges require better mathematics, not just more compute."

The team's key insight was that by applying a mollifier as a convolutional layer within the neural network, they could collapse the entire chain of recursive higher-order automatic differentiation into a single analytic convolution. Instead of computing derivatives step by painful step -- each one magnifying noise -- the mollifier layer smooths the signal first, then extracts derivative information in one clean operation.

The result is a lightweight, architecture-agnostic module that can be dropped into existing neural network designs without rearchitecting them. "That let us solve these equations more reliably, without the same computational burden," said Ananyae Kumar Bhartari, a graduate of Penn Engineering's Scientific Computing master's program and co-first author.

## Concrete Results

In experiments across multiple benchmark inverse PDE problems, Mollifier Layers reduced both memory footprint and training time by 6 to 10 times compared to standard recursive automatic differentiation. Critically, they did so while preserving robust, high-order derivative estimates -- even when the input data was noisy, precisely the conditions under which conventional methods deteriorate most rapidly.

The framework was validated on problems requiring up to fourth-order derivatives, a regime where recursive methods become computationally prohibitive for most research groups. By making these higher-order problems tractable on standard hardware, the work lowers the barrier to entry for labs that lack access to massive compute clusters.

## From Chromatin to Climate

For the Shenoy Lab at Penn, where the work originated, one immediate application is understanding chromatin -- the tightly folded complex of proteins and DNA that packages chromosomes inside cell nuclei. Tiny domains of chromatin, just 100 nanometers in size, regulate which genes are accessible for expression, a process with direct implications for cell identity, aging, and disease.

"These domains are just 100 nanometers in size," said Vivek Shenoy, Eduardo D. Glandt President's Distinguished Professor in Materials Science and Engineering and senior author, "but because accessibility determines gene expression, and gene expression governs cell identity, function, aging and disease, these domains play a critical role in biology and health."

By using mollifier layers to infer the epigenetic reaction rates driving chromatin reorganization, the team aims to move beyond static microscopy snapshots toward dynamic models of how chromatin changes over time and how those changes influence gene expression and cell fate.

But the implications extend well beyond biology. Problems in materials science, fluid mechanics, weather forecasting, and geological modeling all involve higher-order PDEs and noisy observational data. The architecture-agnostic design of mollifier layers means any research group already using neural networks for scientific computing can integrate the module with minimal friction.

## The Bigger Picture

The work fits squarely within a broader trend in scientific machine learning: the recognition that brute-force scaling is not always the answer. Alongside recent advances in physics-informed neural networks and neural operators, mollifier layers represent a growing toolkit of mathematically principled modules that encode domain knowledge directly into AI architectures rather than hoping the network will learn it from data alone.

"Ultimately, the goal is to move from observing complex patterns to quantitatively uncovering the rules that generate them," said Shenoy. "If you understand the rules that govern a system, you now have the possibility of changing it."

That ambition -- not just predicting nature but reverse-engineering its operating instructions -- is what makes inverse PDEs so important and so difficult. With mollifier layers, the Penn team has made the difficult considerably more tractable.
