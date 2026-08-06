---
headline: "'Act As a Real Researcher': A New Benchmark Suite Tests LLMs Across the Full Research Lifecycle"
slug: real-researcher-benchmark-suite
category: research
story_number: 12
date: 2026-08-05
---

# 'Act As a Real Researcher': A New Benchmark Suite Tests LLMs Across the Full Research Lifecycle

Give a modern coding agent a well-specified experiment and it will often run the thing end to end: write the training loop, launch the jobs, plot the curves, even draft the results table. That competence has fueled a wave of claims that AI is on the verge of becoming an autonomous scientist. A new benchmark out of China wants to check that story against a harder question. Not "can the agent run the code?" but "would you trust it as a research intern?"

The answer, for now, is a qualified no.

## A benchmark built around the gaps, not the tasks

In a June 2026 paper titled *Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle*, a team from Xi'an Jiaotong University and Xidian University introduces AARR, a benchmark series meant to evaluate whether large language models can behave like actual researchers across the arc of a project rather than on isolated, self-contained puzzles.

The framing is deliberate. "Despite their evolution from research assistants into autonomous research agents, these systems still exhibit significant limitations in field sensitivity, research ethics, and nuanced scientific judgment," the authors write. "Consequently, frontier agents remain unable to fully replace human researchers." Where most benchmarks reward macro-level execution, AARR targets what the paper calls "the professionalism, thoroughness, and nuanced reasoning that characterize human researchers in granular research scenarios."

AARR is structured as a three-stage ladder of increasing autonomy: AARRI (Act As a Real Research Intern), AARRA (Act As a Real Research Assistant), and AARRS (Act As a Real Research Scientist), which culminates in fully independent discovery. This paper delivers the first rung, AARRI-Bench, a set of 82 containerized tasks. Crucially, the tasks are designed around the cognitive gaps that separate agents from people: context sensitivity, independent judgment, knowing when to stop, and collaboration.

The tasks were sourced from researchers describing real frustrations they hit while using AI agents for science, then organized along two dimensions. Horizontally, tasks fall into four buckets: **context** (reading the situation correctly), **mindset** (research judgment and rigor), **hands-on** (execution), and **interaction** (working with a collaborator). Vertically, they map onto an agent-scope taxonomy that stretches across the research lifecycle, from framing and literature grounding through experiment design, analysis, and write-up.

## Frontier models stall around two-thirds

The headline result is a ceiling. Across combinations of agent harnesses and frontier models, the best-performing configuration, Mini-SWE-Agent paired with Claude Opus 4.7, reached only a **68.3% success rate**, "frequently overlooking subtle yet critical details that are obvious to real human researchers," the authors report. Even that top score sits well short of what you would expect from a competent intern.

The team tested three harnesses (Claude Code, Hermes Agent, and Mini-SWE-Agent) against a broad slate of models including Claude Opus 4.7 and Sonnet 4.6, GPT-5.3 Codex, Qwen-3.6-Plus, Kimi-K2.6, MiniMax-M2.7, and DeepSeek-V4-Flash. Overall scores clustered tightly, from a floor around 51% to that 68.3% peak. In other words, swapping in a stronger model or a fancier scaffold moved the needle only so far.

The most telling number is a gap. When the researchers scored fine-grained test-case pass rates, the same top configuration cleared roughly 90% of individual checks. But under the strict 0/1 reward, where a task counts only if the agent nails its single most important point, performance collapsed to 68.3%, a drop of more than 21 points. Agents were doing most of the busywork correctly while missing the one judgment call that mattered. In one documented case, a harness produced an answer that came close to the scoring criteria but failed to grasp the critical point, while a rival correctly flagged an anomalous data format and passed.

## The limits of "AI as autonomous researcher"

That pattern is the paper's real argument, and it lands directly on the autonomous-scientist narrative. The past year has produced a steady stream of systems claiming end-to-end research automation, from idea generation to manuscript. AARRI-Bench suggests the bottleneck is not scaffolding sophistication. As the authors put it, "developing researcher-like AI requires further exploration of research behavior, rather than merely complex scaffolding."

The skills that separate a good intern from a fast one, knowing when a result looks too clean, sensing that a dataset is mislabeled, deciding an experiment is not worth running, resist brute-force engineering. They are exactly the "field sensitivity" and "scientific judgment" the paper flags as missing. A benchmark that rewards these behaviors, rather than raw task completion, is a useful corrective at a moment when leaderboards are saturating and headline capabilities are easy to oversell.

There are caveats. At 82 tasks, AARRI-Bench is small, and its 0/1 scoring is intentionally unforgiving, which makes it a sharp diagnostic but a coarse ranking tool. The rubric-driven judgments also carry the usual questions about how "critical detail" is defined.

## What to watch

The more interesting test comes next. AARRI is the intern tier; the planned assistant (AARRA) and scientist (AARRS) benchmarks will push toward independent contribution, critical evaluation, and genuine discovery, where the gaps this paper measures should widen further. If frontier systems keep hovering in the high 60s on entry-level research diligence, the "autonomous researcher" pitch will need to reckon with a stubborn truth: the hard part of science was never running the code.
