# Kimi K3 Is So Popular Moonshot Had to Stop Taking New Subscribers

Moonshot AI built a model good enough to top a major coding leaderboard. What it could not build fast enough was the compute to serve everyone who wanted to use it.

On Sunday, July 19, the Beijing startup did something almost no frontier lab does at the peak of a launch: it slammed the door on new customers. Just 48 hours after releasing Kimi K3, its 2.8-trillion-parameter flagship, Moonshot suspended new subscriptions because demand had outrun the GPUs it had on hand.

"Over the past 48 hours, demand has pushed close to the limits of our current capacity," the company said in a statement posted to X. "Our GPUs are feeling it." Existing subscribers were unaffected, Moonshot added, promising it was "adding capacity as fast as we can and will reopen new subscription spots in batches."

## What happened

Kimi K3 arrived late in the week of July 14 and immediately rewrote the map of open models. It is a mixture-of-experts system with 896 experts, 2.8 trillion total parameters, a one-million-token context window and native image input — by size alone, the largest open-weight frontier model anyone has released.

The benchmarks did the rest. On Artificial Analysis's independent Intelligence Index, K3 scored 57, landing it in a tie with Claude Opus 4.8 and GPT-5.5 and just behind Claude Fable 5 and GPT-5.6 Sol. On agentic tasks it punched harder: an Elo of 1668 on the GDPval-AA v2 evaluation, ahead of Opus 4.8's 1600 and GPT-5.5's 1494. And on LMArena's Frontend Code Arena — the blind, developer-voted coding leaderboard — K3 took the number one spot, a 17-place jump from its predecessor and ahead of Fable 5.

Chinese and international developers piled in. By Moonshot's own account, demand surged roughly sixfold within days, and the clusters serving K3's first-party API buckled. Many users also noticed the model ran noticeably slower than top US alternatives — a symptom of the same underlying squeeze. Moonshot says it will introduce two focused membership tiers to allocate resources more deliberately once it reopens signups.

Crucially, the company still intends to release K3's open weights by July 27, under a modified MIT license, which would make it the largest open-weight frontier model in circulation.

## Why it matters

Strip away the leaderboard drama and this is a story about the binding constraint on open AI: compute, not cleverness.

Moonshot has clearly demonstrated it can train a model that trades blows with Anthropic's and OpenAI's best. What it cannot conjure overnight is the fleet of accelerators needed to serve that model to a global audience — and Chinese labs face that wall harder than anyone, operating under US export controls that restrict access to advanced chips and chipmaking gear. A capacity pause is what happens when a frontier-grade model meets a supply chain designed by sanctions.

That tension sits underneath the July 27 open-weights drop. Releasing the weights is Moonshot's pressure-release valve: if it cannot host K3 for everyone, it can hand the model to anyone with their own hardware and let cloud providers, enterprises and rival inference shops carry the load. It is also a statement of confidence — Moonshot is giving away a model that outscores several closed US systems. CEO Yang Zhilin has signaled the company is in no rush on timing, citing more than 10 billion yuan (roughly $1.4 billion) in cash reserves.

The inference economics are the quiet twist. K3 is not the bargain-basement Chinese model of the DeepSeek era: Moonshot priced its API at $3 per million input tokens and $15 per million output — nearly four times K2.6's output price. At about $0.94 per benchmark task it still undercuts Opus 4.8's $1.80, but it is far pricier than open-weight peers like GLM-5.2 and DeepSeek V4 Pro. Serving a 2.8-trillion-parameter model is expensive, and the subscription freeze is a live demonstration that "open" does not mean "cheap to run."

## What to watch

Three things over the next week. First, July 27: whether Moonshot ships the weights on schedule, and under exactly which license terms — that determines how fast K3 proliferates beyond its own strained servers.

Second, whether third parties rush to host it. Reports have already surfaced that Microsoft is weighing adoption; broad cloud availability would relieve the capacity crunch and test real-world demand at scale.

Third, the money. Moonshot is reportedly eyeing a Hong Kong IPO within six months. A model too popular to serve is a good problem to have — but only if the compute, and the capital to buy it, arrive before the buzz fades.
