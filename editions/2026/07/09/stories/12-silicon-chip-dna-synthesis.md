For half a century, silicon chips have been machines for computing. A Harvard-led team has now turned one into a machine for writing the code of life — using nothing more exotic than electricity and water.

In a study published in *Nature Electronics*, researchers report a semiconductor chip that synthesized 64 distinct DNA sequences in parallel on its surface, each up to 39 nucleotides long. Crucially, it did so not with the solvent-heavy chemistry that dominates commercial DNA manufacturing, but through a gentler, water-based enzymatic process choreographed by finely controlled electric currents. The result sets a new benchmark for enzymatic DNA synthesis — and hints at a cleaner, more scalable foundation for the increasingly AI-driven business of designing biology.

## From chemistry to electricity

Synthetic DNA is the raw material of modern biotechnology. Diagnostics, genome engineering, vaccines, and cancer research all depend on being able to write custom strands to order. Today almost all of that DNA is made by phosphoramidite chemistry, a decades-old process that can produce millions of sequences at once but relies on hazardous organic solvents and centralized, industrial-scale facilities.

Enzymatic DNA synthesis has long been pitched as the greener successor. It mimics how living cells build DNA, runs in water, and could eventually shrink DNA-writing down to safe, benchtop — even portable — instruments. The catch has been throughput. Until now, enzymatic methods could manage only about a dozen sequences at a time, a fraction of what chemical synthesis delivers. Against that backdrop, 64 parallel sequences is a meaningful leap.

The work was led by Donhee Ham, the John A. and Elizabeth S. Armstrong Professor of Engineering and Applied Sciences at Harvard's John A. Paulson School of Engineering and Applied Sciences, in collaboration with the Broad Institute, the DNA-synthesis company DNA Script, and Korea's Pohang University of Science and Technology (POSTECH).

## How the chip writes

DNA is assembled one nucleotide at a time. Each freshly added base carries a temporary blocking group that stops the strand from growing further; before the next base can attach, that group has to be stripped off in a step called deprotection. Acidity — low pH — can trigger it.

The trick to parallel synthesis is lowering pH only at the sites due to receive a new base in a given cycle, without disturbing their neighbors. The Harvard chip solves this electrochemically. Each of its 64 synthesis sites holds two concentric ring electrodes surrounding a cluster of anchored DNA. To activate a site, the chip drives current into the inner ring to generate protons, dropping the pH exactly where the enzyme needs to work. Simultaneously, it pulls current from the outer ring to mop up stray protons, penning the acidic zone in place. Cycle by cycle, switching this on only where needed, the chip grows 64 different sequences in lockstep.

The silicon backbone itself is a striking case of reuse. It was originally designed in Ham's lab by former PhD student Jeffrey Abbott to record electrical activity from thousands of neurons at once.

"A defining feature of the chip was precision current injection, which we used to permeabilize neuronal membranes for intracellular access," Ham said. "At a certain point, we wondered whether that same current control could be redirected from cells to molecules — replacing the neuron-facing electrodes with ring-electrode pairs that could localize pH for DNA synthesis. It worked."

## Why cheaper writing matters for AI

The timing is not incidental. As AI systems increasingly propose novel proteins, enzymes, and genetic circuits — from tools like AlphaFold to a wave of generative protein models — the bottleneck is shifting from design to test. A model can dream up thousands of candidate sequences overnight, but each one still has to be written into physical DNA, expressed, and measured to see whether the prediction holds. Cheap, parallel, benchtop DNA writing tightens that design-build-test-learn loop, feeding real experimental results back into the models faster and at lower cost.

The team also gestured at a more distant application: DNA data storage. As a demonstration, they used their 64 sequences to encode a 169-byte snippet of text.

"DNA data storage asks DNA synthesis to operate at a scale far beyond today's needs," said Woo-Bin Jung, co-first author and now an assistant professor at POSTECH, who did the work as a postdoc in Ham's lab. "That is why enzymatic synthesis in water can matter. If far more than 64 sequences can be synthesized in parallel, it could offer an environmentally friendly route toward writing DNA at very large scale."

## The next bottleneck is chemistry, not silicon

When the team tried packing synthesis sites closer together to push density higher, the experiment failed — and the failure was instructive. The chip localized low pH just fine; the problem lay in the deprotection chemistry, where reactive intermediates drifted to neighboring sites and blurred the boundaries.

"The chip did what we asked it to do: it localized low pH at selected sites," said co-first author Han Sae Jung, a postdoctoral researcher at Harvard. "The limitation came from the deprotection chemistry, not from the silicon. That leaves a clear next step for the field — develop a more direct acid-driven deprotection chemistry that can keep pace with the chip."

In other words, the electronics are ready to run ahead. Now the molecules have to catch up.