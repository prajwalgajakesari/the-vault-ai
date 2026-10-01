# Google Launches Gemini 4 Argon, Its First Gemini 4 Frontier Model, Defender-First and Tied With GPT-6 Astra

Google is back at the frontier, but most people will have to wait to use it. On Wednesday the company unveiled Gemini 4 Argon, its first frontier model in more than seven months and the first in the Gemini 4 family. Argon goes first to a small group of cybersecurity defenders, not to the public. Independent testers already rank it level with OpenAI's GPT-6 Astra. It also posts a far lower hallucination rate than its rivals and launches at a fraction of their per-token price.

In a post on X, Google CEO Sundar Pichai said Argon "shows frontier performance in complex workflows, cyber defense and software engineering. Teams are using it extensively at Google, from coding to quantum computing, great feedback." Google's Logan Kilpatrick struck a similar note: "Introducing Gemini 4 Argon, our new frontier model, rolling out to cyber defenders starting today, and more widely as soon as possible."

## A defender-first rollout and a million-token output

Argon's first users are "trusted cyber defenders" in Google DeepMind's Fairwind Program. They and Google's internal teams get the model without cyber guardrails. Google says Argon was trained specifically for defensive security work and can "autonomously find, validate, and patch critical software vulnerabilities." On CWE-bench v1, which measures how well a model fixes security flaws, Google says Argon ties for first place at 68 percent. Google is also taking part in the U.S. government's voluntary program that gives agencies access to new models before public release. Paid API customers and Google AI Ultra subscribers come next. Google has not given a date beyond "as soon as possible."

The biggest technical change is output length. Argon can now generate up to 1 million tokens in a single response, up from 64,000 in the previous generation. Its input context window stays at 1 million tokens. Google's case is that a model with room to reason across hundreds of thousands of tokens can solve hard problems in one pass. To keep those long runs from timing out, the Gemini API adds a "Long Decode Continuation" feature that pauses a long response and resumes it through follow-up requests.
Pricing is aggressive, at least for now. Argon launches at an introductory $2 per million input tokens and $10 per million output tokens. Cached input is 95 percent cheaper, roughly 10 cents per million. When the introductory period ends, the price doubles to $4 and $20. Even at the full rate, that is well below GPT-6 Astra's listed $10 input and $50 output.

Google says thousands of its own employees already use Argon. In one internal project, teams of Argon agents analyzed profiling data from Google's server fleet and applied memory optimizations that freed more than 300 TiB of memory. Other agents are migrating C and C++ codebases to Rust. In a blog post, the company said Argon is "fundamentally changing the way we work and build at Google."

## What the independent numbers say

Google's own benchmark charts show Argon leading most tests, some by wide margins. Outside evaluators are more measured, though still broadly positive. On the Artificial Analysis Intelligence Index, Argon at its "High" reasoning setting scores 53. That ties GPT-6 Astra and Anthropic's Claude Fable 5.1, puts it one point ahead of GPT-6.1 Sol, and is 23 points above Google's previous frontier model, Gemini 3.1 Pro Preview. Anthropic still leads overall, with Claude Opus 5.5 at 58 and Claude Sonnet 5.5 at 56.

Agentic work, a long-standing weak spot for Gemini, improved the most. Argon ranks first on Artificial Analysis's AutomationBench-AA at 77.5 percent, six points ahead of Claude Sonnet 5.5. It scores 57 percent on Terminal Bench 4, a 53-point jump over Gemini 3.1 Pro Preview, though still behind Sonnet 5.5, Opus 5.5 and GPT-6 Astra.

The standout figure is reliability. On AA-Omniscience, which tests whether a model admits what it does not know, Argon's hallucination rate is 15 percent, against 51 percent for GPT-6 Astra and 54 percent for GPT-6.1 Sol. Artificial Analysis calls it the lowest rate of any model scoring 45 or higher on its index. There is a trade-off: Argon's raw accuracy on the test is only 50 percent, 13 points below Astra.

Human raters like it too. Argon (High) took first place in Arena's Text Arena with 1,525 points, 20 points ahead of Claude Opus 4.6. It ranks a more modest eighth in Code Arena's WebDev leaderboard. Vals AI also puts Argon first on its Vals Index at 68.9 percent, the first time a Gemini model has topped it.

## Why it matters

Argon ends a rough stretch for Google DeepMind. The company skipped its already-announced Gemini 3.5 Pro frontier model, and for most of the year it shipped nothing above the Flash class. Artificial Analysis now says Google is back among the top three labs.

The defender-first rollout matters as much as the benchmarks. By putting an unguarded version in front of security teams before developers or consumers, Google is treating offensive-cyber risk as the main deployment constraint, a stance rivals have also edged toward. Its participation in Washington's voluntary pre-release review gives the approach a policy dimension.

The cheap pricing needs a caveat. Artificial Analysis found that Argon uses about 62,000 output tokens per index task, compared with 27,000 for GPT-6 Astra. At the promotional price, a task costs about $1.99, roughly 60 percent of Astra's cost. Once the discount ends, that rises to $3.98, about 20 percent more than Astra. Buyers should budget on the full price, not the introductory one.

The open questions are timing and duration. Google has not said when paid API and Ultra access will open, or how long the introductory pricing will last. Watch for how quickly Fairwind feedback turns into general availability, whether real-world coding results match the benchmark charts, and how OpenAI and Anthropic respond to a rival that undercuts them on token price and hallucinates far less often.
