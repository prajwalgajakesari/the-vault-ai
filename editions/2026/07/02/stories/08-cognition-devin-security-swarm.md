---
headline: "Cognition Launches Devin Security Swarm, an Agent System That Hunts Bugs Across Whole Codebases"
slug: cognition-devin-security-swarm
category: llms-genai
story_number: "08"
date: "2026-07-02"
sources:
  - name: "Cognition Blog — Introducing Devin Security Swarm"
    url: "https://cognition.com/blog/introducing-devin-security-swarm"
  - name: "Devin Blog — Agentic MapReduce"
    url: "https://devin.ai/blog/agentic-map-reduce"
  - name: "Devin Blog — Evaluating Security Swarm"
    url: "https://devin.ai/blog/security-swarm-eval"
  - name: "PR Newswire — Cognition Launches Devin Security Swarm"
    url: "https://www.prnewswire.com/news-releases/cognition-launches-devin-security-swarm-to-tackle-the-vulnerability-backlog-302814800.html"
---

# Cognition Launches Devin Security Swarm, an Agent System That Hunts Bugs Across Whole Codebases

Cognition, the AI lab behind the software-engineering agent Devin, on July 1 unveiled Devin Security Swarm, a "Devin for Security" system that turns loose a coordinated fleet of agents on an entire codebase to find exploitable vulnerabilities, prove they are real inside a sandbox, and open a pull request to fix them. It is a direct bid to solve a problem that the AI coding boom created in the first place: security teams are drowning in findings they cannot act on.

The pitch is timing as much as technology. As AI writes an ever-larger share of production code, scanners are surfacing far more potential flaws than humans can triage. Cognition says some enterprises have watched monthly security findings climb from roughly 1,000 to more than 10,000 in six months, driven in part by the estimated 42% of code now generated or assisted by AI. Many of those findings are false positives, and traditional tooling has no way to tell a security lead which ones actually matter.

"Devin Security Swarm gives security teams engineering capacity they've never had," said Nick Wong, Security Engineering Lead at Cognition. "Now, security teams can validate which vulnerabilities are actually exploitable and fix them directly, instead of handing findings to engineering and waiting."

## How the Swarm Works

The system runs on a new architecture Cognition calls Agentic MapReduce, a pattern borrowed conceptually from distributed computing but rebuilt around reasoning agents. A planner agent first studies the repository and writes what Cognition calls *selectors*: deterministic relevance tests tuned to that specific codebase, such as its route declarations, authentication boundaries, and deserialization sinks. Crucially, those selectors run over every file with no model in the loop, so files that match nothing get dropped before any agent looks at them. That, the company argues, guarantees coverage "by construction" while keeping compute costs down.

Matches are then batched and handed to child agents that investigate in parallel, each reasoning over one bounded shard from a focused context window. A final reducer agent dedupes the results and reasons across shards to assemble attack paths no single worker could see, for instance combining an unauthenticated ID leak with an ID-gated remote-code-execution bug into a single P0. Every serious finding is reproduced in an isolated sandbox against a running build before it reaches the security team, so the report reflects runtime-verified exploits rather than static guesses. After Devin confirms a vulnerability, it writes the patch and opens a PR for review.

## The Eval: 72% Recall at $90 a Run

Cognition's central claim rests on a benchmark it built and published in the open. The lab argues that off-the-shelf security benchmarks use synthetic bugs unlike real code, and that vendor numbers "quote recall we can't audit for false positives or reproduce independently."

So it assembled 50 real, recent vulnerabilities across 14 languages, including Go, Rust, Python, Ruby, Java, C#, JavaScript, C, Swift, PHP, Elixir, Erlang, Kotlin, and Dart. Every case is tied to a published GitHub Security Advisory, with each repository pinned to the last commit before the bug was patched. Critically, every advisory was published *after* the training cutoffs of the models tested, and Cognition says it reviewed agent trajectories to confirm the systems did not simply look up the CVEs. The idea is that a hit reflects genuine reasoning about unseen code, not recall of a memorized answer.

On that dataset, Devin Security Swarm found the target vulnerability in 36 of 50 cases, or 72% recall, at an average of $90.23 per run. Cognition reports that beat every other AI security analyzer it tested: Claude Security hit 68% at $131.87, Codex Security 48% at $118.20, and Cursor Security 26% at $4.60. In other words, Security Swarm claims the highest detection rate at roughly two-thirds the cost of the next-most-accurate tool.

Three critical vulnerabilities were found only by Devin and missed by every other tool: a PHP sandbox bypass via template injection, an argument injection through metadata value parsing, and an overly broad deserialization surface in Spring Kafka. Cognition also concedes a nuance in its favor: because its grading requires the *specific* labeled bug, runs that surfaced other real, unreported vulnerabilities in the right file still scored zero, so it frames 72% as a floor on detection rather than a ceiling.

## Why It Matters

The launch lands in an increasingly crowded market for agentic security. XBOW, founded by CodeQL and GitHub Copilot creator Oege de Moor, made headlines in 2025 when its autonomous agent topped HackerOne's US bug-bounty leaderboard and drew an investment from Accenture. A wave of tools from Escape, Terra Security, Hadrian, and others is chasing the same premise, while incumbents like Semgrep represent the fast, cheap, static-analysis status quo that agentic systems aim to displace.

What distinguishes Cognition's play is where it sits. XBOW attacks running applications from the outside like a pentester; Security Swarm reads source code from the inside and, because it is built on Devin, closes the loop by shipping the fix. That end-to-end remediation is the strategic wedge. The bottleneck in enterprise security has never been finding flaws so much as validating and fixing them, and a tool that opens a mergeable PR collapses the hand-off between security and engineering that Wong describes as the core pain.

The cost curve matters too. Cognition says the first full scan establishes a baseline, and subsequent scans process only changed code, so per-run cost falls over time, an economic model that makes continuous, scheduled scanning plausible rather than a once-a-quarter luxury. The obvious caveat: these are vendor-reported numbers on a vendor-built benchmark, and the false-positive rate, the thing that made scanner fatigue a crisis in the first place, is explicitly not measured by a recall-only eval.

## What to Watch

The proof will be in production. Cognition says Security Swarm is already used by major companies for regular scanning and is generally available to enterprise customers now, alongside a six-week Vulnerability Remediation Program in which Cognition's forward-deployed engineers embed with customers to burn down CVE backlogs. Watch for independent, third-party reproductions of the 72% figure, real-world false-positive rates once the swarm runs against messy monorepos, and how many of its auto-generated remediation PRs teams actually trust enough to merge. If the answers hold up outside the benchmark, agentic security may finally start closing the backlog that agentic coding opened.
