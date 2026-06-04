---
headline: "Study Reveals Gender-Dependent Diagnostic Substitution in LLM Medical Triage Systems"
slug: llm-gender-bias-medical-triage-urgency
category: research
date: 2026-06-03
author: The Vault AI
sources:
  - name: "EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage"
    url: https://arxiv.org/abs/2605.03998
  - name: "Gender Bias in Large Language Models for Healthcare"
    url: https://arxiv.org/abs/2510.08614
  - name: "From Promising Capability to Pervasive Bias"
    url: https://arxiv.org/abs/2504.16273
---

# Study Reveals Gender-Dependent Diagnostic Substitution in LLM Medical Triage Systems

## A sweeping audit of five major AI models finds that swapping a patient's gender in otherwise identical clinical vignettes changes the assigned urgency level up to 44% of the time, with two models systematically undertriaging female patients.

When a 59-year-old woman walks into an emergency department complaining of chest pain, she should receive the same triage priority as a 59-year-old man presenting with identical symptoms, vital signs, and medical history. But a new large-scale fairness audit suggests that AI systems being piloted for hospital triage may not see it that way.

The study, titled EQUITRIAGE and published on arXiv in May 2026 by Richard J. Young of the University of Nevada, Las Vegas and Alice M. Matthews of Concorde Career Colleges, represents the most comprehensive examination to date of gender bias in LLM-based emergency department triage. The researchers evaluated five major language models -- Google's Gemini-3-Flash, NVIDIA's Nemotron-3-Super, DeepSeek-V3.1, Mistral-Small-3.2, and OpenAI's GPT-4.1-Nano -- across 374,275 total evaluations on clinical vignettes derived from real emergency department records.

The methodology was elegant in its simplicity and devastating in its findings. The team constructed 9,346 pairs of clinical vignettes from the MIMIC-IV-ED database, a repository of over 425,000 emergency department visits at Beth Israel Deaconess Medical Center in Boston. Each pair was clinically identical -- same chief complaint, same vital signs, same medications, same medical history -- differing only in the patient's stated gender and a gender-concordant first name. They then asked each model to assign an Emergency Severity Index (ESI) score under four different prompting strategies.

### Every Model Failed the Fairness Test

All five models changed their triage assignments when gender was swapped at rates far exceeding the study's pre-registered 5% threshold for stochastic variation. The counterfactual flip rates ranged from 9.9% for GPT-4.1-Nano to a staggering 43.8% for Nemotron-3-Super. In practical terms, this means that for nearly one in ten patient presentations at best -- and nearly one in two at worst -- simply changing the gender label on an otherwise identical case caused the AI to assign a different urgency level.

More troubling still was the directionality of those flips. Two of the five models showed systematic female undertriage. DeepSeek-V3.1 exhibited the strongest directional bias, with a female-to-male undertriage ratio of 2.15:1, meaning female patients were more than twice as likely to be assigned a lower urgency score than their male counterparts when the AI changed its mind. Gemini-3-Flash followed with a ratio of 1.34:1.

The bias was not evenly distributed across clinical presentations. When the researchers stratified results by chief complaint category, chest pain emerged as the most biased domain. DeepSeek-V3.1 showed a jaw-dropping 9.10:1 female-to-male undertriage ratio for chest pain presentations -- 91 instances of female undertriage versus just 10 of male undertriage in that category. Gemini-3-Flash was not far behind at 4.83:1. This finding is particularly alarming given decades of clinical evidence documenting that women with acute coronary syndrome already experience longer evaluation times and less aggressive diagnostic workups in human-run emergency departments.

### Chain-of-Thought Prompting Made Things Worse

One of the study's most counterintuitive findings involved chain-of-thought (CoT) prompting, a technique widely believed to improve AI reasoning by requiring models to show their step-by-step logic. Rather than reducing bias, CoT prompting degraded triage accuracy for all five models and increased flip rates for four of them. Nemotron-3-Super's flip rate jumped from 43.8% to 63.9% under CoT prompting, and DeepSeek's surged to 57.5%.

This result contradicts prior research suggesting CoT reduces bias in general reasoning tasks. Young and Matthews describe it as a domain-specific failure mode: when forced to articulate clinical reasoning, the models appeared to introduce new errors rather than catch existing ones.

### Demographic Blinding Worked -- But Only Sometimes

The most effective intervention was the blind strategy, which stripped patient name, age, and gender from the clinical vignette entirely. For Gemini-3-Flash, this reduced the flip rate from 11.7% to just 0.5% -- within the range of the study's test-retest stochastic floor -- with only a 2.3% loss in human-concordance accuracy. GPT-4.1-Nano's flip rate dropped to 4.8% under blinding. But the intervention was far from universal: Nemotron-3-Super's flip rate actually increased to 63.5% under the blind condition.

A clever follow-up ablation revealed that different models encode gender bias through entirely different mechanisms. In Gemini, the directional signal was emergent only when both the name and gender token were swapped together; swapping gender alone produced no directional bias. In DeepSeek, the gender token alone carried the signal. An age-preserving blind condition -- which removed name and gender but kept age -- left DeepSeek with a residual female-to-male ratio of 1.25, implicating age as a proxy channel through which bias can re-enter even after demographic identifiers are stripped.

### What This Means for Healthcare AI

The study arrives at a critical moment. Hospitals across the United States are actively piloting LLM-based decision support tools for emergency triage, and the findings raise urgent questions about regulatory readiness. The researchers argue that group-level parity, counterfactual invariance, and gender calibration represent distinct fairness properties that cannot be assumed from one another -- a model can appear fair by one measure while failing dramatically by another.

The clinical stakes are not abstract. Emergency department triage determines the order in which patients receive care, and in time-sensitive conditions like heart attacks and strokes, a one-level difference in triage priority can mean the difference between prompt intervention and dangerous delay. With over 150 million US emergency visits annually, even small systematic biases can translate to large-scale harm.

The central recommendation from EQUITRIAGE is straightforward: per-model counterfactual auditing should be mandatory before any LLM is deployed in a clinical triage setting. No single debiasing strategy works across all models, and the mechanisms driving bias differ fundamentally between architectures. The framework establishes that intervention effectiveness is model-dependent, meaning there is no one-size-fits-all fix.

The broader research landscape reinforces these concerns. A separate 2025 study on gender bias in healthcare LLMs found that consistency rates for assessing clinical relevance of gender dropped as low as 58.97% in some models. Another large-scale audit of nine LLMs across 1.7 million outputs found sociodemographic biases to be pervasive across frontier models.

For healthcare systems racing to integrate AI into clinical workflows, the message from EQUITRIAGE is clear: the same symptoms should produce the same urgency, regardless of who walks through the door. Until that standard is reliably met, these systems are not ready for unsupervised deployment.
