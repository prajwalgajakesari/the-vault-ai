# SpaceXAI Releases Grok 4.6, Matching Top Frontier Benchmarks at Half the Price

When SpaceXAI pushed Grok 4.6 live on August 12, the pitch was not that it had built the smartest model in the world. It was that it had built one nearly as smart as the smartest models in the world, and priced it so far below them that the comparison starts to feel unfair. Grok 4.6 scores 61 on the Artificial Analysis Intelligence Index, the composite that rolls nine benchmarks into a single number. That ties OpenAI's GPT-5.6 Sol and sits just two points behind Anthropic's Claude Opus 5, the current leader at 63. And it does so at $2 per million input tokens and $6 per million output tokens, more than 60 percent cheaper than either rival.

"Introducing Grok 4.6," the company wrote on its official account. "It delivers frontier intelligence and is a significant improvement over Grok 4.5 at the same price." The last five words are the whole strategy. Grok 4.5 shipped roughly five weeks ago; 4.6 arrived without a price increase, without a new base model, and without much fanfare beyond a single post. In a market where each release cycle now compresses into weeks rather than quarters, holding the line on price while closing a five-point benchmark gap is its own kind of announcement.

## What actually changed

Grok 4.6 is a post-training upgrade rather than a new foundation model. xAI held the base constant and spent the improvement budget on a longer supplemental training run, regenerated supervised fine-tuning trajectories across reasoning levels and agent harnesses, and reinforcement learning inside agentic environments spanning general coding, kernel optimization, web development, and computer-aided design. The result is a model tuned less for one-shot answers and more for staying coherent across long, multi-step jobs.

That focus is deliberate. The headline use case for Grok 4.6 is long-running agents, the kind of workload where a model has to research an unfamiliar domain, lay out an application's structure, implement its core interactions, and then keep refining based on feedback without losing the thread. xAI says the model produces stronger first passes on visual and interactive projects, can establish an app's structure and visual language in a single pass, and does more self-testing as a run stretches on. The model ships with a 500,000-token context window and a knowledge cutoff of February 1, 2026.

The benchmark picture is genuinely mixed. Grok 4.6 posted an Elo of 1,753 on GDPval-AA v2, second overall behind Claude Opus 5, and it also topped AA-Briefcase. But it trailed GPT-5.6 Sol Max and Fable 5 Max on DeepSWE and Terminal-Bench, two coding-heavy evaluations. The takeaway is that Grok 4.6 sits near the frontier without dominating it, and its gains cluster in agentic and knowledge-work tasks rather than across every corner of software engineering.

The most striking number is not on any leaderboard. On GDPval-AA v2's complex tasks, Grok 4.6 completes the work in roughly 53 steps. Claude Opus 5 needs about 103. For anyone paying by the token to run agents that grind through dozens of tool calls, fewer steps compound directly into lower bills, on top of a per-token rate that already undercuts the competition.

## The price story has an asterisk

The $2/$6 headline rate covers prompts below 200,000 tokens. Cross that threshold into xAI's long-context band and the rate doubles to $4 per million input and $12 per million output, and the company says the higher rate applies to every token in that request, not just the tokens past the line. For agent workflows that accumulate long histories, a single request tipping over 200K can silently double the cost of the whole call. The 500K window is real, but the second half of it is priced like a different product, and a "fast" variant costs more still.

Availability is broad from day one. Grok 4.6 is the default in Grok Build, ships in Cursor on every plan, is live on the xAI API as grok-4.6, and is routable through OpenRouter, Vercel, and Cloudflare. Cursor and Grok Build are offering double usage for the launch week, and xAI took the unusual step of resetting user rate limits. "We've reset limits to help you keep building during the Grok 4.6 launch," the Grok account posted, pointing users to a reset token in settings. xAI also says the release went through its widest pre-deployment test suite, with safeguards calibrated to the model's capabilities and continued third-party testing after launch.

## What this says about the market

The frontier is starting to look like two different races. One is for the top of the leaderboard, where Anthropic and OpenAI trade the crown by a point or two. The other is for price-to-intelligence, and that is the race SpaceXAI has decided to run. At 61 on the index, Grok 4.6 is not the best model available. But at a fraction of Opus 5's price and a fifth of GPT-5.6 Sol's output cost, it does not need to be. For teams deploying agents at scale, "second best at a third of the price" is often the winning bid.

That reframes the competitive pressure. When benchmark parity is cheap, differentiation shifts to what a model does in production: how many steps it takes, how well it holds a long context, how predictable the bill is. xAI's decision to hold price flat across two releases five weeks apart signals a belief that the ceiling on intelligence matters less to customers than the floor on cost.

## What to watch

Three things. First, whether the 200K long-context cliff bites in practice, since the agent workloads xAI is targeting are exactly the ones most likely to blow past it. Second, whether OpenAI and Anthropic respond with price cuts of their own, or lean harder on their benchmark lead to justify the premium; OpenAI's newly previewed Ultrafast API tier for GPT-5.6 Sol suggests the majors would rather compete on speed and capability than on cost. And third, whether independent agent evaluations confirm the step-efficiency gap that xAI is quietly betting the whole value proposition on.
