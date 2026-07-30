When an AI agent decides to look up a user, pull their order, check the product catalog and then issue an exchange, it is quietly building a plan: a web of which step feeds which. A new interpretability paper argues that plan is not just implicit in the sequence of actions the agent takes — it is written down, in a readable form, inside the model's own activations, before the tools ever run.

In "Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams," posted to arXiv in May 2026, University of York researchers Tianda Sun and Dimitar Kazakov report that the dependency graph among an agent's tool calls — which call's output supplies an argument to which later call — can be recovered by a simple linear probe reading the frozen residual stream of a large model. In plain terms: the structure of an agent's plan is legible in its internal state.

"A low-capacity edge probe on the residual stream of Qwen3-32B decodes the tool-call dependency graph well above both a Hewitt–Liang random-label control and a positional baseline," the authors write in the paper's abstract. To their knowledge, they add, "this is the first structural probe of an LLM agent's runtime tool-call dependency graph."

## What the probe actually reads

The setup borrows a well-worn interpretability recipe and points it at a new target. Structural probes have previously recovered syntax trees from word embeddings and board states from game-playing networks; here the object of study is the directed acyclic graph (DAG) of tool-call dependencies produced when an agent interleaves reasoning with external function calls. An edge from call *i* to call *j* means call *i*'s output feeds an argument of call *j*.

Sun and Kazakov tap Qwen3-32B's residual stream at each tool-call boundary and train a logistic-regression "edge probe" to predict, for each pair of calls, whether a dependency edge exists. Working mostly on the τ-bench retail benchmark, they report the probe reaches an AUROC of 0.869 over 1,129 held-out call pairs (95% bootstrap confidence interval 0.801–0.930), drawn from 105 agent trajectories.

That number only means something against controls, and the paper leans hard on them. A Hewitt–Liang random-label permutation — the standard test for whether a probe is memorizing rather than reading real structure — averages 0.491, with no permutation out of 500 beating the real probe. More demandingly, a purely positional baseline built from five scalars like call index and distance already reaches 0.792, because plan structure correlates with ordering. Conditioned on that baseline, the residual stream still contributes an extra +0.0775 AUROC (CI +0.032 to +0.127). The signal emerges in mid-stack layers, climbing to 0.864 by layer 14 — roughly 22% of the way through the 64-layer network — and peaking at 0.875 around layer 41.

## Topology, not just labels

The more interesting claim is what the probe is reading. Is it tracking the abstract shape of the plan, or just the specific ID strings passing between calls? To separate the two, the authors run a counterfactual contrast. Swapping a single ID value in a tool's output — a "value corruption" that leaves the plan's shape intact — barely moves the decoded graph (Cohen's *d* = 0.06). Emptying a tool response, which forces the agent to genuinely re-plan, moves it a lot (*d* = 0.87). That dissociation, they argue, is the load-bearing evidence that the probe encodes topology rather than lexical content, and it replicates on a second benchmark, ComplexFuncBench, under teacher-forcing (value swap *d* = 0.018 versus emptied observation *d* = 0.702).

An independent, schema-typed oracle that excludes edges detectable by mere string overlap actually decodes even more cleanly, hitting AUROC 0.947 with a conditional-over-position gain of +0.289. The non-positional component, the paper reports, replicates across three further interactive multi-hop benchmarks — and, tellingly, vanishes in single-shot planning tasks where call order alone already tells you the dependency structure.

## Why this matters

For anyone trying to make agents safe or auditable, an internally represented plan is a tempting handle. If the dependency structure of an agent's actions is linearly readable mid-computation, a monitor could in principle verify that an agent's intended plan matches its executed behavior, flag when the two diverge, or catch structural drift before a tool is called. It fits a broader 2026 push toward reading agent internals for hallucination detection, task-drift monitoring and deception probes.

But the authors are unusually disciplined about scope, and the caveats deserve equal billing. Per-layer activation patching shifts the probe's readout at a later boundary — suggesting the representation propagates rather than being a passive readout — yet, crucially, "the realised tool call does not move." As the abstract states flatly: "Our claims concern representation, not behavioural control, and span two model families and one primary domain." Reading a plan is not the same as steering it, and a probe that works on Qwen3-32B in retail scenarios is not yet a general safety tool.

## What to watch next

The obvious next questions are whether the finding holds across more model families and scales, whether high-magnitude value perturbations (not just structural ones) leave the probe invariant, and — the big one — whether reading the plan can be turned into reliably intervening on it. If a future paper shows the decoded dependency graph is causal enough to steer or veto tool calls, this line of work moves from an interpretability curiosity to a live monitoring technique. For now, the headline result stands as a careful, control-heavy demonstration that an agent's tool-call plan is not hidden — it is sitting in the residual stream, waiting to be read.

Sources: [arXiv abstract](https://arxiv.org/abs/2605.25310), [arXiv HTML full text](https://arxiv.org/html/2605.25310v1)
