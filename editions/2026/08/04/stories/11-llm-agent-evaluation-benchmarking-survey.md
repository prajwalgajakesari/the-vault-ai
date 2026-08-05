# As AI Agents Proliferate, a Sweeping Survey Maps How We Actually Evaluate Them

The AI industry spent 2025 and 2026 racing to ship autonomous agents — software that reasons, plans, calls tools, remembers what it did an hour ago, and increasingly acts on a company's behalf without a human watching each step. What the industry did not do, at anything like the same pace, was figure out how to tell whether those agents actually work. A comprehensive survey from researchers at SAP Labs argues that this gap is now the field's central liability, and it offers the most complete map yet of a fractured evaluation landscape.

The paper, "Evaluation and Benchmarking of LLM Agents: A Survey" (arXiv:2507.21504), was written by Mahmoud Mohammadi, Yipeng Li, Jane Lo, and Wendy Yip, and published at the ACM SIGKDD Conference on Knowledge Discovery and Data Mining. Its diagnosis is blunt.

> "The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area."

## A two-dimensional map for a fragmented field

The survey's core contribution is a taxonomy that splits agent evaluation into two questions: *what* to evaluate and *how* to evaluate it.

On the "what" axis, the authors identify four objectives. **Agent behavior** treats the system as a black box and asks whether it finished the task — measured through success rates, Pass@k, output quality, latency, and cost. **Agent capabilities** open the box to probe the competencies underneath: planning and reasoning (scored with metrics like Node F1 and Edge F1 over the agent's action graph), memory and context retention, tool-use accuracy including correct parameter generation, and multi-agent collaboration. **Reliability** asks whether the agent does the same thing twice, using consistency metrics such as pass^k that run identical tasks repeatedly to watch outcomes drift. **Safety and alignment** covers harm and toxicity detection through red-teaming, fairness, and adherence to domain policies.

On the "how" axis, the survey catalogs interaction modes (static offline datasets versus dynamic, simulated, or human-in-the-loop environments) and three families of metric computation: deterministic code-based checks, the increasingly dominant "LLM-as-a-Judge" (and its newer "Agent-as-a-Judge" variant), and human evaluation through expert audits or crowdworkers.

## The benchmarks — and where they fall short

The survey grounds its taxonomy in the real benchmarks practitioners rely on. For interactive web tasks it points to **WebArena**, **VisualWebArena**, **BrowserGym**, and **AppWorld**. For tool use and API orchestration, it cites **ToolBench** and **API-Bank**. For code, **SWE-bench**'s GitHub-issue resolution. For hard multi-step reasoning, **GAIA**, whose questions are simple for humans but demand complex tool chains from agents. For safety, **AgentHarm**. On the tooling side it names emerging evaluation frameworks such as OpenAI Evals and DeepEval, alongside development platforms like Azure AI Foundry.

But the authors' sharpest point is what these benchmarks miss. Most test short, isolated, self-contained tasks. Real deployments do not look like that — and the absence of standardized metrics across objectives makes it nearly impossible to compare two agents fairly or track genuine progress.

## Why enterprise deployment is the real stress test

The paper's industrial origin shapes its most distinctive section: a list of enterprise realities that academic benchmarks routinely abstract away.

> "We highlight enterprise-specific challenges, such as role-based access to data, the need for reliability guarantees, dynamic and long-horizon interactions, and compliance, which are often overlooked in current research."

Each is a concrete failure mode. **Role-based access control** means an agent's permitted actions depend entirely on who is asking — an agent acting for a CEO should not have the same reach as one acting for a junior analyst, and testing whether it merely *can* open a file misses whether it *should*. **Reliability guarantees** raise the bar well past a leaderboard score: a 90% success rate is worthless if the 10% of failures are random and catastrophic, because enterprises need behavior that is predictable and auditable, not merely usually correct. **Long-horizon interactions** expose performance drift and memory degradation over workflows that unfold across days, not seconds. And **compliance** demands adherence to regimes like GDPR or HIPAA, which calls for domain-specific test cases and, the authors suggest, formal verification methods rather than spot checks.

## Analysis: evaluation is the adoption bottleneck

This is the reason the survey matters beyond academia. The barrier to putting agents into production is no longer raw capability — frontier models can already plan and use tools impressively. The barrier is trust, and trust is an evaluation problem. A company cannot deploy an agent into a billing system, a patient record, or a procurement workflow on the strength of a benchmark that tested three-minute browsing tasks. The stochastic nature of language models makes this doubly hard: the same prompt can yield different behavior, so proving reliability requires running tasks many times, which is expensive and rarely done. Until evaluation can certify consistency and policy adherence under realistic constraints, the gap between an impressive demo and a trustworthy deployment stays wide — and it is precisely in that gap that both stalled enterprise projects and real-world safety incidents live.

The survey frames a promising response in **evaluation-driven development** — folding assessment into the build cycle as continuous monitoring rather than a one-time gate before launch, much as test-driven development reshaped software engineering.

## What to watch

The authors call for evaluation that is more holistic, more realistic, and more scalable — benchmarks that bake in access controls, extended time horizons, and compliance checks rather than treating them as edge cases. The signal to watch through the rest of 2026 is whether the next wave of agent benchmarks moves toward those enterprise-grade conditions, and whether "Agent-as-a-Judge" automated evaluation can scale trust as fast as agents themselves are scaling. If evaluation keeps lagging deployment, the mismatch the SAP Labs team documents will not stay a research footnote. It will show up in production.
