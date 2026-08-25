Hand Llama-3-8B-Instruct a set of hard math problems and it scores 12.86 percent. Wire four copies of it into a team, let a manager agent redraw who talks to whom at every single round, and the same model scores 47.14 percent. Nothing about the weights changed. Only the wiring did.

That 34-point swing comes from DyTopo, a paper posted to arXiv in February by Yuxing Lu (Peking University and Georgia Tech), Yucheng Hu and Jiuxin Cao (Southeast University), and Xukai Zhao (Tsinghua). It is one of two recent papers arguing that the multi-agent field has been optimizing the wrong variable — obsessing over which model sits inside each agent while treating the communication graph between them as a fixed design choice made once, at build time, and never revisited.

The papers make a real case. A third paper, from Stanford, makes an uncomfortable one: that once you hold token spend constant, most of the multi-agent literature's gains evaporate.

## Fixed wiring, in plain language

Nearly every multi-agent framework in production ships a hardcoded topology. A chain passes output down a line. A star routes everything through a hub. A tree fans out and merges. A full graph lets everyone broadcast to everyone, which works and costs a fortune — message volume grows with the square of the agent count.

The complaint in DyTopo is that a single graph cannot be right for a whole trajectory. Early in a coding task the researcher agent has context the tester needs; three rounds later the tester has failures the developer needs and the researcher is dead weight on the context window. As the paper puts it:

> "This suggests that communication topology should be an adaptive object, conditioned on the round-level goal, rather than a static design choice."

DyTopo's mechanism is cheap and almost embarrassingly simple. Each round, every agent writes two short natural-language descriptors — a "need" and an "offer." A 22M-parameter sentence encoder (all-MiniLM-L6-v2) embeds them, cosine similarity above a threshold induces an edge, and messages route only along those edges, capped at three inbound sources per agent. The graph is rebuilt from scratch every round.

Across four benchmarks (HumanEval, APPS-Competition, MATH-500, Omni-MATH) and four backbones (MiMo-V2-Flash, GPT-oss-120B, Llama-3-8B, Qwen3-8B), DyTopo wins all 16 cells. The gain over the strongest baseline ranges from 0.90 to 17.14 points. The efficiency table is the more interesting one: on HumanEval with MiMo-V2-Flash, DyTopo scores 92.07 percent using 9,453 tokens, against AgentScope's 90.24 percent for 19,520 tokens. Better accuracy at 48 percent of the token cost, because the manager halts early — 2.6 rounds on average against a fixed 5.

That echoes AgentPrune ("Cut the Crap," arXiv:2410.02506), which found that top topology-search systems GPTSwarm and DyLAN burned 2.4x to 5.3x the prompt tokens of a random graph, and got comparable MMLU accuracy for $5.6 where state-of-the-art topologies spent $43.7.

## Diversity instead of density

SYMPHONY (arXiv:2601.22623), a NeurIPS 2025 poster from Wei Zhu, Zhiwen Tang and Kun Yue at Yunnan University, attacks a different failure of homogeneity. When you run Monte Carlo Tree Search with one LLM generating every branch, the branches look alike:

> "These inefficiencies highlight a fundamental mismatch between the need for diverse exploration in planning and the limited variability achievable by repeatedly sampling from a single, monolithic LLM."

Their fix is a heterogeneous pool. SYMPHONY-S runs Qwen2.5-7B, Mistral-7B and Llama-3.1-8B on three RTX 4090s; SYMPHONY-L uses GPT-4, Qwen-Max and DeepSeek-V3. On MBPP it hits 0.927 pass@1 open-source and 0.965 with APIs, against AgentCoder's 0.918. On WebShop, SYMPHONY-S scores 0.82 — matching the human expert baseline — and SYMPHONY-L hits 0.88. On HotpotQA, SYMPHONY-L reaches 0.79 EM using 7,906 tokens per question, where LATS needed 173,290 tokens for 0.63.

The diversity claim is measured, not asserted: expansions where all four branches are unique exceed 80 percent under the three-model ensemble versus under 20 percent single-agent.

## The control experiment nobody ran

Here is the problem. In April, Dat Tran and Douwe Kiela of Stanford published "Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets" (arXiv:2604.02460). They tested five multi-agent architectures — sequential, subtask-parallel, parallel-roles, debate, ensemble — against a single agent across Qwen3-30B, DeepSeek-R1-70B, and Gemini 2.5 Flash and Pro, at matched thinking-token budgets from 100 to 10,000.

At 1,000 tokens the single agent averaged 0.418; the sequential multi-agent system managed 0.379. At 10,000 tokens: 0.426 versus 0.387. The multi-agent system never crossed 0.389 at any budget above the degenerate 100-token floor.

> "Overall, our results suggest that many reported MAS gains are better explained by compute and context effects than by inherent architectural superiority."

Their argument leans on the Data Processing Inequality — every agent-to-agent handoff summarizes, and summarizing can only lose information. To their credit they mark the boundary: debate beat single-agent at every budget on Gemini-2.5-Pro/MuSiQue, and multi-agent recovered ground when they artificially corrupted the context.

Neither DyTopo nor SYMPHONY runs this control. DyTopo's efficiency table compares against multi-agent baselines and a single unassisted pass, not against one model given 9,453 tokens of thinking budget. That is the missing experiment in both.

## Reproducibility notes

DyTopo has no code release and no reported variance or seeds. Its abstract claims "avg. +6.2" while Section 5.1 says +6.09. Its APPS split is 100 problems and Omni-MATH is 70. More pointedly, every reported Math-500 figure is an exact multiple of 1/70 (12.86, 25.71, 47.14, 87.14), implying a 70-problem subset rather than the 500-problem benchmark the column is named after. The affiliation footnote still reads "Southeast University, Location, Country" — an unfilled LaTeX placeholder. It also cites AgentPrune, GPTSwarm, AutoGen and MetaGPT in related work without benchmarking against any of them.

SYMPHONY does release code and runs each experiment three times, but takes baselines from prior work rather than re-running them, uses oracle feedback on HotpotQA, and reports exactly one significance test. Its own ablation is revealing: SYMPHONY wrapped around a single GPT-4 already scores 0.76 EM on HotpotQA, so much of the gain comes from memory sharing and scheduling, not model heterogeneity.

## What to watch

The next credible topology paper should report a cost-normalized single-agent line as a first-class baseline, not a footnote — total tokens on the x-axis, accuracy on the y-axis, one strong model as the reference curve. DyTopo's genuinely useful finding may be the early-halting result, which is an argument about spending less, not coordinating more. If dynamic routing survives an equal-budget comparison, it is a real result. If it does not, the field has spent two years discovering that four API calls beat one.

Watch also for whether anyone reproduces DyTopo without code. Right now, nobody can.
