# Optical-Networking Startup Lumilens Raises $700 Million at a $5.5 Billion Valuation

Lumilens, a two-year-old startup building optical gear to move data through AI data centers on beams of light rather than electrical signals over copper, emerged from stealth on August 6 with more than $700 million in fresh funding and a $5.51 billion valuation. The round, first reported by The Wall Street Journal, lands as the AI industry’s most valuable resource shifts from raw compute to the wiring that stitches processors together, and it vaults a previously invisible company into the center of one of the buildout’s hardest problems.

The San Jose-based company said the new financing brings its total capital raised to more than $900 million. Just as striking as the valuation is the traction behind it: Lumilens is already shipping its first product into a hyperscaler’s production data centers under what it described as a multibillion-dollar customer agreement, reached only two years after the company was founded in early 2024.

## Inside the Round

The Series C was co-led by Atreides Management, Bain Capital Ventures, Meritech, Seligman Ventures and Spark Capital, with a long roster of additional backers including Addition, Alkeon, HarbourVest, J.P. Morgan Private Capital, Mayfield, Qualcomm Ventures, Peak XV and Redpoint Ventures. Spark had led the company’s Series B in early 2025 and returned to co-lead the C, while Mayfield has backed founder Ankur Singla since the seed round.

Singla is a repeat infrastructure founder. His two previous startups, Contrail Systems and Volterra, were acquired by Juniper Networks and F5 respectively, for a combined sum reported at roughly $676 million. At Lumilens he is joined by CTO and co-founder Ted Schmidt, a former Juniper distinguished engineer who helped build that company’s silicon photonics work following its 2016 acquisition of Aurrion. The leadership bench also draws from Cisco, Meta, Marvell, Lumentum and Coherent.

“The constraint on AI has shifted from how many GPUs you can buy to how many you can connect,” said Ankur Singla, founder and CEO of Lumilens. “Whether they’re training frontier models or serving them to hundreds of millions of users, hyperscalers told us they need the same two things: far more optical capacity for the networks they run today, and a path to directly connecting thousands of GPUs together into a single cluster. We built Lumilens to deliver both.”

## Two Bottlenecks, One Platform

Lumilens targets both of the places where data-center networks are straining. The first is the scale-out fabric that ties racks and rows of GPUs together, where the company sells pluggable optical transceivers rated at 800 gigabits and 1.6 terabits per second and beyond. The second is the scale-up fabric inside a rack, where GPUs are wired directly to one another. There, the company is developing near-package and co-packaged optics (NPO and CPO) that bring optical input-output directly to the processor.

The scale-up problem is rooted in physics. At the data rates AI demands, electrical signals travel only about a meter and a half over copper, effectively capping a tightly coupled domain at a single rack and a few hundred GPUs. Roadmaps that call for thousands, or eventually tens of thousands, of processors acting as one machine require replacing copper with photonics. All of the company’s products are built on a single in-house platform it calls LumiCore, which spans silicon photonics, mixed-signal chips, electrical-optical interposers and optical systems.

The scale-out numbers are equally daunting. Lumilens cites McKinsey projections that 800G transceiver production could fall 40 to 60 percent short of demand through 2027, with 1.6T shortfalls of 30 to 40 percent persisting through 2029. A single 400,000-GPU data center, the company notes, needs more than 2.4 million transceivers and over five million fiber strands.

## Why It Matters

For most of the AI boom, the scarce commodity has been the accelerator itself, and Nvidia’s chips in particular. But as clusters swell toward hundreds of thousands of processors that must behave as a single computer, the network linking those chips increasingly determines performance, power draw and latency. That has turned interconnect into the buildout’s next chokepoint, and drawn heavy investment, including from Nvidia, whose own networking business and silicon-photonics roadmap underscore how strategic the layer has become.

Silicon photonics, the technology of routing data as light on chips, is the wager underneath Lumilens and its rivals. Lumilens pegs the market for photonic interconnects at more than $100 billion, and investors are treating it as the next frontier of AI supply. “The critical component in scaling AI is shifting from compute to connectivity,” said Gavin Baker, managing partner at Atreides Management, who noted the company went from founding to a qualified product deployed inside a hyperscaler’s production data centers within two years. Mayfield’s Navin Chaddha put it more bluntly: “Copper has hit a wall the industry can’t engineer around.”

The added subtext is supply-chain concentration. Backers framed Lumilens as bringing much-needed diversification to an AI hardware stack heavily dependent on a handful of vendors, and the company has deliberately treated manufacturing, from chip assembly to high-volume production, as a product in its own right.

## What to Watch

The central question is whether Lumilens can manufacture at the volume its roadmap and its multibillion-dollar order book demand. The optics industry’s history is littered with companies that could design elegant parts but never scale them, and the McKinsey shortfall figures show how unforgiving demand has become. Watch whether the still-unnamed hyperscaler customer, described as one of the four largest, is eventually disclosed, and whether Lumilens can convert early qualification into repeatable, high-yield production. Also worth tracking: how aggressively Nvidia and incumbents such as Broadcom, Marvell and Coherent move on co-packaged optics, and whether a $5.51 billion valuation for a two-year-old hardware company proves prescient or a marker of how frothy AI-infrastructure financing has become.