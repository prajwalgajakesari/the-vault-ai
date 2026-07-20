# Meta's Muse Spark 1.1 Adds a Million-Token Window and Computer Use, and Tops the Agent Benchmarks

Mark Zuckerberg had not posted on X in three years. On July 9, he broke the silence to announce a model that undercuts Anthropic and OpenAI on price while claiming the top spot on the benchmarks that measure whether an AI can actually finish a job.

Muse Spark 1.1, the first major release from Meta Superintelligence Labs since the unit was reorganized under chief AI officer Alexandr Wang, arrived with a 1-million-token context window, computer-use training across desktop, browser and mobile interfaces, and a public-preview API priced at $1.25 per million input tokens and $4.25 per million output tokens. That is roughly a quarter of what rivals charge for comparable frontier tiers. New sign-ups get $20 in free credits.

## What Meta Is Claiming

The headline numbers are agentic ones. On JobBench, a professional tool-use evaluation, Meta reports Muse Spark 1.1 at 54.7, against 48.4 for Claude Opus 4.8 and 38.3 for GPT-5.5 — the widest margin anywhere in the release. On Finance Agent v2 it posts 57.2, ahead of Opus 4.8 at 53.9, GPT-5.5 at 51.8 and Gemini 3.1 Pro at 43.0. It also leads the compared set on MCP Atlas (88.1) and Humanity's Last Exam with tools (62.1).

All of that is verifiable: the million-token window, the computer-use features and the two first-place finishes appear in Meta's published evaluation report and in independent coverage from Fortune, CNBC and a wide field of trade outlets.

What does not check out is the implication that Muse Spark 1.1 sweeps the board. It does not. On SWE-Bench Pro, Opus 4.8 leads 69.2 to 61.5. On Terminal-Bench 2.1, Muse Spark 1.1's 80.0 trails GPT-5.5 at 83.4 and Opus 4.8 at 82.7. On OSWorld-Verified — the computer-use benchmark most directly relevant to the feature Meta is advertising — Opus 4.8 wins 83.4 to 80.8. And on the harder OSWorld 2.0, a set of 108 long-horizon workflows on a full Ubuntu desktop VM, Muse Spark 1.1 scores 14.2 binary and 47.3 partial, well behind Opus 4.8 at 20.6 and 54.8. Meta is first where tools and enterprise workflows are concerned, and second or third where raw coding and desktop control are.

The context-window claim is more interesting than the raw number. Meta's pitch is not that the model holds a million tokens but that it manages them: retrieving from much earlier in a session, remembering prior actions, and compacting history in a way that preserves the steps needed later. On the computer-use side, the training goal was judgment about method — write a script when automation is faster, click when direct interaction is simpler, and emit batches of actions rather than reasoning one click at a time. The model can also delegate execution to sub-agents running in parallel.

## The Price Is the Product

Zuckerberg was unusually direct about strategy. “Our focus is on delivering strong agentic and multimodal models at very low cost,” he wrote in the X post announcing the model. Speaking to Bloomberg, he sharpened it into a competitive thesis: “Some other labs have very extreme pricing with very high margins. We believe there's an ability to deliver frontier or very high-level intelligence at a more affordable cost.”

Wang, who called the pricing “very aggressive and attractive” relative to Anthropic and OpenAI, framed the coding work as instrumental rather than central. “You kind of have to build coding capabilities as part of that in service of overall agentic capabilities,” he said.

That framing explains the benchmark profile. Meta optimized for the jobs-to-be-done evals — JobBench, Finance Agent v2, MCP Atlas — rather than for the leaderboard positions that dominate developer mindshare. It is a bet that enterprises care more about task completion than leaderboard position, and that a four-times price gap wins the argument.

## Read the Benchmarks Skeptically

There is a real caveat, and it deserves prominence. These are vendor-reported numbers, and at least one has already failed independent replication. Vals AI ran Terminal-Bench 2.1 and got 69.29, more than ten points below Meta's self-reported 80.0.

The methodology has drawn scrutiny too. Commenters on Hacker News flagged that Meta's evaluation harness allocated 6 CPU cores and 8GB of RAM per task — above the official per-task ceilings for all 89 Terminal-Bench 2.1 tasks. The benchmark's highest per-task CPU cap is 4, and only for a single task; just 8 of 89 tasks permit 8GB of RAM. Those ceilings exist to test environment awareness, so exceeding them arguably changes what is being measured.

Meta's own report is candid about the rest: for coding and agentic evals it uses competitors' self-reported figures where available and internal runs where not, and elsewhere reports the more favorable of self-reported or internally reproduced scores. It also labels third-party agentic evaluations as best-effort. That is more transparency than most labs offer, but it is still a scoreboard the home team is keeping.

## What to Watch

Three things. First, whether independent harnesses — Vals AI, Artificial Analysis, LMArena and the agentic evaluation shops — reproduce the JobBench and Finance Agent v2 leads, or whether the Terminal-Bench gap turns out to be a pattern rather than an outlier. Second, whether the price holds once the public preview ends; $1.25/$4.25 with $20 in credits is a customer-acquisition number, and Meta has no obligation to keep it. Third, availability. The API launched in preview for US developers only, and reporting suggests non-US access via OpenRouter has been restricted — a meaningful limit on a model whose main selling point is that anyone can afford to run it at volume.

The more consequential shift may be structural. Meta built its AI reputation on open weights. Muse Spark 1.1 is a closed, paid, metered API. The company is no longer trying to commoditize the model layer by giving it away. It is trying to commoditize it by underpricing everyone else.
