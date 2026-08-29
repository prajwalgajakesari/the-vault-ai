For a decade, Cerebras has sold a single stubborn idea: that the fastest way to run an AI model is to stop chopping the chip into pieces. At Hot Chips 2026 in Palo Alto this week, the company finally admitted the limit of that idea in two dimensions — and announced its plan to escape it in three.

The headline from Cerebras engineers was the CS-6, a system still two generations out on the roadmap, in which the company will stack DRAM directly on top of a wafer-scale processor for the first time. It is a substantial architectural departure. Every Cerebras wafer shipped to date has run entirely out of on-die SRAM, a design that delivers extraordinary bandwidth at the cost of capacity. Stacking DRAM vertically over the logic and SRAM wafer would let Cerebras add memory without surrendering silicon area — and, crucially, without giving up the on-wafer data locality that is its entire competitive premise.

“A wafer-scale processor already fills the largest practical area available in two dimensions,” the company wrote in its Hot Chips technical brief. “Adding substantially more memory means building upward while preserving the data locality that makes wafer scale fast.” Cerebras says it began work on the concept in 2024, and that integrating wafer-scale SRAM and compute with 3D-stacked DRAM through ultra-high-bandwidth connections should deliver ultrafast inference in what it calls an order-of-magnitude smaller system footprint.

## The capacity problem Cerebras has been dodging

The reason CS-6 matters is visible in the CS-4 spec sheet Cerebras spent most of its Hot Chips session detailing. The new WSE-3 Turbo is a genuinely absurd piece of silicon: four trillion transistors, 900,000 AI-optimized cores, 46,225 square millimeters of wafer, 250 sparse FP16 petaFLOPS, and 43.2 petabytes per second of memory bandwidth. A three-wafer CS-4 rack totals 750 PFLOPS, 129.6 PB/s of memory bandwidth, and 160.5 PB/s of aggregate fabric bandwidth.

But it carries just 44GB of SRAM per wafer — 132GB across an entire rack. Nvidia's Vera Rubin NVL72 packs 20.7TB of HBM; AMD's Helios reaches 31TB. Cerebras wins bandwidth by a factor of hundreds and loses capacity by a factor of roughly 150. Models keep growing, KV caches keep lengthening, and 300mm wafers are not getting any bigger. Cerebras has chosen to give vertically.

The near-term story is CS-4 itself, the first system built on the new Nexus rack-scale platform. Nexus reorganizes the machine into three independently upgradeable elements — compute, power, and I/O — with each wafer housed in a self-contained rear-mounted “backpack” that folds power conversion, direct liquid cooling, high-speed I/O, and control electronics into a three-dimensional package built around the wafer. Cerebras says the backpack uses 50 percent fewer components than the CS-3 assembly, relies on 60 percent more automated manufacturing, and cuts datacenter deployment from days to hours.

The performance gain comes largely from power delivery. Conventional GPU boards place AC/DC converters roughly 50 millimeters from the silicon, forcing current through layers of copper. CS-4 puts them about 0.5 millimeters away, with no printed circuit board in the final delivery path — a 100x reduction in distance that nearly eliminates board-level loss. That headroom lets Cerebras push twice as much power into the wafer, which translates into higher clocks and up to twice the performance of the WSE-3 across the board.

Cerebras chief system architect JP Fricker was blunt about the alternative, describing the roughly 5,000 internal cables in a Rubin NVL72 NVLink spine as “a mess” and contrasting them with the on-die interconnect and self-contained modules of the Nexus design. Cerebras claims 2.4 Tb/s of direct wafer-to-wafer bandwidth per wafer, 7.2 Tb/s per rack, and latency as low as two microseconds — down from five.

## Analysis

The competitive logic here is narrow and deliberate. Cerebras is not trying to win training. It is trying to own the decode half of inference, where latency is king and where its bandwidth advantage is decisive. On GPT-OSS-120B, the company claims more than 4,400 tokens per second per user, up to 30 times faster than GPU-based systems, with up to 10x more throughput per watt than CS-3.

“In AI, speed is productivity,” said CEO and co-founder Andrew Feldman. “Historically, fast inference meant using smaller and less capable models. Cerebras CS-4 delivers industry-leading speeds on the largest frontier models, fundamentally changing the paradigm.”

CTO and co-founder Sean Lie framed the payoff in agentic terms. “Being 30 times faster doesn't just make a response feel fast. It gives an agentic system room for more than an order of magnitude as much reasoning, verification, or tool use in the same wall-clock time,” he said. “That's the difference CS-4 makes for real production workloads.”

That is the bet: as agents replace chatbots, per-user token rate becomes the binding constraint on task completion time. Cerebras is also positioning for disaggregated serving, where a GPU or ASIC handles prefill and hands decode to a wafer — an arrangement it is already building with AMD's Instinct MI455X and AWS Trainium.

There is a business angle to the 3D stacking too. Trading SRAM area for stacked DRAM lets Cerebras build physically smaller processors with comparable memory, which could mean more wafer-scale engines per 300mm wafer — a real constraint for a company scaling supply against OpenAI, G42, and AWS commitments.

## What to watch

The intermediate step is CS-5, due in 2027 on the same Nexus platform, targeting up to 10,000 output tokens per second per user on open models like gpt-oss-120b, 5,000 TPS/user on multi-trillion-parameter frontier models, and 3 million tokens per second per megawatt. First CS-4 shipments begin this quarter.

CS-6 remains the harder question. Cerebras declined to disclose bond technology, DRAM capacity, stack bandwidth, or thermal strategy — and stacking memory atop a 46,000-square-millimeter processor that draws enough current to require a busbar is a thermal and yield problem no one has solved at this scale. Watch for a memory-partner announcement and for whether Cerebras names a target year. Until then, CS-6 is a direction, not a date.
