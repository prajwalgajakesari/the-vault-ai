# Alibaba's Qwen Audio-3.1 Arrives as a Five-Model Stack With Price Cuts of Up to 95%

Alibaba's Qwen team has stopped treating voice as a single product line. On Wednesday it released Qwen-Audio-3.1, a family of five speech models meant to cover every direction audio can flow through an application, and it paired the launch with some of the steepest list-price cuts the voice API market has seen: roughly 70% off text-to-speech, about 85% off the Realtime conversational model, and up to 95% off speech recognition.

The company's own framing was blunt. "Five models, one complete audio stack: understanding, generation, interaction & creation," the official Qwen account wrote on X, adding that the release came with "big price cuts across the lineup." The timing was pointed, too. The same day, Google shipped Gemini 3.8 TTS, turning September 23 into an unusually crowded day for developers shopping for synthetic voices.

## Three upgrades, two newcomers

The lineup splits into three upgraded workhorses and two new specialists. Qwen-Audio-3.1-ASR handles speech recognition, Qwen-Audio-3.1-TTS handles synthesis, and Qwen-Audio-3.1-Realtime handles live, spoken conversation. The additions are **TTS-Next**, aimed at audio creation, and **ASR-Next**, aimed at deeper audio understanding.

According to Qwen, the standard ASR model supports 30 languages and 16 Chinese dialects, with a first-character response of about 160 milliseconds. It also cleans up transcripts on the fly; as The Decoder summarized Qwen's description, the model "automatically cleans up filler words and repetitions," which could let meeting and interview tools skip a separate post-processing pass. The file-transcription variant, ASR-Flash-Filetrans, is listed on Qwen Cloud at $0.15 per million input tokens and $0.47 per million output tokens, with hotword support, speaker diarization and dialect control.

ASR-Next goes further than transcription. It returns diarized, timestamped speech and layers on detection of emotion, ambient sound and machine noise, a combination that points toward quality assurance for call centers and industrial monitoring rather than simple captioning. On the generation side, the upgraded TTS model offers multilingual synthesis with cross-language voice transfer and lets developers steer emotion, speed and style through plain text prompts. One example Qwen showcased: "Read this with a sharp, commanding tone, demanding respect." TTS-Next pairs a language model with a diffusion approach to produce voice, sound effects and background beds in a single pass, collapsing what is usually a multi-tool audio production pipeline into one call.

## Realtime-Plus and the full-duplex push

The flagship interactive model, Qwen-Audio-3.1-Realtime-Plus, is built for full-duplex conversation: it listens and speaks simultaneously and supports barge-in, so a user can interrupt mid-sentence. It can also call tools, which Qwen positions as a bridge to APIs, knowledge bases and business systems. The company says the model adapts its delivery to the listener, responding more slowly and with more empathy when it detects a low mood. A technical report on arXiv claims gains over the previous version on multilingual benchmarks, speech-conditioned tool use and selected full-duplex behaviors.

List pricing on Qwen Cloud puts Realtime-Plus at $6.40 per million audio-input tokens, $0.80 per million text-input tokens, $6.40 per million text-output tokens and $24 per million tokens for combined text-and-audio output, with a 262,000-token context window. That context length matters for voice agents, which accumulate long conversational histories and tool results over a single call.

## Why It Matters

The headline number is the 95% cut, but the more consequential move is structural. By shipping recognition, synthesis, conversation, creation and analysis as one coordinated family, Alibaba is pitching Qwen as a one-vendor voice layer, the audio equivalent of what cloud providers have long done for text models. Developers who currently stitch together a transcription provider, a separate TTS vendor and a third system for sentiment or noise analysis now have a single-provider alternative at a fraction of the prior price.

That puts direct pressure on specialists. AI Weekly's editors argued that Qwen "is now setting the floor on enterprise voice API pricing," and suggested procurement teams locked into contracts with Deepgram, ElevenLabs or OpenAI rerun their cost-per-hour math before renewal. Tbreak made a similar point, noting that cheaper per-call costs let teams build voice into customer service, accessibility and multilingual apps without rationing usage.

There are caveats. The reported cuts are relative to Qwen's own previous list prices, not to competitors, and coverage so far has not specified an effective date or whether discounted rates depend on committed capacity. Tbreak also noted that Alibaba had not published region-specific pricing or data-handling terms in the launch material, a real consideration for enterprises weighing a China-headquartered provider for sensitive audio such as customer calls. And benchmark claims for the Realtime model come from Qwen's own technical report, not independent testing.

## What to Watch

The immediate question is how rivals respond. Google's Gemini 3.8 TTS landed the same day, and OpenAI and ElevenLabs have both been expanding their voice offerings; a matching round of price cuts would confirm that voice APIs are following text models into a margin squeeze. Watch also for independent evaluations of ASR-Next's emotion and machine-sound detection, which are the least proven claims in the release, and for whether TTS-Next's one-pass sound design gains traction with podcast, game and video producers. If Alibaba can pair its pricing with clear regional availability and data terms, Qwen-Audio-3.1 could become the default low-cost baseline that every other voice vendor has to justify its premium against.
