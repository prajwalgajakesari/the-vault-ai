The protocol war every conference panel spent 2025 predicting is over, and the anticlimax is the story. Google's Agent2Agent protocol has moved into the Agentic AI Foundation, the Linux Foundation-directed body that already houses Anthropic's Model Context Protocol. Axios broke it August 17, the AAIF posted the same day, and the transfer was dated August 20. Two rival labs, two flagship protocols, one governing board — and the same eight companies holding the platinum seats.

That is either the healthiest thing to happen to agent infrastructure in two years, or the moment a handful of incumbents quietly settled who defines how software talks to software for the next decade. Both readings survive contact with the facts.

## What MCP and A2A actually do

The conflation is constant and worth killing. These are not competing standards. They sit on different axes.

MCP, which Anthropic donated to the AAIF in December 2025, is vertical. It standardizes how a model or agent reaches *down* into tools and data — a file system, a Postgres database, a Jira instance. One integration, many clients.

A2A is horizontal. It standardizes how one agent reaches *sideways* to another, across framework and vendor boundaries. The mechanism is the agent card: a structured, published description of what an agent can do and how to reach it. Another agent reads the card, discovers the capability, and delegates the task without a human brokering the handoff. The AAIF is blunt about the split: "Where A2A fits is at the collaborative edge; where MCP fits is at the tool integration edge."

The problem A2A was built for is unglamorous and expensive. As the foundation described it, "Every new vendor relationship required the same integration work from scratch. The cost wasn't in the agents themselves but in the integrations between them."

## The road here

Google launched A2A in April 2025, then donated it to the Linux Foundation on June 23, 2025, seeding a project with AWS, Cisco, Microsoft, Salesforce, SAP, and ServiceNow. More than 100 companies backed the spec at that point. "By joining the Linux Foundation, A2A is ensuring the long-term neutrality, collaboration and governance that will unlock the next era of agent-to-agent powered productivity," Linux Foundation executive director Jim Zemlin said then.

Consolidation followed fast. IBM folded its Agent Communication Protocol into A2A in August 2025. A2A v1.0 shipped in March 2026 with multi-protocol bindings, version negotiation, multi-tenancy, and cryptographically signed agent cards. Backing now sits above 150 organizations.

It is running in production, not just demos. Huawei has standardized A2A as the link between Celia, its OS-level assistant, and in-app agents across HarmonyOS; Tencent's WeChat uses it to integrate with Huawei and other Android OEM assistants. Google Cloud supports it through ADK, Agent Engine, Cloud Run, and GKE; Azure AI Foundry lets agents expose A2A endpoints; AWS Bedrock AgentCore hosts A2A servers. Google Cloud and PayPal are extending it into commerce via the Agent Payments Protocol.

This move takes A2A out of the Linux Foundation's general portfolio and into the agent-specific one. "As organizations move multi-platform agentic systems into production, interoperability is becoming essential," said Rao Surapaneni, VP and GM of Business Application Platforms at Google Cloud. AAIF CTO Manik Surtani added that the foundation is "creating a neutral home where the community can collaborate on the standards that will enable agents from different vendors, frameworks, and organizations to work together."

## Does a neutral foundation produce a neutral standard?

Here is where skepticism earns its keep.

The AAIF has grown from a few dozen founding members to more than 250 in roughly eight months — though even that number is slippery. Axios reported the foundation launched in December 2025 with "fewer than 40 members"; other accounts put the founding cohort at 49.

The platinum tier is where the leverage sits: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI. That is not a cross-section of the industry. It is the eight organizations with the largest commercial stake in how agents interoperate, sitting on the body that decides how agents interoperate. The AAIF argues this is the point — "A2A's 150+ partner organizations include direct competitors. That breadth only holds together under governance that no single participant controls."

Both things are true. Neutral governance is real protection against one vendor's roadmap becoming everyone's constraint. It is not protection against a set of vendors converging on a shape that suits all of them and disadvantages the next entrant. The Linux Foundation logo governs IP and process; it does not govern who writes the code, who staffs the technical steering committees, or whose use case the spec accommodates first. Kubernetes lived under the CNCF for years while still being unmistakably Google-shaped. Foundations launder incumbency more reliably than they dilute it.

Note also what the platinum roster omits. The two most impressive A2A deployments — Huawei's HarmonyOS assistant and Tencent's WeChat — belong to companies with no seat at the top tier. The protocol's most convincing proof points sit outside the governance that produced it.

And interoperability is not trustworthiness. Mahesh Shanmugasundaram, lead AI solutions architect at Seekr, put it sharply: "Interoperability only expands that already existing trust gap. While the protocol standardizes the pipe, organizations decide what travels through it." He describes the failure mode as an "AI game of telephone" — each agent treating the previous agent's output as verified fact, so a small hallucination at step one arrives at step five wearing authority it never earned.

## What to watch

Three things. First, TSC composition: A2A and MCP stay separate projects with separate technical steering committees, so watch who fills those seats and whether maintainer headcount tracks the platinum list. Second, whether A2A's identity work — signed agent cards, delegated authority — becomes mandatory or stays a checkbox. Verification is the difference between a protocol and a liability. Third, AAIF executive director Mazin Gilbert's framing to Axios is the tell: "Companies don't want just one protocol; they want the whole stack to be open." The foundation now hosts instructions, runtime, tool connectivity, traffic mediation, and agent-to-agent comms. Owning the whole stack is the ambition. Whether "open" and "one roof" can coexist at that scale is next year's question.
