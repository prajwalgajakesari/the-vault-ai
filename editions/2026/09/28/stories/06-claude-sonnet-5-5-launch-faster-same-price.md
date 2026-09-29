# Anthropic Ships Claude Sonnet 5.5: 30% Faster at the Same $2/$10 Price, Pushing Near-Frontier Scores Down the Stack

A week after putting Opus 5.5 at the top of its lineup, Anthropic has brought most of that model's gains down to the tier where developers actually spend money. Claude Sonnet 5.5, released Monday, generates output more than 30% faster than Sonnet 5, costs up to 30% less per task, and keeps the same price: $2 per million input tokens and $10 per million output tokens. On several of Anthropic's own benchmarks it scores within a few points of Opus 5.5, which costs twice as much.

Anthropic calls the model "a faster, lower-cost complement to Claude Opus 5.5." It is the second release in the Claude 5.5 family. Haiku 5.5, aimed at high-volume and cost-sensitive work, is due "in the coming weeks." Sonnet 5.5 is available now on the Claude Platform as `claude-sonnet-5-5`, as well as on Amazon Web Services, Google Cloud and Microsoft Azure.

## The numbers

Agentic coding shows the biggest jump. On Terminal-Bench 4.0, which tests multi-step professional tasks in a command-line environment, Sonnet 5.5 scores 70.6%. Sonnet 5 scored 10.3%, and Opus 5.5's best result is 66.4% at its Xhigh effort setting. The New Stack noted that Sonnet 5 hit timeouts and token limits on that test, which explains part of the gap. Sonnet 5.5 scores 55.5% on CursorBench 4.0, about two points behind Opus 5.5's 57.8%. On OSWorld 2.1, a computer-use benchmark, it scores 80.1% to Opus 5.5's 81.8%. On Cognition's FrontierCode, which checks whether a code change could be merged without human edits, it reaches 52.1% at Xhigh effort, against 54.4% for Opus 5.5 and 49.3% for OpenAI's GPT-6 Sol.

Knowledge work follows the same pattern. On Artificial Analysis' GDPval-AA, which ranks models by Elo score on tasks drawn from 44 occupations, Sonnet 5.5 scores 1,844. That puts it two points behind Opus 5.5, about 400 points ahead of Sonnet 5 and well ahead of GPT-6 Sol's 1,487.
Most of the price story comes from efficiency, since the rates themselves did not change. Anthropic says Sonnet 5.5 "typically needs far fewer tokens to do the same work," in part because it groups tool calls together instead of spreading them over many steps. Early customers reported similar results. Balyasny Asset Management said that on 2,441 internal finance tasks the model averaged about 121,000 tokens per answer, compared with 497,000 for Sonnet 5. Zendesk said tickets were processed 20% faster. "It made fewer wrong decisions and resolved tickets faster than the Claude models we use in production today," said Abhinay Kathuria, Zendesk's director of AI.

Some of the endorsements describe long, heavy workloads that would normally go to a flagship model. "The new model managed tens of thousands of lines of code for gameplay system architecture, kept responses snappy, handled multi-hour tasks, and delivered with less prescriptive prompting," said Daniel Vogel, chief operating officer of Epic Games.
Effort controls, which run from Low to Max, determine how much of that performance a developer gets. Claude Code and the Claude apps default to Medium, and the Claude Platform defaults to High. Anthropic says Sonnet 5.5 at Low or Medium effort beats Sonnet 5's best score on several benchmarks for roughly a tenth of the cost per task. At higher settings, its cost advantage over Opus largely disappears.

## The caveats

Anthropic does not claim Sonnet 5.5 can replace Opus. In the company's words, Opus 5.5 remains "clearly stronger at complex, open-ended work requiring sustained judgment." Anthropic recommends Sonnet for well-scoped bugs, documents, slides, spreadsheets and quick iteration, and Opus for longer-horizon work that depends on judgment.

The first hands-on reviews broadly agree. Every's vibe check concluded the model is a more capable partner than Sonnet 5 "so long as you keep a hand on the wheel and know when to call in Opus." Every's team did not all reach the same verdict. In Kieran Klaassen's 15-task coding test, as reported by Every, Sonnet 5 passed 10 tasks at low effort and Sonnet 5.5 passed 9, a reminder that aggregate benchmark gains do not guarantee better results on any particular workload. Others were warmer. "Claude Sonnet 5.5 cooks," Every designer Tyler Nishida said in Anthropic's launch materials.

There is one deployment change to note. Because Sonnet 5.5's cybersecurity abilities are roughly on par with Opus 5's, it is the first Sonnet model to launch with the cyber safeguards Anthropic uses on its top models. Higher-risk security requests will visibly fall back to Sonnet 5. Developers who run Sonnet with thinking turned off will need to move to a new `between_tools` setting before migrating.

## Why It Matters

Pricing across the industry changed quickly last week. Anthropic cut Opus 5.5 to $4/$20, and OpenAI halved prices on GPT-6 Sol and Luna the same day. Anthropic chose not to cut Sonnet's price and instead raised what the same $2/$10 buys. For teams running agents at volume, the tokens a model uses per task matter more than the listed rate, and a model that finishes the same job in a quarter of the tokens is effectively a price cut that doesn't show up on the rate card. The release also brings scores that were frontier-level a week ago down to the mid tier, which weakens the argument for defaulting to the flagship model on routine work.

## What to Watch

The first thing to watch is whether independent evaluations back up the efficiency claims outside Anthropic's own charts, especially at the Low and Medium effort settings where Sonnet 5.5 is supposed to have its largest cost advantage. Second is whether customers like CodeRabbit, which says it will move simple and moderate code reviews to the new model, shift significant spending away from Opus. Third is Haiku 5.5, which could reset the price floor for high-volume applications once it arrives.