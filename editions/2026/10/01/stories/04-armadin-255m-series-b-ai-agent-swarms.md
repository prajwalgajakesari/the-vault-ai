Kevin Mandia spent two decades cleaning up after the world's worst breaches. His new company is now worth more than $2.5 billion for doing the breaking itself. Armadin, the AI-native offensive security startup Mandia founded last year, said on October 1 that it has raised $255.5 million in a Series B round co-led by Andreessen Horowitz and Accel. Its product sends swarms of autonomous, attacker-like AI agents into corporate and government networks to find the routes a real adversary would take.

The round brings Armadin's total funding to $445 million. It comes just seven months after the Palo Alto company formally launched in March with $189.9 million, and less than a year after a quiet $24 million seed in late 2025.

## The Round

Accel, which led Armadin's Series A, returned to co-lead with a16z. Bain Capital Ventures and Redpoint joined as new investors. Existing backers 8VC, Ballistic Ventures, GV, In-Q-Tel, Kleiner Perkins and Menlo Ventures all participated again. The cap table carries some symmetry: Google bought Mandia's previous company, Mandiant, for $5.4 billion in 2022, and Google's venture arm is now backing his next one. Mandia also co-founded Ballistic Ventures, the cybersecurity fund that took part in the round. In-Q-Tel, the CIA-linked strategic investor, fits Armadin's push into the public sector.

Armadin says it will use the money to scale its agentic security platform and to expand research, model training and go-to-market work. Mandia is CEO. His co-founders are CTO Travis Lanham, chief offensive security officer Evan Peña and chief architect David Slater.

"Offense is uniquely advantaged right now," Mandia said in the funding announcement. "AI lets an attacker find and chain weaknesses faster than any human team can respond. The only way to build a defense that keeps pace is to train it against the best offense available, every day. That is what we built."

## How the Swarm Works

Armadin's pitch is aimed at two staples of corporate security: the penetration test, which happens once or twice a year, and the vulnerability scanner, which scores each finding on its own. The company argues that neither holds up now that frontier models have shortened the gap between a vulnerability's disclosure and a working exploit.

Armadin instead runs a swarm of specialized agents that behave like a skilled attacker. In the first phase of an assessment, the swarm maps an organization's internal systems and users. It then probes those assets for weaknesses and links individually low-severity issues into validated "kill chains." A chain might start with unauthenticated remote code execution at the network edge, move laterally, and end in a full cloud compromise. Customers see each path along with its potential blast radius, and the platform produces prioritized remediation advice so teams fix the most dangerous items first.

The company's biggest public demonstration came in August, in a three-day live exercise run with agentic security operations provider TENEX.ai. According to SecurityWeek, Armadin launched 1,300 attacks involving 26,000 agents and about 17 million offensive actions against more than 25,000 services. The exercise produced 238 security findings, 98 of them rated significant, which the agents chained into 38 validated attack paths. Armadin calls it the largest autonomous AI attack on record. The agents worked without privileged credentials, source code access or allow-listing of security controls. The company says every action passed through a control layer supervised by a safety model trained on feedback from human security experts.

Armadin says it is already running these campaigns in production for Fortune 500 companies and government customers.

The investors say the timing is the point. "Against agentic adversaries, the best defense is a great offense powered by AI," said Ping Li, a partner at Accel. Andreessen Horowitz general partner David George went further: "We invested because we believe Armadin will become the defining security company of the AI era."

## Why It Matters

Armadin is a bet that AI has changed the economics of attack faster than defenders have adjusted. Agent swarms are fast because they parallelize. A hundred agents can run a hundred scans at once, and a finding from one agent can be shared across the swarm right away. SiliconANGLE noted that swarms of this kind have been behind several high-profile real-world breaches in recent months. Defenders working to quarterly test schedules are badly outpaced.

That changes what security teams buy. The valuable output is no longer a long list of CVEs ranked by severity. It is a short list of exploitable paths, ordered by how much damage each could cause. If Armadin's numbers hold up across customers, 17 million actions reduced to 38 paths that matter is the kind of signal-to-noise ratio that justifies a $2.5 billion valuation for a company less than a year old.

It also says something about investor appetite. A $255.5 million Series B seven months after launch puts Armadin among the most aggressively funded security startups of the year, next to large 2026 rounds for companies such as Cyera and Island. Mandia's track record is part of that. He sold Mandiant to FireEye for $1 billion in 2014 before Google's $5.4 billion deal, and he is one of the few founders in the field with two successful outcomes behind him.

There is an obvious tension too. A platform built to act like a world-class attacker, running tens of thousands of agents inside production environments, is a powerful tool to hand anyone. Armadin's safety-model control layer and sandboxing will be examined as closely as its detection rates.

## What to Watch

The next tests are whether Armadin can turn Fortune 500 pilots into continuous, platform-wide contracts, and how quickly incumbents such as Google's own Mandiant unit, CrowdStrike and Palo Alto Networks build or buy competing agentic red-team products. Also watch for independent validation of Armadin's exercise results, for its traction with federal agencies given In-Q-Tel's involvement, and for any regulatory response to autonomous offensive agents operating inside critical infrastructure.
