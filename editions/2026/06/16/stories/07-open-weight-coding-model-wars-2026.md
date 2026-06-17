# The Coding-Model Wars Splinter Into Camps as MiniMax, Qwen and Kimi Crowd the Open-Weight Frontier

In the seventy-two hours after Moonshot AI pushed Kimi K2.7 Code to Hugging Face on June 12, two more coding models landed, a benchmark leaderboard reshuffled twice, and at least three developer Slacks declared a different winner. This is the rhythm of the open-weight coding race in mid-2026: a new contender roughly every two days, each shipping bigger context windows, cheaper tokens and louder benchmark claims than the last. The frontier has not so much advanced as fragmented — into camps that no longer agree on what "best" even measures.

## A frontier defined by launches

The current wave opened on June 1, when Shanghai-based MiniMax released M3, billed as the first open-weight model to fuse three frontier capabilities at once: top-tier agentic coding, a one-million-token context window and native multimodality. Its headline trick is architectural. A new MiniMax Sparse Attention (MSA) scheme delivers roughly 15.6x faster decoding and 9.7x faster prefill at full one-million-token context compared with the prior M2, according to MiniMax's own figures. The model accepts up to 1,048,576 input tokens and emits as many as 512,000 — numbers that, a year ago, belonged exclusively to closed labs.

Eleven days later came Kimi K2.7 Code, Moonshot's coding-first release: a one-trillion-parameter Mixture-of-Experts model activating 32 billion parameters per token across 384 experts, with a 256K context window. Its pitch is efficiency. Moonshot says K2.7 burns roughly 30 percent fewer reasoning tokens than the prior K2.6 while scoring higher, and it ships a new "HighSpeed" mode that the company clocks at around 180 tokens per second on median coding inputs and up to 260 on shorter contexts — roughly six times the standard variant's throughput.

Around them sits a thickening field of open-weight rivals: Alibaba's Qwen3-Coder-Next, an 80-billion-parameter MoE that activates just 3 billion at a time and is tuned to run locally; Z.ai's GLM-5.1, MIT-licensed with a 200K window and claims of eight-hour long-horizon execution; and DeepSeek-V3.2. The closed labs loom over all of it — OpenAI's GPT-5.5, out April 23, and Mistral's Codestral line.

## The camps are forming

What is striking about mid-2026 is not that there are many models, but that they have stopped competing on the same axis. The market has split into recognizable camps.

The **frontier-capability camp** still anchors on closed weights. GPT-5.5 reported 82.7 percent on Terminal-Bench 2.0, and analysts continue to treat it as the safest bet for genuinely hard software-engineering work — at a price to match, around $30 per million output tokens.

The **open-weight value camp** is where the action is. On SWE-Bench Verified, the field's most-trusted proxy for real GitHub-issue resolution, Qwen3-Coder-Next posts 70.6 (and 44.3 on the harder SWE-Bench Pro), while GLM-5.1 self-reports 58.4 on SWE-Bench Pro and logged 75.37 on the May 12 LiveBench coding average. These models are not beating GPT-5.5 outright, but they are doing so at a tenth or less of the cost. MiniMax M3 runs $0.60 per million input and $2.40 output at list — and during a launch promotion on OpenRouter, half that. Kimi K2.7 Code sits higher, at $0.95 input and $4.00 output.

A third **speed camp** has emerged almost overnight, defined by the "HighSpeed" and "Highspeed" variants now shipping from both Moonshot and MiniMax. The bet here is that for agentic loops — where a model makes dozens of tool calls per task — latency, not raw intelligence, is the binding constraint. Cheap, fast, good-enough tokens beat expensive, slow, brilliant ones when the workflow is iterative.

## The benchmark trust problem

The crowding has exposed a measurement crisis. As of mid-June, every published number for Kimi K2.7 Code came from Moonshot itself, several drawn from proprietary in-house suites — Kimi Code Bench v2 (a claimed jump from 50.9 to 62.0), Program Bench, MLS Bench Lite — all run with thinking mode enabled. There are no independent SWE-Bench Verified, Terminal-Bench or LiveCodeBench scores for the model.

"There are no independent third-party numbers for K2.7 on the standard public suites yet, which means a true apples-to-apples comparison with Claude, GPT or DeepSeek does not exist," one analysis noted bluntly after the launch. The gap matters: a model can top its own benchmark and still disappoint in a developer's repository. With releases arriving every two days, third-party evaluators simply cannot keep pace, and the vacuum is filling with vendor marketing.

Codestral, meanwhile, illustrates how segmented the field has become. The December 2025 Codestral 25.12 scores just 42.0 percent on SWE-Bench Verified — middling by agentic standards — yet sits near the top of dense open-weight models on HumanEval-FIM, the in-line code-completion test it was actually built for. "Best" depends entirely on which job you mean.

## What to watch

The next inflection is independent verification. The moment SWE-Bench Verified and Terminal-Bench numbers land for K2.7 and M3, the camps will either consolidate or scatter further. Watch, too, whether the speed variants cannibalize the frontier tier for everyday agentic work — if $0.30-per-million tokens at 180 tokens per second prove "good enough," the economic case for $30 closed models narrows to a sliver of hard problems.

And watch the cadence itself. A field that ships a serious model every two days cannot sustain coherent comparison indefinitely. At some point the wars stop being about which model is best and start being about which evaluation anyone still believes.
