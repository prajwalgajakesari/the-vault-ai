## When Pure Deep Learning Hits a Wall, Physics Steps In

For years, researchers hailed AlphaFold as the solution to biology's grand protein-folding challenge. And in many ways it was — for single-domain proteins with known structural relatives, the accuracy was staggering. But the human proteome is full of large, multi-part proteins that don't fit that mold: sprawling, multi-domain structures with few template relatives, intricate geometries that pure deep learning struggles to stitch together reliably. A team at the National University of Singapore (NUS) now has an answer. Published in *Nature Biotechnology*, their method — D-I-TASSER — couples deep learning with physics-based simulation and clears the bar that AlphaFold-style predictors have repeatedly stumbled over.

In blind benchmark tests, D-I-TASSER predicted complex protein structures roughly 13% more accurately than existing state-of-the-art methods, outperforming both AlphaFold2 and AlphaFold3 across a range of difficult targets. For a field where fractions of an angstrom can determine whether a drug fits its target, that margin is not incremental — it is meaningful.

## How D-I-TASSER Works

The name is a lineage marker: D-I-TASSER descends from the long-running I-TASSER platform developed in the Zhang lab, now upgraded with deep learning at every stage. Where I-TASSER relied primarily on threading and fragment assembly guided by physical energy functions, D-I-TASSER layers in multi-source deep learning potentials — distance maps, contact predictions, hydrogen-bonding restraints — before handing the problem back to iterative physics-based simulation.

The critical architectural innovation is a domain-splitting and reassembly protocol. When a large, multi-domain protein arrives, D-I-TASSER does not try to fold the entire chain at once. Instead, it slices the protein into tractable segments, predicts each fragment's structure independently using deep learning restraints, then uses physical modeling to assemble those fragments into a coherent full-chain structure. The physical constraints — energy minimization and geometry enforcement — act as a reality check on the deep learning outputs, preventing the distortions and clashes that can accumulate when long chains are modeled end-to-end.

This hybrid design makes D-I-TASSER especially powerful precisely where pure deep learning predictors are weakest: proteins without close structural templates in the database, and large multi-domain assemblies where interdomain geometry matters as much as local fold accuracy.

## The Numbers Behind the Claims

Accuracy is measured by TM-score, a geometry-based metric normalized for protein length where above 0.5 indicates a correct fold and above 0.8 near-atomic accuracy. In CASP15 — the biennial blind prediction challenge widely regarded as the field's gold standard — D-I-TASSER posted an average TM-score 18.6% higher than the public AlphaFold2 server on free modeling (FM) domains, where no close templates exist. On multi-domain proteins that gap grew to 29.2%. Across 230 multi-domain proteins on a separate large-scale benchmark, D-I-TASSER outperformed AlphaFold2 in 88% of cases with a 12.9% average TM-score improvement, and it generated correct folds for 95% of CASP15 domains overall.

## In the Researchers' Own Words

The work comes from Professor Zhang Yang, who holds joint appointments at NUS's Cancer Science Institute of Singapore, School of Computing, and Yong Loo Lin School of Medicine.

"For most proteins, we still do not know their 3D structures, and that remains a major blind spot in biology," Prof Zhang said. "A protein's shape determines what it does in the body, but many large, multi-domain proteins are too complex for existing tools to model reliably."

The downstream promise is equally direct. "When we can see a protein's structure more clearly, we can better understand what goes wrong in disease and how potential drugs might interact with it," Prof Zhang added.

The human body encodes roughly 20,000 proteins. Many are multi-domain, and for a significant fraction, reliable structural models remain elusive. D-I-TASSER generated reliable structural models for most proteins in the human proteome, including many that had previously resisted computational analysis.

## Why the AI-Plus-Physics Paradigm Matters

The rise of D-I-TASSER reflects a broader reckoning with end-to-end deep learning in structural biology. AlphaFold and its successors are extraordinarily powerful, but they are also fundamentally pattern-matchers: they excel when training-set relatives exist and degrade when the problem is genuinely novel. Physics-based simulation is slower and computationally heavier, but it enforces atomic-level physical constraints that deep learning can violate when extrapolating to unfamiliar territory.

Hybrid methods like D-I-TASSER treat the two approaches as complementary rather than competing. Deep learning provides rapid, information-dense restraints that steer simulation away from unproductive conformational space; physics-based refinement ensures the final model is geometrically sound. The result is more accuracy on hard targets without sacrificing speed.

For drug discovery, the stakes are high. Multi-domain proteins dominate disease target lists — receptor tyrosine kinases, nuclear receptors, large scaffolding proteins, allosteric regulators. Reliably modeling their interdomain geometry opens structure-based drug design avenues that were effectively closed before. Better antibody-antigen interface models, in particular, could accelerate biologics pipelines considerably.

## What to Watch

The Zhang lab has signaled several next steps. The D-I-TASSER framework is being extended to RNA structure prediction and to protein-protein interaction modeling, with a particular focus on antibody-antigen complexes. Most ambitiously, the team aims to move beyond static structure prediction altogether, integrating AI with physics-based modeling to capture folding pathways — how a protein reaches its final shape inside the cell, not just what that shape looks like. If that effort succeeds, it would shift computational biology from predicting protein endpoints to understanding the journey.

D-I-TASSER is currently accessible through the Zhang group's servers, and its publication is a clear marker: the next generation of structure prediction tools will not be pure deep learning — they will be hybrids that know when to let physics have the final word.
