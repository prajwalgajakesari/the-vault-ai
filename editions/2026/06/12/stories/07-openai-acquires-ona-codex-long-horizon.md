## OpenAI Acquires Ona to Give Codex Days-Long Autonomy on Real Software Projects

OpenAI announced on June 11, 2026, that it has agreed to acquire Ona — the cloud infrastructure startup formerly known as Gitpod — in a deal designed to give its Codex coding agent a persistent, secure place to work across hours and days rather than minutes. Financial terms were not disclosed; the transaction remains subject to customary regulatory approvals.

The acquisition marks the most direct signal yet that OpenAI views Codex not merely as a developer productivity tool but as an autonomous software engineering platform capable of carrying large, multi-day workloads from start to finish without human supervision between sessions.

## What Ona Is — and What It Was

Founded in 2020 in Kiel, Germany, by Johannes Landgraf and Christian Weichel, the company spent its first five years under the Gitpod brand, building cloud-based development environments that let engineers work in reproducible, containerized workspaces rather than configuring local machines. By the time it rebranded to Ona in September 2025, it had served more than 2 million developers and pivoted squarely toward AI-agent infrastructure: pre-configured cloud sandboxes where AI agents can access tools, credentials, repositories, and runtime systems in a controlled, auditable environment.

That pivot was prescient. As AI coding agents matured from single-file autocomplete into multi-step orchestrators capable of spinning up services, running test suites, and issuing pull requests, the missing ingredient was not model intelligence — it was a trustworthy execution surface. Ona built exactly that.

## The Technical Gap Ona Closes

Current agentic coding tools face a hard constraint: when the user closes their laptop or ends a session, the agent loses its context and the work stops. For short tasks — fixing a bug, refactoring a function — that is tolerable. For the kinds of work enterprises actually need automated (migrating a legacy codebase to a new framework, wiring together integrations across dozens of microservices, generating comprehensive test suites across hundreds of files), session-bound execution is a fundamental bottleneck.

Ona's technology provides what OpenAI describes as "persistent environments where agents can access the tools, systems, and context they need to make progress over time." Crucially, those environments run inside the customer's own cloud, meaning credentials are scoped, activity is logged, and data never leaves the organization's security boundary. The agent keeps working after the laptop is closed; the human checks back in to review progress, provide direction, and approve the next phase.

"Enterprises want powerful agents that can do real work while meeting the security and control requirements of their environments," said Thibault Sottiaux, Core Products Lead at OpenAI. "Ona will help us make Codex easier to deploy securely across production workflows for customers operating at the highest standards of trust and scale."

Ona's co-founder and CEO Johannes Landgraf framed the deal in terms of what agents have lacked: "Agents need more than intelligence; they need a trusted workspace. We built Ona to give agents cloud environments with the context, control and collaboration enterprises require. Joining OpenAI lets us bring that foundation into Codex, helping organizations deploy agents with confidence and giving humans more agency over their work."

## Part of a Deliberate Acquisition Strategy

The Ona deal is not a one-off. OpenAI has been systematically acquiring the tooling layer around its models. Earlier this year the company acquired Promptfoo, an open-source evaluation framework widely used to test LLM outputs for correctness, safety, and regression. Taken together, the moves sketch an emerging playbook: rather than waiting for the ecosystem to build production infrastructure around Codex, OpenAI is buying it in.

The pattern mirrors what happened in cloud computing a decade ago, when hyperscalers acquired DevOps tooling companies to reduce friction between development and production. OpenAI appears to be making a comparable bet: that the developers who deploy Codex for serious work will want a vertically integrated stack where model, execution environment, and evaluation tooling come from a single, accountable vendor.

## The Agentic-Coding Arms Race

The timing matters because the competitive pressure on OpenAI's coding story is intense. Anthropic's Claude Code has emerged as the most terminal-native agentic coding experience available, capable of understanding entire codebases, editing files autonomously, running shell commands, and creating pull requests without leaving the developer's local environment. Cursor, from Anysphere, hit $2 billion in annualized recurring revenue by February 2026 — doubling roughly every two months since mid-2025 — and its Composer 2.5 ships parallel agent orchestration natively. GitHub Copilot, meanwhile, has integrated both Claude and Codex models in public preview since early 2026, giving Microsoft a hedged position across the field.

OpenAI's answer with Ona is to compete on a dimension none of those tools fully own: enterprise-grade, long-horizon autonomy with customer-controlled infrastructure. Where Claude Code excels at local, developer-supervised workflows and Cursor dominates the IDE-centric experience, Codex with Ona is positioning for the data-center end of the market — the IT and platform engineering teams that need to automate sustained work across the software lifecycle at organizational scale.

Codex is already reaching that scale in usage terms: OpenAI reports more than 5 million weekly active users, a 400% increase from earlier in 2026. The challenge now is converting that breadth into the kind of deep, production-critical deployments that justify enterprise contracts.

## What to Watch Next

The most consequential near-term question is how quickly the Ona team — joining OpenAI's Codex group post-close — can ship the customer-controlled execution model into generally available products. Enterprise sales cycles are long, and competitors are not standing still: Anthropic has been vocal about Claude Code's enterprise momentum, and Microsoft's dual-model positioning in Copilot gives it unusual flexibility.

Watch also for whether OpenAI's reported S-1 filing (the company submitted a confidential draft to the SEC on June 8) accelerates or shapes the product roadmap here. A publicly traded OpenAI will face pressure to demonstrate that Codex is converting weekly active users into durable, high-margin enterprise contracts — and persistent, secure agent execution is precisely the feature that turns a developer tool into an enterprise platform.

Finally, the Gitpod-to-Ona rebrand hints at a broader thesis: the developer tooling category is collapsing into the AI agent infrastructure category. Companies that built for human developers are now rebuilding for AI agents as the primary user. How that repositioning plays out — and whether OpenAI can absorb Ona's culture and technology without losing the agility that made Gitpod compelling — will define whether this acquisition is remembered as a turning point or a distraction.
