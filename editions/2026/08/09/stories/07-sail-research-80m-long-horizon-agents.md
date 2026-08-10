# Sail Research Raises $80M to Build Infrastructure for Long-Horizon AI Agents

Sail Research, a startup building compute infrastructure purpose-built for AI agents that run for hours or days rather than seconds, has raised $80 million in combined seed and Series A financing at a $450 million valuation, the company announced on June 25, 2026. The raise is one of the clearest bets yet that the next wave of agentic AI will demand its own dedicated backbone, distinct from the chatbot-era stack most cloud providers were built to serve.

The Series A was led by Kleiner Perkins, following an earlier seed round led by Sequoia Capital. Additional investors include Redpoint Ventures, Theory Ventures, Vine Ventures, CRV, A*, and Abstract Ventures. The round also drew a notable roster of angel investors: Alphabet chairman John Hennessy, Intel chief executive Lip-Bu Tan, and Together AI chief scientist Tri Dao.

## What Sail Is Building

Sail Research was founded by Neil Movva, a former NVIDIA, Apple, and Together AI executive, and Samir Menon, a former Apple engineer. The company describes itself as the first infrastructure platform designed specifically for long-horizon agents, and its product has two core pieces.

The first is an inference stack rebuilt from the ground up around throughput and efficiency, aimed at agents that can spend billions of tokens on a single task. Sail claims this stack delivers up to 10x lower cost per token than rival services. The second is Sailboxes, a stateful sandbox environment engineered to run for hours and days at a stretch, and which only charges customers for the time an agent is actively doing work rather than idling.

To demonstrate the approach, Sail says its platform set a new high score of 90.72% on the BrowseComp-Plus benchmark, which measures an agent's ability to complete complex, time-consuming online research tasks, while incurring roughly one-tenth the inference cost of competing services.

"Sail exists to make intelligence abundant," Movva said in the company's announcement. "Every decision we make, from the chip level to the API, is about giving teams the tokens, the scale, and the runtime to build agents without limits."

Movva has framed the core problem as an architectural mismatch. Unlike a human waiting at a keyboard, whose top priority is speed, agents need scale, reliability, and sustainable cost. Sail's answer, he wrote, is to hunt for efficiency at every layer of the stack: carefully choosing chips, writing custom inference engines, and running a global controller that keeps every machine in its fleet fully utilized.

## Why It Matters

For most of the current AI cycle, infrastructure has been optimized for a single interaction pattern: a person types a prompt, waits a beat, and reads a response. Latency is king, sessions are short, and the meter runs on request-response cycles. That model breaks down badly once agents start doing work that spans hours or days.

Long-horizon agents behave differently in ways that stress every part of the stack. They consume enormous volumes of tokens, sometimes billions on a single task, which turns raw inference efficiency into the dominant cost driver. They need to maintain state across long sessions, holding open files, browser tabs, and working memory rather than starting fresh each turn. And they spend significant stretches waiting on tools, on the network, or on other agents, which means a naive billing model charges customers handsomely for idle time.

Sail's pitch is that these are not features you can bolt onto a chatbot-era platform; they require rethinking the system from the chip up. The inference stack targets cost-per-token because that is where a token-hungry agent bleeds money. Sailboxes target statefulness and pay-for-active-work billing because long-running processes make the old per-request economics untenable. If autonomous agents become a meaningful share of enterprise compute, the company is betting that whoever owns the efficient runtime for them owns a large and durable market.

The investor lineup underscores how seriously that thesis is being taken. Backing from Hennessy, Tan, and Dao brings deep credibility in chip design, systems, and inference optimization, precisely the disciplines Sail claims as its edge. The $450 million valuation on a combined seed-and-Series-A raise signals that investors are pricing in the expectation of a category, not just a product.

## What to Watch

The immediate question is whether Sail's efficiency claims hold up outside its own benchmarks. A 90.72% BrowseComp-Plus score at one-tenth the cost is striking, but agent workloads vary widely, and independent, real-world validation across diverse tasks will matter more than a single leaderboard result.

The second question is competitive. Sail is entering a space where hyperscalers, established inference providers such as Together AI and Fireworks, and the frontier labs themselves all have incentives to own the agent runtime. A well-funded startup can move fast on architecture, but incumbents have distribution, existing customer relationships, and their own cost advantages at scale.

Finally, watch adoption and the shape of the customer base. Sail's economics are most compelling for teams running genuinely long, token-heavy agent workloads, and that market is still forming. Whether enterprises are ready to route production agents onto a young infrastructure provider, and whether Sailboxes' pay-for-active-work model proves as attractive in practice as it sounds on paper, will determine how quickly the $450 million valuation looks conservative or aggressive.

*Sources: [Fortune](https://fortune.com/2026/06/25/exclusive-sail-apple-kleiner-perkins-gpu-token-nvdia-sequoia-80-million/), [SiliconANGLE](https://siliconangle.com/2026/06/25/sail-research-raises-80m-optimize-long-horizon-ai-agents/), [Sail Research](https://www.sailresearch.com/blog/sail-raises-80m).*
