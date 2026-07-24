# OpenAI Debuts 'Presence,' an Enterprise Platform for Mission-Critical Voice and Chat Agents

OpenAI on July 22, 2026 introduced Presence, a managed enterprise platform for building, governing and continuously improving production-grade AI agents that handle customer support, sales and internal operations across voice and chat. The launch marks a deliberate pivot for a company long defined by selling raw access to frontier models: with Presence, OpenAI is now selling the scaffolding around the model, the policies, guardrails, testing tools and human oversight that enterprises say they need before trusting an agent with a billing dispute or an insurance claim.

The pitch is aimed squarely at a problem OpenAI says has replaced the old one. As the company put it in its announcement, the challenge for enterprises is no longer proving that AI agents can work, it is making them reliable enough to do high-value work in production. Presence pairs model reasoning with company-defined policies, guardrails and escalation rules, and it is designed to keep an agent accurate and predictable even as products, prices and customer behavior shift over time.

## How Presence Works

Each Presence deployment starts with a narrow, specific job, resolving a billing issue, supporting an insurance claim, or handling an employee IT service request. The agent is granted access only to the knowledge bases and internal systems required for that workflow, and the company defines the operational boundaries: what the agent can do, when it needs human approval, and when a person should take over.

Before anything reaches a real customer, teams can run the agent through simulations covering common requests, edge cases and higher-risk scenarios, with automated graders checking whether it reached the right outcome, followed policy, used its tools correctly and escalated appropriately. Guardrails are built to intervene automatically when an interaction moves outside approved limits.

The distinctive piece is what happens after launch. Production sessions, escalations and quality signals surface gaps in the agent's performance, and OpenAI's Codex coding assistant investigates those signals and proposes updates. Human teams test each proposed change against the live version and approve a controlled rollout, a continuous-improvement loop OpenAI says lets an agent adapt without engineers rebuilding it from scratch.

## Proven on OpenAI's Own Phone Line

OpenAI says Presence is battle-tested rather than experimental, refined over years of enterprise deployments before its public unveiling. The clearest proof point is internal: Presence powers OpenAI's own English-language phone support channel, reachable at 1-888-GPT-0090, where it verifies callers, pulls account context and takes approved actions. Within weeks, the company says, it met or exceeded the benchmarks used to grade frontline human support quality and now resolves roughly 75 percent of inbound issues without a human stepping in. Its Codex-powered improvement loop, OpenAI adds, reduced human handoffs by 15 percentage points in just 10 days.

Several large enterprises are named as early design partners. Spanish banking group BBVA is exploring AI-powered voice support for everyday banking in Mexico. Japanese telecom giant SoftBank is testing natural Japanese-language conversations. And Australian insurer IAG is examining support during high-demand events such as severe weather.

'As a design partner for Presence, we are working closely with OpenAI to help shape and refine voice experiences for financial customer service, as part of our focus on delivering a faster, more seamless, and more personalized experience across every interaction,' said Daniel Ordaz, Head of AI Transformation at BBVA Mexico.

SoftBank's frontline teams, meanwhile, have rated the agent's dialogue highly. 'Our frontline teams have rated the agent's Japanese-language conversations highly for their natural and accurate quality,' said Tadahisa Murakami, Vice President and Head of the Data & Digital Transformation Division at SoftBank Corp.

## From Model Access to Managed Platform

Presence is the second major enterprise move in as many weeks, and the two together tell the story of OpenAI's strategy. On July 9, the company launched ChatGPT Work, a workplace platform whose agents accept a goal, connect to a company's apps and files, run independently for hours and return a finished artifact such as a spreadsheet or slide deck. Where ChatGPT Work targets internal productivity, Presence targets externally facing, mission-critical workflows where a wrong answer carries real cost, and it is delivered as a hands-on deployment rather than a self-serve app.

That shift moves OpenAI up the value chain, and into a crowded room. Google has been pushing Gemini Enterprise, Microsoft has assembled Agent 365 to manage fleets of agents, and a long tail of contact-center and conversational-AI vendors, most of whom lease OpenAI's own models, already occupy well-fortified positions in the customer-experience market. As one OpenAI spokesperson framed the differentiation to trade outlet No Jitter, Presence addresses a different challenge than standalone models or agent-building tools, helping enterprises consistently define how AI represents their business across channels with built-in simulations, graders and guardrails.

## What to Watch

Presence is not yet self-serve. It is available to eligible enterprise customers through a limited general-availability program, with deployments led by OpenAI's Forward Deployed Engineers and select global systems integrators; interested companies are told to contact their account team rather than sign up online. OpenAI has not disclosed pricing, saying deployments are scoped individually with broader pricing details to come as availability expands.

The open questions are whether OpenAI's high-touch, engineer-led model can scale beyond marquee design partners, how the 75-percent resolution figure holds up outside its own support line, and whether owning the full agent stack strains relationships with the many customer-experience vendors that build on its models. For now, the company says it will keep supporting voice customers who prefer direct access to its frontier models through the standard OpenAI API.