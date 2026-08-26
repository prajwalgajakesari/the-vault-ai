Nvidia said on Aug. 24 that Groq 3 LPX, the dedicated inference accelerator it built from technology licensed from chip startup Groq Inc. for roughly $20 billion, has entered full production — formalizing one of the more consequential architectural bets in AI infrastructure. Nvidia is no longer arguing that one chip should run an entire model. It is arguing that inference has split into two jobs wanting two different silicon designs, and it has spent the price of a mid-cap company to own both halves.

Announced at Hot Chips 2026, Groq 3 LPX is what Nvidia calls an interactive AI inference accelerator, and it slots into the company's Vera Rubin platform rather than replacing any part of it. The division of labor is the whole point. Rubin GPUs handle prefill — the compute-heavy work of ingesting enormous context windows. LPX racks handle decode — the bandwidth-hungry business of generating tokens one after another, which determines whether an AI agent feels instantaneous or sluggish.

"Inference is the growth engine of AI," said Jensen Huang, Nvidia's founder and chief executive. "Vera Rubin extends that vision with workload-optimized AI factory configurations designed for the era of agentic AI, advancing the performance frontier with LPX for ultrafast token generation."

## The numbers behind the claim

Nvidia is leaning on third-party data rather than its own marketing slides. In benchmarking by Artificial Analysis, an LPX rack produced a record 3,400 output tokens per second running Gemma 4 31B, an open-source agentic model, at a 100,000-token context — the fastest figure ever recorded for that model. It was measured across 50 back-to-back requests, and throughput held roughly steady from 10,000 to 100,000 tokens of input, which matters more than the peak for agents that accumulate context as they work.

Nvidia frames that as 4x faster responsiveness than the nearest alternative platform — on the Artificial Analysis leaderboard, Cerebras, at 882 tokens per second under the same conditions. The pitch is that the gap converts into completed work: coding tasks finishing in minutes rather than hours, because faster generation lets an agent fit more reasoning steps, tool calls and verification passes into a window of time a human will tolerate.

The chip descends from Groq's SRAM-heavy dataflow architecture, which trades memory capacity for raw bandwidth. Each LPU carries just 500 MB of on-die SRAM, versus 288 GB on a top-specced Rubin GPU — a 576x gap. Nvidia compensates with scale: a full rack holds up to 256 accelerators, pooling roughly 128 GB of SRAM into a single decode engine.

## From licensing deal to shipping racks

Nvidia signed the $20 billion licensing agreement with Groq on Dec. 24, 2025 — its largest transaction on record — and brought over founder Jonathan Ross, president Sunny Madra and the bulk of Groq's staff, a structure widely read as an acquisition in all but name. Eight months later the product is in volume manufacturing.

Nebius Group is the first AI cloud to commit, planning to offer the chip through Nebius Token Factory, its production inference platform. "Generation is the phase of inference that determines how responsive an AI system actually is, and that's exactly what NVIDIA Groq 3 LPX is built to accelerate," said Danila Shtan, chief technology officer of Nebius. "As the first AI cloud bringing it to production via Nebius Token Factory, we're making sure every step of an agent's loop feels instant — through the same API developers are already using, with no migration to a new stack."

Groq's own inference cloud is expected to be among the earliest adopters. Dion Harris, a senior director at Nvidia, told reporters that a rack of 256 Groq 3 chips will be deployed at Nebius alongside Vera CPUs and Rubin GPUs and should be online later this year. For companies selling tokens, Harris said, the hardware "unlocks the ability to offer premium tiers of service for those users and those customers who actually demand the most latency-sensitive" service agreements.

Analysts have flagged caveats. The Register noted that Nvidia needs at least 64 accelerators to hit its record figure while Cerebras reaches its number on one or two, that Gemma 4 31B is a best case — a dense model fitting entirely inside a single rack — and that the comparison excludes Cerebras' newest CS-4 generation. Scaling to large mixture-of-experts models is unresolved: by The Register's math, DeepSeek V3 would require 1,342 accelerators, a little over five racks.

## Why It Matters

The demand-side case is stronger than the benchmark fight. A single agentic request consumes roughly 15 times the tokens of an ordinary chat exchange, according to OpenRouter's analysis of 100 trillion tokens of real-world usage. That ratio turns decode latency from an engineering detail into a P&L line item. If agents are the product, interactivity is the product, and interactivity is a hardware problem.

It also marks a shift in how Nvidia defends its position. For years the company's answer to specialized inference silicon was that general-purpose GPUs would absorb the workload. Groq 3 LPX concedes the opposite — and removes the most credible independent challenger from the board by buying its architecture outright. Nvidia now describes Vera Rubin as an extreme-codesign platform spanning seven chips and five purpose-built racks. The moat is no longer the chip; it is the rack, and the fact that rivals must beat an entire AI factory rather than a single part.

## What to Watch

Three things. First, whether the Nebius deployment lights up before Dec. 31; Nvidia has staked credibility on a same-year turnaround from licensing deal to live capacity. Second, whether MoE performance holds once someone benchmarks LPX on a model that does not fit in one rack — the test separating a category-defining product from a narrow win on dense mid-size models. Third, pricing. If neoclouds can genuinely sell latency as a premium tier, expect fast follows and a real market for differentiated inference SLAs. If not, $20 billion starts to look expensive for a chip that shines mainly on somebody else's 31-billion-parameter open model.
