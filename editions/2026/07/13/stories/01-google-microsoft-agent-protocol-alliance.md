# Google and Microsoft Back a Rival Agent Protocol to Counter Anthropic and OpenAI in the Enterprise

*The Vault — AI Edition · Business · July 13, 2026*

The two companies that spent a decade fighting each other over cloud contracts have found a common enemy, and it is not one another. Google, Microsoft, Salesforce, Snowflake, and ServiceNow have agreed to jointly support a shared standard for how AI agents plug into enterprise software, according to a July 13 report in The Information — a coordinated move that people inside the alliance describe, bluntly, as an effort to beat back Anthropic and OpenAI in the layer of the AI stack that will decide who controls corporate automation for the next decade.

The fight is over plumbing. Not model quality, not benchmark scores, but the unglamorous connective tissue that lets an autonomous agent find a budget approval system, query a customer database, and file a report without a human hand-wiring every integration. Whoever sets that standard gets default status inside every enterprise AI deployment — and right now, the default belongs to a competitor.

## The incumbents' answer to MCP

The standard the alliance is rallying behind is called Agentic Resource Discovery, or ARD, a specification first unveiled in mid-June 2026 and published under an Apache 2.0 license. ARD uses lightweight `ai-catalog.json` manifests that let an agent query a federated registry and discover, on the fly, which tools and other agents are available for a given task. Instead of hardcoding where every resource lives, an agent describes what it is trying to accomplish and ARD helps it locate the pieces. Organizations publish their own catalogs under their own domains, so no single vendor owns the registry.

Beyond the five headline backers, the ARD coalition already includes Cisco, Databricks, GitHub, GoDaddy, Hugging Face, and NVIDIA. The signatory list is the story. Salesforce, Snowflake, and ServiceNow collectively sit on top of most of the world's enterprise customer records, data warehouses, and IT workflows; Google and Microsoft own the clouds it all runs on. If that group ships a coherent, co-supported standard, every company deploying agents suddenly has a Google-and-Microsoft-blessed alternative to building its stack on a rival's protocol.

That rival is Anthropic's Model Context Protocol. Introduced in November 2024 and often described as "USB-C for AI," MCP has quietly become the de facto standard for connecting models to tools over roughly 18 months. The adoption numbers explain the incumbents' urgency: as of July 2026, an estimated 78% of enterprise AI teams run MCP-backed agents in production, 28% of Fortune 500 companies operate MCP servers, there are more than 9,400 public MCP servers, and the protocol's SDKs are downloaded around 97 million times a month. "MCP won the standards war," analyst site andrew.ooo declared in a July 1 assessment. "The interesting question in July 2026 isn't 'should we adopt MCP' — it's 'which use cases move first.'"

## Everyone is cooperating and knife-fighting at once

Here is the complication that makes this a genuine protocol war rather than a clean two-sided battle: the same companies now backing ARD are, simultaneously, members of the very foundation that stewards MCP.

In December 2025, Anthropic donated MCP to the newly formed Agentic AI Foundation under the Linux Foundation, alongside Block's "goose" agent framework and OpenAI's AGENTS.md standard. That foundation's platinum members read like a peace treaty: Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI. Tom's Hardware, covering the group's formation, framed it as tech giants "joining forces" to build shared open-source standards for the agent era and avoid the fragmentation and vendor lock-in that everyone claims to fear.

So Microsoft, Google, OpenAI, and Anthropic are cooperating inside a neutral standards body while Google and Microsoft simultaneously assemble a five-company bloc explicitly positioned against Anthropic and OpenAI in the market. Both things are true at once. ARD's own backers insist the specification is designed to complement MCP and Google's Agent2Agent protocol rather than replace them — a "lightweight federated layer," in their words. Whether that framing survives contact with commercial incentives is the open question.

## Why it matters

Protocol wars sound boring until you remember that the last two of consequence — TCP/IP and HTTP — decided who owned the internet. The company or coalition that controls how agents connect to enterprise data inherits an enormous structural advantage: default status, gravitational pull for every integration, and the ability to make non-compliant tools effectively invisible to automated workflows.

The strategic logic on each side is transparent. Anthropic and OpenAI built their enterprise businesses around models and chat-first interfaces, and MCP extended that reach into every SaaS tool without them having to own the tool. ARD flips the vantage point: it favors a world where agents discover and operate Google Workspace, Microsoft 365, and Salesforce CRM natively, keeping the incumbents' subscription revenue at the center of the workflow rather than downstream of someone else's model. As Crypto Briefing put it in an earlier report on the standard, the backers "aren't building ARD out of altruism."

There is also a credibility gap the alliance has to close. MCP's head start is larger than any press release makes it look, and enterprise software history is not kind to committee-designed standards. A five-company protocol shipping coherently and fast would be, as one industry newsletter noted this week, close to unprecedented.

## What to watch next

The tell will be adoption, not announcements. Watch whether Salesforce, Snowflake, and ServiceNow ship production ARD support in their flagship agent products — all three, notably, already support MCP natively today — and whether enterprises actually publish `ai-catalog.json` manifests at scale. Watch, too, for the Linux Foundation's forthcoming MCP Registry, which addresses the same discovery problem ARD targets and could either blunt the rival standard or absorb it. And watch the labs: if Anthropic and OpenAI stay conspicuously off the ARD list while remaining platinum members of the Agentic AI Foundation, it confirms that the industry has settled into an uneasy détente — open cooperation on the substrate, total war on who gets to be the default on top of it.

---

*Sources: The Information; Tom's Hardware; Crypto Briefing; andrew.ooo; Build Fast with AI; Linux Foundation.*
