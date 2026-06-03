---
headline: "Microsoft Launches AI Agent Store for Windows With 85 Percent Developer Revenue Share"
slug: microsoft-windows-agent-store-85-share
category: business
story_number: "04"
date: 2026-06-02
author: The Vault — AI Edition
sources:
  - name: FourWeekMBA
    url: https://fourweekmba.com/ai-microsoft-windows-agent-store-framework-build-2026/
  - name: Windows News
    url: https://windowsnews.ai/article/microsoft-build-2026-windows-becomes-the-platform-for-ai-agents.420503
  - name: ChatForest
    url: https://chatforest.com/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/
  - name: Windows Developer Blog
    url: https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/
  - name: The Neuron
    url: https://www.theneuron.ai/explainer-articles/everything-microsoft-announced-at-microsoft-build-2026-explained/
---

# Microsoft Launches AI Agent Store for Windows With 85 Percent Developer Revenue Share

At Build 2026 in San Francisco on Monday, Microsoft declared that Windows is no longer just an operating system for humans. It is now a platform for AI agents — complete with a curated marketplace, an open-source developer framework, and a revenue split that undercuts every major app store on the planet.

The centerpiece announcement: the Windows Agent Store, where developers can distribute and sell AI agents that run as first-class citizens inside Windows. Microsoft will take just 15 percent of revenue, leaving 85 percent for developers. For context, Apple and Google both claim 30 percent from their respective app stores. Microsoft is wielding economics as a weapon in what is shaping up to be the defining platform war of the agent era.

## From Assistants to Async Coworkers

Satya Nadella opened his keynote with a thesis that reframed the entire conference. "Windows is no longer a platform for human users only — agents are now first-class citizens in the runtime, the tooling, and the distribution model," the CEO said, describing a shift from synchronous AI assistants that wait for prompts to asynchronous coworkers that execute long-running tasks in the background.

The distinction matters. Today's AI tools — chatbots, copilots, search assistants — operate in a call-and-response loop. A user asks, the model answers, and the interaction ends. Microsoft is betting the next phase looks fundamentally different: agents that triage your email overnight, join meetings on your behalf, detect configuration drift in your deployment pipeline, and prepare design templates before you sit down at your desk.

Adobe and Zoom are among the early design partners. Adobe demonstrated an agent that learns a designer's layout habits and automatically prepares InDesign templates. Zoom showed an agent that can attend meetings for a user and push summarized action items directly into Microsoft Planner. Both examples signal that this is not vaporware — enterprise software companies are already building for the platform.

## A Three-Layer Architecture

Microsoft shipped a full technical stack to support the vision, organized into three distinct layers.

The **Windows Agent Framework (WAF)**, open-sourced under an MIT license, is the developer SDK. Agents are defined in YAML manifests that are portable across local Windows machines, Windows 365 Cloud PCs, and Azure Arc-enabled edge devices. A single agent definition can start as a local process on a laptop, escalate to a cloud GPU when the workload demands it, and publish to Azure as a service — with no re-architecture required. The MIT license is a deliberate signal: developers can fork WAF and deploy agents on-premises without any Azure dependency.

The **Windows Agent Runtime**, previewed for Insiders in June, provides OS-level APIs that embed agents directly into the Windows shell. Unlike traditional applications that run as isolated processes, agents in the Runtime operate as native OS citizens with access to structured data — JSON, XML, and PDF files in the initial preview. Vision-based agents that can interpret screen pixels are planned for 2027.

The **Windows Agent Store** sits on top as the distribution and monetization layer, with its 85 percent revenue split and mandatory security reviews for every listed agent.

## The Enterprise Security Play

Microsoft clearly anticipated the objection that autonomous agents with deep OS access present an enormous attack surface. The answer is AgentGuard and a new technology called Microsoft Execution Containers (MXC).

MXC is a cross-platform, policy-driven execution layer that lets developers declare exactly what an agent can access — specific files, network endpoints, system resources — with containment boundaries enforced at runtime. IT administrators can set rules through Intune, such as preventing an agent from sending financial data to an external API without explicit human approval. Defender, Entra, Intune, and Purview protections layer on top to provide runtime security against malicious prompts, data leakage, and risky agent behavior.

Pavan Davuluri, Executive Vice President for Windows and Devices, framed it bluntly in the official Windows Developer Blog: "As agents become more capable and autonomous, they are delivering material productivity gains. But they are also introducing new risk."

Every agent is assigned a verifiable identity — either a local ID or a cloud-provisioned Entra credential — so that all activity can be attributed and audited. The goal is to make agent actions as traceable as human logins.

## Why the Revenue Share Matters

The 85/15 split is not just a developer perk. It is a calculated land grab. Microsoft is racing to establish Windows as the default agent platform before Apple or Google can build equivalents. By offering economics that are roughly twice as favorable as competing app stores, Microsoft is creating a financial incentive for developers to build Windows-first.

The timing is strategic. The broader industry is converging on the idea that AI agents — not apps — will be the primary unit of software distribution within a few years. Whoever controls the agent marketplace controls the next generation of platform economics. Microsoft is making the bet that generous revenue terms, combined with deep OS integration and enterprise security tooling, will be enough to lock in early developer commitment.

## The Bigger Picture at Build

The Agent Store was part of a sweeping set of announcements at Build 2026. Microsoft also unveiled Project Polaris, its in-house AI model that will replace GPT-4 in GitHub Copilot by August, signaling reduced dependence on OpenAI. Azure Agent Mesh will federate agent execution across on-premises servers, cloud PCs, and edge devices when it reaches general availability in Q4 2026. And new on-device models — Aion 1.0 Instruct and Aion 1.0 Plan — will enable fully local agentic reasoning on Windows hardware without cloud round-trips.

Taken together, the message is unmistakable. Microsoft is not incrementally improving Windows. It is repositioning the entire operating system as the runtime layer for an agent-driven economy — and it is paying developers handsomely to build that future on its platform.

The Windows Agent Runtime preview is available to Windows Insiders starting this month. The Agent Store timeline has not been confirmed, but early design partner access is expected through the Windows Insider program.