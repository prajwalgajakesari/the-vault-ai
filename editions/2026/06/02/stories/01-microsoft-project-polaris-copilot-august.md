---
headline: "Microsoft Project Polaris Will Replace OpenAI as Default GitHub Copilot Engine by August"
slug: microsoft-project-polaris-copilot-august
category: business
story_number: "01"
date: 2026-06-02
---

# Microsoft Project Polaris Will Replace OpenAI as Default GitHub Copilot Engine by August

Microsoft used the opening keynote of Build 2026 on Monday to announce that Project Polaris, its homegrown AI coding model, will replace GPT-4 Turbo as the default reasoning engine inside GitHub Copilot for all 4.7 million paid subscribers and 77,000 enterprise customers starting in August. The move ends Copilot's four-year reliance on OpenAI models and gives Microsoft full vertical control over the most widely deployed AI developer tool on the planet -- from the custom silicon running the inference to the IDE experience shipping the completions.

CEO Satya Nadella, speaking to roughly 2,500 developers at Fort Mason Center in San Francisco, framed the shift as part of a broader transformation. He declared that AI has moved from synchronous assistants to "async coworkers that can execute long-running tasks across key domains." Microsoft positioned Polaris not as a conventional coding assistant but as "a peer programmer, not a pair programmer" -- capable of being assigned bugs, features, and entire code maintenance tasks and completing them independently.

## What Polaris Actually Is

Project Polaris is a mixture-of-experts architecture with specialized sub-modules tuned for distinct programming languages, frameworks, and paradigms. Unlike the general-purpose GPT-4 Turbo that currently powers Copilot, Polaris was purpose-built for software development: code generation, multi-file refactoring, test writing, code review, documentation generation, and dependency analysis. Pro tier subscribers will gain multi-file context windows spanning up to 100,000 lines of code and autonomous test generation capabilities.

According to Microsoft, Polaris outperforms GPT-4 Turbo on the HumanEval and MBPP coding benchmarks, with the largest claimed gains in low-resource languages like Rust and Haskell where training data scarcity makes model architecture matter more than dataset size. Those figures are Microsoft's own and have not been independently verified at publication time.

The model runs on Microsoft's custom Maia 200 AI accelerators inside Azure data centers, which the company says reduces per-inference latency and lowers operational cost compared with routing requests through OpenAI's API infrastructure. The rollout plan gives existing subscribers an automatic migration in August with an optional three-month fallback period to remain on GPT-4 Turbo. After November, Polaris becomes the sole default engine.

## The $13 Billion Relationship Unwinds

The announcement arrives just two months after Microsoft and OpenAI formally ended their seven-year exclusive partnership in April 2026. That breakup had already signaled a coming divergence, but Polaris makes the separation tangible at the product level. The commercial arrangement between the two companies had grown increasingly awkward: OpenAI was simultaneously building Codex, a direct competitor to GitHub Copilot, while Microsoft was competing with OpenAI for enterprise AI accounts.

GitHub CEO Thomas Dohmke, announcing the general availability of Copilot Workspace at the same keynote, called it "the biggest change to Copilot since launch." The Workspace platform -- which lets Copilot reason across entire repositories, propose multi-file edits, run tests, and iterate autonomously -- now ships with a reasoning layer built and operated entirely within Microsoft's stack. For the 77,000 enterprise customers building on the Copilot SDK, Polaris is the model they will be embedding.

Microsoft also unveiled the MAI model suite version 2, covering image generation, multilingual voice synthesis, and transcription -- a coordinated push to replace OpenAI-supplied models across its entire product surface. Pricing for the v2 models was not disclosed.

## Why This Matters

The strategic calculus here extends well beyond one product swap. Microsoft invested $13 billion in OpenAI and built its AI strategy around that partnership. Project Polaris signals that Redmond now believes it can compete on model quality, not just distribution and infrastructure. The company controls the model, the custom inference hardware, the developer platform, and the enterprise billing relationship -- a degree of vertical integration that no other player in the AI coding tools market currently matches.

The timing also matters competitively. Anthropic's Claude Code has been gaining ground rapidly among enterprise developers, with Claude Opus scoring 88.6% on SWE-bench Verified. Microsoft publicly named Claude Code as the competitor Polaris is designed to displace, an unusual acknowledgment of a rival's market position. By running Polaris on its own Maia 200 silicon rather than renting GPU capacity, Microsoft can potentially undercut competitors on price while maintaining tighter latency guarantees -- a critical advantage when developers are making real-time coding decisions.

For the broader AI industry, Polaris represents a template that other cloud hyperscalers may follow: build your own specialized models, run them on your own custom chips, and reduce dependence on external model providers. Google has been on this path with its Gemini models, and now Microsoft has committed to the same playbook for its flagship developer product.

## What to Watch Next

The real test for Polaris comes in August when millions of developers start hitting it with production workloads. Microsoft's internal benchmarks are promising, but coding models live or die on the messy reality of enterprise codebases, legacy frameworks, and edge cases that no benchmark captures. The three-month fallback window will function as a de facto public evaluation period -- if significant numbers of teams opt to remain on GPT-4 Turbo, Microsoft will have a perception problem on its hands.

Watch also for OpenAI's response. The company that once powered the world's most popular AI coding tool now finds itself displaced from it. Whether OpenAI accelerates its own Codex platform or pivots its developer strategy will say a great deal about how the post-partnership AI landscape shakes out. For now, Microsoft has made its bet: the future of GitHub Copilot runs on Microsoft models, Microsoft silicon, and Microsoft infrastructure. August will reveal whether 4.7 million developers agree.
