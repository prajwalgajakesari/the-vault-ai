---
headline: "Anaconda Buys Enkrypt AI to Secure the 'Trillion-Token Enterprise'"
slug: anaconda-acquires-enkrypt-ai
category: business
story_number: "02"
date: 2026-08-05
---

# Anaconda Buys Enkrypt AI to Secure the 'Trillion-Token Enterprise'

Anaconda has spent more than a decade as the plumbing beneath enterprise Python and data science. On Tuesday it made its clearest bet yet on the next problem its customers are staring down: not whether AI agents can move fast, but whether anyone can prove what they are actually doing.

The Austin company announced on August 4 that it has acquired Enkrypt AI, an AI security and compliance startup, folding red-teaming, runtime guardrails and regulatory automation into a platform Anaconda now pitches as the single governed path "from a builder's first prompt to their AI-native application running in production." Terms of the deal were not disclosed. Enkrypt AI, a Gartner-recognized "Cool Vendor in AI Security" in 2025, will continue to operate with no changes to existing products, plans or support for current users.

## The number behind the deal

The acquisition arrives wrapped in a statistic Anaconda clearly wants the market to sit with. In the two months leading up to the announcement, Enkrypt AI scanned more than 268,000 tools, the individual functions AI agents call, across 25,000 Model Context Protocol (MCP) servers. It found more than 143,000 vulnerabilities, affecting 73% of those servers.

That is the crux of the pitch. MCP, the open standard that lets agents reach out to external tools and data, has become the connective tissue of the agent economy over the past year. It has also quietly become an attack surface. Every model an agent runs on, every tool it calls and every MCP server it touches, Anaconda argues, is a potential exposed vector, and most enterprises have no systematic way to see any of it.

"Enterprises are running AI-native applications and services that already contain exploitable vulnerabilities and weaknesses, leaving them exposed to unknown risks they cannot easily address," said David DeSanto, CEO of Anaconda. "Enkrypt AI makes the unknown known, giving teams the security and guardrails required to get the board, CISO, and legal sign-off they need to scale systems with confidence."

## What Enkrypt actually brings

Enkrypt AI's technology spans what the company calls the full AI-native security lifecycle. Before deployment, it runs red-teaming across more than 300 attack categories, so failures surface in testing rather than in front of a user. At runtime, it applies guardrails that block jailbreaks and sensitive-data leakage in real time, and, notably, can be deployed inside a customer's own environment rather than forcing traffic through a public cloud. On top of that sits compliance automation that translates frameworks such as the NIST AI Risk Management Framework and the EU AI Act into guardrails that are enforced automatically.

The compliance timing is not incidental. Key provisions of the EU AI Act became active on August 2, two days before the deal was announced, and Enkrypt is positioning its controls as a way to turn that regulatory pressure into enforced, automated rules rather than a manual audit exercise. The company is also an OpenAI compliance integration partner, giving ChatGPT Enterprise customers turnkey access to its audit and guardrail controls, with the same model-agnostic approach promised soon for enterprises running Anthropic.

## Trust as an architecture problem

Enkrypt's leadership framed the deal less as a feature addition than as a philosophical stance on when security has to happen.

"There's a difference between running AI, and running AI safely," said Sahil Agarwal, co-founder and CEO of Enkrypt AI. "Enterprises are actively looking for a way to reduce AI model security risk, before it levels up to a boardroom problem. Trust can't be added after an agent ships, it has to be built into and run on a trusted foundation from day one."

That "from day one" argument is the thread Anaconda is pulling through a busy year of dealmaking. The Enkrypt purchase follows Anaconda's acquisition of Kilo Code in July, which pushed the platform into agentic engineering environments, and of Outerbounds in April, which added production-grade AI orchestration. Stack them together and the strategy is legible: own the model foundation, the orchestration layer, the agentic build environment and now the security and compliance layer, and sell the whole governed pipeline to enterprises drowning in AI risk. Anaconda says 95% of the Fortune 500 and more than 52 million users already rely on its platform.

## What to watch

The vulnerability numbers make a persuasive marketing hook, but they also raise the harder question of remediation at scale. As Anaconda's own blog concedes, "there's no patch for an exposure that was never fully understood in the first place" — traditional patch-and-move-on security does not map cleanly onto probabilistic model behavior. Enkrypt's red-team research claims to have found exploitable attack categories in every leading frontier model it tested, including those from Anthropic, OpenAI, Google, Mistral and DeepSeek, which suggests the problem is systemic rather than vendor-specific.

The open questions now are integration and independence. Enkrypt has built part of its credibility on being vendor-neutral and cloud-agnostic; folding it into a single platform vendor will test whether enterprises still trust it to grade everyone's homework, including Anaconda's. Watch for how quickly the two products actually merge, whether the Anthropic integration ships on schedule, and whether the trillion-token security pitch survives contact with a real board's procurement process. For now, Anaconda has planted a flag: at agent scale, speed without proof is a liability.
