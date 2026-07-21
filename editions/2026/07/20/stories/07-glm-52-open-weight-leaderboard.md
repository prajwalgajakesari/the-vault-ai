# GLM-5.2 Holds the Open-Weight Crown, but Only Until Kimi K3's Weights Drop on July 27

Every leaderboard has a champion. Almost none of them come with an expiration date printed on the box.

As of this weekend, Z.ai's GLM-5.2 is the best open-weight model in the world for agentic coding and reasoning — top of Artificial Analysis's open-weights ranking, second overall on Arena.ai's Code Arena Frontend board, first on Design Arena, and the default pick on nearly every "best open-source LLM" list refreshed July 19. It is also a model whose reign has a countdown clock on it. Moonshot AI's Kimi K3, a 2.8-trillion-parameter MoE with a 1M-token context window, launched July 16 and already edges past Claude Opus 4.8 on Artificial Analysis's independent index. Its weights ship July 27. Six days from now, the crown almost certainly changes heads.

That is the shape of the open-weight race in mid-2026: not a plateau, but a relay.

## What GLM-5.2 actually put on the board

Z.ai — the Beijing lab formerly known as Zhipu AI, listed in Hong Kong as Knowledge Atlas Technology — ran an unusual release. GLM-5.2 went to paying Coding Plan subscribers on June 13 with no benchmark table at all. The MIT-licensed weights landed on Hugging Face and ModelScope three days later, and only then did the company publish numbers.

The model is 744 billion total parameters with roughly 40 billion active per token, identical in size to GLM-5.1, which shipped only ten weeks earlier on April 7. Context went from 200K to 1M. API pricing is $1.40 per million input tokens and $4.40 per million output.

The scores, where they can be independently checked, are close to the closed frontier. Artificial Analysis put GLM-5.2 at 51 on its Intelligence Index v4.1 — ahead of MiniMax-M3 (44), DeepSeek V4 Pro (44) and Kimi K2.6 (43), and behind only Claude Fable 5 (60), Opus 4.8 (56), GPT-5.5 (55) and Sonnet 5 (53). On GDPval-AA v2, the firm's primary real-world agentic metric, GLM-5.2 scored 1524, effectively level with GPT-5.5 at extra-high reasoning (1514).

"GLM-5.2 is the new leading open weights model on the Artificial Analysis Intelligence Index scoring 51 and it sits on the Pareto frontier of Intelligence vs Cost per Task," the benchmark firm wrote in its June 16 evaluation — the cost line being the part enterprises actually feel, at roughly $0.46 per task.

On Terminal-Bench 2.1, the autonomous terminal-coding suite that has become the de facto agentic yardstick, the numbers depend on who ran them: Z.ai reports 81.0 against Claude Opus 4.8's 85.0, while Artificial Analysis independently measured 78% — a 16-point jump over GLM-5.1 either way. On SWE-bench Pro, GLM-5.2 scores 62.1, beating GPT-5.5 (58.6) but trailing Opus 4.8 (69.2). GPQA Diamond lands at 89% by Artificial Analysis's measurement, with aggregators citing 91.2% from vendor tables.

On Code Arena Frontend — Elo-style blind pairwise human voting, much harder to game than self-reported pass rates — GLM-5.2 (Max) hit #2 by June 16 with a score between 1,593 and 1,595, beating Claude Opus 4.7 (Thinking) by 29 points and trailing only Fable 5, which is currently unsampled after the June 12 US export-control directive pulled it from availability. "GLM-5.2 is the best open model vs Kimi-K2.6 and Minimax-M3 by a large margin," Arena.ai posted, noting #2 on React and #4 on HTML sub-leaderboards.

## Where the gap is still real

The honest version of this story includes the benchmarks nobody puts in a launch tweet. On ARC-AGI-2, which tests novel reasoning that cannot be memorized, GLM-5.2 scores 22.8% at $0.25 per task against GPT-5.5's 85% — not a narrowing gap, a chasm. Humanity's Last Exam sits at 40%. CritPt, a scientific-reasoning suite, at 21%. On FrontierMath's Tier 4 problems, the hardest tier in the set, no verified GLM-5.2 figure has been published at all, which is itself informative.

Leaderboards also disagree. BenchLM's composite, refreshed July 19, ranks GLM-5.2 sixth among open-weight models at 64 — behind MiniMax M3 (69.8) and even GLM-5.1 (67.7) — flagging its evidence as "Estimated" with a 90% interval spanning 48 to 80. Composite and task-specific rankings answer different questions, and GLM-5.2's advantage is concentrated in long-horizon agentic coding, precisely the workload its architecture was tuned for.

And "open weights" is not the same as unencumbered. Self-hosting GLM-5.2 at full precision needs roughly 1,488 GB of GPU memory — eight H200s — putting genuine data sovereignty out of reach for most teams. Route through Z.ai's API instead and your prompts pass through a company subject to China's National Intelligence Law. Z.ai has been on the US Entity List since January 2025.

## Analysis: the crown is the wrong thing to watch

The interesting fact is not that a Chinese lab holds the open-weight lead. It is that the two labs contending for it are both Chinese, that the handoff is scheduled, and that the interval between contenders is now measured in weeks. GLM-5.1 to GLM-5.2 took ten weeks and gained eleven Intelligence Index points. GLM-5.2's tenure at the top will run about six.

Z.ai's positioning leans into exactly that dynamic. "Competition and collaboration are what push all of us forward," Zixuan Li, the company's head of global operations, wrote on X after Zhipu shipped ZCode, its agent harness for GLM-5.2, on July 1 — adding that the company built it "standing on the shoulders of an incredible open developer community." The subtext is not subtle: when the frontier US models are subject to export directives that can switch them off worldwide, a downloaded MIT-licensed checkpoint is the one artifact no directive reaches.

For buyers, the practical takeaway is that picking "the best open model" is now a depreciating decision. GLM-5.2 is the right answer today for long-horizon coding agents at roughly a sixth of Opus-class cost. It will not be the right answer in August, and a procurement process that takes a quarter will conclude on a model two generations stale.

## What to watch next

July 27 is the date. If Kimi K3's weights land on schedule and its Artificial Analysis position holds, the open-weight leader will, for the first time, sit above Claude Opus 4.8 on an independent index — a threshold that changes the conversation from "close enough" to "ahead." Watch three things: whether the released K3 checkpoint reproduces the API-served scores, whether anyone can actually serve a 2.8T-parameter model outside a hyperscaler, and whether Z.ai answers within its now-customary ten-week cycle. On current form, GLM-5.3 would be due in late August.

---

**Sources:** [Tech Times](https://www.techtimes.com/articles/318543/20260617/glm-52-open-weights-live-top-coding-benchmark-api-use-carries-china-data-risk.htm), [Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index), [South China Morning Post](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic), [Crypto Briefing](https://cryptobriefing.com/glm-5-2-code-arena-frontend-leaderboard/), [TECHSY](https://techsy.io/en/blog/best-open-source-llms-2026), [BenchLM](https://benchlm.ai/best/open-source), [Ace Cloud](https://acecloud.ai/blog/best-open-source-llms/)
