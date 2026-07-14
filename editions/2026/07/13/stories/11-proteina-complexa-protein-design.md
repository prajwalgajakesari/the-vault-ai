# Proteina-Complexa, a Protein-Design Reasoning Model, Validates a Million AI-Designed Binders

*Category: Research*

For years, the standard rebuttal to any splashy AI-for-biology result was the same: it looks great in silico, but does it work in a test tube? A collaboration between NVIDIA and the Boston startup Manifold Bio has now answered that question at a scale that is difficult to argue with. Using a new generative model called Proteina-Complexa, the teams designed roughly one million protein binders, then physically tested them against more than 130 targets in the lab — measuring over 100 million protein-protein interactions in a single multiplexed experiment.

The result is one of the largest experimentally validated benchmarks in the short history of generative biology, and a pointed statement about where the field is heading: away from leaderboard scores and toward wet-lab evidence at industrial scale.

## What the model actually does

A protein binder is a protein engineered to latch onto a specific target — another protein, or a small molecule — the way a key fits a lock. Binders are the workhorses of modern therapeutics, underpinning antibodies, diagnostics and targeted drugs. The trouble is that the space of possible amino-acid sequences and 3D shapes is astronomically large, and finding one that binds tightly and specifically has historically taken months of trial and error.

Proteina-Complexa, released by NVIDIA and built on top of its earlier La-Proteina system, attacks the problem with a technique the team calls co-design. Rather than treating backbone generation and sequence design as separate steps — the modular approach used by influential predecessors like RFdiffusion — the model generates the full atomistic structure (backbone and side-chains) and the amino-acid sequence simultaneously. According to NVIDIA's technical writeup, this ensures that "chemical identities and 3D geometry are tightly coupled," producing interfaces optimized for folding and synthesis and enabling a direct handoff to lab testing without intermediate modeling.

The model was trained on over one million curated experimental and predicted structures drawn from the Protein Data Bank, the AlphaFold database and other sources. Its most distinctive feature, though, is borrowed from the world of large language models: test-time compute scaling. During generation, "reasoning" search algorithms such as Beam Search and Best-of-N evaluate and refine candidate binders at intermediate steps, spending extra computation on the hardest targets — much as a reasoning LLM thinks longer before answering a difficult question.

"With test-time scaling, we've enabled the model to refine its logic before outputting a single sequence," said Anthony Costa, Director of Digital Biology at NVIDIA. NVIDIA says the approach runs 30 to 60 times faster than RFdiffusion when designing custom binders.

## Why validation at scale is the real story

The eye-catching number is not the model architecture but the experiment behind it. NVIDIA reports that after generating tens of millions of in-silico candidates, roughly one million binders were filtered and experimentally tested against 133 distinct targets — ranging from well-worn benchmark proteins to therapeutically relevant targets with no previously reported binders.

That throughput came from Manifold Bio, which supplied the wet-lab muscle. In its own announcement dated March 16, 2026, Manifold said it tested one million binder designs against 127 targets in a single multiplexed phage-screening experiment, identifying specific binders to 68% of targets. The company had previously demonstrated the same measurement platform in October 2025 with mBER, an antibody-design model it used to screen 1.1 million VHH antibodies against 145 targets.

"Manifold Bio's platform uniquely enabled this massively multiplexed study, which establishes Proteina-Complexa as competitive with state-of-the-art methods," said Pierce Ogden, co-founder and Chief Technology Officer of Manifold Bio. "This study provides a practical demonstration of scaling laws in de novo protein design, with more designs producing more hits, and makes the case for inference scaling when experimental throughput can keep pace."

That last clause is the crux. Inference-time scaling only pays off if you can test the flood of designs it produces. The bottleneck has quietly shifted from "can we design candidates?" to "can we test them fast enough to learn?"

## Pushing into hard targets

Beyond raw hit rates, the teams reported qualitative wins on problems that have stymied earlier methods. Using surface plasmon resonance and other assays, they measured binders with nano- and picomolar affinities, including strong binders against Activin Receptor Type-2A — a muscle-wasting target for which, they note, no comparable mini-binders had been reported.

More striking, the group designed proteins that bind sugars on red blood cells, a notoriously difficult task because carbohydrates are small, polar and wrapped in water. Of 24 candidates, four clumped red blood cells more efficiently than the natural lectins labs currently rely on — polar surfaces that existing AI tools have largely failed on.

## Analysis: the economics of generative biology

The competitive context matters. RFdiffusion, from the Baker Lab, opened the modern era of diffusion-based binder design; Google DeepMind's AlphaProteo pushed hit rates and affinities higher in 2024. Proteina-Complexa's differentiators are its unified co-design architecture, its reasoning-style inference scaling, and — crucially — an open release of code (Apache 2.0), model checkpoints and datasets. For a field where the most capable tools have often been gated, that openness lowers the barrier for academic and startup labs.

The deeper shift is economic. If designing a plausible binder is cheap and testing a million of them is feasible, drug discovery starts to look less like artisanal engineering and more like a search problem with tunable compute. The presence of Novo Nordisk, alongside Viva Biotech, Duke, Cambridge, LMU Munich and Bonn, signals that large pharma is treating this as pipeline infrastructure, not a demo.

## What to watch next

The obvious next milestones are downstream of binding: do these designs survive the leap from a phage-display hit to a molecule with the developability, stability and safety a drug requires? Manifold's stated ambition is to fold in multiplexed in-vivo data, which would test binders in living organisms rather than assays. Watch, too, for peer-reviewed publication of the validation study, for independent labs reproducing the hit rates on their own targets, and for whether the "scaling laws" Ogden describes hold as targets get harder. The claim that more designs reliably yield more hits is powerful — if it survives contact with the messiest targets in the clinic.
