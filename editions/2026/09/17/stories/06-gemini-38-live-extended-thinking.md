Google's newest "Extended Thinking" model does not think longer about your code. It thinks longer about your phone call.

On September 15, Google shipped Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking — a pair of audio-to-audio models for real-time voice agents, not a new general-purpose Gemini tier. The distinction matters, because the branding invites exactly the wrong reading. There is no "Gemini 3.8" frontier text model in this release. Gemini 3.8 Flash shipped separately on September 2. What landed this week is a speech stack, and the "Extended Thinking" in the name refers to background reasoning that runs *while the model is still talking to you*.

Both models are built on Gemini 3 Pro, according to the [Gemini 3.8 Audio model card](https://deepmind.google/models/model-cards/gemini-3-8-audio/), and both carry a 131,072-token input window and 65,536-token output limit — modest by 2026 standards, and a reminder that these are latency-optimized dialogue models, not long-context workhorses. The model card also lists a knowledge cutoff of January 2025, nearly two years stale at launch.

## What was actually announced

Google's blog post, bylined by principal engineer Tom Ouyang and technical staff member Malini Jaganathan, splits the lineup cleanly. Gemini 3.8 Live is "built for scale and cost efficiency." Extended Thinking is "built for high-complexity tasks, with increased intelligence and multi-step reasoning." The headline capability is that Extended Thinking, per Google, "reasons and speaks simultaneously" — issuing early verbal cues like "Let me check that…" and narrating progress while tool calls finish in the background.

Under the hood, that is a protocol change, not just a UX flourish. Google's developer documentation is blunt about it: with Extended Thinking, `turnComplete: true` "no longer indicates that the model is idle." Clients must instead watch a new `interaction_status` field that reports `IN_PROGRESS` or `IDLE`. Only asynchronous, non-blocking function calls are supported — synchronous blocking mode "returns a hard error" — and proactive audio is permanently on. Developers configure reasoning depth with `thinking_config` at three levels: low, medium, or high. `MINIMAL` is not available.

TechRepublic, covering the launch on September 17, framed the consequence for engineers precisely: "the end of a spoken response no longer necessarily means the underlying task is finished." Any booking, lookup or transaction built on this model needs a completion signal that is not the sound of the assistant's voice.

Availability is staggered. Both models are generally available in the Gemini API and Google AI Studio and in private preview in Gemini Enterprise. Base 3.8 Live powers Search Live for everyone; Extended Thinking reaches Gemini Live, plus Docs for Google AI Pro and Ultra subscribers and Gmail and Keep for all Google AI subscribers. Notably, the broader Live API itself remains in preview even though the models on top of it are marked stable.

## The numbers, and what they don't say

Google's pricing page lists identical rates for both models: $0.75 per million text input tokens and $4.50 per million text output, with audio at $3.00 per million input tokens (about $0.005/min) and $12.00 per million output (about $0.018/min). Image and video input runs $1.00 per million. One price card, two models.

That is precisely where the marketing and the economics part ways. Artificial Analysis, which Google cites for its own top-line claim, measures cost per hour of input audio at **$3.50 for Extended Thinking versus $0.84 for base 3.8 Live** — a 4.2x gap on an identical rate sheet, because thinking tokens bill as output. Extended Thinking takes the #1 slot on the Speech to Speech Index at 82.6, but the field behind it is crowded: OpenAI's GPT-Live-1 (Astra, medium) sits at 81.5 and xAI's Grok Voice Think Fast 2.0 High at 81.3. A 1.1-point lead is a lead, not a moat.

The agentic numbers tell the same story. Extended Thinking's 68.6% on τ-Voice edges GPT-Live-1 Astra's 67.9%. And on human preference — the one metric users actually feel — Extended Thinking scores 990 Elo in the Speech Agent Arena, *below* Google's own cheaper base model at 1083, below GPT-Live-1 Sol (1053) and Astra (1048), and below Grok (1011). Base 3.8 Live also beats it on task success rate (93.2% vs 89.1%) and time to first audio (1.18s vs 1.35s). Google's own blog acknowledges the base model's second-place Arena finish; it does not dwell on the fact that people preferred it to the flagship.

## Why this matters

The thinking-budget arms race has reached voice, and voice is where it gets expensive fastest. In a chat interface, a model that thinks for eight seconds is a spinner. In a phone call, it is dead air — which is exactly the problem Extended Thinking's verbal-cue-and-narrate design exists to paper over. Google is not selling more reasoning so much as selling a way to *hide* reasoning latency behind conversational filler.

That reframes the buying decision. Per-token price is now nearly useless as a comparison metric when two models share a rate card and differ 4x in real cost. What matters is cost per completed task: Extended Thinking resolves 68.6% of τ-Voice scenarios at $3.50/hour, base 3.8 Live resolves 30.1% at $0.84/hour. For a support deflection workload, that ratio — not the sticker price — decides the build.

There is also release-cadence fatigue to name honestly. Gemini 3.8 Flash on September 2, Gemini 3.8 Live on September 15, a blog update on September 17 — three "3.8" events in a fortnight, sharing a version number but not an architecture. A product listing circulating around September 17 under the name "Gemini 3.8 & 3.8 Live Extended Thinking" was a downstream artifact of that blur, not a primary source.

## What to watch

Three things. First, whether the Arena preference gap closes — if users keep preferring the cheap model, "Extended Thinking" becomes an enterprise SKU rather than a consumer default. Second, whether the Live API graduates from preview, since enterprises cannot underwrite call-center deployments on a preview-tier transport. Third, whether rivals adopt the same async-completion protocol; if OpenAI and xAI ship equivalents, `interaction_status`-style state tracking becomes table stakes for every voice agent framework, and Google's two-week lead evaporates into a shared standard.
