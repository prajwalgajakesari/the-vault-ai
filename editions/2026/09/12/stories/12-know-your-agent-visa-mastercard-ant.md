The press release crossed the wire on Wednesday, September 9. The stage appearance came the next day in São Paulo. And what Ant International, Mastercard and Visa announced there, stripped of the framing, was an agreement to keep talking: three rival agent-identity protocols will "explore ways to work toward common principles."

That is genuinely news. Visa's Trusted Agent Protocol, Mastercard's Verifiable Intent and Ant International's Agentic Mobile Protocol were built as competing answers to the same question — how does a merchant know the software at checkout is a legitimate agent acting for a real cardholder, and not a scraper wearing a browser costume. Getting three networks that touch most of the world's card and wallet volume to agree those answers should interoperate is not nothing.

It is also not a standard. There is no published technical specification, no named governance body, and no rollout timeline attached to the Know-Your-Agent framework. What exists is a shared direction of travel and three executives on the record.

## What the three actually agreed to

The substance, per the announcement, is narrower and more useful than "interoperability" suggests. The KYA collaboration centers on three things: making agents traceable across networks by linking each one to a validated operator, cardholder or organization with clear attribution; converging on shared certification requirements so an agent vetted once is recognized elsewhere; and running continuous monitoring on identity and transaction signals to keep that certification current rather than one-and-done.

Critically, each network keeps its own verification and decisioning. The framework is explicitly designed "based on shared principles while preserving each network's own verification and decisioning processes." That is the compromise that made the announcement possible, and it is also the seam where the whole thing could pull apart — shared signals, unshared judgment.

The stated payoff is developer friction. "If an agent registers with Ant, they don't need to register again with Visa, Mastercard," Ant International chief innovation officer Jiang-Ming Yang told CNBC.

The work is modeled on the Safeguards for Agentic Finance at Runtime framework and routed through BuildFin.ai, a platform convened by the Monetary Authority of Singapore. That regulator-convened venue is the closest thing to governance on offer — and it is Singapore's, not Brasília's or Washington's.

## Three protocols, three different starting lines

The parties are not arriving as equals. Visa's Trusted Agent Protocol launched in October 2025 with roughly a year of partner integrations behind it, including Adyen, Shopify and Stripe. Mastercard's Verifiable Intent is newer — March 2026 — but open-source and co-developed with Google. Ant International's Agentic Mobile Protocol shipped in April 2026 into a wallet ecosystem that, per the Worldpay Global Payments Report 2026, accounted for 56% of global e-commerce value in 2025.

"As AI agents become a bigger part of how people discover and buy, trust must scale with them," said Rubail Birwadker, Visa's global head of growth products and strategic partnerships. "Collaborations like this can help create more consistency, better accountability, and greater confidence across the payments ecosystem as AI-driven transactions become more common."

Mastercard chief digital officer Pablo Fourez was more specific about the failure mode being addressed: interoperability across KYA frameworks gives "merchants, platforms, wallets and issuers a consistent way to recognise trusted agents, verify that actions reflect the user's intent, and preserve accountability across the transaction."

Note who is not in the room. OpenAI and Stripe's Agentic Commerce Protocol, Google's AP2, Coinbase's x402 and American Express all sit outside this particular table. A three-way alignment among card networks and one wallet giant is a bloc, not a standard body.

## Nobody said who pays

Here is the gap the announcement does not touch. Identity answers *who* the agent is. It does not answer what happens when a correctly identified, properly certified agent buys the wrong thing.

Under current arrangements, the merchant generally eats it. The merchant stays the merchant of record, and the usual evidence that wins a representment — device fingerprint, IP address, navigation path — now describes a data center rather than a human. A shared KYA credential arguably makes this worse before better: it hands merchants a stronger signal that the transaction was legitimate at exactly the moment the cardholder is arguing it was not what they meant.

American Express, absent from the KYA group, is the one network that has put money against this. On April 14, 2026 it launched its Agentic Commerce Experiences developer kit alongside Amex Agent Purchase Protection, covering eligible charges arising from a registered agent's error. That is a liability position. What Visa, Mastercard and Ant announced is an identity position. The second is much cheaper to promise.

## The number that hasn't moved

McKinsey's projection that agents will orchestrate $3 trillion to $5 trillion of consumer commerce by 2030 is doing heavy lifting in every version of this story. Set against it: only 14% of consumers say they trust AI to complete a purchase without verification, per the Product.ai Trust in AI Commerce Report from April 2026, and 42% will not let an agent spend more than $25 unsupervised.

Visa has reported a 4,700% surge in AI-driven traffic to US retail sites. Almost all of it is browsing. That gap is a consumer-consent problem, and a certification registry does not close it — which is presumably part of why Visa spent $2.4 billion on behavioral-biometrics firm BioCatch in August 2026.

## What to watch

Three markers separate a standard from a press release. First, a published specification with version numbers and a conformance test — the thing that turns "shared principles" into something a developer can build against. Second, a named governance body with a membership policy, which determines whether the framework stays open or hardens into a gate favoring incumbents. Third, and most telling, any change to network dispute rules that assigns agent-error liability somewhere other than the merchant.

Until the third one lands, merchants are being asked to accept a new identity credential without a corresponding change in who absorbs the loss. Identifying the bot was always going to be the easy part.
