---
headline: "'RoboAlign' Teaches Robot Policies to Reason at Test Time, Tightening Language-Action Alignment"
slug: roboalign-vla-test-time-reasoning
category: research
story_number: 11
date: 2026-06-29
sources:
  - name: "arXiv (RoboAlign)"
    url: "https://arxiv.org/abs/2603.21341"
    domain: arxiv.org
  - name: "Do What You Say (runtime reasoning-action alignment)"
    url: "https://arxiv.org/abs/2510.16281"
    domain: arxiv.org
  - name: "The Robot Report (VLA explainer)"
    url: "https://www.therobotreport.com/vision-language-action-models-are-the-next-leap-in-autonomous-robotics/"
    domain: therobotreport.com
---

# 'RoboAlign' Teaches Robot Policies to Reason at Test Time, Tightening Language-Action Alignment

For the past two years, the dominant recipe for building robot brains has looked deceptively simple: take a powerful multimodal language model, teach it to "think" about the physical world through question-and-answer training, and trust that better reasoning will produce better actions. A new paper argues the recipe has a quiet flaw — and that fixing it means letting robots reason their way to an action, then grading the reasoning by whether the action actually works.

The work, titled *RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models* and posted to arXiv in late March 2026, comes from a team led by Dongyoung Kim with collaborators across KAIST, the robotics startup RLWRLD, Yonsei University, and UC Berkeley. Its central claim is blunt: improving a model's embodied reasoning does not reliably improve how well a robot moves. RoboAlign is the authors' attempt to close that gap.

## The problem: smarter talk, clumsier hands

Vision-language-action models, or VLAs, are the foundation-model bet in robotics. As The Robot Report puts it, VLAs integrate "visual perception, language understanding, and common-sense knowledge to provide a foundation for training generalizable robotic policies." The appeal is obvious — pretrained multimodal models already know what a "cup" is and roughly where one sits on a table, so a robot built on top of one needs far less hand-collected demonstration data to generalize.

The trouble is that knowing about the world and acting in it are different skills. "The performance and generalization of VLAs are often limited by the underlying MLLMs, which struggle with key embodied tasks required for action generation, such as spatial reasoning and temporal reasoning," the authors write. The field's standard fix has been to bolt on more reasoning training — visual question-answering about object relationships, affordances, or future trajectories. But that supervision is indirect. It teaches the model to describe a plan in language, not to emit the precise low-level motor commands a gripper consumes.

RoboAlign's most striking evidence is a counterexample. The authors note that RoboBrain 2.0, a model that "achieved the highest reasoning scores among evaluated MLLMs and even outperformed GPT-4o on major benchmarks," nonetheless "yielded the lowest VLA performance" in their tests. More reasoning, worse robot. The authors attribute this to "the modality gap between language and low-level actions; optimizing embodied reasoning purely through language supervision does not guarantee improvements in actual action generation."

## The method: reason first, then grade the reasoning by the action

RoboAlign reframes the objective. Instead of training a model to answer questions and hoping the skill transfers, it makes the model generate low-level action tokens *as the direct outcome of reasoning*, then judges that reasoning by how accurate the resulting action is.

There are two stages. First, supervised fine-tuning teaches the model to produce actions via zero-shot natural-language reasoning — literally thinking step by step inside `<think>` tags before committing to a motion. The paper shows the difference plainly: a model trained with reasoning data narrates, "the robot needs to move its gripper towards the cup, position it correctly, close the gripper to secure the cup, and then lift it up," whereas a model trained without it collapses into a degenerate loop ("Go to the cup. cup./think>cup./think>"). The coherent reasoning is what makes the second stage possible.

That second stage is reinforcement learning. Using GRPO — the same family of RL algorithm popularized by DeepSeek-R1 — RoboAlign samples diverse reasoning trajectories and rewards them based on a blend of correct output format and "FAST token prediction accuracy," measured as the prefix similarity between the generated action sequence and the target. In effect, the action becomes the verifier for the thought. This is the "test-time reasoning" in the title: the model deliberates before each action, and that deliberation has been tuned to land on motions that succeed.

Crucially, the alignment stage is cheap. The team reports doing it with "less than 1% of the data" used for the main fine-tuning.

## What the numbers show

RoboAlign was evaluated on two standard simulation suites — LIBERO and CALVIN, both using a Franka Panda arm — plus a real robot. The headline figures are relative improvements over a supervised-fine-tuning baseline of 17.5% on LIBERO, 18.9% on CALVIN, and 106.6% in the real-world setup.

The detail beneath those averages is more telling. On LIBERO, RoboAlign lifts the average success rate to 86.8%, ahead of strong recent reasoning-based VLAs like CoT-VLA (83.9%) and ThinkAct (84.4%). The biggest gains land on the hardest categories — long-horizon and goal-conditioned tasks — exactly where chained reasoning should help most. On CALVIN's zero-shot transfer to an unseen environment, the authors note that "while all baselines show drops in task completions of length 4 and 5, RoboAlign consistently improves performance across all sequence" lengths. And the approach beat alternative alignment targets: rewarding low-level actions outperformed rewarding high-level language plans (17.5% vs. 13.1%) or 2D point trajectories (15.2%).

## Why test-time reasoning for robots matters

The bet RoboAlign represents is bigger than one benchmark. Embodied AI is converging on the same lesson language models learned in 2024 and 2025: spending more compute to *think* at inference time can beat simply training a bigger or more knowledgeable model. The wrinkle in robotics is that there is no human grader for "did the robot succeed" — the physical outcome itself is the reward signal, which is exactly what RoboAlign exploits.

It is also part of a visible cluster of 2026 work attacking the same seam. Papers like *Do What You Say* propose runtime verification that a robot's textual plan and its actual motion agree, while others pursue verifier-free test-time sampling. The shared premise is that the language-action gap, not raw model size, is the binding constraint on generalist robots. If that holds, the next wave of robotics foundation models may compete less on parameter count and more on how well they reason in the half-second before they move.

## What to watch

RoboAlign is a preprint, and its real-robot evaluation rests on a modest 96 trials per task — promising, but a long way from the messy diversity of homes and warehouses. The open questions are whether action-grounded RL holds up across robot embodiments beyond the Franka arm, whether the reasoning overhead is tolerable for real-time control, and whether the approach scales to the dexterous, multi-step manipulation that generalist robots will ultimately need. The authors report that RoboAlign improves general embodied reasoning *without* degrading broad image understanding — a sign the alignment is additive rather than a trade-off. If that generalizes, "reason, then act, then learn from the result" could become a default loop for embodied models, the way chain-of-thought became one for chatbots.
