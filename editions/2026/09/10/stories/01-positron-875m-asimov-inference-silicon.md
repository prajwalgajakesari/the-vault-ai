The most expensive component in a modern AI accelerator is the memory bolted to it, and the world cannot make enough of it. On Thursday, a startup in Reno, Nevada raised $875 million on the premise that it does not need any.

Positron AI announced a two-tranche Series C financing on September 10, 2026, closing at a $5 billion post-money valuation. The money funds the tapeout of Asimov, the company's first fully custom inference chip — a part designed from the start around commodity LPDDR5X memory instead of the high-bandwidth memory that every competitive AI accelerator depends on. Asimov tapes out on TSMC's N3P process at the end of 2026, with production targeted for the second half of 2027.

The structure of the round shows how fast sentiment turned. The first tranche, a $375 million Series C priced at a $3.5 billion pre-money valuation, was co-led by NEA, Atreides Management, Valor Equity Partners, Andra Capital and SemiAnalysis Capital, the investment arm run by analyst Dylan Patel. A follow-on Series C-1 of up to $500 million was led by NEA alongside Jim Clark, founder of Silicon Graphics and co-founder of Netscape. Other participants include DFJ Growth, the Qatar Investment Authority, Hudson River Trading and Cisco Investments. Four new directors join the board: NEA's Forest Baskett, Atreides' Gavin Baker, Thomas Jermoluk of the Jim Clark Office, and Patel.

Positron's valuation has now roughly quadrupled in seven months. The company raised $230 million in February 2026 at a $1.06 billion valuation, and closed a $51.6 million Series A only in July 2025.

## The Bet Against High-Bandwidth Memory

Positron's technical argument is that inference at scale is bound by memory capacity, usable bandwidth and power — not by peak floating-point throughput. HBM delivers enormous bandwidth, but it arrives in small capacities, requires advanced CoWoS packaging, and is rationed by three suppliers whose output is effectively sold out years ahead.

Asimov's answer is to pack ordinary LPDDR5X directly into the accelerator through a chiplet-based memory design, then extract bandwidth through placement rather than exotic packaging. The company says the chip realizes more than 90 percent of its available memory bandwidth and will ship in configurations spanning 288 GB to 2,304 GB per chip — by Positron's accounting, roughly six times the capacity of HBM-based parts at dramatically lower system cost. Because the design is power-frugal, Positron says its systems can run air-cooled as well as in liquid-cooled racks.

Asimov feeds a follow-on system called Titan, which links four to eight chips into a single node. Titan is designed to serve models beyond 16 trillion parameters with context windows beyond 10 million tokens inside one node, scaling out to thousands of nodes — aimed squarely at long-context and agentic workloads, where the key-value cache, not the model weights, is what overflows memory.

Unusually for a chip startup at this valuation, Positron already has hardware in production data centers. More than 50 racks of Atlas, its first-generation inference system, are being deployed at Oracle Cloud Infrastructure, where the provider Parasail uses that capacity to power its own inference service. Jump Trading and i3d.net are also named production customers.

Chief executive Mitesh Agrawal framed the raise as a race against the clock rather than a research program. “Speed matters in this market, both in how quickly we ship new generations of silicon and in how quickly they reach customers,” he said. “Deploying Atlas at scale taught us an enormous amount about what inference customers actually need, and we have carried those lessons directly into Asimov and Titan.”

Beyond the tapeout, the capital covers LPDDR5X supply commitments, production capacity and system integration, plus a 2-megawatt-plus engineering data center and emulation platform — the unglamorous infrastructure that separates a tapeout from a shipping product.

## Why This Matters

Positron is not the only company claiming a way around the memory wall. Industry trackers count more than 20 inference-silicon startups, among them d-Matrix, Groq, Etched, MatX and EnCharge, each attacking the problem differently. What makes Positron's bet distinctive is that it is a supply-chain bet as much as an architectural one.

Baskett, who led the round for NEA, made that explicit, pointing to the compromises HBM scarcity has forced on even the market leader. “While the rest of the industry is racing to secure scarce HBM and packaging capacity — even Nvidia's Rubin Ultra roadmap has had to scale back, from a terabyte of HBM4E down toward 192GB, simply because the supply isn't there — Positron built Asimov and Titan to sidestep that dependence altogether,” he said. “That's not incremental, that's a fundamentally different bet.”

Patel, who has spent years publicly auditing vendor performance claims, was blunt about the standard he applies. “We spend our lives measuring what AI hardware actually delivers in production, and most inference economics struggle under that scrutiny,” he said, adding that Positron addresses the real constraint without depending on HBM or advanced packaging.

There is a catch worth naming. LPDDR5X is only cheap and abundant relative to HBM today. If memory-first architectures catch on broadly, they will start competing with smartphones — and with each other — for the same DRAM output, and the scarcity Positron is dodging could follow it. Locking in supply commitments now is the hedge.

Money also cannot fix the calendar. Second-half 2027 production means Asimov launches into a market where Nvidia will have shipped two more generations, against a software stack customers have already standardized on. Atlas running inside Oracle today is Positron's strongest counterargument: evidence it can get hardware through procurement, not just fabrication.

## What to Watch

Three milestones will decide whether $5 billion was prescient or premature. First, whether Asimov actually tapes out on N3P by the end of 2026 — slips are the norm, not the exception, for a first full-custom chip. Second, whether samples arrive near the end of the first quarter of 2027 as planned, and whether realized bandwidth, latency and tokens per watt on real silicon match the slides. Third, whether the Oracle footprint grows and whether those customers commit to Titan before it exists. The next twelve months will show whether skipping HBM was insight or wishful thinking.

---

**Sources:** PR Newswire, Converge Digest, Reuters (via Yahoo Finance), The Register, Jon Peddie Research
