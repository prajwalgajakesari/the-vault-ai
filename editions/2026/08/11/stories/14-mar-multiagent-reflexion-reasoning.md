## When One Mind Isn't Enough: Teaching LLMs to Argue With Themselves

Ask a large language model to check its own work and something strange often happens. It looks back at a botched answer, nods approvingly, and confidently repeats the same mistake. This failure mode has a name in the research literature — "degeneration of thought" — and it has quietly undercut one of the more appealing ideas in AI: that a model can improve simply by reflecting on what it just did.

A new paper, "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs," argues the fix is not more reflection but more perspectives. Instead of a single model grading its own homework, MAR stages a structured debate among several agents wearing different personas, then feeds the resulting critiques back into the reasoning process. The authors report that the approach lifts performance on both question answering and code generation over the standard single-model reflection baseline.

## The Problem With Self-Critique

Reflexion, the technique MAR builds on, was one of the breakout ideas of the reasoning-model era. The recipe is simple: a model attempts a task, receives some feedback, writes a short verbal "reflection" on what went wrong, and tries again with that reflection in its context. No weights are updated. The learning, such as it is, happens entirely in language and memory.

The trouble is that a model reflecting on itself is a closed loop. If the model was confident and wrong the first time, it tends to be confident and wrong about its reflection too. The authors describe exactly this pathology: continual reflections of the same LLM onto itself lead to a degeneration of thought, in which the model keeps repeating the same errors rather than escaping them. Self-critique, it turns out, is only as good as the critic — and when the critic and the author are the same system, blind spots stay blind.

## How MAR Works

MAR's central move is to break the closed loop by introducing multiple agents assigned distinct personas, set up as debaters. Rather than asking one model "what did you get wrong?", the framework asks several differently-primed agents to interrogate a candidate answer from their own vantage points. The disagreement between them becomes the raw material for a richer reflection — one that a single self-referential pass would not have produced.

That debate output is then channeled back into the Reflexion-style loop. The model revises its answer not against its own tepid self-assessment but against a chorus of critiques that pull in different directions. The design borrows the intuition behind multi-agent debate — that adversarial diversity surfaces errors — and grafts it onto the memory-driven, iterative structure of reflection. The result is a hybrid: the persistence and self-improvement of Reflexion, with the error-catching power of agents that are not invested in the original answer.

Crucially, like Reflexion itself, this is an inference-time method. There is no fine-tuning, no reward model to train, no gradient updates. Everything happens in prompting and orchestration, which makes the approach cheap to bolt onto existing models — and easy for other researchers to reproduce or contest.

## What the Numbers Show

The authors evaluate MAR on two very different reasoning tasks. On HotpotQA, a multi-hop question-answering benchmark that requires stitching together facts from several documents, MAR reaches 47 percent exact match. On HumanEval, the widely used programming benchmark that scores whether generated code actually passes unit tests, it hits 82.7 percent. In both cases, the paper reports that MAR surpasses reflection driven by a single LLM.

Two benchmarks is a narrow slice, and the paper stops short of claiming a universal reasoning boost. But the pairing is deliberate: HotpotQA stresses factual retrieval and compositional reasoning, while HumanEval stresses precise, executable logic. Gains on both suggest the debate-driven reflection is doing something more general than exploiting the quirks of a single dataset.

## Why This Matters

The appeal of self-improving inference is obvious. If a model can get meaningfully better by thinking harder at test time — no retraining, no new data — then capability becomes something you can buy with compute rather than with another expensive training run. That is why Reflexion and its descendants have drawn so much attention.

MAR's contribution is a pointed diagnosis: naive self-reflection has a ceiling, and that ceiling is the model's own confidence in its mistakes. By outsourcing critique to a diverse panel of agents, the method reframes reasoning as a social process rather than a solitary one — closer to peer review than to introspection. It is a reminder that the same LLM asking itself "am I sure?" is a weak oracle, and that diversity of viewpoint, even simulated, can be a substitute for a genuinely external check.

## What to Watch Next

The open questions are the interesting ones. How many personas are enough, and does the benefit plateau or reverse as agents multiply? What is the token and latency cost of running a full debate for every answer, and is it worth it versus simply sampling more from one model? And does the gain hold on harder, longer-horizon tasks — agentic workflows, math olympiad problems, real software engineering — where a single wrong turn early can doom everything downstream? MAR makes a clean case that arguing beats agreeing when a model checks its own reasoning. The next step is finding out how far that argument scales.
