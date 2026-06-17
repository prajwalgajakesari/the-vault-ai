# Relational Structural Causal Models Push AI Toward Reasoning About Interventions, Not Just Patterns

Modern AI systems are spectacular pattern-matchers. They learn the statistical texture of their training data so well that they can finish a sentence, label a tumor, or predict the next frame of a video. But ask one of those systems what would happen if you *changed* something in the world—reroute the traffic, give the patient a different drug, remove a pedestrian from the scene—and the ground gets shaky. Prediction is not the same as understanding cause and effect, and a model that has only ever *seen* the world has no principled way to reason about *doing* things to it.

A new paper, ["Relational Structural Causal Models"](https://arxiv.org/abs/2606.14892) by Adiba Ejaz and Elias Bareinboim of Columbia University's Causal Artificial Intelligence Lab, announced June 16, 2026, argues that this gap is not a detail to be patched later. It is foundational. To act competently in the world—rather than merely describe it—an AI must carry a model of its environment that is genuinely causal.

## Why pattern-matching hits a ceiling

The conceptual backbone here is the Pearl Causal Hierarchy, often called the ladder of causation, which Bareinboim has spent much of his career formalizing. It has three rungs: association (seeing), intervention (doing), and counterfactuals (imagining). Each rung is strictly more demanding than the one below it.

The catch, captured by the Causal Hierarchy Theorem, is that you cannot climb the ladder for free. Higher-rung questions—what happens if I intervene, what would have happened had I acted differently—generally cannot be answered from lower-rung observational data alone, not without extra assumptions encoded in a causal model. A system trained purely on correlations is stuck on the bottom rung, no matter how much data it sees. This is the precise sense in which "more data" does not, by itself, buy causal understanding.

Structural causal models (SCMs), introduced by Judea Pearl, are the standard machinery for encoding those assumptions. An SCM specifies the variables in a system, the unobserved factors that influence them, and the functions that determine how each variable responds to its causes. From that structure, an SCM implies answers across all three rungs of the hierarchy.

## What relational models add

Classical SCMs, the authors note, assume a fixed cast of characters. The same variables appear every time. But the real world is combinatorial: it is built from objects and the relations among them, and those objects come and go. A driving scene might contain three cars and one pedestrian now, and five cars and two pedestrians a moment later. A useful model has to generalize to combinations of objects it has never encountered before—a property pattern-matchers handle poorly and standard SCMs do not address at all.

The paper's central contribution is to extend structural causal models to exactly these relational, multi-entity settings. The authors develop *relational structural causal models* and then ask a hard question: when can answers about *unseen* combinations of objects actually be pinned down? Their finding is sobering and clarifying at once. Not only causal queries but even observational ones about novel object combinations cannot be identified without further assumptions.

To make identification possible—including in the difficult case of unobserved confounding, where hidden factors influence several variables at once—the authors define *relational causal graphs* and derive symbolic criteria that say precisely when a query is answerable and how to compute it. They then propose *relational neural causal models*, which the paper describes as a provably correct approach. On simulated traffic scenes with varying numbers of cars, signals, and pedestrians, those models outperformed non-relational baselines.

## A frontier for trustworthy, agentic AI

The timing is not incidental. As the field pushes toward agents that take actions rather than just emit text, the inability to reason about interventions becomes a liability rather than an academic curiosity. An agent that books, buys, drives, or prescribes is constantly intervening in the world. If its internal model conflates "things that co-occurred in training" with "things my action will cause," it will be confidently wrong in ways that are hard to detect and harder to trust.

Relational structure raises the stakes further. Agents operate in open worlds full of interchangeable entities—users, files, vehicles, accounts—and the guarantee that matters is generalization to configurations never seen during training. The paper's identification results draw a clean line between what such a system can rigorously claim and what it would merely be guessing at, which is exactly the kind of boundary that audits and safety arguments need.

None of this is a finished engineering recipe. The experiments are simulated, the assumptions behind any causal graph still have to come from somewhere, and scaling these methods to messy real-world data remains open. But the work reframes the problem. The question is shifting from how well a model fits the data it has seen to whether it has the right structure to reason about a world it can act upon. On that frontier, the authors suggest, causality is not optional.

---

*Source: Adiba Ejaz and Elias Bareinboim, ["Relational Structural Causal Models,"](https://arxiv.org/abs/2606.14892) arXiv:2606.14892, announced June 16, 2026.*
