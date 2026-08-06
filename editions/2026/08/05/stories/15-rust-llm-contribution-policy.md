---
headline: "Rust Publishes an LLM Policy: Bots Can Review and Refine, but Not 'Create'"
slug: rust-llm-contribution-policy
category: policy
story_number: 15
edition: 2026-08-05
---

# Rust Publishes an LLM Policy: Bots Can Review and Refine, but Not 'Create'

When the Rust project finally wrote down its rules for artificial intelligence, the entire philosophy fit in a single sentence.

"It's fine to use LLMs to answer questions, analyze, distill, refine, check, suggest, review," the new policy reads. "But not to **create**."

That line, published August 5 in a post on the Inside Rust blog by contributor Jynn Nelson, closes out more than a month of fractious internal debate, an estimated 3,000-plus messages on the project's Zulip chat, and a public pull request that drew objections from some of Rust's most senior figures. Five teams that work on the `rust-lang/rust` monorepo formally adopted the LLM Usage Policy, giving reviewers something they had never had before: a published, canonical set of rules to point to when closing a low-effort, machine-generated contribution.

## What the policy actually says

The policy sorts LLM use into three buckets. Reading, analyzing, and learning are broadly fine. Creating is heavily restricted. And a middle tier is permitted only with disclosure.

On the allowed list: asking an LLM questions about the codebase, having it summarize an issue or PR for your own private use, using it to privately review your own code, and generating candidate solutions to study before writing something "from scratch in your own style." Personal dev tools are fine too, as long as they never get merged upstream.

The banned list is shorter but targets the most common friction points. LLM-authored comments, issue bodies, and PR descriptions are prohibited unless clearly quoted and marked. So is documentation "originally authored" by an LLM, a category the policy explicitly extends to compiler diagnostics. And an LLM review may never be treated as sufficient grounds to merge or reject a change. "LLM reviews, if enabled by a team, **must** be advisory-only," the document states.

Review bots occupy the disclosed middle ground, hemmed in by caveats: they must run from a separate GitHub account marked as an LLM, must be blockable by individual users, and their comments "**must not** be blocking" unless a human reviewer explicitly endorses them. Machine translation, trivial changes, and LLM-assisted bug discovery are likewise allowed only with disclosure.

Crucially, disclosure is the load-bearing requirement. "You must disclose LLM-generated content," the blog post says. "You may not hide LLM involvement." Lying about it is not treated as a mere policy breach but as a Code of Conduct violation, carrying the risk of a ban.

## The 'slop' problem

Nelson is candid about why the rules exist. "At the time of writing, there are **1,281 open PRs** to `rust-lang/rust`," the post notes, framing review bandwidth, not code correctness, as the central crisis. The essay lays out three harms: polished technical products "no longer indicate effort and understanding," easier code generation "exacerbates our existing issues with review bandwidth," and people "mechanically copy-pasting to and from an LLM is a waste of our time."

Reviewing, Nelson argues, "is made of decisions" about whether a change is even a good idea. Rust's culture had long treated a polished PR as a signal of a human who understood their work and might stick around. LLMs severed that link. "In the case of autonomous agents, there is no longer someone on the other end at all."

There is also an experimental carve-out. "Pre-arranged, non-critical, high-quality, well-tested, and well-reviewed code changes that are originally created by an LLM are allowed, **with disclosure**," but only when a reviewer has agreed in advance, the change avoids soundness-critical areas like the trait system or MIR building, and both author and reviewer can fully explain the code. Such PRs get an `ai-assisted` label and are logged to a private channel to gather data.

## A consensus nobody loves

The policy passed over pointed dissent. Niko Matsakis, a principal architect of modern Rust, argued it was "worse than no policy at all," warning it "sets a precedent that I think will harm potential contributors." He called the conditions on the experimental exception "overkill and kind of insulting" toward fellow maintainers. Contributor Diggory Blake questioned the framing entirely, asking whether a concise, clearly beneficial change should be rejected simply for being marked AI-generated. Nelson concedes the point: "I do not think every rule in this policy is wholly good."

The compromise reflects Rust's governance. "Rust operates by consensus," the post notes, and there is "not a consensus within the Rust project - and likely never will be - about when/how/where it is acceptable to use AI-based tools."

## What to watch

Rust now joins a widening spectrum of open-source responses, from outright bans at Zig, Servo, and QEMU to disclosure regimes at LLVM, the Linux kernel, and Firefox. The policy covers only `rust-lang/rust`; an attempt to extend it project-wide failed to reach consensus, and the leadership council is weighing a dedicated LLM sub-team. The real test is the data the experiment collects: whether disclosed, AI-assisted contributors are genuinely learning and sticking around, or whether the slop keeps coming. As Nelson puts it, "This is not the end of the story."
