Meituan, the Chinese food-delivery giant that has quietly become one of the more ambitious model builders in the country, pushed out LongCat-2.5-Preview on Thursday with almost no fanfare. It's a 1.6-trillion-parameter mixture-of-experts model that the company says can see as well as write code. There was no benchmark table, no technical report and no open weights, just a post on X, a changelog entry and a price sheet. For a model this size, that left developers with plenty of questions.

"Okay this is a weird big LLM launch. Why so low-key?" wrote David Hendrickson, who posts on X as @TeksEdge, shortly after the announcement. He listed the headline specs and then added, "That's all we know."

## What Meituan actually shipped

On paper, LongCat-2.5-Preview keeps the architecture Meituan introduced with LongCat-2.0 in June: 1.6 trillion total parameters, roughly 48 billion of them active per token, and a 1-million-token context window. The new piece is native multimodality. The LongCat API platform's changelog, dated September 25, 2026, describes a "new image understanding capability" that can parse image content and supports cross-modal question answering, content summarization and "complex visual reasoning." Meituan pitches the model at long-horizon agent work that runs through terminals, browsers, graphical interfaces, spreadsheets and design tools. The earlier text-only release was tuned mainly for agentic coding.

The model is available now through Meituan's API, which accepts both OpenAI-style and Anthropic-style requests and returns up to 128K tokens per response. The company has published integration guides for Claude Code, Codex, OpenCode, OpenClaw, Kilo Code, Hermes Agent and its own CatPaw tool. Every existing LongCat platform user gets 5 million free tokens to try the model, and previously purchased token packs still work.

List pay-as-you-go pricing is $0.75 per million uncached input tokens, $0.015 per million cached input tokens and $2.95 per million output tokens. For a limited time, Meituan is charging about 40 percent of list: $0.30, $0.006 and $1.20. In China the list price is ¥5 for input and ¥20 for output, discounted to ¥2 and ¥8. Distribution partners moved quickly too. OpenCode announced the next day that "LongCat-2.5-Preview is now free on OpenCode for two weeks," and it is serving the model under a zero-data-retention policy.

The launch material leaves out a lot. According to the Chinese tech briefing service Beating AI, Meituan has not yet released benchmarks for LongCat-2.5, so there is no public data showing how much it improves on GUI operation or long-process tasks. As of Friday, the meituan-longcat organization on Hugging Face listed LongCat-2.0 in full, FP8 and INT8 versions, but there was no 2.5 checkpoint. So for now, the preview is available only through the API.

## A fast-moving lineage

LongCat-2.5 is the latest step in a release schedule that has been unusually aggressive for a company whose main business is delivering lunches. Meituan open-sourced LongCat-Flash-Chat in late August 2025, opened its API platform on September 5, 2025, and released the reasoning-focused LongCat-Flash-Thinking on September 22, 2025. In 2026 it added the 560-billion-parameter LongCat-Flash-Thinking-2601 in January and the 68.5-billion-parameter LongCat-Flash-Lite in February. In April it opened a gated LongCat-2.0-Preview beta with 5 million tokens a day per user. In late May it retired six Flash-series models from its API to free up capacity, and it made LongCat-2.0 generally available on June 30.

The 2.0 launch began with a stealth test. On June 29, the official LongCat account revealed that an anonymous model developers had been using on OpenRouter was Meituan's, posting: "Owl Alpha on OpenRouter — that's us." The company said Owl Alpha had reached the top three on OpenRouter by daily volume. According to the policy newsletter Geopolitechs, Meituan also said LongCat-2.0 was trained on more than 30 trillion tokens using a 50,000-card cluster of domestic Chinese chips. It never named the chip vendor.

Not everyone was impressed with the predecessor. Commentator @teortaxestex noted that LongCat 2.0 "boasted of benchmarks on par with contemporary SoTA," then added: "In the little tests I gave it, it was completely hopeless." That skepticism now carries over to a successor that has published no benchmarks.

## Why It Matters

LongCat-2.5-Preview adds a second trillion-parameter-class Chinese model to the field of computer-use agents, which Western labs have dominated. Few open or low-cost models have been able to compete on seeing a screen, reading a spreadsheet and acting across applications over a million-token session. Even at list price, $2.95 per million output tokens puts Meituan well below Western frontier pricing. At the promotional rate of $1.20, it undercuts many of its domestic rivals as well.

The strategy also looks familiar. Meituan builds usage first, through stealth deployments, free token grants and integrations with the coding agents developers already run, and asks for trust later. That approach made Owl Alpha a top-three OpenRouter model before anyone knew who built it. The difference this time is that Meituan has put its name on a model it hasn't backed with numbers. Because LongCat-2.0's weights were eventually published, outsiders could test the company's claims. For 2.5, no one outside Meituan can do that yet.

## What to Watch

The key question is whether a technical report and benchmark results arrive before the promotional pricing ends. Scores on computer-use evaluations such as OSWorld, and on multimodal agent suites, will show whether the new vision capabilities are competitive or just a feature on a spec sheet. Also watch whether Meituan publishes 2.5 weights on Hugging Face the way it did for 2.0, whether it confirms which domestic accelerators serve the model, and how developers rate it once OpenCode's two-week free window closes in early October.
