Teaching a robot to act the way a person would want it to act has long carried a hidden tax: someone has to sit and judge thousands of attempts. Was that arm's path smoother? Did that gait look more natural? Multiply those tiny verdicts by the tens of thousands of examples modern preference-learning systems demand, and the human-labeling bill becomes one of the quiet reasons "physical AI" has been slow to leave the lab.

A team at KAIST says it has found a way to shrink that bill dramatically. The group, led by Professor Chang D. Yoo of the School of Electrical Engineering, has developed VOTP — short for Video-based Optimal TransPort Preference — a technique that lets an AI absorb human intentions and judgment criteria from just a handful of preference videos rather than the usual mountain of hand-labeled comparisons. The work has been accepted to ICML 2026, to be held at COEX in Seoul this July, and was selected for an Oral presentation, a distinction reserved for 168 of the 23,918 submitted papers — roughly the top 0.7 percent.

## How VOTP Works

Conventional reinforcement learning from human feedback, or RLHF, asks a person to look at pairs of behaviors and pick the better one over and over, building up enough labeled comparisons to train a reward function. VOTP attacks the problem from the other end. It is a semi-supervised framework that starts from only a small set of labeled preference videos and then propagates that judgment across a large pool of unlabeled footage.

The trick is borrowed from two places. The first is the rapid maturation of Video Foundation Models (ViFMs), large pretrained networks that already encode rich visual representations of how things move. The second is optimal transport, a mathematical method — older than machine learning itself — for measuring how to map one distribution onto another at minimal cost. VOTP uses optimal transport to align visual trajectories inside the ViFM's representation space, effectively asking which unlabeled clips most resemble the behaviors a human already endorsed. From those alignments it generates high-fidelity pseudo-labels, letting the system learn an effective reward function from a fraction of the human supervision normally required.

In plainer terms: a video model watches subtle differences in how a robot behaves, and optimal transport does the bookkeeping needed to infer, across many clips, which actions a person would have preferred — without that person having to grade each one.

## What the Team Tested

The researchers did not confine the claim to simulation. According to the team, VOTP was evaluated across D4RL locomotion benchmarks, MetaWorld manipulation tasks, and real tabletop work using a seven-degree-of-freedom Rethink Sawyer arm. Across those settings, the method improved feedback efficiency and frequently outperformed standard preference-learning baselines given the same small label budgets — the apples-to-apples comparison that matters most for a paper whose entire pitch is doing more with fewer human verdicts.

The first author is Lou Minh Tung, a doctoral student in KAIST's School of Electrical Engineering.

Professor Yoo framed the stakes in human terms. "The core of physical AI is making machines understand human intentions and choose the correct actions," he said. Because VOTP "can learn human judgment criteria with only a small number of videos," he added, "it is a core technology that will accelerate the era of robots making human-like judgments."

## Why It Matters

The bottleneck VOTP targets is not exotic; it is the labor of preference labeling itself. Every system that learns what humans want — from a chatbot tuned by RLHF to a warehouse robot taught to handle fragile goods — pays for that alignment in human attention. When the price of teaching judgment falls from tens of thousands of comparisons to a few videos, the economics of building such systems shift. KAIST frames the payoff directly: less direct evaluation of robot actions means lower time and cost to develop robots, autonomous vehicles, and AI agents.

There is also a conceptual shift worth noting. Most preference learning treats human feedback as discrete clicks — this one, not that one. VOTP treats it as something closer to demonstration: show a few examples of good and bad behavior on video, and let the model generalize the underlying criterion. That moves the human's role from tireless grader toward occasional teacher, which is both cheaper and, arguably, more natural. The reliance on video foundation models also rides a broader wave; as those models keep improving, methods that piggyback on their representations stand to improve with them rather than requiring fresh engineering.

The Oral selection is its own signal. ICML's program committee reserves that slot for a sliver of accepted work, and landing it for a feedback-efficiency method suggests the field sees the labeling tax as a problem worth elevating, not just a tweak.

## What to Watch

The open question is generalization beyond curated benchmarks. Locomotion suites and a tabletop Sawyer arm are meaningful proofs of concept, but real deployments — kitchens, roads, factory floors — present messier video, harder edge cases, and preferences that vary person to person. How VOTP's pseudo-labels hold up when the unlabeled footage is noisier than the labeled set will determine whether the savings survive contact with the real world.

Watch, too, for the ICML presentation in July, where the team will field scrutiny on the quality of its pseudo-labels and the robustness of the optimal-transport alignment. And watch whether the broader RLHF community — much of it focused on language models rather than robots — adopts the video-plus-optimal-transport recipe for its own alignment pipelines. If learning judgment from a handful of videos travels well across domains, the technique could outgrow the robotics framing it arrived in.

---

*Sources: [Mirage News](https://www.miragenews.com/kaist-breakthrough-robots-now-mimic-human-1689467/), [Seoul Economic Daily](https://en.sedaily.com/technology/2026/06/10/kaist-develops-physical-ai-breakthrough-that-learns-human), [The Brighter Side of News](https://www.thebrighterside.news/post/robots-that-make-judgments-like-humans-are-coming-faster-than-we-think/), [ICML 2026 Oral listing](https://icml.cc/virtual/2026/oral/71090), [OpenReview](https://openreview.net/forum?id=wWvrC9oajI).*
