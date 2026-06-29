For more than fifty years, software has meant the same thing: a human decides what should happen, writes that logic into static code, and maintains it by hand as the world changes. A preprint posted to arXiv this month argues that the assumption underneath that entire enterprise is quietly collapsing — and that what is replacing it deserves a different name.

In "The End of Software Engineering: How AI Agents Are Fundamentally Restructuring the Software Paradigm," author Zhenfeng Cao of Lingxi Intelligent Investment makes an unusually sweeping claim for a research note. The rise of AI agents, he writes, is "not an incremental improvement but a fundamental restructuring of the software paradigm." The thesis is provocative precisely because it does not treat large language models as faster code-writers. It treats code itself as having been demoted.

## When Code Becomes Disposable

The paper's central move is to redefine what code is for. In traditional systems, code is "the carrier of decision logic" — the place where a human's reasoning lives. In an agentic system, Cao argues, the reasoning lives in the model, and code becomes a tool the model reaches for and throws away.

"When a large language model (LLM) can understand a task, decompose it into subtasks, dynamically generate code to execute those subtasks, and discard that code when it's no longer needed," he writes, "the role of code changes from the system itself to an ephemeral instrument of reasoning." Put more bluntly: "The code it generates is not the system; it is a transient artifact, produced and discarded as needed."

From that distinction, the paper builds a vocabulary. It formalizes traditional software as a tuple of computational resources, deterministic rules, and an execution environment — with the key property that the rules are static. Agentic systems get their own definition: an LLM reasoning engine, a set of tools, a memory subsystem, and a planning loop. The discipline that designs the latter, Cao argues, is not software engineering at all but something he calls "Agentic Engineering," in which humans become "intent architects," coordinators, and auditors rather than authors of logic.

The economic framing follows the same arc. Cao traces a line from licensed software ("Software 1.0," Microsoft and Oracle) to SaaS ("Software 2.0," Salesforce and AWS) to what he labels "Agent-as-a-Service," exemplified by OpenAI and Anthropic. Each transition, he argues, pushed complexity further away from the user. The endpoint is a model where, in his words, "software is not delivered; outcomes are delivered." Because an LLM's capacity scales with compute while human cognition stays fixed at O(1), he contends the shift "decouples solution capacity from human cognitive limits. This is not a 10% improvement; it is a qualitative change."

## The Gap Between the Demo and the Repo

What separates this paper from pure manifesto is that it cites the evidence against itself. Cao leans on a benchmark he calls EvoClaw, which measures agents not on isolated tasks but on sustained software evolution. The result is a cliff: "Overall performance scores drop significantly from >80% on isolated tasks to at most 38% in continuous settings, exposing agents' profound struggle with long-term maintenance and error propagation."

He names four culprits — context drift as codebases outgrow the model's window, cascading error propagation, indifference to technical debt, and what he calls verification fidelity, the risk that "agents can pass tests while introducing subtle semantic errors that only manifest under novel inputs." His own bottom line is hedged: agentic engineering "is real and transformative today as an augmentation paradigm, but will require several more years of concentrated research before fully autonomous software development becomes reliable in production settings."

That caveat lands squarely where skeptics live. The 38-percent ceiling echoes a wider body of 2025–2026 work. A survey of AI agentic programming notes that even SWE-bench Verified — whose pass rates climbed from below 10% to over 70% in a year — is restricted largely to Python and "function- or module-level" tasks, with no multi-turn feedback or build-pipeline management. Harder successors like SWE-Bench Pro were built precisely because the original stopped being a meaningful test. The unresolved question is whether the production gap is, as Cao insists, "not fundamental" — a matter of better memory and verification — or whether stochastic reasoning engines have a reliability floor that no amount of scaffolding crosses.

There are reasons to read the strongest claims warily. This is a single-author preprint from an investment firm, and several of its load-bearing citations — the EvoClaw figures, a LangChain pilot claiming a 93% reduction in root-cause time, an open-source agent with "over 179,000 GitHub stars" — are dated 2026 and difficult to verify independently. The argument is elegant; some of the scaffolding is unconfirmed.

## What to Watch

Cao closes with a four-stage roadmap running from today's tool-augmented copilots to "self-evolving agent ecosystems" projected for 2028 and beyond, and with a line built for citation: "The old software engineering is ending; the new one has already begun."

Whether that reads as prophecy or overreach depends on one number moving. If continuous-evolution benchmarks climb from the high-30s toward the rates agents already hit on isolated tasks, the paper's framing will look prescient. If that ceiling holds, "code as a transient artifact" will remain a compelling description of demos that production teams still cannot trust. The thesis is testable. The next year of benchmarks will start to grade it.
