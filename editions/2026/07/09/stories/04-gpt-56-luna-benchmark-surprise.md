When OpenAI shipped the GPT-5.6 family on July 9, the marketing map looked reassuringly simple: three durable tiers, priced in a neat ladder. Sol, the flagship, sits at $5 input and $30 output per million tokens. Terra, the balanced workhorse, lands at $2.50/$15. Luna, the speed-and-throughput tier, undercuts everyone at $1/$6. The names are meant to signal a hierarchy of capability, with price tracking intelligence in a straight line.

Then developers opened the system card and found the ladder had a loose rung.

On Terminal-Bench 2.1 — OpenAI's own yardstick for command-line and agentic coding, the messy work of planning, iterating, and coordinating tools inside a terminal — GPT-5.6 Luna scored 84.3%. That put the cheapest tier in the lineup *above* Terra, the mid-tier model that costs 2.5 times as much on input and output alike. Luna's mark tied Claude Mythos 5, one of the strongest competing coding models on the board. Terra, sold to customers as "GPT-5.5-class at half the cost," came in below GPT-5.5 itself — which posted 88.0% on the same test.

For a benchmark that maps directly onto how modern coding agents actually operate, that is not a rounding error. It is an inversion of the price ladder.

## What the numbers actually say

The full Terminal-Bench 2.1 slate reads like a warning label for anyone routing by tier name. Sol Ultra tops the chart at 91.9%, with base Sol at 88.8%, edging past Claude Mythos 5 at 88.0%. Those results are unsurprising — you pay flagship prices, you get flagship terminal performance.

It is the bottom of the table that misbehaves. Luna, the tier explicitly built for "high-volume, latency-sensitive jobs where Sol-grade reasoning is overkill," outperformed the tier positioned one step above it. Analysts at ChatForest, comparing the two now-live models directly, framed it in cost-per-point terms: Luna trails Terra by less than two points on most agentic work while running at 60% of Terra's price — and on Terminal-Bench specifically, it doesn't trail at all. It leads.

None of this makes Terra a bad model. Across the broader benchmark suite, Terra "matches or comes within 2 to 3 points of Sol on most benchmarks at half the price," which is exactly the balanced-workhorse story OpenAI is selling. The problem is not Terra's average. It is the assumption that the average holds on every task.

## Tiers are averages, not promises

This is the point the specialist coverage keeps circling back to. DataCamp's analysis of the family put it bluntly: "Tiers are about the intelligence/speed/cost balance across many tasks, averaged out. It is not a guarantee on any one benchmark."

That sentence deserves to be pinned above every routing config in production. OpenAI's own framing supports it. In the GPT-5.6 naming scheme, the number denotes the generation while Sol, Terra, and Luna denote "durable capability tiers that can advance on their own cadence." Terra is optimized for general-purpose balanced performance. Luna is optimized for speed and throughput. Those are different objective functions, and different objective functions produce different peaks. Command-line agentic coding — tight loops, tool calls, fast iteration — happens to sit closer to what Luna was tuned to do well.

As DataCamp characterized the workhorse tier, Terra is "the default I'd start with for most production workloads, the way you'd pick a right-sized agent over a rule-based bot." Sensible advice. But "start with" is not "route everything to," and the Terminal-Bench result is the proof.

## The routing implication

For engineering teams, the practical takeaway cuts against instinct. The tidy price ladder invites a lazy heuristic: cheap job, use Luna; serious job, climb to Terra or Sol. On a large class of agentic coding work, that heuristic is not just suboptimal — it is backwards. Luna at $1/$6 may beat Terra at $2.50/$15 on command-line coding while costing 60% less. A team that reflexively routed its coding agents to Terra could be paying a premium for lower accuracy.

The models went live simultaneously in GitHub Copilot and the Responses API on launch day, so this is not a hypothetical for teams already wiring GPT-5.6 into agent pipelines. The correct move is unglamorous: build an evaluation set from your own task distribution and run both tiers against it. Tier names are a starting hypothesis, not a benchmark result. The system card gives you OpenAI's averages; only your traffic tells you where the peaks land for your workload.

## The bigger signal

The Luna surprise is a small anomaly with a large lesson attached. As frontier labs shift from single flagship models to families of specialized tiers, the intuition that "more expensive equals better at everything" quietly dies. A tier is a bet about balance across many tasks, and any single benchmark can — and here does — buck the ordering.

OpenAI built three models tuned for three different shapes of work. The pricing tells you what they cost. It does not tell you which one wins your specific race. On Terminal-Bench 2.1, the cheapest model in the family crossed the line first, and the only way to know whether it will do the same for you is to run the test yourself.
