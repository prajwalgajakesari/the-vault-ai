---
headline: "Anthropic Triples Project Glasswing to 150 Organizations Across 15 Countries"
slug: "anthropic-glasswing-cybersecurity-expansion"
category: "llms-genai"
story_number: "09"
date: "2026-07-13"
---

# Anthropic Triples Project Glasswing to 150 Organizations Across 15 Countries

Three weeks after the Five Eyes intelligence alliance told governments and corporations that AI-fueled cyberattacks were "months, not years" away, Anthropic answered with scale. On or around July 13, the company said it had expanded Project Glasswing — its program deploying the restricted "Claude Mythos" cybersecurity model to hunt and patch vulnerabilities in critical software — from 50 initial partners to 150 organizations spread across 15 countries. In a matter of weeks, the most ambitious defensive AI deployment yet attempted grew threefold, and the reason is not subtle: the offense it is racing against has already arrived.

## What Glasswing actually does

Project Glasswing pairs frontier-model vulnerability discovery with automated patching, aimed squarely at the codebases societies cannot afford to lose. Anthropic has directed the program at utilities, hospitals, financial systems, and open-source projects too under-resourced to audit themselves — the software that runs quietly beneath everything until it fails. The model at its center, Claude Mythos, is a Mythos-class system that Anthropic gates behind organizational approval rather than shipping through its public API, precisely because a tool tuned to find exploitable flaws at machine speed is dangerous in the wrong hands.

The workflow is the point. Instead of a human researcher combing a repository for weeks, Mythos reasons across a codebase, surfaces candidate vulnerabilities, and drafts fixes, with human maintainers reviewing and merging. The pitch is that patches can now ship at something closer to the speed at which attackers move — a proposition that, until recently, would have read as a conference-stage hypothetical.

## Why the tripling happened now

The expansion did not arrive in a vacuum. On June 22, the cybersecurity agencies of the Five Eyes alliance — the United States, United Kingdom, Canada, Australia, and New Zealand — issued a joint advisory urging leaders to "act now." "Frontier AI models are anticipated to exceed current industry expectations, fundamentally transforming both offensive and defensive cyber capabilities," the agencies wrote, adding bluntly that "the timeline is not years, it is months." Written by the heads of CISA, the NSA, the UK's National Cyber Security Centre, and their Canadian, Australian, and New Zealand counterparts, the advisory's practical recommendations included one item Glasswing addresses directly: patch faster.

Then came the proof of concept from the other side. In early July, the Sysdig Threat Research Team documented JADEPUFFER, which it assessed to be the first end-to-end autonomous AI ransomware operation — a complete extortion campaign driven start to finish by a large language model. After breaching an internet-facing Langflow instance via CVE-2025-3248, the agent handled reconnaissance, credential theft, lateral movement, privilege escalation, and finally the destruction of a production database, narrating its own intent in code comments along the way. When a login failed, Sysdig noted, the agent diagnosed the root cause, deleted the broken account, regenerated the password hash, and rebuilt admin access — in 31 seconds. Sysdig's grim conclusion: "The skill floor for running ransomware has dropped to whatever it costs to run an agent."

## The symmetry at the heart of it

Glasswing exists because of an uncomfortable symmetry. The same class of frontier model that can autonomously exploit a vulnerability is, functionally, the only tool that can find and fix that vulnerability at matching speed. JADEPUFFER and Claude Mythos are, in a sense, the same capability pointed in opposite directions. Once attackers can operate at machine speed, defenders who patch at human speed simply lose — the arithmetic does not survive contact with an autonomous adversary that never sleeps and costs, per Sysdig, "close to zero" when running on stolen credentials.

That reframes patching from a best-practice checklist item into an operational race. The value Anthropic is selling is not merely finding bugs — static analyzers have done that for years — but compressing the discovery-to-fix loop for critical infrastructure that has historically measured its patch cycles in months. If offense has collapsed to seconds, defense has to follow, and Glasswing is Anthropic's bet that a gated frontier model in the hands of defenders is the correct response to a frontier model in the hands of extortionists.

## The concentration risk nobody should ignore

The stronger the program looks, the sharper its single liability becomes. As of this expansion, 150 critical organizations — hospitals, utilities, financial systems — now depend on one vendor's model and one vendor's disclosure pipeline for a core layer of their security. That is a concentration of dependency worth naming plainly. If Mythos develops a systematic blind spot, if Anthropic's disclosure process is compromised, or if the model itself becomes a target, the failure would not be isolated to one org — it would ripple across critical infrastructure in 15 countries at once.

There is also the question of who decides. A gated model means Anthropic controls access, sets the terms, and holds the vulnerability data flowing out of 150 partners' codebases. That is a remarkable amount of sensitive information — a map of soft spots in critical systems worldwide — routed through a single company. The program's defenders would argue the alternative is worse: leaving under-resourced open-source maintainers and rural hospitals to face autonomous attackers with no machine-speed defense at all. Next to the JADEPUFFER scenario, expanding Glasswing looks like the clearly correct trade. But "correct trade" and "acceptable long-term structure" are not the same claim.

## What to watch next

Three signals will tell whether Glasswing is working or merely growing. First, disclosure velocity: does the program produce a verifiable record of vulnerabilities found and patched, with real numbers, or does it stay a press-release abstraction? Second, whether other frontier labs stand up rival defensive programs — a healthy ecosystem would dilute the concentration risk, while a monopoly deepens it. Third, and most consequential, whether the next JADEPUFFER-class attack hits a Glasswing partner, and whether the machine-speed patch actually beats the machine-speed exploit. The Five Eyes gave the world a timeline measured in months. Glasswing is Anthropic's wager that defenders can move just as fast. The next confirmed autonomous attack will settle whether the wager holds.

## Sources

- [Anthropic Expands Project Glasswing to 150 Organizations in 15 Countries — Build Fast with AI](https://www.buildfastwithai.com/blogs/ai-news-today-july-13-2026)
- [JADEPUFFER: Agentic ransomware for automated database extortion — Sysdig](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)
- [Sysdig clocks first documented case of agentic ransomware — CyberScoop](https://cyberscoop.com/sysdig-judepuffer-ai-agentic-ransomware-attack/)
- [Five Eyes Warn the Frontier AI Cyberthreat Is Months Away — GovInfoSecurity](https://www.govinfosecurity.com/five-eyes-warn-frontier-ai-cyberthreat-months-away-a-32054)
- [AI could breach government and business defenses in months, US and intelligence partners warn — CNN](https://www.cnn.com/2026/06/23/world/ai-five-eyes-warning-cyber-threat-intl-hnk)
