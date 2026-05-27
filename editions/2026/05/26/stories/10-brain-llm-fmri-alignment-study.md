---
headline: "Researchers Map Brain-LLM Alignment Using fMRI Data From 112 Participants"
slug: brain-llm-fmri-alignment-study
category: research
story_number: "10"
date: 2026-05-26
author: The Vault AI
tags: [neuroscience, fMRI, LLM alignment, brain-computer interface, multilingual NLP, tokenization, cognitive science]
---

# Researchers Map Brain-LLM Alignment Using fMRI Data From 112 Participants

For years, neuroscientists and AI researchers have danced around a tantalizing question: do large language models process language the way the human brain does? A growing body of work has shown that the internal representations of LLMs can predict patterns of neural activity recorded during reading -- but nearly all of that evidence has come from English speakers reading English text. A new study from researchers at the University of Hong Kong now dramatically expands the picture, using functional MRI data from 112 participants across three languages and seven models to show that the apparent alignment between brains and LLMs is driven not by any universal property of language, but by something far more mundane -- the composition of a model's training data.

## A Trilingual Brain Scanning Experiment

The preprint, titled "Brain-LLM Alignment Tracks Training Data, Not Typology," was posted to arXiv on May 21, 2026 by Dongxin Guo, Jikun Wu, and Siu Ming Yiu. It has been accepted to CoNLL 2026. The researchers collected fMRI recordings from 112 participants -- native speakers of English, Chinese, and French -- as they read aligned translations of Antoine de Saint-Exupery's Le Petit Prince. By using the same literary text across all three languages, the team could isolate linguistic and model-level variables from the content itself.

The study evaluated seven large language models spanning three categories: English-dominant models (including Meta's LLaMA-2-7B), a Chinese-dominant model (Baichuan2-7B), and multilingual architectures. The critical experimental design choice was to compare architecture-matched models that differed primarily in training data composition. "Our central finding is that training-language dominance, not an inherent property of English, drives the alignment pattern," the authors wrote in the paper.

## The English Advantage Was an Illusion

The headline result overturns a long-standing assumption in the field. Previous studies had consistently found that LLM representations aligned more closely with brain activity in English speakers than in speakers of other languages, leading some researchers to speculate that English possessed some structural property that made it inherently more compatible with transformer-based language processing.

Guo and colleagues showed this was wrong. When they tested Baichuan2-7B -- a Chinese-dominant model with an architecture matched to LLaMA-2-7B -- the alignment gradient reversed entirely. The Chinese-dominant model aligned best with Chinese-speaking brains and worst with English-speaking brains. "These results reveal that the apparent 'English advantage' in brain-LLM alignment is an artifact of training data composition," the researchers concluded.

The finding has immediate practical implications for how the field interprets alignment studies. Any comparison of brain-model fit across languages must now account for the language distribution in training corpora -- a variable that most prior work either ignored or treated as fixed.

## Syntax and Semantics Tell Different Stories

Beyond the top-line training data effect, the study uncovered a striking dissociation between different brain regions. Syntax-associated areas, particularly the inferior frontal gyrus (IFG), showed a 2.3 times steeper gradient in alignment degradation as typological distance between languages increased, compared to lexico-semantic regions in the posterior temporal lobe (PTL). In other words, the brain regions responsible for parsing grammatical structure were far more sensitive to mismatches between a model's training language and a reader's native language than regions responsible for processing word meanings.

The researchers also identified a mechanical explanation for part of the cross-linguistic variation: tokenization fertility -- the number of tokens a model's tokenizer produces for equivalent text in different languages -- accounted for roughly 60% of a cross-linguistic shift in the optimal encoding layer. Models that over-segment non-dominant languages effectively push the best-matching layer deeper into the network, a finding that connects low-level engineering decisions about tokenizer design to high-level questions about neural representation.

## Why This Matters for AI

The study arrives at a moment when brain-LLM alignment research is rapidly moving from curiosity-driven neuroscience into practical relevance. Understanding where and why model representations converge with neural activity could inform the design of more cognitively aligned AI systems, improve brain-computer interfaces that decode language from neural signals, and sharpen evaluations of whether LLMs truly "understand" language in any meaningful sense.

The Guo et al. findings introduce an important caution: much of what has been interpreted as evidence that LLMs mirror human language processing may instead reflect the statistical fingerprint of training data. If an English-dominant model aligns well with English-speaking brains simply because both have been shaped by English text, the alignment may tell us more about shared data distributions than about shared computational strategies.

For the multilingual AI community, the tokenization fertility finding is particularly actionable. It suggests that improving tokenizer quality for underrepresented languages could meaningfully change how well models align with speakers of those languages -- not just in benchmark performance, but in the deeper sense of matching neural processing patterns.

## What to Watch Next

The study examined three languages from two language families. Replication across more typologically diverse languages -- including agglutinative, polysynthetic, and tonal languages beyond Mandarin -- will be essential to confirm how general these patterns are. Researchers should also watch for studies that scale the analysis to larger models, where the relationship between training data composition and brain alignment may shift. The reported 2.3x IFG-PTL gradient difference and the 60% tokenization fertility contribution are specific, testable predictions that future work can either confirm or refine. For now, the message is clear: before claiming that an LLM thinks like a brain, check what language it was trained on.