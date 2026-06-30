---
headline: "'Tokenmaxxing' Is Over: Enterprises Pivot From Spend-at-All-Costs to Model-Routing Efficiency"
slug: tokenmaxxing-over-enterprise-efficiency
category: business
story_number: "02"
date: 2026-06-29
---

# 'Tokenmaxxing' Is Over: Enterprises Pivot From Spend-at-All-Costs to Model-Routing Efficiency

Six months ago, the fastest way to look like an AI power user inside a big technology company was to burn tokens. Engineers raced up internal leaderboards for consuming the most artificial intelligence, dispatching autonomous agents to grind on tasks for hours, and defaulting to the priciest frontier model for every job, no matter how trivial. They had a name for it: "tokenmaxxing." Then the invoices arrived, and the spreadsheet-keepers took over. The leaderboards have been quietly deleted, monthly caps installed in their place, and finance teams are now asking a far less flattering question: what did all those tokens actually ship?

That swing, from spend-at-all-costs to ruthless cost discipline, has unfolded in a matter of months across some of the most AI-hungry companies in the world, and it is beginning to look like the first real test of the demand assumptions underpinning the AI boom.

## When the bills landed

The poster child for the reversal is Uber. The ride-hailing company told employees in May that it had blown through its entire projected annual AI spending in just four months. The detail is striking not because Uber was reckless but because it was typical: roughly 95% of its engineers were using Anthropic's Claude Code monthly, and around 70% of code commits were originating from AI. Per-engineer monthly API costs were running anywhere from $500 to $2,000. Uber has since imposed a cap of $1,500 per person, per tool, per month, with higher tiers available on request.

What rattled executives was not the size of the bill alone but the missing link to value. Uber Chief Operating Officer Andrew Macdonald put the tension plainly, noting that if a company cannot connect its spending to useful features shipped, "that trade becomes harder to justify. That link is not there yet."

Uber is far from alone. According to reporting that has rippled out from the *Financial Times*, *The Verge* and *The Information*, Amazon shut down its internal AI usage leaderboard after it devolved into a volume-chasing contest, with senior executive Dave Treadwell warning staff not to use AI "for AI's sake." Microsoft moved to revoke most internal Claude Code licenses in one division and push engineers back to its in-house GitHub Copilot tooling. Meta told employees it would limit AI use after an "exponential increase" in costs, and Walmart and AT&T have set their own caps. The new behavior even spawned a counter-buzzword, "tokenminning," short for token minimizing.

## The fix: route the model, not max the tokens

The technique enterprises are converging on is deceptively simple: reserve frontier models for genuinely hard problems and route everything else to cheaper alternatives. The savings are large. AT&T chief AI officer Andy Markus says firms can cut costs by as much as 90% by opting for less advanced models, adding that "for most use cases, the latest greatest frontier model isn't needed." A wave of "gateway" tools and automatic model routers, from Microsoft, Databricks and the Nvidia-backed startup Factory, has emerged precisely to assign low-complexity tasks to low-cost models without a human deciding each time.

The math behind the bills explains why routing matters so much. A summarized meeting transcript might cost a few hundred tokens; writing a feature can run to tens of thousands. Agents, which repeatedly re-read context as they work, consume roughly 1,000 times more tokens than a standard code question, according to a joint Google and Microsoft paper. Most of that cost is in input tokens, the model re-reading the same context over and over, which is exactly the inefficiency routing and caching attack.

Just as telling is the scramble to change what gets measured. Salesforce, which CEO Marc Benioff says still plans to spend hundreds of millions on AI this year, now tracks "agentic work units" rather than raw tokens. Amazon has reset its north-star metric to "customer and business problems solved." Microsoft's Satya Nadella has been floating "Token Capital," reframing usage as a reusable enterprise asset rather than a meter that only spins.

## What it means for OpenAI and Anthropic

This is where the story turns from corporate housekeeping into a genuine question for the frontier labs. At the height of tokenmaxxing, both OpenAI and Anthropic reported record revenue from coding tools; Anthropic reported a roughly $47 billion annualized run rate in May, up from about $10 billion in revenue for all of last year, while OpenAI's run rate paced closer to $25 billion, up from $13.1 billion in 2025. Much of that vertical growth came from exactly the enterprise token consumption now being throttled.

Gil Luria, an equity analyst at D.A. Davidson, frames the implication bluntly. Current growth rates for Anthropic and OpenAI, he argues, "are the fastest they will ever be, which is mostly a matter of basic math." That, in his view, is a good reason for both companies to go public now, "as is the concern that some of their largest enterprise customers may start limiting their out-of-control token spend." Luria expects "some period of time in the future where there's some rationalizing of spend by companies, and that may be a blip ahead for Anthropic and OpenAI."

For the AI-bubble debate, the pivot cuts both ways. Skeptics will read declining token intensity as the first crack in a demand story that assumed usage could only compound. Bulls will counter, correctly, that almost no one is actually spending less in aggregate. Meta is still on track to spend billions, Salesforce hundreds of millions; they simply want the same or better output for fewer tokens. The risk the labs face is not collapse but normalization, the moment a hyper-growth curve bends toward something that looks like ordinary enterprise software economics, with all the multiple compression that implies for a pre-IPO valuation.

## What to watch

The honest counterpoint is that nobody is certain tokenminning works yet. The link between spend and shipped value may be weak today simply because the measurement tools are immature, not because the spending is wrong. Cut too hard and companies risk throttling the very experimentation that produces breakthroughs, the corporate equivalent of skipping lunch to save money and crashing at 3 p.m.

Three things will tell us which way this breaks. First, whether OpenAI's and Anthropic's next reported run rates show the deceleration Luria predicts, or whether new use cases backfill the throttled coding demand. Second, whether in-house tools like Meta's MetaCode and Microsoft's Copilot CLI meaningfully claw enterprise spend back from the frontier labs. And third, the IPO timing itself: if Anthropic or OpenAI moves to file sooner rather than later, take it as a signal that even the companies selling the tokens believe the easy-growth window is closing.
