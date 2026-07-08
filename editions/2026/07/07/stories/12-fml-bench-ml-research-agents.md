When an AI agent claims it can "do research," the natural next question is: what kind? Most benchmarks that test autonomous machine-learning agents answer with an engineer's yardstick — squeeze another point of accuracy out of a Kaggle-style task, and do it cheaply. A benchmark called FML-bench argues that this misses the thing that actually makes research research: the messy, exploratory work of asking new questions rather than optimizing a fixed one.

Introduced in a paper on arXiv (2510.10472) from a team led by Qiran Zou and Hou Hei Lam, with collaborators spanning the National University of Singapore, Tsinghua University, the University of Minnesota, Weco, and Meta, FML-bench is pitched as a corrective to what its authors call an "engineering-oriented perspective" that "overlooks agents' research processes." The name is a nod to its focus: fundamental machine learning, not applied leaderboard-chasing.

## What the benchmark actually measures

FML-bench is built from eight diverse and fundamental ML research problems drawn from widely recognized academic repositories rather than invented from scratch. The design choices are deliberate. By anchoring tasks in real codebases, the benchmark reduces the coding overhead an agent must clear before it can do anything interesting, and it keeps the focus on general research questions instead of narrow, one-off use cases. The authors also emphasize that the suite is extensible — new tasks can be grafted on from real-world machine-learning GitHub repositories, so the benchmark is meant to grow rather than calcify.

Where FML-bench departs most sharply from its predecessors is in how it scores agents. Instead of collapsing everything into final performance and compute cost, it uses a five-dimensional evaluation framework spanning utility, diversity, academic contribution rate, cost, and step success rate. The headline addition is a metric the team calls Exploration Diversity, which quantifies the variance of an agent's proposals across iterations. In plain terms, it measures whether an agent keeps trying genuinely different ideas or just keeps polishing the same one. Complementary reliability measures — step success rate and step completion rate — track whether an agent can actually carry its own plans through to a working result.

That instrumentation is the point. A leaderboard tells you who won; FML-bench is trying to describe how they played.

## The finding: breadth beats depth

The most consequential result is also the cleanest. When the authors evaluated state-of-the-art research agents on the suite, agents employing broad exploration strategies exhibited higher exploration diversity and, critically, achieved superior performance. Exploration diversity, they report, positively correlated with performance improvements across multiple tasks. Put another way: generating a wider variety of ideas more reliably led to successful methods than repeatedly refining a single promising one.

That cuts against a common intuition in agent design, where iterative self-refinement — an agent grinding on one hypothesis until it works — is often treated as the sophisticated move. FML-bench's data suggests that once an agent clears a basic bar for depth, the marginal return shifts to breadth. The agents that behaved more like a curious lab, spinning up parallel lines of inquiry, outran the ones that behaved like a stubborn debugger.

The comparison is instructive because different agent frameworks embody different search philosophies. Some, in the mold of "The AI Scientist," fan out with parallel exploration for broad coverage; others, like tree-search-based systems, try to balance exploration against exploitation; still others follow a linear, refine-as-you-go loop. FML-bench gives those philosophies a common arena, and the arena rewards the explorers.

## Why it matters for the research-agent boom

FML-bench lands amid a rush of attempts to figure out what autonomous research agents can really do. AblationBench probes whether agents can design sound ablation studies; ResearcherBench and similar efforts test literature synthesis and reasoning; the broader field is stress-testing whether "AI scientists" produce novelty or just plausible-looking pastiche. The recurring worry is that agents excel at templated, narrow tasks and stall when asked to do open-ended, diverse science.

FML-bench's contribution is to make that worry measurable. By explicitly rewarding diversity and academic contribution rather than a single accuracy number, it creates pressure on builders to optimize for the behaviors that resemble real research, not just the outputs. Its authors frame the shift as moving evaluation "from performance to process" — a change in what we ask of agents as much as how we grade them.

There are caveats worth keeping in mind. Eight tasks is a focused set, and a benchmark that draws from public academic repositories inherits whatever quirks and contamination risks those repositories carry. Diversity metrics can be gamed by agents that generate superficially varied but shallow proposals. The authors' own extensibility pitch is an implicit acknowledgment that eight problems is a starting line, not a finish.

## What to watch next

The open code release (github.com/qrzou/FML-bench) makes the interesting experiments reproducible, so expect the community to probe whether "breadth beats depth" holds as tasks scale up and as new frontier models enter the loop. Watch, too, for whether exploration diversity becomes a design target that developers optimize directly — and whether that produces genuinely more creative agents or merely agents that have learned to look creative on the metric. The deeper test is still ahead: not whether an agent can explore broadly, but whether its broad exploration surfaces ideas a human researcher would call new.
