# Xiaomi-Robotics-1 Debuts as a Foundation Model Trained on 100,000 Hours of Real-World Manipulation

Xiaomi's robotics team has entered the race to build a general-purpose brain for robots, and it has done so with one of the largest real-world manipulation datasets disclosed to date. In a paper posted to arXiv on July 16, 2026, the company introduced Xiaomi-Robotics-1 (XR-1), a vision-language-action (VLA) foundation model pre-trained on more than 100,000 hours of real-world manipulation trajectories. The pitch is straightforward and ambitious: a ready-to-use policy that can follow spoken instructions to manipulate objects in environments it has never seen, then be fine-tuned onto new tasks with only a handful of hours of demonstrations.

The release lands squarely in the middle of a 2026 wave of robot foundation models, alongside NVIDIA's Isaac GR00T family and a crop of academic VLA systems, all chasing the same prize: a single model that generalizes across robots and tasks the way large language models generalized across text.

## What Xiaomi Built

According to the paper, authored by the Xiaomi Robotics Team, XR-1 is trained in two stages. The first is a massive, largely embodiment-free pre-training phase. Rather than relying only on expensive robot-collected data, the team drew on over 100,000 hours of manipulation trajectories captured with UMI (Universal Manipulation Interface) devices, hand-held grippers that let humans record demonstrations without a full robot in the loop. That approach sidesteps one of robotics' central bottlenecks: real-robot data is slow and costly to gather.

The authors describe the model's capability in the abstract as "following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box," and "efficiently adapting to novel downstream tasks with minimal fine-tuning data."

A key ingredient, the team writes, is a "scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning." In plain terms, the system automatically writes descriptions of what changes in a scene during each clip, giving the model a language signal to tie actions to intent without armies of human annotators.

The second stage, post-training, aligns those broad capabilities with specific robot bodies and with the kind of casual imperative commands people actually use. Coverage of the release reports that this post-training phase used roughly 10,000 hours of cross-embodiment robot data, including more than 7,200 hours collected in real homes, though those specific figures come from secondary reporting rather than the abstract itself.

## The Scaling Argument

The paper's central claim is not just that XR-1 works, but that it scales. The team reports that performance "consistently improves with increased data scales and model sizes during pre-training," and, crucially, that this "scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments."

That is the load-bearing idea behind every robot foundation model: that pouring in more data and parameters yields predictable gains, the way it has for text and images. Xiaomi is arguing it has now shown that curve holds for physical manipulation.

On benchmarks, the numbers are specific. The paper states XR-1 "establishes a new state-of-the-art with a 57.6% success rate on RoboCasa365, surpassing the previous best of 46.6%," and reports an average score of 20.07 on RoboDojo, well ahead of the prior best of 13.07. Secondary coverage adds that on the standard RoboCasa benchmark the model reached a reported 74.5% average success rate, outperforming rivals including GR00T N1.6 and Pi-0.5, and that on unseen downstream tasks such as phone packing, printer refilling, and laundry loading, it hit a reported 75% success rate using under 10 hours of demonstrations per task, roughly double a Pi-0.5 baseline. Those downstream figures are reported by outlets covering the launch and are not stated in the arXiv abstract.

Xiaomi says code and model checkpoints will be released, and a GitHub repository and project page are already live.

## Why It Matters

For most of robotics' history, each robot and each task meant a bespoke controller. The foundation-model thesis flips that: train one large policy on enough diverse experience and it should transfer, the way a language model trained on the internet can draft an email or a poem it was never explicitly taught. VLA models, which fuse camera input, language understanding, and motor output into one network, are the current front-runner for that role.

What makes XR-1 notable is where its data comes from. By leaning on embodiment-free UMI recordings for the bulk of pre-training and reserving scarcer real-robot data for alignment, Xiaomi is attacking the field's hardest constraint: the sheer expense of teaching robots by having robots do things. If a scaling law genuinely holds when most of the training hours are cheap human demonstrations, the economics of building capable robots shift meaningfully.

The competitive context matters too. NVIDIA has pushed open VLA models like Isaac GR00T N1.6 and its Cosmos world models as infrastructure for the whole industry, and labs worldwide are converging on the same recipe. A consumer-electronics giant like Xiaomi entering with a 100,000-hour dataset signals how quickly embodied AI is moving from research demo to industrial priority.

The caveats are equally important. Simulation benchmarks like RoboCasa365 and RoboDojo are useful but imperfect proxies for messy real-world reliability, and success rates in the 50-to-75 percent range, while state-of-the-art, are far from the dependability a home or factory robot ultimately needs.

## What to Watch

The first test is whether the promised code and checkpoints let outside researchers reproduce the scaling curves, the strongest claim in the paper and the hardest to verify from a single lab's results. Watch, too, for independent real-robot evaluations beyond Xiaomi's own hardware, since out-of-the-box generalization is easy to assert and hard to prove across genuinely unfamiliar settings. And keep an eye on whether the UMI-heavy data strategy becomes a template competitors adopt. If cheap, embodiment-free demonstrations can carry the weight of pre-training, the next robot foundation models may look a lot less like robots collecting their own data, and a lot more like humans quietly recording the physical world.
