On August 21, developer Ben Davis posted a screenshot that ricocheted around AI Twitter within the hour. An anonymous model called Ox Alpha, which had appeared on OpenRouter the day before with no company name attached, had just beaten OpenAI's GPT-5.6 Sol and Anthropic's Claude Fable 5 on DeepSWE, a benchmark that scores how often a coding agent resolves a real GitHub issue on the first try.

"I ran this thing through 10 tasks on DeepSWE (so there could be a ton of variance in it's real score, this is a subset), but uh... gpt-5.6-sol: 52% / fable: 65% / whatever the hell this is: 80%," Davis wrote. "I am very confused."

The caveat was in the post. It did not survive the retweets.

DeepSWE has 113 tasks drawn from 91 open-source repositories across five languages. Ten of them is under 9% of the set, which means a single task swings the score by roughly ten percentage points. Davis has since finished a full 113-task run, and Ox Alpha landed at roughly 63% — level with GPT-5.6 Sol mid, and below the 65% he had measured for Claude Fable 5. Davis called the full-set number the one that "makes way more sense." By then the 80% figure had been laundered through a dozen aggregator posts as settled fact, and it is still circulating.

## What Ox Alpha actually is

OpenRouter's listing describes "a reasoning model designed for coding, sustained agentic work, and production workloads," served by a third party that chose to stay anonymous. The spec sheet is unusual: a 1,048,576-token context window, a 131,072-token output cap, and native text, image and video input. Audio requests come back rejected. It is the first stealth-series model to advertise video.

It also cost nothing. OpenCode, the open-source terminal agent, launched it the same day promising "generous rate limits, near unlimited usage" and capacity for 100 trillion tokens a day. OpenRouter's email put the free window through Monday, August 24; OpenCode's note pointed to roughly August 27. Stripe CEO Patrick Collison, whose company agreed to acquire OpenRouter on August 19, tried it and posted two words: "It's very impressive."

Developers piled in. Nous Research's Hermes Agent and the Zed editor were pushing production traffic through it within hours, and Bloomberg reported Sunday that coding tools including Claude Code had run billions of tokens through the model since Thursday.

## Nobody knows where the code went

That is the part of this story that outlasts the benchmark argument. Thousands of developers pointed agentic coding tools at a 1M-token context window run by a company that has not said its name.

The forensics have been more rigorous than the scoring. A developer known as unclecode, author of the Crawl4AI crawler, built a tool called modelprint that fires nine infrastructure probes at an anonymous endpoint and matches the responses against known models. Ox Alpha lined up with Z.ai's GLM-5.3 on six of nine, including all four normalized tokenizer counts; no other lab's best candidate cleared more than two of the four. A separate analysis by Ananay Arora put it bluntly: "Ox Alpha's tokenizer is one for one identical to GLM's. No other lab's tokenizer gets past 4/11." Davis reported exact token-count matches with GLM-5.3 across 25 prompts, off by a constant +75 tokens he attributed to a hidden system wrapper. Video-token spend matched GLM-5V-Turbo across four controlled clips, and the model shares GLM's distinctive "1301" error code.

None of that is a confession, and unclecode says so in his own documentation: "Matching fingerprints prove shared infrastructure, not identity." A lab can serve two different models on the same stack. Z.ai has said nothing, and one detail complicates the read: GLM-5.3 shipped August 14 as a text-only model, six days before Ox Alpha turned up with video. Treat Zhipu/Z.ai as a strong community inference, not a fact.

The inference matters because of what sits behind it. OpenCode's route advertises "zero data retention" from a provider it does not name. OpenRouter's model page says prompts and completions are retained by the provider and not used for training; the broader stealth-preview terms extend to training, evaluation and improvement. SiliconANGLE's Duncan Riley put the gap plainly: "Enterprise code is flowing to a provider with no name attached. Nobody sending it can check where it lands." And if the GLM attribution holds, that provider's parent was added to the U.S. Commerce Department's Entity List in January 2025.

## The mask is the marketing

Ox Alpha is the fifth anonymous release in six months, and the previous four all resolved the same way. Pony Alpha became Zhipu's GLM-5 in about five days; Hunter Alpha became Xiaomi's MiMo-V2-Pro; Elephant Alpha became Ant Group's Lingxi Ling-2.6-flash; Owl Alpha ran unclaimed for two months before Meituan named it LongCat-2.0.

The stated rationale is that anonymity strips brand bias out of evaluation. The practical effect is cheaper distribution than any launch event buys: a global developer audience in hours, the guessing game as free press, and frontier-scale usage data — long-context stability, tool-calling reliability under load — without the lab owning a single bad benchmark. The lack of a brand is the marketing.

What the Ox Alpha cycle exposed is how badly that interacts with small-sample benchmarking. A 10-task run is a vibe check, not a measurement, and Davis flagged it as one. But an anonymous model with no leaderboard entry creates a vacuum, and the first number into a vacuum becomes the number. Ox Alpha still has no entry on Artificial Analysis or LMArena. The public DeepSWE leaderboard is led by Claude Opus 5 at 73.6%, GPT-5.6 Sol at 72.7% and Claude Fable 5 at 69.7% — with Ox Alpha absent.

## What to watch

Whether anyone claims it after the free window closes around August 27 — the last four reveals took five days to two months. What it costs once the meter turns on, the only figure that tells you whether "frontier" was a spec or a tagline. And whether an independent leaderboard posts a full-set score before the next stealth model arrives and the cycle restarts with a fresh screenshot.
