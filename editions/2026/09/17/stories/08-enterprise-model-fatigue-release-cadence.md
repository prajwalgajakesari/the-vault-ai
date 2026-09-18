In the first week of September, Anthropic shipped Claude Fable 5.1 and Claude Mythos 5.1 on Tuesday. Meta announced Muse Spark 1.3 and Google unveiled Gemini 3.8 Flash on Wednesday. OpenAI countered Thursday with GPT-6 Astra — the same day Abu Dhabi's MBZUAI released its open-source K2 Horizon family.

Four frontier labs, five days, and a procurement function that has largely stopped pretending it can keep up. The industry now has a name for what happened next: model fatigue.

## The buyers are not evaluating everything anymore

The phrase surfaced in CNBC reporting on September 6, and it landed because the people saying it are the ones doing the buying. "I feel like model fatigue is a real thing," Runpod CEO Zhen Lu told the network, describing an environment with "so much frothiness that you have to make noise."

The more consequential admission came from Suresh Vasudevan, CEO of enterprise AI startup Clockwork Systems, who described a triage strategy that is now common: if his team wants to evaluate ten models for a task, it may just pick five. "It's really challenging to go evaluate every one of the ones that are coming out right now," he said. His diagnosis is the sharper line: "Every release is so damn good that it's hard to tell a step-change anymore."

That is the benchmark-noise problem stated plainly. When releases land 11 days apart and each claims a couple of points on SWE-Bench or GPQA, the signal stops justifying the evaluation cost. Noah Faro, technology chief at AI finance startup Farsight, told CNBC that only two models recently moved the needle — Anthropic's Fable 5 in June and Moonshot AI's Kimi K3 in July — and that most of the September wave were point releases, not new models.

Sam Altman's explanation for the pile-up was that "we're all moving to faster cadences," with some of the acceleration down to everyone getting "back after summer vacation." Ahmed Abbasi, a professor at Notre Dame's Mendoza School of Business, offered a less seasonal read: the labs are "all playing the share-of-wallet game," racing toward public markets with Anthropic and OpenAI each valued near $1 trillion privately. Abbasi added that it is "not a coincidence" every major developer announced in the same week.

## The cadence numbers, and the cost nobody budgeted

The compression is measurable. The median interval between major frontier model releases has fallen from 37.5 days in 2023 to 11 days so far in 2026, per release-tracking data compiled by Crypto Briefing; OpenAI's own median gap went from 170.5 days to 49. The tracking site llm-stats logs 392-plus releases across 63-plus organizations, eight in the first eleven days of September alone.

The absorption side has numbers too, and they are less flattering. A Dataiku/Harris Poll survey of 600 enterprise CIOs found 81% expect to rely on two or more LLM providers in 2026 just to stay competitive, and 93% say different models perform better for different use cases — which, as the report notes, requires continual evaluation and switching. Fifty-five percent have already switched providers at least once, with cost reduction the primary driver.

Then there is the gap between how hard CIOs think switching is and how hard it is. A Zapier survey of 542 U.S. executives with active AI vendor contracts, fielded by Centiment in early February, found 89% believed they could switch vendors within a month and 41% thought they could do it in two to five business days. Among those who had actually attempted a migration, only 42% said it went smoothly; the other 58% said it either failed outright or required significantly more effort than expected.

AI consultant Haroon Choudery named the mechanism: switching model vendors "is no longer just an API migration. It is context, workflows, and institutional memory." Most operators he talks to, he added, haven't mapped any of the three.

## Why this matters: velocity is outrunning absorption

The structural problem is an accounting mismatch. Labs book the upside of a fast cadence — mindshare, benchmark headlines, a story for public-market investors — while the cost lands on the buyer's engineering budget as prompt rewrites, eval-suite churn, regression testing, compliance re-review and deprecation migrations. Gartner projects $2.59 trillion in worldwide AI spending in 2026, up 47% year over year. None of that forecast line-items the re-evaluation tax.

That has an uncomfortable implication for pricing power. The case for premium frontier pricing has always been capability leadership. But Gartner flagged "capability convergence" in June: when every new model clusters on standard benchmarks, first-mover advantage evaporates almost immediately. Open-weight competition presses from the other side — Chinese models accounted for 41% of Hugging Face downloads in spring 2026, and Kimi K3 reached benchmark parity at roughly a sixth of comparable closed-model deployment cost.

So the labs are simultaneously raising prices and eroding the reason to pay them. OpenAI lifted GPT-5.2 developer input pricing to $5.75 from $1.25 on GPT-5.1. Anthropic moved Claude's enterprise edition from fixed to dynamic usage-based pricing in April, which analysts expect could double or triple bills for heavy users. Buyers are being asked to pay more for upgrades they have explicitly stopped evaluating.

The likely equilibrium is not revolt. It is architectural defense — abstracting the model layer, routing through gateways, treating providers as interchangeable components. Rational for the buyer, corrosive for the seller: a customer who can swap you out in a config change does not pay a premium for being first.

## What to watch

Three things. Whether Anthropic and OpenAI slow their cadence as IPO scrutiny sharpens — a slowdown would be the clearest signal the share-of-wallet strategy stopped working. The Hugging Face download share for Chinese open-weight models: if 41% keeps climbing, premium closed-model revenue assumptions come under real pressure. And most telling, whether any lab starts competing on stability — longer deprecation windows, guaranteed API compatibility, migration credits. The first frontier lab to sell enterprises a slower release cycle as a feature will be the one that has read the room.
