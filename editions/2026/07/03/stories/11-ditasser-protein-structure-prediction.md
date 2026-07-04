For most of the last five years, the story of computational biology has been the story of AlphaFold — the deep-learning system from Google DeepMind that made protein-structure prediction look, at times, like a solved problem. A quieter rival has been arguing otherwise. It is called **D-I-TASSER**, and its central claim is that pure deep learning is not enough: to get the hardest proteins right, you also need physics.

Developed by a team led by **Professor Zhang Yang** at the National University of Singapore — spanning the Cancer Science Institute of Singapore, the School of Computing and the Yong Loo Lin School of Medicine — D-I-TASSER is a hybrid pipeline that couples neural-network predictions with old-fashioned physics-based folding simulations. Published in **Nature Biotechnology** in 2025 and spotlighted by NUS in February 2026, the method reports beating both AlphaFold2 and AlphaFold3 on the proteins that matter most to disease research: the large, floppy, multi-domain molecules that make up much of the human body.

"For most proteins, we still do not know their 3D structures, and that remains a major blind spot in biology," Zhang said. "A protein's shape determines what it does in the body, but many large, multi-domain proteins are too complex for existing tools to model reliably."

## How D-I-TASSER works

D-I-TASSER — the "D" stands for deep-learning, grafted onto the lab's long-running I-TASSER (Iterative Threading ASSEmbly Refinement) engine — takes a divide-and-conquer approach. Rather than feed an entire sprawling protein into a single model, it slices the molecule into smaller, tractable domains, predicts the shape of each fragment using multi-source deep-learning restraints, and then reassembles the pieces under strict physical constraints through simulated folding.

"The system breaks a complex protein into smaller sections, predicts the shape of each section first, and then uses physical modelling to assemble them into a complete three-dimensional structure," the NUS team explained — a domain-splitting and reassembly protocol that gives D-I-TASSER a notable edge on the interdomain geometry that trips up end-to-end AI models.

The benchmark numbers are specific. Across **500 nonredundant hard protein domains**, D-I-TASSER posted an average TM-score of **0.870** — roughly 5% higher than AlphaFold2 and higher than all AlphaFold versions including v3. On **230 multidomain proteins**, it produced better full-chain TM-scores in **88% of cases**, with an average improvement of **12.9%** over AlphaFold2. That translates to the headline figure NUS emphasized: complex protein structures predicted about **13% more accurately** than existing state-of-the-art methods.

The pedigree runs deep. Earlier incarnations of the pipeline, entered as "Zhang-Server" and "UM-TBM," ranked as the No. 1 automated server in the community-wide **CASP14 and CASP15** blind assessments, in both single-domain and multi-domain categories. CASP16, the round that gave the field its first look at AlphaFold3, kept the Zhang group's approach in the top tier.

The team then did what benchmark champions rarely do: it ran the method at scale. D-I-TASSER was applied to the entire human proteome — roughly **19,512 human proteins** — and, according to the researchers, covered a larger fraction of foldable sequences than the widely used AlphaFold Structure Database. Those genome-wide models and the software itself have been released freely through zhanggroup.org.

## Why It Matters

The significance here is less "AlphaFold has been dethroned" and more "the winning recipe may be a blend." AlphaFold's triumph convinced much of the field that structure prediction was fundamentally a pattern-recognition problem best left to ever-larger neural networks. D-I-TASSER is a well-credentialed counterargument: for the gnarliest targets — big multi-domain proteins whose parts hinge and swivel relative to one another — grounding the AI's guesses in physical laws produces measurably better models.

That matters most for **drug discovery**. A protein's 3D shape dictates where a drug molecule can bind, and errors in interdomain orientation can send a computational drug-design campaign chasing pockets that do not exist. "When we can see a protein's structure more clearly, we can better understand what goes wrong in disease and how potential drugs might interact with it," Zhang said. Multi-domain proteins — receptors, signaling scaffolds, many cancer-relevant targets — are exactly the molecules where accuracy has lagged and where better models could shorten the path to targeted therapies.

There is also a strategic dimension. A freely available, physics-augmented alternative to a DeepMind product keeps the field's methodological diversity alive and gives academic labs a competitive tool that does not depend on a single company's roadmap.

## What to Watch

The obvious caveat: the core research is a 2025 Nature Biotechnology paper amplified by a February 2026 institutional announcement, not a fresh July 2026 release. Independent CASP16 write-ups and third-party benchmarks will ultimately decide how durable the "beats AlphaFold3" claim proves once other groups reproduce it on their own test sets.

The more interesting frontier is where Zhang's team is heading next. The lab is extending the framework beyond static structures to **RNA prediction** and **protein–protein interactions**, with a stated focus on antibody–antigen complexes — a direct entry into the therapeutics arena. Further out, the researchers want to use the same AI-plus-physics marriage to model the **folding pathways** proteins actually follow inside living cells, not just their final shapes.

If that works, it would push the field past the question AlphaFold answered — what does a protein look like? — toward the harder one physics was always meant to address: how does it get there?
