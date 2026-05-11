---
headline: "Anthropic Mythos Preview Finds Zero-Day Vulnerabilities in Every Major OS, Triggering Project Glasswing Security Push"
slug: anthropic-mythos-cybersecurity-zero-days
category: llms-genai
story_number: "06"
date: 2026-05-10
author: The Vault AI
---

# Anthropic Mythos Preview Finds Zero-Day Vulnerabilities in Every Major OS, Triggering Project Glasswing Security Push

An unreleased AI model from Anthropic has discovered thousands of previously unknown security flaws across every major operating system and web browser, prompting an unprecedented industry-wide defensive coalition and raising urgent questions about what happens when artificial intelligence outpaces human security expertise.

## The Discovery That Changed the Equation

Claude Mythos Preview, a general-purpose frontier model that Anthropic has no plans to release publicly, has achieved something no automated system has done before: it autonomously identified and exploited zero-day vulnerabilities in every major operating system, every major web browser, and a wide range of critical software infrastructure. Many of these flaws had survived decades of human code review and millions of automated security scans without detection.

The scale is staggering. Anthropic reports that the model has found thousands of high-severity vulnerabilities, with over 99 percent still unpatched as coordinated disclosure processes work through the backlog. In one striking case, the model uncovered a 27-year-old vulnerability in OpenBSD, an operating system renowned as one of the most security-hardened platforms in existence, which allowed an attacker to remotely crash any machine simply by connecting to it. In another, it found a 16-year-old flaw in FFmpeg -- the video encoding library used by countless applications -- in a line of code that automated testing tools had executed five million times without ever catching the problem.

The model did not just find bugs. It wrote working exploits. In one instance, Mythos Preview autonomously chained together multiple Linux kernel vulnerabilities to escalate from ordinary user access to complete control of the machine. Engineers at Anthropic with no formal security training reportedly asked the model to find remote code execution vulnerabilities overnight and returned the next morning to find complete, working exploits waiting for them.

## Project Glasswing: An Unprecedented Coalition

Rather than releasing this capability into the wild, Anthropic assembled Project Glasswing, a defensive security initiative that reads like a roll call of the technology industry\u2019s most powerful players. Amazon Web Services, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks have all signed on as launch partners, with access extended to more than 40 additional organizations that build or maintain critical software infrastructure.

Anthropic is backing the effort with up to $100 million in model usage credits, plus $4 million in direct donations to open-source security organizations including the Linux Foundation, Alpha-Omega, OpenSSF, and the Apache Software Foundation.

\u201cAI capabilities have crossed a threshold that fundamentally changes the urgency required to protect critical infrastructure from cyber threats, and there is no going back,\u201d said Anthony Grieco, SVP and Chief Security and Trust Officer at Cisco. \u201cThe old ways of hardening systems are no longer sufficient.\u201d

The urgency is echoed across the consortium. Elia Zaitsev, Chief Technology Officer at CrowdStrike, framed the defensive imperative bluntly: \u201cThe window between a vulnerability being discovered and being exploited by an adversary has collapsed -- what once took months now happens in minutes with AI.\u201d

## Benchmark Dominance and Independent Validation

The numbers back up the alarm. On the CyberGym vulnerability reproduction benchmark, Mythos Preview scored 83.1 percent compared to 66.6 percent for Claude Opus 4.6, Anthropic\u2019s next-best model. On SWE-bench Verified, a coding benchmark, Mythos Preview reached 93.9 percent versus Opus 4.6\u2019s 80.8 percent.

Independent validation from the UK\u2019s AI Security Institute confirmed the step change. AISI evaluators found that Mythos Preview succeeded 73 percent of the time on expert-level capture-the-flag challenges that no model could complete before April 2025. More significantly, it became the first AI model to complete The Last Ones, a 32-step simulated corporate network attack spanning reconnaissance through full network takeover -- a scenario estimated to require human professionals roughly 20 hours. Mythos Preview solved it in 3 out of 10 attempts, completing an average of 22 out of 32 steps across all runs.

AISI cautioned that the ranges lack features present in real-world environments, such as active defenders and defensive tooling, meaning the results do not prove Mythos Preview could compromise well-defended systems. But the trajectory is clear and accelerating.

## Analysis: The Dual-Use Dilemma Hits Critical Infrastructure

Anthropic\u2019s decision to withhold the model from public release while sharing it with dozens of major organizations represents a novel approach to AI deployment -- one that acknowledges the technology is simply too dangerous for general availability, at least for now. The company has stated it intends to develop safeguards for an upcoming Claude Opus model that would allow Mythos-class capabilities to eventually reach broader users without the same level of risk.

But the clock is ticking. As Anthropic itself acknowledged in its announcement, it will not be long before similar capabilities proliferate, potentially to actors who are not committed to deploying them safely. The global cost of cybercrime is already estimated at roughly $500 billion annually. A world in which AI models can autonomously discover and weaponize vulnerabilities at this scale could dramatically accelerate that figure.

For open-source maintainers, Project Glasswing may represent a lifeline. Jim Zemlin, CEO of the Linux Foundation, noted that open-source software constitutes the vast majority of code in modern systems and that maintainers have historically lacked access to serious security resources. Project Glasswing, he said, offers a credible path to changing that equation, making AI-augmented security a tool available to every maintainer rather than only those who can afford expensive security teams.

## What Comes Next

Anthropic has committed to publishing a public report within 90 days detailing vulnerabilities fixed and lessons learned. The company is also in ongoing discussions with US government officials about the model\u2019s offensive and defensive cyber capabilities, framing the technology as a national security priority for democratic nations.

The model will be available to Glasswing participants at $25 per million input tokens and $125 per million output tokens after the initial research credits are exhausted. Partners can access Mythos Preview through the Claude API, Amazon Bedrock, Google Cloud\u2019s Vertex AI, and Microsoft Foundry.

For the cybersecurity industry, the message from Mythos Preview is unambiguous: the era of AI-driven vulnerability discovery has arrived, and the gap between finding a flaw and exploiting it has collapsed to near zero. Whether defenders can stay ahead of that curve may be the defining security question of the decade.
