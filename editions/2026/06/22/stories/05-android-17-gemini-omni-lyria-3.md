## Google Bakes Gemini Into the Bones of Android 17

Google has stopped treating artificial intelligence as an app you open and started treating it as part of the operating system you live in. On June 16, the company shipped the final build of Android 17 alongside Wear OS 7, and the headline is not a redesigned settings menu or a faster animation curve. It is that Gemini now runs at the OS level, with three of Google DeepMind's newest models — the multimodal Gemini Omni, the music generator Lyria 3, and the speech-to-speech translation system AudioLM — wired directly into the platform rather than bolted on through a standalone download.

The release arrives first on Google's own Pixel devices through a simultaneous Pixel Drop, the company's now-familiar pattern of using its hardware as a shop window for whatever DeepMind has finished training. But the more consequential detail for the industry is that these capabilities are exposed to third-party developers through Android's AI APIs. A note-taking app, a podcast tool, or a travel planner can now call native multimodal reasoning, on-device translation, and generative music without shipping its own model or routing users out to a separate Google product.

Google is explicit that this is foundational work. Executives have framed Android 17 as the groundwork for "Gemini Intelligence," a broader agentic-OS initiative the company has previewed for later in 2026 in which the system itself can chain multi-step tasks across applications. The June launch is the plumbing; the agent is the building Google says it will put on top.

### What actually shipped

Gemini Omni is the centerpiece. It is natively multimodal — text, images, audio and video handled in a single model rather than stitched together from separate pipelines — and on Android 17 it powers conversational creation. The most demonstrated example is video editing by dialogue: a user can ask the system to trim, restyle or recompose footage in plain language. Google has described Omni as fusing Gemini's reasoning with its Veo rendering, Genie world-simulation and Nano Banana image-editing work into one model, which is why it can move fluidly between understanding a clip and generating new frames.

Lyria 3, Google DeepMind's most advanced music-generation model, is the most novel addition for everyday users. It turns a text prompt or an uploaded photo into a custom 30-second track, complete with AI-generated lyrics and cover art rendered by Nano Banana. The model first reached the Gemini app in beta in February.

"The Gemini app now features our most advanced music generation model Lyria 3, empowering anyone to make 30-second tracks using text or images in beta," wrote Joël Yawili, a senior product manager on the Gemini app, in the launch post he co-authored.

The model is pitched at casual self-expression rather than professional production — a soundtrack for a birthday message, not a chart single. Crucially for the copyright debate now engulfing generative audio, every track is embedded with SynthID, Google's imperceptible watermark, and the company says the model is "designed for original expression, not for mimicking existing artists." As Yawili's co-author Myriam Hamed Torres, a senior product manager at Google DeepMind, put it in the same post: "If your prompt names a specific artist, Gemini will take this as broad creative inspiration and create a track that shares a similar style or mood."

The third pillar is AudioLM, which drives substantially improved speech-to-speech translation on the Pixel 10a, the device that gets the fullest version of the drop. Together with Omni and Lyria 3, it rounds out a release that is squarely about audio and video — the modalities text-first assistants have historically handled worst.

### The dates and the hardware tax

Google has moved Android onto a continuous release cadence; the first Android 17 beta landed in February 2026, and Tuesday's build is the stable version. The marquee on-device intelligence carries a real hardware cost. The local agentic features lean on Gemini Nano v3 and, by Google's stated requirements, a qualifying flagship system-on-chip and at least 12GB of RAM — a bar that rules out a large share of phones sold before 2026. Heavier work, such as the previewed Chrome browsing agent, runs in the cloud on a larger Gemini model instead.

## Why It Matters

For a decade, the smartphone AI story was about assistants you summoned. Android 17 inverts that: the model is ambient, and the operating system is the surface. By exposing Omni, Lyria 3 and AudioLM through platform APIs rather than locking them inside Google's own apps, Google is trying to make Gemini the default substrate for the entire third-party ecosystem — the same playbook that made Google Maps and Google Play indispensable. If developers build on these hooks, switching costs for the whole Android base climb sharply.

It also resets the competitive clock with Apple, which is not slated to ship its catch-up Siri and iOS 27 AI upgrades until September. Google is betting that shipping native multimodal generation and on-device translation a quarter early — and handing them to developers — buys it both mindshare and a head start on the agentic era it keeps promising.

## What to Watch

The open question is whether "Gemini Intelligence" actually arrives as more than a preview. Android 17 is explicitly the groundwork; the agentic OS that executes cross-app workflows is still a 2026 promise, and Google's history of staggered rollouts means the gap between demo and shipped feature can be wide. Watch the developer uptake of the AI APIs, the SynthID watermark's durability as Lyria 3 music spreads across social platforms, and whether the 12GB-RAM floor confines the most interesting features to a thin slice of premium hardware. The plumbing is in. Whether the building gets built is the story of the second half of 2026.
