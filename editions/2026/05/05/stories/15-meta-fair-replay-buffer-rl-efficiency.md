---
headline: "Meta FAIR Shows Replay Buffers Can Slash the Cost of Reinforcement Learning for Large Language Models"
slug: meta-fair-replay-buffer-rl-efficiency
category: research
story_number: "15"
date: 2026-05-05
author: The Vault AI
sources:
  - name: arXiv
    url: https://arxiv.org/abs/2604.08706
    domain: arxiv.org
  - name: Air Street Press
    url: https://press.airstreet.com/p/state-of-ai-may-2026
    domain: press.airstreet.com
  - name: Emergent Mind
    url: https://www.emergentmind.com/papers/2604.08706
    domain: emergentmind.com
  - name: Hugging Face Papers
    url: https://huggingface.co/papers/2604.08706
    domain: huggingface.co
---

# Meta FAIR Shows Replay Buffers Can Slash the Cost of Reinforcement Learning for Large Language Models

The dominant recipe for making large language models smarter through reinforcement learning has a conspicuous blind spot: it throws away nearly every piece of data it generates. A new paper from Meta's Fundamental AI Research lab argues that this wastefulness is not only unnecessary but actively harmful -- and that a well-designed replay buffer can cut training compute by up to 40 percent while matching or even exceeding the performance of conventional approaches.

## The Problem with "Generate and Discard"

Published on April 9 by Charles Arnal, Vivien Cabannes, Taco Cohen, Julia Kempe, and Remi Munos, "Efficient RL Training for LLMs with Experience Replay" takes aim at one of the most expensive bottlenecks in modern AI development. Current on-policy RL algorithms like GRPO (Group Relative Policy Optimization) and PPO generate thousands of model responses -- known as rollouts -- evaluate them against a reward signal, perform a single gradient update, and then discard every response. The next training step starts the entire cycle from scratch.

"Experience replay -- the practice of storing rollouts and reusing them multiple times during training -- is a foundational technique in general RL, but remains largely unexplored in LLM post-training due to the prevailing belief that fresh, on-policy data is essential for high performance," the authors write in the paper.

That belief, the FAIR team argues, is wrong -- or at least incomplete. In traditional reinforcement learning for robotics and game-playing, replay buffers have been standard equipment since DeepMind's landmark Atari work over a decade ago. But the LLM community has largely ignored the technique, assuming that the distribution shift introduced by reusing older data would poison training.

## 40 Percent Compute Savings, No Performance Penalty

The paper's core contribution is a formal framework that treats replay buffer design as a three-way optimization problem, balancing staleness-induced variance (older data becomes less representative of the current policy), sample diversity (more varied data improves generalization), and the computational cost of generating new rollouts (the single most expensive step in LLM RL training).

The empirical results are striking. Testing on Qwen2.5-7B trained on the MATH benchmark using GRPO, the researchers found that a well-chosen replay buffer reached the same final accuracy with approximately 40 percent less compute. The approach was validated across multiple model sizes, including Qwen3-0.6B, and across both the OpenR1-Math-220k and MATH evaluation benchmarks.

"A well-designed replay buffer can drastically reduce inference compute without degrading -- and in some cases even improving -- final model performance, while preserving policy entropy," the authors report.

The implementation is deliberately minimal: inference workers continuously push completed trajectories into a first-in-first-out (FIFO) buffer, while training workers sample uniformly from whatever is currently stored. There is no complex prioritization scheme, no curriculum design -- just a straightforward queue that turns the wasteful generate-and-discard pipeline into a generate-and-reuse one.

## Bigger Buffers, Steadier Training

One of the paper's more nuanced findings concerns buffer size. Larger buffers slow the pace of learning because any given training batch contains a higher proportion of stale data. But this slower pace comes with a payoff: training stability improves markedly, and in some configurations the model reaches a higher peak accuracy than its on-policy counterpart ever achieves.

This tradeoff has practical implications for teams choosing how to allocate their GPU budgets. A lab that can tolerate a somewhat longer wall-clock time might prefer a larger buffer that delivers a better final model. A team on a tighter deadline might opt for a smaller buffer that still captures most of the compute savings while keeping the training curve steep.

## Why It Matters Now

The timing of this research is significant. Reinforcement learning has become the critical post-training step for frontier LLMs, powering the reasoning capabilities that distinguish models like OpenAI's o-series and Meta's own Llama releases. But the cost of RL training has been escalating rapidly, driven primarily by the expense of generating millions of rollouts using increasingly large models. Anything that reduces the number of fresh rollouts required per unit of learning directly attacks one of the largest line items in the AI industry's compute budget.

The Air Street Press "State of AI" report for May 2026 highlighted the work as evidence that strict on-policy sampling is suboptimal when generation costs are high -- a finding that could reshape how labs allocate resources for post-training.

The paper also arrives amid a broader wave of interest in off-policy methods for LLM training. Related work from other groups, including research on freshness-aware prioritized experience replay and difficulty-targeted data selection, suggests that the field is converging on a shared conclusion: the generate-and-discard era is ending.

## The Bigger Picture

Meta FAIR's contribution is notable for its simplicity. The replay buffer requires no architectural changes to existing RL pipelines, no new loss functions, and no hyperparameter searches beyond choosing a buffer size. It is, as the authors describe it, a "minimal, easy-to-drop-in" modification -- the kind of unglamorous infrastructure improvement that can quietly compound across an entire industry.

For the dozens of organizations currently spending millions on RL post-training, a 40 percent reduction in compute is not an abstraction. It is real money, real energy, and real time returned to the research budget. If the finding holds across larger model scales and more complex tasks -- something the paper's framework predicts but does not yet prove -- replay buffers may soon become as standard in LLM training as they have been in robotics RL for the past decade.