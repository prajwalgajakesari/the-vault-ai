---
headline: "Lindy Moved 100% of Its Traffic Off Claude to DeepSeek -- and Watched Its AI Bill Collapse"
slug: lindy-deepseek-migration-cost
category: business
story_number: "03"
date: 2026-06-29
sources:
  - name: CNBC
    url: https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html
    domain: cnbc.com
  - name: The New Stack
    url: https://thenewstack.io/lindy-deepseek-anthropic-switch/
    domain: thenewstack.io
  - name: The Decoder
    url: https://the-decoder.com/ai-startup-lindy-ditched-claude-entirely-for-deepseek-saving-millions-as-cost-pressure-mounts-on-anthropic/
    domain: the-decoder.com
  - name: DeepSeek API Docs
    url: https://api-docs.deepseek.com/quick_start/pricing
    domain: api-docs.deepseek.com
---

# Lindy Moved 100% of Its Traffic Off Claude to DeepSeek -- and Watched Its AI Bill Collapse

When Flo Crivello, the founder and CEO of AI agent startup Lindy, "pulled the trigger" last week, he did not move a slice of his workload or run a cautious A/B test. He moved everything. In a single cutover, 100 percent of Lindy's production traffic shifted off Anthropic's Claude models and onto DeepSeek v4, the flagship open-source model from the Chinese lab that has become shorthand for cheap, capable inference.

"Pulled the trigger today and switched 100% of Lindy traffic to DeepSeek v4, churning from Anthropic models," Crivello wrote on X. "Saves us millions of $ and we're actually seeing an *increase* in performance on many core use cases. Transformative for the business."

It is the kind of decision that, until recently, would have read as reckless: ripping out a frontier US model that defined your product and replacing it wholesale with a Chinese alternative. But for a 25-person company whose inference bill had grown to exceed payroll, Crivello frames it as something closer to triage. The cost curve, he told CNBC, "crashed to the ground." His blunter formulation: "It's a matter of survival for the business."

## When the AI Bill Outgrows the Org Chart

The math driving the move is stark, and increasingly common. Lindy builds AI agents that handle tasks like triaging email inboxes and pre-drafting replies in a user's voice -- exactly the kind of high-volume, always-on automation that burns through tokens. As Lindy scaled, its model spend grew until it surpassed what the company paid its own people. For a venture-backed startup watching its runway, an inference line item larger than the salary line is not a footnote; it is an existential threat.

The price gap explains why DeepSeek was so tempting. After a June 2026 cut, DeepSeek lists V4 Pro at roughly $0.435 per million input tokens and $0.87 per million output tokens, with cached input dropping to a fraction of a cent. Anthropic's premium tiers cost multiples of that. On migrated traffic, the savings were dramatic enough that Crivello would only quantify them with a single word when pressed by The New Stack on exactly how much: "A ton."

What made the decision defensible was not just price but performance. Crivello says Lindy saw "surprising performance gains" on its core use cases -- the inbox triage and reply-drafting that represent the bulk of its volume -- though he acknowledges DeepSeek still trails Anthropic on some complex automation tasks.

## The Migration Was "100x More Work Than We Thought"

The headline makes the switch sound like flipping a setting. The reality was a months-long engineering grind. Crivello says Lindy had been "looking to make this switch and evaluating new OSS models for 6-9 months," and testing DeepSeek specifically since its release roughly two months earlier. The cutover itself, he says, was "100x more work than we thought."

The hard part was evaluation. Lindy ran online evals, offline evals, and "tons of vibe evals" to confirm the new model could match or beat what Claude had been delivering across real tasks. From there it was a gradual rollout -- monitoring not just task accuracy but user retention -- followed by a wholesale rewrite of prompts tuned to DeepSeek's behavior. In other words, the savings were real, but they were not free; they were bought with engineering time most companies underestimate.

Crivello also has an escape hatch. Lindy plans to "escalate to Opus when we detect Lindy is failing at a task," he wrote, "but that'll be marginal." And he is keeping the door open to Anthropic: "I wouldn't be surprised if Anthropic's next release earned them our business back, but they would need to significantly cut prices." Tellingly, Lindy still pays Anthropic -- just for internal use, where a flat-rate Max subscription makes the economics work. "If it wasn't for it, and if we had to pay full token price, we'd switch to something else," Crivello says.

## Where the Playbook Travels -- and Where It Doesn't

Lindy's story is a clean case study in token economics, but it is not a universal mandate, and the tradeoffs deserve to be named. Routing core product traffic to DeepSeek means giving up Anthropic's Constitutional AI safety controls, any US-origin guarantee on the model itself, and the enterprise governance scaffolding -- audit trails, data-residency commitments, compliance attestations -- that regulated buyers treat as table stakes. For a lean startup optimizing burn, those are acceptable costs. For a Fortune 500 bank, hospital, or government contractor, they can be disqualifying.

Crivello draws the line himself. "Companies like us who spend a lot on tokens, 100% -- you'd be irresponsible not to," he says. "Other companies, it will depend, but I think a lot of folks just stick to the brand name." That is the real signal in this story. The generalizable lesson is not "switch to DeepSeek." It is that at sufficient volume, model spend becomes a first-class strategic variable, and the era of defaulting to the premium brand because it is the safe choice is ending for the heaviest token consumers.

The pressure this puts on Anthropic and OpenAI is the subplot worth watching. Crivello's threat to return only "if they significantly cut prices" is precisely the dynamic frontier labs fear: their best customers are also their most price-sensitive, and a credible open-source alternative gives those customers leverage they did not have a year ago.

## What to Watch

Three things will determine whether Lindy is an outlier or a leading indicator. First, retention: if DeepSeek-powered agents hold user retention over the coming quarters, the performance case stops being anecdotal. Second, the escalation rate: how often Lindy actually falls back to Opus will reveal how much frontier capability the cheaper model genuinely replaces versus merely approximates. And third, the incumbents' response -- whether Anthropic and OpenAI answer with price cuts, efficiency-focused tiers, or simply let their margin-conscious power users walk. Crivello has already told them what it would take to win Lindy back. The rest of the market is watching to see if anyone answers.
