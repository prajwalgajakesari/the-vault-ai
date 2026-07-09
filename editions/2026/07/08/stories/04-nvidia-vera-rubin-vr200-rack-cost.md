The price of a seat at the frontier of artificial intelligence just doubled.

A Morgan Stanley Research analysis making the rounds in early July puts the fully built cost of Nvidia's next-generation Vera Rubin "VR200" NVL72 rack at roughly $7.8 million per unit for the hyperscale cloud providers that will buy them by the thousand. That is nearly double the roughly $4 million those same buyers pay today for a GB300 NVL72 rack built on the current Blackwell generation. The bank's estimated bill of materials lands at a precise-sounding $7,803,148 — a number that has become shorthand this week for how expensive frontier compute has become.

The rack is a dense slab of silicon: 72 Rubin GPUs and 36 Vera CPUs, arranged as 36 "Superchip" boards inside Nvidia's familiar Oberon chassis. Each Rubin GPU carries 288 GB of HBM4 and, according to Morgan Stanley, will sell to hyperscalers at about $55,000 apiece in volume — up 57% from the Blackwell generation and enough to push the GPUs alone to nearly $4 million per rack, the single largest line item. The Vera CPUs add roughly $180,000, or about $5,000 each.

## Memory Is The Story

The eye-catching figure is not the GPUs. It is the memory.

Morgan Stanley pegs memory content at about $2 million per VR200 rack, or roughly 25% of the total system cost — a 435% jump from the $373,939 of memory inside a GB300 NVL72. Two forces drive the surge. First, each rack now packs 54 terabytes of LPDDR5X, a threefold increase over the 17 TB in a GB200 machine. Second, the VR200 introduces roughly $1 million or more of 3D NAND storage, a component that was virtually absent from the prior generation.

All of this arrives during the worst memory-supply crunch in a decade. Contract DDR5 prices now run between $12 and $16 per gigabyte, with spot prices near $20, and LPDDR5X — installed on the expensive SOCAMM2 modules that Nvidia's Vera CPUs require — costs more still.

"$2 million of memory content per Vera Rubin NVL72 rack is not something completely unexpected: the system uses a lot of LPDDR5X and 3D NAND memory, and memory now comes at massive prices," wrote Anton Shilov of Tom's Hardware, walking through the SemiAnalysis pricing figures underpinning the estimate. At $8 per gigabyte, the LPDDR5X alone runs about $408,000 per rack; at $10, closer to $540,000 — before Nvidia adds its own markup.

Memory is not the only component reflating. Morgan Stanley's breakdown shows the printed circuit board cost jumping 233%, from $35,100 in Blackwell to $116,730 in Rubin, with NVLink switches, networking silicon, ABF substrates, MLCC capacitors, cooling, and power supplies all climbing. Add it up and the GPUs, CPUs, and memory total about $6.14 million, with the remaining roughly $2 million spread across everything else in the box.

"Vera Rubin is poised to deliver unprecedented performance at a grand price, reinforcing NVIDIA's dominance while underscoring the rising cost of pushing the frontiers of AI," wrote Wccftech's Hassan Mujtaba in his read of the Morgan Stanley note.

Nvidia has confirmed Vera Rubin is in production, with first shipments due in the third quarter of 2026 and volume ramp in the fourth — meaning the $7.8 million rack is not a distant forecast but a purchase order landing this year.

## Why It Matters

The VR200 is the machine expected to train the model generation after today's flagships — the successors to GPT-5.6 Sol, Claude Fable 5, and Gemini 3.5 Pro, widely understood to be GPT-6, Claude Mythos 6, and Gemini 4. A frontier training run is measured in tens of thousands of these racks. At $7.8 million each, a 10,000-rack cluster is a $78 billion hardware commitment before power, real estate, or networking beyond the rack — nearly double what the same cluster count would have cost on GB300.

That math concentrates the field. The doubling of per-rack cost widens the moat around the handful of players — Microsoft, Google, Amazon, Meta, and the largest AI labs backed by them — that can absorb capital outlays at this scale. It is a squeeze that has already surfaced in earnings: Microsoft recently attributed $25 billion of its AI budget to memory and chip costs, and analysts now expect memory to consume roughly 30% of all hyperscaler data-center spending this year, a fourfold jump from 2023.

The shift also rewrites who captures the value inside the box. As memory climbs toward a quarter of system cost and other components inflate, Nvidia's GPUs — still the most expensive line item — represent a shrinking share of the total, handing more of the AI hardware windfall to memory makers like SK Hynix, Samsung, and Micron.

## What To Watch

Three things. Whether memory prices — already described in some reports as shifting on an hourly basis — climb further and push realized rack costs above Morgan Stanley's $7.8 million estimate, closer to the $8.8 million figure Nvidia's supply chain floated in March. Whether hyperscalers respond by leaning harder into their own custom silicon to blunt the cost. And whether the economics of GPT-6-class training still pencil out once the compute bill nearly doubles — the first real test of whether frontier AI's spending curve can keep bending upward.
