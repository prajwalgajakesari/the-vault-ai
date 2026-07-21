---
headline: "Protein AI Moves Past the Static Snapshot and Starts Predicting How Molecules Actually Move"
slug: protein-conformational-prediction-beyond-alphafold
category: research
story_number: 14
date: 2026-07-20
---

# Protein AI Moves Past the Static Snapshot and Starts Predicting How Molecules Actually Move

A protein structure predicted by AlphaFold is a photograph. Biology is a film. The gap between the two is where the last five years of computational structural biology have quietly relocated — and where, over the past eighteen months, the field's most consequential results have landed.

Proteins do not hold still. They breathe, hinge, unfold locally, and flicker between conformations, and much of what they do — catalysis, signaling, allosteric regulation — happens in that motion rather than in any single frame. Drug hunters care for a blunt reason: many of the most valuable binding pockets are *cryptic*, meaning they exist only in transient shapes that never show up in a crystal structure. Predicting the average conformation of a protein tells you almost nothing about the rare one you want to drug.

## From one structure to a distribution

The clearest marker of the shift is BioEmu, a generative deep learning system from Microsoft Research AI for Science published in *Science* on July 10, 2025 under the title "Scalable emulation of protein equilibrium ensembles with generative deep learning." Rather than emitting one structure per sequence, BioEmu samples from a protein's approximate *equilibrium ensemble* — the population of conformations weighted by how often the molecule actually occupies each one.

The compute numbers are the headline. BioEmu generates thousands of statistically independent structures per hour on a single GPU. Reproducing the D. E. Shaw Research molecular dynamics simulation of Protein G, it recovered the same conformational distribution using, by Microsoft's accounting, 10,000 to 100,000 times fewer GPU hours than running MD to convergence. On free energies it reports roughly 1 kcal/mol accuracy against millisecond-scale MD and experimental protein stability measurements — close enough to the noise floor of wet-lab thermodynamics to be useful rather than merely suggestive.

That performance was bought with data. BioEmu was trained on AlphaFold Database structures, an experimental folding-stability dataset, and more than 200 milliseconds of molecular dynamics simulation. Microsoft released over 100 milliseconds of that simulation data alongside the paper — the largest sequence-diverse protein simulation set made public to date — and the model itself under an MIT license.

"This reduces the cost and the required time to analyze functional structure changes in proteins," said Frank Noé, the Microsoft Research partner research manager who led the project and holds an honorary professorship at Freie Universität Berlin. Cecilia Clementi, the FU Berlin theoretical biophysicist who contributed as a visiting researcher, framed the scale argument: "BioEmu provides a scalable method to model protein function at the genomic scale."

Independent voices were measured but positive. "With highly accurate structure prediction, protein dynamics is the next frontier in discovery," said Martin Steinegger of Seoul National University, who was not involved in the work. "BioEmu marks a significant step in this direction by enabling blazing-fast sampling of the free-energy landscape of proteins through generative deep learning."

## The design half of the pivot

The complementary move is from prediction to construction. BindCraft, published in *Nature* in August 2025 by Martin Pacesa and colleagues at EPFL's Laboratory of Protein Design and Immunoengineering with collaborators in the US and Netherlands, inverts the usual pipeline: it drives AlphaFold2 backwards, using the structure predictor itself as the design engine to hallucinate binders with specified properties.

Across roughly a dozen validated targets — including adeno-associated viral capsids, the CRISPR-Cas9 nuclease, cell-surface receptors and common allergens — designed binders hit their intended targets at an average experimental success rate of 46%, with target-specific rates spanning about 10% for HER2 to 60% for SpCas9. That is achieved by testing a handful of designs rather than screening tens of thousands.

"With BindCraft, we essentially reverse-engineer the current pipeline by using the protein structure prediction network right from the start to generate novel binders that have the properties we're looking for," said EPFL PhD student Christian Schellhaas.

## Analysis: the ground truth problem

The honest caveat is that nobody can fully grade this work. A May 2026 *Nature Methods* Perspective by Stephanie Wankowicz and Massimiliano Bonomi puts it starkly: progress on ensemble prediction is "limited by the lack of accurate, high-resolution ground-truth data at the scale required for training and validation," because no single experimental technique resolves a conformational landscape, and the field still lacks agreed ways of defining, comparing and validating ensembles at all.

Generalization is the sharper worry. A January 2026 review by Myeongsang Lee and Lauren Porter of the NIH examined fold-switching proteins — molecules that remodel their secondary structure entirely — as a stress test. Sampling roughly 300,000 structures from 92 fold switchers whose alternative conformations were already in AlphaFold's training set yielded a 35% success rate; on targets outside the training set, performance collapsed to one of seven. Even CFold, an AlphaFold2 retrained on a conformational split of the PDB, got 57% of alternative conformations right while systematically failing on large conformational changes. The authors' conclusion is uncomfortable: these models often predict alternative conformations by association with memorized training structures, not by learning physics.

Intrinsically disordered regions and long-range allosteric coupling remain largely unaddressed. And an equilibrium ensemble is not kinetics — it tells you which states exist and how populated they are, not how fast a protein gets between them, which is often what determines whether a drug works.

## What to watch

Three things. Whether hybrid approaches — 2026 preprints are already pairing BioEmu-style sampling with short MD runs to recover kinetics — become the default workflow. Whether the community converges on shared ensemble benchmarks and validation protocols, the infrastructure Wankowicz and Bonomi argue is the actual bottleneck. And whether cryptic pockets predicted by these emulators produce a drug candidate that survives the clinic. Until then, the field has traded one hard question for a better one.
