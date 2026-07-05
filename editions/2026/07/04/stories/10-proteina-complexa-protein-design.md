For years, the promise of designing a drug-like protein from scratch has run ahead of the evidence. Generative models could sketch elegant molecular shapes, but the number that actually stuck to their intended targets in a test tube was often small, and the benchmarks were smaller still. In late March 2026, NVIDIA moved to change the terms of that debate with Proteina-Complexa, a generative model for designing protein binders that its makers say was stress-tested at a scale rarely seen in the field: roughly one million designs, screened against more than 130 distinct targets.

## What Proteina-Complexa actually does

Proteina-Complexa generates *de novo* protein binders — proteins built to latch onto a specific target, whether another protein or a small molecule — and can also scaffold enzyme active sites. Built on top of NVIDIA's earlier La-Proteina model, it uses a "partially latent flow-matching" framework to co-design a binder's full atomic structure and its amino acid sequence at the same time. In practice, that means the backbone alpha-carbon atoms are modeled explicitly in 3D space, while side-chains and sequence are compressed into a learned latent space.

The distinction matters. Many earlier pipelines split the job: one model drafts a backbone, another threads a sequence onto it. NVIDIA's team argues that co-designing both at once keeps chemistry and geometry tightly coupled, producing interfaces that are "inherently optimized for folding and synthesis." The model was trained on over a million curated experimental and predicted structures drawn from the Protein Data Bank, the AlphaFold database, PLINDER, and the newer Teddymer dataset.

The second ingredient is inference-time compute — the same "test-time scaling" idea reshaping large language models. During generation, search algorithms such as Beam Search and Best-of-N evaluate and refine candidates midstream, spending extra compute on harder targets. "With test-time scaling, we've enabled the model to refine its logic before outputting a single sequence," said Anthony Costa, NVIDIA's director of digital biology.

## The validation numbers

The headline claim is the wet-lab validation. According to NVIDIA, tens of millions of *in silico* candidates were generated, and after filtering, around one million binder candidates were experimentally tested against 133 distinct protein targets — from well-worn benchmarks to therapeutically relevant proteins with no previously reported binders. NVIDIA calls it one of the largest binder-design benchmarks to date.

Much of that throughput came from Manifold Bio, a Boston therapeutics company. In a joint study announced in March, Manifold used multiplexed phage screening to test one million binder designs against 127 targets in a single experiment, measuring more than 100 million protein-protein interactions and identifying specific binders to 68% of targets tested. (The slight difference in target counts reflects the two organizations describing overlapping but distinct slices of the work; treat the figures as of the same magnitude rather than identical.)

"This study provides a practical demonstration of scaling laws in de novo protein design, with more designs producing more hits," said Pierce Ogden, Manifold Bio's co-founder and chief technology officer, who framed the experiment as a case for inference scaling "when experimental throughput can keep pace."

Beyond hit rates, NVIDIA reports quantitative binding kinetics — via surface plasmon resonance and other assays — showing nano- and picomolar affinities for selected targets, including a binder against Activin Receptor Type-2A, a target implicated in muscle-wasting disorders. The team also pushed into notoriously hard territory: designing proteins that bind sugar molecules on red blood cells. Of 24 carbohydrate-binding candidates, four clumped red blood cells more efficiently than natural lectins, with direct binding confirmed by bio-layer interferometry.

## Why binder design matters

Protein binders sit at the center of modern medicine — antibodies, receptor traps, and targeted therapies all depend on one molecule gripping another with precision. Designing them from scratch, rather than screening natural libraries, could shorten discovery timelines and open up "undruggable" surfaces. Polar and carbohydrate targets, which repel most existing tools, are exactly the kind of intractable surfaces the field has struggled with.

Proteina-Complexa lands in a crowded, fast-moving arena alongside DeepMind's AlphaFold3, the RFdiffusion lineage from the Baker Lab, and open models like Chai. What sets this release apart is less a single benchmark than the coupling of generative design with experimental validation at matching scale — and the decision to open-source it. NVIDIA released the code under an Apache 2.0 license, with model checkpoints on NGC and Hugging Face, plus collaborators spanning Novo Nordisk, Viva Biotech, Duke, Cambridge, LMU Munich, and Bonn.

## What to watch

The caveats are the usual ones for computational biology: a phage-display hit rate is a starting point, not a drug. Affinity, specificity, stability, immunogenicity, and manufacturability all still have to survive the long march to the clinic, and none of the validated binders are therapeutics yet. The open questions are whether independent labs reproduce the hit rates, whether the picomolar affinities hold up across target classes, and whether "more designs, more hits" keeps scaling. If it does, the bottleneck in early drug discovery may quietly shift from imagination to experimental throughput — and Manifold's million-design assay suggests that constraint is loosening too.
