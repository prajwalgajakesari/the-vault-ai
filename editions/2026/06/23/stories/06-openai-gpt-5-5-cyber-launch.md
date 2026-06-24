---
headline: "OpenAI Launches GPT-5.5-Cyber, Its Most Capable Defensive Security Model Yet"
category: llms-genai
story_number: "06"
slug: openai-gpt-5-5-cyber-launch
date: 2026-06-23
---

# OpenAI Launches GPT-5.5-Cyber, Its Most Capable Defensive Security Model Yet

On June 23, OpenAI put its strongest cyber model into the hands of the people it trusts to defend the internet — and pointedly out of reach of everyone else. The company released a more capable, more permissive version of GPT-5.5-Cyber as the centerpiece of its Daybreak platform, pairing it with an upgraded Codex Security plugin and a new open-source remediation drive called Patch the Planet. The pitch is blunt: the same frontier intelligence that lets attackers find and weaponize bugs faster than ever should be wielded, first and hardest, by defenders.

The headline number is a benchmark. On CyberGym — a suite that asks an AI agent to reproduce known software vulnerabilities inside controlled testing environments — the updated GPT-5.5-Cyber scored 85.6%, a new state of the art. That edges out the standard GPT-5.5 at 81.8% and, more conspicuously, tops Anthropic's Mythos 5 at 83.8% and Claude Opus 4 at 73.1%. CyberGym, built at UC Berkeley, draws on 1,507 real vulnerabilities across 188 open-source projects, so the gains are not abstract.

## What the model actually does

OpenAI describes GPT-5.5-Cyber as its "strongest model yet for finding and helping patch software vulnerabilities," and the capability list reads less like a chatbot and more like a tireless security engineer. The model can, in the company's words, "sustain deeper analysis across large codebases" — identifying security-relevant components, tracing the reachability of vulnerable code, validating issues in controlled environments, and then developing and testing patches end to end.

The Linux kernel is the marquee demonstration. Turned loose on a codebase exceeding 30 million lines, the model surfaced security-relevant components and generated 8 kernel pointer information-leak proofs-of-concept alongside 24 local privilege-escalation exploits. The same Daybreak effort flagged a 23-year-old use-after-free in OpenBSD's System V semaphore implementation, 34 vulnerabilities in FreeBSD, exploitable bugs in Chrome's V8 engine and Apple's Safari, and a denial-of-service technique dubbed HTTP/2 Bomb affecting NGINX, Apache, IIS and Pingora.

The upgraded Codex Security plugin is how most defenders will touch this. "Developers can run deep scans or review recent changes, generate reports with severity, affected code locations, validation evidence, and remediation guidance, trace attack paths, build threat models, validate findings, and generate codebase-specific patches for review," OpenAI said. It can also triage existing findings from scanners, advisories, bug-bounty reports and ticketing systems, then mass-generate patches to burn down a backlog.

## A walled garden by design

None of this is open to the public. GPT-5.5-Cyber ships only to organizations vetted through OpenAI's Trusted Access for Cyber program, which lowers the model's classifier-based refusals for approved defensive work — secure code review, vulnerability triage, malware analysis, binary reverse engineering, detection engineering, red teaming and penetration testing — while continuing to block requests aimed at credential theft, stealth, persistence and malware deployment.

"OpenAI is releasing a more permissive version of its cybersecurity model, which the company says is designed for advanced, authorized security work," Axios reporter Sam Sabin wrote, capturing the central tension. "AI developers face a difficult balancing act: getting powerful cyber capabilities into the hands of legitimate defenders and researchers while limiting opportunities for malicious use."

OpenAI is also widening distribution through the new Daybreak Cyber Partner Program, which lets vetted vendors embed GPT-5.5 with Trusted Access for Cyber inside their own products. The roster spans much of the security and infrastructure industry — Akamai, Cisco, Cloudflare, CrowdStrike, Fortinet, Oracle, Palo Alto Networks and Zscaler among them. Until now, approved organizations mostly ran these models against systems they owned or were authorized to test; the partner program pushes the capability outward to customer environments.

## The race nobody wants to lose — or stop

The launch lands as a deliberate answer to Anthropic, whose Project Glasswing used Claude Mythos to surface more than 10,000 high- or critical-severity vulnerabilities across systemically important open-source software. But Anthropic's effort has been snared in policy limbo, with the U.S. government ordering it to suspend Fable 5 and Mythos 5 access for foreign nationals — a cautionary tale OpenAI appears determined to route around through governance and partnerships rather than raw openness.

That backdrop hints at the strategic logic underneath Daybreak: build a defensive capability so woven into the world's critical infrastructure — kernels, browsers, the open-source supply chain — that pulling the plug becomes its own security risk. Patch the Planet, launched with Trail of Bits and joined by projects including cURL, Python, the Go project and pyca/cryptography, is the clearest expression of that bet. "Patch the Planet is designed to put that full defensive loop in service of maintainers: discovery, validation, severity review, disclosure, patch development, testing, and deployment," OpenAI said, adding that the aim is "to give the people responsible for shared infrastructure better tools and more capacity, while preserving their agency over how changes land."

The urgency is not self-generated. Intelligence agencies across the Five Eyes alliance warned this month that frontier models will "fundamentally transform both offensive and defensive cyber capabilities," and that "the timeline is not years, it is months." Canada's Centre for Cyber Security was blunter still: organizations should assume AI-driven exploitation "may bypass preventative controls" and outpace vendors' capacity to ship fixes.

## What to watch

The bet is that defenders, armed with an 85.6% model and an industry-wide partner network, can close the gap between disclosure and exploitation faster than attackers can widen it. The open questions are whether Trusted Access vetting holds as distribution scales through dozens of vendors, whether maintainers welcome or drown in AI-generated patches, and whether regulators treat OpenAI's governed approach as the responsible template — or apply the same scrutiny that froze Anthropic's models. If GPT-5.5-Cyber genuinely tilts the kernel-and-browser layer toward defense, the "too important to shut down" strategy will have proved itself. If the floodgates spill, June 23 will be remembered as the day the cyber-AI arms race went fully mainstream.
