# FIRST Projects 66,000 CVEs in 2026 as AI Discovery Outpaces Human Patching

The machines have started hunting for software flaws on their own, and the numbers are now too large for human defenders to ignore. On June 15, the Forum of Incident Response and Security Teams (FIRST) raised its 2026 vulnerability forecast to roughly 66,000 CVEs for the year, up from a February median of 59,427 and more than double the historical annual average of 25,000 to 30,000. It would be the first time in history that annual vulnerability disclosures approach 70,000 — and FIRST attributes the surge largely to AI-assisted discovery tools that scan codebases and firmware at superhuman speed.

The mid-year update, released at FIRST's 38th Annual Conference, found that actual CVE disclosures are already running 46.3% above the projection FIRST published just four months earlier. The organization names three structural drivers: AI-assisted vulnerability discovery, a 449% year-over-year jump in GitHub Security Advisory volume, and a 3,119% increase in activity from VulnCheck acting as a CVE numbering authority of last resort, absorbing a backlog of previously unassigned flaws.

## The Asymmetry at the Heart of the Crisis

The core policy problem is not that software is suddenly more broken. FIRST is explicit that the surge reflects more aggressive research and better reporting, not a collapse in code quality. The problem is asymmetry: AI can find vulnerabilities far faster than humans — or even AI-assisted teams — can triage, prioritize, and patch them. Discovery has been industrialized; remediation has not.

A vivid illustration sits inside Anthropic's Project Glasswing, the program built around its Claude Mythos Preview model. Anthropic reports scanning more than 1,000 open-source projects and identifying 23,019 issues, of which 6,202 were rated high or critical severity. The company and six independent security research firms assessed 1,752 of those high- and critical-severity findings, and more than 90% were validated as true positives — a confirmation rate that suggests these are not noisy false alarms a maintainer can safely dismiss. Anthropic says Mythos has surfaced high-severity flaws in every major operating system and web browser. (These figures are as reported by Anthropic and its named research partners; independent line-by-line verification of the full corpus is not public.)

If a single model can generate tens of thousands of credible findings across a slice of the open-source ecosystem in roughly a month, the binding constraint on security is no longer detection. It is the finite supply of human maintainers — many of them unpaid volunteers — who must read, reproduce, and fix each report before an attacker weaponizes it.

## The Counterintuitive Data Point Policymakers Should Read Carefully

FIRST's own analysis complicates the panic narrative in a way that matters for governance. When the organization filters the raw surge for genuine exploitability — vulnerabilities listed in CISA's Known Exploited Vulnerabilities catalog, or carrying an EPSS exploit-probability score above 10% — the actionable patching burden, it says, remains essentially flat. In other words, the flood is real, but the share that demands urgent action has not exploded in proportion.

That distinction is the whole policy argument. A world that treats all 66,000 CVEs as equally urgent will drown its defenders in low-value work and burn out maintainers. A world that builds disciplined prioritization — reputation-weighted triage, exploit-prediction scoring, and shared signals about what is actually being attacked — can absorb the volume. The risk is that organizations without that maturity react to the headline number rather than the exploitable subset.

The same logic cuts both ways on AI itself. "The same capabilities driving the CVE surge can also find and fix vulnerabilities faster," FIRST notes, pointing to compressed mean-time-to-remediate. Anthropic frames Glasswing as defensive, lining up launch partners including AWS, Apple, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, and NVIDIA to harden shared infrastructure. But the access question is unresolved: if frontier discovery models are a decisive defensive advantage, who gets them, and on what terms? A capability that finds flaws in every browser is, in the wrong hands, a map of the world's attack surface.

## What FIRST Is Actually Recommending

FIRST's prescription is coordination over heroics. "No organization can solve this all alone, which is precisely why FIRST exists," CEO Chris Gibson said. "The teams that will weather the vulnerability storm of 2026 are the ones with trusted networks already in place, who are sharing intelligence and are coordinating response before any crises hit."

That reframes the story from a technology problem into a governance one. Disclosure norms built for a human-paced world — a few thousand CVEs a year, triaged by hand — were not designed for autonomous tools that can file thousands of valid reports in weeks. Coordinated disclosure timelines, maintainer capacity, and the EPSS/KEV prioritization stack all become load-bearing infrastructure rather than nice-to-haves.

## What to Watch

Three things will signal where this goes. First, whether the "actionable burden remains flat" finding holds through the back half of 2026, or whether AI discovery starts surfacing genuinely exploitable, previously unknown flaws at scale rather than reconfirming known patterns. Second, whether regulators move — CISA has already floated tighter critical-patch mandates — and whether those mandates account for exploitability rather than raw count. Third, the access debate: whether frontier vulnerability-discovery models remain concentrated among a handful of vendors and their partners, or whether defenders broadly gain comparable tooling. If discovery stays asymmetric and remediation stays human, 66,000 may read, in hindsight, as the low estimate.
