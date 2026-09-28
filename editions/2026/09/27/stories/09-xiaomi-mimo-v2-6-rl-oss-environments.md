# Xiaomi Open-Sources 7,780 Reinforcement-Learning Environments Behind MiMo-V2.6

Model weights get the attention. The environments that shaped them are harder to come by. Xiaomi has now published both. A week after it released open weights for MiMo-V2.6 Pro and Flash, the company's MiMo team has put out **MiMo-V2.6-RL-oss**, a Hugging Face dataset of 7,780 agentic reinforcement-learning environments under the permissive Apache-2.0 license. It is the kind of training material that frontier labs usually keep to themselves or pay outside vendors large sums to build.

The dataset weighs in at 12.1 GB and is split into five subsets. According to the dataset card, the code subset holds roughly 2,700 software-engineering tasks graded by *executable tests*. About 2,090 visual web-development tasks are scored by *visual grading*. Roughly 1,000 cybersecurity tasks ask an agent to reproduce vulnerabilities and are checked by rule. Another 1,000 cover symbolic music composition, also checked by rule. The remaining 989 are general knowledge-work tasks judged against rubrics. Xiaomi has also published matching Docker images, so each software task comes with its own reproducible sandbox, along with its training code: a fork of verl, the open-source RL framework that grew out of the HybridFlow research project.

The software-engineering rows show how much work goes into each task. Each one bundles a realistic problem statement drawn from a real open-source project, a working directory, a dedicated container image such as a tagged *format-code-task* build, and a reward specification. The problems range from a Home Assistant integration that fails to expose air-quality readings to an S3 client that keeps retrying after its request context is canceled. Some prompts are written in Chinese. An agent can't just answer these tasks in text. It has to operate inside the container, and the result is scored by running code.

## What Xiaomi Is Actually Handing Over

Xiaomi presented the release as part of the MiMo-V2.6 launch, which covered the Pro-RL and Flash-RL models plus a smaller MiMo-V2.6-Distill-Qwen-9B checkpoint meant as a starting point for agentic RL research. eWeek, citing Xiaomi's figures, reported that the larger training runs used 1,568 prompts with 16 rollouts per training step, producing billions of tokens per update. Xiaomi put the cost of the RL phase at about **$2.62 million for Pro and $850,000 for Flash**, not counting pretraining. eWeek noted that those numbers have not been independently replicated, and that Artificial Analysis currently scores MiMo-V2.6-Pro at 46 on its Intelligence Index.

Put simply, anyone with enough GPUs now has the task set, the graders and the training code a Chinese hardware giant used to post-train a competitive open model. The public dataset page had logged 973 downloads and 348 likes at the time of writing. A community-built explorer Space has already appeared, as has at least one outside GitHub project that aims to extract reusable verifier patterns from the release.

Researchers noticed quickly. Harveen Chadha called the release unusually valuable in a post on X. Adithya S K described it as one of the largest open, cross-domain RL-environment releases to date, and Hugging Face researcher Elie Bakouch also highlighted the drop.

## Why It Matters

Over the past year, RL environments have become one of the scarcest inputs in AI. Labeled datasets were the key input of the chatbot era. Agents are trained instead in simulated workspaces that hand out rewards when a task is actually completed. Those environments are expensive to build and hard to make robust, so labs rarely share them.

TechCrunch reported last year that leaders at Anthropic had discussed spending more than $1 billion on RL environments over a single year. The report also described a group of startups built to supply them, including Mechanize, Prime Intellect and new divisions at data vendors Surge, Mercor and Scale AI. Mechanize was reportedly offering engineers $500,000 salaries to build environments for coding agents. "All the big AI labs are building RL environments in-house," Andreessen Horowitz general partner Jennifer Li told the outlet. "Everyone is looking at this space."

So a free drop of nearly 8,000 containerized, verifier-backed tasks matters. It lowers the barrier for academic groups and smaller labs, and it puts pressure on vendors whose pitch depends on environments being scarce. It also points to a view that open-source advocates have held for some time. "RL environments are going to be too large for any one company to dominate," Prime Intellect researcher Will Brown told TechCrunch.

The release also raises questions about how good the environments are. Reward hacking, where a model finds a shortcut that satisfies the grader without solving the task, is still the main weakness of the approach. "I think people are underestimating how difficult it is to scale environments," Ross Taylor, co-founder of General Reasoning and a former Meta AI research lead, told TechCrunch. "Even the best publicly available [RL environments] typically don't work without serious modification." Xiaomi's rubric-judged and visually graded subsets could be especially exposed, because those graders are softer than unit tests.

## What to Watch

The main test is replication. eWeek pointed out that Xiaomi's claims about which parts of its RL pipeline produced its gains have not been independently validated. The Distill-Qwen-9B checkpoint combined with these environments gives outside researchers a relatively affordable way to check them. Expect academic groups to post RL runs on the code and cyber subsets within weeks, and to start probing the verifiers for exploits.

It is also worth watching whether other labs follow Xiaomi's lead. If Chinese labs start releasing environments alongside their weights, the open-model race could move beyond checkpoints to the training infrastructure behind them. That shift would change the economics for environment startups selling to the same labs.

The cyber subset is the one to watch most closely. A thousand containerized vulnerability-reproduction tasks are a valuable training resource for defenders, and a free, Apache-licensed resource for anyone else too. How the community and regulators respond to open offensive-security training environments could become the release's most debated legacy.
