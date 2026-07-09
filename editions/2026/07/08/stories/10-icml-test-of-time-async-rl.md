In 2016, a team at DeepMind taught a neural network to play Atari games — Breakout, Pong, Space Invaders — not on a rack of GPUs, but on a single multi-core CPU. The trick was to run many copies of the game at once, each with its own learner nudging a shared brain. A decade later, that same trick is quietly at the heart of how companies like OpenAI, Anthropic, and Google train the reasoning models you talk to every day.

On July 5, 2026, the International Conference on Machine Learning gave its Test of Time Award to "Asynchronous Methods for Deep Reinforcement Learning," the paper that introduced the algorithm known as A3C. Its authors — Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu — were mostly at DeepMind when they published it at ICML 2016. The selection was orchestrated by Kilian Weinberger, who chairs the awards process.

## What A3C Actually Did

Reinforcement learning is training by trial and error: an agent takes actions, receives rewards, and gradually learns a policy that earns more of them. The problem in 2016 was stability. The dominant method, Deep Q-Networks, leaned on a memory buffer called "experience replay" — storing past interactions and reshuffling them — to keep training from spiraling out of control. That worked, but it was memory-hungry and tied to a specific class of algorithms.

The A3C paper proposed something simpler. Instead of one agent replaying old memories, run many agents in parallel, each exploring its own copy of the environment on a separate thread. Because each agent is off in a different part of the game at any given moment, the stream of experiences they collectively feed into the shared network is naturally diverse — decorrelated, in the jargon — rather than a monotonous run of near-identical frames. That diversity did the stabilizing job that experience replay used to do, and it did it for free.

"The best performing method, an asynchronous variant of actor-critic, surpasses the current state-of-the-art on the Atari domain while training for half the time on a single multi-core CPU instead of a GPU," the authors wrote. The "A3C" name captures the recipe: Asynchronous, Advantage (a way of judging whether an action beat expectations), Actor-Critic (one network that acts, one that scores).

## The Through-Line to LLMs

For years this looked like a games-and-robotics result. Then large language models turned reinforcement learning into an industrial process. RLHF — reinforcement learning from human feedback — is what makes a raw next-word predictor into a helpful assistant. More recently, RLVR — reinforcement learning from verifiable rewards — is how frontier "reasoning" models learn to work through math and code, rewarded when their final answer checks out.

Here the bottleneck returns in a new form. Training a reasoning model has two phases: a rollout phase, where the model generates long chains of reasoning, and a learning phase, where those chains are scored and the weights updated. Generation is slow; if the learner has to sit idle waiting for every rollout to finish before it updates — the naive synchronous approach — expensive accelerators burn cycles doing nothing.

The fix is exactly the A3C insight: decouple the actors from the learner and let them run at their own pace. A wave of 2024–2026 systems — Asynchronous RLHF, LlamaRL, AReaL, Laminar, AsyncFlow, and others — do precisely this, generating rollouts on one pool of hardware while a learner trains continuously on another, tolerating the mild "off-policy" staleness that results. The engineering has grown enormously more sophisticated, but the core bet is unchanged: parallel actors, running asynchronously, make large-scale RL both faster and more stable.

## Why It Matters

The award citation makes the lineage explicit. Asynchronous RL, ICML wrote, "has been a major contributing factor to the success of RL in LLM post-training and has reshaped the way RL is performed in practice. The insight that parallel actor-learners stabilize learning has since inspired numerous successors."

That is a striking claim to attach to a paper whose original benchmark was arcade games. It underscores how much of the modern LLM stack rests on ideas incubated in the deep-RL boom of the mid-2010s — and how the same handful of DeepMind researchers, several of whom went on to work on AlphaGo and its successors, shaped both eras. The Test of Time Award is, in effect, the field acknowledging that the plumbing behind today's chatbots was drawn up years before anyone was training chatbots at all.

It is also a reminder of where the real leverage in AI often sits. A3C was not a bigger model or a cleverer loss function; it was a systems idea about how to organize computation. As RL post-training becomes the dominant cost center for frontier labs, those systems ideas — who runs where, how stale is too stale, how to keep the accelerators fed — are where a great deal of the current competition is being decided.

## What to Watch

The open frontier is how far asynchrony can be pushed before the staleness of off-policy data starts to hurt model quality. The 2025–2026 crop of frameworks is essentially a race to find that limit and design around it. Watch whether the next generation of reasoning models leans harder on fully decoupled, trajectory-level asynchronous training, and whether the efficiency gains show up where users can feel them: cheaper, faster, and smarter models. Ten years on, Atari's parallel actors are still setting the pace.
