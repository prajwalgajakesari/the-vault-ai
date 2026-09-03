# Everyone Benchmarks What Agents Can Do. Almost Nobody Benchmarks What They Cost.

Two web agents ran the same benchmark. One scored 40% and burned $1,577 in API fees. The other scored 42% and cost $171. On a leaderboard, the second agent wins by two percentage points. In a procurement meeting, it wins by nine times.

That comparison — Browser-Use running Claude Sonnet 4 against SeeAct running GPT-5 Medium on Online Mind2Web — appears in the Holistic Agent Leaderboard, one of the few public evaluations that tracks what a benchmark run costs. Almost nobody else does. A comprehensive survey published this summer in Findings of the Association for Computational Linguistics argues that this omission is now one of the largest unaddressed gaps in how the industry measures its most-hyped product category.

## The Survey That Names the Gap

"A Survey on Evaluation of LLM-based Agents," by Asaf Yehudai, Lilach Edelstein, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan and Michal Shmueli-Scheuer — a team spanning IBM Research and Yale — maps the field across five perspectives: the core LLM capabilities agentic workflows depend on, such as planning and tool use; application-specific benchmarks for web and software-engineering agents; evaluation of generalist agents; the core dimensions of agent benchmarks themselves; and the frameworks agent developers actually use.

The good news is real: benchmarks are getting harder, more realistic and more frequently refreshed. The bad news is what the field has not built. The authors identify "critical gaps that future research must address — particularly in assessing cost-efficiency, safety, and robustness, and in developing fine-grained, scalable evaluation methods."

They are blunt about the mechanism. "Current evaluations often prioritize performance while overlooking cost and efficiency measurements," the authors write. "This emphasis can inadvertently drive the development of highly capable but resource-intensive agents, limiting their practical deployment." Their prescription is specific: future frameworks should treat cost efficiency as a core metric, "tracking factors such as token usage, API expenses, inference time, and overall resource consumption."

## What the Numbers Look Like When Someone Measures

The Holistic Agent Leaderboard, built by Sayash Kapoor, Benedikt Stroebl, Arvind Narayanan and a large multi-institution team, is the closest thing the field has to an audit. HAL ran 21,730 agent rollouts across nine models and nine benchmarks in coding, web navigation, science and customer service, at a total cost of roughly $40,000 and 2.5 billion tokens of logged model calls. Its diagnosis of the field is one sentence long: "agents vary widely in costs, but evaluations rarely report these costs."

The spreads it found are not marginal. A single run of SWE-bench Verified costs a median of $163 but ranges to $1,600, with per-task costs from $0.08 to $32.00 — roughly 400x, driven by model pricing and scaffold design. And higher spend does not reliably buy accuracy: on GAIA, an HAL generalist running o3 Medium spent $2,828 to reach 28.5%, while a different configuration hit 57.6% for $1,686. In only one of nine benchmarks did the most expensive model land on the accuracy-cost Pareto frontier at all. Gemini 2.0 Flash made the frontier in seven of nine.

Independent work points the same direction. CLEAR, a multi-dimensional enterprise agent framework, tested six state-of-the-art agents across 300 enterprise tasks and found that "accuracy-optimal configurations cost 4.4 to 10.8x more than Pareto-efficient alternatives" at comparable real-world performance. Kapoor's earlier "AI Agents That Matter" showed simple baseline agents Pareto-dominating Reflexion, LDB and LATS on HumanEval at 50x lower cost — an argument that a large share of agentic complexity is buying leaderboard position rather than capability.

## Why This Is a Procurement Problem

Leaderboards are no longer academic scoreboards. They are the artifact enterprises hand to a vendor-selection committee. And a cost-blind leaderboard is not neutral — it actively rewards spending.

"Cost-blind leaderboards now mislead by design, because they reward extra spending without reporting what that spending bought," write Avijit Ghosh, Yifan Mai, Georgia Channing and Leshem Choshen in an EvalEval Coalition analysis published in April. Their broader finding is that evaluation has crossed a cost threshold that changes who is allowed to do it: an independent reproduction of HAL by Franck Ndzomga landed at $46,000 across 242 agent runs, and a statistically credible version with eight reruns per cell would push the bill toward $320,000. Their conclusion is uncomfortable: "Whoever can pay for the evaluation gets to write the leaderboard."

Robustness is the second half of the survey's gap, and it is entangled with the first. On τ-bench, agent performance has been reported dropping from 60% on a single run to 25% under an eight-run consistency requirement. HAL found that a do-nothing agent passes 38% of τ-bench airline tasks under the original construction, and its own log inspection surfaced data leakage in a τ-bench few-shot scaffold, removed in December 2025, plus agents searching Hugging Face for the benchmark instead of solving the task. A related reliability paper from Rabanser, Kapoor and colleagues concludes that "recent capability gains have only yielded small improvements in reliability."

The accuracy number on the leaderboard, in other words, is often the least robust thing being measured — while the two numbers a buyer needs, dollars per resolved task and pass rate across repeated runs, are the ones nobody publishes.

## What to Watch

Three signals. First, whether cost-per-task migrates from independent trackers into the benchmarks themselves. Artificial Analysis already reports average API cost per task, token mix, wall time and a Pareto line across its coding-agent index; the academic leaderboards mostly do not. Second, whether cheap evaluation gets solved. Static benchmarks compress 100x to 200x without losing rankings; Ndzomga's mid-difficulty filter, which keeps only tasks with 30-70% historical pass rates, cuts task counts 44-70% but yields at most 2x to 3.5x savings. Third, whether reliability reporting becomes table stakes. HAL has paused new model evaluations to focus on it — a signal that the field's own scorekeepers no longer trust single-run numbers.

Until standardized cost metrics exist, every agent leaderboard is reporting half a result.
