Google's dedicated image-generation model line ended on Monday. As of August 17, 2026, three stable Imagen 4 endpoints — `imagen-4.0-generate-001`, `imagen-4.0-ultra-generate-001` and `imagen-4.0-fast-generate-001` — are eligible for shutdown. All three shipped on June 24, 2025. All three lasted a little under fourteen months.

The recommended replacement is `gemini-3.1-flash-image`, the model developers know as Nano Banana 2. It is not a drop-in swap, it does not accept the same parameters, and for most workloads it costs more.

## Three IDs, one replacement, and a different API

Google's deprecations table lists the same August 17 date for all three Imagen 4 IDs, naming `gemini-3.1-flash-image` — in preview since February 26, 2026, stable since May 28 — as the successor. Firebase's migration guide is blunter about the scope: "All Imagen models are deprecated and will **shut down as early as August 17, 2026**. This deprecation and shutdown is applicable across Google and for both the Gemini Developer API and Agent Platform Gemini API."

The words "as early as" are load-bearing. Google's deprecations page notes that listed dates "indicate the *earliest possible dates* on which a model might be retired." No hour was published. Teams that missed the memo may still be getting 200s today, and may not be tomorrow.

What makes this more than a string swap is the interface. Imagen 4 was a `:predict`-style endpoint reached through an `ImagenModel` object and a `generateImages()` call. Gemini image models use `generateContent()` on a `GenerativeModel` with `responseModalities` set to `IMAGE`. Google's migration guide maps the old tiers by thinking level rather than by model: `imagen-4.0-fast-generate-001` becomes `gemini-3.1-flash-image` at thinking level `MINIMAL`, `imagen-4.0-generate-001` the same model at `HIGH`, and `imagen-4.0-ultra-generate-001` the pricier `gemini-3-pro-image`.

Five configuration parameters have no successor. `numberOfImages` is gone — Gemini image models always return a single image, and Google's suggested workaround is to run generation in a loop. `imageFormat` is gone; output is always PNG. `addWatermark` is gone; every output carries a SynthID watermark whether you want one or not. `personGeneration` and `negativePrompt` are gone too. Anyone who built a product around requesting four candidates per call and picking the best is rewriting their generation loop, cost model and rate-limit math at once.

## The bill goes up

Imagen 4 was priced flatly per image: $0.02 for Fast, $0.04 for Standard, $0.06 for Ultra. Gemini 3.1 Flash Image is priced per token, at $60 per million image output tokens — $0.045 for a 0.5K image, $0.067 at 1K (1024x1024), $0.101 at 2K and $0.151 at 4K, with input at $0.50 per million tokens on top.

Like for like, the standard tier goes from $0.04 to $0.067, roughly a 68% increase per 1K image. Fast fares worse: $0.02 to $0.067, more than triple, unless you route through the batch tier at $0.034 and accept the latency. Ultra users pointed at `gemini-3-pro-image` face $0.134 at 1K or 2K and $0.24 at 4K, against $0.06 before.

The counter-argument is that you are buying a different product. Gemini 3.1 Flash Image does multi-turn conversational editing, takes multiple reference images per prompt, carries world knowledge, can ground generation against Google Search and renders up to 4K. Imagen 4 did text-to-image and stopped. Nicole Brichtova, a product lead on visual generation models at Google DeepMind, framed the shift when the first Nano Banana model landed: "We're really pushing visual quality forward, as well as the model's ability to follow instructions." The outputs, she said, "are usable for whatever you want to use them for."

That describes the model fairly. It does not describe a migration path, and the gaps have been visible on Google's developer forums for months. Alexey1, an app developer, posted in March about the related retirement of `imagen-3.0-capability-001`: "The suggested replacement gemini-2.5-flash-image uses the :generateContent endpoint and doesn't appear to support explicit mask image input. Imagen 4.0 has no 'capability' variant." A second developer, Ashoka74, replied in May: "I am affected by this depreciation, planning to migrate to flux-fill. I don't understand why every model provider moves towards text-based generative models with soft-masks, it's just not-as-accurate." A third, Guillaume_Audet, flagged clients with Canadian data-residency rules for whom "Imagen 4.0 appears to be our only image generation option available in Canada."

## Why It Matters

Model deprecation is now a first-class operational risk, and most teams still treat it as a vendor announcement rather than an incident class. Imagen 4 was generally available, not preview, and still had a fourteen-month life. Google's calendar this year retired `gemini-2.0-flash` on June 1, Veo 2 and Veo 3 on June 30, and `text-embedding-004` in January, with `gemini-2.5-flash-image` due October 2, 2026 — a model that only reached GA in October 2025.

Three consequences follow. Hosted-API dependencies have a shelf life measured in quarters, not years, so a pinned model ID is a dated liability, not a stability guarantee. Replacements are increasingly not API-compatible: this one changes the endpoint, request object, response shape, error path and five configuration knobs at once — a sprint, not a config change. And the billing model can change shape underneath you, from flat per-image to per-token, making unit economics a function of output resolution that finance discovers after engineering does.

The defensive posture is unglamorous: keep model IDs in remote config, maintain a golden prompt suite you can re-run against any candidate model, and treat every deprecation email as a ticket with an owner.

## What to Watch

Watch whether Google publishes a hard cutover hour or lets August 17 sit as a soft "earliest possible" window while traffic drains — the answer tells you how much of the deprecation calendar is a deadline versus a suggestion. Watch the documentation drift: Google's pricing page still tells Imagen 4 users to "migrate to Gemini 2.5 Flash Image," itself due to shut down October 2, 2026, while the deprecations table points at `gemini-3.1-flash-image`. And watch the gaps — mask-based editing, multi-image candidates and regional availability were solved problems on Imagen and are open questions on Gemini. Some of that traffic will not migrate to Gemini at all.
