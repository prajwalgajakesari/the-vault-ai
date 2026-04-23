---
headline: "Cloudflare Wraps Agents Week With New Compute, Security, and Agent Toolbox"
slug: cloudflare-agents-week-2026-tools
category: llms-genai
story_number: 10
date: 2026-04-22
author: The Vault AI
---

# Cloudflare Wraps Agents Week With New Compute, Security, and Agent Toolbox

**Cloudflare used its week-long Agents Week event to ship more than a dozen new services aimed at turning its global network into the default operating environment for autonomous AI agents -- a bet that the next wave of software will be written, deployed, and secured by code that never sleeps.**

The announcements, which concluded on April 20, spanned compute infrastructure, security primitives, developer tooling, and what the company calls the "emerging agentic web." Taken together, they represent Cloudflare's most concentrated push yet to define the infrastructure layer beneath the AI agent boom.

"The way people build software is fundamentally changing," said Matthew Prince, Cloudflare co-founder and CEO. "We are entering a world where agents are the ones writing and executing code."

## Compute: 100x Faster, Fraction of the Cost

At the center of the compute story is **Dynamic Workers**, a new isolate-based runtime that Cloudflare says delivers 100x speed improvements over traditional containers at a fraction of the cost. Paired with that is the general availability of **Sandboxes**, persistent Linux environments that give agents full shell and filesystem access when a lightweight isolate is not enough.

Cloudflare also unveiled **Durable Object Facets**, which let Dynamic Workers instantiate Durable Objects with their own isolated SQLite databases -- enabling developers to build platforms that run persistent, stateful code generated on the fly. The company rearchitected its **Workflows** control plane to handle 50,000 concurrent executions with a 300-per-second creation rate, a capacity increase designed for durable background agents that may run for hours or days.

## Security: Zero Trust for Non-Human Traffic

Perhaps the most consequential announcements addressed the security gap that opens when autonomous agents need access to internal systems. Cloudflare introduced **Cloudflare Mesh**, a private networking fabric that extends zero-trust access to users, nodes, and AI agents alike. Integrated with Workers VPC, Mesh grants agents scoped access to private databases and APIs without exposing credentials.

"It doesn't work for a coding agent running autonomously on your laptop that needs to query a staging database at 2am," said Nikita Cano, Senior Product Manager at Cloudflare, describing the limitations of traditional VPN-based authentication for agent workloads.

**Outbound Workers for Sandboxes** add a programmable, zero-trust egress proxy that lets developers inject credentials and enforce dynamic security policies at the network edge. The company also shipped scannable API tokens, enhanced OAuth visibility, and GA for resource-scoped permissions -- all aimed at implementing least-privilege architecture for agent identities.

Rita Kozlov, VP of Product Management, framed the design principle: "For organizations, this means the same permissions that govern a user's actions in the dashboard also apply to that user's agent."

## The Agent Toolbox

The week produced a dense stack of new developer primitives:

- **Artifacts** (beta): Git-compatible versioned storage that enables developers to create tens of millions of repositories, giving agents a permanent, forkable home for code and data.
- **Agent Memory** (private beta): A managed service that extracts and persists conversation context, giving agents recall across sessions.
- **AI Search**: A hybrid vector-and-keyword search primitive with relevance boosting, purpose-built for retrieval-augmented generation pipelines.
- **Browser Run**: Enhanced headless browser access with 4x higher concurrency limits, live view, and session recordings for debugging agent web interactions.
- **Agent Readiness Index**: A scored assessment built on Cloudflare Radar that evaluates how well a website supports autonomous agents by checking for robots.txt, llms.txt, structured data, and markdown delivery.

The company also introduced **Agent Lee**, an in-dashboard agent that helps developers troubleshoot and manage their Cloudflare stack using sandboxed TypeScript, and previewed **Project Think**, a next-generation Agents SDK component designed for long-running, multi-step reasoning tasks.

## High-Performance LLM Inference

In a companion blog post, Cloudflare engineers detailed the custom stack they built to run high-performance large language models on their infrastructure. The team made Moonshot AI's trillion-parameter Kimi K2.5 available through Workers AI with a 3x speed improvement, reducing p90 time-per-token from roughly 100 milliseconds to 20-30 milliseconds through prefill-decode disaggregation. Their proprietary Rust-based **Infire** inference engine now supports multi-GPU configurations, achieves cold-start times under 20 seconds, and delivers up to 20 percent higher tokens-per-second throughput. A new compression system called **Unweight** achieves up to 22 percent model footprint reduction without meaningful quality loss.

## Analysis: Building the Agent Cloud Before Agents Arrive at Scale

Cloudflare's strategy mirrors what AWS did a decade ago for microservices: own the primitives so deeply that switching costs become architectural. By bundling compute, storage, networking, security, and inference into a single platform -- and by processing 241 billion tokens and 20 million AI Gateway requests internally already -- Cloudflare is eating its own cooking at a scale that lends credibility to the pitch.

The partnership signal matters too. OpenAI's Rohan Varma, a product lead, endorsed the platform directly: "Cloud agents are quickly becoming a foundational building block for how work gets done, and with Cloudflare, we're making it dramatically easier for developers to deploy production-ready agents."

The open question is timing. Production AI agents remain rare outside developer tooling and customer support. Cloudflare is building the airport before the planes have been certified. But if autonomous agents do become the dominant software paradigm -- and the venture capital pouring into the space suggests many believe they will -- the company that owns the infrastructure layer wins disproportionately. This week, Cloudflare made its case that the layer should look like theirs.
