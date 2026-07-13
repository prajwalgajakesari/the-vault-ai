## The problem: agents that think too much

Ask a modern AI agent to solve a math problem or navigate a website, and it will often do something wasteful: reason at great length whether the task warrants it or not. The dominant recipe for building these agents is to train a single reactive policy end-to-end and simply hope that useful planning "emerges" from enough data and compute. In practice, that hope has a cost. As a new 2026 arXiv paper puts it, these systems, "without control over the presence, structure, or horizon of planning, typically increase reasoning length dramatically during training, leading to inefficient token consumption that does not reliably translate to accuracy gains."

That single sentence captures a growing anxiety in the agent world. Longer chains of thought mean more tokens, more latency, and more money per task, yet the extra deliberation frequently buys nothing. The paper, "Efficient Agentic Reasoning Through Self-Regulated Simulative Planning," argues the fix is not more thinking but better-governed thinking.

## The method: three systems instead of one

The authors, a team led by Mingkai Deng at the Institute of Foundation Models and Carnegie Mellon University, with collaborators from IST and the University of Lisbon, propose decomposing an agent's decision-making into three interacting systems rather than one monolithic chain of thought.

System I, reactive execution, is fine-grained, free-form reasoning that directly emits the next action and tool call. System II, simulative reasoning, kicks in when planning is warranted: the agent generates a structured plan of proposed actions and predicted future states, using the LLM itself as a world model in language space. System III, self-regulation, is a learned "configurator" that decides, at every turn, whether to make a new plan, continue an existing one, or skip planning entirely.

Their instantiation is called SR2AM (Self-Regulated Simulative Reasoning Agentic LLM). Crucially, all three systems share a single model and are realized as distinct stages inside one chain of thought, so nothing is bolted on as a separate network. The configurator decides whether to plan, the simulative planner decides what to plan, and the actor decides how to act. Training runs in two stages: supervised fine-tuning on trajectories that interleave these decisions, followed by reinforcement learning with Group Relative Policy Optimization so the configurator learns to invoke deeper planning only when it actually helps.

## The results: trillion-parameter accuracy, a fraction of the tokens

The efficiency payoff is the headline. Evaluated across mathematical reasoning, scientific problem-solving, tabular data analysis, and web information seeking, the smaller SR2AM-v0.1-8B posts an overall Pass@1 of 57.0, competitive with unregulated agentic LLMs at 30-32B and tool-using pretrained models at 120-355B parameters.

The larger SR2AM-v1.0-30B reaches 71.3, which the authors place alongside DeepSeek-V3.2 (685B, 73.2) and Kimi-K2.5 (1.0T, 70.9) in the same tool harness, systems more than twenty times its size. And it gets there while spending far less. Against comparable 30-32B agentic models, v1.0-30B consumes 25.8% to 95.3% fewer reasoning tokens at competitive or better accuracy. In one direct comparison with MiroThinker-v1.5-30B, it matched Pass@1 while using 51.2% fewer reasoning tokens (5,518 versus 11,295).

The most revealing finding is about how the model learns to economize. After reinforcement learning, the average planning horizon grew by 22.8% while planning frequency rose only 2.0%. In other words, the agent did not learn to plan more often; it learned to plan further ahead when it chose to plan at all. That pattern held across every task category, from +20.9% in web tasks, where a shifting environment limits how far ahead lookahead is useful, to +32.7% in science.

## Why it matters for real deployments

For anyone paying per token to run agents in production, this is the practical crux. Reasoning length has quietly become one of the largest and least predictable cost drivers in agentic systems, and "always-on" deliberation scales badly. SR2AM reframes efficiency as a control problem: give the model an explicit knob for when and how deeply to deliberate, and let RL tune it toward outcomes rather than verbosity. A 30B model that rivals trillion-parameter systems at a fraction of the token spend is exactly the kind of cost-to-capability trade practitioners have been waiting for.

It also gestures at a cleaner design philosophy. Instead of treating a chain of thought as one inscrutable black box, the three-system factorization makes an agent's planning decisions inspectable: you can see when it decided to plan and how far it looked.

## What to watch

The authors have released both models (8B and 30B) and code, so independent replication of the token-savings claims should come quickly. Watch whether the configurator's discipline holds on longer-horizon, higher-uncertainty tasks like multi-day web agents, and whether the world-model-in-language-space approach transfers cleanly to domains where predicting future states is harder than in math or tabular data. If self-regulation proves robust, expect "decide how much to think" to become a standard component of agent training rather than a research novelty.
