# QPILOTS Steers Flow and Diffusion Policies at Test Time, Sidestepping Brittle RL Fine-Tuning

If you want a robot to pour coffee, sort screws, or thread a cable, the most expressive way to teach it right now is to clone a human demonstrator with a generative model. Diffusion and flow-matching policies do exactly this: instead of predicting a single action, they learn the full distribution of plausible actions and sample from it, capturing the messy, multi-modal way people actually move. They are the workhorses behind much of the recent progress in robot learning. The catch is that imitation only gets you as far as your demonstrations. To push a policy past its teachers, you usually reach for reinforcement learning, and that is where things get painful.

A new paper, "QPILOTS: Efficient Test-Time Q-Steering for Flow Policies" (arXiv:2606.14801, announced June 16, 2026), argues that you can get much of the benefit of RL-based improvement without ever fine-tuning the generative policy at all. Instead, the authors propose steering a frozen, pre-trained flow or diffusion policy at inference time using a learned value function, nudging its samples toward higher-reward actions.

## Why TD-RL on diffusion policies is hard

The standard recipe for policy improvement is temporal-difference (TD) learning: train a critic that estimates the long-run value of actions, then push the policy to favor whatever the critic scores highly. With a simple Gaussian policy this is clean. With a diffusion or flow policy it is not.

The trouble is that these policies do not produce an action in one shot. They generate it through an iterative denoising or integration process, running many small steps to turn noise into a usable action. To backpropagate a value signal into the policy weights, you have to differentiate through that entire multi-step sampling chain. The authors, echoing a now-familiar complaint in the field, note that this is expensive, memory-hungry, and prone to instability: gradients explode or vanish across the chain, the critic and the generator co-adapt in unhealthy ways, and the carefully learned demonstration distribution can collapse. In practice, RL fine-tuning of these expressive policies is brittle and often undoes the very behaviors that made imitation learning attractive in the first place.

## What QPILOTS does

QPILOTS keeps the generative policy frozen and moves the optimization to test time. The pieces are familiar but the assembly is the point. First, a reference policy is trained the easy way, with plain behavioral cloning on demonstrations. Separately, a critic, a Q-function, is trained with standard TD learning to estimate action values. Neither training process has to differentiate through the other, so both stay stable.

The novelty is in how the two are combined at inference. Rather than fine-tuning anything, QPILOTS uses the critic to *steer* the sampling process of the flow policy as it runs. As the policy integrates from noise toward an action, the Q-function's signal is injected to bias the trajectory toward higher-value regions while keeping the sample inside the distribution the policy already knows how to produce. The authors frame the contribution as making this steering *efficient*, the engineering question that separates a clever idea from a usable one, since naive guidance can mean repeated, costly critic evaluations at every step of every rollout. The "pilots" framing is apt: the generative policy still flies the plane, and the Q-function is the navigator adjusting the heading.

This places QPILOTS in a fast-moving cluster of 2026 work on test-time steering of flow policies, alongside gradient-guidance methods such as Q-Guided Flow and value-guided denoising schemes. The shared bet across these efforts is that improvement and generation can be cleanly separated: learn a good value estimate once, then exploit it at deployment without touching the generator.

Because the specific arXiv record was not yet indexed at the time of writing, this account leans on the paper's stated framing and the surrounding literature rather than reported benchmark figures. Readers should treat throughput and success-rate claims as pending verification against the full text.

## Why test-time steering matters for robots and agents

The appeal here is more than tidy engineering. A frozen policy that you steer with an external value signal is modular in a way that fine-tuned policies are not. You can swap critics for different tasks, re-weight objectives on the fly, or impose new constraints at deployment without retraining the expensive generative model, an attractive property when the base policy is a large, hard-won imitation model.

It also changes the safety and reliability story. RL fine-tuning that quietly degrades a demonstration-cloned policy is a real hazard in robotics, where a regressed behavior can mean a dropped object or a collision. Keeping the generator frozen means the worst case is bounded by what the imitation policy already does; steering can only nudge within that envelope. For the broader world of agents, the same logic applies anywhere an expressive generative model needs to be pointed at a reward without being destabilized by it.

The trade-off is the obvious one. Test-time guidance shifts cost from training to inference, and a frozen policy can only be steered toward actions it was already capable of imagining. If the demonstrations never covered a behavior, no amount of Q-steering will conjure it.

## What to watch

The questions that will decide whether QPILOTS sticks are practical. How much does steering slow down inference, and is that acceptable for real-time control? How far can a frozen policy actually be pushed before guidance runs out of room? And does the approach hold up on physical hardware, not just simulation, where the gap between a value estimate and reality is widest? If the efficiency claims survive contact with real robots, test-time Q-steering could become the default way to squeeze more out of expressive policies, leaving brittle RL fine-tuning as the method of last resort.
