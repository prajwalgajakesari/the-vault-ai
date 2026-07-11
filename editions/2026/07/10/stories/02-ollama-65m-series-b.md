The tool that lets developers run open AI models on their own laptops just became one of the best-funded bets on where inference happens. On July 9, 2026, Ollama announced a $65 million Series B led by Theory Ventures, capping an eighteen-month stretch in which its user base doubled and a scrappy download-and-go utility quietly turned into critical infrastructure inside most of corporate America.

The round drew a deep bench of investors alongside Theory, including Benchmark, 8VC, Y Combinator, Pace Capital, 49 Palms, and GTMFund, plus a roster of angels. It brings Ollama's total funding to $88 million. The founders declined to disclose a valuation, and told TechCrunch they would not discuss revenue figures either — a notable silence for a company now sitting at the center of the open-model boom.

What the numbers do show is momentum. Ollama says 8.9 million developers now use the platform, roughly double its base in January 2026, and it is adding close to one million new installs every week. The company counts more than 67,000 community-built integrations and reports adoption inside 85% of the Fortune 500, including customers in tightly regulated sectors like government, healthcare, and finance where sending data to a third-party cloud is often a non-starter. Perhaps the most striking detail: the company has done all of this with a team of just 14 employees.

## The Local-AI Thesis

Ollama's pitch is disarmingly simple. With a single command, a developer can pull down an open-weight model — Llama, Mistral, Gemma, DeepSeek, Qwen and dozens of others — and run it locally on a Mac, Windows, or Linux machine, no cloud account required. When a workload outgrows the laptop, the same interface can scale up to larger models running in Ollama's own cloud. That "runs anywhere" promise is the crux of the investment case.

"Open models should be easy to run, easy to build with, and available wherever people need them — on your own machine, in the cloud, or both," said Jeffrey Morgan, CEO and co-founder of Ollama, who built the project with co-founder Michael Chiang.

For Theory Ventures, the thesis is about positioning. As frontier and open models converge in quality, the argument goes, the layer that actually executes the model becomes strategically valuable — a toll booth on inference rather than on training.

"As open models close the gap for most real work, the platform where AI runs becomes one of the most valuable positions in software," said Tomasz Tunguz, general partner at Theory Ventures.

The company says it will put the new capital toward three things: investing in its product and open-source developer community, scaling its cloud compute footprint, and making key hires. Given a headcount of 14 against nearly 9 million users, the hiring line may be the most consequential.

## Why It Matters

Ollama's raise lands in the middle of the defining infrastructure argument of this AI cycle: should inference happen in the cloud or on the device? For the past three years, the default answer has been the cloud, where OpenAI, Anthropic, and Google run enormous proprietary models behind metered APIs. That model is powerful but carries two persistent costs — literal ones, in the form of per-token billing that scales with usage, and privacy ones, in the form of sensitive data leaving the building.

Local inference flips both. Running a model on your own hardware means no per-token meter, no data egress, and no dependency on a vendor's uptime or usage policies. For a hospital, a bank, or a government agency, that is not a nice-to-have; it is frequently the only compliant path. Ollama's reported penetration into 85% of the Fortune 500 suggests those buyers are already voting with their installs.

The catch has always been capability. Cloud giants held a quality edge that made local models feel like a compromise. What Tunguz and Ollama are betting on is that the edge is narrowing fast — that open-weight models are now "good enough" for the majority of real work, which shifts the leverage from who trains the best model to who owns the runtime where models actually run. If that thesis holds, Ollama is not competing with OpenAI so much as sitting one layer beneath the entire ecosystem, agnostic to which lab wins.

There is a business tension baked in, too. Ollama's core product is free and open-source, the engine of its viral growth. The revenue presumably lives in the cloud tier and, eventually, in enterprise features. Squaring a beloved free tool with a venture-scale business is the same needle countless open-source companies have tried to thread, and the founders' refusal to talk revenue leaves that question conspicuously open.

## What to Watch

Three things will determine whether $65 million was a bargain or a bet. First, monetization: watch for Ollama to formalize enterprise and cloud offerings that convert its enormous free base into paying customers without alienating the developers who built the network. Second, the competitive response — hyperscalers and model labs have every incentive to blunt a runtime layer that commoditizes their APIs, and rival local-inference projects are not standing still. Third, whether the open-model quality curve keeps bending toward parity; the entire thesis rests on it.

For now, Ollama has money, momentum, and a story that fits the moment. The harder work — turning 8.9 million developers into a durable, profitable platform — starts now.
