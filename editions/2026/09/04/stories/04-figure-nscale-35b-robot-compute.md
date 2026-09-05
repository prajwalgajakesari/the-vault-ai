Figure has not yet shipped a humanoid robot into a single consumer home. On Sept. 3 it committed $3.5 billion to buy GPUs anyway.

The San Jose robotics company announced a multi-year strategic partnership with Nscale, the British AI cloud provider, to deploy up to 100,000 Nvidia GPUs on the Vera Rubin platform. The initial GPUs are targeted for deployment starting the second half of 2027 in Barstow, Texas. The $3.5 billion is the floor: both companies said they intend to scale the arrangement to over $6 billion. Nscale will become a Figure shareholder and Figure's preferred compute provider.

It is the largest compute commitment any humanoid robotics company has made, from a firm whose last disclosed valuation was $39 billion post-money, set by a Series C that closed in September 2025.

## The deal, and why now

Figure was unusually direct about the constraint driving it. "Figure is entering a phase where we are largely bound by data and compute needed to train Helix," the company wrote in its announcement, referring to the AI stack that controls its robots.

The data half of that sentence got a plan first. On Aug. 25, Figure came out of stealth with Index, a crowdsourced data-collection app it had been running quietly for four months. The numbers it disclosed then: 264,000 downloads across 108 countries, more than 44,000 weekly active users, over 16 million videos uploaded, $15 million paid out to the contributors it calls Creators, and an ingest rate of 30 minutes of video every second — what Figure characterized as 4.9 years of human work uploaded per day. Per 1,000 hours collected, the dataset contains 373 unique tasks, 1,146 unique manipulated objects and 116 unique environments. By the Nscale announcement nine days later, the ingest rate had moved to 35 minutes of data every second.

Figure had already committed to spending over $1 billion in the next 12 months on data and compute. The Nscale deal is what that looks like extended past a year.

"To bring humanoid robots to every home in the world, we are largely constrained by data and compute," said Brett Adcock, founder and CEO of Figure. "Our AI model, Helix, becomes more capable the same way every learned system does: with more data and compute. Today we're excited to partner with Nscale to bring the compute required to make this vision a reality."

Nscale framed it as a category expansion. "We're excited to partner with Figure as physical intelligence becomes AI's next frontier," said Josh Payne, CEO and founder of Nscale. "We've seen incredible growth with inference and agentic AI and Figure is pushing the boundaries of AI even further."

Nvidia CEO Jensen Huang, whose company is an investor in both parties, supplied the loop diagram: "Nscale and Figure have activated the robotics flywheel: training Figure's models on Nvidia Vera Rubin through Nscale's AI cloud, validating them in Nvidia Isaac Sim, and deploying them on Nvidia GPUs in Figure's robots."

One more clause is worth noting. The companies said they will explore scaling Nscale's supply chain with humanoids — Figure's robots working inside the data centers that train Figure's robots.

## Does robot training actually need frontier-lab compute?

The honest answer is that nobody knows yet, and Figure is spending $3.5 billion to find out.

The case against is that robotics has historically been data-starved, not compute-starved. Vision-language-action models are small next to frontier language models; the bottleneck has been that manipulation data does not exist on the internet and has to be manufactured episode by episode. Figure said as much itself: the data "has to come from the real world." A hundred thousand GPUs do not generate a single new grasp.

The case for is that Index changes the arithmetic. Thirty-five minutes of video per second is roughly 63 years of footage per year of wall-clock time, and raw video is the most compute-expensive modality to train on. Ingesting it also required Figure to rebuild its infrastructure around a five-stage pipeline — filtering, fraud review, deduplication, rebalancing, annotation — with embedding-based similarity checks on every segment. That burden scales with the firehose, independent of any training run. Solve the data bottleneck aggressively enough and you manufacture a compute bottleneck behind it.

The financing structure deserves as much scrutiny as the technology. Nscale is not simply selling capacity; it is making a strategic investment in its customer, and the customer is committing to buy from it. Equity-for-compute is now a standard pattern in AI infrastructure, and it has a standard problem: the vendor's reported backlog and the customer's ability to pay are not independent variables.

Nscale's own position sharpens that point. Bloomberg reported on Sept. 4 — one day after the Figure announcement — that Nscale is seeking $3.5 billion in pre-IPO financing, selling $1.5 billion in convertible notes while seeking $2 billion more from Nvidia. Nscale has told investors it holds roughly $51 billion in contracts, swelled by an approximately $45 billion Anthropic deal signed in late August, and is targeting a U.S. listing as early as this month. The Information reported that Nscale has been citing roughly $103 billion in "revenue," a projection based on signed customer leases rather than current sales.

A company founded two years ago, which raised $155 million in its Series A in December 2024 and $1.1 billion in a Series B in March, is booking multi-billion-dollar contracts against capacity it must raise billions more to build — partly from Nvidia, which also sells it the chips and holds equity in its newest customer.

## What to watch

Three markers. First, whether Nscale's IPO prices this month and what public investors make of a backlog built on pre-revenue counterparties. Second, whether Figure publishes the generalization results it promised alongside Index; the whole compute thesis rests on the claim that Helix scales with data, and that claim is currently internal. Third, the Barstow site itself. Second half of 2027 is a long runway for a first Vera Rubin deployment, and nothing in this deal is real until power is flowing through it.
