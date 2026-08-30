Eight in ten engineers now reach for an AI agent every single day. Just over a third of them say the biggest thing stopping them from using more is that they cannot reliably keep track of what those agents actually did.

That gap — between how fast engineering teams adopted agents and how little of the plumbing needed to run them dependably actually exists — is the through-line of Temporal's second annual State of Development Report, released Wednesday, August 26. Based on 554 usable responses from software engineers, architects and engineering leaders in the US and UK surveyed between April 29 and May 25, 2026, the report reads less like a victory lap for agentic coding and more like an audit of the debt it left behind.

The adoption numbers are genuinely startling. Daily-or-more agent use jumped from **47.3% a year ago to 80.8%** today, a 33-point swing in twelve months. The median respondent runs five agents; the mean is 10.7, dragged upward by outliers including one engineer who reported running 256. Nearly half the sample — 49.1% — now rates agents as in production or core to how they ship. And 51.3% say they can take an AI-generated prototype to production-ready code in hours or faster.

Then the other column of the ledger. Asked to name the top blocker to using agents more, **35.7% said tracking state**, ahead of debugging in second place and token or compute costs in third. Some 41.1% hit agent-related issues daily or more often, and 16.4% hit them hourly or more. Nearly 80% say token and compute costs are limiting their progress. And 39.5% named security concerns as the single largest obstacle to letting agents run fully autonomously — the top answer by a wide margin.

## The confidence gap

Temporal co-founder and CEO Samar Abbas framed the split bluntly in the report's announcement.

> Our second State of Development Report highlights how today's engineers have adopted AI agents faster than most teams have built the infrastructure to run them reliably, Abbas said. The data shows that the teams pulling ahead are those who trust their systems more, because they've solved for state, cost, and reliability.

Temporal sells durable execution, so it has an obvious interest in that diagnosis. But the survey's internal contradictions do the arguing on their own. **91.1%** of respondents say agents improved or revolutionized their productivity. **85.5%** trust agent outputs at least somewhat. And **84.5%** believe their own team uses agents better than competitors do — a statistical impossibility the report politely flags as unlikely. Leadership is more bullish than the people doing the work: CEOs, VPs and directors are 1.4 times more likely than engineers to call their organization very successful with agents, 43.7% against 32.4%.

## The rest of the week agreed

Temporal was not alone. Two days earlier, on August 24, Okta shipped general availability of Agent SSO, folding the open Cross App Access protocol into the core single sign-on product used by more than 20,000 customers. The pitch is that agents currently reach enterprise data through static API keys and one-off OAuth grants — operating, in Okta's phrasing, as anonymous traffic with no owner, no policy and no audit trail. Agent SSO registers a compliant agent in Universal Directory alongside human employees and issues short-lived, identity-governed tokens instead.

> AI agents are fast becoming a primary interface for how work gets done, but granting them access to enterprise systems shouldn't require trading away security or visibility, said Ric Smith, Okta's President of Products and Technology.

Okta's own AI Agents at Work 2026 research puts a number on the deficit: only **34%** of organizations apply the same security controls to AI agents that they apply to human workers.

And on the reliability side, Microsoft's Thinkingbox benchmark, open-sourced this month, supplied the sharpest number of all. Across 507 policy-conditioned business workflows run 20 times each against 12 proprietary and open-weight models, the strongest model scored **65.36% pass@1 but only 25.25% pass^20**. Succeeding once is not the same as succeeding reliably. Worse, many failed trials terminated cleanly with valid-looking tool calls — the agent did not crash, it just quietly did the wrong thing to a database.

## Why it matters

The industry spent 2025 and early 2026 arguing about which model was the best coding agent. This week's data suggests that argument is now mostly settled and mostly irrelevant. Model capability is not what is gating deployment; state, observability, identity and cost are. Tracking state beating debugging as the number one blocker is a specific, structural complaint — it says teams are running long-horizon processes on infrastructure designed for request-response software, and losing the thread when something crashes at step forty of sixty.

That reframing has commercial consequences. It moves budget from model licenses toward orchestration, durable execution, identity providers and evaluation harnesses — which is exactly why Temporal, Okta and Microsoft all shipped or published into the same week. It also explains why 39.5% cite security as the autonomy blocker rather than accuracy. An agent that is wrong is an annoyance. An agent that is wrong while holding a static API key with broad scope is an incident.

## What to watch

Three things over the next quarter. First, whether pass^k style reliability scoring — measuring consistency across repeated trials rather than best-of-n — starts appearing in vendor benchmark claims, or stays confined to research papers where it is less commercially awkward. Second, adoption of Cross App Access beyond Okta's launch partners; it is formally the enterprise-managed authorization extension for MCP, so its uptake is a decent proxy for whether agent identity becomes a standard or a checkbox. Third, watch Temporal's next survey for whether tracking state falls out of the top blocker slot. If it does not, the durable-execution vendors will have been right about the bottleneck — and two years of agent tooling will have gone into the fast part of a system whose slow part nobody fixed.
