Only two AI models can finish more than half of the real scientific research workflows in Terminal-Bench-Science, and on an independent rerun there is little to separate them. Artificial Analysis this week published its own leaderboard for the Stanford-led benchmark. OpenAI's GPT-6 Astra at maximum reasoning effort passed 63.3% of tasks, and Anthropic's Claude Opus 5.5 at xhigh adaptive reasoning passed 61.9%. That is a 1.4-point gap on a 70-task test, which is well inside the range where one or two tasks change the ranking.

The benchmark isn't new. The Terminal-Bench team released Terminal-Bench-Science 0.1 on August 27. The news is that someone other than the labs and the benchmark authors has now measured the frontier models under a single, controlled setup. That matters because the numbers the vendors published look different. In their launch materials, Astra was listed at 64.6% on Terminal-Bench Science 0.1 and Opus 5.5 at 58.7%, a gap of almost six points. Under Artificial Analysis's harness, most of that gap disappears.

## A harness built to remove the scaffolding

Artificial Analysis ran every model through mini-swe-agent, a deliberately minimal agent scaffold, rather than each lab's own tooling such as Claude Code or Codex. Each of the 70 tasks was attempted three times, and scores are pass@1 averaged across those runs. Grading is all-or-nothing. The agent works in a sandboxed terminal with the task's data and software, pytest-based verifier checks written by the task author inspect the resulting files and calculations, and a task passes only if every test passes. Each run can use up to 28,800 seconds, or eight hours, of wall time. Pulling existing annotations or online solutions is not allowed.

The tasks are real research work. Examples from the release include reconstructing ten winters of lake freeze-up and ice-off dates from raw satellite imagery, tracking every cell division across an 800-frame recording of mouse myoblasts, and computing the geocentric state vector of an unknown near-Earth asteroid from raw Minor Planet Center astrometry, with position tolerances measured in kilometres. The 0.1 release contains 19 life-science tasks, 17 physical-science tasks, 17 mathematical-science tasks, 9 engineering tasks and 8 earth-science tasks. Out of 920 proposals from 376 contributors in 22 countries, only 70 tasks made it into the release.

"Scientists, not model developers or data vendors, set the bar for scientific capability in AI," Stanford's Steven Dillmann wrote in the August announcement. In a post on X he added that "it's time science gets as much attention in agentic evals as coding."

## Behind the top two

Below Astra and Opus 5.5 the scores drop off sharply. Anthropic's Claude Fable 5.1 finishes roughly 20 points behind the leaders. Qwen3.8 Max is the strongest closed model from outside OpenAI and Anthropic at 12%. The best open-weight entrants, GLM-5.3 at max effort and DeepSeek V4.1 Flash, score 10% and 9%, more than 50 points behind Astra.

The leaderboard also shows how much reasoning effort changes the result, and what it costs. Opus 5.5 goes from about 24% at low effort to 61.9% at xhigh, while average cost per task rises roughly fivefold. OpenAI's GPT-6 Sol gains 27 points between low and max effort at about 7.5 times the cost. More compute does not always help. Opus 5.5 at max effort scores 59.0%, 2.9 points below its xhigh result. Results by domain follow a similar pattern for most models: mathematics is the strongest area and life science the weakest. Opus 5.5 at xhigh passes 71% of the math tasks and 46% of the life-science tasks. The benchmark authors caution that domain samples of 8 to 19 tasks make those comparisons noisy.

The progress in one month is large. When the benchmark launched, its authors' own leaderboard had Claude Opus 5 on top with a 30.0% resolution rate, followed by GPT-5.6 Sol at 22.4%. Today's leaders have roughly doubled that. The authors said the 0.1 tasks were calibrated specifically to challenge Opus 5 and GPT-5.6 Sol.

## Why It Matters

Scientific AI benchmarks have mostly tested knowledge through isolated questions. This one checks whether an agent can carry a messy computational workflow through to the end, keep track of intermediate state, recover from tool errors, and produce outputs that pass deterministic checks. It has quickly become a benchmark labs cite: both OpenAI and Anthropic reported scores for their new flagships within weeks of release. That is also why an independent rerun is important. Vendor figures come from different harnesses and settings, and in this case they overstated the gap between the two leaders several times over.

The cost numbers are just as useful for buyers. Opus 5.5 lists at $4 per million input tokens and $20 per million output tokens, compared with $10 and $50 for Astra. But at maximum effort Opus 5.5 uses far more tokens, and on Artificial Analysis's broader Intelligence Index it costs about $5.98 per task versus $3.26 for Astra. For teams building science agents, the practical conclusion from the effort curves is that the highest setting is not automatically the best choice. Xhigh beats max on Opus 5.5 while costing less.

Open models are clearly far behind on this kind of work. A 50-point gap on end-to-end research tasks is much wider than the gaps usually seen on coding benchmarks, and it suggests that long-horizon scientific tool use is still mostly limited to frontier closed models.

## What to Watch

The benchmark's maintainers are collecting tasks for Terminal-Bench-Science 0.2, with a pull-request deadline of October 5. They plan to retire saturated tasks and recalibrate against today's leaders, which should push scores back down once Astra- and Opus 5.5-level systems become the calibration target. Also watch whether Artificial Analysis adds this benchmark to its Intelligence Index, how Anthropic's upcoming Sonnet 5.5 and OpenAI's wider GPT-6 Sol rollout score on the mini-swe-agent harness, and whether the life-science results, the weakest domain for most leading models, improve fastest as labs target the benchmark's failure cases.
