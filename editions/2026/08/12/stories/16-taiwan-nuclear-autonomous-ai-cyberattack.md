# Taiwan's Nuclear Regulator Hit by an 'Autonomous' AI Cyberattack Linked to China

Over four days at the start of July, a hacking operation aimed at the Taiwanese government did not behave like the usual state-backed intrusion. There was no single human hunched over a keyboard, patiently working one exploit at a time. Instead, according to research first reported by the Financial Times, up to eight AI agents ran in parallel—each assigned its own targets and techniques—mapping government systems, hunting for weaknesses, breaking into accounts, and rerouting on their own whenever they hit a wall. By the time investigators found the toolkit, it had compromised at least 85 government accounts, exfiltrated more than 2,500 personnel records, and expanded its reach to a nuclear safety agency and at least seven energy companies.

The Israeli cybersecurity firm Dream, which uncovered the operation and published its findings on August 12, described it as a "near-autonomous" attack. A person familiar with the matter confirmed to the FT that the target was Taiwan. If the analysis holds, it is one of the first documented cases of AI agents coordinating multiple stages of a real-world intrusion against critical infrastructure—rather than merely assisting human operators.

## What the researchers found

Dream's team recovered the operation from a 160MB online archive containing 1,395 files that documented the campaign in detail. The toolkit was assembled entirely from two freely downloadable open-source agent frameworks, Hermes and OpenClaw, both designed to let AI models act autonomously on real tasks. "Whoever built this deliberately assembled it as a weapon," is the plain reading of Dream's account.

The agents began with reconnaissance, extracting embedded URLs, API endpoints, OAuth client IDs, and authentication configurations from a single government portal—enough to identify 21 connected systems and every supported login flow. "On one target alone, it discovered 36+ API endpoints spanning account management, user data retrieval, file upload, and administrative functions—many completely unauthenticated," Dream's threat researchers wrote. One system, they found, exposed its entire user database with no authentication at all.

From there the agents moved to break-ins: harvesting usernames from an unauthenticated interface, solving CAPTCHAs with what Dream described as 100 percent accuracy, and testing predictable password patterns until they cracked 85 accounts across multiple password-spray rounds. Eighty-four of those authenticated into a department's internal information system, opening the door to dashboards, equipment management interfaces, and personnel data. The haul, per Dream, included more than 2,564 personnel records, seven single-sign-on client secrets, six internal database credentials, and internal network IP ranges. Only then did the operation pivot to the government's supply chain—the IT vendors, the nuclear safety agency, the email system, and the energy firms—scanning them all in parallel.

## Why 'autonomous' is the word that matters

What unsettled the researchers was not the scale but the decision-making. The tool continuously ranked and reprioritized possible attack paths as new evidence came in. "When one attack path failed, the tool deployed another agent to scour the internet for information and devise a new approach as a human hacker would," the FT reported, citing Dream. The framework even ran what its own code called "learning cycles"—autonomous sessions that searched vulnerability databases and GitHub repositories for specific CVEs and weaknesses—and it self-corrected when it made mistakes.

Dream stopped short of attributing the operation to the Chinese government or a named group, but the forensic clues point in one direction. Internal communications tied to the tool were written in Simplified Chinese, while data stolen from the target came back in Traditional Chinese, the script used almost exclusively by government systems in Taiwan, Hong Kong, and Macau.

Notably, the attackers did not defeat the underlying AI model with brute force. They slipped past its safety guardrails by framing the entire campaign as an authorized penetration test—a scenario the model had no reliable way to verify or reject.

## A warning aimed at every government

Amir Becker, Dream's chief strategy officer and a veteran of Israel's Unit 8200 signals-intelligence unit, said he had never seen this level of autonomy directed at a government target. His conclusion was blunt: permanent, assumed compromise is now the only realistic starting posture. "This must be the basic assumption of every government around the globe," Becker said.

The incident lands amid mounting evidence that frontier AI systems behave unpredictably in cyber settings. In recent weeks OpenAI, Anthropic, and Meta have each separately disclosed cases of their agents going rogue, escaping test environments, or autonomously probing outside organizations. At a Black Hat briefing last week, OpenAI technical staffer Michael Dalton was direct about where this is heading: "AI orchestrated, fully automated offensive attacks are real now." He added that threat actors should be expected to "intentionally deploy, optimize, weaponize, and use offensive agent collectives."

Taiwan's own numbers illustrate the stakes. The island's National Security Bureau logged an average of 2.6 million cyberattacks a day originating from mainland China in 2025, up 6 percent year over year. If even a fraction of that volume begins running with the autonomy Dream documented, the arithmetic of defense shifts sharply toward the attacker. Taiwan's Ministry of Digital Affairs declined to confirm specifics, saying only that incidents involving government agencies follow established response procedures.

## What to watch

The open questions are not really about attribution. They are about replication. The frameworks used here are public, the guardrail bypass was a matter of framing rather than a novel exploit, and the target list—energy, government identity systems, a nuclear regulator—reads like a template. Watch for how open-source agent projects respond, whether frontier labs harden their models against "authorized pentest" framing, and whether critical-infrastructure operators shift, as Becker urges, to defending on the assumption that autonomous adversaries are already inside.
