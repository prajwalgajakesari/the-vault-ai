Anthropic's pricing page for Claude Sonnet 5 used to carry an asterisk. The model launched June 30 at $2 per million input tokens and $10 per million output, a rate the developer docs called introductory and good through August 31. After that, Sonnet 5 would settle at $3 and $15 — which was not a new number, but the standing list price of Sonnet 4.6, the model it replaced.

On August 10, the asterisk came off. “We're making Claude Sonnet 5's introductory pricing permanent,” Anthropic's Claude account posted. “We launched Sonnet 5 in June at $2 per million input tokens and $10 per million output tokens through August 31, and that price will remain unchanged.” The platform documentation now says it without hedging: the scheduled move to $3/$15 on September 1 “will not occur.”

Two things worth straightening out, because they have been muddled in the retelling. The increase was never dated August 31 — the discount ran *through* August 31, and the higher rate would have hit September 1. And Anthropic did not invent a price hike and then retreat from it under pressure. It let a launch discount become the list price. The practical effect is the same and it is not small: Sonnet 5 is now permanently 33 percent cheaper per token than Sonnet 4.6, which still sits at $3/$15 in Anthropic's own table. Everything downstream re-rates with it. Batch processing lands at $1/$5. Cache hits cost $0.20 per million. The full one-million-token context window is billed at standard rates, so a 900,000-token request carries the same per-token price as a 9,000-token one.

## The Tokenizer Tax Did Not Go Away

The pitch that accompanied this story — that a tokenizer change was bundled into the price increase and might have been dropped alongside it — does not survive contact with the documentation. The tokenizer is still there, and it was never contingent on the pricing decision.

Anthropic's docs state that “Claude 4.7 and later models and Claude Mythos Preview use a newer tokenizer,” one that “produces approximately 30% more tokens for the same text.” That change shipped with Opus 4.7, months before Sonnet 5 existed. Sonnet 4.6 and earlier use the previous tokenizer. It was never a September 1 event, so there was nothing to cancel.

Developer Simon Willison ran the numbers at launch using his own Claude Token Counter and found the effect varies sharply by content. “So the new token is roughly 1.4x times more expensive for English, 1.33x for Spanish, 1.28x for Python code and effectively the same cost for Simplified Mandarin,” he wrote on June 30. A 4,279-line Python file that cost 44,014 tokens on Sonnet 4.6 came to 56,113 on Sonnet 5. His table also shows Opus 4.7 and Sonnet 5 producing near-identical counts on every document — 3,347 versus 3,341 tokens on the English Universal Declaration of Human Rights — which confirms the two models share the tokenizer rather than Sonnet 5 introducing its own.

Run that against the new permanent rate and the picture is genuinely better than it was, just less dramatic than the sticker price suggests. Input drops 33 percent per token while code produces about 28 percent more tokens, which nets out to a modest real saving on coding workloads rather than a third off the bill.

## The Cost-Per-Task Problem

The harder number is what Sonnet 5 does with those tokens. Artificial Analysis, evaluating the model before release, scored it 53 on its Intelligence Index — a six-point jump over Sonnet 4.6 — but measured average cost per task at $2.29, against roughly $1.97 for the pricier Opus 4.8 and about $1.20 for Sonnet 4.6. At maximum effort Sonnet 5 burns roughly 40 percent more output tokens per task than its predecessor, and on agentic benchmarks like AA-Briefcase it runs about three times as many agent loops. Those figures were computed at the $3/$15 list rate, so the permanent cut takes a third off them — but the underlying behavior is unchanged.

The Decoder's Matthias Bastian, writing on July 1, put the structural complaint plainly: “Anthropic's models keep getting pricier with each generation, sometimes dramatically so, yet the official price lists don't reflect it.” His prescription was for the industry to quote “cost per standardized task or real-world knowledge work job, rather than raw token prices that lose meaning.” The August 10 decision answers the token-price half of that critique and leaves the other half open.

## Why It Matters

Look at the week around it. OpenAI cut GPT-5.6 Sol by 20 to 33 percent, but only through November 21. Google's Gemini 3.7 Flash discount expires December 31. DeepSeek went the other direction entirely, replacing flat pricing on August 16 with peak and off-peak tiers that raised rates between 50 percent and more than 1,100 percent depending on the model — V4-Pro output went from $0.87 per million to $3.96 at peak.

Against that, Anthropic is the only major lab this month attaching no expiry date to a cheap rate. That is a claim about serving costs, not marketing. A promotional price is a bet you can absorb a loss for a defined window; a permanent one is an assertion that your inference economics clear at that level indefinitely. Anthropic filed its S-1 with the SEC earlier this year, which makes a public commitment not to raise prices a statement it will be held to by investors as well as developers. The company chose to make it anyway.

## What to Watch

Whether the $2/$10 rate holds when Sonnet 5's successor arrives, or whether the pattern simply repeats: flat headline pricing, a new tokenizer, more tokens per task. Watch for Anthropic to publish cost-per-task figures alongside per-token rates, which would settle Bastian's critique. And watch what DeepSeek's peak-hour experiment does to the mid-range — if time-of-day pricing spreads, permanence at a single rate becomes a differentiator worth more than the three dollars per million it costs.