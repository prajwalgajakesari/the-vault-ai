# KAIST's VOTP Teaches Robots Human Judgment From a Handful of Videos

Five labels. That is how many human preference judgments a KAIST team needed to teach a robot arm to pick up a banana more reliably than standard baselines. Ten sufficed for opening a drawer. Aligning a machine to human intent normally means paying annotators to compare thousands of short clips, so that is a startling reduction — and it carried a paper from Professor Chang D. Yoo's lab at the Korea Advanced Institute of Science and Technology onto the Oral stage at ICML 2026 in Seoul this month.

The method is VOTP, which KAIST expands as Video-based Optimal Transport Preference; the paper's title is more literal: *Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning*. Its authors are PhD candidate Tung Minh Luu (first author), master's candidate Hwanhee Kim, Younghwan Lee, and Yoo, all of KAIST's School of Electrical Engineering. It was selected as an Oral, a slot given to 168 papers out of 23,918 submissions — roughly 0.7 percent — at the conference held at COEX in Seoul.

## The bottleneck

Reinforcement learning needs a reward function: a number that says whether what the agent just did was good. For a board game, that number is obvious. For a surgical robot placing a suture, or an autonomous vehicle threading a crowded intersection, it is not. Hand-engineering a reward that captures what a surgeon or a driver wants is brittle, so the field turned to preference-based RL: show a person two clips, ask which is better, fit a reward model to the answers.

That works, and it scales badly. As the authors put it, preference-based RL is a promising alternative to reward engineering, but its scalability is hindered by the large amount of feedback required. Every new task, robot, or definition of success restarts the labeling bill.

## How it works

The intuition is human: someone who watches a few good and bad demonstrations can recognize the same distinction in a clip they have never seen. VOTP tries to give a learning system that transfer.

Short slices of robot trajectory are treated as video and pushed through a pretrained video foundation model, which turns each clip into a vector in a latent space where behaviorally similar motions land near each other. Then — the actual contribution — the system applies optimal transport, a classical framework for moving one probability distribution onto another at minimum total cost, to align the small pool of human-labeled clips with a much larger pool of unlabeled ones. The resulting correspondences become pseudo-labels, and the reward model trains on human labels and pseudo-labels together.

The point is not to remove the human, but to make each judgment cover far more ground.

## What the numbers show

The team evaluated on D4RL locomotion benchmarks, MetaWorld manipulation tasks, and real hardware: a 7-degree-of-freedom Rethink Sawyer arm on a tabletop.

On D4RL locomotion, VOTP came close to an Oracle baseline handed synthetic labels for the unlabeled data — effectively an upper bound. On MetaWorld it beat P-IQL, a preference-learning baseline restricted to the same small labeled set. The most quotable result is the door-open task, where VOTP with 10 labels outperformed a policy trained on ground-truth rewards. Altering lighting, textures, and backgrounds in modified MetaWorld environments did not break it, which matters because real cameras do not see laboratory-clean scenes.

The hardware results deserve the most weight. From 50 teleoperated demonstrations collected by keyboard, themselves only 50 percent successful, the team used 5 preference labels for a LiftBanana task and 10 for DrawerOpen, then filled in the rest with pseudo-labels. Behavior cloning reached 20 percent success on LiftBanana and 40 percent on DrawerOpen. P-IQL reached 50 percent on both. VOTP reached 80 and 70 percent. Inspecting reward over time, the authors found P-IQL rewarding parts of trajectories that ultimately failed, while VOTP separated success from failure cleanly.

## Why few-shot preference learning matters

Preference data is the quiet cost center of embodied AI. Language models bootstrapped alignment from crowdworkers rating text; robotics cannot, because every label means watching a physical system move in a specific environment for a specific task. That cost is why so much robot learning still runs on hand-tuned rewards that generalize poorly.

A method that turns 10 labels into a usable reward signal changes who can afford this work: an engineer commissioning a new arm on a factory line could label a handful of on-site clips instead of funding a labeling campaign. Yoo frames it in those terms. The core of physical AI, he said, is making machines understand human intentions and choose the correct actions — and because VOTP can learn human judgment criteria from only a small number of videos, he called it a core technology that will accelerate the era of robots making human-like judgments.

## The caveats

This is a benchmark result, not a product. The tasks are LiftBanana and DrawerOpen, not suturing; the surgical-robot and autonomous-vehicle framing in KAIST's announcement is potential, not demonstrated capability. Seventy to 80 percent on a tabletop pick is strong against baselines and nowhere near safety-critical. The setting is offline RL, so pseudo-labels can only be as good as the fixed dataset's coverage. KAIST's world-first claim reads as institutional press language; semi-supervised and optimal-transport approaches to preference learning have prior art.

One oddity worth flagging: the public OpenReview record for this exact title and abstract sits under ICLR 2026, submitted September 2025, while KAIST and Korean outlets describe an ICML 2026 Oral. The venue trail is not fully documented publicly.

## What to watch

Whether VOTP holds up on long-horizon tasks with subtle failure modes, where a video encoder may not distinguish a good suture from a bad one at all. Whether the code and the choice of video foundation model are released — the method rests on that embedding space, and public materials do not name the backbone or its parameter count. And whether anyone reproduces the door-open result; a policy that beats ground-truth rewards on 10 labels is either a real signal or an artifact of one benchmark.
