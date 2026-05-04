---
headline: "Microsoft Agent 365 Hits General Availability With $15 Per User Enterprise Agent Control Plane"
slug: microsoft-agent-365-general-availability
category: business
story_number: "01"
date: 2026-05-03
---

# Microsoft Agent 365 Hits General Availability With $15 Per User Enterprise Agent Control Plane

Microsoft on May 1 flipped the switch on Agent 365, moving the product from preview to general availability and establishing what the company calls the first enterprise control plane purpose-built for governing autonomous AI agents at scale. Priced at $15 per user per month as a standalone offering -- or bundled into the new $99-per-user Microsoft 365 E7 Frontier Suite -- Agent 365 signals Redmond's clearest bet yet that the next battleground in enterprise software is not building AI agents, but managing the sprawl they create.

## The Product

Agent 365 gives IT administrators, security teams, and line-of-business leaders a single pane of glass to observe, govern, manage, and secure AI agents running across an organization. The platform features a centralized agent registry, OpenTelemetry-based telemetry and monitoring, and extends Microsoft's existing security stack -- Entra for identity, Purview for data governance, Defender for threat detection -- to cover non-human entities for the first time.

Crucially, Agent 365 is not limited to Microsoft's own ecosystem. The platform works with agents built on OpenAI, Anthropic's Claude, ServiceNow, Workday, and custom LangChain implementations. For agents running on competing clouds, Microsoft is launching an Agent 365 registry sync feature in public preview, allowing administrators to discover agents on AWS Bedrock and Google's Gemini Enterprise Agent Platform and import them into the central registry for monitoring.

There is no additional per-agent charge for the first 10,000 managed agents per tenant. Beyond that threshold, a graduated consumption model applies at roughly $0.15 per agent per month at list price, with volume discounts available for large deployments.

## What Executives Are Saying

Vasu Jakkal, corporate vice president of Microsoft Security, framed the launch as a response to a rapid shift already underway inside large organizations. "These agents are no longer experimental. We are seeing them deeply embedded in organizations, in the operational structure of these organizations, with people using them," Jakkal said in a briefing around the launch. She positioned Agent 365 as an extension of zero-trust principles to AI: "We think about security for agents very similar to security for people."

CEO Satya Nadella, who has spent much of 2026 evangelizing the agentic AI paradigm, reiterated his vision at the launch event. "The best way to think about these agents are just as your teammates," Nadella said. "Sometimes we mysticize these agents as things that take a lot of effort to build. Our vision is that it should be as simple as creating a Word doc or a PowerPoint slide."

## Why This Matters

The general availability of Agent 365 crystallizes a strategic pivot that has been building inside Microsoft for over a year: the company is no longer just selling AI capabilities -- it is selling the governance layer around them. This is a significant distinction. As enterprises move from experimenting with a handful of copilots to deploying hundreds or thousands of autonomous agents across procurement, HR, finance, and customer service, the management problem becomes at least as important as the capability itself.

The $15 per user price point is deliberately accessible, positioned well below the $30 per user that Microsoft charges for Microsoft 365 Copilot. The message is clear: governance should not be an afterthought bolted on at premium cost but a foundational layer that ships alongside agent deployment. The bundling into the E7 suite at $99 per user -- which also includes M365 E5 and Copilot -- creates a natural upsell path while making Agent 365 feel like table stakes rather than a luxury add-on.

The multicloud registry sync is perhaps the most strategically interesting piece. By offering to manage agents running on AWS and Google infrastructure, Microsoft is positioning Agent 365 as a Switzerland-style neutral control plane -- an unusual move for a hyperscaler that typically prefers lock-in. The implicit argument is that wherever your agents run, your governance should be centralized, and Microsoft wants to own that center. It is the same playbook that made Active Directory and later Entra ID indispensable: control the identity layer and the rest of the stack follows.

For competitors, this raises uncomfortable questions. Google and Amazon have their own agent orchestration tools, but neither has shipped a dedicated governance-first product at this price point. Startups in the agent observability space -- companies building monitoring and audit trails for autonomous AI -- now face a well-funded incumbent bundling their core value proposition into a $15 SKU attached to the world's largest enterprise software distribution channel.

## What to Watch Next

The real test for Agent 365 will be adoption velocity. Microsoft reportedly had over 10,000 organizations in the preview program, but converting preview tenants to paid licenses is a different challenge entirely. Watch for the company's fiscal Q4 2026 earnings call in July, where management will almost certainly be pressed on Agent 365 attach rates alongside Copilot seat growth. Also worth monitoring: whether the multicloud registry sync moves from preview to general availability before the end of 2026 -- that timeline will reveal how seriously enterprises are demanding cross-cloud agent governance versus how much of it remains aspirational. Finally, keep an eye on the per-agent consumption pricing above the 10,000-agent threshold; as agent counts scale exponentially, that graduated model could become a meaningful revenue line -- or a friction point that pushes large customers to negotiate hard.
