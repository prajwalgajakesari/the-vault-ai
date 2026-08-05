# Crogl Releases a Free Autonomous 'AI SOC Agent' for Security Teams

Most security software takes months to buy and weeks to install. Crogl wants to be running in your environment before lunch. On July 30, 2026, the Albuquerque-based startup made its Enterprise AI SOC Agent — an autonomous software "analyst" that investigates security alerts on its own — available as a free download, betting that the fastest way to win over skeptical practitioners is to hand them the product with no contract, no procurement cycle, and no per-token meter running in the background.

The move lands squarely in the middle of 2026's defining enterprise-software story: the migration of AI from chat assistants to production-grade agents that take action inside critical systems. In the security operations center (SOC), where analysts drown in alerts and burn out fast, that shift has arrived faster than almost anywhere else.

## What the agent actually does

Crogl describes its product as "an autonomous AI SOC agent that investigates alerts, hunts threats, documents every investigative step, and generates complete investigation reports." In practice, that means the agent connects to the tools a security team already runs — a SIEM, threat-intelligence feeds, endpoint tooling — and works through the queue of alerts a human analyst would otherwise triage by hand, writing up its reasoning as it goes.

The company leans hard on a "sovereign by design" pitch. Crogl runs inside the customer's own environment — on-premises, in their cloud, or in fully air-gapped deployments — and, per the company, customer data never leaves that environment. It also claims to plug into an existing stack without "schema normalization, proprietary data pipelines, or changes to existing workflows," while keeping "analysts in control of every decision." Pricing, when customers move past the free tier, is a flat fee with unlimited investigations rather than the consumption-based, per-token billing common to AI tooling — "no per-token metering and no consumption surprises," the company says.

The free version is aimed at the moments when friction hurts most: an active breach, a newly disclosed vulnerability, or an internal investigation where a team can't afford a multi-week evaluation. Crogl's framing is blunt about the target: "Crogl is not for everyone. It is built for enterprises that want AI to work with their existing tools, on their own data, and under their control."

## The people and the money

Crogl was founded in 2023 by a trio with deep security-engineering pedigrees: CEO Monzy Merza and CTO David Dorsey, both veterans of work spanning Sandia National Laboratories, Splunk, and Databricks, along with Chief Engineer Bradford Lovering, a former Splunk chief architect and Microsoft Technical Fellow. The company emerged from stealth in March 2025 announcing $30 million in total funding — a $25 million Series A led by Menlo Ventures on top of a $5 million seed round led by Tola Capital — around what it then called a "knowledge engine" for security teams.

The urgency behind the product shows up in the company's own research. In a report released earlier in 2026, Crogl found that enterprises investigate just 37% of their daily security alerts — meaning nearly two-thirds of the warnings a SOC generates never get a proper look. That gap is the entire premise of the agentic-SOC category: there are far more alerts than there are analysts, and the shortfall is structural, not something more hiring can fix.

## Why practitioners, not marketing

Merza's launch messaging reads as a shot at the crowded field of AI-security vendors making outsized autonomy claims. "The debate around AI for security operations shouldn't be settled by marketing. It should be settled by practitioners," Merza said. "The future of AI for security operations belongs to organizations that maintain control of their data and deployments, extend the security investments they've already made, and can scale AI with predictable economics."

The company put an early tester's account front and center to make the point. "I had Crogl installed and connected to my SIEM and VirusTotal in under 10 minutes, on my own," said Rick Rice, a principal instructor at Splunk. "I asked it to summarize alerts and got accurate, detailed answers back immediately. When I asked for a VirusTotal report on the most common malicious file hash in my environment, it returned the report and guidance on how to contain it. Most things I test don't get that far in the first sitting. No marketing demo. No hand-holding. Just my environment. My data."

## The agentic SOC goes mainstream

Crogl is not operating in a vacuum. The agentic SOC has become one of the hottest corners of cybersecurity, with well-funded rivals such as Dropzone AI, Prophet Security, Simbian, and Torq — plus platform incumbents like Microsoft, CrowdStrike, and Palo Alto Networks — racing to ship autonomous or semi-autonomous investigation agents. The common thesis is the same everywhere: Tier-1 triage, the repetitive first-pass analysis that consumes most of an analyst's day, is a job that large language models can increasingly do at machine speed and around the clock.

What differentiates Crogl's launch is the go-to-market, not just the technology. Free, self-serve downloads are unusual for enterprise security software, where sales still typically run through lengthy proofs-of-concept and six-figure contracts. By removing procurement friction, Crogl is betting on product-led growth — the SaaS playbook of letting the tool sell itself inside the organization before a purchasing conversation ever happens. It is also a distribution strategy: get the agent installed during the chaos of an active incident, when a team has neither the time nor the patience to evaluate vendors, and prove value when it matters most. The company is amplifying all of it with a heavy presence at Black Hat USA 2026, including partner sessions with AWS, Cribl, Palo Alto Networks, Splunk, ReversingLabs, and ZeroFox, and a Merza appearance at the show's AI Summit on August 4.

## What to watch

The open questions are the ones that dog every autonomous security agent. How much does the "agent" genuinely investigate versus summarize, and how does its accuracy hold up on messy, real-world alert data rather than a curated demo? How much human oversight does "analysts in control of every decision" actually require day to day? And can a free-download motion convert into paying enterprise customers at the scale a venture-backed company needs?

For security leaders, though, the calculus is simpler than the hype. If an agent can meaningfully close the gap between the 37% of alerts that get investigated and the rest that don't, the price of trying it — now zero — is hard to argue with. The harder question, as always in security, is what happens the first time the machine gets one wrong.

## Sources

- [Crogl Announces Its Sovereign AI SOC Agent Is Available as a Free Download (PR Newswire)](https://www.prnewswire.com/news-releases/crogl-announces-its-sovereign-ai-soc-agent-is-available-as-a-free-download-302838557.html)
- [Founded by Cybersecurity Researchers and Practitioners, Crogl Launches With Its Breakthrough Knowledge Engine and Announces $25 Million Series A (GlobeNewswire)](https://www.globenewswire.com/news-release/2025/03/06/3038257/0/en/Founded-by-Cybersecurity-Researchers-and-Practitioners-Crogl-Launches-With-Its-Breakthrough-Knowledge-Engine-to-Combat-Cyber-Risk-and-Announces-25-Million-in-Series-A-Funding-Led-b.html)
- [Crogl Offers Free AI SOC Tool as MSSPs Face Rising Alert Pressure (MSSP Alert)](https://www.msspalert.com/news/crogl-offers-mssps-a-free-version-of-its-agentic-ai-powered-security-platform)
