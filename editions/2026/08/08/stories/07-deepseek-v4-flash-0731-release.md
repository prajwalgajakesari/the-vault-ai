DeepSeek moved its fast, low-cost V4 Flash model out of preview and into public beta on July 31, 2026, and within days an independent research firm had crowned it the cheapest well-known AI model in the world to run. The release — carrying the build tag 0731 and reachable simply by setting the model name to `deepseek-v4-flash` — extends the Chinese lab's pattern of undercutting rivals on price while chasing them on capability, and it lands squarely in the middle of an efficiency race that is reshaping how the industry prices intelligence.

The headline is not a bigger model. According to DeepSeek's official API change log, "DeepSeek-V4-Flash-0731 keeps the same model architecture and size as DeepSeek-V4-Flash-Preview, and was only re-post-trained." What changed is behavior on agentic and coding tasks. The company says the update delivers "significantly enhanced agent capabilities, with benchmark results far exceeding V4-Pro-Preview" — a striking claim, since it means the cheaper Flash tier now outscores the lab's own larger Pro preview on the workloads that matter most to developers.

## What DeepSeek shipped

V4 Flash is a Mixture-of-Experts model with roughly 284 billion total parameters but only about 13 billion activated per token, which is the architectural trick underpinning its low serving cost. It carries a 1-million-token context window and, per third-party listings, a maximum output in the hundreds of thousands of tokens. DeepSeek's published API pricing sits at $0.14 per million input tokens and $0.28 per million output tokens, with heavy discounts on cached input — rates that remained unchanged from the preview through the 0731 build.

On the benchmarks DeepSeek chose to highlight, the 0731 build posts 82.7 on Terminal Bench 2.1, 54.4 on DeepSWE, 76.7 on Cybergym and 54.2 on NL2Repo, alongside internal full-stack and hard-coding test sets. The company also says V4 Flash now natively supports the Responses API format and is specifically adapted for OpenAI's Codex, a clear signal that DeepSeek is courting the agentic-coding and tool-use crowd rather than pitching a general chatbot. The weights were published under a permissive license, keeping the model in the open-weights camp that has defined DeepSeek's releases.

## Why the price story dominated

Benchmark scores are contested currency, but cost is not — and cost is where V4 Flash made news. Research firm Artificial Analysis, cited by Reuters and Quartz, found V4 Flash to be the least expensive well-known model to run globally, at roughly 3 cents per benchmark test. That compares with about 86 cents for Moonshot AI's Kimi K3, $1.86 for OpenAI's GPT-5.6 Sol and $3.15 for Anthropic's Claude Fable 5, according to the firm's tally. Put differently, running the same evaluation suite on V4 Flash costs on the order of 100 times less than on a leading Western frontier model.

Artificial Analysis leans on cost-per-task rather than sticker price per token precisely because the two can diverge: a model that looks cheap per token can still run up a large bill if it needs many more reasoning steps to reach a correct answer. That V4 Flash wins on the blended metric — not just the headline rate — is what gives the efficiency claim teeth. The firm's composite Intelligence Index placed the model in the middle of the pack on raw capability, so this is a value story, not a frontier-leadership one.

## Analysis: pressure on the price of intelligence

The strategic message is hard to miss. By pushing a re-post-trained Flash tier that beats its own Pro preview on agentic coding while holding prices flat, DeepSeek is signaling that useful, tool-using models can be commoditized faster than many Western incumbents' pricing assumes. Chinese labs — DeepSeek, Moonshot's Kimi, Alibaba's Qwen and others — have collectively driven the cost of a capable open-weights model down steeply, and each release resets the floor a little lower.

For OpenAI, Anthropic and Google, the challenge is less about losing the top of the benchmark tables than about defending the economics of the vast middle market — the high-volume, agentic, code-and-tools workloads where a 100x cost gap is impossible to ignore for cost-conscious buyers. Open weights add a second lever: enterprises wary of API dependency can self-host, further eroding per-token revenue.

## What to watch next

Three things. First, whether DeepSeek's V4-Pro official release, which the company says will "follow soon," pushes the same efficiency gains up a tier. Second, whether independent evaluations of real agentic tasks — not just curated benchmarks — confirm that the cheaper Flash model genuinely rivals pricier rivals in production. Third, how Western labs respond: with price cuts, cheaper distilled tiers, or a bet that reliability and ecosystem lock-in still command a premium. The answer will say a lot about whether low-cost, open efficiency is now the industry's center of gravity.
