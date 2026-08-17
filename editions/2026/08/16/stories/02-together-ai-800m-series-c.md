*The Vault — AI Edition | Business | August 16, 2026*

Together AI has never shipped a proprietary frontier model. It has no chatbot, no consumer app, no benchmark chart of its own to defend. What it has is a $1.15 billion annual bookings run rate, an $8.3 billion valuation, and a thesis that the most valuable position in artificial intelligence may not be building the smartest model at all — but running everyone else's open weights cheaper than anyone else can.

The four-year-old San Francisco company announced an $800 million Series C at an $8.3 billion post-money valuation on July 1, led by Aramco Ventures, with participation from Vista Equity Partners, General Catalyst, Emergence Capital, NVIDIA, March Capital, Pegatron, Salesforce Ventures, SentinelOne's S Ventures, DTCP Growth, Lux Capital, Geodesic and PSP Partners. The valuation is more than double the $3.3 billion Together commanded in its $305 million Series B roughly sixteen months earlier — a repricing that arrives as enterprises quietly redirect production AI workloads away from closed frontier APIs and toward open-weight alternatives.

"Intelligence is becoming a foundational resource for the modern economy, every bit as essential as electricity, bandwidth or capital," said co-founder and CEO Vipul Ved Prakash in the announcement. "Our mission is to ensure that intelligence is abundant, not expensive. The future of AI won't be owned by a few companies. It will be built by millions of developers and businesses, and open-source models are making that possible."

## The margin problem nobody advertised

The commercial logic behind the round is less philosophical than Prakash's framing suggests. Companies that built AI features on closed frontier models over the past two years are discovering that per-token pricing which looked trivial in a prototype becomes ruinous in production. As AI systems shift from generating demo responses to running agents that write code, resolve support tickets and process document backlogs, inference volume — and inference cost — compounds faster than revenue.

"The cost structure of closed frontier LLMs that appears manageable in a prototype often becomes unsustainable in production," Prakash wrote in the company's announcement blog. "As usage grows, inference bills compound faster than budgets, forcing companies to ration intelligence just as demand for it accelerates."

Together's pitch is that open-weight models — DeepSeek, NVIDIA's Nemotron, MiniMax, Kimi and GLM among them — have closed enough of the quality gap to make that rationing unnecessary. The company says customers routinely see 6x to 20x lower costs at equal or better performance, with savings reaching 60x in some deployments. Customer support firm Decagon cut its inference bill sixfold after migrating. Together's paying roster now includes Cursor, Cognition, ElevenLabs and Suno, and the platform serves more than a million developers.

The market data supports the trend line. Open-source model usage across the industry tripled in twelve months, according to research from AI gateway OpenRouter that Together cites, and McKinsey found that nearly three-quarters of organizations expect to increase their use of open-source AI. Annual bookings crossed $1.15 billion last quarter.

## Capacity, not just capital

The more consequential number in the announcement may not be the $800 million. Alongside the equity, Together secured commitments for **over 500 megawatts of compute capacity to be capitalized independently by its new investors** — a structure that keeps the cost of physical infrastructure off Together's own balance sheet while giving it access to the GPUs it needs. The company expects its infrastructure footprint to grow roughly 50-fold over the next five years.

That arrangement explains Aramco's presence at the top of the cap table more clearly than any strategic-synergy language could.

"Building AI infrastructure over the next decade will be the biggest infrastructure project in human history," said Abhishek Shukla, managing director of Prosperity7 Ventures US, the diversified venturing arm of Aramco Ventures. "Together has built the platform that makes open source models genuinely usable at enterprise scale, and the team's ambition matches the scale of the opportunity in front of them. We're proud to partner with them, not just on this round but on scaling compute and capacity globally."

## Why this matters

Neocloud economics are brutal. Renting GPU capacity is capital-intensive and thin-margin, living or dying on utilization, and Together both leases chips from other providers and buys its own — it signed a multi-year agreement in June with Rumble Inc. for NVIDIA HGX B300 systems. The category is crowded and richly funded: Baseten was valued at up to $13 billion in June, Groq raised $650 million, and TensorWave took $350 million at $1.55 billion.

Together's differentiation is that it is not purely a landlord. FlashAttention-4 for NVIDIA's Blackwell architecture, the Together Megakernel and together.compile are research outputs that translate directly into tokens-per-dollar — the only metric that matters when your product is arbitrage on someone else's model weights. The company is betting that a research-driven inference stack is a durable moat where raw GPU rental is not.

"The shift toward open source isn't a niche preference anymore, it's becoming the default for any company that wants to scale AI without losing its margin," said Joe Floyd, general partner at Emergence Capital, an investor since Together's 2023 Series A.

The strategic risk is inventory risk of a peculiar kind. Together's entire business depends on labs it does not control continuing to release competitive open weights. Should that pipeline narrow — or should closed-model providers cut prices aggressively enough to erase the 6x-to-20x gap — the arbitrage compresses.

## What to watch

Notably, Together raised less than the $1 billion The Information reported it was seeking in March, but at a valuation well above the $7.5 billion figure then under discussion. Watch three things: whether bookings growth keeps pace with the 50x capacity build-out, whether the 500 MW of independently capitalized compute actually breaks ground on schedule, and whether frontier labs respond with price cuts steep enough to make the open-weight discount look like a temporary window rather than a structural shift.

---

**Sources:**
- [TechCrunch](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/)
- [Together AI](https://www.together.ai/blog/announcing-our-series-c)
- [Business Wire](https://www.businesswire.com/news/home/20260701243402/en/Together-AI-Raises-$800-Million-at-$8.3-Billion-Valuation-to-Make-Frontier-AI-Accessible-to-All)
- [DatacenterDynamics](https://www.datacenterdynamics.com/en/news/together-ai-raises-800m-in-series-c-funding-round/)
