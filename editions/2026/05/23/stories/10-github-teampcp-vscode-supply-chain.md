# GitHub Confirms 3,800 Internal Repositories Breached Via Poisoned VS Code Extension

*A single malicious update — live for just 18 minutes — was enough for TeamPCP to walk through the front door of one of the internet's most critical software platforms.*

---

GitHub officially confirmed on May 21, 2026 that roughly 3,800 of its own internal repositories had been exfiltrated by TeamPCP, a prolific cybercriminal group with a growing portfolio of supply chain devastation. The breach originated from a single GitHub employee's workstation. The entry point: a poisoned version of Nx Console, a widely used Visual Studio Code extension with more than 2.2 million installs, that was live on the Visual Studio Marketplace for just 18 minutes before it was caught. Eighteen minutes was all it took.

The incident is not just a breach of a major technology company. It is a stark demonstration that the software supply chain — the invisible scaffolding of extensions, packages, and plugins that developers trust daily — has become the most exploited attack surface in enterprise security.

## How the Attack Unfolded

The chain of compromise began before GitHub was ever in the picture. TeamPCP had previously compromised a developer at TanStack, a popular JavaScript library ecosystem. That breach yielded credentials that were then used to compromise a maintainer at Narwhal Technologies, the company behind the Nx framework and Nx Console. With those stolen credentials, the attackers pushed a malicious update — version 18.95.0 of the `nrwl.angular-console` VS Code extension — to the official Visual Studio Marketplace on May 18, 2026, at 12:30 p.m. UTC. It was pulled at 12:48 p.m. UTC, 18 minutes later, but the damage was already in motion.

According to OX Security researcher Nir Zadok, the trojanized extension was designed to be nearly invisible. "The extension looked and behaved like normal Nx Console, but on startup it silently ran a single shell command that downloaded and executed a hidden package from a planted commit on the official nrwl/nx GitHub repository," Zadok said. "The command was disguised as a routine MCP setup task so it would not raise suspicion."

The malware functioned as a credential harvester, silently exfiltrating secrets from 1Password vaults, Anthropic Claude Code configurations, npm tokens, GitHub credentials, and Amazon Web Services keys. A GitHub employee had Nx Console installed. Their credentials were among those swept up. From there, TeamPCP had what they needed to access GitHub's internal repositories.

GitHub moved fast once the breach was detected. The company isolated the affected endpoint, removed the malicious extension version, and rotated critical secrets — prioritizing the highest-impact credentials first. "We have no evidence of impact to customer information stored outside of GitHub's internal repositories, such as our customer's own enterprises, organizations, and repositories," Alexis Wales, GitHub's Chief Information Security Officer, said in a published statement. "Some of GitHub's internal repositories contain information from customers, for example, excerpts of support interactions. If any impact is discovered, we will notify customers via established incident response and notification channels."

## The Blind Spot That TeamPCP Keeps Exploiting

Security researchers were quick to point out that this breach is a symptom of a systemic failure in how organizations think about developer security. Aikido Security's Mackenzie Jackson was blunt in his assessment: "Developer workstations are the number one target in supply chain attacks right now, and this is exactly why. TeamPCP has compromised Trivy, Checkmarx, Bitwarden CLI, TanStack, and now GitHub, all in 2026, all through developer tooling. A single VS Code extension on one employee's machine was enough to get access to 3,800 internal GitHub repositories. Most security teams still have zero visibility into what extensions or packages are on their developers' machines, or how recently they were published. That's the blind spot these attacks keep walking through."

The auto-update feature that ships with VS Code by default was also singled out as a structural vulnerability. Aikido researcher Raphael Silva explained the core problem: "Every popular extension marketplace ships with auto-update on by default. VS Code, Cursor, the whole lineup. The reasoning makes sense in isolation, because most developers never update anything manually, so leaving it off means a long tail of editors running stale, vulnerable code. The trade-off stops making sense once you account for hostile or compromised publishers. Auto-update gives an attacker who controls a release a direct push channel into every machine running that extension. Marketplaces don't impose any review gate or waiting period between when an update is published and when installed clients pull it in."

This is not a theoretical problem. The community spotted the malicious Nx Console update in 11 minutes — faster than GitHub's own detection — but even that response time meant thousands of developers had already received the update automatically.

## TeamPCP's Supply Chain Playbook

TeamPCP, also tracked as UNC6780, has spent 2026 systematically dismantling trust in open-source development infrastructure. Their targets have included Aqua's Trivy vulnerability scanner, Checkmarx's KICS infrastructure-as-code analyzer, the LiteLLM library, the Telnyx SDK, TanStack, Mistral AI, and Grafana Labs. The pattern is consistent and deliberate: compromise a widely trusted tool used by security or AI developers, harvest credentials from every machine that installs the infected version, then use those credentials to compromise the next link in the chain.

The Nx Console attack is a textbook example of this compounding logic. A TanStack compromise yielded credentials that unlocked an Nx maintainer. The Nx compromise yielded the credentials of a GitHub employee. The GitHub employee's credentials yielded 3,800 internal repositories. The group has since advertised the stolen data on an underground cybercrime forum, seeking at least $50,000 from potential buyers, and has threatened to publicly release the material if no sale materializes.

Jeff Cross, co-founder of Narwhal Technologies, addressed the structural failings that made this possible. "This incident highlights that there need to be deeper, more fundamental changes to how we and other maintainers need to think about securing developer tooling and open source distribution," he wrote on X. "We're also beginning conversations with other high-profile open source maintainers about how we can work together on some of the deeper structural problems around software supply chain security. A lot of the assumptions the ecosystem has operated under for years no longer hold."

The scale of the developer exposure is still being determined. Microsoft initially estimated only 28 installs of the malicious version, but Cross's own analytics suggested the real number may have been significantly higher — potentially over 6,000 installs — underscoring just how fast an 18-minute window of exposure can move through the auto-update pipeline.

## What Has to Change

The GitHub breach arrives at a moment when the security community has been escalating warnings about the developer tooling attack surface for years, with little systemic response. VS Code extension permissions are effectively unrestricted: an installed extension runs with full access to a developer's file system, environment variables, SSH keys, cloud credentials, and any secrets in memory. There is no permission sandbox, no credential isolation, no mandatory delay between a publisher pushing an update and clients receiving it.

Charlie Eriksen, a security researcher at Aikido Security, made the operational consequence explicit: "The thing people underestimate about VS Code extensions is that they have full access to everything on the developer's machine. EDR doesn't cover this layer at all. What's missing for most organizations is any kind of visibility into what's actually running on developer machines and the ability to control it."

The immediate policy levers are not complicated to identify. Marketplace review gates that impose even a short mandatory delay between publication and distribution would have stopped this attack. Signed, verified extension releases with publisher identity attestation would raise the cost of a compromised account. Sandboxed extension permissions — the kind that mobile app ecosystems have enforced for over a decade — would limit blast radius even when an extension is fully malicious. The technical solutions exist. What has been missing is the urgency to deploy them.

GitHub has promised a full incident report when its investigation concludes. The broader question is whether this breach — the most visible supply chain attack to hit a major platform in recent memory — is finally the incident that forces the developer tooling ecosystem to treat extension security with the same rigor applied to application security. If it is not, TeamPCP's next campaign already has a template.

---

*Sources: The Hacker News, Help Net Security, CyberScoop, SecurityWeek*
