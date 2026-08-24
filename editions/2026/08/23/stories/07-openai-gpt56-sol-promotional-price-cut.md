OpenAI cut the price of its most expensive model on Friday, August 21, and stapled an expiration date to the discount. GPT-5.6 Sol now bills $4 per million input tokens and $20 per million output, down from $5 and $30 — a 20% cut on the way in, a 33.3% cut on the way out. The rates are guaranteed at least through November 21. OpenAI has not said what happens on November 22.

The asymmetry matters more than the headline percentage. A request pays separately for what it sends and what it generates, so the real saving depends on a workload's token mix. WinBuzzer's Markus Kasanmascheff ran the arithmetic: a job burning 3 million uncached input tokens and producing 1 million output tokens cost $45 at the old rates and costs $32 now — 28.9% off. Input-heavy retrieval lands nearer 20%; output-heavy agent loops nearer a third.

The change reaches deeper than the two headline numbers. Cached input fell from $0.50 to $0.40 per million, preserving the tenfold discount for reusing a prompt prefix; cache writes fell from $6.25 to $5.00. Requests above 272,000 input tokens sit in a separate band where the whole request reprices, and that band moved too: input $10 to $8, output $45 to $30. With a 1,050,000-token context window, Sol crosses that threshold easily. Credits for ChatGPT Work and Codex qualify too; included usage on Pro, Plus and Business is untouched.

## Sol Sat Out the Last Round

Three weeks after the GPT-5.6 family shipped on July 9, OpenAI repriced most of it. On July 30 Luna dropped 80% to $0.20/$1.20 and Terra 20% to $2/$12, gains the company credited to production GPU kernel improvements and better speculative decoding — work it said came from tasking GPT-5.6 with optimizing its own runtime. Sol got Fast mode in the API instead, and kept its launch rates.

"we want to offer the best price/intelligence tradeoff at every level," Sam Altman wrote on X that day. Sol — 64.6% on SWE-bench Pro, 94.6% on GPQA Diamond, 72.7% on DeepSWE v1.1 — was evidently the level where OpenAI thought the tradeoff was already right. Twenty-two days later it wasn't. The August move brings the flagship into that sequence, but on different terms: a guaranteed window rather than a new list price.

The competitive math explains the urgency. At $4 and $20, Sol now undercuts Anthropic's Claude Opus 5 — $5 and $25 per million — on both sides of the ledger. Meanwhile Jefferies analysts led by Thomas Chong measured average enterprise inference at $1.16 to $1.18 per million tokens between August 6 and 8, the lowest reading of 2026 on an index covering commercial APIs and open-weight platforms — down from $2.04 on May 31. They tied the collapse to an "increasing emphasis on cost efficiencies" across U.S. and Chinese labs alike.

## The Divergence Is Messier Than It Looks

The tidy version of this week says OpenAI and Google cut while DeepSeek and Anthropic raised. Two-thirds of that is wrong.

DeepSeek did move hard the other way. At 16:00 UTC on August 16 it replaced flat rates with peak and off-peak billing, pushing V4-Flash output from $0.28 per million to $1.32 at peak, and V4-Pro output from $0.87 to $3.96. Increases ran from 50% to more than 1,100%. The company said the goal was "to allocate resources more reasonably" — congestion pricing, not margin repair, at least officially.

Anthropic went the opposite way from the one the calendar implied. Claude Sonnet 5 launched in June at $2/$10 as introductory pricing "through August 31," with standard $3/$15 rates due September 1. On August 11 Anthropic canceled the step-up: "We're making Claude Sonnet 5's introductory pricing permanent," the company wrote. A scheduled 50% increase simply evaporated.

Google's cut is real but landed the week before. Gemini 3.7 Flash arrived August 13 at $0.75 input and $3.75 output — half the prior Flash tier, and explicitly introductory through December 31, after which it doubles.

## Why It Matters

Strip away the direction of travel and a pattern emerges: three of the four labs are now quoting prices with expiry dates. Sol is cheap until November 21. Gemini 3.7 Flash is cheap until December 31. DeepSeek's "permanent" 75% V4-Pro discount lasted until August 16. Only Anthropic converted a promotion into a permanent rate, and it did so by declining to raise prices rather than by lowering them.

That is what a promotional cut signals about unit economics. A permanent price reset is a claim about serving cost — we made inference cheaper, here is the durable number. A three-month window is a claim about demand. It says the lab wants share on its frontier tier now, at a margin it has not committed to defending in Q1. OpenAI attributed July's Luna and Terra cuts to specific engineering wins and made them permanent. It has attributed Friday's Sol cut to nothing in particular and made it temporary. Read the difference.

For buyers, per-token list price has become the least stable input in a budget model. Zack Kass, OpenAI's former go-to-market chief, framed the demand side bluntly to Axios: "At some point, the next model doesn't matter to you." When capability converges, price is the differentiator — and when price itself is provisional, cost per completed task on your own workload is the only figure that survives contact with an invoice.

## What to Watch

November 21 is the date to diary. If Sol's $4/$20 becomes the list price, OpenAI has genuinely moved frontier serving costs down and the July efficiency story extends to the biggest model. If it snaps back to $5/$30, the promotion was a share grab timed against Anthropic's Sonnet 5 lock-in and Google's Flash discount, and Q4 budgets built on it need rewriting. Watch also whether Amazon Bedrock's matching Sol reduction carries the same November cliff, and whether Jefferies' index keeps falling — because if inference prices keep sinking while every frontier discount is scheduled to expire, somebody's math is wrong.
