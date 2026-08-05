# Google's Gemini Enterprise Agent Platform Hits General Availability, and Its 'Spark' Agent Learns to Drive Chrome

Google Cloud this week moved the core of its Gemini Enterprise Agent Platform into general availability, retiring the "public preview" caveats that had let enterprises experiment while quietly holding production budgets in reserve. In the same stretch, a very different kind of agent, the consumer-facing Gemini Spark, began doing something that only weeks ago sounded like a lab demo: driving a user's own logged-in copy of desktop Chrome to book property viewings and tee up flight searches. Together, the two announcements mark August 2026 as the moment Google stopped talking about agents as a promise and started shipping them as infrastructure.

## From preview to production

The Gemini Enterprise Agent Platform, the rebranded and expanded successor to Vertex AI that Google unveiled at Cloud Next '26 in April, saw a cluster of its most consequential services reach general availability. That list includes Agent Runtime, Agent Identity, Agent Gateway, Agent Registry, Agent Memory Bank, Agent Evaluation, and Agent Observability, a stack Google frames as everything a company needs to build, scale, govern, and optimize agents from one console rather than shuttling between three.

The two features that matter most for anyone worried about turning autonomous software loose inside a corporate network are state and identity. Through Agent Memory Bank, agents can now maintain continuity across sessions, picking up a task where they left off "even if days or weeks have passed," in Google's phrasing, rather than starting cold each time. For enterprise workflows that unfold over multiple days, an insurance claim, a procurement cycle, a customer support escalation, persistent state is the difference between a chatbot and a colleague.

Agent Identity is the security half of that equation. Rather than borrowing a shared service account, every agent gets its own native IAM identity built on open standards, tied to the agent's lifecycle and scoped to least privilege. Google says the design mitigates token theft by binding access directly to the agent runtime, produces non-repudiable audit logs of every action an agent takes, and automatically retires credentials when an agent is decommissioned, eliminating the dormant keys that haunt security teams.

## Real deployments, real quotes

The GA push arrived with customer proof points rather than hypotheticals. Comcast rebuilt its Xfinity Assistant on the platform, moving from scripted automation to a multi-agent system.

"Agent Runtime has been a massive accelerator, allowing us to deploy a sophisticated multi-agent architecture that increases digital containment while ensuring secure, grounded interactions via Gemini," said Rick Rioboli, Chief Technical Officer, Connectivity & Platforms at Comcast.

L'Oréal, another named adopter, framed its interest around governance as much as capability. "Google Cloud gives us the resilience, the multi-LLM flexibility, and the enterprise-grade trust framework we need to scale this platform globally, while keeping human oversight at the center," said Etienne Bertin, the company's Group CIO, a line that neatly captures why identity and observability, not raw model horsepower, have become the selling points of this generation of agent tooling. Google is backing the ecosystem with a $750 million innovation fund for partners building agents on the platform.

## Spark takes the wheel in Chrome

While the enterprise stack hardened, the consumer story got more provocative. Gemini Spark, Google's agentic assistant, gained the ability to operate the desktop version of Chrome directly, a shift away from its previous reliance on a remote, Google-managed browser. With permission, Spark can use a person's own logged-in accounts and saved passwords to run multi-step errands: researching and comparing flight options and beginning the booking process, or scheduling viewings for saved apartment listings, moving between pages without the user guiding every click.

Crucially, Spark returns control to the user before sensitive actions such as payments, a deliberate handoff that keeps a human in the loop at the moment money changes hands. Google also says it has added defenses against prompt injection, the attack in which malicious instructions hidden in a webpage try to hijack an agent. The Chrome browsing capability began rolling out in the U.S. on August 3, while access to Spark itself expanded to Google AI Pro subscribers in more than 160 additional countries.

The design philosophy quietly echoes the enterprise side: give the agent scoped access, log what it does, and force a return to human judgment at the highest-risk step. An agent using your saved passwords is exactly the sort of power that makes the least-privilege, auditable model on the enterprise platform feel less like compliance theater and more like a necessary blueprint.

## The agent race tightens

Google's dual announcement lands in a market that has abruptly reorganized itself around production-grade agents. Microsoft has pushed its Copilot Studio and autonomous agents deep into Microsoft 365 and Azure, leaning on Entra for agent identity. Salesforce has bet the company narrative on Agentforce, selling outcome-priced digital labor to its CRM base. OpenAI has advanced its own computer-using and browser-operating agents for consumers and developers alike. Everyone, in other words, is now shipping agents that can take actions, not just answer questions.

What differentiates the current phase is that the competition has moved from capability to control. The hard problems are no longer "can the agent do the task" but "who is this agent, what is it allowed to touch, and can we prove what it did afterward." Google's decision to make Agent Identity a first-class IAM primitive, complete with non-repudiable auditing, is a direct answer to the governance anxieties that have kept many pilots from graduating to production. Spark driving Chrome with saved passwords is the same wager aimed at consumers, betting that trust, not novelty, is the constraint on adoption.

## What to watch

The open questions are now operational. Will persistent, multi-day agent state hold up against the messiness of real enterprise systems, and how will security teams respond to fleets of individually credentialed agents that must themselves be monitored, rotated, and retired? On the consumer side, prompt injection remains the unsolved frontier: an agent with your logged-in accounts is a lucrative target, and the first high-profile exploit of a browser-driving assistant will test whether "returns control before payment" is a sufficient guardrail. The technology has clearly crossed from demo to deployment. Whether the governance scaffolding Google is racing to pour keeps pace with the autonomy it is unleashing is the story of the next quarter.
