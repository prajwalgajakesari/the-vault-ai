Apple started pushing the rebuilt Siri to the public this week, in beta, in English only, behind a waitlist, and not at all in the European Union. The press release describes what is underneath in one sentence, two-thirds of the way down: the new capabilities are "powered by the next generation of Apple Foundation Models, custom-built in collaboration with Google and its Gemini models." That is Apple announcing, in the passive voice of a footnote, that its most visible AI product runs in significant part on a competitor's frontier model.

The rollout landed on September 14 alongside iOS 27, iPadOS 27, macOS 27, watchOS 27 and visionOS 27. Siri AI — Apple's branding, not a typo — is English-first, with French, Japanese, Korean, Portuguese and Spanish promised next month. It requires an Apple Intelligence-enabled device: iPhone 16 or later, iPhone 15 Pro and Pro Max, M1 iPads and Macs or newer, Apple Vision Pro, and Apple Watch Series 9 or later. The most advanced on-device model, driving expressive voices and improved dictation, needs at least 12GB of unified memory, narrowing it further to iPhone Duo, iPhone 18 Pro, iPhone Air, iPhone 17 Pro, M4 iPads and M3 Macs. Users under 13 are excluded. So is everyone in China, pending regulatory work.

## The two-year gap

Apple demoed a personalized, context-aware Siri at WWDC in June 2024. It slipped past iOS 18.4, was formally delayed in March 2025, and at WWDC 2025 Craig Federighi told developers only that Apple would share more in the coming year. The rebuilt assistant was finally unveiled at WWDC on June 8, 2026, and shipped as a beta three months after that. From stage demo to public beta: twenty-seven months, and what closed the gap was a check to Google.

Bloomberg reported in November 2025 that Apple would pay Google roughly $1 billion a year for a custom 1.2-trillion-parameter Gemini model built to power Siri. Apple and Google confirmed a multi-year partnership on January 12, 2026. For scale, Apple's own cloud-side foundation model was reported at around 150 billion parameters — the Google model is roughly eight times larger, and uses a mixture-of-experts design so only a fraction of those parameters fire per query.

## What runs where

Apple's architecture routes requests across tiers. Simple work stays on device, handled by a system orchestrator and Apple's own AFM Core Advanced model, which also drives the Spotlight index and App Toolbox integrations Apple says "work entirely on device." Heavier requests go to Private Cloud Compute, where Apple runs AFM Cloud, AFM Cloud Pro, an image model, and a World Knowledge Service. The largest reasoning tasks reach the custom Gemini model — and that is where the interesting engineering is, because Apple did not simply hand queries to Google's API.

"To bring this model to production, we worked with both Google and Nvidia to extend our private cloud compute infrastructure to Nvidia GPUs in Google's cloud, while maintaining Apple's unmatched privacy guarantees," said Sebastian Marineau-Mes, who runs Apple's Apple Intelligence Experience team. In other words, Apple pushed its PCC attestation and no-retention model onto hardware sitting inside Google Cloud, so that the model runs on Google's silicon without Google seeing the inputs. Apple's stated guarantee is unchanged from the 2024 version: "When Private Cloud Compute is handling users' requests, their personal data is not stored nor made accessible to Apple or anyone else. Outside experts can continue to verify this privacy promise at any time."

That verification claim is the load-bearing one. PCC's security researcher program and published server images are the mechanism; whether independent researchers can audit the Google-hosted nodes to the same standard as Apple's own data centers has not been demonstrated publicly.

Apple is also still insisting Siri is not a chatbot, despite shipping a dedicated Siri app with iCloud-synced conversation history. "We see Siri not as a separate chatbot, an unintegrated place you go and chitchat, but rather as an integral but conversational tool that you use in the moment," Federighi said at WWDC.

## Why it matters

Apple spent a decade arguing that owning the stack is the product. It now ships its flagship AI feature on a licensed model from the company that also pays it roughly $20 billion a year to be Safari's default search engine — an arrangement already under antitrust scrutiny. The $1 billion flows the other direction, which is a rounding error against Apple's R&D budget and a meaningful signal about where Apple concluded its own frontier models stood. Apple evaluated OpenAI and Anthropic proposals and picked Google.

The more durable story is architectural. If Apple can genuinely run Private Cloud Compute attestation on third-party hardware in someone else's cloud, it has built a template for renting frontier capability without renting out user data. Every regulated industry that wants a frontier model but cannot ship data to a model vendor is watching that. If it turns out the guarantee weakens at the Google boundary, Apple has spent its most valuable asset — the privacy claim — on a catch-up feature.

Meanwhile the EU gets nothing on iPhone. Federighi: "We're deeply disappointed that our EU users won't have Siri AI on iPhone or iPad when we share our new software releases later this year." Apple blames the Digital Markets Act's interoperability requirements; the Commission rejected its proposed Trusted System Agent workaround and an 18-month phased rollout. EU users do get Siri AI on macOS 27 and visionOS 27, which undercuts the technical-impossibility framing somewhat.

## What to watch

Whether the waitlist clears in days or weeks, and what that implies about PCC capacity. Whether the October language expansion holds. Whether security researchers get audit access to the Google-hosted PCC nodes, and what they publish. Whether the $1 billion figure survives usage at iPhone scale — a per-query cost structure across a billion-plus devices does not obviously stay flat. And whether Apple ships a replacement model of its own, the only version of this story where the arrangement is temporary.
