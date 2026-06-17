# Defakto Raises $30.75 Million to Secure the Identities of AI Agents

For most of computing history, identity security meant managing people: employees logging in, contractors granted temporary access, the occasional privileged administrator. That assumption is breaking down. Inside the modern enterprise, the overwhelming majority of "users" are not people at all. They are software services, automated pipelines, cloud workloads, and, increasingly, autonomous AI agents that authenticate, request data, and act on systems thousands of times a second.

Defakto, a California-based identity company formerly known as SPIRL, has raised $30.75 million in a Series B round to build the security layer for exactly those non-human actors. The round, announced October 21, 2025, was led by XYZ Venture Capital, with participation from The General Partnership, Bloomberg Beta, WndrCo, Adverb Ventures, J.P. Morgan, and Michael Coates, the former chief information security officer of Twitter. The financing brings the company's total raised to roughly $50 million.

## What the company is building

Defakto describes its product as a non-human identity and access management (IAM) platform, purpose-built to secure "every automated interaction." In practice that means replacing two things security teams have leaned on for decades and quietly come to dread: static credentials and overprivileged service accounts.

Static secrets — long-lived API keys, hardcoded passwords, certificates that rarely rotate — are convenient to issue and notoriously hard to track. They leak into source code, logs, and configuration files, and they grant standing access that lives on long after anyone remembers creating it. Defakto's pitch is to swap those for dynamic, verifiable identities that cover the full lifecycle of a machine actor, from a microservice to a CI/CD pipeline to an AI agent. The platform is designed to work across AWS, Azure, Google Cloud, and hybrid environments, and to slot into development workflows without adding friction for engineers.

The company was founded by Danny Oliveri, who serves as chief executive, and Eli Nesterov, the chief technology officer. Oliveri frames the problem as a structural gap rather than a tooling shortfall.

"Every enterprise has invested in securing its people. But non-humans are now the majority of users, and their identities are still governed by outdated, secret-based models that create mounting technical debt," he said.

He went further on what the round is meant to fund: "We didn't build another tool to give you more visibility or manage secrets. We built a platform to eradicate them, eliminate overprivileged access, and give enterprises the same foundation for machines and AI that IAM gave them for people." The company has said the capital will go toward accelerating product development and expanding its go-to-market efforts.

## Why "non-human identity" became a category

The funding lands in the middle of one of the fastest-moving stories in enterprise security: the realization that machines now vastly outnumber humans on corporate networks, and that almost nobody is governing them properly.

Non-human identities — service accounts, API keys, certificates, machine tokens — have been growing by more than 40 percent year over year, according to market research tracking the space. In some enterprises they already outnumber human identities by ratios ranging from 40-to-1 to more than 100-to-1. Each of those identities can hold credentials, carry permissions, and reach sensitive systems. Unlike human accounts, they rarely face multi-factor authentication, periodic access reviews, or an offboarding process when the workload they served is retired.

That asymmetry has made machine identities a favored target. They frequently carry elevated privileges and operate without the oversight applied to employees, which makes a single leaked key or forgotten service account a quiet path deep into an environment. Recent breach analyses have repeatedly traced major intrusions back to compromised non-human credentials rather than phished employees. Industry bodies have taken note: a 2026 KPMG cybersecurity report flagged non-human identities as a critical priority for CISOs.

The arrival of agentic AI has turned a chronic problem acute. AI agents do not merely hold credentials — they make autonomous decisions about which systems to access and what actions to take, often chaining together calls across many services to complete a task. An agent that can read a database, call an external API, and trigger a workflow needs an identity, scoped permissions, and an audit trail, just as a human would. But agents are spun up and torn down far faster than any HR process, and they can act at machine speed and machine scale. Vendors across the identity sector — from incumbents like Okta and SailPoint to a wave of startups — have spent the past year reframing their roadmaps around "agent identity" and zero-trust controls for autonomous systems.

## The competitive and analytical picture

Defakto is not alone in chasing this market, and the crowded field is itself a signal. Established secrets-management and identity vendors are extending into non-human identity, while specialized startups argue that the problem demands a ground-up architecture rather than a bolt-on. Defakto's differentiation rests on the claim that visibility and secrets management are insufficient — that the goal should be to eliminate static secrets entirely in favor of short-lived, cryptographically verifiable identities issued and revoked automatically.

That is a defensible thesis, and the investor roster lends it credibility: a former Twitter CISO and J.P. Morgan are the kind of buyers and operators whose participation suggests the problem resonates with the people who would actually deploy the product. It is worth noting, too, that $30.75 million is a meaningful but not enormous Series B by 2026 cybersecurity standards, where stealth-stage rounds have crossed nine figures. Defakto is betting on being early and architecturally right in a category that is still defining its own boundaries, rather than outspending rivals.

The harder questions are the ones every entrant in this space faces. Replacing static secrets requires deep integration into the cloud platforms and developer pipelines that enterprises already run, and incumbents own those relationships. Standards for how AI agents should authenticate and carry identity are still immature and contested. And "non-human identity" risks becoming a label stretched across products that do quite different things, from discovery and inventory to issuance and governance.

## What to watch

The signal in Defakto's round is less about one company than about a shift in where security budgets are heading. For two decades, identity meant protecting humans. As enterprises wire autonomous agents into core operations, the locus of risk is moving to the machines — and the firms that can credibly manage who, or what, an AI agent is, and what it is allowed to touch, are positioning themselves at the center of the next phase of enterprise security. Whether Defakto becomes, in Oliveri's words, the "de facto standard" will depend on adoption that this round is only beginning to fund.
