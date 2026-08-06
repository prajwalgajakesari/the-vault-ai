---
headline: "MAS-Orchestra Trains Multi-Agent Systems With Function-Calling RL and Debuts MASBENCH"
slug: "mas-orchestra-multiagent-rl"
category: "research"
story_number: 11
edition: "2026-08-05"
---

# MAS-Orchestra Trains Multi-Agent Systems With Function-Calling RL and Debuts MASBENCH

For two years, the pitch for multi-agent systems has been intuitive to the point of seeming obvious: if one language model is smart, a team of them, each handling a slice of the work, should be smarter. The reality has been messier. Hand-built agent crews frequently cost more, run slower, and answer no better than a single well-prompted model. A new paper from Salesforce AI Research argues the problem is not the idea but the plumbing, and proposes to fix it by teaching a model to design the whole team at once.

The paper, "MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks," was accepted to ICML 2026 and is authored by Zixuan Ke, Yifei Ming, Austin Xu, Ryan Chin, Xuan-Phi Nguyen, Prathyusha Jwalapuram, Semih Yavuz, Caiming Xiong and Shafiq Joty. Alongside the method, the team released MASBENCH, a controlled benchmark built to answer a question the field has mostly hand-waved past: when does a multi-agent system actually beat a single agent?

## The trouble with wiring agents by hand

The authors are blunt about why automatic multi-agent design has underdelivered. As they write in the abstract, the shortcomings "stem from two key factors: (1) methodological complexity — agent orchestration is performed using sequential, code-level execution that limits global system-level holistic reasoning and scales poorly with agent complexity — and (2) efficacy uncertainty — MAS are deployed without understanding if there are tangible benefits compared to single-agent systems."

In plain terms: most orchestration frameworks build an agent system the way a script runs, one line at a time. The orchestrator decides the next step, sees what happens, then decides the step after that. That keeps the model reasoning locally, never stepping back to reason about the shape of the whole system. And because nobody agreed on how to measure the payoff, teams shipped elaborate agent pipelines on faith.

## Orchestration as a function call

MAS-Orchestra's central move is to reframe the job. Instead of executing agents step by step, the orchestrator is trained to emit an entire multi-agent system in one shot, treating each specialist sub-agent — a chain-of-thought solver, a self-consistency voter, a debate agent, a web-search agent — as a callable function with a defined interface. The orchestrator reasons over which functions to compose, how many to run, and how to combine their outputs, without getting tangled in each one's internal execution.

That abstraction turns MAS design into a function-calling problem, and function calling is something models can be trained to do well with reinforcement learning. The team optimizes a 7-billion-parameter Qwen2.5 orchestrator with GRPO, rewarding it for producing systems that reach correct final answers efficiently. Because sub-agents are hidden behind clean interfaces, the approach scales as agents get more complex, the exact failure mode of code-level orchestration.

The learned behavior is telling. On easy math (AIME24), the orchestrator quickly learns to stop overcomplicating: after roughly 20 training steps it delegates 100 percent of the work to a single strong sub-agent. On hard search tasks (BrowseComp+), it spins up several agents and fires three to four parallel searches per question. The system, in other words, learns when a crowd helps and when it just adds cost.

## MASBENCH, and the honest scoreboard

MASBENCH is the paper's diagnostic contribution. It characterizes tasks along five structural axes — Depth (longest dependency chain), Horizon (number of required intermediate sub-tasks), Breadth (maximum dependencies of any sub-task), Parallel (independent components), and Robustness (sub-tasks under adversarial attack) — with values spanning 2 to 12. The takeaway is deflating for multi-agent maximalists: gains "depend critically on task structure, verification protocols, and the capabilities of both orchestrator and subagents, rather than holding universally."

Where the structure rewards coordination, though, the method delivers. MAS-Orchestra reports besting GPT-5 and Claude-Sonnet-4.5 by up to 23 percent across five benchmarks while running more than 10 times more efficiently. In the paper's table, its 7B orchestrator posts 66.25 on AIME24 and 61.25 on AIME25 against GPT-5's 55.00 and 47.72, and reaches 49.00 on HotpotQA and 11.00 on the notoriously hard BrowseComp+.

## Why coordination is the field's live wire

Multi-agent coordination is having a moment because single-model scaling is getting expensive and orchestration promises a cheaper axis of improvement. MAS-Orchestra lands amid a burst of related work — Salesforce's own IlluMAS warning that agent crews often fail to beat single agents, plus reward-modeling and stability efforts like OrchRM and Dr. MAS. The common thread is a shift from "more agents" to "trained, measured agents."

What to watch: whether a small trained orchestrator conducting frontier models becomes the default pattern, and whether MASBENCH's five axes get adopted as the yardstick that finally makes multi-agent claims falsifiable. If both hold, the next year of agent research may look less like architecture astronomy and more like engineering.
