# A New Protein-Design Model, Proteina-Complexa, Generates Binders Validated Against 130+ Targets

For decades, designing a protein that reliably grabs onto a chosen target was a slow, artisanal craft: a mix of physics simulations, trial and error, and a great deal of luck. NVIDIA and a group of academic and biotech collaborators say they have now turned that craft into something closer to industrial-scale search. Their new generative model, Proteina-Complexa, produced roughly one million candidate protein binders that were then experimentally tested against more than 130 distinct targets, in what the teams describe as one of the largest binder-design benchmarks ever run.

The result is not just a bigger model. It is a demonstration that de novo protein design, long promising in silico, can be validated in the wet lab at a scale that begins to look like real drug discovery.

## What Proteina-Complexa actually does

Proteina-Complexa is a generative model for designing de novo protein binders and enzymes, released by NVIDIA Research alongside open source code, model checkpoints, and datasets. Built on top of NVIDIA's earlier La-Proteina model, it uses what the team calls a "partially latent flow-matching" framework to co-design a binder's full atomic structure and its amino acid sequence at the same time.

In practice, that means the model does not treat backbone generation and sequence design as separate steps, the way many earlier pipelines did. Backbone alpha-carbon atoms are modeled explicitly in 3D space, while side-chain atoms and the sequence itself are compressed into a learned latent space via an autoencoder. Generating geometry and chemistry together, the researchers argue, produces interfaces that are inherently better optimized for folding, synthesis, and tight binding.

The other headline ingredient is inference-time compute. Rather than sampling a design in one pass, Proteina-Complexa runs "reasoning" search algorithms such as Beam Search and Best-of-N during generation, evaluating and refining candidates at intermediate steps and spending extra compute on the hardest targets. NVIDIA says the combined approach runs 30 to 60 times faster than RFdiffusion, the widely used diffusion model from the Baker Lab, when designing custom binders. The model was trained on more than one million curated experimental and predicted structures drawn from the Protein Data Bank, the AlphaFold database, PLINDER, and the newer Teddymer dataset.

## The million-design validation

The scale claim rests on a joint study with Manifold Bio, a Boston therapeutics company, announced in March 2026. Manifold used its multiplexed screening platform to test one million binder designs against 127 targets in a single experiment, measuring more than 100 million protein-protein interactions. The study identified specific binders for 68% of the targets tested. NVIDIA's own accounting, spanning collaborations with several partners, puts the total at roughly one million filtered candidates tested against 133 distinct protein targets, from established benchmarks to therapeutically relevant proteins with no previously reported binders.

"Manifold Bio's platform uniquely enabled this massively multiplexed study, which establishes Proteina-Complexa as competitive with state-of-the-art methods," said Pierce Ogden, Ph.D., co-founder and chief technology officer of Manifold Bio. "This study provides a practical demonstration of scaling laws in de novo protein design, with more designs producing more hits, and makes the case for inference scaling when experimental throughput can keep pace."

That last point is the intellectual center of the work: the idea that protein design, like large language models, may obey scaling laws where more compute and more designs translate into more validated hits, provided the lab can test them fast enough.

"Proteina-Complexa was built to generate protein binders at the speed and scale that drug discovery demands, powered by a novel architecture that redefines generative design," said Anthony Costa, director of digital biology at NVIDIA. "With test-time scaling, we've enabled the model to refine its logic before outputting a single sequence. Testing over a million designs against 127 targets in a single experiment validates that this scaled reasoning approach works."

Beyond the headline numbers, the teams reported binders with nano- and picomolar affinities, including designs against Activin Receptor Type-2A, a muscle-wasting target for which no similar mini-binders had been reported. The model also produced proteins that bind small molecules and, strikingly, sugar molecules on red blood cells, a notoriously hard "polar" target class. Of 24 sugar-binding candidates, four outperformed the natural lectins used in labs today.

## Why validated de novo binders matter

The significance is less about any single number and more about closing the loop between generation and evidence. Earlier milestones set the trajectory: the Baker Lab's RFdiffusion made de novo backbone generation practical, and Google DeepMind's AlphaProteo, unveiled in 2024, reported experimentally validated binders with strong success rates against a handful of targets. Proteina-Complexa's contribution is breadth and throughput, pairing a reasoning-style generative model with a screening partner able to test a million designs at once against more than a hundred targets, including "intractable" polar surfaces that defeated earlier hydrophobic-favoring tools.

That combination hints at a discovery paradigm where the bottleneck shifts from ideas to experimental capacity, and where success rates on a per-target basis can be reported honestly across dozens of proteins rather than cherry-picked demos.

## What to watch

Two things will determine whether this is an inflection point or an impressive benchmark. First, translation: a binder that lights up in a phage display or SPR assay is a long way from a drug, and the field will watch whether these designs survive developability, in vivo studies, and the clinic. Manifold's own platform folds in multiplexed in vivo data, which could accelerate that test. Second, openness: NVIDIA has released the model under permissive licenses (Apache 2.0 for code, an open model license for checkpoints), which means independent labs can probe whether the 68% hit rate holds on their own hard targets. If it does, the case for inference-time scaling in biology gets a lot harder to argue with.
