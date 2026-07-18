Shai Morag told his wife he was going to retire. That was after Tenable bought his cloud identity startup Ermetic for $265 million in 2023, after he stayed on as the acquirer's chief product officer, and after CEO Amit Yoran — the man who bought his company — fell ill and died in January 2025. Morag left. The retirement lasted about as long as it takes to notice an unsolved problem.

On Wednesday, Oak — the Israeli company he founded in December 2025 with Tal Marom — emerged from stealth with $60 million in seed funding and a product already generally available at enterprise customers. The round was co-led by Accel, Greylock Partners, and CRV, with Hetz Ventures, AlphaDrive Ventures, and strategic angels participating. It is among the largest seeds ever raised by an Israeli cyber company, and it wasn't raised on a slide deck: Calcalist reported the money back in November 2025, revealing it arrived in two tranches — an initial $20 million round Greylock joined, then a $40 million round that brought in Accel and CRV.

Oak calls what it is building an "Identity Operating System": a single control plane governing every identity — human, machine, or AI agent — replacing the fragmented stack most enterprises have accreted over two decades. The pitch is that identity is broken in a way no additional tooling will fix, and that AI agents are the forcing function.

"The market has reached a breaking point," Morag said. "I've built several companies in this space, so I understand why identity has stayed broken for so long. The tools were never built to work as one, and adding more of them was never going to fix it. Oak is the platform the industry has needed for twenty years, and could never build until now."

## The actual problem

The numbers behind the pitch are striking. CyberArk's 2025 Identity Security Landscape, a Vanson Bourne survey of 2,600 security decision-makers, found there are **82 machine identities for every human** in organizations worldwide — a ratio already absurd before agents entered the picture. More damning is the governance mismatch: 88% of respondents said "privileged user" applies solely to human identities, while 42% of machine identities actually hold privileged or sensitive access. Enterprises built their access-control apparatus around a population that is now a rounding error in their own environments.

This is the assumption AI agents break. Human identity rests on implicit rhythms: a person is hired, provisioned, works from roughly one location, gets reviewed quarterly, and is deprovisioned when they leave. An agent has none of those properties. It authenticates as a machine, spawns credentials at software speed, may live ninety seconds or ninety days, and inherits permissions from whatever instantiated it. A quarterly access review is meaningless against something whose entire lifecycle fits between two reviews.

Oak's answer is an AI connector framework that reaches into any application — cloud, on-prem, SaaS, or homegrown — building a live identity graph from raw evidence rather than static records, with new connectors in hours rather than months. Critically, it maps the access each identity *holds* against what it actually *uses*, stripping permissions in real time rather than at review time. Marom, who led product teams at Tenable and Salesforce, says the founders interviewed more than 100 CISOs and IAM leaders before writing the product.

"They all share the same problems of running too many disconnected tools, being unable to see how access is used, and no way to govern AI agents," Marom said. "Just as CNAPP consolidated the fragmented cloud security stack, identity is now at that same inflection point." The analogy is not casual: CNAPP is the exact category Morag sold into last time.

## A $60M seed prices in a lot

Oak has roughly 50 employees across Israel and San Francisco, "dozens of customers" by Morag's own account, and no disclosed valuation. A $60 million seed against that prices in a category that doesn't clearly exist yet as a standalone market.

The bear case: agent identity is a feature, not a company. Okta, Microsoft Entra, and CyberArk have the distribution, contracts, and switching costs to bolt agent governance onto what enterprises already run. Vendor lock-in here runs unusually deep — Morag and Accel's Andrei Brasoveanu both concede this, which is why they argue Oak must scale fast. And consolidation is underway: Palo Alto Networks has agreed to acquire CyberArk, making the incumbent stack broader, not narrower.

The bull case: "bolting AI onto outdated platforms," as Oak's release puts it, produces exactly the fragmentation CISOs complain about, and the winner will be whoever rebuilds the substrate. Gartner projects 70% of CISOs will adopt identity visibility and intelligence capabilities by 2028 — a budget line that lands somewhere.

Accel is betting on the operator more than the thesis. "Backing Shai a second time was one of the easiest decisions we've ever made," said Brasoveanu, whose firm led Ermetic's Series A pre-revenue and gave Morag a standing offer to fund whatever came next. "He and his team have spent their careers solving the hardest problems in enterprise security, and identity is the biggest one left standing."

Morag has been here three times — Integrity-Project to Mellanox in 2014, Secdo to Palo Alto Networks in 2018, Ermetic to Tenable in 2023, roughly $500 million combined. This one is meant to be different. "Our vision is to be born as a giant," he told TechCrunch. He has told his wife it is his last: "I will go big or go home."

## What to watch

Three things. First, whether Oak names customers — "dozens" and "enterprise clients" is where every stealth exit starts, and the logos are the tell. Second, Black Hat USA in August, where Oak showcases the platform at booth 4203 and faces its first real technical scrutiny. Third, the incumbents: if Okta and Microsoft ship credible agent-identity governance inside twelve months, Oak's window narrows to whatever it lands before the default becomes good enough. Morag says he'll keep raising regardless. Having priced the seed like a Series B, he may have to.
