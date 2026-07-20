# Grok 4.5's Real Claim Isn't the Score — It's Doing the Same Work With a Quarter of the Tokens

The most important number in SpaceXAI's Grok 4.5 launch is not 83.3%. It is 15,954.

That is the average number of output tokens Grok 4.5 burns to resolve a SWE-Bench Pro task, according to xAI's own launch materials — against 67,020 for Claude Opus 4.8 running at max settings. A 4.2x gap. Roughly a quarter of the tokens for work in the same neighborhood. Artificial Analysis, the independent benchmarking firm that engineering teams increasingly treat as a neutral referee, replicated the efficiency advantage rather than merely repeating it from the press release.

Meanwhile the benchmark score everyone quoted — 83.3% on Terminal-Bench 2.1 — puts Grok 4.5 in third place. GPT-5.5 (xhigh) scores 83.4%. Anthropic's Fable 5 (max) scores 84.3%. Grok loses by a tenth of a point and a full point respectively. On a leaderboard, that is a loss. On an invoice, it is noise.

## What actually shipped

Grok 4.5 launched July 8, 2026, jointly developed by SpaceXAI and Cursor, which SpaceX acquired for $60 billion in all-stock less than a month before the model shipped. Cursor's launch post confirms the architecture and the training data: "Grok 4.5 is a mixture-of-experts model that we trained jointly with SpaceXAI," the company wrote, and "training included trillions of tokens of Cursor data which capture a wide-range of user interactions with codebases and software tools."

The 1.5-trillion-parameter figure attached to the underlying V9 foundation model is worth flagging as contested. It does not appear in either company's official launch materials; it traces to Musk's own posts and secondhand reporting, and should be treated as self-reported rather than confirmed.

Pricing is where the story gets structural. Grok 4.5 costs $2 per million input tokens and $6 per million output. Opus 4.8 runs $5/$25. GPT-5.5 sits at $5/$30. Fable 5 charges $10/$50. Stack the two advantages — roughly 4x cheaper output tokens and 4.2x fewer of them — and you get Artificial Analysis's Coding Agent Index numbers: $2.49 per task for Grok 4.5 in Grok Build, versus $5.07 for GPT-5.5 in Codex and $11.80 for Fable 5 in Claude Code. Grok averaged 1.9 million total tokens per task against GPT-5.5's 6.2M and Fable 5's 7.2M.

Elon Musk framed it on X the day of launch: "It is an Opus-class model, but faster, more token-efficient and lower cost." He narrowed the claim in a follow-up post the same day — Grok 4.5 is "roughly comparable to Opus 4.7, but much faster" — which is a materially more defensible statement, and one the independent data broadly supports.

## Why token efficiency is becoming the real battleground

For two years the industry competed on a single axis: can the model do the task at all. That question is mostly settled at the frontier. Four labs now cluster within a few points of each other on the hardest agentic coding evals. What differentiates them is what it costs to get there — and that cost is increasingly dominated by tokens consumed, not tokens priced.

This is a consequence of agents. A chat turn is a few thousand tokens. An agentic coding session is a loop: read files, run tests, read the failure, revise, re-run. Every wasted reasoning step multiplies across the loop. A model that reaches the same fix in half the steps does not save you 50 percent — it saves you 50 percent compounded across every retry, every subagent, every parallel run. xAI put this explicitly in its training writeup, saying it "scaled reinforcement learning with a strong focus on per-token intelligence" and that the model solves tasks "in under half the number of steps."

The market is already pricing this in. Cursor CEO Michael Truell said Grok 4.5 had "become the daily driver for many on our team" — a notable signal from the company best positioned to know the model's limits, even accounting for the obvious ownership conflict.

The caveat matters, and AIToolsRecap put it bluntly in its review: "The token efficiency advantage only matters if Grok 4.5's outputs are correct — token-efficient wrong answers cost less but produce worse results." Grok 4.5 trails Opus 4.8 on SWE-Bench Pro (64.7% vs 69.2%) and on the neutral-harness DeepSWE 1.1 (53% vs 59%). A cheap failure that a human has to redo is not cheap. Efficiency per task is only meaningful once you normalize by completion rate.

Two more asterisks. Cursor disclosed in a footnote that "an earlier snapshot of the Cursor codebase was accidentally included in training," and pulled its own CursorBench score rather than publish a number it could not vouch for. And Artificial Analysis measured Grok 4.5's hallucination rate at 54 percent, up from 25 percent for Grok 4.3 — the model knows more, and is also more confident when it is wrong.

## What to watch

Three things. First, whether rival labs start publishing tokens-per-task alongside accuracy. The metric only becomes a battleground once everyone is forced to report it. Second, whether Grok 4.5's efficiency holds outside benchmark harnesses, on messy real repositories where the cheap path is often the wrong one. Third, the 500K context window — a step down from Grok 4.3's 1M — which quietly caps exactly the large-codebase workloads where per-task economics matter most.

Benchmark scores at the frontier were always going to converge. The bill is what teams will actually choose on.
