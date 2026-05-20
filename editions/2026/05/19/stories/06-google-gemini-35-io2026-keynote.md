---
headline: "Google Unveils Gemini 3.5 as Its Most Capable Model at I/O 2026 Keynote"
slug: google-gemini-35-io2026-keynote
category: llms-genai
story_number: "06"
date: 2026-05-19
---

# Google Unveils Gemini 3.5 as Its Most Capable Model at I/O 2026 Keynote

Google opened its annual I/O developer conference on Tuesday with a sweeping declaration: the company is fully inside what CEO Sundar Pichai called "the agentic Gemini era," anchored by the launch of Gemini 3.5 Flash — a model that surpasses its own previous Pro-tier system across nearly every benchmark while running four times faster than competing frontier models at roughly half the cost.

The announcement, delivered from Shoreline Amphitheatre in Mountain View before thousands of developers on May 19, 2026, marks Google's clearest signal yet that the AI model race has moved beyond raw intelligence scores into a new competitive axis: speed, cost, and the ability to execute long-running autonomous tasks on behalf of users and enterprises.

## The Model and the Numbers

Gemini 3.5 Flash launches as generally available starting today, accessible via the Gemini app, Google AI Studio, the Gemini API, and Google's agent development platform Antigravity. The headline figures are striking: compared to Gemini 3.1 Pro, the new model scores 76.2% on Terminal-Bench 2.1 (versus 70.3%), 83.6% on MCP Atlas for scaled tool use (versus 78.2%), and 57.9% on Finance Agent v2 (versus 43.0%). On the GDPval-AA leaderboard — a benchmark designed to capture economically valuable real-world agentic tasks — Gemini 3.5 Flash reaches 1,656 Elo, compared to 1,314 for its predecessor. For multimodal reasoning, CharXiv scores 84.2%.

Pricing is set at $1.50 per million input tokens and $9.00 per million output tokens, with a 1,048,576-token context window. Google is framing the cost advantage explicitly: frontier-tier competitors carry a price multiple that makes 3.5 Flash structurally cheaper for high-volume enterprise deployments.

Pichai drove the savings case home during the keynote with a pointed illustration. "Top companies are processing about 1 trillion tokens a day," he said. "If they shifted 80% of their workloads from other frontier models to 3.5 Flash, they'd save over $1 billion dollars annually. That is real savings they can pour back into their company."

## Why This Flash Outpaces the Previous Pro

The more technically significant claim is not just that 3.5 Flash beats competing models — it is that a Flash-tier model now eclipses Gemini's own prior Pro tier. Historically, the Flash designation has implied speed and economy at the expense of reasoning depth. Google appears to have compressed that trade-off substantially. When plotting intelligence versus tokens per second on the Artificial Analysis Intelligence Index, Pichai said Gemini 3.5 Flash sits "in a league of its own in the top right quadrant" — high intelligence, four times the output velocity of other frontier systems.

The performance jump has an internal backstory. Google has been running Gemini 3.5 Flash inside its own development infrastructure through Antigravity, the company's agent-first coding platform. Internal token processing accelerated from 500 billion tokens per day in March to more than 3 trillion tokens per day by the keynote — a compounding feedback loop that Pichai credited with sharpening the model before its public release.

Google also announced that a more capable Gemini 3.5 Pro is in active internal testing and will arrive next month, a detail that drew audible disappointment from portions of the developer audience who expected it at I/O. The company positioned the delay as deliberate: Pro is being refined further before release.

## Gemini Spark and the Agentic Push

The 3.5 Flash launch is inseparable from the broader product architecture Google unveiled around it. Gemini Spark — the company's new consumer-facing personal AI agent — runs on Gemini 3.5 and the Antigravity harness, operating on dedicated virtual machines in Google Cloud on a 24/7 basis. Spark can manage long-horizon background tasks, integrate with Google's own tool suite, and will connect to third-party tools via MCP protocol in the coming weeks. A beta rolls out to Google AI Ultra subscribers in the U.S. next week.

Pichai also introduced Antigravity 2.0, a standalone desktop application for managing cohorts of autonomous AI agents. A performance-optimized version of Flash specifically tuned for Antigravity is described as 12 times faster than other frontier models — three times the already-advertised 4x advantage — a figure that, if confirmed by independent testing, would represent a meaningful structural edge for continuous coding and agentic orchestration workloads.

Alongside Gemini 3.5, Google announced Gemini Omni Flash, a new multimodal model designed to accept any input modality and generate video outputs — the first step in what Google described as moving "from predicting text to simulating reality." Image and text output capabilities are expected to follow.

## Scale as Context

To frame the Gemini 3.5 release, Pichai led with a token-volume narrative that underscored the scale of Google's distribution advantage. Monthly tokens processed across Google's surfaces grew from roughly 480 trillion at I/O 2025 to over 3.2 quadrillion by May 2026 — a seven-fold increase in a single year. The Gemini app has grown from 400 million to 900 million monthly active users in the same period. Developer usage of Google's model APIs now exceeds 19 billion tokens per minute, with 8.5 million developers building on the platform each month.

This scale matters to the Gemini 3.5 story in two ways. First, improvements to Flash-tier models will have outsized real-world impact because Flash is the tier that most developers actually deploy at volume. Second, it raises the competitive stakes: OpenAI, Anthropic, and Meta are all pursuing similar agentic positioning, and Google's ability to iterate models at this volume gives it a structural feedback loop that competitors cannot easily replicate.

## What the Benchmark Story Actually Means

The competitive framing deserves scrutiny. Google's own charts place Gemini 3.5 Flash above GPT-5.5 and Claude Opus 4.7 on the Artificial Analysis Intelligence Index speed comparison — but independent, third-party confirmation of those rankings remained limited at time of publication. The GDPval-AA metric is a relatively new evaluation, and its methodology for quantifying "economically valuable tasks" is not yet standardized across the industry. Buyers evaluating these claims should run workload-specific benchmarks before making procurement decisions.

What is not in dispute is the pricing. At $1.50 input and $9.00 output per million tokens, Gemini 3.5 Flash is priced to make the cost-of-switching calculation easy for developers already on the fence. The model's availability across Google's full product surface — from AI Studio and the developer API to Search, Antigravity, and the Gemini app — also means Google can drive adoption simultaneously at the consumer, developer, and enterprise layers, compressing the time between model release and real-world feedback.

## What Comes Next

The Gemini 3.5 Pro announcement signals that Google's model cadence is accelerating. A Pro release next month would place Google's most capable publicly available model within weeks of I/O — a tighter iteration loop than the company has historically managed. Pichai closed the keynote with a signal that the current pace is not expected to slow: "As we look across the full stack of innovation, from the infrastructure behind TPU 8i to the frontier capabilities of Gemini 3.5 and Antigravity, it's clear we're firmly in our agentic Gemini era."

For developers, the practical question is whether Gemini 3.5 Flash's agentic benchmark advantages translate into production gains on their specific workloads. Google has structured its pricing and availability to make that experiment low-friction. The answer to that question, aggregated across millions of developers over the coming sixty days, will do more to shape the competitive landscape than any benchmark chart shown on stage.
