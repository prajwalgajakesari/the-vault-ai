Somewhere in the enterprise software stack, an AI agent is quietly installing a "skill" it found on the open internet — a bundle of instructions and code that extends what it can do. Nobody signed it. Nobody reviewed it. And per research published Monday by an Israeli startup that has existed for roughly six months, more than 17,800 such public AI add-ons are circulating right now, accounting for roughly 6.7 million installations, all of them pulling instructions from external sources nobody verified.

That research is the calling card for **AIR Security**, which emerged from stealth on September 1 with $50 million and a pitch that sounds almost quaint until you sit with it: AI agents need a firewall.

The money arrived in two seed rounds that closed within weeks of each other, both inside the company's first six months. Sequoia Capital led the first at $10 million. Greenoaks Capital Partners led the $40 million that followed. Swish Ventures and Netz also participated, alongside security-world angels including Wiz co-founder Yinon Costica, Clay co-founder Varun Anand, Cognition president Zach Frankel, and Anne Neuberger, the former White House deputy national security adviser for cyber and emerging technology.

## What AIR actually built

AIR was founded in February 2026 by CEO Yair Saban and CTO Niv Hoffman, who met roughly a decade ago in Israel's Unit 8200 intelligence corps doing offensive cybersecurity. The company employs around 40 people and has recruited Ryan Knisley, formerly CISO at both The Walt Disney Company and Costco Wholesale, as chief strategy officer.

The product has three moving parts. Discovery: the platform maps every agent running across a company's endpoints, cloud accounts, and SaaS applications, including shadow deployments where employees use unapproved AI tools or personal accounts. Enforcement: AIR hooks into those agents to intercept and analyze actions in real time — loading a skill, fetching a web page, calling an MCP server. And a continuously maintained whitelist; Saban says the platform currently filters out roughly 27% of the add-ons and skills it encounters online. AIR is also building a marketplace of pre-vetted add-ons so enterprises can extend their agents without rolling the dice.

Saban's framing leans on an analogy from an earlier era of the same mistake.

*"In the early 2000s, whenever you installed a driver, the driver didn't need to be signed. Today, every time you install a driver, you see a signature saying who signed it, because the driver is actually loading code into the kernel,"* Saban told TechCrunch. *"You don't have that with skills or plug-ins or MCPs, and it's a shame, because it's the same mechanism, it's the same lesson, but we haven't learned it."*

His sharper argument is that the industry is worrying about the wrong thing. The dominant enterprise anxiety around agents is permissions — what an agent is allowed to touch. Saban thinks that's secondary. "We think it becomes dangerous when it is exposed to malicious information," he told Calcalist, naming three vectors: extensions installed on an agent, websites it visits, and internal organizational data. An agent fed poisoned content will misuse permissions it was legitimately granted.

AIR's own research supports the point. Beyond the 17,800 add-ons, its researchers found AI skills impersonating Anthropic and OpenAI, apparently designed to slip past platform security reviews. At least one, AIR says, could execute arbitrary code on enterprise systems.

The company claims more than 20 customers, about a quarter of them large enterprises, with the strongest demand from financial services and pharmaceutical firms — the industries with the most regulators looking over their shoulder.

## Why this matters: the agent supply chain becomes a real attack surface

For twenty years, software supply chain security was a specialist concern: important, underfunded, mostly about npm packages and build pipelines. Agents change the economics in two ways.

The first is speed. A traditional supply chain attack requires a compromised dependency to survive a build, a review, and a deploy. An agent installs a skill mid-task, at runtime, based on its own judgment about what it needs. There is no pull request. Greenoaks partner Patrick Backhouse put it plainly in the funding announcement: agents operate at runtime "using skills, plugins, add-ons, and MCPs from sources that no security team has reviewed, and slipping past scanners built for yesterday's code."

The second is mutability. A skill that passed review in March can be rewritten in June by whoever maintains it — or by whoever compromised the maintainer's account. Sequoia partner Bogomil Balkansky calls this the crux of the category, and conveniently for his portfolio company, the hardest part to copy.

*"This is not a scanning problem, it is a continuous re-verification problem,"* Balkansky told TechCrunch. *"Inspecting every skill, plugin, MCP server and sub-agent an enterprise's agents touch, re-inspecting each one every time it changes, in real time and across an entire company's agent fleet, is an infrastructure problem long before it is a security problem."*

Saban agrees that this — not discovery — is the defensible piece. "Gaining visibility over the endpoint, that is easy," he said. "Everybody's going to do it. It's hard to create a moat around that."

He is right to worry, because everybody is. Noma Security, Zenity, Astrix Security, and Operant AI all sell overlapping agent discovery and control products. Zenity closed a $125 million Series C in August; Noma raised a $100 million Series B last year. AIR's $50 million makes it well-capitalized for a six-month-old company and modestly capitalized for the category it just entered.

## What to watch

Three things. Whether the labs and platform vendors hosting skill and MCP directories ship native signing and provenance, which would collapse much of AIR's value proposition into the platform layer; Saban concedes this is coming but bets enterprises will still want a cross-vendor product. Whether the vetted marketplace gains traction, since a whitelist nobody uses is just a spreadsheet. And whether AIR converts its 20-odd customers into the "significant sales" Saban expects next year. He has already telegraphed the next step: "We have raised a lot of money and are using it and will raise more rounds."
