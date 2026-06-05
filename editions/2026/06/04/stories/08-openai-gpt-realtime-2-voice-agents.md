---
headline: "OpenAI Launches GPT-Realtime-2, Bringing GPT-5-Class Reasoning to Voice Agents"
slug: openai-gpt-realtime-2-voice-agents
category: llms-genai
story_number: 8
date: 2026-06-04
---

# OpenAI Launches GPT-Realtime-2, Bringing GPT-5-Class Reasoning to Voice Agents

OpenAI shipped three new audio models on May 7 that collapse transcription, reasoning, translation, and speech synthesis into a single voice-intelligence suite for developers -- a move that could reshape the economics of the fast-growing voice AI market and put pressure on an entire ecosystem of specialized vendors.

The flagship release, GPT-Realtime-2, is the first voice model to carry what OpenAI describes as GPT-5-class reasoning, enabling live voice agents that can listen, think through complex requests, call multiple tools simultaneously, handle interruptions, and sustain long conversations without losing context. Two companion models round out the launch: GPT-Realtime-Translate, which handles real-time speech translation across more than 70 input languages and 13 output languages, and GPT-Realtime-Whisper, a streaming speech-to-text engine that transcribes audio as the speaker talks.

The Realtime API, which had been in beta, is now generally available.

## The Technical Leap

The most consequential technical change in GPT-Realtime-2 is the context window expansion from 32,000 to 128,000 tokens -- a 4x increase that makes longer sessions and complex agentic workflows feasible without the external state-stitching that developers previously relied on. The model also introduces adjustable reasoning effort across five levels -- minimal, low, medium, high, and xhigh -- with low set as the default to keep latency tight for routine interactions while allowing developers to dial up deliberation for harder requests.

On OpenAI's internal benchmarks, GPT-Realtime-2 at high reasoning effort scores 15.2% higher than its predecessor GPT-Realtime-1.5 on Big Bench Audio, the company's audio-reasoning evaluation. At xhigh effort, instruction-following performance on the Audio MultiChallenge benchmark improves by 13.8%. Function calling -- the backbone of any voice agent that needs to take action in the real world -- jumped from 49.7% to 66.5% on the ComplexFuncBench audio evaluation.

New conversational features address the awkward silences that have plagued production voice agents. Preambles let an agent say phrases like "let me check that" while it executes tool calls behind the scenes. Parallel tool calling allows the model to fire multiple backend requests simultaneously while narrating what it is doing. And improved recovery behavior surfaces failures gracefully rather than freezing mid-conversation.

## Early Adopters Report Production-Grade Gains

The launch customer list reads like a cross-section of enterprise voice use cases: Zillow, Priceline, Intercom, Glean, Genspark, and Deutsche Telekom are among the companies that tested the new models before general availability.

The most striking early result comes from Zillow. "What stood out about GPT-Realtime-2 was the intelligence and tool-calling reliability it brings to complex voice interactions," said Josh Weisberg, SVP and Head of AI at Zillow. "On our hardest adversarial benchmark, this translates to a 26-point lift in call success rate after prompt optimization -- 95% versus 69%. GPT-Realtime-2 is also materially more robust on Fair Housing compliance, which is critical for our business."

The translation model is drawing attention from companies serving multilingual markets. BolnaAI, a voice-AI startup building for Indian languages, reported meaningful improvements in regional language accuracy. "In our evals across Hindi, Tamil, and Telugu, GPT-Realtime-Translate delivered 12.5% lower Word Error Rates than any other model we tested, along with lower fallback rates, higher task completion, and latency that sustained natural conversation," said Prateek Sachan, Co-founder and CTO at BolnaAI.

Deutsche Telekom is testing the translation model for multilingual customer support, where lower latency and stronger fluency can make cross-language service interactions feel more natural.

## Aggressive Pricing Puts Competitors on Notice

The pricing structure signals that OpenAI is playing for market share. GPT-Realtime-2 is priced at $32 per million audio input tokens -- dropping to just $0.40 per million for cached inputs -- and $64 per million audio output tokens. GPT-Realtime-Translate comes in at $0.034 per minute, while GPT-Realtime-Whisper costs $0.017 per minute.

Those translation and transcription rates are aggressive enough to undercut most enterprise pipelines that stitch together separate vendors for each step. As The Next Web noted, the pricing comparison becomes particularly uncomfortable for companies like ElevenLabs, which raised its Series D in February at an $11 billion valuation explicitly on the voice-agent thesis, and Deepgram, which sells streaming transcription as a standalone primitive.

The competitive dynamic is straightforward: enterprises that have been assembling voice agents from a patchwork of Whisper or Deepgram for transcription, ElevenLabs or Cartesia for text-to-speech, and GPT-4 or Claude for reasoning now have the option of a single integrated model that handles audio in and out with reasoning happening inside the loop.

## What It Means

OpenAI's three-model launch represents the clearest signal yet that voice AI is moving from experimental novelty to production infrastructure. The combination of GPT-5-class reasoning, expanded context windows, robust tool calling, and real-time translation in a single API marks a step change from the call-and-response voice bots that defined the previous generation.

But significant work remains for developers. OpenAI ships active content classifiers and EU data residency support, but the integration burden of compliance, brand voice tuning, escalation logic, and tool-call observability stays with the builder. None of the three models removes the need for guardrails, evaluation frameworks, and analytics that production voice agents demand.

The next quarter will be the first real test -- when benchmarks give way to production workloads and the competitive question shifts from who has the best demo to who reduces the deployment burden fastest. For now, the Realtime API is live, the pricing is set, and the rest of the voice AI industry has its response to write.