# Camunda Unveils ProcessOS Agentic Operating System for Enterprise AI Orchestration

*With a bold declaration that every enterprise process is already legacy, Camunda is betting that the next decade belongs to companies willing to tear up their workflows and rebuild them from the ground up.*

---

In front of 1,200 enterprise leaders and technologists from 25 countries gathered in Amsterdam for the annual CamundaCon, Camunda CEO Jakob Freund made a blunt diagnosis of where AI adoption stands in corporate America — and across the world. Chatbots, recommendations, AI-assisted search: none of it is enough. "Every process in your enterprise is legacy," Freund told the crowd on May 20. "It was designed for a world where AI did not exist." His prescription came packaged as ProcessOS, a new agentic operating system unveiled at the conference that Camunda says will let enterprises discover, re-engineer, and continuously optimize their core business processes using AI — not bolt AI onto the ones they already have.

The announcement marks the company's most ambitious product expansion since it pivoted hard into agentic orchestration six months ago. ProcessOS is now available in closed beta for selected enterprises, with a full release targeted for Camunda version 8.10.

---

## What ProcessOS Actually Is

ProcessOS is not a replacement for Camunda's existing orchestration platform — the one that already processes millions of concurrent workflow instances daily for more than 700 organizations, including nine of the ten largest U.S. banks. It is an intelligence layer that sits inside the Camunda Hub and wraps four tightly integrated AI agents around the full lifecycle of a business process.

The four agents map to four verbs: Discover, Re-engineer, Build, and Optimize. Together, they are designed to take a process from hidden operational reality — buried inside legacy systems, tribal knowledge, and disconnected documentation — through to a running, AI-native workflow that can be continuously tuned against business outcomes.

Discovery is where the system starts. ProcessOS queries live systems, analyzes operational data, and uses structured questionnaires to surface how a process actually works — not how anyone assumed it worked. In Camunda's own internal pilot, a Discovery Agent queried real production systems and produced complete process documentation in under an hour. Roughly 66 percent of the input came from system data; the remaining third came from short questionnaires completed by process participants. A three-hour stakeholder review followed.

The Re-engineering phase is where ProcessOS's ambition comes into focus. Rather than optimizing within existing constraints, it proposes structural transformation based on defined business outcomes. In Camunda's Quote to Cash pilot — a process spanning 30 people, six divisions, 17 roles, 12 systems, and 14 document artifacts — the Re-engineering Agent proposed collapsing 79 touchpoints in the current state down to just 2 in the happy path. The resulting design routes most interactions through a single Slack surface for employees, with a new Deal Agent coordinating the other agents behind the scenes.

The Build Agent then generates the actual implementation artifacts: BPMN process diagrams, DMN decision tables, data mappings, agent prompts, integrations, and UI forms. Camunda estimates engineers handled the remaining 20 percent that required hands-on configuration.

The results from the Quote to Cash pilot are striking. Cycle time dropped from 115 days to 80. Error rates fell from 10 percent to approximately 2 percent. The team estimates around 6,000 person-hours freed per year — roughly five hours saved per deal closed. And a transformation that would traditionally take nine to twelve months of calendar time was compressed into four weeks.

---

## Governance Baked In, Not Bolted On

Enterprise AI adoption has repeatedly stalled not on capability but on accountability. ProcessOS attempts to address this directly through what Camunda calls "verification by design." Visual process models explicitly show which steps are performed by AI agents, under which conditions, and which steps require human judgment. No process modification reaches production without human review and approval. Every change goes through a human-in-the-loop checkpoint before deployment.

The system also maintains a growing organizational knowledge base — a catalog of approved design patterns, connectors, policies, and procedures that compounds over time. ProcessOS prioritizes these approved building blocks when generating new processes, incorporating human feedback to improve its understanding of how a specific enterprise actually operates.

"The same shift that is happening to software development is coming for business operations," said Daniel Meyer, Camunda's CTO, during the keynote. "Developers used to write every line of code. Now AI writes more and more of it. Business processes are next. In ProcessOS, you describe the desired outcome in natural language, and then ProcessOS creates the process, deploys it, and continuously optimizes it based on the business outcomes you defined."

The current AI coding agent embedded in ProcessOS is Claude Code, though Camunda has designed the architecture to remain open — not locked to any single model or vendor.

---

## The AWS Angle

ProcessOS runs natively on AWS, with deep integration into Amazon Bedrock for foundation models and Amazon Bedrock AgentCore for agent memory, identity, and gateway services. Camunda is also available on the AWS Marketplace with production-ready reference architectures for Amazon EKS, ECS, and EC2. The partnership has been formally recognized: just one day before CamundaCon, on May 19, Camunda received the Rising Star Technology Partner of the Year award at the AWS Partner Summit in Hamburg.

The Bedrock AgentCore integration is significant. AgentCore, AWS's infrastructure layer for running and managing AI agents at enterprise scale, provides exactly the kind of memory, identity management, and gateway services that long-running business process automation demands. Coupling ProcessOS with AgentCore means Camunda is positioning itself as the orchestration backbone for enterprises that have already committed to AWS — a large and growing segment of the enterprise market.

---

## Market Validation and Enterprise Reaction

Camunda's timing aligns with a broader Forrester assessment of where enterprise process automation is heading. "GenAI has pushed the boundaries of automatable processes," the firm wrote in its Adaptive Process Orchestration Software Landscape report for Q2 2026, "and APO is an evolutionary step toward the promise of autonomous business operations. This market is evolving toward AI-first agentic approaches that blend AI with deterministic workflows while vendors consolidate tools into orchestration backbones emphasizing governance, observability, and hybrid human-in-the-loop execution."

The announcement drew a notable public endorsement from Barclays. "ProcessOS tackles the real reason AI adoption stalls in large enterprises: we can't build tomorrow's processes using only what we know today," said Lily Wang, Managing Director at Barclays. "Transformation starts with a bold vision of the future — and ProcessOS turns that vision into a practical path forward."

That kind of enterprise credibility matters for what Camunda is attempting. The company already has significant footprint in regulated industries — financial services, insurance, healthcare — where governance and auditability are not differentiators but minimum requirements. ProcessOS's verification-by-design approach is calibrated for exactly that environment.

---

## A Bet on the Decade

Freund's framing at CamundaCon was deliberately sweeping: "Every company will reinvent itself or die. The constraint is not access to AI but knowing where it belongs in your business and redesigning your operations and enterprise architecture around it."

That framing — provocative, almost confrontational — is a calculated positioning move. Camunda is not competing on model quality or foundation capabilities. It is competing on orchestration, governance, and the institutional knowledge layer that lives between an enterprise's intent and its actual operations. By embedding AI into the process-building lifecycle itself, ProcessOS attempts to make the Camunda platform increasingly indispensable the longer an enterprise uses it.

For enterprises considering where to place their agentic infrastructure bets, the closed beta is the first real opportunity to test whether the Quote to Cash results can be replicated across their own operations. The evidence so far — four weeks instead of twelve months, 115-day cycles compressed to 80, error rates cut by four-fifths — is compelling enough to deserve serious attention.

Camunda is hosting a webinar on the topic on June 24 for U.S. and Americas-based teams, and June 25 for European participants.
