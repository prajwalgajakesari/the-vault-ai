---
headline: "Microsoft Open Source Tools Hacked to Steal AI Developers' Passwords"
slug: microsoft-open-source-supply-chain-attack
category: policy
story_number: 15
date: 2026-06-09
---

# Microsoft Open Source Tools Hacked to Steal AI Developers' Passwords

The malware did not wait for you to run any code. It fired the moment you opened the repository.

On June 5, 2026, a self-replicating worm called Miasma tore through Microsoft's GitHub presence in an automated sweep that lasted just 105 seconds, compromising 73 repositories across four Microsoft organizations — Azure, Azure-Samples, Microsoft, and MicrosoftDocs. GitHub disabled the affected repos in response, breaking CI/CD pipelines and cutting off access to critical Azure tooling for an unknown number of developers worldwide. The incident stands as one of the most aggressive software supply-chain attacks ever recorded against a single company's open source estate.

The attack was devastatingly simple in its design. Miasma planted configuration files inside the compromised repositories — files that trigger a credential-harvesting payload the instant a developer opens the project inside an AI coding agent such as Claude Code, Gemini CLI, Cursor, or VS Code. No build step required. No manual execution. The payload activated on open, silently exfiltrating cloud platform passwords, API keys, and developer credentials before the developer typed a single line of code.

Azure bore the worst of it. The Azure organization alone lost 49 repositories — essentially the entire output of Microsoft's Azure Functions team. Developers working on serverless infrastructure, event-driven architectures, and the Durable Task orchestration framework found their tooling gone overnight.

Microsoft spokesperson Ben Hope confirmed the company's response in a statement to TechCrunch: "As part of our investigation, we notified a small number of customers who may have pulled down content from the affected repositories. We will continue to investigate, and if anything further is identified that requires customer action, we will reach out directly through our established support channels." Microsoft declined to specify how many customers were affected, but security researchers say the realistic exposure runs into the tens of thousands of developers.

## A Second Bite: The Re-Compromise Problem

What makes this incident particularly alarming is that it was not Microsoft's first. In mid-May 2026, the Durable Task PyPI package was initially compromised — three malicious versions were uploaded in a 35-minute window on May 19 using a stolen publishing token. Those packages were quickly pulled, and Microsoft appeared to have contained the damage. It had not.

Security firm OpenSourceMalware characterized the June attack as a direct "re-compromise" of the Durable Task project, strongly suggesting that Microsoft failed to rotate the GitHub Actions secrets stolen in the original May breach. The attackers — most likely a threat group identified as TeamPCP — exploited the same stale credentials to push a malicious commit to the Azure/durabletask repository, seeding the wider Miasma worm campaign from there.

Cloudsmith, which was among the first to publicly identify and name Miasma, described the worm in its analysis as "a new variant of the Shai-Hulud" open-source malware kit that TeamPCP released in mid-May 2026. The group had already cut its teeth against multiple high-profile targets before reaching Microsoft: 42 npm packages tied to TanStack, Mistral AI across npm and PyPI, 639 versions across 323 packages in the @antv ecosystem, and the @redhat-cloud-services npm scope. Microsoft, despite its scale and security resources, was not a harder target — it was simply next.

## Why It Matters

This attack crystallizes a threat the security community has warned about for years but that is only now arriving with full force: AI coding agents as a supply-chain attack surface.

Traditional malware needed a developer to download and execute a package. The new playbook requires only that a developer open a repository inside a tool like Claude Code or Gemini CLI — tools that by design read, index, and interpret repository contents automatically as part of the coding workflow. The attack surface has expanded precisely because these tools are more helpful. Every repository a developer opens in an AI agent is now a potential execution context for malicious configuration.

The implications ripple outward. Developers using AI coding tools at enterprise scale — which is to say, most modern software teams — are now part of a threat model that did not meaningfully exist two years ago. A compromised open source repository belonging to a company as visible and trusted as Microsoft is not a suspicious artifact that an experienced developer would think to quarantine. It is, or was, exactly the kind of dependency they would open without a second thought.

There is also a governance failure at the center of this story. Credential rotation is basic hygiene. That Microsoft apparently left the same GitHub Actions secrets in place weeks after a confirmed breach allowed a second, larger attack to unfold. For enterprises dependent on Microsoft's open source tooling, that lapse will be harder to ignore than the initial attack.

The Miasma campaign also signals a maturation of the TeamPCP threat group. The worm's ability to self-replicate across repositories using harvested credentials — spreading laterally through a victim's own GitHub organization — represents a meaningful step up in sophistication from static package poisoning.

## What to Watch

Several threads deserve close attention in the coming days and weeks. First, the customer notification scope: Microsoft has acknowledged reaching out to a "small number" of customers but has not defined what that means in absolute terms. Independent researchers estimate real developer exposure could be in the tens of thousands. The gap between those two figures will be a test of transparency.

Second, the response from AI coding tool vendors. Claude Code, Gemini CLI, Cursor, and VS Code were the delivery mechanism here — not by any fault of their own, but because their design makes them ideal attack vectors for configuration-file exploits. Watch for whether these tools introduce repository-level sandboxing, configuration-file scanning, or trust-on-open warnings as mitigations.

Third, policy and regulatory posture. The European Union's Cyber Resilience Act, which comes into full effect later this year, places new due-diligence requirements on software component integrity. This attack is exactly the scenario that act was written to address. Expect it to be cited in enforcement discussions.

Finally, watch whether TeamPCP escalates. The group has now successfully compromised targets ranging from open source JavaScript ecosystems to one of the world's largest cloud providers. The playbook is public, the tooling is open-sourced, and the results have been demonstrable. The Miasma worm is unlikely to be the last iteration.

---
*Sources: TechCrunch, SC World, The Register, BleepingComputer, Cloudsmith, StepSecurity, OpenSourceMalware, Rescana*
