# NVIDIA Open-Sources NOOA, a Radically Simple Agent Framework Scoring 82% on SWE-bench

NVIDIA Labs on August 9, 2026 open-sourced NOOA, an agent framework built on a single, almost defiant idea: an AI agent is just a Python class. No graphs, no chains, no sprawling orchestration DSL. Methods are the actions the agent can take, fields are its state, docstrings are its prompts, and type annotations are contracts the runtime enforces. Released under Apache 2.0 and installable today with `pip install nooa`, the alpha (v0.0.8) arrives with benchmark numbers that are hard to ignore: 82.2% on SWE-bench Verified, 86.8% on CyberGym L1, and 85.1% mean RHAE on ARC-AGI-3.

The name is a backronym for NVIDIA-labs Object-Oriented Agents, and the framework leans all the way into that object-oriented framing. Where most agent stacks ask developers to wire tools, memory, and control flow into external structures, NOOA folds all of it back into ordinary Python.

## What Makes the Design Novel

The clever pivot is how NOOA decides what runs deterministically and what runs on a model. A method with a normal body executes as plain Python — fast, predictable, testable. But a method whose body is just an ellipsis (`...`) becomes an "agentic method": at runtime the harness fills in that body with an LLM-driven loop, using the method's signature, type hints, and docstring as the prompt and contract. The type annotations are not decoration; the runtime validates against them and retries on failure.

That single distinction lets a developer mix hand-written logic and model-generated behavior inside one class without leaving the language. NOOA ships execution strategies for the agentic methods, including a PredictStrategy (a single typed LLM call with a local retry loop when validation fails) and a CodeActStrategy (an iterative Python REPL where the model repeatedly calls `execute_python(...)`). Because everything is a class, agents are straightforward to unit-test, trace, subclass, and audit — properties NVIDIA explicitly pitches as governance wins.

Crucially, NOOA is model-agnostic. It routes through LiteLLM, so the same agent class can run on GPT-5.5, NVIDIA's own models, or anything else LiteLLM supports. NVIDIA is not selling a model here so much as a harness.

## The Benchmark Numbers

The headline figure — 82.2% on SWE-bench Verified — was achieved with GPT-5.5 at "xhigh" reasoning effort. Just as notable as the score is the efficiency claim: NVIDIA says NOOA reaches it using roughly 1.1 million tokens per task, while competing harnesses burned about 2.2 million tokens to land lower scores. On CyberGym L1, a security-focused benchmark, NOOA posted 86.8%, and on the reasoning-heavy ARC-AGI-3 it reported an 85.1% mean RHAE — all, per NVIDIA, at roughly half the token budget of the open harnesses it was compared against.

Efficiency at that scale matters commercially. If a simpler harness can match or beat heavier frameworks while halving token spend, the cost argument alone could move teams.

## The Containment Caveat

NOOA's own README carries a blunt security warning that deserves to travel with every one of those benchmark numbers: the framework's AST checks are not a containment boundary. Because agentic methods can execute model-generated Python — the CodeActStrategy is literally a REPL the model drives — running NOOA on untrusted tasks means running arbitrary code. NVIDIA's guidance is unambiguous: run it inside a container or a VM. The static analysis NOOA performs can catch some patterns, but it is a linting aid, not a sandbox. Teams that treat "82% on SWE-bench" as a green light to point NOOA at production repos without isolation are misreading the label.

This is v0.0.8 alpha software, supporting only Python 3.12 and 3.13, and the security posture reflects that maturity.

## Why It Matters

The agent-framework landscape has spent two years accreting complexity. LangChain, LangGraph, AutoGen, CrewAI and their peers introduced abstractions — chains, graphs, role hierarchies — that solved real problems but also became the thing developers spend their time fighting. NOOA is a bet in the opposite direction: that the abstraction developers already know, the class, is enough, and that the LLM belongs inside methods rather than around them.

For NVIDIA, the play is strategic rather than commercial in the narrow sense. By making NOOA model-agnostic and Apache-licensed, NVIDIA lowers the friction of building serious agents on any model while positioning its own tooling and hardware as the natural place to run them at scale. The release also lands alongside NVIDIA's broader open-security push, reinforcing a narrative of the company as an infrastructure and standards player, not just a chip vendor. If NOOA's "an agent is a class" idiom catches on, NVIDIA authored the idiom.

The efficiency story is the sharpest competitive edge. A framework that halves token consumption while topping a hard benchmark reframes the conversation from "which framework is most expressive" to "which framework is cheapest per solved task."

## What to Watch

Three things will decide whether NOOA is a landmark or a curiosity. First, reproducibility: independent replications of the 82.2% SWE-bench result, on models other than GPT-5.5, will show whether the harness or the model is doing the heavy lifting. Second, the security ergonomics — whether the community builds convenient, default sandboxing around NOOA, or whether the "run it in a VM" warning gets ignored in the rush. Third, adoption: alpha frameworks live or die by whether real projects subclass them. Watch the GitHub stars, sure, but watch the pull requests more.
