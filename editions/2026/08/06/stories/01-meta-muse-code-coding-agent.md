Meta has finally planted a flag in the fastest-moving corner of enterprise AI. On Wednesday, August 6, 2026, the company released **Muse Code** in beta, a terminal-based coding agent aimed squarely at developers working across sprawling software repositories. It is Meta's first dedicated AI coding agent, and the company is not being coy about the target: Muse Code is priced and positioned to undercut Anthropic's Claude Code and OpenAI's Codex, the two tools that have come to define the agentic-coding category.

The launch arrives with a new model underneath it. Muse Code runs on **Muse Spark 1.2**, a coding-focused model Meta says it co-trained alongside the agent so the two are tuned to work together. The pitch is end-to-end autonomy: the agent can take on complete software engineering tasks across large codebases, from planning the change, to writing the code, to validating the result.

## What Meta shipped

Muse Code installs from the command line with a single command and is available in beta for macOS and Linux. Its headline capability is parallelism. Rather than working a large task in a single thread, the agent spins up its own sub-agents that run simultaneously in isolated environments, so multiple pieces of work advance at once without stepping on each other.

Meta CEO Mark Zuckerberg described the mechanic directly in a post announcing the tool. "When a job is big enough, it fans out to separate sub-agents working in parallel in isolated worktrees," he wrote. "Your working copy is never touched. In testing we had it build six features for a game simultaneously with no collisions." Zuckerberg added that Muse Code can accomplish "complete software engineering tasks across large repos," including "planning changes, writing code, validating the results."

The most distinctive part of the release, though, is the price sheet. Muse Code ships with two tiers. The standard, pay-as-you-go tier is priced at roughly **$1.25 per million input tokens** and **$4.25 per million output tokens**, with cached input at $0.15 per million. The second, a "contributor" tier, slashes those numbers to **$0.10 per million input tokens** and **$0.20 per million output tokens**, with cached input at just $0.002 per million. The catch: developers on the contributor tier must consent to Meta using their prompts and completions to train its models. On output tokens, that discount works out to more than a 20x price cut in exchange for handing over your data.

## The benchmarks, and the caveats

On performance, Meta's launch charts put Muse Spark 1.2 at **59.3% on DeepSWE 1.1**, a coding benchmark, which the company frames as a 6.3-point improvement over the prior Spark 1.1 release. Notably, Meta's own published comparisons place Anthropic's Claude Opus 5 ahead on all three coding benchmarks it disclosed, including an internal test Meta designed itself. In other words, Meta is not claiming the best model. It is claiming the best deal.

That framing came straight from the top of Meta Superintelligence Labs. Alexandr Wang, Meta's AI chief who leads the lab, told the Wall Street Journal that the distinction is cost, not capability. "We think that for a lot of workflows and a lot of use cases, this can be an incredibly good option, especially from a cost perspective," Wang said.

As with any vendor-supplied numbers, the benchmark claims have not yet been independently verified, and DeepSWE results in a controlled setting rarely map cleanly onto messy real-world repositories.

## Why it matters

AI coding is the clearest product-market fit the current generation of models has found, and the economics have become the battleground. Claude Code and Codex have built loyal followings but can run up serious token bills on large jobs. Meta's strategy reads as a classic platform play: accept that its model trails on raw quality, compete aggressively on price, and use a data-for-discount arrangement to bootstrap a training flywheel from real developer usage.

That flywheel is the actual product. The contributor tier is not just a pricing gimmick; it is a mechanism to acquire high-signal, real-world coding traces that Meta can feed back into future Spark models. For a company that has spent lavishly to catch up in AI, buying developer data at a discount may be cheaper than buying it any other way. The open question is whether professional teams, especially at enterprises with strict IP and confidentiality rules, will trade proprietary code and prompts for a lower bill. Many will not touch the contributor tier at any price, which pushes them onto the standard tier where Meta's cost advantage narrows considerably.

## What to watch next

The tells will come quickly. Watch for independent DeepSWE and SWE-bench-style evaluations from third parties to test whether Spark 1.2's numbers hold outside Meta's own charts. Watch adoption of the contributor tier specifically, which will reveal how much developers actually value their data versus their spend. And watch how Anthropic and OpenAI respond, whether they cut prices, ship faster background-agent features to match Muse Code's parallel sub-agents, or simply lean on quality leadership. For now, Meta is late to the coding-agent race but has arrived with the one weapon incumbents least want to fight over: price.
