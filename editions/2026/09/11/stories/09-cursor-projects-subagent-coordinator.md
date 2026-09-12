# Cursor's Coordinator Agent Farms Work Out to Thousands of Subagents

Cursor spent four years teaching developers to accept a suggestion. This week it started asking them to hand over a quarter's worth of work instead.

Anysphere shipped **Projects** in beta on September 10, 2026: a persistent workspace fronted by a single *coordinator* agent that plans multi-PR bodies of work, delegates them to subagents, and keeps grinding on a cloud machine long after the laptop lid closes. The coordinator never touches the code. It reads the repo, writes a plan, spawns workers, and brings finished pull requests back for review. Cursor claims the pattern scales to thousands of concurrent subagents, and it landed the same day OpenAI pushed its own Agents API into public beta — putting the managed Codex harness, hosted sandboxes and subagent orchestration behind one API call.

The design rests on one deliberate constraint: the thing you talk to never has its hands full.

The coordinator doesn't write code itself but directs other agents that do, wrote Cursor's Alexi Robbins and Fredrika Lindh in the launch post. Because it delegates rather than executes, they argue, it is never blocked and is always responsive to direction — you can interrupt it mid-migration and it answers immediately, because it was never the one waiting on a test suite.

Three capabilities hold the thing together. Projects run cloud-first on dedicated machines, spinning up a local agent only when something needs the developer's own environment. Each Project keeps a set of shared context files that sync across every machine its agents touch, so the agent that figured out how to boot a service last Tuesday leaves instructions for every agent after it. And *subscriptions* let a coordinator watch a Slack channel, follow every open PR, fix failing CI, or simply run on a schedule — acting on signals rather than prompts.

Andrew Milich of Cursor compressed the pitch to a sentence on X: Work with a single agent across multiple PRs, with subscriptions, a shared filesystem, and memory. Colleague Fatih Arslan offered a more grounded number than the marketing one, saying his coordinators manage tens of agents each across local, remote and cloud machines.

## The numbers, and what they are not

Cursor has been dogfooding Projects for months on framework migrations spanning hundreds of PRs and on what it calls *gardening* — the maintenance work that never ends. One internal design-system Project now scans every incoming PR, extracts components that belong in the shared library, and writes a new lint rule whenever it sees the same mistake twice. Cursor says it is on track to touch 20 to 100 PRs a day with one engineer checking in where attention is needed.

Then come the headline figures: new users merge **30% more PRs**, and users who lean primarily on Projects merge **six times as many**.

Those are self-reported, unaudited, and published without a baseline, a cohort size, or a time window. They also have a selection problem at their center. Developers who reorganize their whole workflow around a beta orchestration layer are not a random sample — they skew toward people already running migrations, already shipping in small reviewable increments, already working in high-volume repos with strong CI. A 6x gap between people who committed and people who dabbled measures commitment at least as much as it measures the tool. Cursor has published a correlation and invited everyone to read it as a cause.

PR count is also a load-bearing metric doing work it was not built for. Merged PRs measure throughput of artifacts, not shipped value. A coordinator instructed to keep each PR under 300 lines will mechanically produce more PRs for the same feature. If the migration that used to be one enormous diff is now forty small ones, the counter goes up and nothing about the software changed.

## The bottleneck just moved downstream

The more interesting shift is architectural. Autocomplete put a human in the loop on every token. Chat-based agents put a human in the loop on every task. A coordinator fanning out to hundreds of workers puts a human in the loop on every *batch* — and human review does not parallelize. Cursor's own migration guidance describes the trust curve explicitly: review each PR closely at first, then review less as the fixes hold up. Some engineers on the Cursor team already let their Projects merge their own PRs and review afterward. That is a reasonable risk posture for a styling migration and a genuinely alarming one for anything with money in it.

Then there is the bill. Developer Flavio Copes, who spent launch day with the feature, was blunt about the economics: A coordinator that fans out to hundreds of subagents consumes a ton of tokens, and I prefer working on one thing at a time, under more control, where I can read what the agent is doing while it does it. Cursor's own guidance puts daily agent users at $60 to $100 a month and anyone running multiple agents at $200 or more — against a Pro plan that starts at $20, with Pro+ at $60, Ultra at $200 and Teams seats at $40 per user. Fanning out to thousands of subagents is a pricing event, not just a product feature. Cursor has also not documented how a months-long coordinator thread avoids context bloat, which is the load-bearing technical question nobody has answered.

Copes drew the line most teams will end up drawing: gardening yes, migrations yes, anything touching payments no.

Watch three things. Whether Cursor publishes methodology behind the 6x claim, or quietly retires it. Whether review tooling — Cursor's own Bugbot included — scales fast enough to absorb 20 to 100 machine-authored PRs a day without turning approval into a rubber stamp. And whether the coordinator abstraction survives contact with teams that do not live in PRs at all. Cursor, GitHub, Devin, OpenHands and Claude Code are all converging on the same primitives now. The architecture is no longer the differentiator. The review bottleneck is.
