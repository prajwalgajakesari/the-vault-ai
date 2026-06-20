---
headline: "ScaleSWE Mines Millions of GitHub Pull Requests to Turn Small Open Models Into Capable Coding Agents"
slug: "scalesswe-github-pr-coding-agents"
category: "research"
story_number: 12
date: "2026-06-19"
---

# ScaleSWE Mines Millions of GitHub Pull Requests to Turn Small Open Models Into Capable Coding Agents

The most valuable training resource for building a coding agent has been sitting in plain sight all along: the billions of merged pull requests that developers have already written, tested, and shipped on GitHub. A research effort called ScaleSWE has now built an automated pipeline to harvest that resource at industrial scale—sifting six million pull requests across thousands of repositories—and used it to push a comparatively small open model to a roughly 64% resolve rate on SWE-bench Verified, the field's most-watched benchmark for software-engineering agents.

That number is the headline, but the method is the story. ScaleSWE is less a model than a factory for the data that models learn from, and it lands squarely in one of 2026's defining research arguments: whether the future of capable coding agents belongs to ever-larger frontier systems, or to small open models trained on better data.

## What ScaleSWE actually built

The work is described in a paper titled "Immersion in the GitHub Universe: Scaling Coding Agents to Mastery," posted to arXiv (2602.09892). At its center is what the authors call an "automated, sandboxed multi-agent workflow" for constructing software-engineering training data without the manual curation that has bottlenecked earlier datasets.

The pipeline coordinates three specialized agents. An environment-builder agent stands up an isolated Docker container for a target repository, autonomously reading files like `setup.py`, `pyproject.toml` and `README.md` to infer dependencies and resolve conflicts by parsing terminal feedback—work the paper notes "can be challenging even for experienced developers to set up correctly." A unit-test creator agent synthesizes executable Fail-to-Pass and Pass-to-Pass test cases, the validation backbone that determines whether a candidate fix actually works. A problem-statement agent then writes a clean, self-contained task description grounded in the pull request and its tests.

Run that loop over GitHub at scale and you get Scale-SWE-Data: 100,000 verified, executable task instances drawn from 5,200 repositories, which the authors describe as the largest verified SWE dataset to date. The funnel is steep. The team began with roughly 23,000 repositories and 6 million merged pull requests, used an LLM-as-a-judge to filter for quality based on diffs, descriptions and merge messages, and narrowed toward about a million candidate PRs before the agentic construction stage produced the final 100,000 instances. To control compute, the pipeline builds at most ten full environments per repository and reuses the "nearest" environment for other PRs—yielding, on average, 19 test instances per repository.

## Why the result matters

To prove the data was good for training and not just for benchmarking, the researchers distilled 71,498 high-quality solution trajectories from a 25,000-instance subset using DeepSeek-V3.2, then fine-tuned Qwen3-30B-A3B-Instruct on them. The resulting Scale-SWE-Agent reached a 64% resolve rate on SWE-bench Verified—up from the 22% the base Qwen model scored, a nearly three-fold improvement and what the authors call a substantial boost.

The size of the model is the point. Qwen3-30B-A3B is a mixture-of-experts model that activates only about 3 billion parameters per token—small enough to run on modest hardware and entirely open-weight. Getting that class of model to resolve roughly two-thirds of SWE-bench Verified, a suite of real, human-validated GitHub issues, would have been the province of frontier proprietary systems not long ago. (For context, engineered agent stacks built on top-tier proprietary and large open models have been reported in the 70s and higher on the same benchmark, but at a very different cost and openness profile.)

The implication for practitioners is concrete: if a 30B open model fine-tuned on synthetic-but-real trajectories can clear ~64%, then self-hostable, auditable coding agents become viable for teams that cannot or will not send their codebase to a frontier API.

## The data-synthesis trend ScaleSWE belongs to

ScaleSWE is not alone, and that is the broader signal. A cluster of 2026 work—papers with names like SWE-Universe, SWE-Next and others scaling "real-world verifiable environments"—has converged on the same insight: the scarce ingredient for coding agents is no longer model capacity but verified, executable training tasks with trustworthy tests. The frontier labs have largely solved scale by spending on compute and proprietary data. The open-research counter-move is to manufacture high-quality data automatically and let smaller models close the gap.

What distinguishes the ScaleSWE approach is its willingness to push the construction burden onto agents rather than rules. Earlier dataset efforts leaned on hand-crafted heuristics—predefined install commands, rigid filters—that break down as repository diversity grows. By letting an agent explore a codebase, fight through a dependency install, and write tests interactively, the pipeline trades determinism for reach, capturing the messy heterogeneity of real software that rule-based methods tend to discard.

There are caveats worth keeping in view. SWE-bench Verified is a single benchmark, and the community has spent the past year documenting how agent scaffolding, test-harness quirks and even contamination can inflate or distort scores; a 64% figure from one fine-tune is a strong signal, not a settled verdict. The pipeline also leans on large proprietary and open teacher models—DeepSeek and Gemini-class systems—to build its data, so "small model" describes the deployed agent, not the full cost of producing it. And synthetic trajectories distilled from a teacher inherit that teacher's blind spots.

## What to watch

The team has begun releasing pieces of its work—a portion of the dataset on Hugging Face and an accompanying agent framework—which means the central claims are increasingly checkable by outsiders rather than taken on faith. The questions that will decide ScaleSWE's significance are practical ones: Does the data hold up under independent evaluation and on benchmarks beyond SWE-bench? Do the fine-tuned small models generalize to real engineering tasks outside the test distribution, or do they overfit to the benchmark's shape? And can the pipeline extend cleanly beyond Python-heavy repositories into the polyglot reality of most production codebases?

If the answers trend positive, the takeaway is uncomfortable for anyone betting that capable coding agents require frontier-scale models behind a paywall. The raw material—decades of human pull requests—is public, and pipelines like ScaleSWE are getting very good at turning it into something a 30-billion-parameter open model can learn from.
