# Researchers Push for Explainable Protein-Design AI to Crack Open the Black Box

The same class of AI models that lets scientists dream up enzymes never seen in nature is also one of the least understood tools in modern biology. Now a team in Barcelona wants to change that before these systems quietly become fixtures of drug discovery, industrial chemistry and climate technology.

In a perspective paper published in *Nature Machine Intelligence* on May 10, 2026, researchers at the Centre for Genomic Regulation (CRG) lay out what they call the most comprehensive survey to date of "explainable AI" for protein language models, together with a roadmap for making the technology transparent, trustworthy and safe to deploy. Protein language models, or pLMs, borrow the architecture of large language models like the ones behind chatbots, but instead of learning from text they learn the statistical grammar of amino acid sequences. Trained on hundreds of millions of natural proteins, they can now generate entirely novel sequences with useful properties on demand.

The catch, the authors argue, is that almost nobody can explain why a given model produces a given answer.

"Protein language models are moving fast but our understanding of fundamental biological processes such as folding or catalysis has not advanced alongside these breakthroughs," said Dr. Noelia Ferruz, a group leader at the CRG and the paper's corresponding author. "In some ways, we have even lost part of the transparency that characterized physics-based models. Without better ways to explain what these models learn and how they make decisions, we risk building powerful tools that we cannot fully trust."

## Four places to look inside the box

The review, led by first author Andrea Hunklinger, reframes a scattered and technically dense literature around a simple question: when you want to know why a model made a prediction, where should you look? The authors identify four points along a model's pipeline.

The first is the **training data** itself, which can reveal whether a model carries biases, such as underrepresenting human genetic diversity or lacking enough human proteins to begin with. The second is the **input sequence**, the equivalent of asking which amino acids or regions of a protein most influenced a prediction, much as a housing-price model might weigh square footage or location. The third is the **model's internal architecture**, described as opening the hood to check whether the artificial neurons are processing information correctly. The fourth is **input-output behavior**, probing the system by slightly altering a sequence or a question and watching how the answer shifts.

Mapping the terrain matters because researchers have begun importing heavy interpretability machinery from mainstream AI. Among the concrete techniques the field is testing: attention analysis inherited from the "BERTology" tradition of dissecting language models; supervised probing classifiers that check whether biological concepts are encoded in a model's internal representations; and, most notably, sparse autoencoders (SAEs), an unsupervised method that decomposes a model's tangled internal activations into cleaner, human-readable features. Recent work has shown that SAE features extracted from ESM2, one of the most widely used pLMs, line up tightly with Gene Ontology terms, and related efforts have used automated neuron labeling to steer models toward desired traits.

## Five jobs for explainability

Surveying dozens of studies, the CRG team sorts the goals of this work into five roles. In nearly every case, explainability today acts as an **Evaluator**, confirming that a model has learned patterns biologists already recognize, such as binding sites or structural motifs. A smaller set of studies use it as a **Multitasker**, repurposing learned signals to annotate new proteins. Rarer still are the **Engineer** and **Coach** roles, where insights are used to trim components, redesign architectures and steer sequence generation.

The fifth role, the **Teacher**, is the most ambitious and the least realized. A Teacher model would reveal genuinely new biological principles that humans had not recognized. The authors compare it to the moment AlphaZero began surprising chess grandmasters with novel strategies, or when AI helped reconstruct damaged ancient texts.

"While Evaluators are useful to benchmark the model's quality, they do not allow to extrapolate to unknown examples, improve the models' architecture, and more importantly, reveal biological insights that emerge from the training data," Hunklinger said.

## Why It Matters

Protein design sits at a rare intersection where an opaque model's output becomes a physical molecule with real-world consequences. A pLM's suggestions may end up as a therapeutic antibody, an industrial catalyst, or an enzyme engineered to pull carbon dioxide from the air. When those recommendations rest on statistical correlations rather than mechanistic understanding, a wrong or biased prediction is not just an inconvenience, it can waste months of lab work or, in the wrong context, raise biosecurity concerns about dual-use design.

That is why the roadmap deliberately echoes the broader interpretability movement now reshaping AI. Sparse autoencoders, the technique generating the most excitement in protein circles, are the same tool that labs like Anthropic have used to expose interpretable features inside large language models. The CRG authors are effectively arguing that biology cannot afford to treat explainability as an afterthought the way much of the AI industry once did. Trust, reproducibility and safety, they contend, have to be engineered in, not bolted on. Their call for open-source tooling and shared benchmarks reflects a field trying to standardize before commercial pressure locks in black-box norms.

## What to Watch

The authors stress that reaching Teacher status will not happen on its own. They call for robust benchmarks that can test whether an explanation genuinely reflects a model's reasoning rather than a plausible-sounding story, and for open-source tooling that makes interpretability comparable across labs. Crucially, they insist that any AI-derived insight be validated experimentally in the wet lab before it counts as biological knowledge.

Ferruz frames the destination as controllable design. "Imagine being able to tell a model: 'Design a protein with this shape, active at this pH,' and not only receive a candidate sequence, but also a clear explanation of why that design should work, and importantly, why alternatives would fail," she said. Reaching that level of mechanistic transparency, she added, "would move protein language models from impressive generators to truly reliable design partners." Watch for whether the interpretability toolkit maturing in mainstream AI can make that leap, and whether regulators and journals begin demanding explanations alongside sequences.