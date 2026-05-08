---
headline: "OpenAI Drops Three Voice Models That Translate 70 Languages in Real Time"
slug: openai-voice-models-70-languages
category: llms-genai
story_number: "07"
date: 2026-05-07
---

# OpenAI Drops Three Voice Models That Translate 70 Languages in Real Time

OpenAI on May 7 released a trio of real-time audio models that give developers the building blocks for voice applications capable of reasoning through complex requests, translating live conversations across more than 70 languages, and transcribing speech the instant it leaves a speaker"s mouth. Taken together, the launch marks the company"s clearest signal yet that it views voice not merely as an interface novelty but as the primary way millions of people will interact with software in the years ahead.

The three models are GPT-Realtime-2, a voice-native reasoning engine built on GPT-5-class intelligence; GPT-Realtime-Translate, a live translation system spanning more than 70 input languages and 13 output languages; and GPT-Realtime-Whisper, a streaming speech-to-text model engineered for low-latency transcription. All three are available immediately through OpenAI"s Realtime API, and developers can test them in the company"s Playground environment.

## Reasoning at the Speed of Speech

GPT-Realtime-2 is the headline act. OpenAI calls it the first voice model to carry GPT-5-class reasoning, meaning it can work through multi-step problems, call external tools, handle mid-sentence corrections, and maintain conversational coherence across long exchanges. The model quadruples the context window from 32,000 tokens to 128,000 tokens, a change that enables substantially longer and more complex voice sessions without the memory loss that plagued earlier iterations.

Performance benchmarks back up the claims. GPT-Realtime-2 at its highest reasoning setting scores 15.2 percent higher than GPT-Realtime-1.5 on Big Bench Audio, an evaluation that tests challenging reasoning capabilities in audio-capable language models. On Audio MultiChallenge, which measures instruction following in multi-turn spoken dialogue, the model posts a 13.8 percent improvement over its predecessor.

Developers also gain fine-grained control over how hard the model thinks. Five reasoning levels, from minimal to xhigh, let builders balance latency against depth, keeping simple interactions snappy while reserving heavier computation for genuinely difficult requests. New preamble phrases such as "let me check that" and parallel tool calling with audible status updates help voice agents feel responsive even when performing complex background work.

Josh Weisberg, Senior Vice President and Head of AI at Zillow, offered an early production perspective: "What stood out about GPT-Realtime-2 was the intelligence and tool-calling reliability it brings to complex voice interactions. On our hardest adversarial benchmark, this translates to a 26-point lift in call success rate after prompt optimization, 95 percent versus 69 percent."

## Breaking the Language Barrier in Real Time

GPT-Realtime-Translate tackles a problem that has bedeviled global businesses for decades: enabling natural conversation between people who do not share a common language. The model accepts speech in more than 70 languages and outputs translated audio in 13 languages, preserving meaning while matching the pace of live conversation. OpenAI designed it to handle regional pronunciation, domain-specific terminology, and the kind of mid-thought pivots that characterize natural human speech.

Deutsche Telekom is already testing the model for multilingual customer support, where a caller can speak in any language they are comfortable with while the agent receives a real-time translation. Vimeo demonstrated how the system can translate product education videos live as they play, allowing global customers to hear updates in their preferred language without waiting for a separately produced localized version.

Prateek Sachan, Co-founder and CTO at BolnaAI, highlighted the model"s performance in linguistically complex markets: "In our evals across Hindi, Tamil, and Telugu, GPT-Realtime-Translate delivered 12.5 percent lower Word Error Rates than any other model we tested, along with lower fallback rates, higher task completion, and latency that sustained natural conversation."

## Transcription That Keeps Pace

GPT-Realtime-Whisper rounds out the trio as a streaming transcription model built for applications where every second of latency matters. Unlike batch transcription services that process audio after the fact, Whisper transcribes speech as it happens, enabling live captions for meetings, classrooms, and broadcasts, as well as real-time meeting notes and follow-up workflows for customer support, healthcare, and recruiting.

## Pricing and Market Implications

OpenAI priced the models to encourage adoption. GPT-Realtime-2 costs 32 dollars per million audio input tokens, with cached input tokens at just 40 cents per million, and 64 dollars per million audio output tokens, representing a 20 percent reduction from the GPT-4o-Realtime-Preview pricing. GPT-Realtime-Translate comes in at 3.4 cents per minute, and GPT-Realtime-Whisper at 1.7 cents per minute.

The pricing strategy reflects a broader competitive dynamic. Google, Meta, and a growing roster of startups are all racing to build voice-native AI experiences, and OpenAI appears determined to set the floor on cost while raising the ceiling on capability. The 128K context window, in particular, is a direct response to developer complaints that earlier voice models lost coherence in extended sessions, a dealbreaker for enterprise use cases such as customer support, healthcare intake, and financial advisory.

## Why This Matters

The release repositions voice from a consumer convenience into enterprise infrastructure. When a single API call can reason through a complex real-estate query, translate a customer support conversation from Tamil to English in real time, and transcribe the entire exchange for compliance records, the technology moves from "nice to have" to operationally critical. OpenAI is betting that voice-to-action, where a user describes what they need and the system reasons, retrieves, and executes, will become one of the dominant interaction paradigms for the next generation of software. With Zillow, Priceline, Deutsche Telekom, Intercom, and Glean among the early adopters, the company is building its case not on demos but on production deployments where the models must perform under real-world pressure.