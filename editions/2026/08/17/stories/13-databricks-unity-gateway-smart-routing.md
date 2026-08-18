Databricks' own engineers were doing what most enterprise developers do in 2026: pointing every coding task at the most capable model on the menu without asking whether it needed one. On August 13 the company published its fix — a small, cheap classifier that reads a task description before any code is written, guesses how hard the job is, and picks the model accordingly. Against an internal benchmark Databricks says no model lab has seen, the router cut cost per task by 35%. Against public coding benchmarks, 56%.

The feature is Smart Routing, in beta inside Unity AI Gateway, Databricks' control plane for enterprise AI access and spend. It runs natively inside Claude Code and Codex, and extends across harnesses through Omnigent, the company's meta-harness.

"Against our own internal benchmark, which no labs have had access to, we saw 35% savings," wrote Ankit Mathur and five co-authors. "Against public coding benchmarks that demonstrate our results generalize, we achieved 56% cost savings." On internal workloads it outperformed any single model at 65% of the cost per task of a leading model like Opus 5; on public benchmarks it matched Opus 5 at less than half the cost.

## The classifier is deliberately small

The key choice is where the routing decision happens. Databricks rejected per-request routing because at scale costs are dominated by cache hit rate, and preserving that requires sending consecutive turns to the same model at the same effort level. Instead it uses task-aware routing: assess complexity once at the start of a session, then commit to a model and harness for the duration.

The classifier is not a trained neural router but a cheap, low-latency model prompted to extract semantic labels from the opening task description — what part of the system changes, what code evidence the prompt carries (a snippet, a traceback, or nothing), how it appears to be failing, how localized the fix looks. From those fields the router derives a task-type family and a language family, defaults to a medium-sized model, then escalates or delegates down — all on that opening information alone, with no tests, no answer key, nothing about the repository.

"Using a frontier model would tax every request (even the simple ones we want to save on), so the extractor is intentionally small and fast," the authors write. Notably, Databricks publishes no parameter count and no millisecond figure for the overhead the extractor adds — an omission worth pressing on, since the economics rest on the classifier costing near-nothing.

"Most of the win comes from using cheaper models for simpler tasks," the post concludes — less clever arbitrage than an admission the default was badly miscalibrated. Reviewing its own pre-routing traces, Databricks found many sessions spending frontier money on work that did not need it.

## Candid about what does not work

Databricks published its ceiling alongside its results. "A router with perfect foresight would beat every single model at a fraction of what ours spends," the authors write. They are equally blunt about benchmark validity: benchmark tasks arrive as self-contained statements of work; real sessions do not. "Opening prompts are rarely precise, since what a developer types first is a symptom or a rough intention rather than a specification, and our router reads that first message and commits."

The obvious remedy — re-route mid-session — collides with the cache economics that drove the design. "In today's world, with costs dominated by cache-hit-rate, switching mid-session is untenable at scale," they write, pointing to context compaction as the natural seam, the approach Cognition uses in Devin Fusion. Databricks is deploying first where task scoping is free: PR reviews, sub-agent launches, batch migrations and scheduled jobs — cases where a machine wrote the task statement.

The field is crowded. RouteLLM, the UC Berkeley and LMSYS framework trained on Chatbot Arena preference data, reported over 85% cost reduction on MT-Bench while retaining 95% of GPT-4's performance, routing only 14% of queries to the strong model. NVIDIA open-sourced NeMo Switchyard on August 11, claiming costs down to roughly a third of an Opus-only baseline. Jason Andersen, VP and principal analyst at Moor Insights & Strategy, cautioned that such figures "represent vendor-specific use cases rather than universal baselines." Routing is no free lunch either: "Model routing is not plug-and-play. Like a network router, getting the best outcomes requires skilled operators and careful configuration," he wrote. "Get those wrong, and the router becomes overhead rather than optimization."

## Why It Matters

A control plane is forming above the models with four load-bearing parts: routing, harnesses, caching and observability. Databricks now ships all four — Smart Routing picks the model, Omnigent picks the harness, cache-hit-rate discipline shapes both, and session traces land in Unity Catalog under enterprise access policies.

The immediate effect is commoditizing. If a classifier can pick among the 33 models released this year and beat any of them individually on cost-adjusted quality, then no single frontier model is the product — the portfolio is. That is Andersen's read too: for closed-model vendors, routing means "one more reason for customers to build supplier diversity into their AI strategy," strengthening open-weight models by making substitution cheap.

But the layer doing the commoditizing is itself sticky, and arguably stickier than any model. Switching models is an API change. Switching control planes means re-plumbing routing policy, spend gates, harness orchestration and — critically — the trace archive that governs and evaluates everything. Stripe's reported $7 billion agreement to acquire OpenRouter prices that position bluntly: the switchboard is worth more than most of what it switches between. Databricks, NVIDIA, AWS Bedrock and Microsoft Foundry are building toward the same seat.

## What to Watch

Whether Databricks publishes the classifier's latency and cost overhead, and whether independent teams reproduce the 35% and 56% figures on workloads it did not select. Whether mid-session re-routing ships, and whether cache-miss pricing becomes an explicit router input. Whether design partners report the same savings without quality regressions their developers notice. And the competitive response: the labs that benefit least from commoditization control the harnesses these routers plug into, and have every incentive to make third-party routing harder.
