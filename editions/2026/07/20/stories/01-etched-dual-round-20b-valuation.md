# Etched Is Raising Two Rounds at Once, at $10B and $20B, and Neither Has Closed

Three weeks ago, Etched was a four-year-old chip startup that had just come out of stealth with $800 million raised and a $5 billion valuation set in December. As of last Friday, it is negotiating two separate venture rounds simultaneously — one led by Sequoia Capital at a $10 billion valuation, another led by Jane Street at roughly $20 billion — and neither one has closed.

That is not a typo, and it is not a sequence. It is two live negotiations at prices a factor of two apart, running in parallel, for a company whose first product has not yet shipped a single commercial unit.

## The two rounds

The Wall Street Journal reported the talks on July 17, in a story by Kate Clark, Anissa Gardizy and Robbie Whelan. The $20 billion round, led by existing investor Jane Street, would quadruple the $5 billion post-money valuation Etched set in an unannounced $500 million round led by Stripes that closed in December 2025. The $10 billion round led by Sequoia would merely double it. Terms on both remain subject to change, and neither had been signed as of July 17.

Back-to-back financings of this kind — selling a stake at one price, then raising again at a much higher one almost immediately — have become a structural feature of the 2026 AI funding cycle rather than an anomaly. The Journal framed the pattern as a measure of how much bargaining power the leading AI companies now hold over investors competing for allocation. When two rounds overlap at a 2x spread, the later investors are effectively paying a premium for the privilege of not being left out.

Etched was founded in 2022 by Harvard dropouts Gavin Uberti, Chris Zhu and Robert Wachen, all of whom became Thiel fellows. Its existing cap table already reads like a stress test of investor conviction: Stripes, Peter Thiel, Ribbit Capital, Primary Venture Partners, Hudson River Trading, Jump Trading, Two Sigma, and VentureTech Alliance, a fund with ties to TSMC. The angel list includes Geoffrey Hinton, Fei-Fei Li, Andrej Karpathy, Arthur Mensch, Scott Wu and Stanley Druckenmiller. Jane Street alone has put in more than $100 million to date.

## What the money is buying

The asset underneath the valuation is a chip called Sohu, an application-specific integrated circuit built to do one thing: transformer inference, the process of running an already-trained model against live queries. It is manufactured on TSMC N4P silicon and paired with 144 gigabytes of HBM3E memory. Etched says an eight-chip server can hold a 400- to 600-billion-parameter model and process more than 500,000 tokens per second on Llama 70B, against roughly 23,000 for an equivalent eight-GPU H100 server.

Two architectural choices do the work. Low Voltage Inference runs the math blocks at under half the voltage of conventional AI chips, raising FLOP density without triggering the thermal throttling that forces general-purpose silicon to downclock under sustained load. Cluster Scale Memory creates a shared low-latency pool across chips, separating weight reads from key-value cache reads — the bandwidth contention that holds GPU utilization on inference workloads to roughly 30 to 40 percent of theoretical capacity. Etched claims over 80 percent sustained utilization on trillion-parameter sparse models.

The commercial proof point investors are underwriting is $1 billion in signed customer contracts, booked before a single rack has shipped. Those are committed purchase orders, not deployed systems or recognized revenue. Etched says early customer tests show it achieving state-of-the-art throughput, latency, and power efficiency on inference workloads, but has not released numbers from them, and no independent benchmark organization has published third-party measurements from physical Sohu hardware under production conditions. First racks are due to ship this summer.

## Why this matters

Uberti has never been coy about the shape of the bet. ‘We are making the biggest bet in AI,’ he told TechCrunch in 2024. ‘If transformers go away, we will die. But if they stick around, we are the biggest company of all time.’

That binary is precisely what makes the dual-round structure interesting rather than merely greedy. A $20 billion valuation on a pre-shipment ASIC company is not a bet on execution risk being low. It is a bet that the transformer architecture is durable enough, and inference spending large enough, that specialization beats generality — and that Nvidia structurally cannot follow. Nvidia could build a transformer-only accelerator, but doing so would concede that CUDA’s programmability premium is no longer worth paying, which would accelerate the erosion of its own moat. Etched is betting on that constraint holding.

The competitive field validates the thesis even if it does not validate Etched specifically. Cerebras had the year’s first breakout IPO in May. Groq raised $650 million in June. OpenAI unveiled its first Broadcom-built custom chip. Amazon, Google and Microsoft all ship in-house silicon. Inference is where the money is going.

## What to watch

Three things. Whether either round actually closes, and at what price — a $10 billion clearing price with the $20 billion round collapsing would be a far louder signal than the headline suggests. Whether independent benchmarks from shipped racks over the next six to twelve months confirm the 80 percent utilization and 500,000 tokens-per-second figures. And whether the $1 billion in contracts converts into recognized revenue, or quietly renegotiates. Committed orders for unproven silicon are a bet by the buyer too.
