# OpenAI Ships ChatGPT Images 2.5, Five Months After 2.0

Five months after ChatGPT Images 2.0 landed in April 2026, OpenAI has shipped its successor — and the pitch is no longer about whether the model can draw. It is about whether the model can be *directed*.

ChatGPT Images 2.5 began rolling out on Tuesday, September 8, 2026, across ChatGPT, ChatGPT Work, and Codex on desktop, mobile, and web. Unlike the staggered releases that have characterized OpenAI's recent launches, this one went to all tiers at once — free users included. Developers received two new API models: GPT-Image-2.5 Flare, the default for high-volume work, and GPT-Image-2.5 Sunburst, aimed at premium editing workflows that trade speed for control. Both are available now.

The headline number is latency. OpenAI claims generation is up to 50% faster than Images 2.0, and describes Flare as producing higher-quality output than GPT-Image-2 at half the latency. That got a second data point from a launch partner: the agent startup Manus measured Flare at two to four times the generation speed of GPT-Image-2. Adobe is bringing both models into Firefly, and Higgsfield AI and Runway also supplied early feedback.

## What actually changed

The substantive upgrades are less about raw fidelity than about persistence. Images 2.5 is built to keep a subject recognizable when its setting, style, or composition changes — the reference-led generation problem that has dogged every image model since the diffusion era began. Precision editing targets only the requested element while leaving subject, background, layout, and brand treatment intact, rather than silently regenerating the whole frame. Across longer conversations, earlier edits are more likely to survive subsequent instructions, reducing the drift that makes iterative production work expensive in retries.

OpenAI also says the model handles complex visual instructions more coherently and is better at transparent backgrounds — a small but commercially loaded capability for anyone producing packaging or app assets.

The interface changes may matter more than the weights. Users can now type `@Sketch` to draw directly inside ChatGPT and hand that drawing to the model as a spatial guide. Image comments let a user point at a region and request a focused revision. Templates such as Poster and Merch supply a predefined format up front. Shared images can optionally carry their source prompt, so recipients can adapt a concept with their own photos.

Axios' Ina Fried, who tested the model ahead of launch, reported that it "does a much better job preserving the likeness of people and pets." In one test the model's chain-of-thought notes showed it explicitly preserving a cat's "wonderfully unimpressed expression" across style transfers — a window into how identity is being reasoned about rather than merely approximated.

Adele Li, OpenAI's product lead on images, framed the new controls as a deliberate move away from prompt-and-pray generation. "The sketch tool and these templates are kind of an attempt to make people more engaged in the process of creation, rather than them being a passive force," Li told Axios. She also described a goal that cuts against the flattening effect of a single dominant model: "I don't want to be able to see ChatGPT in the world. I want people to be able to generate and express their own individualism."

Pricing is the one area where reporting diverges. Data Studios' analysis lists every Flare and Sunburst token rate at exactly 2x the corresponding GPT-Image-2 rate — image output moving from $15 to $30 per million tokens, image input from $4 to $8, text input from $2.50 to $5. Several other outlets have characterized the rates as unchanged. This newsletter has not independently confirmed the delta; readers running production workloads should check OpenAI's API pricing page directly before budgeting. What is not in dispute is the operational point: if the 2x figure holds, a latency-limited pipeline that doubles its throughput while paying double per token can see spend rise toward 4x if it stays saturated.

## The commoditization question

Image generation is now solved in the way text summarization is solved: everybody can do it, and doing it is not a business. OpenAI says users create more than 3 billion images per week across ChatGPT Images and the GPT-Image API. That volume is precisely why the differentiation has moved elsewhere.

On the Artificial Analysis Image Arena, GPT Image 2 has held the top spot, but as of September its lead had narrowed to roughly 21 points over Microsoft's MAI-Image-2.6-Preview across more than 15,000 blind comparisons. Google's Nano Banana Pro competes on price — reported around $0.027 per image at the Nano Banana 2 tier — and is the usual free-tier default. Midjourney, now at V8, remains the aesthetics specialist and has largely stopped competing on instruction-following. FLUX.2 owns the controllability niche.

Read that spread and the strategy behind 2.5 is obvious. If raw output quality converges, the moat is the editing loop: whether a model can hold a face, a logo, and a layout stable across eight consecutive revisions inside a workflow the user never leaves. Sketch, comments, and templates are not features so much as switching costs. Adobe integrating both models into Firefly is the same bet from the distribution side.

The ethical ledger has not moved. As Axios noted, these systems were trained on the work of real artists, usually without consent or compensation. OpenAI says 2.5 retains C2PA metadata, invisible watermarking, and prompt-and-image safety checks — provenance infrastructure that helps identify AI output but does nothing about how the model learned to produce it.

## What to watch

Three things. First, whether the 2x pricing figure is confirmed — it determines whether Flare's speed gain is an economic win or a wash. Second, Google's response; the Nano Banana line iterates fast and competes on cost, not capability. Third, DevDay 2026, where OpenAI is expected to detail managed agents. An image model with reliable multi-turn edit persistence is a far more useful primitive for an autonomous agent than one that regenerates from scratch every turn. That, more than fidelity, is probably what 2.5 was built for.
