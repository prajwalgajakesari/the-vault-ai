When a language-model agent learns to solve tasks by trial and error, it often finds a shortcut that works for exactly one problem and nothing else. It memorizes a brittle sequence of moves rather than a transferable habit. A 2026 arXiv paper, "Skill Reuse as Compression in Agentic RL," proposes a clean way to think about that failure and, more importantly, a way to train against it: treat a good agent as one whose behavior compresses well.

The work comes from Zhikun Xu, Yu Feng, Jacob Dineen, Taiwei Shi, Jieyu Zhao, and Ben Zhou, with affiliations at Arizona State University, the University of Pennsylvania, and the University of Southern California. It was posted to arXiv on May 29, 2026.

## The problem: agents that overfit to a single task

Agentic reinforcement learning (RL) has become a common way to push LLM-based agents past what prompting alone can do. The agent acts in an environment, gets rewarded for success, and updates its policy. The catch is that reward-chasing does not distinguish between a genuinely reusable strategy and a lucky, over-specialized one. Both get reinforced if they happen to work. The result is agents that ace the tasks they trained on and stumble the moment the setup shifts.

The authors' central hypothesis reframes this in information-theoretic terms: agents generalize better when their successful trajectories are structurally compressible, meaning they can be decomposed into a small set of reusable, abstract patterns. A brittle, one-off solution is, in this view, an incompressible one, a long string of idiosyncratic actions that share nothing with the agent's other successes.

## The core idea: compression as a training signal

The method, called ReuseRL, grounds agentic RL in the Minimum Description Length (MDL) principle, the classic idea that the best model of some data is the one that lets you describe the data most concisely. Here the "data" is the agent's own successful behavior.

In the authors' description, "ReuseRL extracts a shared skill dictionary from successful trajectories and augments the RL objective with a segmentation cost, explicitly penalizing idiosyncratic behaviors that encode poorly." In practice that means two things happen alongside ordinary reward optimization. First, the system mines recurring sub-sequences from trajectories that worked and collects them into a reusable skill dictionary, the shared vocabulary an agent can draw on across tasks. Second, the training objective adds a cost for behavior that cannot be cleanly segmented into those shared skills. An agent that keeps inventing bespoke, non-reusable move sequences pays a penalty; an agent that composes its answers out of the common dictionary does not.

The framing is elegant because it turns a vague goal ("learn general skills") into a concrete, optimizable quantity ("describe your successes with fewer bits"). The paper also backs the intuition with theory, proving a PAC-Bayes generalization bound for the compression penalty, which formally links how compressible an agent's behavior is to how well it should transfer.

## The results

The authors evaluate ReuseRL on three text-based agent benchmarks: ALFWorld, TextWorld-Cooking, and Countdown-Stepwise. Across all three, they report that ReuseRL improves both in-distribution and out-of-distribution success rates over vanilla GRPO, a standard RL baseline, as well as over strong round-length baselines. The out-of-distribution gains are the ones that matter most for the thesis: they are the direct test of whether compressible behavior actually transfers to unfamiliar variants rather than just polishing performance on the training tasks.

The paper does not appear to claim a single headline accuracy number so much as a consistent directional improvement across environments and distribution shifts, which is the appropriate way to argue a generalization result.

## Why it matters

Skill abstraction and hierarchical RL are old ideas: the field has long wanted agents that build a library of subroutines and recombine them. What is notable here is the specific bridge to compression. Instead of hand-designing a skill hierarchy or bolting on a separate discovery module, ReuseRL makes reusability a property the reward objective directly optimizes for, with an MDL justification and a generalization bound to match. It fits a broader 2026 wave of work on agent skill libraries and skill evolution, but it offers an unusually crisp answer to the question of what makes a skill worth keeping.

## What to watch next

The open questions are about scale and reach. These benchmarks are text-based and relatively contained; the interesting test is whether a compression penalty still helps on longer-horizon, tool-using, or multi-agent settings where skill dictionaries could grow large and noisy. Also worth watching: how ReuseRL's mined skills compare to those from the neighboring wave of skill-evolution and skill-library papers, and whether "compressibility" becomes a standard diagnostic for how well an agent will generalize before you ever test it out of distribution.
