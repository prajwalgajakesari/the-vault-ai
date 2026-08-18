Z.ai did not train a new model. It kept training the old one — and what came out is now the strongest open-weights coding agent on the market and, by the company's own admission, better at finding software vulnerabilities than it expected or intended.

GLM-5.3, released Thursday, August 14, shares its base model with GLM-5.2. Every gain came from scaling reinforcement-learning post-training on that same 743-billion-parameter foundation. "Scaling post-training is all we did for GLM-5.3," the Beijing lab wrote in its launch post. "With GLM-5.2 we built the stack... Over the past month we kept scaling on this stack: more environments, more diverse tasks, and more compute spent training on them."

The coding numbers are strong. The cyber numbers are the ones that made Z.ai hold the weights back.

## The Coding Numbers

The headline jump is Terminal-Bench 3.0, which measures autonomous shell and tool use in real Linux environments: GLM-5.3 scores 28.3, against 4.6 for GLM-5.2, with no new pretraining run. On DeepSWE v1.1, an end-to-end GitHub-issue-fixing benchmark, it moves from 46.2 to 66.9. SWE-Marathon v1.1 goes from 19.4 to 42.5.

"GLM-5.3 is our strongest coding agent so far," wrote Lou, a Z.ai team member who posts as @louszbd on X. "It scores more than six times higher on Terminal-Bench 3.0 and ranks #1 among open models on 8 out of 9 benchmarks."

Z.ai also claims a roughly 50 percent gain on its internal Z.ai Code Bench, hitting 34.5 percent at Max effort while burning about 75,000 output tokens per task — versus GLM-5.2's 23.4 percent at 96,000. Better results, fewer tokens. That efficiency framing matters more than the raw score, because it is where the economics live.

The closed frontier is still ahead. Z.ai's own blog concedes GLM-5.3 "remains behind Claude Fable 5, which reaches 39.5% at Max effort." On Terminal-Bench 3.0, Fable 5 (33.7) and GPT-5.6 Sol (34.6) beat it; on DeepSWE v1.1, so does Chinese open rival Kimi K3 at 67.5.

Pricing is the counterweight. GLM-5.3 ships first through Z.ai's GLM Coding Plan and its ZCode agent, on a points quota with off-peak calls at half cost, and works with Claude Code and OpenCode. Zhipu's API sits at roughly a tenth of U.S. frontier per-token rates — GLM-5.2's official rate was $1.40 in / $4.40 out per million tokens, against $1.75 / $14 for GPT-5.3-Codex.

## The Part Z.ai Didn't Plan For

Z.ai deliberately added vulnerability-discovery data and security task environments to post-training. It expected better bug hunting. What it says it got was categorically different: the model "began to reason across multiple stages of exploitation, forming coherent plans for complete exploitation chains."

On CyberGym, which tests white-box vulnerability discovery from source, GLM-5.3 scored 84.5 percent versus 77.2 percent for GLM-5.2 — above Anthropic's Mythos at 83.8 percent and OpenAI's GPT-5.6 Sol at 83.6 percent, per Zhipu's own testing. On ExploitBench it more than doubled, 24.4 to 54.4 percent, though it still trails Mythos (78 percent) and GPT-5.6 Sol (76.5 percent) there.

Tested against real codebases with security teams in China, Z.ai says the model surfaced 2,436 vulnerabilities across 269 projects after expert review and deduplication — 1,097 rated medium-to-high severity, spanning kernels, browser engines, and network protocols. Axios reports findings in the Linux kernel and across widely used VMware and Apache projects. The oldest flaw dates to 1981. Findings go into a public Security Disclosure Ledger; at launch, 53 were disclosed and 2,383 remained under embargo.

Then the demo that traveled furthest. "We gave GLM-5.3 a complex reverse-engineering task. It found a potentially serious vulnerability in Cursor," Lou wrote. "We disclosed it privately. Appreciate Cursor team is working closely with us on a fix." No CVE has been published, and there is no independent confirmation beyond the vendor's account.

So the weights are late. Z.ai is staging release — selected security partners in controlled settings first, then broader API access, then full weights in roughly two weeks. That is a sharp break from GLM-5.2, which landed MIT-licensed on Hugging Face almost immediately. "An open world cannot have only open attack surfaces," the company wrote on X. "It must also have an open shield." It also acknowledged that once weights are public, it cannot control how the model is modified or used.

## Why It Matters

Two things are converging here, and only one is comfortable.

First, the open-weight frontier gap is now a matter of months, not generations — and it is being closed by post-training compute rather than ever-larger pretraining runs. That is a cheaper lever, one a lab on the U.S. Entity List can pull without new frontier silicon. Chinese open-weight models already out-consume American ones on OpenRouter token usage. Price is doing the work benchmarks don't.

Second, agentic coding ability and offensive cyber ability are not separable. They are the same capability pointed at different targets: read a large unfamiliar codebase, form a multi-step plan, execute in a shell, verify. Z.ai scaled the first and got the second for free. Security researcher Joshua Saxe argued of the previous generation that "GLM-5.2, not Mythos, is the real security emergency" — his point being that a downloadable model removes the API chokepoint that lets U.S. labs observe and throttle malicious use. GLM-5.3's exploitation gains sit highest exactly where the "purely defensive" argument is weakest.

Every number above is Z.ai-run. CyberGym at 84.5 percent has not been independently reproduced, and the internal Code Bench cannot be audited outside the company.

## What to Watch

The two-week clock. If the weights land on schedule at roughly the end of August, the real test begins: whether independent evaluators reproduce 84.5 percent on CyberGym, whether the 2,383 embargoed findings hold up as fixes ship, and how fast someone fine-tunes the safety hardening back off. Watch the Cursor disclosure for a CVE. Watch whether U.S. labs — several of which have already slowed releases over cyber risk — read this as cover to move faster or proof they were right to slow down. And watch Washington, reportedly weighing how to regulate open models as their capabilities converge with closed ones. GLM-5.3 will be the case study either way.
