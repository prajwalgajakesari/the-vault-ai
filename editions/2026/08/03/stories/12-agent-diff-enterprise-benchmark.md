# 'Agent-Diff' Benchmark Tests Whether AI Agents Can Really Handle Enterprise APIs

Ask an AI agent to book a meeting, tag a file, or close a ticket, and it will usually tell you it did the job. A new benchmark from Minerva University argues that the only way to know whether it actually did is to go look at the software afterward and check what changed.

That is the premise of **Agent-Diff**, a benchmarking framework released this month that evaluates nine large language models across **224 tasks** spanning four real enterprise services: Slack, Box, Linear and Google Calendar. Instead of grading an agent on the text of its final answer or on whether it called the "right" API in the "right" order, Agent-Diff snapshots the entire state of the underlying system before and after the agent runs, then compares the two. Success is defined by whether the world actually changed the way it was supposed to.

"Rather than fuzzy trace or parameter matching, we compute the state difference between sandbox snapshots... and define task success by whether the expected change in environment state was achieved," the authors write. The approach, they add, lets them "enforce invariants and detect unintended side effects (e.g., modifications or deletions of unrelated resources)" — a way of catching an agent that completes its task but quietly deletes something it should have left alone.

The paper (arXiv 2602.11224), authored by Hubert M. Pysklo, Artem Zhuravel and Patrick D. Watson, is slated for presentation at KDD '26. It lands squarely inside a growing wave of agentic benchmarks — Terminal-Bench, SWE-Bench Pro and others — built to expose how brittle AI agents remain the moment they leave chat and start touching real systems.

## How state-diff evaluation works

Agent-Diff's core innovation is what the authors call a "state-diff contract." Each of the four services runs as a fully isolated, containerized replica that, from the agent's point of view, is "indistinguishable from real upstream APIs in terms of latency, headers, and error schemas." All network traffic is intercepted and routed to these local replicas, so runs are reproducible without the temporal instability of hitting a live production API.

Every service is backed by a relational database with typed entities — Users, Channels and Messages in Slack; Files and Folders in Box. Before the agent acts, Agent-Diff snapshots all entity tables; after it finishes, it snapshots them again and computes the difference. Human-authored assertions then check that specific entities were created, updated or deleted the right number of times, and that nothing else moved.

The task suite spans 108 unique API endpoints (Box: 27, Slack: 25, Linear: 19, Calendar: 37) and is deliberately gnarly. By the authors' accounting, **66% of tasks** hide the information the agent needs, forcing it to discover identifiers through API queries rather than receiving them in the prompt, and **53%** require coordinated changes across multiple entities. One Calendar task asks the agent to create a new shared calendar, grant a colleague write access, schedule an event around a third person's free/busy availability, update a location and delete a cancelled event — seven distinct endpoint calls under an optimal policy. Every model executes through the same standardized Bash-and-Python scripting layer, so comparisons are apples-to-apples.

## The results

Agent-Diff reports two numbers per model: an assertion-weighted score that awards partial credit, and a stricter full-task pass rate. The gap between them is the story.

DeepSeek-V3.2 topped the board with an **88.1** overall assertion-weighted score, yet fully completed only **76%** of tasks. Devstral-2512 followed at 86.0 (74% pass), with Qwen3-VL-235B, Kimi-K2 and Grok-4.1-fast clustered in the mid-70s. Gemini-3-Flash scored 73.8, GPT-OSS-120B 68.5, and the smaller frontier-lab models trailed: Claude Haiku 4.5 landed at 49.3 (50% pass) and Llama-4-Scout at the bottom, scoring as low as 20.9 on Linear.

In other words, even the strongest agent botched roughly one enterprise task in four — and the models tested were largely the efficiency-tier releases (Flash, Haiku, Fast, Scout, OSS) rather than flagship reasoners. Scores also swung sharply by service, with several models cratering on Box's nested-permission hierarchies and Linear's issue-dependency state machines.

## Why It Matters

Enterprises are being sold on agents that book, file, message and update on their behalf. But most benchmarks grade agents on their final text output — a setup that rewards a confident summary over a correct action. An agent can narrate a flawless account of scheduling a meeting while creating the event on the wrong calendar, inviting the wrong person, or silently overwriting an existing entry. Final-answer scoring never sees the difference.

State-diff evaluation is a direct answer to that blind spot. By measuring the actual delta in system state — and flagging unintended side effects — Agent-Diff shifts the question from "did the agent say the right thing?" to "is the system now in the right state?" That is precisely the question that matters when an agent has write access to a company's calendars, files and project trackers. The partial-credit-versus-pass-rate gap also quantifies a reliability tax: agents that look competent on average can still fail to fully complete a meaningful share of real workflows, which is the difference between a helpful assistant and an unsupervised liability.

## What to Watch

Three things are worth tracking. First, whether flagship reasoning models — the paper largely benchmarks efficiency-tier releases — close the pass-rate gap when run against the same suite. Second, whether state-diff evaluation gets adopted or extended by other groups; the authors have released code and data, and the method generalizes to any API-backed system with a snapshottable state. Third, whether "no harmful side effects" becomes a standard reliability metric for enterprise agents, alongside raw task completion. As agents move from demos to production, the benchmark that checks what actually changed may prove more consequential than the one that checks what the agent claimed.
