---
headline: "When Agents Book Ahead: A Network Controller That Reserves Capacity for Calls It Hasn't Seen Yet"
slug: asge-rr-agentic-service-graph
category: research
story_number: 13
date: 2026-08-12
arxiv_id: 2608.06033
---

# When Agents Book Ahead: A Network Controller That Reserves Capacity for Calls It Hasn't Seen Yet

An AI agent rarely works alone. Ask a coding agent to fix a bug or a research
agent to summarize a field, and behind the single prompt sits a cascade of
remote calls: to language models, to memory stores, to search tools and code
sandboxes scattered across a network. Each call competes for the same finite
pool of compute and bandwidth. And here is the awkward part that most
orchestration systems ignore: you often do not know which calls are coming until
the agent gets there.

A new paper on arXiv, submitted August 6, 2026 by Trond Vatten and Yuming Jiang
of the Norwegian University of Science and Technology, treats that uncertainty
as a network-control problem rather than a scheduling afterthought. Titled
"ASGE-RR: Agentic Service Graph Embedding with Revisable Reservations for Dynamic
AI-Agent Calls," it argues that the shape of an agent's future work can be
partly predicted, and that predicting it well enough to reserve capacity in
advance lets more workflows finish on time.

## The problem: a graph that reveals itself as it runs

The authors give the underlying structure a name. As an agent executes, its
dependency calls to models, tools and stores "collectively form an agentic
service graph (ASG)." Unlike a conventional web request, where a load balancer
can see the job and route it, much of this graph is invisible at the start.
"Many dependency calls are revealed only at runtime," the paper notes.

That creates a trap familiar to anyone who has managed shared infrastructure.
Handing all available capacity to the call you can see right now may starve a
more valuable call that surfaces a moment later from a different workflow. The
greedy choice is locally sensible and globally wasteful. Vatten and Jiang
formalize the dilemma as Agentic Service Graph Embedding (ASGE): an online
problem of mapping runtime-revealed workflow calls onto specific service
replicas and network paths, all while respecting limits on capacity, cost and
deadlines.

## The proposal: reservations you are allowed to change your mind about

ASGE-RR is their answer, and the mechanism is right there in the name. Rather
than committing resources only when a call arrives, the controller looks ahead.
It "protects capacity for likely future calls while enforcing the constraints,"
evaluating candidate replica-and-path mappings against predicted continuations
of the workflow.

The word doing the heavy lifting is "revisable." Predictions about what an agent
will do next are, unavoidably, guesses. A rigid reservation built on a wrong
guess would be worse than no reservation at all, hoarding capacity for calls that
never come. So ASGE-RR treats each reservation as provisional: it "updates
reservations as new execution information becomes available." As the real graph
reveals itself, the bookings tighten or loosen to match. This is the difference
between a controller that plans and one that plans and then adapts.

## Method and results

To test the idea, the authors did not rely on synthetic traffic. They ran two
real agent frameworks, OpenHands and GPT Researcher, driving them with a model
they identify as gpt-5.6-luna, then replayed the resulting call patterns across
two contrasting testbeds: a controlled Docker environment and a wide-area network
(WAN) setup with real network distance and latency.

A first finding is diagnostic rather than about performance. Across every task
they examined, at least one runtime-revealed dependency call could be "steered
before connection establishment" -- meaning there is a genuine control point where
a system can intervene before the call locks onto a destination. Without such a
handle, the whole approach would be moot.

On performance, the authors are careful not to oversell small-scale experiments.
Their headline number: on the WAN testbed, ASGE-RR completed "(up to) 10 percent
more workflow value" than two baselines given the same information -- a
rolling-horizon controller and a controller that steers only the current call.
The gain comes precisely from the reservation logic: protecting resources for
likely future calls let more workflows finish within their deadlines.

## Why orchestration infrastructure matters

It is tempting to file capacity routing under plumbing, but the plumbing is
increasingly where agent reliability is won or lost. As agentic systems move from
demos to production, the bottleneck shifts from whether a model can reason to
whether a fleet of concurrent workflows can all get the compute and network paths
they need before their deadlines expire. A more capable model does not help a
task that times out waiting for a tool call. The contribution here is a way to
frame that contention as a first-class control problem, complete with a testbed
methodology grounded in real agent frameworks rather than abstractions.

The framing also reflects a subtler point: the runtime-revealed structure of a
workflow is not just noise to be endured. As the authors put it, it "creates a
new network control opportunity." Knowing the rough shape of what an agent tends
to do next is itself a resource.

## Open questions

The paper is candid about its limits. The testbeds are small, and a 10 percent
edge in a controlled setting is a signal, not a guarantee it survives at scale
with thousands of concurrent workflows and noisier predictions. Everything hinges
on the quality of those predicted continuations; the abstract does not detail how
robust the gains are when the predictor is wrong, or how much prediction
overhead the controller can absorb before it stops paying for itself. Whether
revisable reservations generalize beyond OpenHands and GPT Researcher, and how
they interact with cost as opposed to pure deadline pressure, are questions for
larger deployments. But as a formulation of a problem the field is about to hit
hard, ASGE-RR stakes out useful ground.
