# 'Learning When to Plan' Teaches AI Agents to Budget Their Own Thinking Time

Ask a modern AI agent to accomplish something in the world and it will usually stop to think before every single move. That habit, borrowed from popular frameworks like ReAct, feels responsible. It is also, according to a new study, wasteful and often counterproductive. A team led by Davide Paglieri argues that the smarter behavior is not to think more, but to think at the right moments, and they have built agents that learn to do exactly that.

The paper, "Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents," comes from researchers at University College London, IDEAS NCBR, the University of Warsaw, the University of Oxford, New York University, and Princeton University. It tackles one of the least glamorous but most consequential questions in agent research: when is deliberate reasoning actually worth the cost?

## The Problem With Thinking All the Time

"Test-time compute" is the extra computation a model spends reasoning through a problem before answering. For hard questions, spending more of it clearly helps. But agents operating over long horizons face a different economics. Every planning step burns tokens, adds latency, and, crucially, can introduce noise that destabilizes an otherwise fine plan.

The authors show both extremes fail. Planning before every action, the ReAct default, is expensive and actually degrades performance on long tasks. Never planning caps how much an agent can achieve. The interesting territory is in between, where an agent reasons only when the expected payoff outweighs the cost.

To make that precise, the team develops a framework for the cost-benefit trade-off of planning in partially observable environments. In their formulation, an agent should spend compute on planning only when the anticipated improvement in performance exceeds the combined cost of tokens, latency, and the instability that excessive replanning can cause.

## How the Method Works

Rather than bolt on a separate controller to decide when to think, the researchers keep everything inside a single model. Their agent is one monolithic LLM that expresses its choice through its own output format: it decides to plan simply by beginning a generation with a special plan token. The same output string is then parsed to pull out the action and, if present, the new plan. Deciding, planning, and acting all live in one network.

Training happens in two stages. First, supervised fine-tuning on synthetic data primes the model with examples that mix planning and non-planning steps within the same trajectory, teaching it that both modes are valid. Second, reinforcement learning, using Proximal Policy Optimization on Llama-3.1-8B-Instruct, refines the skill in a long-horizon environment. The reward is the task reward minus an explicit penalty proportional to the number of tokens a plan consumes, so the agent is motivated, in effect, to plan only when it pays off.

The testbed is Crafter, an open-ended survival game that demands long chains of subgoals, from gathering wood to eventually mining a diamond. It is a demanding stand-in for the kind of multi-step, partially observable tasks real-world agents face.

## The Results

The headline comparison is striking. The team's fine-tuned 8-billion-parameter agent, trained with both stages, reaches a reward of 0.387 while generating just 1,714 tokens per episode on average. A much larger Llama-3.3-70B baseline that plans every four steps scores 0.379 but burns 11,511 tokens. In other words, the small dynamic-planning agent edges out a model nearly nine times its size while producing roughly 85 percent fewer tokens.

The internal comparisons reinforce the point. The dynamic SFT+RL agent (0.387) beats its own "never plan" variant (0.298) and the SFT-only dynamic agent (0.343). Notably, applying RL without the SFT priming stage backfires: that configuration collapses to 0.210 reward while ballooning to nearly 11,000 tokens, confirming that priming is a prerequisite for learning good planning discipline.

RL also improved the quality of the planning loop itself. The SFT+RL agent completed 20 percent of its plans within 15 steps (versus 16 percent for SFT alone) and appropriately abandoned 41 percent of plans through adaptive replanning when the environment shifted (versus 35 percent).

One further finding points toward safer, more collaborative systems: after RL, agents could be steered by human-written plans to reach performance beyond what they achieve alone. In a best-of-N analysis, an agent guided by human plans even solved Crafter outright by mining a diamond, something no autonomous configuration managed. That steerability emerged only after RL, not from priming alone.

## Why It Matters

For the past few years, the dominant story in AI has been scale: bigger models, more parameters, more compute. This work is part of a growing counter-narrative that says efficiency is becoming the frontier. Agents are increasingly deployed in loops that run for dozens or hundreds of steps, and at that length the cost of reflexive reasoning compounds fast. An agent that matches a 70B model at a fraction of the token budget is not just cheaper to run; it is faster, more deployable, and more sustainable.

The framing also reframes reasoning as a resource to be budgeted rather than a switch to be left on. That is a subtle but important shift, moving the field from "how much can the model think" toward "when should it." The steerability result adds a governance angle: agents that can be guided by human plans, and that reason legibly about when they are planning, are easier to supervise.

## What to Watch

The experiments center on Crafter, a rich but game-like environment. The open question is how well learned planning discipline transfers to messier real-world domains: software engineering agents, web navigation, robotics, and tool-use pipelines where latency costs are not effectively zero. Watch for whether the two-stage recipe generalizes across model families and larger scales, whether the token penalty needs careful tuning per domain, and how the human-steering result develops into practical human-agent collaboration. If dynamic planning holds up beyond the game world, "knowing when to think" could become a standard ingredient in how capable agents are built.
