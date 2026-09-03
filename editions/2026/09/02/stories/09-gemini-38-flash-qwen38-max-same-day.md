# Google and Alibaba Both Shipped a Flagship on September 2. Neither Mentioned the Other.

Inside a single UTC day, the two labs with the fastest shipping cadence in the industry each pushed a new flagship into production. Alibaba's Qwen team announced Qwen3.8-Max-0902 at 10pm Eastern on Tuesday — already September 2 in Greenwich, and already stamped into the model id, qwen3.8-max-2026-09-02. Google DeepMind released Gemini 3.8 Flash the following afternoon. Neither announcement, neither benchmark table, and neither blog post mentions the other company.

That is the clearest signal yet of how the frontier has fragmented: Google is benchmarking itself against OpenAI, xAI and Anthropic; Alibaba is benchmarking itself against Claude Opus 5 and its own previous snapshot. The two are converging on the same customer — the enterprise buying long-horizon coding agents — from opposite ends of the pricing and licensing spectrum, and pretending the other lane does not exist.

## Two Launches, Eighteen Hours Apart

Gemini 3.8 Flash is Google's fourth Flash-tier model in under four months. It scores 59 on the Artificial Analysis Intelligence Index at high reasoning, three points above its predecessor and level with GPT-5.6 Sol at extra-high effort. The context window holds at 1M tokens. Pricing holds too, at a discounted $0.75 per million input tokens and $3.75 per million output through December 31, after which it doubles to $1.50/$7.50.

"Gemini 3.8 Flash delivers substantial gains from 3.7 Flash, often approaching the performance of higher-cost frontier models," wrote Tulsee Doshi, Google senior director of product management, and Raluca Ada Popa, Gemini security lead at Google DeepMind, in the launch post. "On DeepSWE v1.1 (Long-Horizon Software Engineering) 3.8 Flash outperforms most larger frontier models in autonomously solving complex engineering problems end to end, only at a fraction of the cost."

Qwen3.8-Max-0902 is an in-place upgrade to a model that already existed. Same 2.4-trillion-parameter base, same 1M context window, same $2 input and $6 output per million tokens. What changed is post-training. The QwenCloud model card describes coding that now handles "more complex engineering-scale projects and long-horizon autonomous development" and agent behavior with "greater composure in multi-tool orchestration and end-to-end task delivery." The X announcement compressed it to five words: "Further post trained on Coding & Cowork."

The gains are concentrated exactly where the old snapshot was weakest. On Qwen's own launch table, TerminalBench 3.0 went from 11.3 to 29.0. ProgramBench went from 10.5 to 28.0. JobBench rose from 53.4 to 64.0, and the in-house WorkArena Elo climbed 120 points to 1,468. Alibaba says its front-end CodeArena score rose 22 points to 1,691, first on that leaderboard.

## The Numbers Each Side Chose to Show

Google's headline improvement is agentic. The three-point Intelligence Index gain comes almost entirely from tool use and coding — the largest single jump is 12 points on the tool-use benchmark tau-cubed-Banking, to 45%. Humanity's Last Exam barely moved. And the cost story is more complicated than the unchanged sticker price: because 3.8 Flash emits roughly 30% more output tokens per task, Artificial Analysis measures its cost per Intelligence Index task at $0.58, up about 40% from 3.7 Flash's $0.40. Doshi and Popa concede the mechanism directly: "3.8 Flash works harder. On complex tasks, it exhibits greater diligence — executing extra reasoning steps, and calling tools iteratively."

Qwen's table is more candid than most vendor tables and less useful than it looks. Claude Opus 5 leads 0902 on TerminalBench, DeepSWE, NL2Repo, ProgramBench, SWE-Marathon, CoWorkBench, JobBench and Toolathlon. Three of the benchmarks shown are Qwen's own, and 0902 loses two of them. A footnote warns that rival TerminalBench numbers are "the best published score across harnesses," which makes those columns directional at best. Where 0902 leads is specific: repository-level code understanding, agentic SaaS workflow automation, and visual reasoning.

## Why This Matters

**The open-versus-closed price gap is no longer where trackers say it is.** Third-party aggregators listing Gemini 3.7 Flash near $75.00 per million tokens and Qwen3.8 Flash near $15.00 are off by two orders of magnitude — a unit-conversion error, not a market. The real spread is tighter and stranger: Google's closed Flash model undercuts Alibaba's Max model on fresh tokens ($0.75 vs $2.00 input), while Qwen's explicit cache reads at $0.17 per million make it the cheaper option for agents that re-read the same repository every turn. Cheap is now a function of workload shape, not of licensing.

**Open weights and flagship releases have decoupled at Alibaba.** Qwen3.8-Max-0902 is API-only; the announcement says nothing about a downloadable checkpoint. The open Max-class artifact is Qwen3.8-2.4T-A95B, released August 12 under a custom license requiring a separate commercial agreement from model-as-a-service and AI-assistant vendors above $50 million in trailing revenue. Only the small Qwen3.8-27B — 27 billion parameters, 262K native context, shipped in mid-August, not on September 2 — carries Apache 2.0. Alibaba is using the small model as a funnel and the flagship as the toll booth.

**Cadence is now a competitive claim in itself.** Google shipped four Flash models in four months under a DeepMind leadership change that saw Demis Hassabis move to chairman and Koray Kavukcuoglu take over as SVP. Alibaba has 61 tracked models and nine in the last six months. Version numbers have stopped meaning much: Alibaba added a date suffix rather than incrementing, and Google's 3.8 arrived roughly three weeks after 3.7.

## What to Watch

Google's introductory pricing expires January 1, and a 100% increase on a model already costing 40% more per task will reprice a lot of agent economics at once. Watch whether Qwen ships open weights for the 0902 snapshot or leaves the August A95B checkpoint as the last downloadable Max. Watch for independent replication of Qwen's coding numbers on common harnesses — a jump from 11.3 to 29.0 on TerminalBench is the kind of result that either holds up or evaporates. And watch the benchmark tables themselves: Qwen's compared against Fable 5, not Fable 5.1, which Anthropic shipped the day before. On a release cadence this fast, every comparison table is stale before it publishes.
