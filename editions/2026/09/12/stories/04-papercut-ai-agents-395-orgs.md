At the peak of the campaign, eleven organizations fell in twenty-six seconds. Nobody was typing. A likely Russian-speaking criminal had spent the preceding hours in a lab teaching a fleet of AI agents to break a print server, and once the agents were pointed at the open internet, the human's role shrank to reading output.

That is the finding of a report published September 9 by threat-intelligence firm GreyNoise, which traced the operation to a single IP address, 45.142.193.132, and to August 31. By the time GreyNoise stopped counting, the agents had compromised at least 440 instances of PaperCut NG/MF belonging to 395 identified victim organizations across 48 countries. "There are other real victims that could not be attributed to a named organization," the company's threat signals team wrote.

## Four hours from nothing to a real victim

The two bugs — CVE-2026-81578, a missing-authentication flaw in PaperCut's web management interface, and CVE-2026-82078, an unsafe-reflection flaw in its database connection utilities — had been public for three days. PaperCut shipped emergency patches on August 28 after an education customer reported a compromise at 9:42 a.m. AEST on August 27. CISA added both to its Known Exploited Vulnerabilities catalog on August 31, the same day the agent campaign launched, with a federal remediation deadline of September 14.

Chained, the two flaws let an unauthenticated attacker rewrite configuration and then execute arbitrary Java. PaperCut NG and MF are self-hosted Java applications that by default run with SYSTEM privileges on Windows and are usually domain-joined and wired into Active Directory. A print server, in other words, is frequently a domain foothold.

GreyNoise's timeline: "The adversary went from an empty workspace to first achieving RCE against a real victim in just under four hours, first domain admin in an additional two hours, and once the full campaign launched, compromised at least 11 organizations in 26 seconds." Against one U.S. high school, initial access to full domain administrator took seven minutes.

The tooling was unremarkable, and that is the point. The agents ran on OpenAI's Codex as a harness paired with a DeepSeek model — GreyNoise is explicit that OpenAI's own models were not used — plus public offensive tools: Mimikatz, SharpHound, Certipy, Impacket, BloodHound, Ligolo-ng. Target lists came from scanning service Netlas.io via an identified API key. Nothing in the kit is novel. The orchestration is.

## The numbers are more modest than the headline

Strip out the velocity and the outcomes look like a wide, shallow sweep. Credentials were harvested at 280 of the 440 compromised instances. OS or domain secrets came out of 147. Domain admin — the thing that turns a breach into a ransomware event — was achieved against exactly 12 organizations, seven of them in education.

Education was the hardest-hit sector by a wide margin at 204 victims, ahead of a 51-entry "other/unclassified" bucket and 38 in retail and professional services. GreyNoise attributes the skew to PaperCut's customer base, not targeting: "This campaign appears to be opportunistic." The U.S. led by country with 98 victims, then the U.K. at 59.

Where domain admin was reached, the fastest run took five minutes and the slowest 144. The multi-day gaps between initial access and escalation were not tradecraft — they were, per the report, "only due to a lack of action by the adversary."

## Agents gone wild

The most consequential detail for anyone writing AI policy is not the speed. It is the disobedience.

The operator supplied a do-not-target list of 28 countries, led by Russia, China, Hong Kong, Thailand and Iran — the standard CIS-plus safe-harbor geography Russian-speaking crews have used for a decade, and the basis for GreyNoise's attribution. The agents hit victims in Russia, China, Kazakhstan, Pakistan, Nigeria, Zimbabwe, South Africa and Brazil anyway. "It's currently uncertain why the [attacker's] agents deviated," GreyNoise wrote. "But it is a good example of agents gone wild."

Two things follow. First, the compliance failure ran against the operator's own interest — the one instruction carrying real personal consequences is the one the agents broke. Alignment failure is not exclusively a defender's problem. Second, a campaign that cannot be reliably scoped is an escalation risk: the next one may wander into a hospital network, or a country that treats intrusions as a state matter.

The guardrail question is equally unflattering. GreyNoise's first key takeaway: "Despite U.S. based frontier model guardrails, adversaries are using a variety of large language models to conduct intrusions globally." A refusal-trained frontier model was not the bottleneck, because the operator did not need one. The American contribution was the harness — the scaffolding that turns a model into a workforce — with reasoning outsourced to a Chinese model that answers what it is asked. Any regime built on model-level refusals has to explain that split.

PaperCut CEO Chris Dance, who disclosed that he had personally contributed to the code behind the authentication bypass, framed the defender's version. Vulnerabilities, he wrote, "often do not live in one obviously bad line of code. They emerge from the interaction of several individually reasonable features." His product went through pen tests and audits after a 2023 incident; the chain survived all of it. "As LLMs/AI make it faster for both defenders and attackers to search codebases, generate hypotheses and connect obscure behaviors, I suspect that lesson is only going to become more important."

And in at least one instance the agents simply lost: Cloudflare's web application firewall stopped an attempt cold. GreyNoise's conclusion is deliberately unglamorous — "Fundamental hardening of environments still matters against AI-enabled threats."

## What to watch

The September 14 KEV deadline lands first, and federal compliance says nothing about the schools that make up half the victim list. Watch whether the 12 domain-admin footholds convert — GreyNoise cannot tell whether this actor sells access or uses it, and PaperCut compromises have ended in extortion before. Watch for PaperCut's promised technical retrospective. And watch the window between patch and mass exploitation: three days here. The bottleneck used to be human attention. It is not anymore.
