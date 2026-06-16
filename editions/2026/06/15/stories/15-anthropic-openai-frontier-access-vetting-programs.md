## Anthropic and OpenAI Are Becoming Gatekeepers of Who Gets the Most Powerful AI

For most of the cybersecurity industry's history, competitive advantage came from talent, data, and infrastructure. As of June 2026, it increasingly comes from something else: whether a private AI lab in San Francisco has decided you are trustworthy enough to use its most capable model.

That shift crystallized over a single week this month. On June 9, Anthropic released **Fable 5**, the first publicly available model in its new "Mythos class," positioned a tier above Claude Opus 4.8 — and shipped it with classifiers that quietly route high-risk cybersecurity and biology requests away from the frontier model and down to Opus. Three days later, on the evening of June 12, the company **disabled all public access** to both Fable 5 and the more powerful Mythos 5 worldwide, complying with a U.S. government export-control directive it received at 5:21 PM ET. The recall hit every customer on the planet — paying enterprises and Anthropic's own employees included — because, the company said, it could not filter foreign nationals from U.S. users in real time.

The episode is more than a compliance story. It is the clearest signal yet that the two leading American AI labs are constructing formal, permanent machinery to decide who may wield their most dangerous capabilities — and that governments now have a hand on the kill switch.

## Two labs, one strategy: selective access

Anthropic and OpenAI have converged on the same answer to an awkward problem: their frontier models are good enough at finding and exploiting software vulnerabilities to be genuinely dangerous, yet too commercially valuable to lock in a vault.

Their solution is **tiered, vetted access**. Anthropic's restricted Mythos-class capability runs through a controlled gateway called **Project Glasswing**, which on June 2 expanded to more than 150 additional organizations across over 15 countries — bringing the total past 200. The partner roster reads like a who's-who of the security and infrastructure establishment: Apple, Google, Microsoft, Nvidia, AWS, CrowdStrike, Palo Alto Networks, Okta, Samsung, the EU cybersecurity agency ENISA, and NATO. New entrants must meet security requirements before they get in. Anthropic says Glasswing partners have already surfaced more than 10,000 high- or critical-severity vulnerabilities.

OpenAI runs a parallel system. Its **Trusted Access for Cyber (TAC)** program, introduced in February and scaled up on April 14, vets thousands of individual defenders and hundreds of teams, then hands the highest tiers a cyber-permissive model, **GPT-5.4-Cyber**, fine-tuned with a lower refusal boundary for legitimate security work — including binary reverse engineering. Anthropic, for its part, is now building its own formal trusted-access program to govern Mythos 5 and future, less-restricted models, though it has set no timeline.

The dynamic is unmistakable. As Axios reporter Sam Sabin summarized it, "It's now up to the AI labs to decide who gets access to the cybersecurity industry's most cutting-edge capabilities." Behind the scenes, organizations have spent months lobbying Anthropic for a seat at the table.

## The line that keeps moving

The governance problem sits in the gap between "safe for general use" and "too capable for unrestricted access" — a line that moves every time capabilities jump.

Anthropic's own conservatism illustrates the dilemma. **Dianne Penn**, Anthropic's head of product management for research and labs, told Axios the company is being deliberately cautious at launch, "meaning some legitimate security work may also get routed away from Fable 5." In other words, the safeguards are tuned to over-block — defenders pay a tax so the labs can sleep at night.

OpenAI frames the same calculus as a matter of who, not what. "Cyber capabilities are inherently dual-use, so risk isn't defined by the model alone," the company wrote in its April access announcement. "We don't think it's practical or appropriate to centrally decide who gets to defend themselves." Its stated goal is to make tools "as widely available as possible while preventing misuse," leaning on identity verification and monitoring rather than blanket refusals.

But the June 12 recall exposed the limits of that posture. Anthropic pushed back hard on the government's reasoning, stating it disagreed "that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people," and warning that "if this standard was applied across the industry, we believe it would essentially halt all new model deployments for all frontier model providers." A safety-conscious lab built the gates; the state walked through them and shut the whole thing down anyway.

## What it means to be the gatekeeper

Three implications follow, and none of them are comfortable.

**Security.** Concentrating frontier cyber capability in a vetted few may keep "scary hacking capabilities only in the hands of the good guys," as Axios put it. But it also creates a stark have/have-not divide. The thing to watch, Sabin noted, is whether trusted-access users "begin finding vulnerabilities, conducting research and building products that organizations without access simply can't match." Defenders left outside the gate could fall structurally behind — while determined attackers, who never asked permission, route around the controls entirely.

**Competition.** When access to the best models becomes the differentiator, the labs become kingmakers in a market they also compete in. Anthropic and OpenAI get to decide which security vendors are equipped to win — even as both eye public markets and need to monetize these models. Selective access conveniently delivers both safety theater and a revenue stream. Smaller players, startups, and researchers in less-favored jurisdictions have little recourse and no appeals process beyond lobbying.

**Public accountability.** This is the deepest problem. Decisions about who may use civilization-scale cyber tools are being made inside private companies, by criteria that are largely opaque, with governments able to override them by fiat and no public process in between. There is no FOIA request for a Glasswing rejection, no published standard for what tips a model from "deployable" to "recalled." The vetting programs are governance — they are simply governance without democratic input.

## What to watch next

The immediate question is whether Fable 5 and Mythos 5 come back, and on what terms; Anthropic is contesting the directive, and the outcome will set precedent for how far Washington can reach into a commercial model's deployment. Watch, too, for the launch of Anthropic's formal trusted-access program and whether it adopts OpenAI's automated, KYC-style verification or something more discretionary.

The larger story is structural. As the next generation of models pushes capabilities higher, the "safe enough for everyone" line will keep retreating — and the population of people deemed trustworthy enough to cross it will be defined, audited, and revoked by a handful of private labs and the governments leaning over their shoulders. The era of open frontier access is closing. What replaces it is a permissioned internet of intelligence, and right now, the gatekeepers are writing their own rules.
