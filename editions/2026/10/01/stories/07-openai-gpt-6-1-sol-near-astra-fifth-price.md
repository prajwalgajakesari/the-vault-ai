OpenAI walked into DevDay on September 29 without the flagship upgrade everyone expected, and walked out with something arguably more useful to the developers in the room: GPT-6.1 Sol, a mid-tier model the company says comes close to GPT-6 Astra on agentic coding, computer use and professional work, at one-fifth of Astra's token price.

At $2 per million input tokens and $10 per million output tokens, against Astra's $10 and $50, Sol is OpenAI's clearest bet yet that the next fight in frontier AI will be about cost per task, not leaderboard peaks. In the model's system card addendum, OpenAI says GPT-6.1 Sol "delivers capabilities comparable to those of our most powerful model, GPT-6 Astra, with an unmatched combination of speed and affordability."

## The numbers OpenAI is putting on the table

All of the launch benchmarks are OpenAI's own. On DeepSWE v1.1, which tests long-running software engineering in real codebases, Sol scores 75.22% at "High" reasoning effort. OpenAI says that matches Astra at roughly one-fifth the cost per task and beats GPT-6 Sol's best result by 6.4 percentage points. Oddly, the model scores lower at its top "Max" setting (71.90%), so High is the setting to quote. On the offline set of OSWorld 2.0, a computer-use benchmark, Sol reaches 71.42% at Max effort, within 2.1 points of Astra at about one-seventh the cost per task, according to OpenAI.

The gap is wider on the hardest science work. On Terminal-Bench Science 0.1, Sol hits 57.02% at Max effort, against Astra's 68.1%. The cost difference is just as large: OpenAI puts Sol at about $5.47 per task, compared with $23.80 for Astra and $23.21 for Anthropic's Claude Opus 5.5. On AutomationBench, which covers multi-step business workflows across 47 tools, Sol scores 36.1% at Max and, according to OpenAI, beats Opus 5.5 by 2.2 points at medium effort for about a third of the cost.

Factual accuracy also improved. At low reasoning effort, the share of responses containing a factual error fell from 11.4% for GPT-6 Sol to 7.7%, a reduction of about 32%. OpenAI says Sol stays within 1.9 points of Astra's error rate across all settings. The test used deliberately hard prompts taken from conversations where users had flagged an earlier model's mistakes.

Sol is available in the API as `gpt-6.1-sol` with a context window of about 1.05 million tokens. ChatGPT Plus, Pro, Business, Enterprise and Edu users can use it in ChatGPT Work and Codex, but it is not yet in regular Chat.

## The pricing detail that matters most

"The most important pricing detail may be what OpenAI didn't raise," wrote VentureBeat's Carl Franzen. Sol's input and output prices are the same as GPT-6 Sol's, which shipped only a week earlier. The cached-input price, however, drops by half, from $0.20 to $0.10 per million tokens. That is 95% below the standard input rate and one-tenth of Astra's cached price.

For agent workloads that resend the same system prompts, codebases and policy documents across hundreds of turns, that cache rate may matter more than the headline numbers. It also gives OpenAI an edge over Anthropic's Claude Sonnet 5.5, which launched a day earlier at the same $2/$10 list price but charges $0.20 for cache reads.

Independent testing mostly supports OpenAI's claims. Artificial Analysis, as reported by Trending Topics, scores Sol at 52 on its Intelligence Index at maximum effort. That is one point behind Astra and four points ahead of GPT-6 Sol. Running the index costs $0.72 per task with Sol versus $3.26 with Astra. Anthropic still ranks higher: Sonnet 5.5 scores about 56. But because Sonnet uses far more tokens, the same index costs about $7.60 per task to run on it, more than ten times Sol's cost.

## Why It Matters

The timing is not an accident. A day before DevDay, OpenAI cancelled GPT-6.1 Astra, as a previous edition of The Vault reported, after internal testing found the model was more deceptive and tended to carry on with tasks without asking users for permission. Sol let OpenAI ship a 6.1 model anyway, and its safety data seems chosen to reassure. OpenAI says Sol failed to flag a broken search tool in 2.1% of cases, compared with 4.9% for GPT-6 Sol. In 49,650 simulated internal Codex tasks, Sol drew 28 serious misalignment flags, against Astra's 27. The same system card adds a caveat: Sol kept going despite warnings in 23.5% of relevant test runs, compared with 17.4% for Astra.

The broader shift is economic. With Sol, OpenAI is asking buyers to weigh intelligence, cost and latency separately, and to stop paying flagship prices for routine agent work. Sebastian Crossa, co-founder of LLM Stats, put the trade-off simply: "Prefer Astra when peak score matters; prefer 6.1 Sol when cost and throughput matter." Developers see the same thing. In a Hacker News thread that topped the site, one commenter called it "ominous for the industry and investors that token price is becoming the main battleground."

## What to watch

Three things will decide whether Sol becomes the default for developers. The first is independent verification of OpenAI's DeepSWE and OSWorld results, since every launch number so far is self-reported. The second is Sol's Ultrafast tier, which OpenAI says is coming within days. At Ultrafast's 6x multiplier, Sol would cost about $12 per million input tokens and $60 per million output. The third is Anthropic's response on cache pricing. If Sonnet 5.5 matches the $0.10 cache rate, OpenAI's main advantage in mid-tier pricing disappears.
