Salesforce spent twenty-seven years teaching the business world to click. On Tuesday afternoon, hours before it reported second-quarter earnings, it shipped a product whose entire premise is that clicking was the problem.

The company announced Claudeforce, an expanded partnership with Anthropic, and with it a plugin called Salesforce in Claude that carries live CRM records, business rules, workflows and permitted actions directly into Anthropic's Claude CoWork. It launches with 37 prebuilt sales skills — meeting prep, deal health review, pipeline review — built jointly by the two companies rather than bolted on as generic prompts over an API. A seller can ask Claude which deals are slipping, get a synthesized answer drawn from live Salesforce data, and push an update back into the record without ever loading a Salesforce page.

Be precise about the state of it. Salesforce in Claude is with select pilot customers now. Open beta is expected in September 2026. Nothing here is generally available. And the two primary sources already disagree on the roadmap: Salesforce's own press release says additional prebuilt skills will begin launching in late 2026, while Salesforce president of applications and marketing Patrick Stokes told VentureBeat that skills for other business functions start arriving in the third quarter. That is a small discrepancy, but it is the kind that tends to widen.

## The moat argument

The obvious question is why a company whose valuation rests on being the place where sales work happens would voluntarily move that work somewhere else.

Stokes has an answer, and he gave it without hedging. “The value of Salesforce is not in our UI itself. It's not the application,” he told VentureBeat. “The value of Salesforce is in the data and the metadata, the years worth of kind of encoded workflows and business practices that have been built up inside of Salesforce. What we're doing is we're taking that and we're exposing it to a new UI.”

Marc Benioff put a slogan on it: “Here, the UI is the AI — allowing you to build custom apps dynamically and answer any enterprise question. Probabilistic intelligence alone doesn't run a company, and deterministic systems don't reason.” On the earnings call he was blunter, telling analysts: “This nonsense of the SaaSpocalypse, I think it's time for it to stop.” The market agreed, at least for a day — CRM shares jumped roughly 14% after the results.

Dario Amodei's framing was narrower and, read carefully, more revealing about who needs whom. “Salesforce in Claude brings this same frontier intelligence into the systems where much of the world's commercial activity happens,” Anthropic's CEO said. “Through this partnership, companies can point Claude at the customer information and business context that they've been building in Salesforce for decades.” Point Claude at it. The verb tells you which layer is being positioned as the active one.

This is not a one-off. Salesforce released Headless 360 in March — APIs, MCP servers and CLI tools designed to let agents call Salesforce with no interface at all. Data 360's MCP server is bundled into Enterprise Edition and above, running against existing API limits. Claudeforce is the consumer-facing culmination of an eighteen-month architectural bet, not a partnership announcement dressed up as one.

## If agents do the work, what is a seat?

Here is where the story gets uncomfortable, and where Salesforce is least specific.

There is no unified price. Salesforce charges through headless consumption — Stokes explained that a customer's Salesforce user license edition determines how much incremental API access they get — while the Claude inference itself is contracted separately with Anthropic. “You can't buy this on one piece of paper at the moment,” Stokes conceded. Two vendors, two invoices, one workflow.

That is the seat-pricing problem in miniature. Per-user licensing prices access to an interface. If the interface is Claude and the labor is done by an agent making thousands of API calls, the seat is billing for something that increasingly resembles a permission stub. Salesforce appears to be positioning API consumption as the successor metric, which is strategically shrewd and commercially unproven.

Analysts have been circling this since Headless 360 launched. Ashish Chaturvedi, executive research lead at HFS Research, told CIO in May that metering agent traffic creates a trap: “If you start metering every MCP call and API interaction, you create a perverse incentive: customers will throttle agent usage to control costs, which kills the very adoption flywheel Salesforce needs to justify the strategy.” Dion Hinchcliffe of The Futurum Group warned that CIOs may soon need FinOps-style governance for CRM itself — token budgets, API quotas, chargeback models. Salesforce declined to tell CIO how MCP calls are currently billed.

There is also a data-hygiene question buried in the launch materials. Salesforce's press release credits Claude-powered Slackbot with 8.1 million hours of annualized productivity gains, up more than 2x quarter over quarter. VentureBeat, briefed the same week, reported 3.8 million hours and 83% workforce adoption. Both cannot be current. Productivity-hour claims from vendors deserve the scrutiny they rarely get.

## What to watch

Three things. Whether the September open beta actually opens in September, and to whom. Whether Salesforce discloses a real consumption price sheet or keeps routing this through negotiated enterprise agreements, where discounting hides the unit economics. And whether the skills expand past sales into service and marketing on the promised schedule — because 37 sales skills is a demo, and a hundred skills across four clouds is a platform.

The deeper tell will be renewals. Salesforce is betting its data and metadata are the moat and the screens were incidental. If it is right, seat counts hold and consumption revenue stacks on top. If it is wrong, it has just spent a launch event teaching its customers that the expensive part of Salesforce is the part they can now skip.
