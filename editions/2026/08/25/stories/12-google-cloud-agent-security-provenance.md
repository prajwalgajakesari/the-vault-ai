Google Cloud spent 2026 arguing that the bottleneck on autonomous AI is not model quality or GPU supply. It is identity. In a State of AI Infrastructure report published August 24, the company found that 79% of technology leaders named security, governance, or operations — not cost, not capacity — as their most significant challenge to scaling inference. Google Cloud's answer is blunt: stop treating AI agents as software, and start treating them as principals. Give every agent a cryptographic identity, then force its traffic through a proxy that is allowed to say no.

"AI agents are the ultimate insiders," wrote Doug Ko, senior product marketing manager for security at Google Cloud, in the post accompanying the report. "We grant them permission to read emails, query databases, and trigger API calls. They don't just retrieve information, they take action." The same survey found 35% of senior IT decision makers citing insufficient security for multi-system access as a primary blocker to agentic deployment.

## What actually shipped

The machinery arrived at Google Cloud Next '26 in Las Vegas, April 22 to 24, and was detailed in a May 6 post by Abhishek A Hemrajani, senior director of product management for Google Cloud Security. "Traditional controls simply aren't built for autonomous AI agents that interact with sensitive data at machine speed," Hemrajani wrote.

The foundation is Agent Identity — a first-class principal type distinct from both human identities and generic service accounts, built on the open SPIFFE standard, cryptographically attested and automatically provisioned. Agent Identity for Agent Runtime is generally available. Agent Identity for the Gemini Enterprise Agent Platform is in preview, as is Agent Identity Auth Manager, which handles OAuth flows when an agent acts on a user's behalf.

Above that sits Agent Gateway, which brokers every agent-to-agent and agent-to-tool connection, plus Identity-Aware Proxy for Agents — in preview — enforcing IAM policy using agent identities and contextual attributes derived from the Model Context Protocol. IAM allow and deny policies for Agent Identity are generally available; Principal Access Boundary, which sets hard ceilings an agent can never exceed regardless of inherited permissions, is in preview. Model Armor, Google's runtime guardrail against prompt injection, tool poisoning, and data leakage, now runs inline for Agent Gateway, Agent Runtime, and Google Cloud MCP servers.

Two things are not yet shipped. Unified Access Policy — the layer that can mandate human-in-the-loop approval for sensitive agent actions — is listed as "coming soon." And the advice to require human sign-off on irreversible operations such as high-value financial transfers and resource deletions comes not from a product page but from a bylined August 4 Cyber Defense Magazine article by Harika Rama Tulasi Karatapu, a network security customer engineer at Google. It is architecture guidance, not an enforced control.

The provenance argument is likewise doctrine rather than product. In a February 28 Cloud CISO Perspectives post, Royal Hansen, Google's vice president of engineering for privacy, safety, and security, wrote that the company advocates "implementing tamper-proof provenance for risks associated with models, orchestration servers, tools called by agents, and third-party security, mirroring but expanding on traditional software supply chain best practices." That extends binary authorization thinking into the agent stack — but for now it remains a recommendation.

## The threat model underneath

The urgency is not theoretical. OWASP's GenAI Security Project, in the 2026 edition of its State of Agentic AI Security and Governance, maps prompt injection to six of the ten categories in its Top 10 for Agentic Applications — and unlike the 2025 edition, it catalogs CVEs and breach reports rather than hypotheticals. In March, a backdoored build of LiteLLM, the model gateway used by CrewAI, DSPy, and Microsoft GraphRAG, sat on PyPI for roughly three hours and drew nearly 47,000 downloads. CVE-2026-22708, disclosed against Cursor, let attackers poison an agent's execution environment so allowlisted commands like git branch delivered arbitrary payloads — the allowlist auto-approved exactly what the attacker needed.

That is the confused deputy problem in new clothes. An agent holding broad credentials on an operator's behalf turns every input channel it reads into an authorization channel.

## Why It Matters

Agent identity is quietly becoming the new IAM primitive, and the arithmetic explains why. Palo Alto Networks' 2026 Identity Security Landscape, based on a survey of 2,930 cybersecurity decision-makers, found machine identities now outnumber human identities 109 to 1 — and 79 of those 109 are AI agents. Ninety-nine percent of organizations have adopted agents. Only 37% say they could revoke an agent's credentials. Only 30% have immutable audit logging of what those agents did.

For twenty years IAM assumed the principal was a person or a static service account with a deterministic execution path. An agent is neither. It decides its next action from text it read a moment ago, and that text may be hostile. Google Cloud's bet is that the fix is not a new category of tool but a new principal type inside the old model — which is why the SPIFFE lineage matters more than the marketing. Thomas Kurian, Google Cloud's CEO, framed it at Next as mapping every agent ID to "defined authorization policies that are traceable and auditable," adding: "We're bringing zero trust verification to every agent and at every orchestration step."

Francis deSouza, Google Cloud's chief operating officer, put the harder part plainly. Access control for agents, he said, "may change over time in a way that's more dynamic than human identities." Static grants do not describe a principal whose job changes mid-task.

## What to Watch

Three things. First, whether Unified Access Policy ships with real human-in-the-loop enforcement, or whether HITL stays a pattern customers wire up themselves. Second, whether tamper-proof provenance for models, MCP servers, and agent tools gets an attestation format and a verifier — the way binary authorization did for containers — or remains a whitepaper position. Third, portability: SPIFFE is open, but Agent Identity, Agent Gateway, and Model Armor are Google Cloud services, and multicloud shops will want to know whether an agent's identity survives leaving the perimeter that issued it.
