---
headline: "IBM and Together AI Sign $240 Million Deal for an Nvidia-Powered Inference Cluster"
slug: "ibm-together-ai-240m-inference-cluster"
category: "business"
story_number: "05"
date: "2026-08-12"
---

# IBM and Together AI Sign $240 Million Deal for an Nvidia-Powered Inference Cluster

When IBM wanted to prove it still belonged in the AI infrastructure conversation, it did not build another chatbot. It signed a check. On August 11, the 114-year-old company and the San Francisco startup Together AI announced a multiyear, $240 million agreement to stand up a large, dedicated Nvidia-powered cluster on IBM Cloud — one built not to train the next frontier model, but to run open-source models in production for enterprises paying by the token.

The deal is small next to the tens of billions being spent on training superclusters. But its shape says something bigger about where the money is headed next.

## What is being built

Under the agreement, IBM will deploy a large cluster of Nvidia HGX B300 systems — servers that link Nvidia's newer Blackwell-generation GPUs — connected with Nvidia's Spectrum-X Ethernet networking. According to reporting from Reuters, the initial U.S.-based deployment will run roughly 2,000 Blackwell-class chips. Nvidia says the HGX B300 platform is built to deliver up to 30 times more "AI factory" output than the prior generation. IBM expects the cluster to come online in the first quarter of 2027.

Crucially, this is inference infrastructure, not training infrastructure. Together AI will use the cluster to serve open-source model inference — the moment-to-moment work of answering queries, generating text, and powering agents — rather than the compute-heavy grind of building models from scratch. IBM described it as its first dedicated, large-scale cluster built specifically for inference on IBM Cloud using HGX B300 systems.

## The pitch: frontier performance without the frontier price

The commercial logic centers on token economics — the cost of generating each unit of AI output — which has quietly become the defining battleground of enterprise AI.

"Enterprises want the performance of the best frontier models without the closed-model price tag, and that only works if the infrastructure underneath is fast and reliable at scale," said Vipul Ved Prakash, CEO of Together AI. "Working alongside IBM with Nvidia gives us that foundation. This cluster lets us bring production-grade inference to more companies, faster, and it's a big step in our push to make open-source AI the obvious choice for enterprises."

Together AI, founded in 2022, operates what it calls an "AI Native Cloud," a platform spanning inference, training, fine-tuning, and agentic workflows built on open models. The company says it now serves 400 trillion tokens monthly and, in July, raised an $800 million Series C at an $8.3 billion valuation. It selected IBM and Nvidia, it said, for their ability to deliver GPU capacity "at the pace required for rapid AI scaling and lowest token cost."

Demand appears to be running ahead of supply. Together AI's chief revenue officer, Kai Mak, told Reuters the new capacity "will be sold out at least two to three months ahead of time" — a striking claim for hardware that will not be live until 2027.

## Why IBM, and why now

For IBM, the deal is a bid to reclaim relevance in a market that largely passed it by. IBM Cloud has never cracked the top tier dominated by Amazon, Microsoft, and Google, and IBM's stock fell more than 20 percent in July after preliminary second-quarter results disappointed investors. Landing a marquee AI-native customer — and effectively stepping into the "neocloud" business of renting specialized GPU capacity — gives Armonk a fresh story to tell.

"Enterprises are in a race to adopt agentic AI at scale to drive real business outcomes," said Alan Peacock, general manager of IBM Cloud. "IBM and Nvidia are delivering scalable, economical, enterprise-grade AI infrastructure that can help Together AI accelerate innovation for the next generation of AI infrastructure."

The arrangement extends a deepening IBM-Nvidia partnership. The two expanded their collaboration at Nvidia's GTC conference in March around GPU-native data analytics and hybrid cloud infrastructure. Nvidia, for its part, framed the deployment in its now-familiar utility language. "AI factories are becoming essential enterprise infrastructure — like electricity and telecommunications — turning compute and data into intelligence," said Dion Harris, a senior director for HPC and AI infrastructure at Nvidia.

## The inference inflection

The deal is a clean data point for a thesis gaining momentum across the industry: AI spending is shifting from training to inference. Training a model is a one-time capital event; inference is a recurring operating cost that scales with every user, every query, and — increasingly — every autonomous agent making dozens of model calls to complete a task. As enterprises move pilots into production, inference is where the sustained compute demand, and the sustained revenue, will live.

Open-source models sit at the heart of that shift. Businesses are drawn to them to control costs and to keep sensitive workloads off third-party closed APIs, a concern sharpened by high-profile security incidents involving models from vendors including Anthropic, OpenAI, and Meta. Running open weights on dedicated infrastructure lets enterprises fix their token costs and keep data inside a perimeter they control — the exact promise this cluster is designed to sell.

## What to watch

Three things will tell whether this is a turning point or a footnote. First, execution: the cluster is not due until Q1 2027, and GPU deployments routinely slip. Second, whether IBM can convert a single flagship win into a repeatable neocloud business rather than a one-off. And third, the broader signal — if inference-first deals like this multiply, it will confirm that the center of gravity in AI infrastructure is moving from the labs building models to the platforms running them at scale. For IBM, a company that has spent a decade searching for its place in the AI era, $240 million may prove less about the sum than about the direction.
