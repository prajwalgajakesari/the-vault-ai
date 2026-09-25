Alibaba wants to own every layer between the silicon and the software agent. At its Apsara Conference in Hangzhou this week, the company unveiled the **Zhenwu V900**, an in-house AI accelerator that CEO Eddie Wu called the most powerful AI chip in China, alongside a rebuilt cloud platform designed not for human developers but for fleets of autonomous AI agents. Together, the announcements amount to Alibaba's clearest bid yet to become a vertically integrated AI supplier, one that designs its own chips, runs its own data centers, trains its own models and now sells the plumbing enterprises need to deploy agents at scale.

## A Chip Built for Half-Million-Card Clusters

The V900 comes from T-Head, Alibaba's chip design unit, and succeeds the Zhenwu M890. Alibaba says it delivers three times the performance of its predecessor, with 216 GB of GPU memory, 1,200 GB/s of inter-chip bandwidth and native support for the low-precision FP8 and FP4 formats that dominate modern inference. The M890, by comparison, carried 144 GB of memory and 800 GB/s of interconnect bandwidth.

“At Apsara Conference, we are introducing our next-generation AI chip, the Zhenwu V900. It is the most powerful AI chip in China today, delivering three times the performance of its predecessor,” Wu said in his keynote on September 22. “A single cluster built on V900 can support up to 500,000 cards to power frontier model training and inference.”

That scale comes from an upgraded supernode server that bundles the V900 with T-Head's ICN switch, Panmai SmartNIC and Zhenyue SSD controller. Where the M890 topped out at 128-chip supernodes, T-Head says more than 1,000 V900s can operate as a single system. Mass production and commercial release are slated for the first quarter of 2027, pulled forward from a third-quarter 2027 target on Alibaba's May roadmap.

The commercial traction is real. Zhenwu chips now serve more than 650 customers across automotive, finance, energy and manufacturing, up from roughly 400 external customers in May, when T-Head reported more than 560,000 chips shipped. Wu said the company anticipates “a significant growth in the annual AI chip shipment volumes.” Still, as *Tom's Hardware* noted, Alibaba disclosed no FLOPS figure, process node, foundry or power numbers, so the “most powerful” and three-times claims cannot yet be independently checked.

## The Agentic Cloud

The software half of the pitch is what Alibaba Cloud calls its agentic cloud, organized around three layers: model, harness and context. The **AI Native Cloud** handles training and inference at scale; Alibaba says its Platform for AI completed state-of-the-art post-training of a Qwen model in five days, its new Cloud Parallel File Storage cuts enterprise AI storage costs by 69%, and its HPN 8.0 Pro network supports more than 130,000 ports at 800G in a single cluster.

The centerpiece for enterprises is the **Agent Native Cloud**, led by **AgentCore**, a platform to build, run and manage AI agents across their full lifecycle, paired with an **Agent Security Center** for lifecycle security and compliance. Beneath it sits a Context Engine: **Agent Context** stitches a company's documents, business systems, chat records and multimodal data into a single memory foundation, which Alibaba says cuts token usage by up to 67%. The company's OpenLake lakehouse was also upgraded, with claimed 38% lower total costs and 40% faster queries.

At the edge, Alibaba launched **Qwen Intelligence**, a full-stack agent solution that lets phone makers build assistants capable of complex, cross-app tasks, with Honor the first partner. On the model front, covered separately in today's edition, Qwen 4 is in training and later generations are projected to reach 5 to 10 trillion parameters.

Wu framed the entire stack with an electricity analogy. “If tokens are the electricity powering the AI era, then chips are the power plants,” he said. “If chips generate tokens, the cloud is the grid that delivers them wherever they are needed.”

## Why It Matters

Alibaba is the rare company outside the United States attempting to control the full AI stack, and the V900 is the load-bearing piece. With access to top-tier Nvidia hardware constrained, a domestic accelerator that can be clustered at half-million-card scale gives Alibaba Cloud a supply line it controls, and a product it can sell to hundreds of other Chinese firms. It also puts T-Head in direct competition with Huawei's Ascend line, whose next-generation 960PR is due in the third quarter of 2027, a quarter or two after the V900.

The agent platform matters for a different reason: it is where cloud revenue will be won. Wu argued that agents running long-horizon tasks will become permanent “residents” on the cloud, constantly consuming compute. Tools like AgentCore and Agent Context are designed to make Alibaba the default place to host them, and a 67% cut in token usage is the kind of cost claim that moves enterprise buyers. Joe Tsai, Alibaba's chairman, summed up the goal as “guiding AI from technological breakthroughs toward value creation.”

The constraint is supply. Wu conceded that “global shortages across the AI data center supply chain are currently limiting the speed at which we can scale our compute infrastructure,” even as Alibaba set a target of more than 20 GW of data center capacity by 2032. The company also plans first-ever cloud regions in Türkiye, Finland and the Netherlands within 12 months, adding to its 107 availability zones across 31 regions.

## What to Watch

The real test arrives in early 2027, when the V900 enters mass production and independent benchmarks can finally measure its performance against Huawei's Ascend parts and Nvidia's export-compliant offerings. Watch whether T-Head's customer count keeps climbing past 650, whether AgentCore wins marquee enterprise deployments outside China as the new European and Turkish regions come online, and whether the chip ends up on the agenda as U.S.-China talks on AI continue.
