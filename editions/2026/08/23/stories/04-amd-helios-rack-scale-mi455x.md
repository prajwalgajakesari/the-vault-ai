The unit of competition in AI infrastructure is no longer a chip. It is a cabinet 1.2 meters wide and 44 OpenRack units tall, weighing roughly 5,000 pounds, pulling as much as 245 kilowatts through a liquid-cooled 50-volt DC busbar. On July 23 at San Francisco’s Moscone Center, AMD stopped arguing the point and shipped one.

Helios, launched at AMD’s Advancing AI 2026 conference and now in full production with partner shipments due by the end of the third quarter, is the company’s first true rack-scale system. It packs 72 Instinct MI455X GPUs across 18 liquid-cooled compute blades, each pairing four accelerators with a single 96-core sixth-generation Epyc 9006 “Venice” CPU, three 800Gbps Pensando Vulcano NICs per GPU, and a 400Gbps Pensando Salina DPU. Six switch trays carry a dozen of Broadcom’s 102.4Tbps Tomahawk 6 ASICs, and ROCm ties it together. The parts are AMD’s; the product is the rack.

For a decade AMD sold silicon into other companies’ systems. Helios is the first time it sells the system — a capability bought with the $4.9 billion acquisition of ZT Systems in 2025, whose manufacturing arm AMD resold for $3 billion while keeping the engineers.

## Inside the Rack

Per rack, AMD claims 2.9 exaflops of peak FP4, 1.4 exaflops of FP8, 31 terabytes of HBM4 and 1.7 petabytes per second of memory bandwidth, with 43 TB/s of scale-out and roughly 260 TB/s of scale-up fabric. The MI455X is a 24-chiplet assembly — eight compute dies on TSMC 2nm stacked over two 3nm fabric-and-cache dies holding 96MB of L2 apiece, plus two 3nm I/O dies, around 320 billion transistors. Each GPU carries 432GB of HBM4 across twelve 36GB stacks at 23.3 TB/s and peaks near 40 petaflops of FP4.

It has no FP64 at all. AMD stripped double precision to buy die area for MXFP4 and MXFP8, pushing scientific computing onto a separate part, the MI430X, already won into EuroHPC’s Alice Recoque and Oak Ridge’s Discovery.

Against Nvidia’s Vera Rubin NVL72 — the reference on every AMD slide — the company claims 15% more peak FP4 compute, 50% more HBM capacity, 6% more HBM bandwidth, 50% more scale-out bandwidth and up to 30% more tokens per dollar.

“Every Helios can deliver more performance for the largest models, more capacity for longer context, and the bandwidth to scale across thousands of racks,” CEO Lisa Su said during her keynote.

## The Asterisks Are Load-Bearing

The tokens-per-dollar figure is modeled, not measured. AMD’s own footnote pins it to the Kimi K2 Thinking workload at 32K input and 8K output, using projected hourly GPU pricing. The FP4 comparison sets AMD’s peak against Nvidia’s published dense NVFP4 numbers, while Nvidia markets the NVL72 at 3.6 exaflops of sparse NVFP4 — different arithmetic, argued past each other. The Register reports Vera Rubin’s adaptive compression should give Nvidia a 25% FP4 lead on inference workloads that can use it.

AMD said the quiet part out loud. Anush Elangovan, AMD’s VP of AI software, told press ahead of the keynote that the MI455X hit 20 petaflops of FP4 in real-world testing — exactly half of peak.

“It’s delivered bandwidth and flops, and it is still the best in the industry today. There is no other accelerator that I have seen that can hit that yet,” Elangovan said.

Power is another unknown. Helios draws 225 to 245 kW under load; Nvidia has published no system-level figure for Vera Rubin, and The Register estimates 240 to 250 kW. No third-party production benchmarks exist.

## Who Is Actually Buying

The demand is more concrete than the benchmarks. OpenAI expects Helios online beginning in Q4 2026, accelerating through 2027, under an arrangement including warrants for ~10% of AMD. Anthropic committed to up to 2 gigawatts of MI455X capacity, paired with an AMD investment of up to $5 billion in the model developer. Meta is validating Venice platforms and testing Helios racks under a reported $100 billion, 6-gigawatt deal. Microsoft will deploy Helios for Azure inference. Oracle, HUMAIN, TensorWave and Vultr round out the list; HPE, Lenovo and Supermicro will build the systems.

“There is nobody else in the semiconductor industry today that can offer what AMD is offering other than Nvidia,” said Ashish Nadkarni, an analyst at IDC. “They are making steady progress to be the strong No. 2 in the market.”

Matt Kimball, VP and principal analyst at Moor Insights & Strategy, called Helios a direct answer to the NVL72 line. “That is big traction,” he said of the customer roster. “You’re quietly seeing Instinct market share increase quarter over quarter, year over year, so it’s starting to establish.”

## Why It Matters

Every previous Instinct generation arrived roughly a year behind Nvidia’s equivalent, which made it the value option, not the alternative. Helios lands in the same window as Vera Rubin, at spec parity or better, with committed gigawatts from four of the five buyers who matter. That is the first time a second source has existed at rack scale — not a second chip, a second rack.

The architecture is the durable part. AMD tunnels Ultra Accelerator Link over Ethernet for scale-up, which means merchant Broadcom switches rather than bespoke NVLink silicon, and aligns scale-out with the Ultra Ethernet Consortium. A hyperscaler can swap switches and NICs without abandoning the rack design. Nvidia’s fabric bandwidth is formidable; its roadmap is also non-negotiable.

Su now expects AI infrastructure to reach $1.4 trillion by 2030, up from a $500 billion-by-2028 projection a year earlier.

## What to Watch

Benchmarks from the Microsoft Azure ramp in H2 2026 will decide whether AMD’s modeled throughput survives production workloads. Watch whether ROCm ships day-zero support for frontier models; software has been the perennial gap. Watch HBM4 allocation, which both vendors bid for from the same suppliers and which governs how fast those gigawatts arrive. And watch the clock: Nvidia’s Rubin Ultra is disclosed for 2027, and AMD’s Helios 500 answers it the same year. Any advantage here has a twelve-month shelf life.