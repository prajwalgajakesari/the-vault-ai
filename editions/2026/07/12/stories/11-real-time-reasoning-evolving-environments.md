## The world does not wait for the model to finish thinking

Almost every benchmark that grades an AI agent shares a quiet, convenient fiction: time stops while the model reasons. The traffic freezes, the clock halts, the other players politely wait for the language model to emit its next token. Real life is not so courteous. A new 2026-circulated arXiv paper, "Real-Time Reasoning Agents in Evolving Environments," sets out to strip away that assumption and measure what happens when the environment keeps moving while the agent is still mid-thought.

"Agents in the real world must make not only logical but also timely judgments," the authors write. "This requires continuous awareness of the dynamic environment: hazards emerge, opportunities arise, and other agents act, while the agent's reasoning is still unfolding." That sentence is the whole thesis. Reasoning that is correct but late can be worse than useless.

The work comes from Yule Wen (Tsinghua University), Yixin Ye (Shanghai Jiao Tong University), Yanzhe Zhang (Georgia Institute of Technology), and Diyi Yang and Hao Zhu (Stanford University), under Stanford's SALT Lab. It was submitted to arXiv in November 2025 as a 30-page paper with a public code release and dataset.

## A gym where the clock keeps ticking

To study the problem, the team built the Real-Time Reasoning Gym, a set of non-turn-based games in which an agent may act at any moment but the world evolves regardless of whether the agent has decided anything. Three environments each stress a different pressure. Freeway forces an agent across lanes of moving traffic, where hazards emerge continuously. Snake dangles food that appears and vanishes, rewarding agents that seize fleeting opportunities without trapping themselves. Overcooked requires cooperation with a scripted partner whose policy shifts over time, demanding coordination rather than solo planning.

The clever design choice is how the gym measures time. Rather than wall-clock seconds, which depend on whatever GPU you happen to own, the benchmark counts elapsed tokens as a hardware-agnostic unit of time. That lets researchers tune two independent dials: cognitive load (how hard the puzzle is) and time pressure (how many tokens the agent may spend before the world advances). The authors validated the abstraction against real hardware, finding token count and physical inference time correlate almost perfectly (R-squared of 0.9986) using DeepSeek's API.

## Fast reflexes, slow plans, and the trap in between

The paper frames two familiar strategies. Reactive agents use bounded computation for quick, System-1-style responses. Planning agents spend extended reasoning on System-2-style deliberation. Both fail in predictable ways. Reactive agents stay timely but make shallow decisions when the puzzle gets hard. Planning agents make good decisions when unhurried, then fall apart under a deadline. The authors quantify the cliff: a planning agent's normalized score collapses from 0.92 to 0.05 as time pressure increases.

Their proposed fix, AgileThinker, refuses the trade-off by running both systems at once. A planning thread deliberates in the background while a fast reactive thread makes the actual moves, and crucially, the reactive thread can read the planning thread's partial, still-streaming reasoning trace. The slow thinker's half-formed plan immediately sharpens the fast thinker's snap decisions, without waiting for the plan to finish.

The result is a much gentler decline. Under the same rising pressure that dropped the planning agent to 0.05, AgileThinker slips only from 0.90 to 0.58. In wall-clock experiments, using a reactive DeepSeek-V3 thread and a planning DeepSeek-R1 thread, AgileThinker scored 0.88 on Freeway, 0.45 on Snake, and 0.89 on Overcooked, against near-zero planning-agent scores of 0.12, 0.04, and 0.00. "AgileThinker consistently outperforms agents engaging only one reasoning paradigm as the task difficulty and time pressure rise," the authors write, "effectively balancing reasoning depth and response latency."

## Why it matters beyond games

The games are toys, but the pressure they model is not. Any agent that touches the physical or interactive world, a robot crossing a room, a trading bot, a driver-assist system, a customer-service agent negotiating with a live human, faces a version of Freeway's problem: deliberation has a cost measured in missed opportunities and emerging hazards. Most of today's reasoning research optimizes accuracy while implicitly assuming latency is free. This paper argues that assumption quietly disqualifies those methods from real deployment, and shows that even state-of-the-art models struggle once the clock is allowed to run.

It also offers a concrete architectural lesson. Better single-model budget control, the paper finds, cannot bridge tight and loose deadlines alone; the dual-thread design, where fast and slow reasoning share a live scratchpad, appears to be doing real work.

## What to watch

The open questions are practical ones. The optimal token budget varied by environment (roughly 5,000 tokens for Freeway, 2,000 for Snake and Overcooked), hinting that real-time agents will need to estimate their own thinking budgets on the fly. Watch for whether AgileThinker-style parallel reasoning gets folded into embodied and robotics stacks, whether the Real-Time Reasoning Gym becomes a standard testbed the way earlier agent benchmarks did, and whether labs start reporting latency-under-pressure numbers alongside the accuracy scores that have dominated the leaderboard so far.
