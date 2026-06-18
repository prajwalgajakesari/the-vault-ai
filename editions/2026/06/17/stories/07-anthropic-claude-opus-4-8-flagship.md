Anthropic released Claude Opus 4.8 on May 28, calling its new flagship a "modest but tangible improvement" over its predecessor — a description that undersells what the launch actually delivers. The headline number is that Opus 4.8 now sits at the top of the Artificial Analysis Intelligence Index. But the more consequential changes ship around the model: a user-facing "effort control" dial, a "dynamic workflows" mode in Claude Code that can spin up hundreds of parallel subagents, and a fast inference mode that is three times cheaper than the one it replaces.

Taken together, the release is less about a single benchmark leap and more about Anthropic tuning how much compute its best model spends, when, and at what price — the levers that increasingly decide who wins the frontier race.

## What's new in the model

Opus 4.8 is a hybrid reasoning model with a 1 million-token context window by default on the Claude API, Amazon Bedrock, and Vertex AI (200k on Microsoft Foundry) and up to 128k output tokens. Anthropic says it beats both Opus 4.7 and rivals OpenAI's GPT-5.5 and Google's Gemini 3.1 Pro across most tested categories.

The gains are clearest in coding and agentic work. On SWE-bench Pro, the model hits 69.2%, up from 64.3% for Opus 4.7 and 58.6% for GPT-5.5, according to Anthropic's figures. SWE-bench Verified inches up to 88.6% from 87.6%, and Terminal-Bench 2.1 climbs to 74.6% from 66.1%. On Humanity's Last Exam, a multidisciplinary reasoning test, Opus 4.8 scores 49.8% without tools and 57.9% with tools — the highest marks Anthropic reports in the field. The model also claims the strongest computer-use result Anthropic has measured, scoring 84% on Online-Mind2Web.

The independent benchmarking firm Artificial Analysis ranks Opus 4.8 first on its Intelligence Index with a score of 61.4, edging out GPT-5.5 at 60.2 and leaving Opus 4.7 (57.3) behind. Crucially, Artificial Analysis notes the model reached that score using roughly 15% fewer turns and 35% fewer output tokens per task than Opus 4.7 — a detail that matters because Opus 4.7, despite identical sticker pricing, ran noticeably more expensive in practice by burning through more tokens.

Anthropic also leaned hard on honesty. The company says Opus 4.8 is about four times less likely than its predecessor to let flaws in code it wrote pass unremarked, and "more likely to flag uncertainties about its work and less likely to make unsupported claims." Its alignment team reported that the model "reaches new highs on our measures of prosocial traits like supporting user autonomy and acting in the user's best interest," with rates of misaligned behavior substantially lower than Opus 4.7.

## Effort control and dynamic workflows

The two features launching alongside the model may matter more than the weights themselves.

Effort control is the more visible change. A new dial next to the model selector in claude.ai and Cowork lets users decide how hard Claude works on any given response. Higher settings make the model think more frequently and more deeply; lower settings return faster answers and consume rate limits more slowly. Opus 4.8 defaults to "high," which Anthropic judges the best balance and which spends a similar token count to Opus 4.7's default while performing better. Power users can select "extra" ("xhigh" in Claude Code) or "max" for difficult tasks and long-running asynchronous jobs. The control is available on all plans.

That is a meaningful shift in how frontier models are sold. For the past two years, vendors have largely hidden reasoning depth behind model names and "thinking" toggles. Handing the dial directly to users — and tying it to rate limits rather than just quality — reframes inference as a budget the customer manages, not a fixed property of the model.

Dynamic workflows, available in research preview, push in the opposite direction: toward more autonomy. In Claude Code, the model can plan a large task, then run hundreds of parallel subagents in a single session before verifying its own outputs and reporting back. Anthropic's flagship example is a codebase-scale migration "across hundreds of thousands of lines of code from kickoff to merge," using the existing test suite as the bar to clear. The feature is limited to Enterprise, Team, and Max plans.

Early enterprise testers were uniformly positive in Anthropic's launch materials. "Claude Opus 4.8 has noticeably better judgment," said Tom Pritchard, a staff engineer quoted by Anthropic. "In Claude Code, it asks the right questions, catches its own mistakes, pushes back when a plan isn't sound, and builds up confidence around complex, multi-service explorations before making big changes."

Cursor co-founder and CEO Michael Truell, also quoted in Anthropic's announcement, pointed to efficiency rather than raw capability: "On CursorBench, Claude Opus 4.8 exceeds prior Opus models across every effort level. Tool calling is meaningfully more efficient, using fewer steps for the same intelligence, and it carries end-to-end tasks through."

## Pricing and the efficiency story

Standard pricing is unchanged from Opus 4.7 at $5 per million input tokens and $25 per million output tokens. The real pricing news is fast mode, which runs Opus 4.8 at 2.5x speed for $10 input and $50 output per million tokens — three times cheaper than the equivalent mode on the previous generation.

The token-efficiency numbers are the quiet thread connecting everything. If Opus 4.8 genuinely uses 35% fewer output tokens per task than 4.7, real-world bills could fall even with identical per-token rates — a welcome reversal after 4.7 drew complaints for costing 30% to 40% more in practice than 4.6 despite flat pricing. Databricks CTO Hanlin Tang said the model lets the company's Genie agent reason over PDFs and diagrams "at 61% cheaper token cost than Opus 4.7."

## What to watch

Opus 4.8 lands in a frontier market where benchmark leads are thin and short-lived; Anthropic shipped it just weeks after Opus 4.7. The more durable story is the strategy: efficiency gains that lower effective cost, a user-controllable effort budget, and agentic workflows aimed squarely at large-scale engineering work rather than chat.

Anthropic also signaled what comes next. The company says it is developing cheaper models with Opus-level capabilities, and a higher-intelligence class above Opus built on its Mythos-Preview line — currently restricted to a small set of organizations for cybersecurity work pending stronger safeguards. Whether the next leap comes from a smarter model or simply a cheaper, more controllable one is the question Opus 4.8 leaves open. For now, the dial is in the user's hands.
