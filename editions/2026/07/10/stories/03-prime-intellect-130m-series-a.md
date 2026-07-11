Prime Intellect, the San Francisco startup that has spent two years arguing that frontier AI does not have to be built inside the walls of a handful of hyperscaler-funded labs, now has $130 million and a unicorn valuation to prove it. On July 8, 2026, the company announced a Series A led by **Radical Ventures**, with participation from NVIDIA Ventures, Intel Capital, Dell Technologies Capital and its existing backers. The round values Prime Intellect at roughly **$1 billion** and lifts its total funding past **$150 million**.

The raise is one of the largest to date for a company built on a contrarian premise: that state-of-the-art models can be trained not on a single tightly-coupled supercluster, but across GPUs scattered around the world and stitched together over ordinary internet links. Prime Intellect calls the resulting platform an "open superintelligence stack" — a full pipeline spanning compute access, large-scale reinforcement learning, sandboxes, evaluation environments and deployment.

"It shouldn't just be a few nerds in a glass tower in San Francisco that have the capability to train AI models," co-founder and chief executive Vincent Weisser said, describing the thesis behind the company. "It should be every enterprise, every nation state."

## The decentralized training bet

Prime Intellect has spent the past 18 months turning that slogan into working systems. In late 2024 it released **INTELLECT-1**, a 10-billion-parameter model it billed as the first decentralized training run of a large language model at meaningful scale. It followed with **INTELLECT-2**, a 32-billion-parameter model trained through globally distributed reinforcement learning, and more recently **INTELLECT-3**, a 106-billion-parameter mixture-of-experts model.

The technical trick that makes geographically-spread training viable is bandwidth reduction. Using an approach based on DiLoCo and a custom int8 all-reduce, the company says it cut the communication required between nodes by roughly **400 times** versus conventional data-parallel training, while delivering comparable model quality. Layered on top are fault tolerance for node failures, the ability to run on cheaper spot instances, and the flexibility to add or drop compute mid-run — features that matter when your cluster is a patchwork of machines rather than a single owned data center.

That combination has attracted a paying customer base faster than most infrastructure startups. Prime Intellect says it now works with more than **6,000 customers** — a mix of AI startups, newer labs and enterprises — and reached over **$100 million in annualized revenue** in under a year, a striking figure for a company selling training infrastructure rather than a consumer app.

## Owning the model, not renting it

The pitch increasingly aimed at enterprises is that reinforcement learning has changed who can build frontier-quality AI. Pre-training concentrated capability inside a few labs; RL, the company argues, lets a company train directly on its own product and workflows and own the optimization loop rather than wait on the next release from a closed vendor.

Payments company Ramp is the showcase example. Working on Prime Intellect's platform, Ramp trained a 35-billion-parameter model for spreadsheet search that, by its own account, beat a frontier Anthropic model on accuracy while running faster and far cheaper.

"Rather than wait on a better frontier model, we trained our own for the workflow that mattered to us," said Karim Atiyeh, Ramp's co-chief executive, describing the project. Other named users include Zapier and the startup Flapping Airplanes, and the angel roster on the round reads like a who's who of the current AI build-out, including Aravind Srinivas of Perplexity, Aaron Levie of Box, Cloudflare's Matthew Prince and Harvey's Winston Weinberg.

Prime Intellect says the new capital will go toward scaling its distributed compute clusters, funding larger RL runs, and pushing research into what it calls Recursive Language Models — systems designed to manage their own context and coordinate sub-agents over long horizons — plus continual-learning infrastructure in which training and inference collapse into a single loop.

## Why It Matters

The dominant story in AI infrastructure has been one of concentration: enormous capital, exclusive access to the newest NVIDIA silicon, and single sites drawing gigawatts of power. Prime Intellect is a direct wager against that model. If frontier-class training can be spread across pooled, commodity, even spot-priced GPUs, the moat that centralized hyperscalers have dug — access to a specific kind of tightly-networked cluster — becomes far less decisive. The investor list underlines the tension: NVIDIA, Intel and Dell all backed a company whose core promise is to make training less dependent on owning the biggest, most expensive cluster. For enterprises weary of building strategy atop a closed vendor's roadmap, "train a model you actually own" is a genuinely different value proposition, and $100 million in run-rate suggests it is more than a slogan.

## What to Watch

The open questions are about scale and durability. Prime Intellect's largest models remain well below the trillion-parameter tier of the closed frontier, and it will need to show that decentralized methods hold up as runs grow. Watch whether its Recursive Language Model and continual-learning bets produce shipped systems or stay research previews, whether the 6,000-customer base converts into durable enterprise contracts, and how the closed labs respond as more companies decide that renting intelligence is no substitute for owning it.
