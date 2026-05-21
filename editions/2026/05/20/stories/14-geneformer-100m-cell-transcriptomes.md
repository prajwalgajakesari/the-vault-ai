---
title: Geneformer Model Scales to 100 Million Human Cell Transcriptomes for Network Biology Predictions
slug: geneformer-100m-cell-transcriptomes
category: research
story_number: "14"
date: 2026-05-20
sources:
  - https://www.nature.com/articles/s43588-026-00972-4
  - https://www.nature.com/articles/s43588-026-00990-2
  - https://www.nature.com/articles/s41596-026-01364-8
  - https://huggingface.co/ctheodoris/Geneformer
---

# Geneformer Model Scales to 100 Million Human Cell Transcriptomes for Network Biology Predictions

A transformer model that once learned the language of human biology from 30 million cells has now consumed more than 104 million — and the difference is not merely one of scale. Published in Nature Computational Science this spring, a new study shows that Geneformer, the foundational AI model for single-cell transcriptomics developed by Christina V. Theodoris and colleagues, has grown from a 10-million-parameter system into a 316-million-parameter architecture whose predictive power on gene network tasks follows a clean power law: more data, more parameters, better biology.

The implications stretch far beyond benchmark scores. Geneformer is one of a small class of AI tools that can predict which genes are central to disease-driving networks, which transcription factors can be nudged to reprogram cell fate, and which targets are most likely to improve outcomes in conditions such as cardiomyopathy — all without wet-lab experiments. At 316 million parameters pretrained on a transcriptomic corpus now called Genecorpus-104M, the model represents the most comprehensive attempt yet to encode the regulatory logic of the human cell into a single, transferable model.

## From 30 Million Cells to 104 Million

The original Geneformer, introduced in 2021 and published in Nature in 2023, was pretrained on approximately 30 million single-cell transcriptomes. The core innovation was the representation strategy: rather than feeding each cell's raw gene expression counts into the model, Geneformer ranks each cell's genes by expression level, foregrounding the informative signal — transcription factors, pathway nodes, lineage markers — while pushing ubiquitous housekeeping genes to the back. The ranked list becomes a sentence; the cell becomes a document; the corpus becomes a library encoding the grammar of cellular identity.

For the 2026 update, the team assembled Genecorpus-104M, a corpus of approximately 104 million human single-cell transcriptomes drawn from a broad range of tissues and disease states. Successively larger models were pretrained on this data — from smaller configurations up to the 316-million-parameter flagship — allowing the researchers to map the scaling laws for transcriptional masked learning with the same rigor that language model researchers apply to text.

The results were unambiguous. The 316-million-parameter model pretrained on more than 100 million transcriptomes significantly outperformed the original 10-million-parameter model on both gene-level and cell-level tasks, with zero-shot performance — meaning predictions made without any task-specific fine-tuning data — improving most dramatically on the hardest biological challenges.

## Quantization Brings Research-Grade AI to Ordinary Hardware

A second major contribution of the 2026 work is model quantization. Large foundation models are computationally expensive, and the gap between a model's theoretical capabilities and what a typical academic lab can run in practice has grown alongside model size. The Geneformer team applied quantization techniques that compress the full-precision model into a more compact numerical representation, dramatically reducing resource requirements while preserving biological fidelity.

The numbers are striking: quantized Geneformer requires only 15 percent of the inference time and 34 percent of the computational resources of the full-precision model, with no meaningful loss of performance on zero-shot or fine-tuning benchmarks. The contextual gene and cell embedding space — the learned geometric representation of biological relationships — is preserved intact. Researchers with modest GPU budgets can now run a state-of-the-art network biology model that would previously have demanded significant cloud compute.

"The largest model shows the highest zero-shot performance on both gene- and cell-level biologically meaningful tasks," the authors note, underscoring that the scaling gains are not confined to fine-tuned applications but extend to entirely novel prediction problems where no labeled training data exists. That property is particularly valuable for rare diseases, clinically inaccessible tissues, and emerging cell types where labeled datasets may never reach the scale needed to train task-specific models from scratch.

## What the Model Can Do — and Why It Matters for Drug Discovery

Geneformer's practical utility spans a range of network biology tasks that map directly onto drug discovery workflows. The model can distinguish transcription factor dosage sensitivity, predict gene network centrality, characterize bivalent chromatin dynamics, model transcription factor regulatory range, and simulate the effects of gene perturbations in silico — all from a ranked expression profile of a single cell.

The therapeutic target prediction capability has already demonstrated real-world impact. Earlier work using Geneformer identified a novel transcription factor in cardiomyocytes through zero-shot learning alone — a finding that would have required extensive wet-lab screening to reach through conventional methods. The model also predicted candidate therapeutic targets for cardiomyopathy that subsequently improved contractility in an induced pluripotent stem cell model of the disease, providing in vitro validation of a computationally generated hypothesis.

With the expanded 104-million-cell corpus, the model's tissue and disease coverage is substantially broader, which should improve generalization to disease contexts not well represented in the original 30-million-cell training set. The addition of disease-state transcriptomes — cells drawn from patients rather than healthy donors — is particularly significant for therapeutic target identification, where the relevant biology is the perturbed network, not the healthy baseline.

A companion paper published simultaneously in Nature Protocols describes a practical workflow for using Geneformer to discover candidate therapeutic targets, lowering the barrier for research groups who want to apply the model to their own disease areas without building the infrastructure from scratch.

## Open Science, Accessible Infrastructure

The updated Genecorpus-104M, all Geneformer model weights, and quantization code are freely available on the Hugging Face Model Hub, continuing the open-science ethos of the original release. That accessibility matters: foundation models for biology derive much of their value from broad community adoption, diverse fine-tuning applications, and the accumulation of domain-specific benchmarks that collectively sharpen understanding of where the models succeed and where they fail.

The scaling law characterization is itself a contribution to that collective understanding. By demonstrating that transcriptional masked learning follows a power law relationship between model parameters, pretraining data, and downstream task performance, the 2026 work provides a principled roadmap for the next generation of biological foundation models. The question is no longer whether more data and larger models improve biological predictions — it is how far the scaling curve extends before it flattens, and what complementary architectural innovations will be needed to push beyond it.

For a field that has historically operated at the scale of thousands of cells per experiment, a model that has processed 104 million transcriptomes representing the breadth of human tissue diversity represents a genuine inflection point. The biology encoded in those cells — every disease state, every developmental transition, every tissue-specific gene regulatory program — is now, in compressed form, available for interrogation at the cost of a forward pass through a 316-million-parameter transformer.

---

*Sources: Nature Computational Science, Nature Protocols, Hugging Face*
