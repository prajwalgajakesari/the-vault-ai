---
title: Anthropic Adds Private MCP Tunnels and Self-Hosted Sandboxes to Claude Managed Agents
slug: anthropic-managed-agents-mcp-tunnels
category: llms-genai
story_number: "07"
date: 2026-05-20
sources:
  - https://9to5mac.com/2026/05/19/anthropic-enhances-claude-managed-agents-with-two-new-privacy-and-security-features/
  - https://www.testingcatalog.com/anthropic-launches-new-secure-tools-for-claude-managed-agents/
  - https://www.infoq.com/news/2026/05/code-with-claude/
  - https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/
  - https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/
  - https://www.infoq.com/news/2026/05/claude-mcp-tunnels/
---

# Anthropic Adds Private MCP Tunnels and Self-Hosted Sandboxes to Claude Managed Agents

Anthropic drew a bright line between what an AI agent can do and where it is allowed to do it — and handed that second decision entirely to enterprises.

At its Code with Claude developer conference in London on May 19, 2026 — marking Anthropic's first developer gathering outside the United States — the company announced two new infrastructure capabilities for its Claude Managed Agents platform: self-hosted sandboxes, now available in public beta, and MCP tunnels, currently accessible by request in research preview. Together, the features let organizations deploy autonomous Claude agents while keeping both code execution and access to internal systems firmly inside their own security perimeters.

## The Problem They Are Solving

Enterprise AI adoption has run into a consistent wall: security and compliance teams cannot sign off on agents that execute arbitrary code on third-party infrastructure or that require internal APIs and databases to be publicly exposed. Until now, organizations using Claude Managed Agents had to accept that tool execution — the moment when an agent actually runs code, queries a database, or calls a service — happened on Anthropic's infrastructure. For regulated industries and security-sensitive organizations, that was often a non-starter.

The new features attack both sides of that problem simultaneously. Self-hosted sandboxes relocate where execution happens. MCP tunnels redefine how agents reach internal systems.

## Self-Hosted Sandboxes: Your Infrastructure, Anthropic's Orchestration

Self-hosted sandboxes draw a clear architectural boundary between orchestration and execution. Anthropic continues to handle the agent loop — the reasoning, context management, multi-step planning, and error recovery that make Claude's agents capable of autonomous work. But when the agent actually needs to run code or invoke a tool, that work now occurs inside infrastructure the customer controls.

Supported infrastructure partners at launch include Cloudflare, Daytona, Modal, and Vercel, each tuned for different enterprise profiles. Cloudflare runs sandboxes in microVMs at scale with granular outbound network controls. Daytona provides stateful sandboxes that can be paused and restored with full state retention — useful for long-running engineering tasks. Modal, built for AI workloads, adds container-based sandboxes with access to both CPU and GPU resources. Vercel combines virtual machine-level security with fast startup times and allows customers to bring their own cloud environment while managing firewall and credential policies themselves.

Real-world deployments announced alongside the feature underscore the breadth of use cases. Rogo, an AI platform for institutional finance, is building an analyst agent that uses Claude Managed Agents for reasoning while routing all data handling through Vercel for compliant processing. DoorDash is constructing an internal productivity agent running on Modal. Clay's engineering agent, Sculptor, uses Daytona to build and monitor automation workflows, taking advantage of that provider's stateful sandbox persistence across sessions.

The architecture reflects an explicit design choice: "The agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure, while tool execution moves to your own configured environment," as Anthropic described in documentation accompanying the launch. The split gives enterprises the AI reasoning layer without surrendering the execution layer.

## MCP Tunnels: Private Networks Without Public Exposure

MCP tunnels address the complementary challenge of connecting agents to internal systems without opening those systems to the internet. The mechanism is architecturally straightforward: rather than require organizations to punch inbound holes in firewalls or expose private API endpoints publicly, a lightweight gateway is deployed inside the private network and opens a single outbound encrypted connection back to Anthropic's infrastructure.

The security model is deliberately layered. The tunnel carries three independent encryption channels: mutual TLS between Anthropic and the tunnel edge, an inner TLS session between Anthropic's backend and the customer's proxy — terminated using a certificate only the customer holds — and OAuth authentication on each individual MCP server. The transport layer is provided by Cloudflare, which can observe connection metadata such as timing, byte volume, and subdomain identifier, but cannot read MCP request or response payloads because the inner TLS layer is opaque to it.

"A lightweight gateway opens a single outbound connection, end-to-end encrypted, with no inbound firewall rules or public endpoints required," Anthropic stated in its technical documentation. The goal is to let agents reach internal databases, private APIs, or ticketing systems as tools — without those systems ever receiving inbound traffic from the public internet.

MCP tunnels work with both Claude Managed Agents and the Messages API directly, giving organizations the same private connectivity option whether they manage their own agent loops or rely on Anthropic's managed platform. That dual compatibility is meaningful: companies already using the Messages API to build custom orchestration can adopt MCP tunnels without migrating to the full managed agents stack.

## Why This Architecture Matters

The split between orchestration and execution represents a meaningful shift in how cloud AI services can be structured. Most current AI platforms treat the model, the orchestration layer, and the execution environment as a unified stack that lives entirely on the provider's infrastructure. By externalizing execution, Anthropic is acknowledging that for a growing segment of enterprise customers, control over where code runs matters as much as the capability of the model doing the reasoning.

The four-provider sandbox ecosystem signals a deliberate platform strategy as well: rather than build a single proprietary execution environment, Anthropic is positioning Claude Managed Agents as an orchestration layer that plugs into existing infrastructure choices. Organizations that have already standardized on Cloudflare Workers, Modal for ML workloads, or Vercel for application deployment do not need to adopt a new execution environment — they bring their existing stack and connect it to Claude's reasoning capabilities.

MCP tunnels represent a similarly pragmatic bet on standards. The Model Context Protocol, which Anthropic open-sourced in late 2024, has grown into the dominant framework for connecting AI agents to external tools and data sources. By building private network access directly into MCP rather than a proprietary connector format, Anthropic ensures compatibility with the broader MCP ecosystem — and solves a security requirement that previously forced enterprises to choose between agent capability and network isolation.

For sectors with strict data residency requirements — financial services, healthcare, government — that tradeoff was often decisive. Self-hosted sandboxes and MCP tunnels together remove it from the equation.

## Availability and What Comes Next

Self-hosted sandboxes are available now to all Claude Platform customers in public beta. MCP tunnels require a separate access request given their research preview status, signaling that Anthropic is still iterating on the feature before broad rollout.

The Code with Claude London conference itself — Anthropic's first European developer event — served as the backdrop for both announcements, reflecting a broader push to build developer community outside the company's San Francisco base. Other announcements at the event included updates to Claude Code, Anthropic's AI-assisted development tool.

For enterprises evaluating AI agent platforms, the combined announcement removes two of the most commonly cited deployment blockers: data residency concerns around execution environments, and the security exposure of making internal systems reachable from the public internet. Whether the four-provider sandbox roster expands and how the MCP tunnel research preview matures into general availability will be among the features to watch in Anthropic's platform roadmap through the rest of 2026.

The orchestration stays in San Francisco. The execution, increasingly, can stay with you.
