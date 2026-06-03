# Intel Debuts Xeon 6+ on 18A Process, Betting 288 Cores Can Unclog the Agentic AI Bottleneck

*Monday, June 2, 2026 | 4 min read | 870 words*

**Key Takeaway:** Intel ships its first 18A data center CPU with 288 cores targeting the structural CPU shortage that agentic AI workloads have exposed in GPU-first data centers.

---

TAIPEI -- Intel made its most consequential manufacturing bet tangible on Monday at Computex 2026, launching the Xeon 6+ "Clearwater Forest" processor family -- the first data center CPU built on its 18A process node. The flagship Xeon 6990E+ crams 288 Darkmont efficiency cores into a single socket and ships immediately through Dell Technologies, Hewlett Packard Enterprise, Lenovo, and Supermicro.

The announcement, delivered by CEO Lip-Bu Tan during a keynote alongside partners Foxconn, Siemens, and Hitachi, lands at an inflection point for the data center industry. As AI deployments shift from model training toward inference and agentic workloads -- where autonomous software agents orchestrate dozens of parallel tasks -- the CPU is reclaiming strategic importance in architectures that spent the last three years prioritizing GPU capacity above all else.

## The Agentic CPU Gap

The core thesis behind Clearwater Forest is deceptively simple: data centers built for the training era are starving for CPU cycles in the agentic era.

"Data centers that have built on GPUs for the last three years are suddenly finding they are bottlenecked by the CPU," Tim Wilson, Intel vice president and general manager of data center silicon engineering, said during a Computex roundtable. "They have a massive GPU fleet that costs billions of dollars sitting idle, waiting for the CPU to respond."

Intel estimates typical GPU utilization in agentic deployments runs between 20 and 30 percent -- not because accelerators lack capacity, but because CPUs cannot feed them fast enough. Industry analyst Ben Bajarin of Creative Strategies quantified the structural shift: while training-era data centers operated at roughly a one-CPU-per-four-GPU ratio, agentic inference changes that relationship to approximately one-to-one or less.

That math reshapes procurement priorities. If every GPU rack now needs a matching volume of CPU throughput for orchestration, task dispatch, and data movement, core density becomes a first-order purchasing criterion.

## 288 Cores, 576 MB Cache, and a Manufacturing Milestone

Clearwater Forest is architecturally dense. Twelve compute tiles fabricated on Intel 18A -- each carrying 24 Darkmont E-cores -- are stacked atop three active base tiles built on Intel 3, which house 576 MB of shared L3 cache and memory controllers. Two I/O tiles on Intel 7 complete the package, all bonded together using Foveros Direct 3D packaging and 12 EMIB bridges.

The result: a single liquid-cooled rack can deliver 36,864 cores in 32U of compute space at roughly 100 kilowatts -- what Intel calls the highest agent density available today.

Performance claims are pointed. Intel says the 6990E+ delivers 30 percent greater average performance per thread than AMD's 192-core EPYC 9965, and 55 percent better performance per watt versus its own prior-generation Xeon 6780E. Against the previous Sierra Forest flagship, the company claims 2.26x higher average throughput.

The per-thread framing deserves scrutiny. AMD's EPYC 9965 uses simultaneous multi-threading, offering 384 logical threads from 192 physical cores. Intel's 288 E-cores run single-threaded. Full-die throughput comparisons remain conspicuously absent from Intel's materials -- a gap independent benchmark labs will fill as review units ship.

## Ecosystem and Rackscale Ambitions

Tan used the Computex stage to announce rackscale AI infrastructure built with SambaNova and Foxconn, combining Xeon processors with SambaNova SN-50 Reconfigurable Dataflow Units for inference workloads. Foxconn will handle system integration and also plans a CPU-dense rack variant for workloads that skip acceleration entirely.

Vector Core Compute, a new enterprise inference cloud backed by Vista Equity Partners and Cambium Capital, demonstrated fully disaggregated inference live on stage -- using Xeon 6 for orchestration, SambaNova RDUs for decode, and NVIDIA Blackwell GPUs for prefill. Together.ai is the first commercial customer, and Vista has secured early access for its 90-plus portfolio companies serving more than 750 million users.

Strategic partnerships with Siemens for industrial edge and robotics, Hitachi for foundry tools and quantum computing, and two smaller firms -- Echo Neurotechnologies for brain-computer interfaces and Greenstone Biosciences for drug development -- round out the ecosystem play.

## Supply Constraints and Market Context

There is a catch. Intel product line director Kira Boyko acknowledged during the roundtable that 18A chip allocation is being managed "daily, in some cases" -- a signal of tight supply against strong demand. The constraint reflects competition for 18A fab capacity across Intel's product lines, including the Core Ultra Series 3 client processors already in market.

The financial backdrop favors Intel's momentum. Q1 2026 revenue reached $13.6 billion, up 7 percent year-over-year, with data center and AI revenue hitting $5.1 billion -- a 22 percent annual gain that beat Wall Street expectations. Shares have surged more than 200 percent from their 2024 lows under Tan's leadership.

But competition looms. AMD is ramping its 256-core EPYC Venice on TSMC 2nm for later this year, with a claimed 70 percent generational improvement. Intel's per-thread advantage over current EPYC may look different against next-generation Zen 6 cores.

## The Bigger Picture

Clearwater Forest matters beyond its spec sheet because it answers a question the industry has been asking since Intel began its manufacturing turnaround: can 18A ship real products to real customers on a real timeline?

The answer, as of June 2, 2026, is yes -- with caveats on volume. For data center architects facing the agentic CPU gap today, Clearwater Forest offers immediate availability through tier-one OEMs on a proven platform. Whether Intel can manufacture enough of them to meet the moment remains the open question that will define the next several quarters.

"For more than five decades, Intel, its ecosystem partners, and Taiwan have brought the world the foundational technologies for the PC, Internet, and now AI eras," Tan told the Computex audience. "Today, with the rise of inference, agentic, and physical AI, Intel is poised to bring the world new innovations from the chip to systems level."

---

**Sources:**
- [Intel Newsroom](https://newsroom.intel.com/artificial-intelligence/intel-announces-new-ai-innovations-at-computex)
- [Dataconomy](https://dataconomy.com/2026/06/02/intel-xeon-6-plus-chips-ai-infrastructure-computex-2026/)
- [Blockonomi](https://blockonomi.com/intel-intc-stock-drops-despite-computex-2026-reveals-xeon-6-and-ai-infrastructure-launch/)
- [TechTimes](https://www.techtimes.com/articles/317620/20260602/intel-xeon-6-plus-clearwater-forest-launches-288-cores-18a-node-hits-data-center.htm)
- [Tom's Hardware](https://www.tomshardware.com/tech-industry/intel-xeon-6-plus-roundtable-transcript-computex-2026)
- [Neowin](https://www.neowin.net/news/computex-2026-intel-launches-xeon-6-with-up-to-288-e-cores/)
