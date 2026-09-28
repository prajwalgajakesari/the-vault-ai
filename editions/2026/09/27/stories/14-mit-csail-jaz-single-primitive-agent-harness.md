# MIT CSAIL's JAZ Rebuilds the Agent Harness Around a Single LLM Primitive and Beats Letta at Less Than Half the Cost

The agent industry has spent two years bolting things onto the agent loop: memory stores, vector search, reflection pipelines, playbook curators. A new paper from MIT CSAIL argues most of that scaffolding may be unnecessary. Its framework, JAZ, strips the harness down to one LLM-backed function call, and on two demanding benchmarks the stripped-down version beats purpose-built memory and self-improvement systems while spending less money.

The paper, "Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity," was posted to arXiv on September 22. Its ten authors are Zhening Li, Joshua Liu, Mateja Vukelic, Nicole Shen, Supriya Lall, Amitayush Thakur, Alex Zhang, Omar Khattab, Jonathan Light and Armando Solar-Lezama, most listed with MIT CSAIL affiliations. The list matters: Zhang and Khattab are behind recursive language models (RLMs), the 2025 work showing that a code-running agent with recursive subagents could outperform plain LLMs on long-context tasks. JAZ explicitly positions itself as a generalization of both CodeAct and RLMs.

## One Primitive, Two Properties

At the center of JAZ is a single primitive called *invoke*. The authors describe it as "a function whose implementation is provided at runtime by an LLM every time it is called." In practice, an agent runs as a Python REPL session. It writes code, and that code can call *invoke* again, spawning subagents through ordinary program control flow. Recursion, in the authors' words, is not an add-on: "like RLMs, recursive subagents are the default."

The second design property is subtler and, according to the paper, the one that does most of the work. Everything the model can see, including its own user prompt and its full interaction history, is exposed as a variable inside the REPL. Existing CodeAct and RLM implementations let users pass data and tools into the environment, but JAZ additionally makes the prompt and the transcript first-class objects the agent can search, slice and hand off by reference.

Around that core, JAZ provides composable hooks rather than built-in subsystems: iteration and recursion limits, a shared cost budget and a context-window warning. Memory and self-improvement are not features of the framework. They are behaviors the agent writes for itself in code, prompted to do so.

## The Numbers

The long-horizon test was StuLife, a benchmark of 1,284 ordered tasks simulating a college semester, of which 939 are graded and 207 require "far recall" of information delivered more than 50 tasks earlier. A typical episode runs 7,000 to 8,000 environment interactions. Every method used GPT-5.4 nano. On the far-recall subset, JAZ *invoke* posted a 69.9% pass rate against 61.8% for Letta Agent, the latest version of MemGPT, and 32.0% for a JAZ-hosted CodeAct-with-subagents baseline. JAZ's run cost $18.30 against Letta's $42.10, which is less than half. Across all graded tasks, JAZ scored 72.6% to Letta's 70.9%.

The authors trace the gap to a single exam question, task 1,282, which required recalling a lecture delivered 497 tasks earlier. In one run, JAZ reached it at recursion depth 70 after 69 tail-recursive handoffs, searched its accumulated history for the protocol names in one turn and answered correctly. Letta's conversation search, which blends keyword and vector retrieval, surfaced near-miss protocols instead. "Domain-specific harnesses encode assumptions that make them work well in many situations, but they become rigid in environments that break those assumptions," the authors write.

On AppWorld's test-challenge split, JAZ tested continual self-improvement. A top-level GPT-5.4 agent dispatched tasks to GPT-5.4 nano subagents in batches, read their histories and rewrote their prompts and skills between batches. It reached 74.2%, ahead of ACE (Agentic Context Engineering), a dedicated self-improvement harness, at 69.9%, and CodeAct with subagents at 71.1%. Reported total cost was $10.90 for JAZ against $13.50 for ACE, even though the researchers restricted ACE's learning to the first 10% of tasks because its reflector and curator cost ten times more per task than JAZ.

## Why It Matters

The prevailing assumption in agent engineering is that capabilities like long-term memory and learning from experience require dedicated infrastructure: databases, retrieval tools, fixed reflection loops. JAZ is evidence that, with a sufficiently expressive loop, a model can build those capabilities on the fly and tailor them to the task in front of it. The authors frame the result as proof that "prompting a minimal agent loop is sufficient to elicit long-horizon and self-improvement capabilities."

For builders, the cost result may be the headline. Specialized harnesses impose fixed workflows, such as reflection after every task or retrieval through a single search tool, and those workflows cost tokens whether or not they help. JAZ's meta-agent chose its own batch sizes and read subagent trajectories only when needed. That flexibility is where the savings came from.

The team also went further than most on reproducibility. The companion jaz-evals repository ships configs for all ten experimental arms, pins the framework to version 0.2.0a4 on PyPI and discloses that its StuLife fork repairs task data for 132 of 1,284 tasks, applied identically to every arm. The README is candid that the published runs came from development checkouts and that the pinned release is the closest installable version rather than the literal one.

## What to Watch

The caveats are real. Both benchmarks were run on a single model family, the AppWorld margin of about four points sits within a few standard errors, and the StuLife numbers come from a modified fork, so they cannot be compared directly with other published StuLife results. Whether *invoke* holds up with open-weight models, or with smaller models that write less reliable code, is untested.

The bigger question is whether harness vendors respond by getting thinner. If JAZ's thesis holds up under independent replication, the valuable layer shifts from memory products and reflection pipelines toward language-level primitives, budget hooks and observability. Expect the RLM community to test that quickly, and watch whether frameworks like Letta add history-as-variable access of their own.
