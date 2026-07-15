When several AI agents talk out a hard problem and then take a vote, the crowd is supposed to be wiser than any single member. A new paper argues the crowd is often just louder, and that counting hands is one of the weakest possible ways to decide who is right.

In "Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge," posted to arXiv on February 10, 2026, researchers Wei Yang, Shixuan Li, Heng Ping, Peiyu Zhang, Paul Bogdan, and Jesse Thomason introduce a method they call AgentAuditor. Instead of tallying final answers across a team of language-model agents, it treats each agent's chain of reasoning as evidence to be inspected, compared, and adjudicated. The result, they report, is a system that reliably picks correct answers even when the majority is confidently wrong.

## The problem with counting votes

Multi-agent systems have become one of the most popular ways to squeeze more reasoning out of large language models: spin up several agents, let them reason independently or debate, then aggregate their outputs. The aggregation step, though, has stayed crude. As the authors write, "most frameworks still aggregate agent outputs with majority voting," a heuristic that "discards the evidential structure of reasoning traces."

The deeper danger, they argue, is a failure mode they call confabulation consensus, a situation "where agents share correlated biases and converge on the same incorrect rationale." Because agents built on similar base models tend to make similar mistakes, majority voting can systematically amplify a shared error. The wrong answer wins precisely because it is popular. A correct minority, holding the better argument, gets outvoted.

That is the gap AgentAuditor is built to close. Rather than asking how many agents landed on an answer, it asks which line of reasoning actually holds up.

## Auditing the tree instead of tallying the answer

The core move is structural. AgentAuditor "replaces voting with a path search over a Reasoning Tree that explicitly represents agreements and divergences among agent traces." In practice, the individual reasoning chains produced by the agents are merged into a single tree: where agents reason the same way, their paths overlap; where they split, the tree branches. Those branch points are the moments that matter.

From there, the method "resolves conflicts by comparing reasoning branches at critical divergence points, turning global adjudication into efficient, localized verification." Instead of trying to judge whole answers in one sweep, an adjudicator zooms in on the specific junctions where the agents disagree and checks which branch is better supported. It is a shift from grading essays to auditing the exact steps where two arguments part ways, which is both more targeted and cheaper than re-evaluating everything end to end.

The authors pair this with a training technique they call Anti-Consensus Preference Optimization, or ACPO. As the paper describes it, ACPO "trains the adjudicator on majority-failure cases and rewards evidence-based minority selections over popular errors." In other words, the adjudicator is deliberately taught on the hard cases where the crowd is wrong, and rewarded for siding with a well-argued minority rather than defaulting to consensus. That directly targets the confabulation-consensus trap, teaching the judge to resist the gravitational pull of agreement.

## What the numbers show

The authors stress that AgentAuditor is "agnostic to MAS setting," meaning it is designed to bolt onto existing multi-agent frameworks rather than replace them. To test that breadth, they evaluate across five popular multi-agent settings. The headline result: AgentAuditor "yields up to 5% absolute accuracy improvement over a majority vote, and up to 3% over using LLM-as-Judge."

Those margins deserve context. A few points of absolute accuracy may sound modest, but the comparison is against the two dominant aggregation strategies in the field. Majority vote is the default in most deployed multi-agent pipelines, and LLM-as-judge, in which a single model is asked to grade or pick among candidate answers, is the more sophisticated alternative most teams reach for next. Beating both, consistently and across settings, is the paper's central claim, and it locates the gains in exactly the cases where the two baselines are weakest: when the popular answer is the wrong one.

## Why this matters

As companies wire language models into agentic systems that plan, call tools, and hand work off to one another, the question of how to trust a collective answer stops being academic. A multi-agent pipeline that quietly rewards whatever its agents agree on is fragile in a specific and dangerous way: it is most confident exactly when correlated errors line up. Confabulation consensus is not a corner case; it is the natural consequence of running many similar models against the same problem.

AgentAuditor reframes reliability as a verification problem rather than a popularity contest. By preserving the reasoning traces and auditing the points of disagreement, it makes the aggregation step legible, showing not just which answer won but where the competing arguments diverged and why one branch prevailed. That transparency is valuable in its own right for anyone who has to debug or defend an agent's decision. And ACPO's design, training a judge to prize evidence over agreement, points toward verification layers that are explicitly hardened against the crowd being wrong.

The broader signal is that the industry's cheapest aggregation habits may be leaving reliability on the table. If a lightweight auditing layer can recover several points of accuracy without swapping out the underlying agents, the marginal cost of trustworthiness looks lower than assumed.

## What to watch

The open questions are about scale and cost. The paper reports gains of "up to" 5% and 3%, so the next thing to watch is how those improvements hold up on average across harder benchmarks, larger agent teams, and longer reasoning trees, where the number of divergence points, and the expense of auditing them, grows. Watch too for whether ACPO-style anti-consensus training generalizes beyond the settings tested, or whether an adjudicator taught to distrust the majority can be pushed too far toward contrarian errors. And with the work now public, the practical test is adoption: whether teams building production multi-agent systems begin replacing majority vote with reasoning-tree audits, and whether independent replications confirm that auditing the argument really does beat counting the votes.
