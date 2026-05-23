# Hadrian Releases Open Source OpenHack Tool for AI-Powered Vulnerability Discovery in Code

When Hadrian's security researchers pointed a commodity large language model at a dozen open-source applications used by Dutch government agencies, they did not use Anthropic's restricted Claude Mythos or any other frontier-only system. They used a structured workflow, a handful of instructions, and a harness that knew what to do with both. In a matter of hours, the analysis surfaced hundreds of vulnerabilities — including a critical-severity flaw that exposed server credentials and provided direct access to an underlying Azure database via an unauthenticated local file inclusion leading to remote code execution.

That demonstration was the proof of concept. On May 20, Hadrian released the methodology behind it: OpenHack, an open-source tool for AI-powered source code review, available immediately at github.com/hadriansecurity/openhack under the MIT License, running natively inside Claude Code, Codex, and Cursor.

## The Problem With Asking an AI to "Just Find the Bugs"

The temptation when giving a capable LLM access to a codebase is to let it improvise. Ask it to read the repo and report what looks vulnerable, and it will produce output — a mixture of plausible bugs, hallucinated bugs, real bugs explained incorrectly, and the occasional genuine insight. The triage burden that follows can take longer than reading the code yourself.

Hadrian's researchers identified two failure modes behind most of that noise. The first is unscoped prompts: when an agent doesn't know the specific question it's answering, it answers all of them at low confidence. The second is self-graded findings: the same agent that proposed a vulnerability gets to decide whether it's real, with no independent check.

OpenHack is designed to eliminate both. The tool enforces a scenario-first workflow: every unit of agent work is exactly one routing unit, one expert analyst, and one proof question. The agent that proposes a finding is not the agent that approves it. A separate triage agent evaluates each candidate against the original evidence before anything becomes a recorded finding.

"In today's offensive security landscape, AI-powered vulnerability discovery must transition from being a research curiosity to a commodity capability," said Rogier Fischer, co-founder and CEO of Hadrian. "We've been working on this for some time, but our discovery of critical vulnerabilities made it concrete. OpenHack's effectiveness proves that security teams don't need Mythos to find critical vulnerabilities."

## How a Run Unfolds

OpenHack operates as a file-based workspace and a set of agents that mirror how Hadrian's internal research team performs automated vulnerability discovery. Every run lives under a structured directory, and every important step writes a plain file — cloned source, recon output, routing units, scenario prompts, scenario results, finding candidates, triage decisions, final findings, logs. The full review is auditable end to end, and runs can be handed off to colleagues or resumed from any checkpoint.

The lifecycle moves through five phases. Reconnaissance crawls the source to generate routing units — the fundamental map of the attack surface, clustering noisy line-level findings into deterministic review surfaces like auth flows, parsers, and storage boundaries. Routing then pairs each surface with a specific expert and a specific proof obligation. Expert review runs each scenario independently, scoped to a single codebase section and a single security invariant. Independent triage evaluates every candidate finding for reportability, exploitability, and blast radius before anything is admitted to the final report. Validation then traces every final finding back through the complete chain of custody: recon item, routing unit, scenario, scenario result, finding candidate, triage decision, finding.

An optional Semgrep pass can enrich the recon phase with high-signal static analysis, though the tool treats those results as routing evidence rather than verified vulnerabilities — a distinction that reflects the workflow's broader philosophy of never skipping independent verification.

For users who prefer not to use the CLI, opening the repository in a coding harness and issuing a natural language instruction is enough. The harness reads AGENTS.md, initializes the run, summarizes each checkpoint, and prompts for human approval at every phase transition.

## Not a Frontier Model Problem

The release arrives against a backdrop of growing attention to AI-assisted security research, including Anthropic's Claude Mythos, which remains restricted due to its ability to surface previously unknown vulnerabilities at scale. The implicit assumption in that restriction — that dangerous capability requires frontier-scale compute — is exactly what Hadrian's work challenges.

"Attackers have workflows like this already, in one form or another," continued Fischer. "We'd rather hand defenders the same scaffolding we use internally than watch them re-derive it under pressure. Releasing OpenHack gives security teams a fighting chance to run the same kind of review against their own code before someone else does."

The Techzine analysis of the release put the point bluntly: OpenHack is model-agnostic and runs on commodity LLMs, yet it reached the same class of critical finding that Mythos-level systems are credited with. Whatever advantage defenders held in 2024 from the assumption that "attackers don't have access to good code-understanding tools" has, by Hadrian's accounting, already closed.

Mozilla separately reported that Mythos found 271 vulnerabilities with very few false positives in its own research. The contrast with OpenHack is instructive: the two approaches converge on similar quality outcomes from different directions — one through model scale, one through workflow architecture.

## A Responsible Release

Hadrian's decision to open-source the tool was not made lightly. The company noted in its blog post that the repository contains methodology, not weaponry: the agents are scoped, the workflow demands human approval at every phase transition, and the expert manifests describe attack techniques already well-documented in OWASP and MITRE references. The repository includes responsible disclosure guidance in SECURITY.md.

The expert families currently shipped with OpenHack cover the OWASP 2025 top vulnerability categories. Hadrian has deliberately implemented them as Markdown manifests rather than Python plugins — the bar for adding or sharpening an expert is writing prose about evidence requirements, not learning a class hierarchy. Future additions planned include infrastructure-as-code families and expanded evidence templates for cryptographic misuse.

OpenHack requires Python 3.9 or later. The repository includes the CLI, agent prompts, expert manifests, file schemas, and full documentation. Hadrian says further vulnerability disclosures from its internal research, conducted using the methodology now public in OpenHack, are expected in the coming months.

The release is a direct argument that the security community's preparedness gap is not a model access problem. It is a workflow problem — and Hadrian is proposing that the solution is now free to use.
