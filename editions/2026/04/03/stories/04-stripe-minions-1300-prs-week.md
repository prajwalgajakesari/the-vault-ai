# Stripe's AI Minions Now Ship 1,300 Production Pull Requests Every Week

Stripe has crossed a significant milestone in autonomous software development. The payments infrastructure company's homegrown AI coding agents—nicknamed "Minions"—are now merging over 1,300 production pull requests per week, fundamentally reshaping how the company approaches developer productivity and code generation at scale.

Built on a customized fork of Block's open-source Goose coding agent, Minions operate completely unattended, executing tasks from conception to completion with no human interaction required until code review.

"A typical minion run starts in a Slack message and ends in a pull request which passes CI and is ready for human review, with no interaction in between," explained Alistair Gray, a software engineer on Stripe's Leverage team.

## Architecture Behind the Scale

Each Minion task runs on a devbox—a pre-configured AWS EC2 instance identical to those used by human engineers. These instances spin up from a warm pool in approximately 10 seconds. Each devbox is isolated from the internet and production systems. The infrastructure connects to Stripe's centralized Toolshed—an internal MCP server exposing over 400 tools.

Minions handle repetitive, well-defined tasks: dependency updates, consistent refactoring, API version migrations, and boilerplate generation. A built-in two-CI-run limit ensures tasks complete efficiently.

## Scale Without Compromise

Every single line of the 1,300 weekly pull requests has been reviewed and approved by human engineers before merging. The payment processing industry, where Stripe processes over $1 trillion in annual transaction volume, demands uncompromising reliability. Over 3 million automated tests run across Stripe's repositories.

## What Comes Next

The next frontier involves expanding Minions beyond well-defined tasks into more complex, multi-week initiatives. The real story is whether organizations can build AI systems that augment human judgment rather than replace it while scaling to thousands of production changes per week.