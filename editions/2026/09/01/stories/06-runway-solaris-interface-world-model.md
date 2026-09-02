Pull a shirt off a rack and drag it onto a photo of yourself. The shirt lands. Nothing compiled to make that happen — no HTML, no CSS, no click handler somebody wrote in advance. A video model looked at where your cursor went and guessed what the next frame should look like, then drew it.

That is the demo Runway published on August 31 alongside **Solaris**, which it calls the first model in a category it invented for the occasion: *Interface World Models*. The premise is a direct attack on the thing every piece of software has in common. "Every piece of software built today still requires a translation," Runway writes in its research post: a design has to become code before it can do anything. Solaris skips the translation. The frame *is* the application.

Runway's co-founder and CEO Cristóbal Valenzuela put the thesis more bluntly when he shared the work: "Video is the universal interface. Eventually, all UI will be chat and gestures in, chat and video out."

## What Runway actually built

Solaris is Gen-4.5, Runway's video generation model, retrofitted for two things it was never designed to do: understand interaction, and respond fast enough that a human doesn't notice the delay. It descends from GWM-1, the general world model Runway shipped earlier this year.

The architecture splits into two halves. A language model does the reasoning — it interprets what the user asked for, decides whether a click should modify the current scene or transition to a new one, and emits the prompts that steer rendering. Solaris does the rendering, one frame at a time, treating clicks and drags as conditioning signals in exactly the way it would treat a text prompt. Because the model only ever observes interactions that have already happened, it learns the mapping from action to visual consequence without anyone programming the consequence.

Getting a diffusion model to interaction speed took three moves, per Runway: generate frames autoregressively so each depends only on what came before, distill dozens of denoising steps down to a handful, then train the fast model on its own outputs so quality doesn't drift. The target is 720p, held stable across a full session rather than a single clip.

Runway ran two evaluations. The first tested how well frontier multimodal models — GPT-4o, Gemini 2.5 Pro and Claude Fable 5 among them — could rebuild a website from a single screenshot, scored on structural similarity and DINOv3 feature matching across 30 interfaces. Fidelity degraded consistently as visual complexity rose, which Runway offers as the cost of routing an interface through language. The second was a head-to-head: Solaris versus Claude Opus 5, same starting image, same interaction requests, judged by 250 participants across 30 examples and nearly 7,500 pairwise comparisons. Solaris was preferred on instruction following in 61% of comparisons against 24% for the coded result, with 13% called equivalent. On which behaved more naturally in the scene, the gap widened to 71% against 21%, with 6% equivalent.

## Read the fine print

"No code" is doing a lot of work here. There is still a language model in the loop writing prompts, still a serving stack, still a starting frame somebody has to compose. What Solaris removes is the *intermediate representation of the interface* — the DOM, the component tree, the behaviors enumerated ahead of time. A real deletion. Not the same as software without engineering.

The latency figure circulating in coverage deserves the same scrutiny. Runway publishes no measured per-frame number. It observes that interactions "stop feeling interactive somewhere around half a second of delay" and calls that the threshold it had to cross — a design target quoted back as a benchmark. No throughput table, no hardware disclosure, no p99.

Then there is state, or the absence of it. Solaris has no cart, no database row, no persisted form. What looks like memory is coherence in a stream of generated pixels, and Runway lists "long sessions" among its unsolved problems. It also concedes that legible text — the thing interfaces depend on more than any other visual element — remains hard, floating a hybrid where image models render text-heavy views during pauses. Accessibility is open too, which follows: a frame of video has no semantics for a screen reader. Runway is candid that per-frame generation still costs more than serving a page built once.

The comparison itself invites a question. Beating Claude Opus 5 one-shotting an interaction from a screenshot is not the same as beating a product team. Runway chose the 30 examples, defined the task, and ran the study.

And under all of it sits an assumption nobody has tested. Maximilian Schreiner, writing at The Decoder, landed on the part Runway's post never addresses: "Whether people actually want interfaces that keep changing is a question Runway leaves open." Predictability is a feature of software, not a limitation of it. A button that lives in the same place every time is doing work.

## Why this matters

The industry spent 2025 and 2026 converging on the opposite bet. Every coding agent, every design-to-code tool, every app builder assumes the artifact is source. Solaris argues the artifact is the render, and that the compression step everyone treats as neutral is where fidelity dies.

The quieter argument may matter more. Runway frames Solaris as a training environment for agents, which currently overfit to the layouts they saw and fall over on a hotel site that looks slightly different. An environment that generates layouts which never existed is a plausible answer to that generalization problem — and it does not require anyone to accept generated UIs as consumer software.

*Watch for whether Runway publishes hard latency and cost numbers, whether an early-access partner ships something a real customer touches, and whether the text-rendering problem gets solved or gets papered over with a hybrid. There is no pricing, no API, no open weights and no ship date — only a form.*
