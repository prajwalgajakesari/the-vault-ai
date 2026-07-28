For nearly a decade, the promise of AI in biology has been dominated by a single verb: predict. AlphaFold taught machines to forecast how a protein folds. Now a new model is trying to invert the problem — not to read structures that already exist, but to write functional ones that do not. And for the first time, someone has tested those inventions a million at a time.

On March 16, 2026, the Boston-based therapeutics company Manifold Bio announced results from a joint study with NVIDIA validating **Proteina-Complexa**, a generative model built to design protein binders — proteins engineered to latch onto a specific target. Using its own high-throughput screening platform, Manifold said it tested roughly one million binder designs against 127 targets in a single multiplexed experiment, measuring more than 100 million protein-protein interactions and finding specific binders for 68% of the targets tested.

## From static prediction to functional design

The distinction matters. AlphaFold and its successors answer the question "what shape is this protein?" Proteina-Complexa answers a harder one: "invent a new protein that will stick, tightly and specifically, to this exact spot." That is the actual bottleneck in drug discovery, where the goal is not a picture of a molecule but a molecule that does something.

Proteina-Complexa is built on NVIDIA's earlier La-Proteina model and uses a technique the company calls co-design — generating a binder's backbone, its side-chain atoms, and its amino-acid sequence simultaneously rather than in separate, stitched-together stages. According to NVIDIA's technical documentation, the model was trained on more than one million curated experimental and predicted structures drawn from the Protein Data Bank, the AlphaFold database, PLINDER, and the newer Teddymer dataset.

The most consequential design choice borrows a page from large language models: inference-time compute, or "test-time scaling." Instead of emitting a single guess, the model runs search algorithms such as Beam Search and Best-of-N during generation, spending extra computation to refine difficult candidates before committing to an output.

"Proteina-Complexa was built to generate protein binders at the speed and scale that drug discovery demands, powered by a novel architecture that redefines generative design," said Anthony Costa, Director of Digital Biology at NVIDIA. "With test-time scaling, we've enabled the model to refine its logic before outputting a single sequence."

## The million-binder benchmark

The headline number is not the model but the validation. Designing binders in silico is cheap; the field's persistent problem has been proving that computer-generated proteins actually work in a test tube. Manifold's contribution was throughput — matching the scale of AI generation with the scale of experimental measurement.

"Manifold Bio's platform uniquely enabled this massively multiplexed study, which establishes Proteina-Complexa as competitive with state-of-the-art methods," said Pierce Ogden, Ph.D., co-founder and chief technology officer of Manifold Bio. "This study provides a practical demonstration of scaling laws in de novo protein design, with more designs producing more hits, and makes the case for inference scaling when experimental throughput can keep pace."

The two organizations report the figures slightly differently, and the distinction is worth attributing carefully. Manifold's press release describes one million designs tested against 127 targets. NVIDIA's technical write-up frames the broader campaign more expansively: tens of millions of in-silico candidates were generated, and after filtering, roughly one million were experimentally tested against 133 distinct protein targets, spanning established benchmarks and therapeutically relevant proteins with no previously reported binders.

Those targets were not all easy marks. NVIDIA reports that the model produced binders with nano- and picomolar affinities, including against the Activin Receptor Type-2A — a target relevant to muscle-wasting disorders — for which no comparable mini-binders had been reported. In a harder test still, the team designed proteins that bind sugar molecules on red blood cells, a notoriously intractable class of polar targets; four of 24 designs clumped red cells more efficiently than the natural lectins used in labs today.

## Why the collaboration list matters

The validation was not a two-party affair. NVIDIA credits collaborators including Manifold Bio, Novo Nordisk, Viva Biotech, Duke University, the University of Cambridge, LMU Munich, and the University of Bonn. The presence of Novo Nordisk — a pharmaceutical giant now synonymous with metabolic-disease blockbusters — signals that this is not a purely academic curiosity but a tool major drugmakers are willing to put their names to. The model, code, checkpoints, and datasets have been released openly under permissive licenses.

## What to watch

The open question is whether test-tube binding translates into medicine. A high-affinity binder is a starting material, not a drug; it still must be shown to be safe, manufacturable, and therapeutically useful in living systems. Manifold has hinted at the next step — folding these designs into multiplexed in-vivo studies through its "direct-to-vivo" platform. Watch, too, for whether the scaling law Ogden describes holds: if generating and testing ten times more designs reliably yields more usable hits, functional protein design may follow the same brute-force trajectory that made language models suddenly, unnervingly capable. If it plateaus, the million-binder experiment will be remembered as an impressive benchmark rather than a turning point.
