---
headline: "Longsys Launches AIDIMM Memory Modules for Running 70B-Parameter LLMs at the Edge"
slug: longsys-aidimm-edge-ai-70b-computex
category: llms-genai
date: 2026-06-03
author: The Vault AI Staff
---

# Longsys Launches AIDIMM Memory Modules for Running 70B-Parameter LLMs at the Edge

The AI industry has spent the past two years telling everyone that the future of inference is local. At Computex 2026 in Taipei, Chinese semiconductor memory giant Longsys showed up with the hardware to prove it. The company debuted AIDIMM, a new memory module that packs up to 128 GB of capacity, a 256-bit bus, and 307.2 GB/s of bandwidth into a single compact form factor -- enough, the company claims, to reliably run large language models with more than 70 billion parameters entirely at the edge, no cloud required.

The announcement, made during the annual Computex trade show running June 2 through 5, positions Longsys at the center of an accelerating race to move AI workloads off centralized data centers and onto local devices. While chipmakers like NVIDIA and Qualcomm have dominated the conversation around edge AI processors, Longsys is making the case that memory -- not compute -- is the real bottleneck holding back local inference at scale.

## Solving the Memory Wall

Running a 70-billion-parameter model locally is not just a matter of having a fast enough processor. The model weights alone for a 70B LLM at FP16 precision consume roughly 140 GB of memory. Even with aggressive quantization techniques that compress weights to 4-bit precision, the memory footprint still lands around 35 to 40 GB -- and that is before accounting for the KV cache, activation memory, and operating system overhead that pile on during inference.

Conventional memory solutions have struggled to deliver the combination of capacity, bandwidth, and thermal stability that these workloads demand. Incomplete model loading forces systems to swap data between storage and memory, destroying latency. Thermal throttling kicks in during sustained inference runs, degrading performance. And upgrading memory in compact edge devices has historically been expensive and mechanically complex.

AIDIMM is designed to attack all three problems simultaneously. The module delivers its 307.2 GB/s of bandwidth through a 256-bit bus interface, providing the sustained throughput needed to feed model weights to the processor without creating bottlenecks. Dynamic voltage scaling between 0.9 V and 1.05 V, combined with what Longsys calls FDVFS (Fine-grained Dynamic Voltage and Frequency Scaling) power tuning, allows the module to balance performance against heat dissipation -- a critical factor in compact edge enclosures where thermal headroom is measured in single-digit watts.

"They effectively resolve common pain points including incomplete model loading, thermal-induced performance throttling, and cumbersome hardware maintenance, delivering tailored memory solutions for diverse edge AI terminals," the company stated in its official Computex announcement.

## Beyond Memory: A Full-Stack Edge AI Play

Longsys is not stopping at DRAM modules. Alongside AIDIMM, the company launched AILPBGA, a high-bandwidth memory chip designed for even more compact embedded AI inference scenarios. The AILPBGA offers 24 to 64 GB of capacity and 307 GB/s of bandwidth in a 22 x 22 mm package with native LPDDR compatibility -- small enough to fit inside robotics controllers, industrial vision systems, and autonomous vehicle compute units where every millimeter of board space matters.

The company also showcased its broader edge AI storage portfolio, powered by proprietary technologies including SPU (Storage Processing Unit), HLC (High Level Cache), and iSA (Intelligent Storage Agent). These components are designed to optimize Mixture-of-Experts model inference through expert offloading, intelligent cache scheduling, and prefetch algorithms. The goal, according to Longsys, is to make storage an active participant in the inference chain rather than a passive data repository.

"Powered by proprietary SPU, HLC, and iSA technologies, the portfolio optimizes MoE LLM inference via expert offloading, smart cache scheduling, and prefetch algorithms to resolve storage hurdles," the company said. Live demonstrations at the Computex booth showed the solutions supporting large models and long-context workloads that exceeded standard hardware specifications, while cutting DRAM usage significantly to make edge AI deployment more accessible and cost-effective.

Rounding out the lineup, Longsys displayed PCIe Gen4 and Gen5 mSSDs with highly integrated packaging and advanced thermal design. The Gen5 variant uses a compact 20 x 30 mm form factor compatible with M.2 2230, delivering sequential reads up to 11 GB/s and writes up to 10 GB/s with capacity reaching 8 TB. A specialized cooling solution using vapor chamber elements, graphene heat spreaders, and thermal interface materials extends peak performance at 11 GB/s to 181 seconds of sustained throughput -- a metric that matters far more than burst speed for AI inference workloads that run continuously.

## The Edge AI Memory Race Heats Up

Longsys is not operating in a vacuum. Micron showcased its own AI-focused memory solutions at Computex 2026, emphasizing that AI systems need memory with throughput, not just compute power. Samsung, SK Hynix, and a growing roster of memory vendors are all pivoting their product roadmaps toward edge AI applications as the market opportunity becomes clearer.

The timing reflects a broader industry shift. Enterprise customers increasingly want to run AI models locally for reasons spanning data privacy, latency reduction, regulatory compliance, and cost control. A 70B-parameter model running in the cloud can cost tens of thousands of dollars per month in API fees for high-volume applications. Running that same model on local hardware, once the upfront investment is made, drops marginal inference costs close to zero.

But the analyst community is watching with cautious optimism. As Igor's LAB noted in its coverage of the Longsys announcement, the company has presented concepts, technologies, and demos, but no independent measurements from real AI PCs or embedded systems yet. The difference between a trade show demo and sustained production deployment in thermally constrained edge enclosures is significant. Pricing, platform integration, software ecosystem support, and long-term thermal stability under real workloads will determine whether AIDIMM becomes a category-defining product or a well-engineered solution searching for a market.

## What to Watch

Longsys, founded in 1999 and listed on the Shenzhen Stock Exchange (301308.SZ), has historically been better known for its consumer storage brand Lexar than for cutting-edge AI hardware. This Computex launch signals a deliberate strategic pivot. The company is betting that the storage and memory layers -- not just processors and accelerators -- will be where the edge AI hardware wars are won and lost. For organizations planning to deploy 70B-class models outside the data center, the AIDIMM specifications suggest the memory technology is finally catching up to the ambition. Whether it ships at the right price, with the right ecosystem support, and at the right time will determine if Longsys can capitalize on what may be the most consequential hardware transition since the smartphone era.
