Anthropic has rolled out a significant wave of updates to Claude Managed Agents throughout May, adding capabilities that transform the platform from a simple agent deployment tool into a full-fledged multi-agent orchestration system. The headline features -- dreaming and multiagent orchestration -- represent the company's vision of AI agents that learn from experience and collaborate with each other.

The updates, announced across multiple releases in early and mid-May, come just weeks after Managed Agents launched in April 2026. The rapid iteration pace signals Anthropic's urgency to establish its platform as the default infrastructure for enterprise AI agent development.

"We are seeing customers build agent systems in weeks that would have taken months with custom infrastructure," said Mike Krieger, Anthropic's Chief Product Officer, in a May 7 blog post. "These updates take that further by letting agents improve themselves and work together."

## Dreaming: Memory That Learns

The most novel addition is a feature Anthropic calls "dreaming," which extends Claude's memory capabilities by reviewing past sessions to find patterns and help agents self-improve. When enabled, an agent periodically analyzes its interaction history to identify recurring questions, common failure modes, and opportunities for better responses.

The dreaming process runs asynchronously between active sessions, generating updated behavioral guidelines that the agent applies to future interactions. In practice, this means a customer support agent might notice that users frequently ask about a specific policy detail and proactively incorporate that information into its responses.

The feature draws inspiration from memory consolidation in biological systems, where the brain replays and reorganizes experiences during sleep. Anthropic was careful to note that dreaming operates within the agent's existing safety guardrails and does not modify the underlying model weights.

## Multiagent Orchestration

The second major addition enables a lead agent to decompose complex tasks and delegate subtasks to specialist agents, each configured with its own model, system prompt, and tool set. The specialists work in parallel on a shared filesystem, with the orchestrator managing coordination and result synthesis.

This architecture enables sophisticated workflows that would be unwieldy for a single agent. An enterprise deployment might have a lead agent that receives a financial analysis request, delegates data extraction to one specialist, statistical modeling to another, and report formatting to a third, then assembles the final deliverable.

## Security and Infrastructure Updates

Anthropic also shipped two infrastructure features in mid-May aimed at enterprise security requirements. MCP tunnels allow agents to securely connect to internal tools behind corporate firewalls, while self-hosted sandboxes move agent code execution to customer-controlled infrastructure.

The self-hosted sandbox option, launched in public beta, lets enterprises run agent workloads on their own infrastructure or through managed providers like Cloudflare, Daytona, Modal, and Vercel. This addresses a key concern for regulated industries where data residency and audit requirements prevent using shared cloud infrastructure.

## Finance-Specific Templates

Rounding out the May updates, Anthropic released ten ready-to-run financial agent templates covering tasks including pitchbook generation, KYC screening, earnings review, month-end close automation, and reconciliation workflows. The templates, announced May 5, are designed to help financial services firms deploy production agents without building from scratch.

## What to Watch

The combination of dreaming, multiagent orchestration, and enterprise security features positions Managed Agents as more than a hosting platform -- it is becoming an opinionated framework for how AI agents should be built. Watch for competitive responses from OpenAI and Google, both of which are building their own agent deployment infrastructure.