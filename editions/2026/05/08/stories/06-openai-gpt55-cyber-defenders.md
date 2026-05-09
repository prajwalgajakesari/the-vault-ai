---
headline: "OpenAI Rolls Out GPT-5.5-Cyber to Vetted Security Teams With Fewer Guardrails for Defenders"
slug: openai-gpt55-cyber-defenders
category: llms-genai
story_number: "06"
date: 2026-05-08
sources:
  - name: OpenAI Blog
    url: https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/
    domain: openai.com
  - name: Help Net Security
    url: https://www.helpnetsecurity.com/2026/05/08/openai-gpt-5-5-cyber-model/
    domain: helpnetsecurity.com
  - name: Axios
    url: https://www.axios.com/2026/05/07/openai-gpt-55-cybersecurity-model
    domain: axios.com
  - name: UK AI Security Institute
    url: https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities
    domain: aisi.gov.uk
  - name: Neowin
    url: https://www.neowin.net/news/openai-doubles-down-on-cyber-defense-gpt-55-cyber-limited-preview-now-available/
    domain: neowin.net
---

# OpenAI Rolls Out GPT-5.5-Cyber to Vetted Security Teams With Fewer Guardrails for Defenders

OpenAI is placing its most powerful cybersecurity tool yet into the hands of vetted defenders, launching GPT-5.5-Cyber in limited preview to approved security teams with deliberately loosened guardrails designed to let the good guys work faster than the adversaries trying to break in.

The model, announced on May 7 and made available through OpenAI's Trusted Access for Cyber program, represents the most permissive variant in the company's cybersecurity lineup. It is engineered for specialized workflows such as authorized red teaming, penetration testing, and high-severity vulnerability validation that standard consumer-facing models would refuse to assist with.

## A Tiered Trust Architecture

At the heart of the release is OpenAI's Trusted Access for Cyber (TAC) framework, an identity and trust-based access system that vets cybersecurity professionals before granting them elevated model permissions. The framework establishes multiple access tiers: the base GPT-5.5 model available to general users; GPT-5.5 with Trusted Access for Cyber, which OpenAI recommends as the entry point for most defensive security workflows; and now GPT-5.5-Cyber, which sits at the top with the fewest restrictions and the strictest verification requirements.

"The initial preview of cyber-permissive models like GPT-5.5-Cyber is not intended to significantly increase cyber capability beyond GPT-5.5 -- it's primarily trained to be more permissive on security-related tasks," OpenAI wrote in its blog post announcing the release. The company emphasized that the differences between model access levels are most pronounced when comparing prompts and responses, not raw capability.

Launch partners for the program include Cisco, CrowdStrike, Palo Alto Networks, Cloudflare, Intel, Snyk, and SentinelOne -- a roster that reads like a who's who of enterprise security. These organizations will be among the first to integrate GPT-5.5-Cyber into their defensive operations.

"We'd like to help companies secure themselves, and we think it's important to start work on this quickly," OpenAI CEO Sam Altman wrote on X, signaling that the company views cybersecurity as both a commercial opportunity and a moral imperative.

## Staggering Benchmark Results

Independent testing from the UK's AI Security Institute paints a striking picture of just how capable GPT-5.5 has become at cyber tasks. In AISI's evaluation, GPT-5.5 achieved a 71.4 percent pass rate on expert-level cybersecurity capture-the-flag challenges, edging out Anthropic's Claude Mythos Preview at 68.6 percent and substantially outperforming GPT-5.4 at 52.4 percent.

Perhaps the most jaw-dropping result involved a complex reverse-engineering challenge that required an attacker to decode a custom virtual machine implemented in Rust, build a disassembler from scratch, reverse-engineer an authentication protocol, and solve for a valid password. A human expert from Crystal Peak Security needed roughly 12 hours to complete the challenge. GPT-5.5 solved it in 10 minutes and 22 seconds at a cost of $1.73 in API usage.

On AISI's most demanding test, a 32-step corporate network attack simulation called "The Last Ones" that models an enterprise intrusion spanning four subnets and roughly 20 hosts, GPT-5.5 completed the full chain end-to-end in 2 of 10 attempts. The simulation, which AISI estimates would take a human expert around 20 hours, requires chaining reconnaissance, credential theft, lateral movement across Active Directory forests, and a CI/CD supply-chain pivot.

## The Asymmetry Problem

The release arrives at a moment when the cybersecurity community is grappling with a fundamental asymmetry. Models of GPT-5.5's caliber are becoming potent offensive tools whether companies like OpenAI intend it or not, and AISI's evaluation noted that rapid improvement on cyber tasks appears to be a byproduct of general advances in reasoning and coding rather than deliberate specialization. If that trend holds, each new frontier model generation will arrive with incrementally stronger offensive cyber capabilities baked in.

OpenAI's strategy with GPT-5.5-Cyber is to lean into this reality rather than pretend it away. By giving defenders access to the same capabilities that adversaries might exploit, the company is betting that transparency and controlled access will produce better security outcomes than blanket restrictions.

During early testing, selected partners used GPT-5.5-Cyber to automate and expand red-teaming exercises on infrastructure systems and to validate high-severity vulnerabilities. OpenAI said it plans to document these results in a future technical deep dive as part of a responsible disclosure process.

"We expect to continue to accelerate defenders with various models, including both our flagship models through Trusted Access for Cyber, and with dedicated cyber models like GPT-5.5-Cyber and even more cyber-capable models in the future," the company stated.

## What to Watch

The AISI evaluation did surface concerns. Expert red-teamers identified a universal jailbreak that could elicit harmful cyber content across all malicious queries, and while OpenAI made updates to its safeguard stack, a configuration issue prevented AISI from fully verifying the fixes. That finding underscores a persistent tension: making models more permissive for defenders inevitably creates a wider attack surface for misuse.

The UK government's latest Cyber Security Breaches Survey, published the same week, found that 43 percent of businesses suffered a cyber breach or attack in the past 12 months. With frontier AI models now capable of completing in minutes what takes human experts hours, the race between offense and defense is accelerating -- and GPT-5.5-Cyber is OpenAI's bet that arming the defenders is the right move.

## The Bottom Line

OpenAI is making a calculated gamble: that the cybersecurity industry benefits more from powerful, permissive AI tools in trusted hands than from models hobbled by overly cautious guardrails. With GPT-5.5 already demonstrating expert-level offensive capabilities in independent testing, the question is no longer whether AI will reshape cybersecurity, but whether defenders can adopt these tools fast enough to stay ahead.
