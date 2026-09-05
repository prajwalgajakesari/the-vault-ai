On April 2, Microsoft AI charged 36 cents to turn an hour of audio into text. On Wednesday, September 3, it launched the third model in that line, MAI-Transcribe-2, and charged a dime. Five months, three releases, a 72% price cut — and an asterisk: the $0.10 rate is an introductory offer that expires December 31, 2026, and Microsoft has not said what comes after.

The arithmetic is what makes this a story rather than a spec sheet. A bank putting 100,000 hours of call-center audio through the API annually goes from a $36,000 line item to a $10,000 one. At that level, transcription stops being something procurement negotiates. It becomes a rounding error — which is the point.

## What shipped

MAI-Transcribe-2 covers 60 languages, up from 43 in June's MAI-Transcribe-1.5 and 25 in the April original. It is in public preview through Microsoft Foundry, the MAI Playground and OpenRouter.

The feature list matters more than the language count, because most of it has historically been sold separately. Speaker diarization returns speaker-labeled segments instead of an undifferentiated block of text. Word-level timestamps attach start and end times to every word, enabling click-to-play navigation, frame-accurate captioning and redaction of specific passages. Keyword biasing lets developers pass a phrase list of drug names, ticker symbols or employee names as recognition hints. Configurable output styles offer a "verbatim" default that preserves fillers and false starts for compliance work, and a "clean" mode that strips them. Code switching handles conversations that move between languages mid-sentence — Microsoft explicitly names Hinglish and Spanglish. Language identification is automatic by default.

Naomi Moneypenny, who announced the release on the Microsoft Foundry blog, framed diarization and timestamps as overdue rather than novel: they are, she wrote, "the two structural capabilities production workloads have been asking for most," and diarization in particular was "a long-standing failure mode for general speech models in any workflow with more than one person in the room."

## Whose numbers are whose

Three performance claims are circulating, and they do not all carry the same weight.

The FLEURS result — first place across 60 languages at a 5.2% average word error rate — is Microsoft's own evaluation on a public benchmark, not a third-party audit. FLEURS is read speech, a poor proxy for a noisy contact-center call. And the average has gone up: Microsoft reported 3.7% for MAI-Transcribe-1.5 in June. That almost certainly reflects folding in 17 more low-resource languages rather than any regression, but it is a vendor-run number and should be read as one.

The Artificial Analysis figures are independent. The firm tests models through their public APIs and, in its non-streaming leaderboard, records MAI-Transcribe-2 at a 2.0% word error rate with a median speed factor of 410.7x real time — an hour of audio back in roughly ten seconds. That places it second overall for accuracy, behind Alibaba's Fun-Realtime-ASR preview, and first on the accuracy-latency Pareto frontier. For comparison, the same leaderboard has ElevenLabs' Scribe v2 at 2.2% and 54.7x, Google's Gemini 3.5 Transcribe at 2.6% and 89.9x, OpenAI's GPT-Transcribe at 3.3% and 40.0x, and Microsoft's own MAI-Transcribe-1.5 at 2.4% and 190.3x. Artificial Analysis normalizes pricing to the cost of 1,000 minutes of audio; on that basis it estimates Scribe v2 at about $0.22, GPT-Transcribe at about $0.27 and Gemini 3.5 Transcribe at about $0.30.

The speed multiples Microsoft quotes — 10x GPT-Transcribe, 7x Scribe v2, 5x Gemini 3.5 Transcribe — are Microsoft's rounding of Artificial Analysis data. eWeek's own read of the same leaderboard produced 10x, 7.5x and 4.6x. These are rolling medians and will drift.

Per-language, the picture is uneven. eWeek found MAI-Transcribe-2 strong in Chinese (4.5% WER) and French (2.8%), but beaten by Gemini 3.1 Pro on Armenian (6.1% vs. 12.6%) and by Scribe v2 on Afrikaans (10.6% vs. 13.1%).

## The commoditization trade

Microsoft names four rivals in its announcement: GPT-Transcribe, Gemini 3.5 Transcribe, Whisper V3-Large and Scribe v2. It does not mention Deepgram, AssemblyAI, Speechmatics or Rev. That omission is the strategy. Microsoft is positioning against frontier labs that treat speech as a platform checkbox, while pricing at or below where the specialists sell high-volume enterprise contracts — and bundling into the base rate the features those specialists have gated behind premium tiers. Their remaining moat is domain depth, and keyword biasing is aimed squarely at it.

For OpenAI, the damage is quieter but structural. GPT-Transcribe is the slowest and least accurate model on that leaderboard at roughly 2.7x the price, and it is sold largely through Azure — a channel whose owner now has a cheaper, faster in-house substitute and every incentive to route traffic to it.

The in-house logic is not subtle. Mustafa Suleyman, Microsoft AI's chief executive, told The Verge in April that the first transcription model ran at "half the GPU cost of the other state-of-the-art models," calling it "a huge cost-saving" for Microsoft, and credited it to "a small, focused 10-person team" that had been "liberated from any of the bureaucracy." Microsoft owns Teams, Nuance and Azure Speech; every hour of audio that moves onto MAI-Transcribe-2 is an hour it stops paying a partner for. Yoni Michael of Typedef put the enterprise version of the argument to Reworked: "They've invested billions into OpenAI, but for Copilot and enterprise offerings, controlling their own foundation model stack reduces risk, licensing costs and dependence on another company's roadmap."

The unpriced risk sits in January. Ten cents is an offer, not a rate card, and a buyer who migrates a pipeline in October has no leverage when it expires.

## What to watch

Four things. Whether Microsoft publishes a post-December price before enterprises finish evaluating. Whether MAI-Transcribe-2 leaves public preview — Microsoft Learn currently ships it with no SLA and an explicit note against production use, inputs capped at 300 MB or two hours. Whether Microsoft addresses streaming at all; Artificial Analysis runs a separate streaming leaderboard, and the silence there is conspicuous for a model pitched at voice agents. And whether Teams, Nuance and Azure Speech actually cut over, which Microsoft has declined to confirm. Also missing: any diarization error rate. A transcript can post near-perfect WER and still attribute every other sentence to the wrong person.
