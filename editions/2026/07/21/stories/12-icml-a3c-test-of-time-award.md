# A 10-Year-Old Reinforcement Learning Paper Just Won ICML's Test of Time — and It's Everywhere in Today's LLMs

When eight DeepMind researchers published "Asynchronous Methods for Deep Reinforcement Learning" at ICML 2016, their headline result was a program that learned to play Atari games faster on a single multi-core CPU than earlier systems had managed on a bank of GPUs. A decade later, that same idea is quietly running underneath the reinforcement learning pipelines used to post-train frontier large language models. On July 5, ICML's program chairs made the connection official, naming the paper — and the A3C algorithm it introduced — the winner of the ICML 2026 Test of Time Award.

The recognition, announced ahead of the conference held July 6–11 in Seoul, singles out a specific through-line from a 2016 games benchmark to the 2026 era of RLHF and reasoning models.

## What the citation actually says

The award citation is unusually direct about why a reinforcement learning paper from the pre-ChatGPT era matters now.

"This paper pioneered asynchronous reinforcement learning (RL), which has been a major contributing factor to the success of RL in LLM post-training and has reshaped the way RL is performed in practice," the ICML 2026 program chairs — Alekh Agarwal, Miroslav Dudík, Sharon Li and Martin Jaggi — wrote in the official announcement.

They added: "The insight that parallel actor-learners stabilize learning has since inspired numerous successors and has built a lasting legacy within the machine learning community."

The selection process was orchestrated by Kilian Weinberger, a program co-chair of the original ICML 2016. All papers accepted that year were considered, citations and reputation narrowed the field to eight, and subfield experts were consulted before, in the chairs' words, "one paper emerged as a clear winner." The winning authors are Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver and Koray Kavukcuoglu.

## What A3C did, in plain terms

Reinforcement learning trains an agent by trial and error: the agent takes actions, receives rewards, and gradually adjusts its behavior to earn more reward. The hard part is that consecutive experiences from a single agent are highly correlated — one long game looks a lot like itself from moment to moment — and that correlation makes the learning signal noisy and unstable.

Before 2016, the dominant fix was a "replay buffer": store past experiences and shuffle them to break the correlation. A3C — short for Asynchronous Advantage Actor-Critic — took a different route. It ran many agents in parallel, each in its own copy of the environment, each exploring differently. Their updates were sent asynchronously to a shared set of parameters. Because the workers were doing different things at the same moment, their combined stream of experience was naturally decorrelated, no replay buffer required. The result was more stable learning, less memory overhead, and training that scaled across ordinary CPU cores.

The "actor-critic" half describes the machinery: an actor that picks actions and a critic that estimates how good a situation is, with the "advantage" measuring how much better an action turned out than expected. That template — actor, critic, advantage — is still the backbone of the algorithms used today.

## The line to modern LLMs

The connection the citation draws is not that today's models literally run A3C. They mostly do not; the field moved on to PPO, GRPO and their descendants. What survived is the architectural insight: separate the actors that generate experience from the learners that update the model, and run many actors in parallel and asynchronously to keep the pipeline fed.

That pattern is exactly what modern LLM post-training needs. In reinforcement learning from human feedback (RLHF) and in newer reinforcement-learning-with-verifiable-rewards (RLVR) setups, the expensive step is generating rollouts — having the model produce long chains of tokens that then get scored by a reward model or a verifier. Doing that generation in lockstep with training wastes enormous amounts of accelerator time. The systems used to train reasoning models and LLM agents instead run fleets of asynchronous rollout workers whose outputs feed a central learner, precisely the decoupling A3C introduced for Atari a decade earlier.

## Why it matters

Test of Time awards are, by design, a verdict rendered with hindsight, and this one reflects a shift in how the field reads its own history. A3C was a milestone in deep RL when it appeared, but for years its practical relevance seemed to fade as replay-based methods and, later, offline RL took the spotlight. The 2026 citation reframes it: the durable contribution was never the specific algorithm or the Atari scores, but the systems idea that parallel, asynchronous experience collection is what makes large-scale RL tractable.

That idea is now load-bearing infrastructure. The current wave of AI progress — reasoning models, tool-using agents, and the alignment pipelines that shape model behavior — leans heavily on RL post-training, and RL post-training at scale leans on asynchronous actor-learner designs. Honoring A3C is, in effect, ICML acknowledging that a plumbing decision from 2016 became one of the enabling conditions for the LLM era.

## What to watch

The open question is whether asynchrony's payoff outruns its cost. Asynchronous updates introduce "staleness" — actors generate data using a slightly out-of-date policy — and as models grow, managing that gap between rollout and learner becomes a central engineering problem. Expect the next round of research to focus on exactly this: how far off-policy asynchronous LLM training can drift before it destabilizes, and what new stabilizers replace the ones A3C made obsolete. If history rhymes, the systems idea that wins the 2036 Test of Time may already be hiding in one of this year's rollout schedulers.
