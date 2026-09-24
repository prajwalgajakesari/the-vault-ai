# Epoch AI: The Cost of a Fixed Level of AI Performance Is Falling 47% Every Quarter

In January 2025, OpenAI's o3 could score 75% on GPQA Diamond, a multiple-choice exam of PhD-level physics, chemistry and biology, for about 30 cents a question. Just under 18 months later, GPT-5.6 Luna matched that score for four hundredths of a penny. That is a 725-fold drop. According to a new report from the research group Epoch AI, it is not a one-off. It is the trend.

In "The plunging price of thought," published this week, Epoch researchers Luke Emberson and David Roodman estimate that the cost of reaching a fixed level of AI performance has fallen about **47% per quarter since 2023**, or roughly 13x per year. The authors put it bluntly: "No other general-purpose technology in history appears to have gotten so cheap so fast." By their math, the decline is four times faster than DNA sequencing, six times faster than compute, 18 times faster than lithium-ion batteries, and 54 times faster than US residential electricity over the century to 1973.

## How Epoch Measured It

Earlier studies, including a 2024 Andreessen Horowitz analysis and Epoch's own work from March 2025, tracked the *price per token* of models that could hit a given score. Epoch argues that approach broke down once reasoning models arrived. A reasoning model may be cheaper per token but burn far more tokens per answer. So this time the team measured the *actual cost to reach a score*: the cheapest model able to hit a given accuracy on a given benchmark at a given moment.

The dataset covers five primary benchmarks: FrontierMath Tiers 1-3, OTIS Mock AIME 2024-2025, GPQA Diamond, Chess Puzzles and a confidential "Mystery Game Puzzles" test. Epoch keeps that game's identity secret so labs cannot train for it. The data and code are public on GitHub.

Speeds varied by domain. Math costs fell fastest, at 50-52% per quarter (16-19x per year). Game-based puzzles fell slowest, at 39-43% per quarter (7-10x per year). On FrontierMath, the first model to clear 25% on Tiers 1-3 cost about $0.55 per attempt. Eighteen months later, GPT-5.6 Luna did it for about $0.0015, a 377x drop.

The researchers also found that prices fall fastest right after a capability debuts. Averaged across the five benchmarks, the cost of newly state-of-the-art performance falls 66% per quarter (75x per year). Two years later, the decline slows to what the authors call a "mere" 32% per quarter (4.7x per year). Their explanation is that labs can briefly charge a premium for a new frontier capability before competition and better engineering push the price down.

Epoch lists its caveats plainly. Labs may be "benchmaxxing," training toward specific tests so that scores improve faster than real-world usefulness. A good benchmark score is not the same as useful work. And because the analysis tracks the single cheapest model for every performance level, it assumes a user who switches models constantly. The authors note that real users do not, "and therefore do not reap quite the same savings." The authors say their bottom-line figures are "reasonably representative of reality" but "should not be read as exact."

## The Other Side of the Ledger

The report arrived on the same day as a much less upbeat view of AI spending. At a McKinsey Live session on the economics of agentic AI, reported by Fortune's Sheryl Estrada, senior partner Lari Hämäläinen agreed with the direction of Epoch's numbers. "Intelligence at a certain capability level is getting a lot more affordable," he said. He noted that GPT-4 launched in early 2023 at $60 per million output tokens, while GPT-4-class performance now sometimes costs well under a dollar.

Enterprise bills are rising anyway. As each unit of intelligence gets cheaper, companies are buying far more of it, mostly through autonomous agents that inspect, rewrite and retry their own work. Hämäläinen said the same agentic task can cost up to 30 times more from one run to the next. He also said vendors are keeping part of the efficiency gains as higher margins. He urged leaders to stop tracking cost per token and instead measure what a task costs, how often the agent succeeds, and how much human time it takes to check the result. His co-presenter, McKinsey Global Institute director Tanguy Catlin, offered a warning for CFOs: "The truth is, there is no single cost lever."

## Why It Matters

Epoch's paper changes how to think about AI costs. The AI boom is raising input costs, from chips to power, yet Epoch says the price of the *output* is collapsing. Economist Alex Tabarrok, writing at Marginal Revolution, took a competitive lesson from the report: frontier labs are not just building better models, they are making any given level of capability cheaper to serve. That, he argued, makes the threat from open models smaller than it looks. His summary: "Smarter and cheaper."

For companies that buy AI, the lesson is less simple. Epoch's "relentless switcher" assumption is also a piece of advice. The savings go only to organizations that can swap models as the cost frontier moves. Wharton's Ethan Mollick made that point on X, citing the paper's score-versus-cost curves as a reason not to lock workflows to today's cheapest model. McKinsey's data adds that cheaper intelligence does not produce cheaper operations by itself. Agent loops, run-to-run variance and verification time can absorb a 13x annual price cut. Teams that measure cost per successful task will see the savings. Teams that only watch per-token prices may not.

## What to Watch

The key question is whether the 66%-to-32% slowdown continues until costs level off, or whether new model generations keep resetting the curve. Watch whether Epoch extends the method to coding and agentic benchmarks. Its appendix already flags odd results on SWE-bench Verified, and those are the workloads driving enterprise bills. Also watch whether vendors pass the next round of efficiency gains on to customers or keep more of them as margin, as Hämäläinen suggested they already are.
