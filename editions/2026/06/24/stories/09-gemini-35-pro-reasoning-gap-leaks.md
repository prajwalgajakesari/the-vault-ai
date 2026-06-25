Six weeks after Sundar Pichai stood on the Google I/O stage and promised developers that Gemini 3.5 Pro would ship in June, the calendar is closing in and the model is still locked behind an enterprise preview. Now a fresh batch of unconfirmed leaks suggests that when it finally arrives, it may land with a reasoning gap against the two rivals Google most needs to beat: Anthropic's Fable 5 and OpenAI's anticipated GPT-5.6.

The leaks, surfaced by the testing collective Universe of AI and reported by Geeky Gadgets, paint a model that is strong where Google has historically been strong and soft precisely where the frontier fight is being decided. According to those accounts, Gemini 3.5 Pro struggles in advanced reasoning, long-horizon task execution, and — most pointedly for the developer audience Pichai was addressing — bidirectional code processing and code infilling. None of this has been confirmed by Google, and the claims should be treated as exactly what they are: pre-release chatter from people testing a gated preview build, not benchmark results from a shipped model.

## What the leaks claim

The throughline in the leaked notes is that Gemini 3.5 Pro handles linear generation well but falters when a task demands working backward through context — filling code into the middle of an existing file, reconciling edits across a large codebase, or holding a multi-step plan together over a long horizon. Those are the workloads where Fable 5 has built its reputation and where OpenAI's leaked "UltraFast Codex" mode for GPT-5.6 appears aimed. Reporting on GPT-5.6 also points to a context window expanding to roughly 1.5M tokens, narrowing one of Gemini's few clear advantages.

There is a genuine bright spot. The same leaks describe a significant jump in vision and multimodal understanding, the lane where Google's research pedigree runs deepest. If that holds up after general availability, it gives Gemini 3.5 Pro a defensible story — just not the one Google wanted to tell to coders.

The confirmed specs remain impressive on paper: a 2M-token context window, a Deep Think reasoning mode gated to Ultra subscribers at $250 per month, and frontier multimodal understanding. Expected pricing lands around $15 per million input tokens and $60 per million output tokens — roughly 10x the cost of Gemini 3.5 Flash, and a price that only pays for itself if the reasoning is genuinely best-in-class.

{}

## Why the timing is brutal

The leaks would sting in any month. They sting more in this one. In the same week, Google DeepMind lost two of its most recognizable researchers: John Jumper, the Nobel laureate and AlphaFold co-creator, departed for Anthropic after nearly nine years, and Noam Shazeer — co-author of "Attention Is All You Need," the paper that gave the world the Transformer — left for OpenAI. Both moves landed inside roughly 48 hours, and Google's shares fell more than 5% as the news spread.

That backdrop turns a delayed launch into a narrative problem. As Fortune framed it in its June 23 report, the departures have left "some question if the lab can remain at the forefront of AI development." A frontier model that slips its window and then leaks soft on coding feeds directly into that doubt. Google's pitch has long been that its research depth would eventually translate into a model that wins on every axis. The leaks, if accurate, suggest a model that wins on perception and multimodality but cedes the developer battleground.

And the developer battleground is the one that matters commercially right now. Coding assistants and agentic tooling are where enterprise spend is concentrating, where Anthropic has carved out a durable lead with the Claude line, and where OpenAI is pushing hard with Codex-branded speed modes. A model that is weak at code infilling and bidirectional processing is weak at exactly the task that fills an IDE sidebar all day. Earlier reporting already had Gemini 3.5 Flash trailing Fable 5 on coding benchmarks while competing closely with GPT-5.5 at a lower price; the Pro tier was supposed to close that gap, not inherit it.

## The June 30 watch

The immediate question is simply whether it ships. Gemini 3.5 Pro has been in limited Vertex AI enterprise preview since early June but has not reached general availability, and prediction markets put the odds of a June 30 launch at roughly 50 to 55 percent — effectively a coin flip on a deadline Google set for itself. Pichai's on-stage ask to "give us until next month," which reportedly drew a groan from the I/O audience, now reads less like confidence and more like a hedge.

There is a plausible benign reading. Google may be holding the model precisely to address the weaknesses the leaks describe, and a preview build is by definition unfinished — infilling and long-horizon behavior are the kinds of things that improve sharply in the final tuning passes. A polished GA model could land well above its leaked reputation, and the multimodal gains alone could reframe the conversation.

But the company no longer controls the timing of the story. Every additional day past June 30 is a day GPT-5.6 and Fable 5 own the frontier conversation, a day the talent-flight narrative compounds, and a day the leaks calcify into received wisdom. Whether Gemini 3.5 Pro closes the reasoning gap or merely confirms it, the next week will tell us a great deal about whether Google can still ship a frontier model on its own schedule — and on its own terms.
