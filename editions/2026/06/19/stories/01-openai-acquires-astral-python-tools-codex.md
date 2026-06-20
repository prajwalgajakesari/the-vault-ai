# OpenAI Acquires Astral, Maker of uv and ruff, to Supercharge Codex's Python Workflow

*The Vault — AI Edition | Business | June 19, 2026*

OpenAI is buying its way deeper into the daily life of the working Python developer. The company announced it will acquire Astral, the four-year-old startup behind the breakout open source tools uv, Ruff, and ty — software that millions of developers already lean on to install dependencies, lint code, and check types. The move plants OpenAI's Codex agent directly inside the Python toolchain, a position no rival AI coding assistant currently occupies.

The deal, disclosed alongside statements from both companies, would fold Astral's roughly 30-person team into OpenAI's Codex group after closing. Terms were not disclosed. The acquisition is still subject to "customary closing conditions, including receipt of regulatory approval," OpenAI said, and the two companies will operate independently until it closes.

## What OpenAI is buying — and why

Astral's tools are not niche. uv handles dependency and environment management; Ruff delivers extremely fast linting and formatting; and ty, the company's newer type checker, enforces type safety across codebases. All three are open source under permissive MIT and Apache 2.0 licenses, and they have accumulated hundreds of GitHub contributors since founder and CEO Charlie Marsh — a former Khan Academy engineer — started the company in 2022 with the stated goal of making "programming more productive."

For OpenAI, the strategic logic is about owning more of the loop. Codex, the company's coding assistant, has been on a tear: OpenAI says it has seen 3x user growth and a 5x jump in usage since the start of 2026, and now counts more than 2 million weekly active users. But OpenAI wants Codex to be more than an autocomplete engine.

"Our goal with Codex is to move beyond AI that simply generates code and toward systems that can participate in the entire development workflow—helping plan changes, modify codebases, run tools, verify results, and maintain software over time," the company wrote in its announcement. Astral's tools "sit directly in that workflow." In practice, that means a Codex agent could write a change, then immediately reach for Ruff to format and lint it, uv to resolve dependencies, and ty to verify types — before a human ever sees the diff.

Thibault Sottiaux, Codex Lead at OpenAI, framed the acquisition as an acceleration of that ambition. "Astral's tools are used by millions of Python developers. By bringing their expertise and ecosystem to OpenAI, we're accelerating our vision for Codex as the agent most capable of working across the entire software developer lifecycle," he said.

Marsh, for his part, cast the deal as a continuation of Astral's founding mission rather than a departure from it. "Astral has always focused on building tools that transform how developers work with Python—helping them ship better software, faster. As part of Codex, we'll continue evolving our open source tools to push the frontier of software development," he said in OpenAI's announcement. In a separate blog post, he went further, writing that "if our goal is to make programming more productive, then building at the frontier of AI and software feels like the highest-leverage thing we can do. It is increasingly clear to me that Codex is that frontier."

## Why it matters

The acquisition is a sharp escalation in the AI coding wars. Microsoft's GitHub Copilot, Google's Gemini Code Assist, and a crowd of startups are all racing to own the AI-assisted development workflow. By absorbing Astral, OpenAI gains a structural advantage that money alone is harder to replicate: deep integration into the plumbing Python developers run thousands of times a day. uv and Ruff are not features OpenAI is bolting on — they are infrastructure the broader ecosystem has already standardized around.

That same fact is what worries parts of the open source community. Both companies have stressed an explicit commitment to keep the tools open. Marsh called open source "the heart" of Astral's story, saying "it sits at the center of everything we do," and OpenAI tied its pledge to a "developer-first philosophy." But as The New Stack reported, the announcements were conspicuously light on the details that actually determine long-term trust — governance, licensing arrangements, and contribution structures all remain unspecified.

The permissive licenses offer a meaningful safety valve: MIT and Apache 2.0 code can be forked, modified, and redistributed, so the community is not strictly captive even if OpenAI's priorities shift. Yet the open questions are real. Will uv and Ruff continue to evolve for the independent developer who has no interest in Codex, or will roadmap decisions increasingly bend toward OpenAI's agentic ambitions? Who steers contribution policy once Astral's maintainers are OpenAI employees? An AI lab quietly setting the direction of foundational language tooling is a new kind of concentration for the Python world to digest.

## What to watch

Three things will tell the real story. First, regulatory review: the deal is explicitly contingent on approval, and an AI giant acquiring widely adopted developer infrastructure is exactly the kind of transaction antitrust authorities have signaled interest in scrutinizing. Second, governance specifics — whether OpenAI publishes a concrete commitment on open source maintenance, contribution rights, and licensing, or lets the ambiguity linger. Third, the fork question: if developers sense the tools drifting toward Codex lock-in, the permissive licenses make a community fork technically straightforward, and the credible threat of one may matter as much as any fork that actually materializes.

For now, uv, Ruff, and ty remain where they have always been — in millions of developers' workflows. The question is whose roadmap they will follow next.

---

**Sources:** [OpenAI](https://openai.com/index/openai-to-acquire-astral/); [The New Stack](https://thenewstack.io/openai-astral-acquisition/); [Astral blog](https://astral.sh/blog/openai); [Simon Willison](https://simonwillison.net/2026/mar/19/openai-acquiring-astral/)
