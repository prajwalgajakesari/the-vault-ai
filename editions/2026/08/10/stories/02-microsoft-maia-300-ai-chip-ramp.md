# Microsoft Ramps Up Its Maia 300 AI Chip, Ordering Over 300,000 Units From TSMC

Microsoft is preparing to scale its homegrown silicon program to a level it has never attempted before. On Monday, August 10, 2026, reports surfaced that the company plans to significantly ramp production of its next-generation Maia 300 AI accelerator, with an unveiling expected as early as next month and negotiations underway with Taiwan Semiconductor Manufacturing Company (TSMC) to secure capacity for more than 300,000 units by 2027.

The move, first reported by *The Information* and confirmed across multiple trade outlets, marks the most aggressive push yet in Microsoft's multi-year campaign to reduce its dependence on Nvidia's costly GPUs for the AI workloads running across Azure. If Microsoft hits its targets, the Maia 300 would represent a step-change from the tens of thousands of prior-generation chips the company has produced to date.

## From a slow start to a full-throated ramp

Microsoft's silicon story has been one of ambition tempered by delays. The company shipped its first Maia chip in November 2023 and then, by its own analysts' accounting, fell behind rivals in scaling custom hardware. Amazon has pressed ahead with Trainium and Inferentia, and Google Cloud has seen strong uptake on its Tensor Processing Units, which were used to train its Gemini models.

The Maia 200, unveiled in January 2026, was the reset. Built on TSMC's 3-nanometer process, it packs more than 140 billion transistors, pairs 216GB of HBM3e memory running at 7 TB/s with 272MB of on-chip SRAM, and delivers over 10 petaFLOPS of 4-bit (FP4) compute within a 750-watt envelope. Microsoft designed it explicitly for inference — the high-volume business of serving models to users — rather than training. In its launch blog, the company claimed the chip is "the most performant, first-party silicon from any hyperscaler, with three times the FP4 performance of the third generation Amazon Trainium, and FP8 performance above Google's seventh generation TPU."

The Maia 300 is the next rung. Andrew Wall, general manager of Azure Maia, told Techzine that the 300-series is expected to arrive sometime in 2027, while the Maia 200 is likely to remain in service for another four to five years — a signal that Microsoft intends to run a broad, long-lived fleet rather than churn through generations. The reported order of 300,000-plus units is a manufacturing commitment on a scale that puts Microsoft in the same conversation as Amazon's half-million-chip Trainium clusters.

## Why it matters: the vertical-integration play against Nvidia

The strategic logic is straightforward. Nvidia commands the overwhelming majority of the AI accelerator market, and its GPUs are expensive and supply-constrained. Every hyperscaler that designs its own chip is trying to claw back margin, control its own roadmap, and insulate its capacity from a single vendor. Microsoft has been one of the largest contributors to Nvidia's revenue, which makes its pivot toward first-party silicon especially consequential.

"Microsoft is back at it — custom silicon for AI — after taking an almost 3 year break," said Holger Mueller, an analyst at Constellation Research. "Microsoft has had a big role fueling Nvidia's financials. Maia 200 hits all the right numbers from performance, memory, liquid cooling and the cloud infrastructure to support it. Now it is all about the rollout speed across the Azure data center landscape."

That last point is the crux. Designing a competitive chip is one thing; deploying hundreds of thousands of them across global data centers, with a mature software stack, is another. Microsoft is positioning Maia for inference precisely because that is where volume and cost pressure are greatest as Copilot, Microsoft Foundry, and its Superintelligence team consume ever more compute. Better performance-per-dollar — Microsoft claims Maia 200 offers 30% better economics than its current fleet hardware — compounds fast at that scale.

Crucially, the story is not a clean break from Nvidia. Like Amazon and Google, Microsoft continues to buy enormous volumes of Nvidia GPUs even as it builds an alternative. The custom-silicon push is less an escape hatch than a hedge: enough in-house capacity to gain leverage on price and supply, without abandoning the ecosystem that still runs most frontier training.

## The Anthropic question

One of the more intriguing threads is demand beyond Microsoft's own walls. Reports indicate Microsoft wants to persuade major AI labs to adopt Maia, with Anthropic named as a prospective customer. That would be a notable validation — Anthropic already runs Claude models on Amazon's Trainium and Google's TPUs — and it hints at Microsoft's ambition to make Maia a merchant-grade platform rather than a captive one. Winning external customers is the difference between a cost-savings project and a genuine competitor in the accelerator market.

## What to watch

- **The September unveiling.** Microsoft is expected to formally reveal Maia 300 as soon as next month. Watch for specifications — particularly memory capacity, interconnect bandwidth, and whether the chip extends beyond inference toward training.
- **Whether the TSMC order firms up.** The 300,000-unit figure reflects negotiations, not a signed guarantee; component supply and TSMC's constrained 3nm-class capacity could cap the ramp. Some reports suggest Microsoft's longer-term ambition reaches beyond one million units.
- **External adoption.** Any confirmed commitment from Anthropic or another major lab would signal that Maia has crossed from internal tool to market contender.
- **Rollout speed.** As Mueller noted, execution across the Azure footprint — not benchmarks — will decide whether Microsoft's silicon bet pays off.

For now, the message from Redmond is one of intent: after a slow start, Microsoft is committing real manufacturing volume to the idea that the future of Azure AI runs, at least in part, on chips it designed itself.
