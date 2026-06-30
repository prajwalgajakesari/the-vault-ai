# OpenAI Previews GPT-5.6 as Three Tiers — Sol, Terra, and Luna — but You Cannot Use It Yet

OpenAI on Friday unveiled its most capable model family to date — GPT-5.6, split into three permanent tiers named Sol, Terra, and Luna — and then did something the company has never done before: it told almost everyone they cannot have it. Initial access is restricted to roughly 20 organizations individually vetted and cleared with the U.S. government, the first time a frontier American AI model has shipped behind a federally gated rollout.

The result is a launch with two stories running in parallel. One is about raw capability: Sol, the flagship, set state-of-the-art records on coding and security benchmarks and became the first model to cross the halfway mark on one of the industry's hardest agentic evaluations. The other is about control — a Trump administration executive order, a list of "trusted partners" shared with Washington, and a general release that OpenAI will only promise is coming "in the coming weeks."

## Three durable tiers, not one model

The headline architectural shift is that GPT-5.6 is not a single model dressed up with different reasoning settings. It is three distinct, durable tiers, each aimed at a different slice of the cost-capability curve.

**Sol** is the flagship, tuned for the hardest problems — complex software engineering, long-horizon agentic tasks, and cybersecurity research. It ships with new "ultra" and "max" reasoning modes that trade latency for depth. **Terra** is the balanced workhorse, priced at roughly half of Sol and aimed at high-volume business work like customer support, internal tooling, and document analysis. **Luna** is the fast, cheap tier for everyday tasks — summarization, drafting, and routine automation — and notably, even Luna edges out the previous generation's flagship on several evaluations.

The pricing makes the ladder explicit. Sol runs $5 per million input tokens and $30 per million output tokens; Terra is $2.50 and $15; Luna is $1 and $6. That is a clean 2x step between each tier, a structure that reads less like a temporary product lineup and more like a permanent menu OpenAI intends to keep refilling with each generation.

## The benchmark numbers

On capability, the numbers are striking. On Terminal-Bench 2.1, the industry's marquee command-line automation benchmark, Sol's ultra mode posted a record 91.9%, with its max mode at 88.76% — both clearing GPT-5.5's 83.4% and edging past Anthropic's Claude Mythos 5 at 88%.

More significant for the agentic frontier, Sol became the first model to clear 50% on Agent's Last Exam, hitting 50.9% in "code mode." That benchmark has functioned as a wall for the field; crossing it is the kind of milestone that reorders leaderboards.

The third number is the one that explains the access restriction. On OpenAI's internal cyber capture-the-flag testing — work adjacent to the public ExploitBench evaluations — all three models crossed the company's "High" cyber-capability threshold, with Sol at 96.7%, Terra at 91.84%, and Luna at 85.19%. A model that can autonomously find and exploit software vulnerabilities at that level is exactly what new federal rules were written to catch.

## Why you cannot use it yet

That is where the government comes in. The restricted rollout traces directly to a Trump administration executive order issued June 2, 2026, which established a framework for federal agencies to benchmark and assess frontier models with advanced cyber capabilities before they reach the broad public.

OpenAI's own announcement was unusually candid about the arrangement. "At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government," the company wrote, adding: "We are taking this short-term step because we believe it is the best way to increase availability in the coming weeks, while working with the Administration to develop the cyber Executive Order framework and a process for future model releases."

For now, GPT-5.6 lives only in the OpenAI API and Codex — not in ChatGPT — and only for the cleared partners. The phrasing matters: this is OpenAI framing a government-gated launch as a bridge to wider access, not a cage.

Chief executive Sam Altman drew that line sharply in public. Extensive safety testing "is not a bad idea," he said on X. "I just don't like the idea of the government picking the customers." It is a careful posture — endorse the evaluation, resist the precedent.

## What it means for the market

Two durable shifts are worth sitting with. The first is structural. By hardening GPT-5.6 into three named, permanently differentiated tiers with a tidy pricing ladder, OpenAI is conceding that the era of one-model-fits-all is over and that competition now happens across a spectrum. This is a direct answer to Anthropic's Claude lineup and Google's Gemini tiers, both of which have segmented flagship, mid, and economy offerings. Terra at $2.50 input is a pointed shot at the high-volume enterprise middle, where margins and switching costs are decided.

The second shift is harder to price. A government-gated launch is a new cost of doing business at the frontier — and a new moat. If clearing a federal cyber review becomes the price of releasing a top-tier model, the labs with the deepest Washington relationships and compliance machinery gain an advantage that has nothing to do with model quality. Anthropic and Google will face the same executive order; how each navigates it could matter as much as the next benchmark.

## What to watch

The single most important variable is timing. "Coming weeks" is doing a lot of work, and the gap between preview and general availability will signal how heavy the federal review process actually is. Watch whether broad GA arrives with the full three-tier suite intact or whether Sol — the variant the cyber controls are really about — lags behind Terra and Luna. And watch the precedent: if this becomes the standard path for frontier releases, the question Altman raised about who picks the customers will define the next phase of the AI race as much as any leaderboard.
