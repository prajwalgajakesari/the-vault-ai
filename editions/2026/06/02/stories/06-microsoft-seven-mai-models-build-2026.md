---
headline: "Microsoft Unveils Seven In-House MAI Models Spanning Reasoning, Image, Code, and Voice"
slug: microsoft-seven-mai-models-build-2026
category: llms-genai
story_number: "06"
date: 2026-06-02
authors:
  - The Vault AI
tags:
  - microsoft
  - mai-thinking-1
  - build-2026
  - reasoning-models
  - github-copilot
  - microsoft-foundry
sources:
  - name: Thurrott
    url: https://www.thurrott.com/a-i/336960/build-2026-microsoft-launches-first-flagship-reasoning-ai-model-and-more
  - name: WinBuzzer
    url: https://winbuzzer.com/2026/06/02/microsoft-adds-seven-mai-models-to-foundry-for-developers-xcxwbn/
  - name: Neowin
    url: https://www.neowin.net/news/microsoft-unveils-mai-thinking-1-reasoning-and-mai-code-1-coding-models/
  - name: Microsoft AI
    url: https://microsoft.ai/news/introducing-mai-thinking-1/
  - name: Tom"s Guide
    url: https://www.tomsguide.com/news/live/microsoft-build-2026
  - name: TechTimes
    url: http://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm
---

Microsoft just declared its independence from OpenAI -- at least on the model-building front.

At Build 2026 on Monday, the company"s AI Superintelligence team unveiled seven in-house MAI-branded models spanning reasoning, coding, image generation, voice synthesis, and transcription. The flagship, MAI-Thinking-1, is Microsoft"s first reasoning model trained entirely without OpenAI data or distillation, a milestone that redraws the competitive map for enterprise AI.

## The Flagship: MAI-Thinking-1

MAI-Thinking-1 is a sparse Mixture-of-Experts architecture with 35 billion active parameters drawn from roughly one trillion total parameters. It ships with a 256K-token context window, function calling, developer instructions, and full compatibility with the Chat Completions API -- meaning teams already wired into that standard can slot it in with minimal integration work.

Microsoft says the model was trained from scratch on commercially licensed data with zero distillation from third-party models. That provenance story is aimed squarely at enterprise buyers who weigh intellectual-property risk alongside raw performance. And the performance claims are aggressive: Microsoft says independent human raters on Surge prefer MAI-Thinking-1 over Anthropic"s Claude Sonnet 4.6 for overall quality across single and multi-turn tasks, while it matches Claude Opus 4.6 on SWE-Bench Pro, a demanding software-engineering benchmark. On the math side, it reaches 97.0% on AIME 2025 and 94.5% on AIME 2026.

"For the first time developers will be able to tune the weights of the model themselves," said Microsoft AI CEO Mustafa Suleyman, signaling that MAI-Thinking-1 is not just another API endpoint but a platform for deep customization. Weight tuning gives enterprises an adaptation path far beyond prompt engineering or retrieval-augmented generation layers.

MAI-Thinking-1 enters Microsoft Foundry in private preview, with a public preview planned through the MAI Playground.

## Six More Models Complete the Lineup

The remaining six models turn Build 2026 from a single-model launch into a full-stack AI offensive:

**MAI-Code-1 and MAI-Code-1-Flash.** MAI-Code-1-Flash is a lean 5-billion-parameter coding model purpose-built for GitHub Copilot and Visual Studio Code. Its bigger sibling, MAI-Code-1, is already live inside those tools. Microsoft is betting that inference-efficient, specialized coding models can outperform general-purpose giants on the tasks developers actually run thousands of times a day -- autocomplete, refactoring, and test generation.

**MAI-Image-2.5 and MAI-Image-2.5-Flash.** The image models handle text-to-image generation and image editing with what Microsoft calls "control-with-preservation" features. MAI-Image-2.5 has already climbed to third place among image-generation model families on the Arena leaderboard. It is live in PowerPoint and Microsoft Foundry, with OneDrive integration coming soon.

**MAI-Transcribe-1.5.** Microsoft"s updated transcription model supports 43 languages with domain-specific terminology and claims five-times-faster processing than competing models while maintaining state-of-the-art accuracy.

**MAI-Voice-2 (plus Flash variant).** The voice synthesis models now cover more than 15 additional languages with new voice options, including voice cloning and voice prompting capabilities.

The image, transcription, and voice models are generally available now on Microsoft Foundry and MAI Playground.

## Distribution Beyond Azure

In a notable move, Microsoft announced that its MAI models will also be available on Fireworks AI, Baseten, and OpenRouter -- third-party inference platforms that compete with Azure itself. "Fireworks AI is now generally available on Foundry, giving developers a single platform experience with enterprise governance and Azure data residency, regardless of the model they choose," said Kyle Daigle, Microsoft Developer CMO and COO of GitHub.

That distribution strategy turns availability into an operational choice rather than a platform lock-in decision, a pragmatic concession that developers increasingly expect model portability.

## The Competitive Picture

The timing is deliberate. Google made Gemini 3.5 Flash generally available on May 19 with agentic workflows and long-horizon tasks in focus. Anthropic shipped Claude Opus 4.8 on May 28 with benchmark and agentic-workflow improvements. Microsoft"s seven-model salvo, announced just five days later, ensures it enters the conversation with breadth rather than a single point of comparison.

More broadly, the MAI launch represents Microsoft"s clearest statement yet that it intends to be a model builder, not merely a model distributor. The company already hosts OpenAI, Meta, Mistral, and dozens of other providers through Foundry. Now it is asking developers to evaluate its own models in the same decision framework -- on cost, governance, latency, and workload fit.

## What It Means

For developers, the practical upshot is more choice inside an ecosystem they are likely already using. For Microsoft, it is a hedge: if the OpenAI partnership ever shifts, Redmond now has its own reasoning, coding, and multimodal stack to fall back on. And for the broader industry, seven models trained without OpenAI data send an unmistakable message -- the era of any single lab holding a monopoly on frontier AI capability is over.