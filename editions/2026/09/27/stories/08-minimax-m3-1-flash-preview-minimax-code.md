# MiniMax Ships M3.1-Flash-Preview to MiniMax Code for High-Volume Everyday Development

MiniMax has put the first piece of its next model generation into developers' hands, and it did so in an unusual way. There was no model card, no benchmark chart and no public API price. On September 27 the Shanghai lab switched on **M3.1-Flash-Preview** inside MiniMax Code, its own coding agent, and pitched it as the fast default for routine engineering work. Developers already paying for a MiniMax Token Plan can use it now.

The company's MiniMax_Agent account announced that the model "debuts today on MiniMax Code," describing it as "built for everyday development, it's fast, reliable, and ready for real work, from quick bug fixes to full features." That post was essentially the whole launch. PANews and APIMaster.AI both reported the same positioning: the model is meant for speed and stability on routine development, from single bug fixes to complete feature builds.

## What Actually Shipped

The preview is only available inside MiniMax Code. MiniMax's main corporate account said the model runs on the existing Token Plan with no extra setup, so subscribers can pick it in the model selector without new keys or billing changes. Token Plan pricing is listed on MiniMax's developer platform. Annual Plus, Max and Ultra tiers cost **$220**, **$550** and **$1,320**, and include roughly **1.7 billion**, **5.1 billion** and **12.5 billion** M3 tokens per month.

MiniMax also added a few temporary incentives. It reset Token Plan quotas, and from September 28 through October 7 (UTC+8) users who check in daily get double credits. APIMaster.AI reports that the double credits apply to M3.1-Flash-Preview as well as H3 and H3 Max, MiniMax's video generation models.

According to reporting from Startup Fortune and APIMaster.AI, MiniMax Code offers five reasoning-effort levels with the new model: low, medium, high, xhigh and a new max tier. Startup Fortune also reports a context window of up to 1 million tokens, which matches what M3 offers. MiniMax has not published specifications for the preview itself.

The tooling around the model is open. The MiniMax Code command-line client, now at version **0.4.12**, is published on GitHub under the permissive MIT license. That means teams can inspect, fork and embed the agent harness even though the model behind it is only reachable through MiniMax's service.

APIMaster.AI warned developers against assuming there is an API route. "The UI's M3.1-Flash-Preview label is not a verified API request ID," the marketplace wrote. It added that the full M3.1 tier and the larger M3 Pro "have not been released through a public API."

## The Stealth Prelude

The launch came after a stretch of detective work by the developer community. Startup Fortune reports that four days before the release, an anonymous model called Space Bunny Alpha appeared free on OpenRouter. Developers used tokenizer comparisons to fingerprint it, and one test found a 24-out-of-24 token match with MiniMax's model family. MiniMax has not confirmed any link between the two.

Startup Fortune's Walter Schulze summed up the approach bluntly. "It's iteration speed treated as the product," he wrote, arguing that MiniMax is letting the model prove itself before worrying about the usual launch paperwork.

## The M3 Baseline

The preview builds on MiniMax-M3, the open-weight flagship released June 1. According to VentureBeat and other outlets, M3 scored **59.0%** on SWE-Bench Pro, just ahead of GPT-5.5 at 58.6% and Gemini 3.1 Pro at 54.2%, and **80.5%** on SWE-bench Verified. Several reviewers noted that M3 still trailed Anthropic's Claude Opus 4.8 by about 10 to 13 points on comparable agent evaluations. M3's API launch pricing is $0.30 per million input tokens and $1.20 per million output tokens, half of the standard $0.60 and $2.40 rates.

## Why It Matters

Speed-tier coding models are where the money is. Most agentic coding sessions are made up of many small edits, test runs and retries rather than rare hard problems. The vendor that makes those calls cheap and fast ends up with the daily usage. Putting a Flash-class model on a flat-rate annual plan measured in billions of tokens is an attempt to become the default engine for that work. It targets developers who have gotten used to watching per-token bills from Western frontier labs.

MiniMax can afford to be aggressive. The company listed in Hong Kong in January, raising $619 million, and Startup Fortune reports that its annualized revenue grew from about $100 million at the end of 2025 to $800 million by its August 26 first-half results. First-half revenue from open platform services, its API business, rose 703% to $74 million. Mainland investors put about $1.4 billion into the stock through Stock Connect in August. MiniMax now needs its developer products to justify that valuation, and a fast coding model tied to a subscription is a direct way to do it.

The quiet launch has a cost, though. Without published benchmarks, pricing or an API identifier, enterprise buyers can't easily compare M3.1-Flash-Preview with other models, and the Space Bunny Alpha episode raises questions about how openly MiniMax runs its evaluations.

## What to Watch

The next milestone is a public API release. That would bring a real model identifier, per-token pricing and a model card that confirms or corrects the community's numbers. The double-credit promotion runs through October 7, and whether usage holds up after it ends will show how much of the early adoption came from the free credits. MiniMax has also named M3.1, M3 Pro and H3.1 as separate items on its roadmap, and APIMaster.AI notes unconfirmed community reports that M3 Pro could reach roughly 3 trillion parameters. Independent benchmarks of the Flash preview, especially on SWE-Bench Pro, will decide whether MiniMax's fast release strategy gains developer trust.
