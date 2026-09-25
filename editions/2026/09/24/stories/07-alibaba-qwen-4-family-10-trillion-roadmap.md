Alibaba walked onto the Apsara Conference stage in Hangzhou this week with four new model names and no models. Qwen 4 Max, Qwen 4 Plus, Qwen 4 Flash and Qwen 4 27B were previewed on September 22 as the next generation of the company's flagship AI family, but none of them came with a release date, a price, a context window, a benchmark score or downloadable weights. What did come with a number was the roadmap behind them: Alibaba says it intends to train a model at the scale of **5 to 10 trillion parameters**, as much as three and a half times the size of the largest open-weight model in the world today.

## Four tiers, zero spec sheets

The Qwen 4 lineup keeps the tiered shape Alibaba has used since the Qwen 3 generation. Max is the flagship, positioned against the top models from every other frontier lab. Plus is the balanced middle tier with the broadest multimodal support. Flash is built for low-latency, high-volume workloads. And the 27B is the open-weight tier meant for local deployment, the direct successor to Qwen3.8-27B, a dense Apache 2.0 model that runs on a single GPU and that Alibaba CEO Eddie Wu described on stage as the most popular model among developers worldwide on desktop.

Qwen project lead Liu Dayiheng told the audience that Qwen 4 is in training on a new-generation architecture and will be released “very soon.” That is the only timing on the record. Outside observers already have a partial look at the design, however: Alibaba open-sourced Qwen3.8-Flash-Next in late August and labeled it an experimental preview of the architecture that will underpin Qwen 4. That model pairs 125 billion sparse parameters, roughly 6 billion active per step, with a separate 51-billion-parameter N-gram memory table, and Alibaba says it trained at roughly 90 percent lower cost than Qwen3.7-Plus. The conference framing positioned the new family around agentic, tool-using work rather than chat.

The benchmark Qwen 4 Max must beat is Alibaba's own. Qwen3.8-Max, generally available since August 3 at $2 per million input tokens and $6 per million output tokens, is a 2.4-trillion-parameter mixture-of-experts model with 95 billion parameters active per token, and its weights were published on August 12.

## The trillion-parameter target

The headline figure belongs not to Qwen 4 but to what comes after it. The 5-to-10-trillion band is a stated target for the Qwen 4.5 and Qwen 5 generations, and Alibaba has attached no parameter count to Qwen 4 Max itself. Wu framed the larger model in explicitly ambitious terms: it is meant to complete more complex, longer-horizon tasks and to advance the company toward artificial superintelligence, or ASI.

Wu argued that the technical path to ASI has become increasingly clear, pointing to recursive self-improvement, a loop in which models take on real-world tasks, identify their own limits, and design experiments, synthesize data and evaluate the results on their own. He said the Qwen team has made meaningful progress exploring that approach, alongside ongoing work on architecture and data optimization. He also named unified multimodal understanding and generation as a core research direction.

The keynote leaned hard on scale. Wu estimated that machine thinking accounts for less than 3 percent of all human thinking today and predicted it will eventually handle 99.9 percent. He dismissed the current wave of coding assistants as an early artifact, calling AI coding “simply the light bulb of the Machine Intelligence era.”

The compute to back those claims was announced in the same breath. T-Head, Alibaba's chip unit, unveiled the Zhenwu V900, which Wu called “the most powerful AI chip in China today” and which can be clustered up to 500,000 cards, while Alibaba Cloud set a target of more than 20 gigawatts of data center capacity by 2032. Both, along with the company's new agent platform, are covered in a separate story in today's edition.

## Why It Matters

Alibaba has become the single most important supplier of open-weight models on the planet, and every Qwen generation has reset what developers expect to run on their own hardware. That is why the least glamorous name on the slide, Qwen 4 27B, may matter most. Within days of the Qwen3.8-27B release, the community had GGUF builds, quantizations and fine-tunes, and a new 27B on a more efficient architecture would ripple through thousands of local deployments.

The trillion-parameter target is a different kind of signal. Moonshot AI's Kimi K3, released in July with 2.8 trillion parameters and open weights published later that month, currently holds the record for the largest open-weight model ever. A 10-trillion-parameter Qwen 5 would more than triple that. Whether Alibaba would release weights at that scale is an open question, but its decision to publish Qwen3.8-Max's 2.4 trillion parameters suggests the company is willing to open up even its biggest checkpoints.

There is also a geopolitical subtext. The announcements landed two days before a Trump–Xi meeting in Washington with AI on the agenda, and pairing a 10-trillion-parameter ambition with domestic silicon is Alibaba's clearest argument yet that Chinese labs can scale frontier training without unrestricted access to Nvidia's best chips. Parameter count alone has never guaranteed capability, though, and a roadmap is not a result.

## What to Watch

The first test is simple: when do the Qwen 4 weights and endpoints actually arrive? In the Qwen 3.8 cycle, the 27B weights landed about ten days after the flagship, and a public prediction market currently prices a Qwen 4 launch before November 1 at 74 percent. Watch for the license on the 27B, since the 3.8 generation shipped three different licenses across its tiers, and for whether Qwen 4 Max carries a parameter count at all. Longer term, watch whether a 5-to-10-trillion-parameter training run materializes on T-Head silicon, and whether Alibaba keeps its open-weight promise at a scale no lab has yet attempted.
