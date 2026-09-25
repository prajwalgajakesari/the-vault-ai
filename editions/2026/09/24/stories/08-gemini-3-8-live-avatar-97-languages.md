Google's real-time voice agent now has a face. On Wednesday the company made **Gemini 3.8 Live with Live Avatar** generally available in Gemini Enterprise. The feature pairs Gemini's native live-dialogue models with near-real-time video generation, so an enterprise agent can appear as an animated persona that talks, listens, watches through a user's camera, and keeps its lip-sync and facial expressions in step across **97 languages**.

The launch comes one week after Google introduced Gemini 3.8 Live and its Extended Thinking variant. That reasoning mode is still in private preview. Live Avatar, first previewed at Google Cloud Next 2026, has skipped ahead of it into production, with **US and EU endpoints**, provisioned throughput, and the compliance and data-governance commitments large buyers look for.

## A talking head built on a speech-to-speech core

Google describes Live Avatar as an extension of its speech-to-speech stack, not a video layer added on top. “By pairing near real-time video generation with speech, the Live Avatar feature creates an experience that listens, sees, and speaks with a dynamic visual persona,” wrote research scientist **Shuo-yiin Chang** and software engineer **CJ Zheng** of the Gemini Audio Team in the announcement post. They framed the pitch around how people actually talk: “Conversation is inherently multimodal: we listen, look, speak, and use facial expressions to communicate.”

The headline figure is multilingual. Google says the avatar handles speech-to-speech synchronization natively and can switch languages in the middle of a conversation, adjusting lip movements and expressions *without degrading video fidelity or introducing visual drift*. Visual drift, where a generated face slowly loses its likeness or falls out of sync over a long session, is the typical failure of streaming avatar systems. The underlying model detects which of the 97 languages a user is speaking on its own.

Google also stresses what the avatar can do while it is talking. With **asynchronous tool execution**, the agent can start API calls and fetch data in the background and keep the conversation going. One demo shows it checking a guest into a hotel without pausing. The model can also take in live camera feeds and screen shares at the same time as audio. In a second demo, an insurance-claims intake agent looks at damage shown on camera and fills in a claim record while an Agent Development Kit (ADK) agent team checks the policy and assembles the adjuster packet in the background.

Customers can pick from a library of preset avatars. They can also generate a fully animated custom persona from one high-quality reference image, and Google's Cloud demo adds an audio sample to clone the voice. That custom path is available only through **enterprise allowlisting and verification**, and every audio and video stream carries an imperceptible **SynthID** watermark.

## Early customers

Google named several early adopters. Cox Automotive built a conversational shopping assistant for Autotrader that highlights parts of the screen and calls tools to guide buyers through search, comparison, and financing. “Shoppers increasingly expect to describe what they need in their own words rather than work through filters and menus,” said **Marianne Johnson**, EVP and Chief Product Officer at Cox Automotive.

Equal AI, an Indian consumer-assistant startup, already runs Gemini Live at large scale. “Today, it handles over a million live calls daily across nine Indian languages,” said CEO **Akhilesh Damaraju**, who credited Gemini 3.8 Live with better interruption handling, multilingual conversation, and tool-call reliability. Salesforce says it is exploring the model alongside Agentforce for customer service.

## Why It Matters

Talking-head video avatars have mostly belonged to startups like HeyGen, Synthesia, and D-ID. Their core product has been pre-rendered presenter video, with interactive, real-time avatars added more recently. Google is now shipping the whole stack in one API call: the reasoning model, the voice, the vision, the tool-use layer, and the rendered face, all sold through the same Gemini Enterprise contract a company may already have. For a CIO building a customer-service kiosk or onboarding flow, that removes an integration step and a vendor. Avatar specialists will have to compete on customization, creative tooling, and price instead of on having real-time video at all.

The launch also shows how the big labs expect agents to be judged. Google's Cloud post, written by Group Product Manager Fabien Blanc-paques, says enterprise voice AI is moving past simple speed and cost metrics toward interaction quality. A face that keeps its lip-sync in Hindi, Portuguese, and Japanese within one call is a clear way to show that quality, and it is hard for a text-first competitor to match quickly.

The identity safeguards matter as much as the features. Real-time, photoreal, multilingual avatars that can be built from one photo are exactly what regulators worry about in deepfake fraud. By gating custom avatars behind allowlisting and watermarking every frame with SynthID, Google is trying to show that a hyperscaler can offer this capability responsibly. Whether that holds up depends on how strictly the allowlist is run and on whether anyone outside Google routinely checks for the watermark.

## What to Watch

Watch three things: pricing per avatar-minute compared with HeyGen and Synthesia's enterprise tiers, whether Google opens custom avatars beyond the allowlist, and whether Live Extended Thinking reaches general availability so the avatar can reason more deeply without breaking the conversation. Also expect a response from OpenAI and Microsoft, whose real-time voice APIs have no native face yet, and from the avatar startups, which now face their largest competitor inside the cloud accounts of their own customers.
