# OpenAI Launches $25K Bio Bug Bounty to Stress-Test GPT-5.5 Safety

OpenAI is putting a price on its own model's vulnerabilities. The company announced on April 23 a restricted Bio Bug Bounty program that will pay up to $25,000 to the first security researcher who can devise a universal jailbreak capable of bypassing GPT-5.5's biosafety guardrails -- a move that marks one of the most targeted and high-stakes red-teaming exercises ever conducted on a frontier AI system.

The challenge is deceptively simple in description but formidable in practice: participants must craft a single prompt that can defeat all five questions in a curated bio safety challenge, starting from a clean chat session with no prior context. The first person to demonstrate a complete, reproducible universal jailbreak walks away with the top prize. OpenAI has indicated it may also issue smaller discretionary awards for partial successes.

## A Controlled Hunt for Dangerous Gaps

Unlike traditional bug bounties that cast a wide net across a product's attack surface, OpenAI's Bio Bug Bounty is surgically narrow. The program is invitation- and application-only, restricted to researchers with vetted backgrounds in AI red teaming, cybersecurity, or biosecurity. All participants must hold existing ChatGPT accounts and sign a non-disclosure agreement. Every prompt, model output, and finding produced during the program remains under NDA.

Testing is confined to a single environment: GPT-5.5 running on Codex Desktop. Applications opened April 23 with rolling acceptances and close June 22, 2026. The testing window runs from April 28 through July 27, giving accepted researchers a full three months to probe the model's defenses.

"In our ongoing work to strengthen our safeguards for advanced AI capabilities in biology, we're inviting researchers with experience in AI red teaming, security, or biosecurity to try to find a universal jailbreak," OpenAI said in its announcement of the program.

## What Pre-Release Testing Already Found

The bounty program does not exist in a vacuum. It complements a battery of pre-deployment safety evaluations documented in the GPT-5.5 system card, which OpenAI published alongside the model's launch. The company subjected GPT-5.5 to its full Preparedness Framework, including targeted red-teaming for advanced biology and cybersecurity capabilities, and collected feedback from nearly 200 early-access partners before release.

External assessors were part of the process as well. SecureBio, an independent biosecurity organization, evaluated two pre-release checkpoints of GPT-5.5 between April 2 and April 9. The group found that GPT-5.5 exceeded state-of-the-art scores on the Virology Capabilities Test, surpassing every other model SecureBio has tested. While the checkpoints "consistently recognized high-risk prompts and refused to provide in-depth, practical assistance," SecureBio flagged a critical caveat: the organization did not systematically test how robust those mitigations are to jailbreaking.

"Given that uncertainty, the models' strong high-level reasoning capabilities, and the models' blind spots on dual-use topics, we conclude that the models' potential for facilitating sophisticated planning by expert actors remains a critical biosecurity consideration," SecureBio wrote in its pre-release assessment.

That candid admission helps explain why OpenAI is now offering cash for exactly the kind of adversarial testing SecureBio did not perform.

## Red Teaming as an Emerging Industry Standard

The Bio Bug Bounty sits within a broader shift across the AI industry toward structured adversarial testing. OpenAI already operates separate Safety Bug Bounty and Security Bug Bounty programs for researchers interested in broader vulnerability work. Anthropic, Google DeepMind, and Meta have all established their own red-teaming pipelines, and the White House's October 2023 executive order on AI safety explicitly encouraged frontier labs to adopt pre-deployment adversarial evaluations.

But the GPT-5.5 bounty pushes the concept further in two important ways. First, it narrows the scope to a single, high-consequence domain -- biology -- rather than treating safety as a monolithic category. Second, it defines success in binary terms: either a universal jailbreak exists, or it does not. That clarity transforms red teaming from a qualitative exercise into something closer to a falsifiable experiment.

The approach is not without critics. Some biosecurity researchers have argued that offering financial incentives to break biological safety guardrails -- even under NDA -- risks normalizing the search for dangerous prompts and could produce techniques that eventually leak. Others counter that if a universal jailbreak exists, it is better discovered by vetted researchers under controlled conditions than by bad actors in the wild.

## What It Means for the Field

The program's design reveals how OpenAI is thinking about safety at the frontier. Rather than relying solely on internal evaluations and third-party audits, the company is building a layered defense that includes financial incentives for external adversaries. Each major model release is now paired with a public-facing safety document and a targeted red-teaming exercise -- a launch routine that treats safety evaluation as an ongoing process rather than a one-time gate.

For the broader AI ecosystem, the Bio Bug Bounty sets a precedent. If a $25,000 prize is enough to surface a universal jailbreak in GPT-5.5, it will validate the model and demonstrate that relatively modest investments in structured adversarial testing can yield high-confidence safety assurances. If no one claims the prize, it provides a different kind of evidence: that the model's biosafety guardrails withstood three months of focused attack by credentialed specialists.

Either outcome produces information the field badly needs as AI models grow more capable in sensitive domains. The testing window opens April 28. The clock starts then.
