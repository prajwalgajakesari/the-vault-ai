# ACLArena Finds Forgetting in Multi-Stage Agent Post-Training Is Non-Monotonic

Teach an AI agent math, then web search, then online shopping, then how to follow instructions, and you might expect each new skill to stack on top of the last. A new paper says that is not what happens. When researchers put a Qwen3-8B model through that four-stage curriculum, its score on the AIME26 math benchmark rose to 25.83 after the math stage, held at 23.33 after search, fell to 6.04 after the e-commerce stage, and then climbed partway back to 10.21 once instruction-following training was done.

The paper, ACLArena: Agent Continue Learning in Multi-stage Post-training (arXiv:2609.23989), was posted on September 21 and was among the papers featured on Hugging Face's daily papers page. Haixin Wang is the lead author. The 12-person author list also includes Xiaoxuan Wang, Junkai Zhang, Alexander K. Taylor, Chenguang Wang, Jason Cong, Yizhou Sun and Wei Wang. The team frames its subject as a practical gap in how agents are built today. "Building general-purpose agents for industrial deployment requires integrating multiple capabilities, each typically acquired at a distinct stage of training," the authors write. "Yet there is currently no well-established recipe for Agent Continual Learning (ACL), with little understanding of the trade-offs among existing integration paradigms."

## A forgetting curve that goes up and down

Catastrophic forgetting, where new training overwrites old skills, is one of the oldest problems in neural networks. The usual picture is a steady loss: every new task costs a bit more of the old ones. ACLArena finds something messier. "Sequential training exhibits non-monotonic capability evolution," the paper states. Later stages can damage an earlier skill and then partly restore it, and the pattern differs from task to task. In the math example, the e-commerce stage did the most damage. The instruction-following stage that came after it gave back about four points.

The authors look at forgetting from two angles, the whole model and individual tokens. At the token level they find that most of the model's output barely changes from stage to stage. "Low-entropy tokens: ~95% remain stable across stages," the paper reports. The tokens that do get rewritten are the high-entropy ones, the uncertain decision points where the model picks between very different next steps. That suggests forgetting in agents is concentrated in a fairly small set of choices, not spread evenly across everything the model knows.

With that diagnosis in hand, the team tested three existing ways of combining skills learned at different stages: multi-teacher on-policy distillation, self-distilled fine-tuning (SDFT) and model merging. They compared how well each one recovers earlier capabilities while keeping new ones. Then they proposed their own recipe, which the abstract describes as combining "offline replay over high-quality trajectories with a routed network of multiple LoRA experts each specialized via RL."

## Mixture of Low-Rank Experts

The method, called Mixture of Low-Rank Experts (MLE), works in two steps. First, a shared backbone is built with SDFT, replaying high-quality trajectories from every domain, and then frozen. Second, a small LoRA adapter is trained with reinforcement learning for each stage. At inference time, an environment tag picks which expert gets attached to the backbone. Because each domain's reinforcement learning happens in its own adapter, a new stage cannot overwrite the weights an earlier stage depends on.

On the numbers reported, MLE comes close to independently trained single-domain experts, which are the ceiling the paper measures against. It scores 49.7 on Natural Questions against the expert's 49.9, 57.7 on single-hop search against 56.0, and 32.9 on the tau-cubed Retail e-commerce benchmark against 33.2. It also reaches 85.0 on IF-Eval. On AIME26 it scores 21.04, about the same as the paper's multi-teacher mixed on-policy distillation baseline at 21.25, and roughly double the 10.21 the plain sequential pipeline ended with. Training used the Slime RL framework on NVIDIA H200 nodes.

## Why It Matters

Multi-stage post-training is now standard practice for building agents. Labs add tool use, browsing, coding and domain workflows in separate stages, often run by separate teams and tuned on separate reward signals. ACLArena's main finding is a warning about how those pipelines are evaluated. If forgetting goes up and down instead of steadily down, a checkpoint that looks fine on an earlier benchmark after one stage could look very different after the next. Order matters, and a benchmark check at a single point in the curriculum can miss regressions that only show up later.

The token-entropy finding also points to a cheaper fix than retraining everything. If about 95 percent of low-entropy behavior stays stable, protecting a model mostly means protecting a small number of high-stakes decision points. MLE takes a blunter approach: it keeps each domain's RL updates in their own adapters so they never touch shared weights. For teams already serving LoRA adapters, a frozen backbone with routed per-domain experts is a fairly small change to their infrastructure.

There is a cost. Routing by environment tag assumes the system knows which domain a request belongs to. That is easy in a benchmark suite and harder in a general-purpose assistant, where a single task might mix search, arithmetic and a shopping cart.

## What to Watch

The authors describe the work as limited to Qwen3-8B-Base and a fixed four-stage curriculum, so it is still an open question whether the non-monotonic pattern holds for other model families, bigger models or different stage orders. The next tests will be whether other labs see the same up-and-down behavior when they report results after every stage, and whether MLE's routing still works when an agent has to switch domains in the middle of a task. The paper is 25 pages long and marked as under review, so a revised version may add some of those experiments.
