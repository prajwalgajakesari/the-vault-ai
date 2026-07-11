NVIDIA has spent a decade selling the shovels of the AI gold rush. This week it made a pointed case that it can also sell the gold — and give it away.

On July 8, the company published benchmark results showing that its open-weight Nemotron 3 Ultra model, paired with LangChain's Deep Agents harness, matched the best closed models on a suite of enterprise agent tasks while running at roughly one-tenth the inference cost. In LangChain's public agent evaluation, Nemotron 3 Ultra posted an aggregate score of 0.86 at a cost of $4.48 per run. The next best-performing model on the leaderboard, according to NVIDIA and LangChain, cost $43.48 to hit a comparable score — nearly a 10x gap for what NVIDIA frames as business-task parity.

For a company whose market power rests on GPUs, the framing is deliberate: the model, not just the silicon, is now part of the pitch. And the model is free to download.

## An open model built for agents that run for hours

Nemotron 3 Ultra is a mixture-of-experts model with 550 billion total parameters and 55 billion active per token, built on a hybrid Transformer-Mamba architecture and supporting a context window of up to 1 million tokens. NVIDIA positions it as a "frontier-reasoning and orchestration" model — tuned less for one-shot chat than for long-running agentic workflows: coding agents, deep research, multi-step planning, and the kind of high-volume orchestration pipelines that enterprises are only now beginning to deploy in production.

Crucially, NVIDIA shipped it as a genuinely open release rather than a weights-only drop. The company published four checkpoints — an NVFP4-quantized build, a BF16 post-trained instruct model, a BF16 base model, and a reward-model variant — alongside training data and recipes, all under the Linux Foundation's permissive OpenMDW-1.1 license, which allows commercial use. Enterprises can self-host and eliminate per-token costs entirely, or reach the model through hosted providers including Baseten, Crusoe Cloud, DeepInfra, Fireworks, Nebius and Together AI. On OpenRouter, paid access runs $0.50 per million input tokens and $2.20 per million output tokens, with a free tier also available.

On raw agent quality, the model holds up against the best open competitors. NVIDIA cites a 91% score on PinchBench Agent Productivity, matching Kimi K2.6 and edging out Qwen 3.5. NVIDIA also says Ultra achieves roughly 5x higher throughput than other open models in its class — the metric that turns an accurate model into a usable one for agents that fire thousands of tool calls per task.

## The trick was the harness, not retraining

The most striking claim in the announcement is what LangChain did *not* do. To reach closed-model parity, its engineers never retrained or fine-tuned Nemotron 3 Ultra. Instead, they ran the model against LangChain's public Deep Agents benchmark, studied the execution traces to find where it dropped points, and then re-engineered the environment around it — adjusting system prompts, tool descriptions and middleware.

"The way to build better agents is to keep improving the system around the model," said Harrison Chase, cofounder and CEO of LangChain. "Memory, tool use, evaluation and model behavior compound when teams can tune them together. Our work with NVIDIA shows that enterprises can get strong performance from an open stack while keeping control over the agent systems they are building."

That work shipped as NemoClaw for LangChain Deep Agents, an open reference blueprint that bundles the tuned harness with NVIDIA's OpenShell secure runtime for executing agent actions. The pitch to enterprises is ownership end to end: an open model, an open harness and an open runtime, all runnable on a company's own infrastructure and governance. LangChain, whose agent-engineering platform NVIDIA says draws more than 200 million monthly downloads, is publishing the tuned Nemotron profile directly. NVIDIA named Abridge, Amdocs and Box as early adopters embedding specialized agents into their platforms, with consultancy EY building implementation practices around the blueprints.

## Why It Matters

For most of the AI boom, the competitive logic was tidy: closed labs like OpenAI and Anthropic built the best models, and everyone rented NVIDIA's GPUs to run them. Nemotron 3 Ultra complicates that. NVIDIA is now competing on the model layer itself — and doing so with an open-weight release designed to undercut the closed incumbents on cost for exactly the agentic workloads that are supposed to drive the next wave of enterprise spending.

The strategic reasoning is not subtle. NVIDIA does not need to win the model business to profit; it needs the total volume of AI compute to grow. Cheap, open, high-throughput models that enterprises deploy at scale sell more GPUs, whoever's logo is on the weights. The move also rides a broader current: at ICML 2026 the same week, NVIDIA landed 74 accepted papers, and the conference's paper distribution reflected a decisive academic tilt toward open frontier models as the default foundation for research. When the tooling, the research and the cheapest capable models are all open, the pressure lands squarely on labs guarding proprietary systems.

## What to Watch

The headline number — 10x cheaper at parity — comes from LangChain and NVIDIA's own evaluation on LangChain's benchmark, so independent replication on third-party agent suites will be the real test of whether the cost advantage holds outside a harness tuned specifically for this model. Watch, too, for how OpenAI, Anthropic and Google respond on price for agent workloads, and whether the "tune the harness, not the model" playbook generalizes to other open weights. If it does, the durable moat in enterprise AI may shift from who trains the best model to who engineers the best system around a good-enough open one — a contest NVIDIA is now positioned to win from both ends.
