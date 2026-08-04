# Rhoda AI Emerges From Stealth With $450 Million to Give Robots 'FutureVision' Control

After 18 months of near-total silence, a Palo Alto robotics startup that had been quietly incubated inside Khosla Ventures pulled back the curtain in March with one of the largest opening rounds the physical-AI sector has seen. Rhoda AI exited stealth on March 10, 2026, unveiling FutureVision, a robot foundation model built on video-predictive control, alongside a $450 million Series A that values the young company at roughly $1.7 billion.

The round was led by Premji Invest and drew a deep roster of technology backers, including Khosla Ventures, Temasek, Capricorn Investment Group, Mayfield, Prelude Ventures, Matter Venture Partners, Leitmotif, and Xora, as well as venture veteran John Doerr. For a company with no consumer product and only a handful of disclosed industrial pilots, it is an outsized bet on a specific thesis: that the fastest path to useful robots runs through internet video, not painstaking lab demonstrations.

Rhoda is led by co-founder and CEO Jagdeep Singh, a serial deep-tech entrepreneur best known for founding solid-state battery company QuantumScape. He is joined by Chief Science Officer Eric Ryan Chan and Stanford professor Gordon Wetzstein, who heads the university's Computational Imaging Lab. The company says it has spent its stealth period building a "new class of robot foundation model designed to bring general intelligence into the physical world."

## How FutureVision Works

The technical heart of Rhoda's pitch is what it calls a Direct Video-Action (DVA) model, an architecture that reformulates a robot's control policy as a video-generation problem. Rather than leaning primarily on teleoperated robot trajectories, Rhoda pre-trains its models on hundreds of millions of internet videos to build what it describes as a "strong prior on motion, physics, and physical interaction." It then post-trains on smaller amounts of robot-specific data to map those video predictions onto actual hardware movements.

In operation, the resulting system continuously observes its environment, predicts future states as video, converts those predictions into actions, executes them, and re-observes the world — repeating the loop every few hundred milliseconds. That closed-loop design is the crux of Rhoda's argument against the vision-language-action (VLA) models that dominate current robot-learning research. Open-loop approaches, the company argues, generate plans without continuous feedback and struggle when layouts shift, unfamiliar objects appear, or workflows change unexpectedly.

"We believe the next era of robotics requires models that understand how the world moves — not just what it looks like or how it's described in language," said Jagdeep Singh, co-founder and CEO of Rhoda. "By learning from internet-scale video and operating in closed loop, our systems are designed to adapt to real-world variability in ways conventional approaches struggle to achieve. The goal is simple: robots that work in the real world, not just controlled lab settings."

Rhoda claims the heavy video pretraining pays off in sample efficiency, letting the model pick up new tasks with as little as ten hours of teleoperation data. FutureVision itself serves as the company's intelligence layer — a foundation model that powers Rhoda's own systems today and, over time, is expected to be licensed to partners running different robotic hardware and software.

## A $450 Million Bet on the Data Flywheel

The financing is structured to fund exactly the kind of real-world grind that separates robotics demos from deployable products. Rhoda says the Series A will support continued research and engineering, expansion of industrial pilots across manufacturing and logistics partners, and growth of a multidisciplinary team spanning generative AI, computer vision, and robotics.

Investors framed their conviction around a compounding-advantage argument. "We believe the first company to deploy intelligent, manipulation-capable robots at scale in real-world environments will kick-start a powerful data flywheel, creating a compounding advantage in capturing the long tail of real-world edge cases," said Sandesh Patnam, Managing Partner at Premji Invest.

Rhoda points to early field results to back the thesis. In a recent high-volume manufacturing evaluation, the company said its robots completed a component-processing workflow in under two minutes per cycle without human intervention, exceeding the customer's key performance indicators — a claim that, if it holds up across sites, would put Rhoda ahead of much of the field on the metric that matters most to industrial buyers: reliable autonomy amid changing materials and layouts.

## Why It Matters

Rhoda lands in the middle of an increasingly crowded and richly capitalized race to build "physical AI" — foundation models for robots analogous to the large language models that reshaped software. Skild AI, Physical Intelligence, Figure, and a wave of humanoid startups have all raised at eye-watering valuations on variations of the same premise. What distinguishes Rhoda is its wager on video prediction as the core representation, sidestepping the language-centric VLA paradigm that most rivals have embraced.

If that approach generalizes, it could reset expectations for how quickly robots can be taught new tasks and how well they cope outside choreographed conditions — the gap that has kept general-purpose robots perpetually "two years away." A $450 million Series A at a $1.7 billion valuation, before meaningful revenue, is also a signal in itself: capital is flowing toward the teams that can credibly claim a path out of the lab, and Singh's track record plus Khosla's incubation clearly gave investors the confidence to write very large checks very early.

## What to Watch

The open questions are the ones no press release answers. Can video-pretrained models sustain sub-two-minute cycle times across many customer sites, not just a single evaluation? Will Rhoda's licensing ambitions — putting FutureVision on third-party hardware — materialize, or will it stay vertically integrated? And how does its sample-efficiency claim of ten hours of teleoperation hold up against competitors making similar boasts? Watch for named commercial deployments in manufacturing and logistics, any peer-reviewed or benchmark disclosures on the Direct Video-Action model, and whether the data flywheel Premji Invest is betting on actually starts to spin. In a sector long on demos and short on dependable deployments, Rhoda's next 18 months out of stealth will matter far more than its first 18 in it.
