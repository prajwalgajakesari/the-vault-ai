---
headline: "Google Documents 32 Percent Surge in Prompt Injection Attacks Hijacking Enterprise AI Agents"
slug: google-prompt-injection-agent-hijacking
category: research
story_number: "11"
date: 2026-05-01
---

# Google Documents 32 Percent Surge in Prompt Injection Attacks Hijacking Enterprise AI Agents

Malicious instructions hidden inside ordinary web pages are hijacking enterprise AI agents at an accelerating rate, with Google researchers documenting a 32 percent surge in prompt injection attacks between November 2025 and February 2026 -- the first large-scale empirical evidence that a vulnerability security experts have warned about for years is now being actively weaponized in the wild.

The findings, published April 23 in a Google Security Blog post titled "AI Threats in the Wild," draw on one of the largest datasets ever assembled for this purpose: Google's repository of 2 to 3 billion web pages crawled per month through the CommonCrawl archive. Researchers Thomas Brunner, Yu-Han Liu, and Moni Pande from Google's Threat Intelligence teams scanned multiple snapshots of the archive to track how indirect prompt injection -- the technique of embedding hidden commands in web content that AI agents unknowingly execute -- is evolving from a theoretical concern into a practical threat.

## What They Found

The research team categorized prompt injections discovered across the public web into several buckets, ranging from harmless pranks to genuinely dangerous attack vectors. On the benign end, some injections simply altered an AI agent's conversational tone or appended helpful context to summaries. Others were designed to block AI agents from scraping content altogether -- a defensive use case that nonetheless demonstrates the technique's prevalence.

The truly alarming discoveries sat at the other end of the spectrum. Researchers identified prompt injections containing fully specified PayPal transaction instructions, complete with recipient accounts and transfer amounts, designed to trick AI agents with payment capabilities into initiating fraudulent transfers. Other injections attempted to steal passwords, exfiltrate sensitive data, or redirect agents to attacker-controlled servers. Some attackers employed hidden text and CSS tricks -- white text on white backgrounds, zero-pixel font sizes, off-screen positioning -- to make their injections invisible to human readers while remaining fully legible to AI systems parsing the underlying HTML.

"Our findings indicate that, while past attempts at IPI attacks on the web have been low in sophistication, their upward trend suggests that the threat is maturing and will soon grow in both scale and complexity," the researchers wrote.

## The SEO Parallel

A significant portion of the injections Google identified were aimed at search engine optimization -- or more precisely, its AI-era equivalent. These injections attempt to manipulate AI agents and language models that retrieve and summarize web content, steering them toward specific products, services, or narratives. The researchers drew a direct parallel to the early days of web SEO, when hidden text and doorway pages were used to game traditional search rankings before Google's algorithms adapted.

The implication is clear: as AI agents increasingly mediate how users discover and interact with online information, the incentive to manipulate those agents will only intensify.

## Why the Threat Is Escalating

The researchers pointed to a fundamental shift in the cost-benefit calculus facing attackers. "Threat actors tend to engage based on cost/benefit considerations. In the past, IPI attacks were considered exotic and difficult. And even when compromised, AI systems often were not able to execute malicious actions reliably. We believe that this could change soon," the team warned.

Two forces are converging to make that prediction credible. First, today's AI agents are far more capable than their predecessors -- they can send emails, execute terminal commands, process payments, and interact with enterprise databases. A browser-based AI that merely summarizes web pages is a low-value target, but an agentic system connected to PayPal, Slack, or an internal CRM represents a high-impact attack surface. Second, threat actors themselves are now using AI to automate their operations, dramatically lowering the cost of crafting and deploying prompt injection attacks at scale.

## Industry Context

The Google research lands at a moment when the broader security community is sounding alarms. OWASP continues to rank prompt injection as the number one vulnerability in its Top 10 for LLM applications in 2026, a position it has held since the list's inception. Security audits have found prompt injection vulnerabilities in roughly 73 percent of production AI deployments.

The problem is compounded by the fact that no definitive fix exists. The UK's National Cyber Security Centre has stated that prompt injection may never be fully solved, and OpenAI CISO Dane Stuckey has called it a "frontier, unsolved security problem." The core challenge is architectural: large language models are designed to interpret natural language flexibly, and there is no reliable way to draw a hard boundary between legitimate instructions and malicious data embedded in the content they process.

Google itself published a companion blog post detailing its approach to mitigating indirect prompt injection in Google Workspace, describing a layered defense strategy that includes input sanitization, output validation, and behavioral monitoring. But the company acknowledged that these are mitigations, not solutions -- the arms race between attackers and defenders is only beginning.

## The Bottom Line

For enterprises rushing to deploy AI agents with real-world capabilities, Google's research delivers an uncomfortable message: every web page, email, and document your agent reads is a potential attack vector. The 32 percent surge documented over just three months suggests the window for getting security architectures right is closing fast. Organizations connecting AI agents to sensitive internal systems without real-time monitoring of agent behavior are, in the researchers' framing, flying blind into an increasingly hostile environment.
