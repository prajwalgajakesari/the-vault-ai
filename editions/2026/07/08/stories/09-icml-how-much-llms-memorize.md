When a jury or a judge eventually rules on whether a chatbot "copied" someone's novel, they will need a number. How much of the book did the model actually keep? For years the honest answer from the research community was a shrug: nobody had a clean way to separate the text a model has genuinely absorbed from the text it merely learned to predict the way any fluent reader would. A paper honored at ICML 2026 finally offers a figure, and it is startlingly precise. A GPT-style language model, the authors conclude, stores about 3.6 bits of information for every parameter it has.

On July 5, the ICML 2026 program chairs named "How much can language models memorize?" one of five Outstanding Paper Honorable Mentions. The work comes from a cross-institution team spanning Meta's FAIR lab, NVIDIA, and Cornell: John Xavier Morris, Chawin Sitawarin, Narine Kokhlikyan, Chuan Guo, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, and Saeed Mahloujifar. What the award committee singled out was not just the headline number but the conceptual machinery the authors built to earn it.

## The Question Underneath the Lawsuits

The debate the paper wades into is deceptively simple to state. When a language model produces text, is it regurgitating stored copies of its training data, or is it generalizing — reconstructing patterns the way a person who has read widely can write a passable sonnet without having memorized any particular one? The answer matters enormously outside the lab. It sits at the center of the copyright suits filed against AI companies by authors, newspapers, and music publishers, and it shapes privacy questions about whether a model can leak the personal data it was trained on.

The trouble is that memorization and generalization look identical from the outside. If a model completes a famous first line correctly, is that because it stored the sentence verbatim, or because the sentence is so predictable that any competent model would guess it? Prior studies, as the authors note, "have struggled to disentangle memorization from generalization." Without that separation, every measurement of "how much a model memorizes" was contaminated by ordinary learning.

## Splitting Memorization in Two

The paper's core move is to define memorization in terms of information — how many bits a model knows about a specific datapoint — and then split that quantity cleanly in two. The award citation lays out the framing:

> "This paper proposes that one could measure Kolmogorov memorization: how much of a distribution is explained by what is learned by a model. But the paper further breaks this down into intended memorization (generalization) and unintended memorization. The theoretical approach of this paper to distinguish unintended from intended memorization is a novel perspective to think about what LLMs are achieving."

Intended memorization is the useful kind: information about the true data-generating process, the statistical structure of language itself. That is generalization, and it is what we want a model to do. Unintended memorization is information about a particular dataset that has nothing to do with the broader distribution — the fingerprint of specific training examples. It is the second category that keeps copyright lawyers and privacy researchers awake.

To pin down capacity, the researchers built a clever test. They trained models on datasets of pure random noise, where there is no underlying pattern to generalize to. Every bit a model retains in that setting has to be raw storage. That let them read off a model's total capacity, and the answer landed consistently between 3.5 and 3.6 bits per parameter across configurations. (Training in full 32-bit precision nudged it up toward 3.83; the leaner bfloat16 format sat around 3.51.)

## When Memorization Turns Into Understanding

The more revealing result came from watching what happens as real training data piles up. The team trained hundreds of transformer models, from 500,000 to 1.5 billion parameters. A model, they found, memorizes individual examples until its fixed capacity fills — and then something flips. Once there is more data than the model can store outright, it is forced to stop hoarding and start finding patterns. That is the onset of "grokking," the well-documented moment when a network abruptly shifts from rote overfitting to genuine generalization. Unintended memorization actually goes down as the model gets better at the task.

That inversion carries a counterintuitive implication for the copyright fight: a model trained on more data, not less, may retain less about any single copyrighted example. Scarcity of data, not abundance, is what pushes a model toward memorizing its inputs.

## Why It Matters

For the first time there is a principled, measurable definition of what a model has "copied" versus what it has "learned," backed by scaling laws that connect model size and dataset size to the risk of extracting a specific example. That gives courts, regulators, and privacy auditors something firmer than intuition. If capacity is roughly 3.6 bits per parameter, a billion-parameter model has a hard ceiling on how much verbatim training data it can physically hold — a fact that could bound both liability and leakage. It also reframes the anxiety about ever-larger training sets: past a threshold, more data dilutes memorization rather than deepening it.

## What to Watch

The measurements are anchored on GPT-style transformers up to 1.5 billion parameters. Whether 3.6 bits per parameter holds for frontier models orders of magnitude larger, for mixture-of-experts architectures, or for multimodal systems remains open. Expect the framework to surface quickly in litigation and policy debates, where "unintended memorization" is a far more testable standard than "substantial similarity." And watch whether the grokking-onset finding reshapes how labs think about the data-to-parameters ratio in their next training runs.
