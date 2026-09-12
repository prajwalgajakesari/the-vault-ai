# Asked to Improve Their Own Scaffolding, Models Got It Right Half the Time

Give a frontier model the code it runs inside, show it where that code is failing, and ask it to make things better. Then check whether the fix holds on tasks it never saw. A benchmark released September 1 by ByteDance Seed and four collaborators answers with uncomfortable precision: across 64 attempted revisions, the visible improvement and the held-out improvement pointed the same way just 34 times. That is 53.1 percent, a coin flip dressed as engineering.

The benchmark is called **HarnessDev**, and its central move is to change what gets graded. Every agent evaluation in wide use, from SWE-bench to BrowseComp, fixes a harness and scores the model's answers. HarnessDev fixes the model and scores the harness.

An *agent harness* is the software wrapped around a model that turns text generation into action: the execution loop, tool definitions, context management, persistent state, retry logic, and the verifier that decides when a task is done. Unglamorous plumbing that matters enormously. The paper opens with the cleanest illustration available: on Terminal-Bench 2.1, GPT-5 with identical weights solves 35.2 percent of tasks inside Terminus 2 and 49.6 percent inside Codex CLI. Same model, fourteen points, all of it scaffolding.

## What the benchmark actually does

HarnessDev, from ByteDance Seed with SUTD, Georgia Tech, M-A-P and TokenWave.AI, splits the problem in two.

In **Creation**, every model gets the same deliberately crippled starting point: a seed harness with file, search and process primitives, a results writer, and nothing else. No agent loop, no planner, no verifier, no retry logic, no stopping rule. Run unmodified it scores zero everywhere, so any nonzero result must come from control logic the model wrote itself. Six models were tested — Opus 4.8, GPT-5.5, Gemini 3.1 Pro, DeepSeek V4 Pro, Qwen 3.7 Max and Seed 2.0 Pro — across four domains and five benchmarks totalling 2,207 instances.

In **Evolution**, the model starts from its own frozen creation and revises it using real execution feedback: a fixed 100-task SWE-bench Pro set and all 89 Terminal-Bench tasks, on a budget of ten full evaluation pairs. Every version it declares is *also* scored afterward on 630 SWE-Pro instances the model never sees. That separation produces the headline number.

The authors are blunt about why this is not ordinary code editing. When a model modifies a standalone program, they write, the target behavior is externally specified and success is locally verifiable. But when a model modifies its own harness, it is editing the execution substrate through which it acts: the change alters how the model itself observes, plans, and recovers in all future tasks.

## The scores

Models can build working harnesses, just not competitive ones, and not evenly. Under Self-Eval, where each harness runs on the model that wrote it, Opus 4.8 posted the best average at **67.8** against a human-engineered reference of **86.2**. On writing, Opus edged the reference, 84.6 to 83.7. On machine-learning experimentation, Opus (32.9) and Gemini (32.4) beat the 24.0 MLE-bench reference outright. On code, Opus hit 69.3 on SWE-Pro against 80.0. On search, a chasm: the best BrowseComp score was 52.6, against 92.2.

Harnesses also turned out to be quietly overfitted to their authors. Swapping the executor to a fixed Gemini 3.1 Pro dropped Opus's SWE-Pro score from 69.3 to 33.0, partly because one harness had hard-coded a 120-step limit tuned to its original executor. And much of the generated machinery never runs: of 108 code components across 18 harnesses, 18 never fired, all of them state or memory code. Eleven harnesses defined a State class, yet across 26,679 trajectories not one checkpoint event occurred.

## Why this matters

2026 has been the year self-improving agents moved from thought experiment to product roadmap. That pitch rests on one assumption HarnessDev puts under a microscope: that a model shown its own execution traces extracts a durable lesson rather than a local patch.

The evidence is mixed in a diagnosable way. All five self-runtime lineages *did* improve on held-out tasks, by +1.43 to +4.44 points (mean +3.11), real gains. But the process producing them looks less like engineering than drift. Of the 64 version switches, 8 regressed on both benchmarks, 16 on one, 27 moved only within the noise band (a single commit can swing ±4.75 points), and just 2 showed clear positive evidence. Only 2 of 9 declared final versions were actually best on held-out tasks. The models largely could not tell which of their own changes were the good ones.

Pin the runtime model and it darkens. In four lineages run with Gemini as executor throughout, only Opus improved (+2.70); GPT-5.5 regressed 10.32 points. A harness improvement is not a property of the harness. It is a property of the harness-plus-executor pair, precisely the thing a platform vendor cannot hold fixed.

Diagnosis was the weakest link: the dedicated trajectory-inspection interface, built for reading failure traces, was called **twice** across the entire study. The one unambiguous win came when Opus 4.8 noticed that 99 of 100 runs reported success while only 48 actually passed, traced it to premature completion, and added a completion gate. That is exactly the behavior the field is betting on. It happened once.

The authors' own summary is measured: models can make useful local improvements, while robust evolution across unseen tasks and runtime models remains an open challenge. The project page is blunter — the goal is not constant change, it is knowing which changes to keep.

## What to watch

Whether the Evolution track, currently code-only, expands into search and browsing, where the reference gap is widest and self-improvement claims loudest. Whether anyone reports a workable held-out selection rule: visible feedback is fine for local search and unreliable for picking a final version, which argues for versioning and rollback over autonomous promotion. And whether the labs shipping agent platforms start publishing cross-executor numbers. If a harness tuned by one model collapses under another, the portable-scaffolding story underwriting much of the agent tooling market needs an asterisk — and right now the only people measuring it built the benchmark.
