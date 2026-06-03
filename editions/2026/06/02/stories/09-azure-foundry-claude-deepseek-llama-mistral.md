---
headline: "Azure AI Foundry Adds First-Party Support for Claude, DeepSeek, Llama, and Mistral"
slug: azure-foundry-claude-deepseek-llama-mistral
category: llms-genai
story_number: "09"
date: 2026-06-02
authors:
  - The Vault AI
tags:
  - microsoft
  - azure-ai-foundry
  - anthropic
  - claude
  - deepseek
  - meta-llama
  - mistral
  - build-2026
  - multi-model
sources:
  - name: Build Fast with AI
    url: https://www.buildfastwithai.com/blogs/ai-news-today-june-2-2026
  - name: ChatForest
    url: https://chatforest.com/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/
  - name: A Guide to Cloud and AI
    url: https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/
  - name: The Neuron
    url: https://www.theneuron.ai/explainer-articles/everything-microsoft-announced-at-microsoft-build-2026-explained/
  - name: Azure Blog - Claude in Microsoft Foundry
    url: https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/
---

Microsoft wants enterprises to stop thinking of Azure as an OpenAI-only shop -- and at Build 2026 on Monday, the company made its most aggressive move yet to prove it.

Azure AI Foundry, Microsoft's unified platform for deploying and managing AI models, now offers first-party support for frontier models from Anthropic, Meta, Mistral AI, and DeepSeek alongside its existing OpenAI integration. The result is a catalogue exceeding 11,000 models accessible through a single Azure endpoint, one billing relationship, and a unified governance layer -- making Azure the only major cloud provider offering both Claude and GPT frontier models on the same managed infrastructure.

## The New Model Lineup

The headline additions landing in Foundry as public previews and general availability releases:

**Anthropic Claude.** Claude Sonnet 4.5, Haiku 4.5, and Opus 4.1 entered public preview through Foundry's serverless deployment, with Claude Opus 4.8 following days later. All are deployable via Foundry's APIs with Microsoft Entra authentication, Azure billing eligible against Microsoft Azure Consumption Commitment (MACC) agreements, and support for Python, TypeScript, and C# SDKs. Notably, Claude also appears as a model option inside Microsoft 365 Excel Agent Mode and Copilot Researcher.

**Meta Llama.** Meta's Llama 3 family is available through Foundry's catalogue, bringing open-weight models into the same managed environment as closed-weight frontier systems.

**Mistral AI.** Mistral's lineup including Codestral, Ministral, Mistral Small, and Mistral Medium covers code generation, general-purpose chat, and multimodal tasks within Foundry's unified endpoint.

**DeepSeek.** DeepSeek R1 is generally available on both Foundry and GitHub, providing a reasoning-focused alternative at a different price-performance point.

Additionally, Fireworks AI reached general availability on Foundry, giving developers fast access to a broad range of open-source models through the same single Azure endpoint.

## Why Multi-Model Matters

The strategic logic is straightforward: no single model wins every task. A financial-services firm might route complex reasoning through Claude Opus for auditable chain-of-thought, use GPT-5.5 for high-throughput document processing, lean on Mistral for cost-efficient code generation, and deploy Llama locally for latency-sensitive inference. Until now, doing this across providers meant managing multiple billing relationships, authentication systems, and compliance frameworks.

Microsoft's answer is Model Router, a Foundry capability that can automatically route requests across models for cost and performance optimization at runtime. Combined with the Microsoft Agent Framework 1.0, which reached general availability at Build, developers can drop a Claude Agent SDK or OpenAI agent into a MAF workflow as a named participant while the orchestrator handles switching.

"You bring your code and your framework; the platform handles the rest," is how Microsoft framed Foundry's hosting philosophy during the keynote -- a line aimed directly at teams exhausted by infrastructure sprawl.

## The Numbers Behind the Platform

The scale of Foundry's ambition is visible in the raw figures. The model catalogue now exceeds 11,000 entries spanning frontier closed-weight models, open-source offerings, Microsoft's own seven-model MAI family, and specialized systems for vision, multilingual, time-series, and voice tasks. Hosted Agents -- Foundry's managed runtime for production AI agents -- reaches general availability by end of June 2026 with sub-100-millisecond cold starts and zero idle cost.

On the infrastructure side, Claude models currently run on Anthropic-managed infrastructure rather than Azure's regional compute, though EU-region native inference support is listed as coming later in 2026. This is a pragmatic concession: enterprises get unified billing and governance today while the compute layer converges over time.

## Competitive Context

The move positions Azure squarely against AWS Bedrock and Google Cloud's Vertex AI in the multi-model platform race. AWS Bedrock already offers Claude, Llama, and Mistral; Google Vertex provides Gemini alongside partner models. But Microsoft's argument is integration depth: Foundry models plug directly into Microsoft 365 Copilot, Teams, Excel Agent Mode, and the Agent 365 governance layer that IT administrators already manage.

For Anthropic specifically, the partnership expands distribution without diluting the brand. Claude appears in Foundry as a named, selectable model -- not abstracted behind a generic endpoint. Enterprises already committed to Azure spend can now adopt Claude without a separate procurement cycle, which lowers the friction that has historically kept organizations locked into whichever model their cloud provider defaults to.

## What This Means for Developers

The practical upshot for engineering teams is reduced switching cost. Building on Foundry's APIs means a model swap -- from GPT-5.5 to Claude Opus to Mistral -- requires changing a deployment configuration, not rewriting integration code. The Foundry Toolkit for VS Code, now generally available, lets developers create agents from templates, debug runs locally with trace visualization, and deploy to Foundry Agent Service directly from the editor.

The deeper signal is that the model layer is commoditizing faster than anyone expected. When Azure, AWS, and Google all offer the same frontier models, the competitive battleground shifts to orchestration, governance, cost management, and integration with the surrounding enterprise stack. Microsoft is betting that its breadth across identity (Entra), productivity (Microsoft 365), security (Defender and Purview), and developer tools (GitHub and VS Code) gives it an advantage no pure-play cloud can match.

For now, the multi-model era is officially here -- and Azure just made sure it has a seat at every table.
