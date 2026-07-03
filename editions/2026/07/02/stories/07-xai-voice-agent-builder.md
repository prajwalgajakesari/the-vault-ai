# xAI Launches Voice Agent Builder, a No-Code Tool for Grok-Powered Phone Agents

xAI is making a play for the fast-growing voice-AI market, launching a no-code product on July 1 that lets any business turn a plain-language description into a working phone agent in about two minutes. The company calls it Voice Agent Builder, and it runs on Grok Voice, xAI's speech-to-speech model tuned for messy, real-world telephone calls.

The pitch is aggressive on both simplicity and price. "Today, we're announcing Voice Agent Builder in beta: a no-code platform to configure production voice agents on Grok Voice," xAI wrote in its announcement. "It's for operators and developers who want high-volume production voice agents without building the surrounding stack from scratch." Agents are billed at $0.05 per minute of audio, with voices included and no separate platform fee. Telephony on a free provisioned number costs an additional $0.01 per minute.

## What Ships in the Box

The product is squarely aimed at call-center workloads: support lines, sales outreach, and appointment scheduling. Out of the box, xAI says, "you get telephony, knowledge retrieval, tools, guardrails, MCPs, and observability in one place." Each account comes with a free phone number ready for production traffic, and businesses that already have numbers can bring them over via SIP from any major telephony provider, or connect a custom client over WebSocket.

Setup is deliberately spare. An operator writes a prompt describing how calls should flow, then attaches documents, tools, and guardrails. Knowledge lives in a "knowledge base" that ingests plain text, Markdown, Word, PowerPoint, Excel, HTML, and JSON, organized into reusable collections so that policies and product specs can be shared across agents rather than pasted into every prompt.

Crucially, the agents can act, not just talk. Through tools and connectors, an agent can schedule appointments in Google Calendar or Outlook, send confirmation emails, check order status or issue refunds against a company's own APIs, manage tickets in Linear or Notion, and pull files from Google Drive or OneDrive. When it runs out of road, it can transfer the call to a human or end it cleanly, sending real-time notifications so a human can step in.

On voices, the builder offers 80-plus built-in options or a clone of a brand's own voice generated from roughly two minutes of audio, across 25-plus languages with mid-conversation switching. Every call is recorded and transcribed, with call replay, full transcripts, and a view of which tools the agent invoked. Guardrails set hard limits, such as never reading back card numbers or straying off-script.

## One Model, Not Three

xAI's core technical argument is architectural. "Most voice stacks stitch together three APIs—speech-to-text, a language model, and text-to-speech—often with each stage hosted by a different provider," the company wrote. "Every hop adds cost, latency, and new failure modes." Voice Agent Builder instead runs on a single speech-to-speech path coupled tightly to Grok Voice, which is where xAI credits its sub-second response times.

The company backed the claim with a benchmark. On what it calls the tau-voice Bench leaderboard, which measures agents against noisy telephony audio, strong accents, interruptions, and callers who change their minds mid-sentence, Grok Voice Think Fast 1.0 scored 67.3%, ahead of Google's Gemini 3.1 Flash Live at 43.8% and OpenAI's GPT Realtime 1.5 at 35.3%. "We trained Grok Voice on those calls," xAI wrote of its hardest-call training approach. Benchmarks are self-reported and worth treating with caution, but the gap is notable.

## Why It Matters

The voice-agent market has become one of the most crowded corners of applied AI, and xAI is entering as a price-aggressive latecomer. Analysts peg the broader conversational-AI market at roughly $2.4 billion in 2024, growing at nearly 35% annually toward an estimated $47.5 billion by 2034. That has drawn a dense field: ElevenLabs, fresh off a $500 million raise at an $11 billion valuation, builds the full pipeline in-house and prices conversational AI from roughly $0.08 per minute up; Retell AI lists usage-based pricing around $0.07 per minute; Vapi charges a $0.05-per-minute orchestration fee on top of bring-your-own-model costs; and OpenAI's gpt-realtime bundles speech and reasoning at about $0.06 per minute.

Against that backdrop, xAI's headline $0.05-per-minute rate with voices included and no platform fee undercuts most rivals on the sticker, and its single-vendor, single-model story is a direct shot at the orchestration platforms that stitch third-party components together. The competitive edge xAI is really selling is consolidation: instead of separate meters for recognition, reasoning, synthesis, and platform, it offers "a small number of meters you can multiply by call volume and be done." For buyers who have wrestled with the hidden costs of multi-vendor voice stacks, that simplicity may matter as much as the per-minute number.

There are caveats. The product is in beta, the benchmark is xAI's own, and voice agents in customer-facing roles carry real reputational and compliance risk, which is presumably why guardrails and call replay feature so prominently. There is also the Musk factor: xAI, now a division of SpaceX, has a habit of shipping fast and iterating in public, which cuts both ways for enterprises evaluating a mission-critical support line.

## What to Watch

The near-term test is adoption. xAI is betting that no-code speed plus transparent pricing will pull small and mid-market operators away from incumbents, and pull enterprises tempted by a single-vendor stack. Watch whether ElevenLabs, Retell, and Vapi respond with price cuts of their own, whether independent benchmarks corroborate Grok Voice's tau-voice Bench lead, and whether the beta holds up under the "hardest workflow" xAI is daring customers to throw at it. As the company put it: "A voice agent is easier to judge by ear than by benchmark. Build one, give it your hardest workflow, and call it."
