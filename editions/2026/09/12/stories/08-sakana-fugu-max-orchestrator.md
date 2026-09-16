Sakana AI shipped two models on September 11 and trained the weights for neither. Fugu Max and Fugu Ultra v2 are orchestrators: a language model that reads your query, builds an agent scaffold on the fly, and farms the work out to a pool of open-weight and specialist models — NVIDIA's Nemotron family among them — before stitching the answers into one response. You send one request to one OpenAI-compatible endpoint. What happens behind it is, per Sakana's FAQ, "not exposed by design."

The pitch is cost. Fugu Max lists at $2 per million input tokens and $6 per million output, which Sakana says is 40-60% under Sonnet 5, GPT-5.6 Terra and Kimi K3 on output. On Sakana's numbers it takes the best overall score on six benchmarks — Terminal Bench 2.1, GPQA Diamond, AA-LCR, GDP.pdf, AutomationBench, and SWEFish, an internal set built from Sakana's own coding tickets — and expands the cost-performance Pareto frontier on seven of ten.

"A system that deploys a multi-trillion-parameter model to execute a simple data lookup is not intelligent, but wasteful," the release notes argue. "The future belongs to systems that know not just how to solve a problem, but which machinery to deploy for the lowest possible cost."

## The ceiling, without the ceiling's suppliers

Fugu Ultra v2 is the more interesting claim. It scores 48.3 on Chartography, a visual-reasoning and data-interpretation test, against 27.3 for Opus 5 and 29.5 for Fable 5, and 74.3 on DeepSWE. It takes best or joint-best on five of eight benchmarks and places top-two on seven of eight.

The footnote under the chart is the story: Fable 5, Fable 5.1 and GPT-6 Astra are not in Ultra v2's agent pool. Sakana is claiming frontier-tier output assembled entirely from models that are not frontier-tier — a direct rebuttal to the assumption that orchestration is just a wrapper around somebody else's best model. Sakana frames this as insurance, citing the export controls that pulled Fable and Mythos offline worldwide earlier this year. In June it put the argument plainly: relying on one company's APIs for critical infrastructure "is a material vulnerability."

Pricing did not move for Ultra. It stays at $5/$30 per million, with $10/$45 above 272K tokens of context — the same card it carried in June as v1.0 and in July as v1.1. Three versions, one rate sheet.

## Where the discount goes

The 40-60% number describes visible tokens. An orchestrator produces a lot of tokens that are not visible.

Sakana's pricing page is candid about this, and the wording matters: orchestration tokens "represent real token usage outside of the input and output tokens and will be counted in the final price of the request. The price will be the same as standard input and output tokens." They sit in their own usage fields and are additive, not a breakdown of the output count — unlike OpenAI's reasoning-token accounting, which Sakana explicitly distinguishes itself from. What Sakana never publishes is how many a typical request generates.

TokenCost's Ankit Aglawe worked out where the saving dies. On a coding-agent turn of 30,000 input and 2,000 output tokens — the shape most buyers of a cheap orchestrator actually have — Fugu Max stops being cheaper than Sonnet 5 at 11.1% orchestration overhead. That turn is 94% input, and on input Fugu Max has no discount at all: $2.00 is exactly what Anthropic charges for Sonnet 5 and OpenAI for Terra. The entire saving is $4 per million on 2,000 output tokens, or eight tenths of a cent. One uncached internal re-send of that prompt costs six.

Sakana's technical report says Ultra is trained to design workflows of up to five steps, and its documentation elsewhere notes that each internal call re-sends the full prompt including history and prior tool results. Five steps over a 50,000-token context is a quarter-million input tokens for one turn.

Fugu Max's card — $2.00, $6.00, $0.25 cached — matches Qwen3.8 Max to the cent on all three lines. Qwen3.8 Max is a single model, sits on Sakana's own comparison chart, and beats Fugu Max on CharXiv, 88.4 to 88.1. As Aglawe put it: "A fixed card on a pool whose top-tier member is unnamed is a bet that Sakana's routing keeps the expensive member idle often enough for $6 to cover it."

## What routing does to pricing power

If this works, the interesting casualty is not any individual model. It is the ability of a lab to charge a premium for being the default endpoint.

An orchestrator that is genuinely model-agnostic turns frontier APIs into interchangeable inventory. Sakana's FAQ says it expects roughly two weeks to fold a newly released frontier model into the pool — the price card is fixed while the supply underneath it churns. Value migrates from whoever owns the weights to whoever owns the traffic, and the labs become utility suppliers bidding into a router they cannot see inside. Sakana already distributes through OpenRouter, Vercel, opencode, Creao and Merge.

The caveats mostly repeat the ones that dogged Fugu's June debut. Every Fugu score here is Sakana's own; Artificial Analysis lists no Sakana model, and its fugu-max page returns a 404 — awkward for a launch chart whose ninth panel is an Artificial Analysis benchmark. Latency is the recurring complaint: Ethan Mollick called Fugu Ultra "incredibly slow" in June, with coding tests running 30 minutes; Hamel Husain judged it strong on code review and "a bit jagged in its abilities" elsewhere. OpenRouter's day-one readings for Max ranged from 38 to 72 tokens per second. There are no open weights, and the service is not sold in the EU or EEA.

## What to watch

Whether Sakana publishes an orchestration-overhead figure — without one, the headline discount is unfalsifiable and every cost tracker reading `input_tokens` and `output_tokens` under-reports the bill. Whether any independent evaluator scores Fugu Max at all. And whether the labs respond by shipping their own routers or by tightening terms on the pooled access that makes Fugu possible.
