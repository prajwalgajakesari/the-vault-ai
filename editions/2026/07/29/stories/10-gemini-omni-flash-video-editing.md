Google has quietly reframed one of the messiest jobs in digital production — video editing — as a conversation. With the public-preview launch of Gemini Omni Flash on its Gemini Enterprise Agent Platform, the company is betting that the next generation of marketing teams, agencies and app developers will stop wrestling with timelines and effects panels and instead simply tell a model what they want changed, one plain-English instruction at a time.

The model went live on June 30, 2026, alongside the general availability of Nano Banana 2 Lite (branded internally as Gemini 3.1 Flash-Lite Image), a companion image generator that Google says can produce a picture in as little as four seconds. Together the two releases form the clearest expression yet of Google's mid-2026 strategy: fast, cheap, multimodal "Flash" models built to be embedded directly inside agentic workflows rather than used as standalone creative toys.

## What Omni Flash actually does

Gemini Omni Flash is a video generation and editing model that accepts text, images and video as input and returns 720p video with natively synchronized audio. What distinguishes it from a conventional text-to-video system is the editing loop. Rather than treating each render as a one-shot prompt, Omni Flash is designed for iterative refinement — a user points at what is wrong and the model changes only that, while preserving the original audio and video tracks.

Google frames the capability around four pillars: conversational editing (swapping characters, relighting scenes or altering camera angles through natural language); multimodal input that maintains character, object and style consistency; "world knowledge and simulation" that pairs an understanding of physics with cultural and historical context; and text-and-action synchronization, which renders legible on-screen typography and syncs it with movement.

"Great creative happens when your tools move at the speed of your ideas," wrote Michael Gerstenhaber, Google Cloud's VP of Product Management for Cloud AI, in the launch announcement. He said the goal was to help teams "create rich, reliable experiences while reducing regeneration time and costs" — a pointed nod to the expensive trial-and-error that has defined generative video to date.

The pricing is the headline for enterprise buyers. Omni Flash is priced at $0.10 per second of video output, which works out to roughly $1.00 for a 10-second clip in output tokens, before input token costs. Google is explicit that this is a price-performance play, claiming "some of the best price-performance for video generation and editing capabilities on the market." There is no free tier.

## Why it matters

The strategic move here is placement, not just capability. Omni Flash lives inside the Gemini Enterprise Agent Platform and can be tried in Agent Studio, meaning developers can wire video creation into an agent the same way they would wire in a database query or an API call. Video stops being a separate destination app and becomes a callable step in an automated pipeline — remix a product shot, localize an ad for a new market, swap a spokesperson, all without a human opening a video editor.

Early enterprise partners suggest that framing is landing. WPP, the advertising giant, received early access and folded the model into WPP Open, its agentic marketing platform. "Gemini Omni Flash's multi-modal capabilities — allowing for seamless image, audio, and video input references — combined with intuitive conversational editing, represent a leap forward for controlled AI production," said Elav Horwitz, WPP's Chief Innovation Officer, adding that teams had tested asset localization, product swaps and style transfers for clients.

Adobe is also on board, bringing both Omni Flash and Nano Banana 2 Lite into Firefly. And Google's recommended production recipe is telling: use Nano Banana 2 Lite to rapidly generate still concepts, then hand them to Omni Flash to animate and edit — a fast, cheap, two-stage assembly line for short-form video.

The cost structure matters because it changes the economics of iteration. At a dime per second, a team can afford to regenerate and refine dozens of times, which is precisely the behavior conversational editing encourages. Both models ship with C2PA content credentials and imperceptible SynthID watermarks enabled by default, Google's answer to mounting enterprise and regulatory pressure over synthetic media provenance.

## What to watch next

Omni Flash launched with real limits. Output caps at 720p and clips are short, and Google notes that support for audio references, video references, last-frame conditioning, scene extension and higher resolutions "will be available soon." Provisioned throughput — the reserved-capacity option enterprises need for high-concurrency production — is live for Nano Banana 2 Lite but only "rolling out soon" for Omni Flash.

The open questions are whether Google lifts the resolution and duration ceilings fast enough to compete with dedicated video generators, how the conversational-editing paradigm holds up on complex multi-shot sequences, and whether the aggressive $0.10-per-second price forces rivals such as OpenAI and Runway to respond. For now, Google has made the cheapest credible bet that the future of video editing is a chat window.
