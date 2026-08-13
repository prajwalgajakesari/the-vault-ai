---
headline: "Code-Testing Startup Blacksmith Raises $45 Million as Valuation Jumps Nearly 10x"
slug: "blacksmith-45m-code-testing-series-b"
category: "business"
story_number: "07"
date: "2026-08-12"
---

# Code-Testing Startup Blacksmith Raises $45 Million as Valuation Jumps Nearly 10x

The great irony of the AI coding boom is that generating software was never really the hard part. Checking it is. As tools like Cursor, OpenAI's Codex, and Anthropic's Claude Code let engineers spin up pull requests faster than any human can review them, the bottleneck has quietly migrated downstream, to the unglamorous work of testing and verifying all that machine-written code before it ships. Blacksmith, a two-year-old startup built squarely on that bottleneck, just raised $45 million to widen it into a moat.

The Series B, led by Peak XV Partners, values the company at $550 million, according to CEO and co-founder Aditya Jayaprakash and a report in TechCrunch, which broke the news. That is nearly 10 times the $60 million valuation Blacksmith carried when it closed a $10 million Series A less than a year ago. Existing backers GV (formerly Google Ventures) and Y Combinator both returned, lifting total funding raised to $58.5 million.

## From CI plumbing to a validation layer

Founded in 2024, Blacksmith started life as a piece of infrastructure most people outside engineering teams never think about: cloud compute purpose-built for continuous integration, or CI, the automated pipeline that runs builds and tests every time a developer proposes a code change. Its pitch was speed. By running GitHub Actions workloads on dedicated hardware with caching and storage tuned for the job, Blacksmith promised to make those checks run dramatically faster and cheaper than the general-purpose runners most teams default to.

That foundation turned out to be well positioned for the AI coding wave. In a blog post announcing the round, Jayaprakash wrote that the release of Anthropic's Claude Opus 4.5 in December "meaningfully changed the way developers write software." Since the start of the year, he said, the number of CI jobs running on Blacksmith has grown 5 to 10 percent week over week, compounding as more engineers lean on coding agents. Every model improvement expands what those agents can do, and every expansion produces more code that has to be validated.

Blacksmith's customers describe the strain bluntly. "Our developers adopted Claude Code, PR volume increased 4x, and our CI infrastructure can't keep up," the company quoted one as saying. "We're now having incidents almost every week that block engineers from merging code."

The startup now serves more than 5,000 customers, including Mercury, Supabase, Clerk, Ashby, and Expensify, up from roughly 700 less than a year ago. (Blacksmith's own announcement puts the figure north of 6,000 companies.) On top of the CI cloud, it has layered Codesmith, an AI coding agent that not only builds features and fixes bugs but plugs directly into the validation loop, diagnosing failed checks and autofixing them to keep pull requests in a mergeable state.

## The economics of writing more code

The numbers underneath the valuation help explain investor enthusiasm. Jayaprakash told TechCrunch that Blacksmith reached a $10 million annualized revenue run rate with just 10 employees before scaling headcount to about 30, and that revenue has since climbed into the "tens of millions of dollars." He declined to give an updated figure but noted that some of its largest customers now spend more than $1 million a year on the platform.

"Validating code is still a bottleneck, and it's an even bigger bottleneck because people are writing even more," Jayaprakash said.

That single sentence captures the thesis animating this deal. The prevailing worry about AI coding tools, that they will hollow out demand for developer infrastructure, gets inverted here. If agents make each engineer several times more productive at producing code, they also multiply the volume of software that must be built, tested, and merged. The demand curve for verification bends upward, not down. Blacksmith is betting the second-order market around AI code generation, the picks-and-shovels layer of testing, CI, and validation, grows faster than the generation market itself.

## A crowded, well-capitalized field

Blacksmith is far from alone in noticing. Its competitors span incumbents and upstarts alike: GitHub Actions, the default CI system for millions of repositories; validation features increasingly baked into Codex and Claude Code themselves; Cursor's automation tooling; and the managed AI code-testing services offered by Amazon Web Services, Microsoft Azure, and Google Cloud. Jayaprakash says Blacksmith competes on two axes, the raw speed of running tests and affordability, and is spending the new capital largely on compute. The company already manages hundreds of thousands of processor cores and plans to grow that footprint by an order of magnitude in the coming months to stay ahead of demand.

Peak XV, the former Sequoia Capital India and Southeast Asia franchise, brings a track record in developer-tools and product-led companies, having previously backed Supabase and PostHog. Jayaprakash recounted meeting partners Shailendra Singh and Arnav Sahu "for the first time over Thai food in Menlo Park," and said they "understood the big picture rather quickly." Notably, the round actually closed in March; Blacksmith simply never got around to announcing it until now.

## What to watch

The open question is whether validation infrastructure becomes a durable standalone category or gets absorbed into the AI coding platforms that create the demand in the first place. Blacksmith is hedging toward the former by expanding beyond CI into a broader suite, with Jayaprakash teasing a forthcoming Codesmith QA that would autonomously test changes before they merge. If AI keeps accelerating code production the way its boosters promise, the market for making sure that code actually works may prove to be one of the more defensible bets in the entire stack. The next signal to watch is retention and spend among Blacksmith's largest accounts, the clearest evidence yet of whether the testing bottleneck is a lasting business or a temporary one.
