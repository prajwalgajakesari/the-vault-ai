---
title: "Sakana AI Introduces KAME Architecture for Real-Time Knowledge-Augmented Speech"
slug: sakana-ai-kame-speech-architecture
category: llms-genai
story_number: "08"
date: 2026-05-17
edition: 2026/05/17
sources:
  - name: MarkTechPost
    url: https://www.marktechpost.com/2026/05/03/sakana-ai-introduces-kame-a-tandem-speech-to-speech-architecture-that-injects-llm-knowledge-in-real-time/
  - name: Sakana AI Official (ICASSP 2026)
    url: https://sakana.ai/kame-icassp-2026/
  - name: Sakana AI Technical Blog
    url: https://pub.sakana.ai/kame/
  - name: arXiv Paper (2510.02327)
    url: https://arxiv.org/abs/2510.02327
  - name: Artiverse
    url: https://www.artiverse.ca/sakana-ai-unveils-kame-for-real-time-smarter-voice-interactions/
---

# Sakana AI Introduces KAME Architecture for Real-Time Knowledge-Augmented Speech

**The Tokyo lab cracks voice AI’s oldest dilemma: speak fast or speak smart. KAME does both.**

For years, building a conversational voice AI meant picking a poison. You could have a system that responds in the blink of an eye but knows embarrassingly little, or one that draws on the full knowledge of a frontier language model but makes users wait long enough to lose the conversational thread. Sakana AI, the Tokyo-based research lab co-founded by former Google Brain researcher David Ha, has published a new architecture called **KAME** — Knowledge-Access Model Extension — that refuses the tradeoff entirely.

Accepted to ICASSP 2026, KAME is a tandem system that runs a real-time speech-to-speech front-end and a full-scale LLM back-end simultaneously and asynchronously, letting the two components inform each other on the fly. The result: near-zero response latency alongside a knowledge quality that rivals state-of-the-art cascaded systems. The model weights, inference code, and paper are all publicly available.

## The Fault Line in Voice AI

To understand what makes KAME significant, it helps to understand the two paradigms it bridges.

Direct speech-to-speech (S2S) models like KyutAI’s Moshi are end-to-end audio transformers. They ingest audio tokens and emit audio tokens in a continuous loop, meaning they can start replying before the user even finishes their sentence — latency measured in tens of milliseconds. The catch is that audio carries far more information per token than text: tone, rhythm, emotion, and prosody all compete for model capacity alongside factual knowledge. The result is a system that feels fluid but often produces shallow, low-confidence answers.

Cascaded systems take the opposite approach. Speech goes in, gets transcribed by an ASR model, routes through a powerful text LLM, and returns as synthesized audio. Knowledge quality is excellent — you can wire in any frontier model — but the pipeline is inherently serial. The system cannot begin LLM processing until the user stops speaking, which introduces a median latency of around **2.1 seconds** before the first word of the response is heard. That gap is long enough to make natural back-and-forth feel stilted.

KAME’s wager is that these two components do not need to wait for each other.

## Architecture: Speak While Thinking

KAME operates with two modules running in parallel. The **front-end S2S module** is built on the Moshi architecture and processes audio at the cycle of discrete audio tokens — roughly every **80 milliseconds** — generating a spoken response immediately. Internally, Moshi has three concurrent streams: input audio, an inner monologue in text, and output audio. KAME adds a fourth: the **oracle stream**.

The **back-end LLM module** consists of a streaming speech-to-text (STT) component feeding a full-scale language model. As the user speaks, the STT component builds a growing partial transcript and periodically ships it to the back-end LLM. The LLM returns candidate text responses — called “oracles” — that are streamed back to the front-end in real time. Because the user’s speech is still arriving, these oracles begin as educated guesses and grow progressively more accurate as the transcript fills in.

The front-end S2S transformer conditions its ongoing speech output on both its own internal state and these incoming oracle tokens, effectively updating its response mid-sentence as better information arrives. Because both modules run asynchronously, the initial response latency stays near zero — the same as Moshi running alone.

The paper’s framing is deliberately direct: “Two heads are better than one.” The system shifts the paradigm from “think, then speak” to “speak while thinking.”

## Training Without Ground Truth

One non-trivial engineering challenge: no naturally occurring dataset contains oracle signals. Sakana AI’s team addressed this with a technique they call **Simulated Oracle Augmentation**. Using a simulator LLM and a standard conversational dataset, they generated synthetic oracle sequences that mimic what a real-time LLM would produce at different stages of transcript completeness.

They defined **six hint levels (0–5)**: at level 0, the front-end receives no oracle at all; at level 5, it receives the verbatim ground-truth response. Levels 1–4 capture the realistic scenario where the oracle starts vague and sharpens as the transcript grows. The final training corpus consisted of **56,582 synthetic dialogues** drawn from MMLU-Pro, GSM8K, and HSSBench, converted to audio via TTS and augmented with these progressive oracle sequences.

## Benchmark Results: Closing the Gap

The team evaluated on a speech-synthesized subset of the MT-Bench multi-turn Q&A benchmark, focusing on reasoning, STEM, and humanities categories (coding, math, and writing were excluded as unsuitable for spoken interaction).

The numbers tell a clear story. Moshi alone scores **2.05**. KAME backed by GPT-4.1 scores **6.43**, and KAME backed by Claude Opus 4.1 scores **6.23** — both at the same near-zero latency as Moshi. The leading cascaded system, Unmute (also backed by GPT-4.1), scores **7.70** — but only after a 2.1-second wait.

To isolate the effect of KAME’s premature-generation problem — the fact that the front-end starts speaking before the full query is heard — the team also scored the back-end LLM’s text outputs from the final oracle injection in each session directly. Those scores averaged **7.79** across reasoning (6.48), STEM (8.34), and humanities (8.56) — statistically comparable to Unmute’s 7.70. In other words, KAME’s remaining gap to cascaded systems is not a ceiling on the LLM’s knowledge but a consequence of committing to speech output before the user has finished asking.

## Backend Agnostic by Design

One of the more commercially significant aspects of KAME is its flexibility. The front-end was trained using GPT-4.1-nano as the simulated back-end, but swapping in a different model at inference time requires zero retraining. Sakana AI tested GPT-4.1, Claude Opus 4.1, and Gemini 2.5 Flash interchangeably.

The substitution experiments also revealed task-specific strengths: Claude Opus 4.1 outperformed GPT-4.1 on reasoning tasks, while GPT-4.1 led on humanities questions. That opens the door to query routing — a production system could direct a factual query to one LLM and a reasoning-heavy question to another, without touching the front-end model at all.

## Why It Matters

Voice AI has been stuck at a false binary for years. Consumer products have largely resigned themselves to the latency of cascaded systems, treating the delay as a necessary cost of intelligence. Real-time systems like Moshi showed that zero-lag conversation was possible but sacrificed too much depth for general-purpose use.

KAME’s architecture suggests that latency and knowledge are not actually in fundamental tension — they were in tension only because prior designs assumed a serial pipeline. By decoupling the two components and letting them run asynchronously, Sakana AI has demonstrated that a system can begin speaking immediately while still steering itself toward a more knowledgeable answer as it goes.

The architecture is arguably closer to how expert humans handle real-time conversation: start forming a response based on early context, stay ready to revise as more information arrives, and never let uncertainty justify silence.

With weights and code released publicly and the paper accepted to a major signal-processing conference, KAME is well-positioned to influence the next generation of voice assistants — both at research labs and in production.

---

*Sources: [Sakana AI ICASSP 2026](https://sakana.ai/kame-icassp-2026/) | [Technical blog](https://pub.sakana.ai/kame/) | [arXiv 2510.02327](https://arxiv.org/abs/2510.02327) | [MarkTechPost](https://www.marktechpost.com/2026/05/03/sakana-ai-introduces-kame-a-tandem-speech-to-speech-architecture-that-injects-llm-knowledge-in-real-time/) | [GitHub](https://github.com/SakanaAI/kame)*