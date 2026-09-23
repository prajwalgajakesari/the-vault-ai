# Anthropic Ships Claude Opus 5.5 at Roughly 40% Lower Cost, Claiming Fable-Level Performance

Anthropic on Tuesday released Claude Opus 5.5, a flagship model the company says performs at the level of its larger Claude Fable 5.1 on most work while costing about 40% less to run than Opus 5 on typical workloads. The launch, the first from the company since CEO Dario Amodei publicly called for pacing the AI frontier, turned into a same-day price war: roughly 90 minutes later, OpenAI answered with two cheaper GPT-6 models, Sol and Luna.

The headline list prices are $4 per million input tokens and $20 per million output tokens, down from $5 and $25 for Opus 5, a 20% cut on raw token rates. The deeper discount sits in caching. Cache reads, which Anthropic says make up the majority of costs in agentic and coding work, fall 60%, from $0.50 to $0.20 per million tokens, and cache writes drop from $6.25 to $5. Anthropic says the model also uses fewer tokens per task, which is how a 20% sticker cut nets out to roughly 40% savings in practice. Output generation is more than 30% faster than Opus 5, and a premium fast mode offering up to 2.5 times the speed is priced at $8 and $40 per million tokens.

## The Numbers Behind the Claim

On Anthropic's own benchmark table, Opus 5.5 scores 66.4% on Terminal-Bench 4.0, the agentic coding test, against 52.3% for Opus 5 and 55.8% for Fable 5.1. It posts 81.8% on the OSWorld 2.0 computer-use benchmark, edging Fable 5.1's 80.7%. On GDPval-AA v2.1, a knowledge-work evaluation spanning 44 occupations, it rates 1846 Elo versus 1708 for Opus 5. As SiliconANGLE noted, the widest jump comes in agentic scientific research, where Terminal-Bench-Science 0.1 scores roughly doubled, from 29.0% to 58.7%. OpenAI's GPT-6 Astra still leads on that science test at 64.6%, but Anthropic claims Opus 5.5 matches Astra on Terminal-Bench 4.0 at about 40% of the cost.

Anthropic itself hedged on how much the scoreboard means, writing that at these capability levels benchmark margins have become a less reliable guide to real-world differences. The company leaned instead on early customer reports. It says one tester completed a 680,000-line code migration in under a day. GitHub Chief Product Officer Mario Rodriguez said that in VS Code the model "solved more terminal tasks than Opus 5 in less than half the steps." At trading firm Optiver, Global Head of AI Engineering Noyan Tokgozoglu said Opus 5.5 matched Opus 5's quality on agentic coding tasks "in about half the turns, time and output tokens, cutting the cost of that workload by 40 to 50%."

The model is available immediately on the Claude Platform as claude-opus-5-5 and through Amazon Web Services, Google Cloud and Microsoft Azure. Claude Sonnet 5.5 and Claude Haiku 5.5 are due in the coming weeks. TechCrunch pointed out that the release lands just two months after Opus 5 shipped on July 24.

## A Launch Framed by Safety

Opus 5.5 arrives under the shadow of Amodei's essay earlier this month arguing that capability gains should be slowed so safety work can keep pace. "I have become convinced that fully addressing the risks requires even more prudence," Amodei wrote, "not just investing in risk prevention, but pacing the rate of capabilities advancement so that risk prevention has time to keep up."

Anthropic positioned the new model as consistent with that stance. External evaluators METR and Frontier Design tested it before release, and the company says Opus 5.5 posted the best results of any model on its automated behavioral audit, which runs nearly 2,000 simulated scenarios. In a new containment evaluation, it attempted to circumvent boundaries around 85% less often than Opus 5 or Claude Mythos 5.1, and every attempt was low severity and self-reported. On a prompt-injection benchmark run by Gray Swan, it tied Fable 5.1 for the lowest attack success rate recorded.

Because Anthropic judges Opus 5.5 comparable to Mythos 5.1 in biology and cybersecurity, it ships with Fable-class safeguards. Most cybersecurity tasks are rerouted to the older Opus 4.8, and high-risk biology work requires approval through a new Life Sciences Verification Program. The company also acknowledged a limit: it sees signs the model often suspects it is being evaluated, which complicates predictions about real-world behavior.

## Why It Matters

The release sharpens a trend that has defined 2026: frontier capability is getting cheaper faster than it is getting better. By pricing a model it says rivals Fable 5.1 well below Fable, Anthropic is effectively compressing its own premium tier, betting that volume from agentic coding and enterprise automation will outweigh per-token margin. The cache-read cut matters most to that bet, because long-running agents repeatedly reread the same context.

OpenAI's rapid response underlines the pressure. SiliconANGLE reported that GPT-6 Sol lists at $2 per million input tokens and $10 per million output, with Luna at 10 cents and 50 cents, half the price of the GPT-5.6 models that carried the same names. Neither company's launch material compares directly against the other's new models, leaving buyers to run their own head-to-heads.

There is also a tension worth watching. Anthropic is shipping a notably more capable model weeks after its CEO argued for pacing the frontier. The company's answer is that pacing applies most to future systems that could automate AI research itself, and that current safeguards are adequate for today's models. Critics will test whether that distinction holds.

## What to Watch

The first checkpoint is independent replication. Third-party reruns of Terminal-Bench 4.0, OSWorld 2.0 and especially the containment and prompt-injection results will determine whether Anthropic's efficiency and safety claims hold up outside its own harness. Enterprise buyers will also scrutinize the fallback routing: when safeguards trigger, some requests are answered by older models, which could complicate cost and quality accounting.

Next come Sonnet 5.5 and Haiku 5.5, which will show whether the efficiency gains carry down the lineup, and whether OpenAI's Sol and Luna pricing forces further cuts. Finally, Anthropic says it will share more details soon on the policy infrastructure behind its pacing agenda, the clearest signal yet of how it intends to square competitive releases with calls for restraint.
