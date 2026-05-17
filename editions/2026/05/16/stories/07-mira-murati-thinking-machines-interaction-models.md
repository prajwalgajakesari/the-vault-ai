---
title: "Mira Murati's Thinking Machines Reveals Real-Time Multimodal AI Interaction Models"
slug: mira-murati-thinking-machines-interaction-models
category: llms-genai
story_number: "07"
date: 2026-05-16
---

# Mira Murati's Thinking Machines Reveals Real-Time Multimodal AI Interaction Models

The startup has introduced a new class of AI architecture it calls Interaction Models — and the benchmarks suggest the rest of the industry may need to rethink how it builds conversational AI from the ground up.

---

On May 11, 2026, Thinking Machines Lab — the AI startup founded by former OpenAI CTO Mira Murati — pulled back the curtain on its first in-house model: a system it calls an Interaction Model. Built from scratch to perceive and respond across audio, video, and text simultaneously, the reveal marks the company's clearest statement yet on where it believes conversational AI has gone wrong — and how it intends to fix it.

The announcement, long anticipated since the company raised $2 billion at a $12 billion valuation just ten months ago, lands Thinking Machines squarely in competitive territory with OpenAI's GPT-Realtime and Google's Gemini Flash — but with a fundamentally different architectural argument at its core.

## The Problem With How Every Other Lab Built Interaction

Most AI systems handle real-time conversation through a patchwork of components: voice-activity detection identifies when a user stops speaking, a transcription layer converts audio to text, a language model processes the text, and a text-to-speech engine converts the response back to audio. Each handoff introduces latency. Each boundary is a seam where the experience frays.

Thinking Machines says that is not a tuning problem. It is an architectural one.

"Most labs treat autonomy as the goal and interactivity as scaffolding around a turn-based core," said Murati in the company's blog post accompanying the release. "We think the way we work with AI matters as much as how smart it is."

The company's answer is TML-Interaction-Small, a 276-billion-parameter Mixture-of-Experts model — though only 12 billion parameters are active at any given moment — trained from scratch for continuous, simultaneous perception and generation. Rather than waiting for a user to finish speaking, the model processes input and generates output in overlapping 200-millisecond micro-turns. It can listen while it speaks, interrupt when appropriate, and react to visual context from a live video feed — behaviors the company describes as "full duplex" interaction.

## A Two-Model Architecture

The architecture splits responsibility between two systems. The Interaction Model stays live with the user: it listens, backchannel-signals, asks clarifying questions, and holds the conversational thread. A separate Background Model handles heavier cognitive work — reasoning chains, tool calls, web searches — running asynchronously and passing results back to the Interaction Model without breaking the flow of the conversation.

The design is a deliberate inversion of the standard approach, where a single large model tries to both reason deeply and respond instantly. Thinking Machines argues that this compromise has forced every major lab to accept an interaction experience that feels fundamentally unnatural.

## The Numbers Back the Claim

On FD-bench v1.5 — a benchmark for interaction quality that measures responsiveness, turn-taking naturalness, and multimodal coherence — TML-Interaction-Small scored 77.8, compared to 47.8 for OpenAI's GPT-Realtime 2.0. In raw latency terms, the model achieves a 0.40-second response time, faster than Google's Gemini 3.1 Flash at 0.57 seconds and well ahead of OpenAI's GPT-Realtime 2.0 at 1.18 seconds.

Those are prototype numbers, and Thinking Machines is careful to note that TML-Interaction-Small is not yet commercially available. Access is currently limited to a small cohort of research partners, with a broader rollout expected later in 2026. Larger variants of the model, which would offer greater reasoning depth, remain too computationally expensive to serve at scale — a constraint the company says it is actively working to overcome.

## Context: A High-Stakes Debut

The release carries significant weight beyond the technical merits. Thinking Machines was co-founded in February 2025 by Murati alongside a roster of former OpenAI heavyweights including John Schulman, Barrett Zoph, Lilian Weng, Andrew Tulloch, and Luke Metz. The company secured backing from Andreessen Horowitz, Nvidia, AMD, Cisco, and Jane Street — and unusually, from the government of Albania, Murati's country of origin, which amended its national budget to make a $10 million investment.

"We started Thinking Machines to advance human-AI collaboration, and this is our first bet on what that looks like," Murati wrote. The framing is deliberate: where competitors have raced toward autonomous agents that act independently, Thinking Machines is making a different bet — that the future of AI lies in tighter, more natural collaboration with humans, not replacement of them.

## Analysis: Architecture as Argument

What makes the Interaction Models announcement notable is not just the benchmark performance — it is the clarity of the thesis behind it. Thinking Machines is not claiming to have built a smarter model. It is claiming to have identified a category error in how the entire industry has approached the problem.

Whether that argument holds up at commercial scale remains to be seen. The MoE architecture and the two-model split introduce their own engineering complexities, and competitors like OpenAI and Google are not standing still. But in a landscape where most AI announcements compete on raw capability metrics — context windows, benchmark scores, parameter counts — Thinking Machines is betting that the quality of the interaction experience itself is an undervalued dimension of the market.

If the FD-bench scores translate to real-world deployments, that bet could prove prescient. And given the team assembled in San Francisco and the runway that $2 billion provides, the rest of the industry would be wise to take the argument seriously.

The broader rollout for TML-Interaction-Small — and the larger variants still in development — is expected in the second half of 2026.

---

*Sources: [Thinking Machines Lab Blog](https://thinkingmachines.ai/blog/interaction-models/), [VentureBeat](https://venturebeat.com/technology/thinking-machines-shows-off-preview-of-near-realtime-ai-voice-and-video-conversation-with-new-interaction-models), [Semafor](https://www.semafor.com/article/05/13/2026/mira-muratis-thinking-machines-previews-interaction-models), [Analytics Drift](https://analyticsdrift.com/mira-murati-thinking-machines-interaction-model/)*
