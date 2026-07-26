# Teaching AI Agents to Plan Before They Act — Efficiently

The reigning recipe for smarter AI agents in 2026 has been blunt: let them think longer. Give a model more room to reason, more tokens to burn, and watch the benchmark scores climb. But that recipe has quietly hit a wall. Longer reasoning traces cost more, run slower, and increasingly fail to deliver reliable gains — sometimes the extra deliberation makes things worse, as models talk themselves into errors or overflow their own context windows.

A new paper from researchers at Carnegie Mellon University and the Institute of Foundation Models offers a pointed alternative: teach the agent to decide, on its own, when thinking is worth it. Titled "Efficient Agentic Reasoning Through Self-Regulated Simulative Planning," the work argues that the appetite for ever-longer reasoning is not a law of nature but a design flaw — a symptom of building agents as one undifferentiated stream of chain-of-thought with no genuine control over their own planning.

## Three systems instead of one stream

The authors, led by co-first authors Mingkai Deng, Jinyu Hou and Lara Sá Neves, propose splitting an agent's decision-making into three interacting systems. System I is reactive execution — the fast, free-form reasoning and action that handles routine steps. System II is simulative reasoning: instead of unconstrained chain-of-thought, the agent proposes candidate actions, predicts their consequences using a world model, and picks the sequence that best advances the goal. System III is the crucial addition — a learned "configurator" that decides, turn by turn, whether to plan at all and how far ahead to look.

"We argue that efficient agentic reasoning benefits from a decomposition of decision-making into three interacting systems: simulative reasoning (System II) that grounds deliberation in future-state prediction using a world model, rather than unconstrained chain-of-thought; self-regulation (System III) that decides when and how deeply the agent plans at each turn through a learned configurator; and reactive execution (System I) that handles fine-grained reasoning and action," the authors write.

The practical payoff of that configurator is that the expensive planning machinery only fires when a step is genuinely hard. On easy moves, the agent can skip planning entirely and just act. In the team's instantiation, called SR²AM (Self-Regulated Simulative Reasoning Agentic LLM), the language model itself serves as the world model, and the configurator and planner are implemented as distinct stages inside the model's chain-of-thought rather than as separate external modules.

## Planning further, not more often

The most striking finding concerns what happens when the system is trained with reinforcement learning. Rather than learning to plan constantly, the agent learns to plan more deliberately. "Analysis reveals that RL increases average planning horizon by 22.8% while planning frequency grows only 2.0%, indicating that the model learns to plan further ahead rather than more often," the authors report. In other words, when the agent does decide to plan, it looks several steps into the future — but it reserves that effort for the moments that warrant it, leaving simple turns unplanned.

The team evaluated two models — an 8-billion-parameter version built on Qwen3-8B and a 30-billion-parameter version built on a Qwen3 reasoning model — across 11 benchmarks spanning math (including AIME and MATH-500), science (GPQA-Diamond, SuperGPQA, and a subset of HLE), tabular analysis (FinQA), and web information-seeking tasks (BrowseComp, GAIA and XBench-DeepSearch).

According to the paper, the smaller 8B model reached an overall Pass@1 of 57.0 while consuming an average of roughly 3,700 reasoning tokens per trajectory — competitive, the authors say, with unregulated agentic models several times its size. The larger 30B model reached 71.3, which the paper describes as competitive with far larger systems in the 685-billion to 1-trillion parameter range. The efficiency claim is the headline: among comparably sized agentic models clearing a 60 Pass@1 bar, the authors report their model uses between 25.8 and 95.3 percent fewer reasoning tokens while matching or beating accuracy. Against one specific 30B competitor, they cite 51.2 percent fewer reasoning tokens at competitive accuracy.

## Why budgeting compute is the story of 2026

This paper lands squarely inside the defining research theme of the year. Through 2025 and into 2026, the field leaned hard on test-time compute — the idea that you can trade more inference-time thinking for better answers. It worked, until diminishing returns set in at scale. The frontier question has shifted from how to make models think more to how to make them think the right amount. Anthropic, OpenAI and others have shipped user-facing knobs for reasoning effort; the research community is now trying to make that budgeting automatic and internal.

The self-regulation framing matters because it reframes efficiency as a capability rather than a constraint. Most token-saving techniques prune or truncate after the fact. Here, the model is trained to own the decision — to treat its own compute as a resource to allocate. The authors put the underlying diagnosis bluntly: the need for ever-longer reasoning traces, they suggest, "may be a consequence of building the agent as an undifferentiated reactive policy, which lacks genuine internal agency over its own planning."

## What to watch

The authors are candid about limits. Their world model lives entirely in language space, which caps how well it predicts real physical or social dynamics; extending the approach to multimodal or embodied settings is flagged as future work, as is testing it in multi-agent environments. They also note that they evaluated the system holistically and have not yet isolated how accurate the configurator and world model are on their own.

The more provocative thread is the suggestion that self-regulation need not stop at planning. The same configurator mechanism, the authors argue, could govern when an agent updates its world model, revises its goals, or learns from mental simulation — turning a single regulated process into many. If that pans out, the lesson of this paper may outlast its benchmarks: the next leap in agents might come not from thinking more, but from knowing when to stop.
