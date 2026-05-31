---
headline: "Project Glasswing Finds 10,000 Vulnerabilities in 30 Days, Shifting Cybersecurity Bottleneck From Discovery to Remediation"
slug: glasswing-10000-vulnerabilities-bottleneck-shift
category: research
story_number: 10
date: 2026-05-30
author: The Vault AI Edition
---

# Project Glasswing Finds 10,000 Vulnerabilities in 30 Days, Shifting Cybersecurity Bottleneck From Discovery to Remediation

For decades, the central constraint in software security was the same: finding vulnerabilities before attackers did. That constraint no longer applies. In its place is a new and arguably more difficult one -- fixing them fast enough to matter.

Anthropic's Project Glasswing, a consortium of roughly 50 organizations armed with the restricted Claude Mythos Preview model, has surfaced more than 10,000 high- or critical-severity vulnerabilities across systemically important software in just 30 days. The scale of discovery has outpaced the global capacity to respond, exposing a remediation crisis that the cybersecurity industry was not built to handle.

## The numbers behind the surge

Launched in April 2026, Project Glasswing grants gated access to Mythos Preview -- a frontier AI model purpose-built for autonomous vulnerability discovery -- alongside up to $100 million in usage credits. Partners include AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. IBM joined the consortium in May, bringing its enterprise security expertise to the effort and contributing findings through coordinated disclosure and upstream open-source patches.

Anthropic has also independently scanned more than 1,000 open-source projects with Mythos. The model flagged 23,019 potential issues, of which 6,202 were estimated as high or critical severity. When six independent security research firms reviewed 1,752 of those high- or critical-rated findings, 90.6 percent turned out to be valid true positives, and 1,094 were confirmed as genuinely high or critical. That false-positive rate is, by multiple accounts, better than human testers typically achieve.

The standout individual find was CVE-2026-5194, a critical flaw in wolfSSL (CVSS score: 9.1), the open-source cryptography library embedded in billions of devices worldwide. Mythos Preview constructed an exploit that could allow an attacker to forge digital certificates -- effectively enabling fake bank websites or email providers to appear perfectly legitimate to end users. The vulnerability, discovered by Nicholas Carlini of Anthropic's Frontier Red Team, has since been patched in wolfSSL version 5.9.1.

But wolfSSL was far from the only legacy code to fall under scrutiny. Mythos also unearthed a 27-year-old vulnerability in the OpenBSD kernel and a 16-year-old flaw in FFmpeg's H.264 decoder, where the underlying bug dated back to a 2003 commit and became exploitable after a 2010 refactor. These are the kinds of deeply buried flaws that human auditors have walked past for years.

## Partners report tenfold detection increases

Individual consortium members have reported results that redefine the baseline for what security teams can accomplish. Cloudflare found 2,000 bugs across its critical-path systems, 400 of which were rated high or critical severity, with a false-positive rate its team described as better than human testers. Mozilla found and fixed 271 vulnerabilities in Firefox 150 while testing Mythos Preview -- more than ten times the number identified in Firefox 148 using Claude Opus 4.6. Palo Alto Networks shipped more than five times its usual volume of patches in a recent release cycle. Microsoft has warned that its monthly patch counts will "continue trending larger for some time."

XBOW, an independent offensive security platform, called the model "a significant step up over all existing models" on its web exploit benchmark.

## The bottleneck has moved

The paradox at the heart of Project Glasswing is that its success has created a new crisis. Anthropic acknowledged this directly in its May 22 update: "Progress on software security used to be limited by how quickly we could find new vulnerabilities. Now it's limited by how quickly we can verify, disclose, and patch the large numbers of vulnerabilities found by AI."

Of the 530 high- or critical-severity bugs Anthropic has disclosed to open-source maintainers so far, just 75 have been patched. Several maintainers have asked Anthropic to slow down its rate of disclosure because they lack the capacity to design fixes. On average, a high- or critical-severity bug found by Mythos takes two weeks to patch -- and that timeline assumes a maintainer is available and willing to engage.

The remediation gap is compounded by the flood of low-quality, AI-generated bug reports from other sources already overwhelming maintainers. Anthropic says it reproduces and assesses each issue before reporting, but the sheer volume is straining a system built on volunteer labor. And with Anthropic's 90-day coordinated disclosure policy, unpatched vulnerabilities may become public whether or not a fix is ready.

## A new security posture

Anthropic is not standing still on the remediation problem. The company has launched Claude Security in public beta for enterprise customers, which has been used to patch over 2,100 vulnerabilities in three weeks using Claude Opus 4.7. It has partnered with the Open Source Security Foundation's Alpha-Omega project to help maintainers triage incoming reports, and begun a Cyber Verification Program that lets security professionals use its models without certain safeguards for legitimate penetration testing and red teaming.

Beyond vulnerability hunting, Mythos is proving useful for broader security work. At one Glasswing partner bank, the model helped detect and prevent a fraudulent $1.5 million wire transfer after attackers compromised a customer's email and conducted spoofed phone calls.

## What comes next

Anthropic has been clear that Mythos-class models will not be released publicly until stronger safeguards exist to prevent misuse. But similarly capable models from other AI companies are not far behind, and the window during which vulnerabilities are being rapidly discovered and slowly patched presents heightened risk.

"Glasswing helps the most systemically important cyber defenders gain an asymmetric advantage," the company stated. "However, there is an urgent need for as many organizations as possible to shore up their cyber defenses."

The message to software developers and network defenders is blunt: shorten patch cycles, harden default configurations, enforce multi-factor authentication, and deploy updates faster. The age of security through obscurity -- where bugs survive simply because no one looked hard enough -- is ending. What replaces it will be defined not by how well we find problems, but by how fast we fix them.
