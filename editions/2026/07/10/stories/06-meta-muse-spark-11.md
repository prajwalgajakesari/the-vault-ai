Late on the night of July 9, 2026, Mark Zuckerberg did something he had not done in three years: he posted on X. The occasion was Muse Spark 1.1, a multimodal reasoning model from Meta Superintelligence Labs that arrived not as another set of open weights but as a closed, hosted, metered product — Meta's first paid frontier API.

"Today we're releasing Muse Spark 1.1 — a strong agentic and coding model at a very low price," Zuckerberg wrote, capturing the entire pitch in a single sentence. The model is not trying to top the leaderboard. It is trying to be the cheapest capable thing you can wire into an agent stack, and to be the model that runs the other models.

That framing matters because Muse Spark 1.1 is explicitly built to orchestrate. Meta trained it to operate as a primary agent that gathers context, forms a plan, and delegates execution across parallel subagents — or, flipped around, as a subagent that sticks to a narrow job, understands the tools in front of it, and escalates back to the main agent when it hits a wall. The whole design assumes the model will be one node in a multi-agent system rather than a lone chatbot answering a prompt.

## The specs and the price

The headline number is the price. Meta is charging $1.25 per million input tokens and $4.25 per million output tokens, with $20 in free credits for new accounts. Zuckerberg characterized that as roughly a quarter of what Anthropic and OpenAI charge for comparable models — a claim that lines up with how Muse Spark 1.1 slots against Claude Opus 4.8 and GPT-5.5 in Meta's own materials.

The context window is 1,000,000 tokens (1,048,576, per the API docs). Inputs span text, images, video, and documents; output is text. Because it is a reasoning model, it thinks before answering, and that reasoning effort is adjustable per request. The API also exposes structured output, parallel tool calling, a Files API, prompt caching, and a `web_search` tool that returns cited answers.

Access splits two ways. Consumers get the model free in "Thinking" mode inside the Meta AI app and on meta.ai. Developers pay per token through the Meta Model API, which launched in public preview alongside the model — US-only at first, with no EU access yet and a waitlist for partners who aren't already onboarded.

## Agent-native by design

The clearest signal of what Meta is building came in its benchmark table, which splits cleanly along one axis: tool use versus raw accuracy.

On MCP Atlas, a test of scaled tool use, Muse Spark 1.1 scores 88.1, ahead of Opus 4.8 (82.2), GPT-5.5 (75.3), and Gemini 3.1 Pro (78.2). On JobBench, a professional tool-use benchmark, it posts 54.7 against Opus 4.8's 48.4 and GPT-5.5's 38.3. On Humanity's Last Exam, run with tools, it leads at 62.1. It tops every row that measures a model's ability to coordinate tools and work.

The coding and multimodal rows tell the opposite story. On SWE-Bench Pro, Muse Spark 1.1 scores 61.5, behind Opus 4.8's 69.2 and ahead of GPT-5.5's 58.6. On DeepSWE 1.1, a long-horizon coding test, it lands at 53.3, well behind GPT-5.5's 67.0. On OSWorld-Verified (computer use) it reaches 80.8, and on BabyVision (visual reasoning) 76.3 — third place in both. As MarkTechPost put it in its analysis, "this is an orchestration model, not a coding-accuracy leader." Every figure is vendor-reported, with rivals shown in their strongest configurations and Meta choosing the benchmark set and running the harness.

What earns those tool-use scores is behavior, not just training data. The model actively manages its million-token window — remembering earlier actions, retrieving information from much earlier in a session, and compacting what it keeps rather than letting context blow past the limit. Meta's research team also reports zero-shot generalization to unfamiliar native tools, MCP servers, and custom skills, meaning the model can pick up capabilities it has never seen without retraining. For computer use, it was trained to write a script when automation is faster and to click when direct interaction is simpler, batching actions at each step.

Crucially, wiring it in is cheap in engineering terms too. The Meta Model API speaks both the OpenAI SDK — Chat Completions and Responses formats — and Anthropic's Messages format. Migration is a base-URL change rather than a rewrite; Anthropic-format harnesses such as Claude Code point at the Messages endpoint, and agent CLIs like OpenCode register a provider with three values. The model also supports the Model Context Protocol, the open standard Anthropic introduced in late 2024.

## Why It Matters

Meta spent years giving models away as open weights. Muse Spark 1.1 is the pivot into the same paid-API business that Anthropic and OpenAI have built franchises on — and it enters not by claiming the best scores but by undercutting on price and specializing in orchestration.

That is a deliberately different lane. If the future of production AI is fleets of agents delegating to one another, the economics are punishing: every subagent call burns tokens, and cost compounds fast. A model that is genuinely strong at tool use and delegation, priced at roughly a quarter of the incumbents, is aimed squarely at teams for whom the orchestration layer — not the single smartest answer — is the bottleneck. Meta is betting the money in agents is in the plumbing, and it wants to be the cheap default that plans the work and dispatches it.

## What to Watch

The open questions are the usual ones for a preview. Every benchmark is Meta-reported, so independent evaluations on SWE-Bench Pro, Terminal-Bench, and real agent workloads will decide whether the orchestration story survives contact with production. Preview pricing can change once the free credits and land-grab phase end. And the closed model is a strategic reversal: no local deployment, no fine-tuning, and — for now — no EU access. If Muse Spark 1.1 does become the low-cost backbone of multi-agent systems, watch how quickly Anthropic and OpenAI respond on price, and whether Meta's decision to meter its frontier model reshapes how the rest of its lineup ships.
