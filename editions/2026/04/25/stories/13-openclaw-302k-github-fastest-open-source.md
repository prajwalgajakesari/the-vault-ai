# OpenClaw Surpasses 302K GitHub Stars to Become Fastest-Growing Open-Source Project in History

In the span of roughly 60 days, a personal AI assistant framework created by an Austrian developer has shattered every growth record on GitHub -- and in doing so, has rewritten the rules for what open-source AI projects can achieve.

OpenClaw, the autonomous agent framework formerly known as Clawdbot, crossed 302,000 GitHub stars on April 3, 2026, making it the fastest-growing open-source project in the platform's 18-year history. By April 8, the count had climbed further to 350,600 stars with 70,400 forks and 1,600 contributors. To put that trajectory in perspective, React took more than a decade to accumulate 243,000 stars. OpenClaw eclipsed that figure in two months.

## From Weekend Hack to Global Phenomenon

The project began as a weekend experiment by Peter Steinberger, the founder of document-technology company PSPDFKit, which he sold for a reported $800 million. First published in November 2025 under the name Clawdbot, the tool was designed to let a large language model run as a persistent, autonomous assistant on a user's own hardware -- executing shell commands, managing files, and automating web tasks through familiar messaging platforms like WhatsApp, Telegram, Slack, and Discord.

Anthropic filed a trademark complaint over the original name in January 2026, prompting a brief rebrand to "Moltbot" -- a nod to the project's lobster mascot -- before Steinberger settled on "OpenClaw" three days later because, as he put it, "Moltbot never quite rolled off the tongue."

The name change did nothing to slow momentum. Within 72 hours of its January relaunch, the project had 60,000 stars. By the end of the month, it had surpassed 100,000 stars and recorded two million visitors in a single week. On March 3, it overtook React at 250,829 stars to become GitHub's most-starred software repository, trailing only TensorFlow -- a mark it soon surpassed as well.

"OpenClaw just beat React's 10-year GitHub record in 60 days," wrote technology analyst Aftab in a widely circulated Medium post. "Now nobody knows what to do with it."

## Why Developers Are Flocking to It

OpenClaw's appeal rests on a simple but powerful proposition: it runs entirely on the user's own machine. In an industry increasingly dominated by cloud-based AI services that route sensitive data through third-party servers, OpenClaw's local-first architecture offers developers and enterprises something they have been clamoring for -- full control over their data and execution environment.

The framework is model-agnostic, supporting Claude, GPT-4, Gemini, Grok, DeepSeek, and local models through Ollama. Users manage their own API keys and control their own costs. A local Gateway daemon handles authentication, session state, tool execution, and event routing, consolidating messages from more than 20 messaging platforms into a single agent workspace.

"The core innovation is architectural simplicity combined with powerful integration," noted Tosin Akinosho, writing for Decision Crafters. "OpenClaw provides a local Gateway -- a control plane that manages sessions, channels, tools, and events."

The project's ClawHub skills marketplace already lists more than 800 published extensions, covering everything from Gmail triage and GitHub automation to Spotify control and smart-home orchestration. A plugin architecture enables community contributions, and a growing library of pre-built agent templates lowers the barrier to entry for non-technical users.

## A New Institutional Home

On February 14, 2026, Steinberger announced he would be joining OpenAI, and that OpenClaw would be transferred to an independent 501(c)(3) foundation. OpenAI is providing financial sponsorship, but the project retains its MIT open-source license and community governance model -- a structure designed to reassure contributors that the framework will not be captured by any single corporate interest.

The governance question matters. At least 168 startups have already sprung up in the OpenClaw ecosystem, collectively generating nearly $400,000 in monthly revenue according to TrustMRR data. A separate commercial entity, OpenClawd, offers managed hosting with pre-configured security. And Moltbook, a social network for AI agents built on the framework, has attracted 1.5 million registered agents.

## Security Concerns Linger

Rapid growth has brought scrutiny. Researchers discovered approximately 42,000 exposed OpenClaw instances running without adequate security controls -- a finding reported by The New Stack that has prompted the development team to prioritize security hardening and improved ClawHub vetting to prevent malicious skills from entering the marketplace.

The local execution model, while a privacy advantage, also places the burden of security squarely on individual users and organizations. Security teams evaluating the framework are advised to review its permission model carefully, configure sandboxed execution environments, and establish command whitelisting before deployment.

## What It Means for Open-Source AI

OpenClaw's meteoric rise is more than a curiosity of GitHub gamification. It signals a genuine structural demand for AI tools that prioritize user sovereignty -- the ability to run powerful autonomous agents without surrendering data or control to a cloud provider. The venture capital firm a16z highlighted the milestone in a public post, noting that OpenClaw "managed to surpass both Linux and React on its way to the number one all-time leader in GitHub stars."

Whether the project can sustain its momentum will depend on how well its new foundation navigates the twin challenges of security and governance at scale. But for now, OpenClaw has demonstrated that in the age of AI agents, the open-source model is not just alive -- it is setting records that the industry's largest incumbents never came close to matching.
