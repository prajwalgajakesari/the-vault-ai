## The problem with grading a genius

How do you know whether an AI agent has actually discovered a new machine-learning algorithm, or merely regurgitated one it saw during training? For the fast-growing field of automated ML research, that question has become an uncomfortable blind spot. The benchmarks used to score algorithm-discovery systems tend to be small, static, and years old, which means a modern language model may have already ingested their solutions. A high score can signal memorization as easily as ingenuity.

A 2026 arXiv paper from a large team led by the University of Oxford's Alexander D. Goldie takes direct aim at that gap. Titled Procedural Generation of Algorithm Discovery Tasks in Machine Learning, it introduces DiscoGen, a system that manufactures fresh algorithm-discovery problems on demand, so agents can never simply recall the answer.

## Why old benchmarks break down

The authors are blunt about the state of the art. "Our ability to improve and evaluate algorithm discovery systems has thus far been limited by existing task suites," they write. "They suffer from many issues, such as: poor evaluation methodologies; data contamination; and containing saturated or very similar problems."

Data contamination is the headline worry. Once a benchmark's tasks and their known-good solutions circulate on the public internet, they can leak into the training data of the very models being tested. Add in the fact that most existing suites contain only tens of problems, many of them near-duplicates, and it becomes hard to tell genuine discovery from clever recall.

## How DiscoGen works

DiscoGen borrows an idea that transformed reinforcement-learning research: procedural generation. Instead of a fixed list, it defines each task with a handful of configuration parameters and combines them to spawn an enormous space of unique problems. Across 14 domains, including on-policy and offline reinforcement learning, computer-vision classification, Bayesian optimization, language modeling, continual learning, and model unlearning, the generator can produce on the order of 99 billion distinct tasks.

Crucially, the tasks are modular. Rather than asking an agent to solve a whole problem end to end, DiscoGen asks it to invent specific components: a loss function, an optimizer, a network architecture, a training routine. Each task also fixes an evaluation objective (maximize performance, or minimize energy or time while clearing a threshold) and, importantly, splits datasets into a meta-train set the agent may experiment on and a meta-test set held out entirely. A discovered algorithm is judged on data it never touched during search, a design meant to reward genuine generalization. As the authors note, overfitting to a dataset is still overfitting.

To make results comparable across labs, the team also ships DiscoBench, a small, fixed subset of DiscoGen tasks with a principled meta-train/meta-test separation. The full generator, by contrast, is meant for optimizing agents, and the paper frames repeatedly querying it as a form of meta-meta-learning, or improving the agents that improve the algorithms.

## What the numbers show

The early findings are humbling for today's systems. Testing three frontier code models, GPT-OSS 120B, Devstral2, and Deepseek-v3.2, the authors report that current models "consistently struggle to outperform standard baseline implementations across domains." On the On-Policy RL domain, success rates collapse as tasks get harder: Deepseek-v3.2 solves 75 percent of single-component tasks but drops to zero when asked to edit four components at once. The other models fare no better at that difficulty.

The generator's scale also paid off in a prompt-optimization experiment. When the team tuned an agent's prompt over 30 steps, using a single repeated task led to overfitting, while drawing a new task at every step produced prompts that generalized better. Held-out performance improved monotonically with the number of distinct tasks seen, evidence that variety, not repetition, is what teaches an agent to discover.

## Why it matters

AI-for-science is one of the field's boldest bets: agents that don't just apply known methods but invent new ones. That vision only works if we can measure progress honestly, and contamination-prone benchmarks make honest measurement nearly impossible. By turning evaluation into an effectively inexhaustible, procedurally fresh supply of problems, DiscoGen offers a way to separate real capability from lucky recall, and to train better research agents rather than merely rank them.

The work is a broad collaboration spanning Oxford, UC Santa Barbara, UCL, the University of Wisconsin-Madison, and TU Delft, with supervision from Roberta Raileanu, Shimon Whiteson, and Jakob N. Foerster. DiscoGen and DiscoBench are released open source.

## What to watch

Watch whether DiscoBench becomes a shared yardstick the way procedurally generated environments did for RL. Watch, too, whether open contributions expand the 14 domains, and whether meta-meta-learning loops can push agents past the baselines they currently fail to beat. The authors point to algorithm world models, curriculum learning, and better tree search as next frontiers. For now, the more telling result is the simplest one: given genuinely novel problems, today's best models mostly cannot out-discover a standard implementation.
