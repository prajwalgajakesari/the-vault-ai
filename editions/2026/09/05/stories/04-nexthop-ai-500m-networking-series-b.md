Every AI buildout story runs the same photograph: racks of accelerators glowing blue down a cold aisle. What never makes the frame is the layer that decides whether those chips do anything together — the switches, optics and east-west fabric stitching tens of thousands of GPUs into one machine. Nexthop AI has raised $500 million on the argument that this unphotogenic layer, not the silicon, is now the binding constraint.

The Santa Clara company closed an oversubscribed $500 million Series B at a $4.2 billion valuation, led by Lightspeed Venture Partners, with Andreessen Horowitz joining as a major new investor plus Altimeter and all existing backers. An earlier $110 million round, also led by Lightspeed with Kleiner Perkins, WestBridge, Battery Ventures and Emergent Ventures, took it out of stealth in March 2025.

## Three corrections before the reporting

The round is not new this week: Nexthop announced it on **March 10, 2026**, and it has resurfaced in September aggregator roundups.

The founder is not Ravi Vasudevan. Nexthop AI was founded in 2024 by **Anshul Sadana**, who spent 17 years at Arista Networks — most recently as chief operating officer — and eight years at Cisco before that.

And the claim that Meta is a named early customer is unconfirmed: no source reviewed for this piece names any Nexthop customer. The company describes its buyers only as hyperscalers and NeoClouds. Its platforms do support FBOSS, the operating system Meta open-sourced, the likely origin of the inference, but an inference is all it is.

## What Nexthop actually sells

Nexthop does not ship a catalog. It co-develops hardware in lockstep with a few very large operators on a joint-design manufacturing model. Alongside the funding it launched three systems, all on Broadcom silicon.

The NH-4010 is a 51.2-terabit-per-second switch on Tomahawk 5 that Nexthop claims saves 15 to 20 percent power in like-for-like configurations — at fleet scale, tens of megawatts. The NH-4220 doubles that to 102.4 Tbps on Tomahawk 6 and is pitched as the densest air-cooled system in its class. The NH-5010, on Broadcom Qumran 3D, is a deep-buffer switch built for what Nexthop calls a disaggregated spine: splitting the spine tier in two, one layer moving traffic inside the building, the other handling packets between sites.

All three support RoCEv2, which lets one GPU write directly into another’s memory without routing through a CPU, plus DCQCN for congestion control. At the 2025 launch, Sadana described 1.6-terabit ports and chassis pushing 50 to 100-plus terabits — throughput that until recently lived only in telecom core routers.

## Why the fabric became the bottleneck

Large training runs are synchronous. Every step ends with a collective operation in which thousands of GPUs exchange gradients, and the run proceeds only when the slowest link finishes. A cluster is fast not because its accelerators are fast but because its fabric does not stall. Add tail latency, congestion and one flapping optic, and utilization sits far below what the invoice implies.

“The AI wave is right in front of us, and it is causing a massive disruption, including at the infrastructure level,” Sadana told Network World at launch. “So I felt there is a gap in the market.”

His pitch is specific: compress development cycles by six to 12 months, evaluate four to six architectural alternatives instead of one or two, capture single-digit gains that only matter multiplied by a million ports. Power is the sharpest version — when a campus is capped by its grid interconnect rather than capex, a 15 percent cut in switch power buys more accelerators behind the same substation.

## Arista, Broadcom, Nvidia

The competitive picture is difficult. Nvidia sells Spectrum-X as an integrated fabric alongside its GPUs and has every incentive to make the bundle the path of least resistance. Arista — Sadana’s employer for 17 years — owns the cloud switching franchise and has moved hard into AI back-end fabrics. Broadcom supplies the silicon inside almost everything, including Nexthop’s own boxes — both its key supplier and the reason rivals match its chip generation.

Nexthop’s wedge is that hyperscalers do not want a bundle: they want to own the software and avoid a single-vendor fabric, but cannot staff every hardware program in-house at AI speed. “AI datacenter networking is being rearchitected as genAI drives a new wave of infrastructure buildout by hyperscalers and neoclouds,” said SemiAnalysis founder Dylan Patel in Nexthop’s announcement, putting the segment on a path to $100 billion by 2031.

## The case for open networking

Nexthop’s platforms run any version of SONiC or FBOSS a customer chooses, or ship turnkey with Nexthop NOS, its SONiC-derived stack with added security hardening and faster patching. That decouples hardware refresh from OS lock-in, precisely the dependency hyperscalers spent a decade escaping.

Sadana is clear-eyed about how open the open stack really is. “It might be open source, but they have lots of libraries that are actually closed within their own company,” he said of cloud operators. Nexthop is not selling a universal OS; it sells the engineering to bend an open base to each customer’s private extensions.

Lightspeed’s Guru Chahal framed the ambition without hedging: “The rapid growth of AI is forcing a fundamental rethink of data center network architecture — and that creates one of the largest infrastructure market opportunities we’ve seen in a generation, with the potential to build a $100B+ company.”

## What to watch

Three things. Customer names: a $4.2 billion valuation on an undisclosed list is an act of faith, and a hyperscaler design win going public is the next datapoint. Tomahawk 6 volume: the NH-4220 is a claim until it ships at scale, and power figures verified by a buyer rather than a datasheet would settle the efficiency argument. And whether Nvidia tightens Spectrum-X or loosens it. If the bundle wins, the open-NOS thesis narrows to the few operators big enough to build their own. If not, Nexthop raised at exactly the right moment.