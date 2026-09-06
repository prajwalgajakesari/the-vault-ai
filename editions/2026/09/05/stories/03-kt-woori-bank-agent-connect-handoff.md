South Korea's Woori Bank wants its chatbot to stop talking and start doing. On August 31, KT Corp. said it had won Woori's "AI chatbot and consultation bot rebuild" and begun development. At the center is a new KT solution called Agent Connector — and what matters is not better answers. It is that Agent Connector is built to hand a live customer conversation to an AI agent that can execute banking tasks.

That is a different category of risk. A chatbot that gets an answer wrong produces a bad answer. An agent with write access to a core banking system that misreads an intent produces a transaction. In Korea, where consolidated financial-sector AI guidelines took effect on June 22, that distinction is now supervised rather than debated.

## What KT actually announced

The verifiable facts are thin. KT won the rebuild of Woori's non-face-to-face consultation channels, and will link AI Banker — Woori's AI-based financial consultation service — with AI agents to expand consultation scope and task-processing functions. The stated goals: better intent classification, higher inbound resolution rates, and extension of AI into outbound calls and branch consultations.

Agent Connector is the plumbing. Per KT, it connects chatbots, consultation bots, AI Banker and AI agents and carries consultation context between them, so a customer who switches channels keeps the thread. KT calls the end state an "agentic AICC" — a contact center that handles the task behind an inquiry rather than routing it to a human.

What KT did not announce: contract value, go-live date, which model powers it, which transactions agents may complete, or how consent and audit trails are captured at the handoff. None of that appears in the release or the Korean coverage. Task execution is an architecture commitment here, not a shipped feature.

KT's comparable work sets a floor for scale. On August 10, KT said it completed a next-generation AICC for NH NongHyup Bank valued at 40 billion won, roughly $29 million, quadrupling the tasks the AI call bot handles without a human from 45 to 180 and cutting handling times around 20%. KT now runs AICC for four of Korea's five major commercial banks.

Kim Won-tae, head of KT's Public and Financial Business Headquarters, framed the shift: "AI chatbots and consultation bots in the financial sector are evolving beyond simple inquiry guidance toward understanding customer needs and supporting actual task processing." Kim Sun-woo, head of Woori's AI Data Business Department, kept the bank's side modest: "We will reduce inconveniences customers experience during consultations and provide faster and more consistent financial services." Both quotes are AI-translated from Korean.

## Two vendors, one agent stack

KT is not the only company building agents inside Woori. In April, Samsung SDS was named preferred bidder on a separate Woori project: more than 175 agents across 29 core tasks in five areas including corporate lending, asset management and internal controls, on its FabriX platform. It deploys roughly 90 agents this December and phases through August 2027, claiming a 30% gain in processing speed. Il-jin Oak, vice president of Woori's Digital/IT unit, described the goal as moving from "AI that asks and answers" to "AI that works and resolves issues."

So one vendor owns the front door and another the agent estate behind it. Agent Connector is the seam.

## Why the handoff is the hard part

Three problems sit at that boundary, and better models solve none.

Authorization step-up: a session authenticated well enough to read a balance is not authenticated well enough to move money. The handoff must re-establish assurance mid-conversation without breaking the seamless-continuity promise that is Agent Connector's pitch. Continuity and re-authentication pull in opposite directions.

The record: Korean consumer protection obligations around explanation and suitability attach to recommendation and sale. If an agent moves from discussion into a product action, the bank needs a replayable artifact of what was disclosed and agreed — and context that flows seamlessly across channels is what most resists being frozen into one.

Liability: when an agent acts on a misclassified intent, fault could sit with the bank, KT as integrator, or the model provider. Korean regulation puts the duty on the licensed institution — Woori carries exposure for software it did not write.

The Financial Services Commission published consolidated draft AI Guidelines for the Financial Sector on December 22, 2025, merging three earlier documents; they took effect June 22, after the AI Basic Act commenced January 22. Voluntary in form and supervisory in practice, they set out seven principles and expect AI decision-making bodies, dedicated risk functions, explainability controls and human oversight of final decisions. One is titled use of AI as a support tool — framing that presumes a human at the decision point, which an agent completing a transaction end to end tests directly. Expect the first agent-executable tasks to be low-value and reversible: card reissue, address changes, lost-card blocks, lookups. Not lending. Not investment sales.

## The telco as AI integrator

That KT is the vendor says something about Korea's market structure. Network separation and data residency rules push financial AI onto domestic infrastructure, favoring a local telco with a sovereign cloud over a hyperscaler. KT's five-year, multibillion-dollar Microsoft partnership, announced in 2024, was built for this: Korea-tuned models, a sovereign cloud on Microsoft Cloud for Sovereignty for regulated financial and public customers, and $450 million of KT infrastructure. KT also fields its own Korean model line, Mi:dm, and sits in a consortium picked in August to distribute AI nationally under a rule routing at least half of queries through certified Korean models. What runs Agent Connector, KT has not said.

## What to watch

The disclosure that matters is the task list — the transactions Woori lets an agent complete without a human. That, not the press release, is the real measure. Watch also for a named model, for how Agent Connector meshes with FabriX, and for whether the FSC addresses agentic execution as it supervises against the new guidelines. If this works, KT sells it to the other three banks whose contact centers it runs. If it stalls, it stalls at the handoff, not the conversation.
