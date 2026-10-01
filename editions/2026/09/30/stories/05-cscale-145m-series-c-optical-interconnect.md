# CScale Emerges From Stealth With $145M Series C, Backed by Nvidia and Intel, to Wire AI Scale-Up Systems With Light

In a data center built around hundreds of thousands of AI accelerators, a laser failing somewhere is no longer a rare event. It is the normal state of the fleet. That is the premise behind CScale, a Palo Alto optical interconnect startup that came out of stealth on Wednesday with $145 million in Series C funding and two of the most important strategic backers in AI hardware: Nvidia and Intel Capital.

Atreides Management, Valor Equity Partners and Premji Invest co-led the round. Sutter Hill Ventures, which has backed CScale since it was founded, invested again, as did existing investor Maverick Silicon. Nvidia and Intel Capital are CScale's first strategic investors. The round takes the company's total funding to $188 million. CScale says the money will go toward developing and commercializing its optical interconnect for AI "scale-up," the high-bandwidth, ultra-low-latency links that let many accelerators behave like one much larger computer.

## A pitch built on failure

CScale has said little about how its hardware works. In its announcement it described an "integrated light engine" meant to provide reliable optical connectivity for AI infrastructure at gigawatt scale. The design is meant to contain optical failures so they don't reach the workload, rather than simply making broken parts easier to swap.

The company's argument rests on arithmetic. CScale says that in the gigawatt-class AI data centers expected by the end of the decade, a single scale-up domain will cover thousands of tightly coupled accelerators spread across dozens of racks. Multiply the optical links across a fleet that size and, as the company puts it, failures that are rare on any one link become a continuous fleet-level condition, degrading parts of the AI factory unless they are contained.

"As AI scale-up domains extend across dozens of racks, optical interconnect becomes essential," said Martin Lund, CEO of CScale. "At that scale, reliable, predictable communication is fundamental to system economics. Easier part replacement improves serviceability, not continuity. We're designing the interconnect for continuity. Lasers will fail. Compute shouldn't."

Gavin Baker, managing partner and chief investment officer at Atreides Management, framed the investment the same way. "AI infrastructure is no longer just a compute problem. It is a systems problem," he said. "As scale-up systems move toward gigawatt-class deployments, interconnect bandwidth means nothing without system reliability. Every optical failure is a compute failure."

Sandesh Patnam, managing partner at Premji Invest, pointed to the team's engineering choices. "CScale's strength is its architectural judgment: understanding which technical choices create value for the entire system," he said.

The leadership has deep networking-silicon experience. Lund built Broadcom's switching business into a billion-dollar franchise and held senior roles at Microsoft and Cadence. Most recently he ran Cisco's Common Hardware Group, which covered silicon, hardware systems and optics, including Silicon One. Founder and CTO Sanjai Kohli co-founded SiRF, which helped bring GPS to mass-market devices and earned him the 2010 European Inventor Award. He later founded Inovi, which Facebook acquired in 2014. CScale was founded in 2023 and has about 85 employees worldwide.

## Why optical interconnect matters for AI infrastructure

The bottleneck in AI clusters has moved from the chip to the wires between chips. Scale-up networks, the fabric that lets GPUs within a domain share memory and synchronize at very high bandwidth, have so far relied mostly on copper. Copper is cheap, power-efficient and dependable over short distances. But at the signaling rates current accelerators need, its usable reach shrinks to roughly a single rack. Once a scale-up domain grows past that, which is what CScale's "dozens of racks" describes, the links have to become optical.

Optics brings its own problem: lasers and optical components fail more often than passive copper cables. In a scale-up domain where thousands of accelerators run in lockstep, one bad link can stall or slow a whole training job. That is the gap CScale is targeting. Competitors have mostly sold bandwidth and energy efficiency. CScale is selling continuity, the idea that a failed component should not cost compute time.

The field is crowded and well funded. Celestial AI raised $250 million for its Photonic Fabric platform, built to get past copper's limits, and later agreed to be acquired by Marvell for $2.35 billion. Lightmatter raised $400 million at a $4.4 billion valuation, taking its total funding to $850 million. Eliyan recently raised its own $145 million Series C as it expanded into electro-optical interconnects. Nvidia's participation is especially notable, since the company sells its own scale-up fabric and would be among the biggest potential customers for any technology that extends it.

## Today's deals

CScale was not the only Series C announced on Wednesday. Metaview, the AI recruiting platform, raised $60 million led by Insight Partners, with participation from GV and others, bringing its total funding to $110 million. The two deals sit at opposite ends of the AI economy, one in physical infrastructure and one in agent software, and both show investors still writing large late-stage checks across the stack.

## What to watch

CScale has not disclosed a product timeline, performance specifications or customers, so the next milestones will matter. Watch for a technical disclosure that shows how its light engine contains failures in practice, for any sign of how closely it works with Nvidia and Intel beyond their investments, and for design wins with the hyperscalers and neoclouds building gigawatt-class sites. If the industry's move from copper to optics in scale-up arrives on the schedule CScale describes, the reliability argument could become a buying criterion for the largest AI clusters, not just a talking point.
