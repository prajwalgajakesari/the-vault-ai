Google Cloud is betting that the fastest path to next-generation AI runs straight through Nvidia's newest silicon. At Nvidia's GTC 2026 conference, the company said it plans to be among the first cloud providers to offer Nvidia's Vera Rubin NVL72 rack-scale systems, folding the successor to today's Blackwell platform into its AI Hypercomputer architecture when the hardware ships in the second half of 2026.

The move deepens an already sprawling partnership between the two firms and lands in the middle of an escalating race among hyperscalers to be first in line for Rubin, the platform Nvidia has positioned as the engine of a coming wave of reasoning models and agentic AI.

## What Google is buying

The Vera Rubin NVL72 is a full rack, not a single chip. Each system pairs 72 Rubin GPUs with 36 "Vera" CPUs, Nvidia's custom Arm-based processors carrying 88 Armv9.2 cores apiece. Every Rubin GPU ships with 288 GB of HBM4 memory, and the GPUs are stitched together with sixth-generation NVLink delivering roughly 260 TB/s of scale-up bandwidth inside the rack.

The performance claims are aggressive. Nvidia says a single Rubin package delivers about 50 petaflops of NVFP4 inference, roughly five times a Blackwell GPU, and that the NVL72 rack can hit up to five times the inference performance of the current generation while cutting cost per token by as much as tenfold. That efficiency pitch comes at a cost in power: each rack draws somewhere between 190 and 230 kilowatts, up from the 120 to 130 kilowatts of a GB300 Blackwell rack and a world away from the roughly 40 kilowatts a Hopper rack once needed.

For Google Cloud, the systems slot into AI Hypercomputer, the company's integrated stack of compute, networking, storage and software that also underpins its homegrown TPUs. Rather than force customers to choose between Google silicon and Nvidia silicon, the company is positioning Rubin as another supported option for CUDA-native training and inference alongside its TPU fleet.

## An arms race measured in gigawatts

The Google announcement cannot be read in isolation. Nvidia and OpenAI earlier signed a letter of intent to deploy at least 10 gigawatts of Nvidia systems, with the first gigawatt slated to come online in the second half of 2026 on the Vera Rubin platform. That single figure captures the scale of the buildout now underway: a gigawatt of AI compute is roughly the output of a large nuclear reactor, and OpenAI's target is ten of them.

"NVIDIA and OpenAI have pushed each other for a decade," Nvidia founder and chief executive Jensen Huang said in announcing that partnership, calling the effort "the biggest AI infrastructure project in history." OpenAI's Sam Altman framed compute as the foundational input for the entire industry, saying "compute infrastructure will be the basis for the economy of the future."

Against that backdrop, cloud providers are jockeying not just for capacity but for bragging rights. Microsoft has claimed to be the first hyperscaler to "power on" a Vera Rubin NVL72 system, validating an early rack in its lab and Fairwater data-center facilities ahead of a broader Azure rollout. Nvidia's own materials list AWS, Google Cloud, Microsoft Azure, Oracle Cloud and a roster of specialist providers including CoreWeave, Lambda, Nebius and Nscale as targeting H2 2026 availability.

Google's careful phrasing, positioning itself "among the first" rather than the first, reflects that crowded field. Being early matters because the customers who most need Rubin, the labs training frontier reasoning models and the enterprises deploying agentic systems, are the same customers cloud providers most want to lock in for the long haul.

## Nvidia's rack-scale strategy

Rubin also underscores how thoroughly Nvidia has redefined what it sells. The company no longer merely ships GPUs; it ships tightly co-designed racks built on its third-generation MGX modular design, complete with NVLink switching, networking and liquid cooling engineered as a unit. That approach makes Nvidia harder to displace and gives the hyperscalers a standardized building block they can deploy quickly, but it also cedes system-level design to Nvidia at a moment when Google, Amazon and Microsoft are all investing heavily in their own accelerators.

For Google, the calculus is pragmatic. Its TPUs remain central to its inference economics and to workloads written in JAX, but a large share of the market is built on CUDA and expects Nvidia hardware on tap. Offering Rubin lets Google compete for that business without conceding it to rivals, while its parallel TPU roadmap preserves a hedge against depending entirely on a single, supply-constrained vendor.

## What to watch

The open questions are less about silicon than about the physical world around it. Rubin racks are power-hungry and demand advanced liquid cooling, and the constraint on how fast any provider can deploy them may be electricity and data-center readiness rather than chip supply. Nvidia has already trimmed HBM4 memory-bandwidth targets after suppliers struggled to hit an initial 22 TB/s goal, a reminder that the supply chain is stretched.

If the H2 2026 timelines hold, the second half of this year will offer the first real evidence of whether Rubin's efficiency claims translate into cheaper tokens and faster training for customers, and whether Google's "among the first" positioning is enough to win share in a market where being merely fast may not be fast enough.