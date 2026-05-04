---
headline: "OpenClaw Agent Registry Hit by 820 Malicious Skills in Largest AI Agent Security Breach of 2026"
slug: openclaw-820-malicious-skills-crisis
category: llms-genai
story_number: "09"
date: 2026-05-03
---

# OpenClaw Agent Registry Hit by 820 Malicious Skills in Largest AI Agent Security Breach of 2026

The open-source AI personal assistant OpenClaw is at the center of the most significant AI agent security crisis of 2026, after researchers confirmed that at least 820 of the roughly 10,700 skills listed on its ClawHub marketplace were laced with malware -- including keyloggers, remote access trojans, and the Atomic macOS Stealer. Combined with a critical remote code execution vulnerability tracked as CVE-2026-25253, the incident has exposed fundamental weaknesses in how the fast-growing agentic AI ecosystem handles software supply chains.

## The Scale of the Compromise

OpenClaw, which has accumulated over 135,000 GitHub stars and became one of the most popular open-source AI agent frameworks of 2025, allows users to extend their personal AI assistant through installable plugins called skills. These skills are published to ClawHub and SkillsMP, community registries that until recently operated with minimal vetting.

Security firm Reco first flagged the problem in late January 2026, identifying a campaign it dubbed ClawHavoc. Initial scans found 341 malicious skills across ClawHub, representing roughly 12 percent of the registry at that time. Subsequent sweeps by Trend Micro, VirusTotal, and independent researchers pushed the confirmed count past 820, meaning nearly 8 percent of all listed skills were compromised. Some researchers have suggested the true figure may be higher, as threat actors continued uploading new malicious packages even after initial disclosures.

The malicious skills targeted both macOS and Windows users with distinct payloads. On macOS, the primary threat was Atomic Stealer, also known as AMOS, an infostealer that harvests usernames and passwords, keychain credentials, private keys, certificates, and the contents of Desktop, Downloads, and Documents folders as well as Apple Notes. Windows targets received a different package: a VMProtect-packed infostealer bundled with a keylogger and remote access trojan capabilities, delivered through password-protected ZIP files to evade automated scanning.

## How the Attack Works

What makes the ClawHavoc campaign particularly notable is its attack vector. Rather than relying on traditional social engineering aimed at humans, the threat actors embedded malicious instructions inside SKILL.md files -- the metadata documents that OpenClaw agents read to understand how to configure and use a skill. The AI agent itself becomes the unwitting intermediary, parsing the poisoned instructions and presenting fake setup requirements to users, such as prompts to enter system credentials or download a supposed dependency.

This represents a meaningful evolution in supply chain attacks: the adversary is not just exploiting the software distribution channel but is leveraging the AI agent as a trusted proxy to manipulate the end user. Researchers at 1Password described it as social engineering aimed at the AI rather than the human, a pattern that security teams have been warning about as agentic AI adoption accelerates.

## CVE-2026-25253: The One-Click RCE

Compounding the supply chain compromise is CVE-2026-25253, a critical vulnerability in OpenClaw itself carrying a CVSS score of 8.8. The flaw exists in the OpenClaw Control UI, which blindly trusts a URL parameter called gatewayUrl and automatically connects to it, leaking the user authentication token to any attacker-controlled server in the process.

With the stolen token, an attacker can open a direct WebSocket connection to the victim local OpenClaw instance, bypassing firewall and localhost protections entirely. From there, the attacker can disable user confirmation prompts, escape container sandboxes, and execute arbitrary commands on the host machine -- achieving full remote code execution in milliseconds with no user interaction beyond loading a malicious webpage.

SonicWall and Broadcom both published advisories confirming active exploitation in the wild. By the time public disclosure occurred on February 3, security firms had identified over 40,000 OpenClaw instances exposed on the public internet, with 63 percent assessed as vulnerable to remote exploitation. Broader scans found over 135,000 instances running on publicly accessible IP addresses.

## The Governance Gap

The incident has intensified debate around what researchers at DEV Community and IBM X-Force have called the runtime governance gap in agentic AI. OpenClaw skills run with the same permissions as the host agent, which typically operates with broad system access -- reading files, executing commands, making network requests. There is no sandboxing, no permission scoping, and until the breach, no meaningful code review process for skills submitted to ClawHub.

Cisco researchers noted that the OpenClaw architecture exemplifies a broader pattern across personal AI agent platforms: convenience and extensibility are prioritized over security boundaries. The assumption that community-contributed plugins are safe mirrors the early days of browser extensions and mobile app stores before those ecosystems learned hard lessons about supply chain integrity.

## Remediation and Response

The OpenClaw maintainers released version 2026.1.29 on February 4, patching CVE-2026-25253 and introducing a mandatory skill signing mechanism for ClawHub. Users running any prior version are advised to update immediately, rotate all authentication tokens and credentials, and audit installed skills to remove unrecognized packages.

ClawHub has since purged confirmed malicious skills and implemented automated static analysis scanning for new submissions. However, security researchers have cautioned that the registry still lacks runtime behavioral analysis, meaning skills that pass static checks but activate malicious behavior conditionally could still slip through.

## What to Watch Next

The OpenClaw crisis is likely a preview of security challenges to come as agentic AI platforms proliferate. With Microsoft, Google, and dozens of startups racing to ship agent frameworks that support third-party plugins and tool integrations, the attack surface for AI supply chain compromises is expanding rapidly. Enterprises evaluating agent deployment should watch for the emergence of dedicated agent security governance tools -- a market that Microsoft began addressing this week with Agent 365 -- and should treat any agent skill or plugin marketplace with the same skepticism they apply to unvetted open-source dependencies. The era of trusting AI agent extensions by default is over.