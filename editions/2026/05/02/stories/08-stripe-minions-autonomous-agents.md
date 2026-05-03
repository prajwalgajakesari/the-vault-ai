---
headline: "Stripe Minions Ship 1,300 Pull Requests Per Week as Autonomous Coding Agents Scale"
slug: stripe-minions-autonomous-agents
category: llms-genai
story_number: "08"
date: 2026-05-02
---

# Stripe Minions Ship 1,300 Pull Requests Per Week as Autonomous Coding Agents Scale

At Stripe, an engineer tags a bot in Slack with a bug report or feature request. Ten seconds later, a cloud machine spins up pre-loaded with Stripe's entire codebase. An AI agent reads the ticket, gathers context from internal documentation and Sourcegraph, writes the code, runs linters and a selective battery from more than three million tests, and opens a pull request -- all before the engineer finishes their coffee. No human touches a keyboard until the code review stage. Stripe calls these agents Minions, and they now ship more than 1,300 merged pull requests every week.

That number, disclosed by the Stripe engineering team and confirmed by infrastructure lead Steve Kaliski on the Lenny's Podcast "How I AI" series, represents one of the highest sustained volumes of autonomous, agent-written code changes at any private technology company. The figure has been growing at roughly 30 percent week over week, climbing from around 1,000 PRs to 1,300 in under two weeks during the system's ramp-up phase. These are not autocomplete suggestions or copilot-style inline completions. Each pull request is a full, end-to-end code change -- branched, written, tested, and submitted for human review without a single line typed by a developer.

## Built on Block's Goose, Rebuilt for Autonomy

Minions run on a heavily modified internal fork of Block's open-source Goose coding agent. Stripe's engineering team stripped out everything designed for interactive human use -- confirmation dialogs, interruptibility hooks, human-triggered commands -- and rebuilt the harness for fully unattended, one-shot execution. The term "one-shot" is deliberate: each Minion receives a task, executes it from start to finish in a single autonomous run, and either produces a clean pull request or reports failure. There is no back-and-forth conversation with a developer mid-task.

The underlying infrastructure makes this possible. Stripe provisions what it calls "devboxes" -- standardized AWS EC2 instances loaded with the full source tree, warmed Bazel and type-checking caches, and code generation services. These machines are drawn from a pre-warmed pool, allowing a new agent environment to be ready in under ten seconds. Because devboxes run in a QA environment already isolated from production data, agents operate with full permissions and no confirmation prompts, eliminating the friction that slows down interactive coding assistants.

## Blueprints: Where Determinism Meets Agency

The architectural innovation at the heart of Minions is what Stripe calls Blueprints -- orchestration flows that alternate between fixed, deterministic code nodes and open-ended agent loops. Drawing on patterns described in Anthropic's "Building Effective Agents" framework, Blueprints fuse workflows and agents into a single execution graph. Deterministic nodes handle predictable operations like git branching, running linters, and executing specific test suites. Agent nodes handle the creative, ambiguous work: reading a Jira ticket, understanding intent, searching the codebase, and writing the actual code.

Before the LLM even activates, a deterministic orchestrator prefetches context by scanning the Slack thread for links, pulling Jira ticket details, finding relevant documentation, and querying Sourcegraph for related code. This context is assembled and handed to the agent node, which dramatically reduces hallucination and wasted inference cycles. Stripe also built a central internal MCP server called Toolshed that hosts over 400 tools spanning internal systems and SaaS platforms, giving Minions structured access to the full breadth of Stripe's developer ecosystem.

## CI/CD as the Quality Gate

Quality control is baked into the pipeline rather than bolted on afterward. A local executable runs selected lints on each git push in under five seconds using heuristics. If that passes, CI selectively runs tests from Stripe's battery. The system allows at most two CI rounds to balance speed, cost, and diminishing returns -- if the code does not pass after two attempts, the Minion reports failure rather than burning compute in an infinite retry loop. What comes out the other end is a clean pull request following Stripe's exact templates, with a green CI build, ready for human review.

## Not a Copilot -- a Colleague That Works Overnight

The distinction between Minions and copilot-style assistants is fundamental, not incremental. GitHub Copilot and similar tools operate as real-time typing assistants embedded in an IDE, suggesting completions as a developer writes code. Minions operate asynchronously and autonomously. A developer fires off a task via Slack and can walk away entirely. The agent works in the background -- often overnight or in parallel with dozens of other Minions -- and the developer returns to a finished pull request awaiting review.

This model changes the economics of software development. Even if a Minion only gets a task 80 percent right, it eliminates a massive amount of boilerplate and routine work. The human reviewer focuses on architecture, edge cases, and business logic rather than writing the initial implementation. Stripe's engineers are effectively becoming reviewers and architects rather than line-by-line coders for an expanding category of tasks.

## What This Means for the Industry

Stripe's Minions represent the clearest evidence yet that autonomous coding agents are moving from experiment to production infrastructure. The 1,300 PRs per week figure is not a demo or a benchmark -- it is sustained, production-grade output at one of the world's most technically rigorous fintech companies. The implications ripple outward. If Stripe can achieve this with a modified open-source agent framework, every company with a large codebase and a strong CI/CD pipeline has a template to follow.

The Blueprints architecture is particularly significant. By combining deterministic guardrails with agentic flexibility, Stripe has found a middle path between fully autonomous agents that hallucinate wildly and rigid automation that cannot handle ambiguity. Expect this pattern -- deterministic scaffolding around agentic cores -- to become the default architecture for enterprise coding agents over the next twelve months.

## What to Watch Next

Three developments deserve attention. First, whether Stripe open-sources any portion of its Blueprints framework or Toolshed MCP server, which would accelerate adoption across the industry. Second, how the acceptance and merge rate of Minion-authored PRs evolves as the system tackles increasingly complex tasks beyond migrations, boilerplate, and bug fixes. Third, whether competing approaches from companies like Google, Amazon, and Microsoft converge on similar one-shot, asynchronous architectures or chart a different course. The race to ship autonomous coding at enterprise scale is no longer theoretical. Stripe is already running it in production.
