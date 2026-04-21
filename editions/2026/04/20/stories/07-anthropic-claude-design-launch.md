# Anthropic Launches Claude Design, Targeting Slides, Prototypes, and Enterprise Visual Work

# Anthropic Launches Claude Design, Targeting Slides, Prototypes, and Enterprise Visual Work

Anthropic opened a new front in the AI platform war on Friday, rolling out **Claude Design**, a standalone visual-creation product that lets teams build prototypes, pitch decks, one-pagers, and functional UIs by talking to Claude instead of dragging rectangles around Figma. The research preview went live April 17 for subscribers on Anthropic's Pro, Max, Team, and Enterprise plans, and markets reacted before the press release had finished circulating: **Figma's stock closed down 7.28%** on the day, settling at $18.84.

The launch arrives out of Anthropic Labs, the experimentation arm that also shipped Claude Cowork earlier this year, and it sits on top of **Claude Opus 4.7**, the vision-heavy model Anthropic released just 24 hours earlier. Opus 4.7 tripled the company's long-edge image resolution ceiling to 2,576 pixels, a spec that matters less as a benchmark than as a prerequisite: Claude Design has to read whole screenshots, Figma frames, and design-token sheets without losing detail.

## What Claude Design actually does

Users describe what they want. Claude builds a first draft. From there, the surface looks less like ChatGPT and more like a design tool: inline comments, direct edits, custom sliders Claude generates on the fly for things like corner radius or spacing, and an organization-scoped sharing layer. The output isn't locked inside Anthropic's walls. Projects export to PDF, PPTX, a hosted URL, or straight into Canva, where they land as fully editable files.

The feature Anthropic is leaning on hardest is codebase-aware design systems. During onboarding, Claude ingests a team's repository and design files and extracts colors, typography, spacing, and components. Every subsequent project inherits that system automatically — the pitch from Anthropic is that a PM sketching a prototype shouldn't have to re-pick brand blue every time.

"What used to take a week of back-and-forth between briefs, mockups, and review rounds now happens in a single conversation," said **Aneesh Kethini, a product manager at Datadog**, one of the launch partners. Brilliant, the online learning platform, told Anthropic the compression is even steeper on complex work. "Our most complex pages, which took 20+ prompts in other tools, only required 2 prompts in Claude Design," said **Olivia Xu, a senior product designer at Brilliant**.

## A partnership, not a collision, with Canva

The most politically interesting piece of the launch is the Canva relationship. Rather than position Claude Design against Canva, Anthropic routed the export layer through it. The two companies have been building together for nearly two years — Canva shipped an MCP for Claude in July 2025 — and Claude Design extends that into a bidirectional workflow.

"We're excited to build on our collaboration with Claude, making it seamless for people to bring ideas and drafts from Claude Design into Canva, where they instantly become fully editable and collaborative designs," said **Melanie Perkins, Canva's co-founder and CEO**, in a joint statement.

Figma, by contrast, was not invited to the party. Anthropic CPO Mike Krieger stepped off Figma's board three days before launch, a move that now reads as choreography rather than coincidence.

## Why this matters

Claude Design is Anthropic's clearest signal yet that it intends to build specialized product surfaces on top of its models, not just sell API access and a chat box. Chat is commoditizing; vertical workflows — design, code, research, ops — are where enterprise budgets accumulate. With Anthropic reportedly holding 37% of business AI spend in Q1 2026 versus OpenAI's 33%, the company is monetizing that lead by converting chat subscribers into multi-product subscribers without raising prices.

It's also a test of the Labs model. Claude Cowork in January, agentic plugins shortly after, and now Claude Design — Anthropic is shipping narrow, opinionated products on a quarterly-ish cadence and letting the market vote. Enterprise admins have to explicitly enable Claude Design in Organization settings (it's off by default), which gives security teams a gating mechanism and gives Anthropic a clean telemetry signal on real enterprise adoption.

For the incumbents, the picture is uneven. Canva has absorbed Claude Design as a funnel. Gamma, the AI deck-builder that raised on this exact workflow, now faces a better-funded competitor bundled into an existing subscription. Figma is the most exposed: its 80–90% share of UI/UX design work is precisely what Claude Design's codebase-aware prototypes target. The 7% single-day stock move suggests investors already see it that way.

## What to watch

A few things will decide whether Claude Design is a side quest or a flagship. First, a **general-availability timeline** — Anthropic hasn't committed to one, and research previews at the company have historically run three to nine months. Second, **Figma's response**: expect a Make AI relaunch or a deeper OpenAI integration within the quarter. Third, **pricing**: access is bundled today, but a premium Design add-on for Enterprise is the obvious next SKU. And fourth, **enterprise adoption signals** — watch whether admins flip the default on at scale, and whether design-system ingestion holds up on messy real-world codebases rather than the polished ones Brilliant and Datadog brought to the demo.
