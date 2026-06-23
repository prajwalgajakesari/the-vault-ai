For most of the past year, the dirty secret of agentic coding has been the same one that has dogged large language models since the beginning: they forget. Point an AI agent at a sprawling codebase and let it grind for a few hours, and somewhere in the third or fourth hour the context window fills, earlier reasoning gets compressed or evicted, and the agent starts making confident decisions on a corrupted memory of what it already did. This month, Boris Cherny, the Claude Code lead at Anthropic, shipped an experimental fix for exactly that failure mode — and quietly broke one of his own design rules to do it.

In version 2.1.172, released June 9, Cherny enabled **nested subagents**: a parent agent can now delegate a subtask to a child agent, which can in turn spawn its own children, down to a hard ceiling of five levels. Until now, Claude Code allowed subagents but forbade them from spawning more subagents, keeping delegation flat. The new hierarchy turns that flat structure into a tree.

## How the hierarchy works

The mechanism is deceptively simple, and it is fundamentally about context, not parallelism. Each subagent runs in its own isolated context window and returns only a compact summary of its work to its parent. That means a deeply nested task — say, refactoring a module, which requires reading a dozen files, which each require tracing a function call — can push the noisy, token-heavy exploration work down to a child agent whose window fills and is discarded, while the parent's window stays clean and focused on the decision that actually matters.

"Agents kicking off agents as a way to better manage context," is how Cherny framed the motivation. The point, as observers who tested the feature noted, is not to run more agents at once but to push low-value work further away from the conversation a developer actually cares about. Each new layer of nesting buys another fresh context window before the previous one overflows.

Cherny has been explicit that the five-level cap is a starting point rather than a finished design, asking users for feedback on whether the ceiling feels too tight or about right in real workflows. In his own widely circulated configuration notes, he advises developers to "append 'use subagents' to any request where you want Claude to throw more compute at the problem" and to "offload individual tasks to subagents to keep your main agent's context window clean and focused."

## A second update tightens the guardrails

Nested subagents arrived alongside a separate and arguably more consequential change for teams running Claude Code unattended. In version 2.1.183, released June 18, Anthropic hardened the safety of auto mode against irreversible commands.

The agent will now **block destructive git operations** — `git reset --hard`, `git checkout -- .`, `git clean -fd`, and `git stash drop` — unless the user has explicitly asked to discard local work. It also blocks `git commit --amend` on commits the agent did not create in the current session. On the infrastructure side, `terraform destroy`, along with the Pulumi and CDK equivalents, is now blocked unless the specific target stack has been explicitly requested.

The change reads as a direct response to a class of incident that has become a recurring nightmare as autonomous agents get more rope: an agent, trying to "clean up" a working tree or tear down what it thinks is a stale environment, wipes uncommitted work or destroys live infrastructure. Documented "terraform destroy" mishaps had already circulated widely in the community before the fix landed.

## Why It Matters

The timing is pointed. A Black Duck study published June 9, drawing on a UserEvidence survey of 831 developers, found that **97% of developers now use AI coding tools** — but only about a third of organizations have a fully governed oversight process around them. GitHub Copilot leads adoption at 83%, with Claude Code close behind at 63%, and most teams run several assistants at once.

The productivity case is no longer in doubt: 92% of respondents credit AI assistants with faster releases, and developers report saving roughly eight hours a week. But the study's sharpest finding is that governance is a force multiplier, not a tax — 90% of fully governed teams report major gains, versus just 44% of ungoverned ones. Meanwhile 90% of teams hit problems with AI-generated code, and 64% report moderate-to-extreme concern about security defects.

Read together, the two Claude Code updates map almost perfectly onto that gap. Nested subagents push capability — longer, more ambitious autonomous sessions. The auto-mode blocks push governance — fewer ways for an unsupervised agent to do irreversible damage. The market is rewarding teams that ship both at once, and Anthropic appears to be betting that the tool itself, not just corporate policy, should carry some of that governance burden.

## What to Watch

Three things. First, whether the five-level cap holds: Cherny has invited feedback, and the depth limit is the kind of number that tends to move once real workloads reveal whether nesting prevents context loss or simply creates harder-to-debug chains of delegation where a summary three levels down quietly drops a critical detail.

Second, whether nested subagents actually reduce the compression errors they are meant to fix, or relocate them. Summarization at each boundary is itself lossy; a five-level tree has five places for nuance to leak out.

Third, whether the destructive-command blocks become a template. If Anthropic extends the deny-by-default posture to more irreversible operations — database drops, force pushes, package publishes — auto mode starts to look less like a power-user toggle and more like the governed default that two-thirds of organizations currently lack. For a market where adoption has hit 97% and oversight has not, that may be the more important shift.

---

**Sources:** [Digg](https://digg.com/ai/megudrsi), [Claude Code changelog](https://code.claude.com/docs/en/changelog), [Claude Code v2.1.183 release notes (DevelopersIO)](https://dev.classmethod.jp/en/articles/20260619-cc-updates-v2-1-183/), [Black Duck / PR Newswire](https://www.prnewswire.com/news-releases/ai-coding-hits-97-enterprise-adoption-new-black-duck-study-shows-governance-is-the-roi-multiplier-302794103.html), [SD Times](https://sdtimes.com/ai/ai-coding-adoption-rate-hits-97-black-duck-study-reveals/), [Boris Cherny on Threads](https://www.threads.com/@boris_cherny/post/DUMZy85EoFj/).
