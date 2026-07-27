Elon Musk's xAI has planted a flag in the speech-to-text market, with **Grok STT 1.0** surfacing on the OpenRouter model catalog on July 23, 2026 — a versioned, generally available transcription model that turns the company's earlier audio experiment into a production-grade product aimed squarely at Deepgram, ElevenLabs, and OpenAI's Whisper.

The 1.0 release formalizes an audio push that began in the spring. xAI first announced standalone **Grok Speech to Text (STT)** and **Text to Speech (TTS)** APIs on April 17, 2026, describing them as "two powerful standalone audio APIs" built "on the same stack that powers Grok Voice, Tesla vehicles, and Starlink customer support." The July arrival of Grok STT 1.0 as a discretely versioned endpoint — priced and benchmarked — is the clearest signal yet that xAI intends to compete for enterprise transcription budgets, not just power its own consumer chatbot.

## What xAI is shipping

Grok STT 1.0 is available through a REST endpoint (`/v1/stt`) for batch transcription of large audio files and a WebSocket API for real-time streaming. xAI lists the same feature set that leading transcription providers treat as table stakes: **word-level timestamps**, **speaker diarization** (identifying who said what), and **multichannel audio** support for cleanly separating callers on, say, a two-line phone recording.

The model also performs what xAI calls intelligent **Inverse Text Normalization** — converting spoken language into properly structured text, so a dictated "four one four five five five one two three four" becomes a formatted phone number, and spoken currency, dates, and account numbers land as clean, machine-usable strings rather than raw words. On the language front, xAI advertises support for **25+ languages** with the ability to switch mid-stream.

Pricing is the headline pitch. Grok STT costs **$0.10 per hour of audio for batch** processing and **$0.20 per hour for streaming**, with the accompanying TTS model billed at $15.00 per million characters. Those STT numbers undercut much of the established market and reflect a familiar Musk-company strategy: use vertically integrated infrastructure to compete aggressively on cost.

## The accuracy claims

xAI's most pointed marketing is aimed at accuracy, and the company published a head-to-head benchmark table pitting Grok STT against ElevenLabs, Deepgram, and AssemblyAI across domains measured by **word error rate (WER)**, where lower is better.

By xAI's own numbers, Grok STT posts a **6.9% overall WER**, versus 9.0% for ElevenLabs, 11.0% for Deepgram, and 12.9% for AssemblyAI. The gaps widen dramatically on the domain xAI most wants to sell into — telephony and business calls:

- **Phone call entity recognition** (names, account numbers, dates): Grok STT **5.0%**, ElevenLabs 12.0%, Deepgram 13.5%, AssemblyAI 21.3%
- **Meetings**: Grok STT **10.9%**, ElevenLabs 12.2%, AssemblyAI 15.7%, Deepgram 16.3%
- **Telephone**: Grok STT **9.3%**, ElevenLabs 9.4%, Deepgram 11.0%, AssemblyAI 11.2%
- **Video/Podcasts**: Grok STT and ElevenLabs tied at **2.4%**, ahead of Deepgram (3.0%) and AssemblyAI (3.2%)

xAI frames the model as excelling at "entity recognition and business use cases like medical, legal, and financial" — the high-value, error-intolerant workflows where a single mistranscribed account number or drug name carries real cost.

**An important caveat:** these are vendor-published benchmarks. They have not been independently verified, and the specific test sets, audio conditions, and formatting settings behind the numbers are xAI's own. Transcription accuracy is notoriously sensitive to accents, background noise, and domain jargon, so real-world WER for any provider often diverges from marketing tables.

## Where it fits in the Grok lineup

Grok STT slots into an increasingly broad xAI product surface that spans the Grok chatbot, the Grok Voice conversational assistant, the Grok CLI for developers, and image tools. By carving speech recognition out as its own priced, versioned API rather than burying it inside Grok Voice, xAI is following the same playbook OpenAI used when it exposed Whisper as a standalone transcription endpoint — turning an internal capability into a revenue line and a developer on-ramp. The company's claim that the model runs on the same audio stack behind Tesla's in-car assistant and Starlink's customer support hints at the enormous volume of real-world voice data xAI can draw on.

## The competitive landscape

The speech-to-text market xAI is entering is crowded and maturing fast. **OpenAI's Whisper** remains the default open-weight reference point and powers countless downstream tools, while OpenAI's newer hosted transcription models compete on the API side. **Deepgram** has built an enterprise business on low-latency streaming and per-minute pricing; **AssemblyAI** leans on developer-friendly speech intelligence features; and **ElevenLabs**, better known for voice synthesis, has pushed hard into transcription and is the closest competitor to Grok STT on xAI's own charts.

xAI's wedge is the combination of aggressive per-hour pricing and claimed accuracy in telephony and business audio — the segments where transcription is a cost center that companies would love to shrink. If the 6.9% overall WER holds up under independent testing, xAI has a credible product. If it doesn't, the low price alone may still win latency-tolerant, high-volume batch workloads.

## What to watch

Three things will determine whether Grok STT 1.0 is a genuine contender or a spec-sheet entry. First, **independent WER validation** — third-party benchmarks on standard datasets and messy real-world audio will reveal whether xAI's numbers survive contact with accents, noise, and jargon. Second, **latency and uptime** in production, the metrics that actually decide voice-agent deals and that OpenRouter tracks live. Third, whether xAI's rock-bottom **$0.10-per-hour** pricing forces Deepgram and ElevenLabs to respond — a price war would be the clearest sign xAI has arrived. For now, the speech-to-text race has a loud new entrant, and it is undercutting the field on day one.
