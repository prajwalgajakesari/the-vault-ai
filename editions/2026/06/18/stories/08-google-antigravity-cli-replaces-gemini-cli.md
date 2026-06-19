# Google's Antigravity CLI Replaces the Gemini CLI as the Legacy Model Catalog Gets Cleared

On June 18, 2026, the `gemini` command that thousands of developers had wired into their terminals, shell scripts, and CI/CD pipelines stopped serving requests. In its place Google is pushing the **Antigravity CLI** — a closed-source, Go-based binary called `agy` — as the front door to its Gemini 3.5 agentic stack. There was no grace period for consumer tiers. Any automation that still shelled out to `gemini` on the morning of June 18 simply broke.

The cutover is the sharpest edge of a much wider consolidation. While Google retired the legacy CLI, it was simultaneously running one of the most aggressive Gemini API deprecation waves in the platform's history — clearing out an entire generation of 2.0 and image-and-video preview models in a matter of weeks. Taken together, the message to developers is unambiguous: the old surface area is being demolished, and everything is being funneled onto the Gemini 3.5 agentic platform Google unveiled at I/O 2026.

## What changed on June 18

Gemini CLI and the Gemini Code Assist IDE extensions stopped serving requests for Google AI Pro and Ultra subscribers, as well as individuals on the free Gemini Code Assist tier, on June 18. Enterprise customers running through Google Cloud keep their legacy access for now, but Google is steering even them toward Antigravity with their existing GCP projects.

The successor is not a drop-in rename. The original Gemini CLI was an open-source project with roughly 105,000 GitHub stars. Antigravity CLI is a closed-source rewrite with a new binary (`agy`), a new configuration layout, and a different quota model that swaps daily limits for weekly ones. It is one piece of a broader ecosystem: a standalone **Antigravity 2.0** desktop app, the CLI, managed agents, and an SDK, all sharing a single agent harness built for multi-agent orchestration.

The breaking changes go deeper than the binary name. Reporting from migration guides and TechTimes coverage of the cutover describes an MCP configuration change that fails silently — copy an old config without renaming the relevant field and `agy` starts cleanly, but the MCP server never connects, leaving an agent running without the tool it expects and quietly producing wrong results. The free tier, by several accounts, dropped from roughly 1,000 requests per day on the old CLI to around 20 on Antigravity, a cut north of 95 percent for hobbyists and individual developers.

## The model catalog gets cleared

The CLI swap landed in the middle of a deprecation blitz. Per Google's own release notes, the Gemini 2.0 family — `gemini-2.0-flash`, `gemini-2.0-flash-001`, `gemini-2.0-flash-lite`, and `gemini-2.0-flash-lite-001` — reached its shutdown on June 1, 2026, with Google directing teams to `gemini-3.5-flash` or `gemini-3.1-flash-lite`. The image preview models `gemini-3.1-flash-image-preview` and `gemini-3-pro-image-preview` are slated to shut down June 25, with video generation models following on June 30. For generation, Google points developers to **Veo 3.1** (`veo-3.1-generate-preview` and `veo-3.1-fast-generate-preview`), and the GA image replacements are the cheekily named "Nano Banana 2" (`gemini-3.1-flash-image`) and "Nano Banana Pro" (`gemini-3-pro-image`).

The economics of the migration are not neutral. Independent analyses flagged that moving off the deprecated `gemini-2.0-flash` to `gemini-3.5-flash` can mean a roughly 15x jump in per-token cost — a meaningful jolt for high-volume, latency-tolerant workloads that were specifically built on the cheap 2.0 tier.

## The agentic stack Google is betting on

Antigravity is the centerpiece of Google's I/O 2026 pivot to agent-first development. The platform pairs with Gemini 3.5 Flash, which Google says runs about four times faster than other frontier models measured by output tokens per second and is tuned for agentic coding workflows.

CEO Sundar Pichai framed the bet in personal terms at I/O. "The new model has been a game-changer for us internally at Google," he said. "We've been using 3.5 Flash with the reimagined version of our agent-first development platform, Antigravity. And it's dramatically accelerated how we build."

Developers were less enthusiastic. Within 24 hours of the May 19 transition announcement, the official GitHub thread reportedly drew roughly 143 thumbs-down reactions against 4 cheers. The complaints clustered: a closed-source successor replacing a beloved open-source tool, far tighter free-tier limits, dropped configuration knobs, and a roughly 30-day deadline that many teams felt was far too short to rewrite internal tooling. As one migration write-up put it bluntly, a deadline "announced mid-sprint means at most one sprint to plan, execute, and verify the migration before the old tool stops working."

## Analysis: consolidation, lock-in, and the agentic tooling war

The strategic logic is clear. Google is collapsing a sprawl of consumer CLIs, IDE extensions, and preview model IDs into one agentic platform it fully controls. Antigravity being closed-source matters here: the open Gemini CLI let developers fork, audit, and self-host workflows; `agy` does not. That trades community goodwill for tighter control over the runtime, the quota model, and the upgrade cadence — a more defensible position in the agentic-coding fight against **Claude Code, OpenAI's Codex, and Cursor**, all of which are racing to own the developer's terminal and orchestration layer.

But consolidation has a cost, and it is being paid in migration fatigue. Within roughly a month, a developer relying on Google's stack could face a CLI rewrite, a model-ID swap for 2.0 workloads, an image-model migration before June 25, a video-model migration before June 30, and a 15x cost recalculation — much of it on overlapping deadlines. Hard cutovers with no consumer grace period are a deliberate forcing function, but they also erode the trust that made the open Gemini CLI a 105,000-star project in the first place. Every silent breakage and every shrunk free tier is a reason for an indie developer to evaluate a competitor instead.

## What to watch

- **Enterprise timeline:** Google has only deferred, not canceled, the legacy sunset for Cloud customers. Watch for a firm enterprise cutover date.
- **The June 25 and June 30 shutdowns:** the image and video model retirements are the next hard deadlines; expect a fresh round of broken pipelines and Veo 3.1 migration scrambles.
- **Free-tier backlash:** if the ~20-request daily cap holds, watch whether hobbyist mindshare drifts toward Cursor, Codex, or Claude Code.
- **Cost migration pain:** the 15x jump from 2.0 to 3.5 Flash could push price-sensitive teams to `gemini-3.1-flash-lite` — or off Gemini entirely.
