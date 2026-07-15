## An ICML 2026 Method Lets Small Models Reason Like Ones Three Times Their Size

For most of the last five years, the reliable way to make an AI model reason better has been to make it bigger. More parameters, more compute, more cost. A training method presented during ICML 2026 in Seoul this month challenges that reflex directly: it teaches a model to reach for only the handful of parameters that matter for the task in front of it, and in the process lets small models punch far above their weight.

The approach, which researchers describe as "selective activation sparsity," trains a model to use only the most relevant parameters for each specific task rather than firing its entire network for every token it processes. According to reporting on the first two weeks of July's research output, it was among the most-cited efficiency results to emerge from the conference. On reasoning benchmarks, models trained with the method performed comparably to models roughly three times their size.

That is a striking claim, and it lands in the middle of the year's dominant research storyline. "The biggest trend in AI research heading into July 2026 is the sustained improvement of reasoning-capable models," noted the Skycrumbs research roundup that surfaced the result, referring to models that "think" by generating chains of reasoning before answering. Efficiency work like selective activation sparsity is what makes that trend affordable.

## How the method works

The core intuition behind activation sparsity is old, but its application to reasoning models is new. In a dense transformer, essentially every parameter participates in producing every output. That is wasteful: a question about arithmetic and a question about legal reasoning do not require the same internal machinery, yet a conventional model activates all of it regardless. Sparsity research argues that only a small fraction of a network's neurons are meaningfully "on" for any given input, and that a model can be trained to lean into that structure rather than fight it.

Selective activation sparsity, as described in the July reporting, pushes this further by making the sparsity task-aware during training. Instead of pruning parameters permanently or routing tokens to fixed expert modules, the method trains the model to dynamically select the most relevant parameters per task. The result is a network that behaves like a much larger one when it needs to, while doing far less computation on any single pass.

The reported headline figure — matching models about three times larger on reasoning benchmarks — is the kind of ratio that, if it holds up under independent replication, reorders the economics of both training and deployment. The reporting was careful to hedge on scalability, noting the implications apply "if this approach proves scalable."

## The broader efficiency push at ICML

The result did not appear in a vacuum. Activation sparsity has become one of the more active corners of efficiency research, building on a lineage of work that has spent the last two years mapping how and why large language models leave most of their neurons idle. ICML 2026 was a natural venue for the next step.

The conference itself was unusually large. The Vector Institute alone reported 73 accepted papers at ICML 2026, its strongest showing at the venue to date, including 11 spotlight papers spanning "reinforcement learning and post-training for advanced reasoning" and "foundational work in optimization." Efficiency and reasoning were threaded through much of that portfolio, a sign of where the field's attention has migrated.

That attention is being reinforced from other directions. A separate preprint from MIT and Stanford researchers, circulated the same month, argued that success on hard mathematical and logical problems "isn't model size but rather how the model is trained to self-correct during the reasoning process." Taken together with the sparsity work, a common thesis is forming across the research community: the path to better reasoning runs through smarter training, not simply larger models.

## Why this matters

The most immediate consequence is cost. Training frontier models has become a capital-intensive arms race, and inference — the price of actually running a model for every user query — has quietly become the larger long-term bill. A method that lets a smaller model deliver the reasoning quality of a much larger one attacks both sides of that ledger at once. Fewer active parameters per pass means less compute burned per token, which translates directly into lower serving costs and lower energy draw.

The second consequence is where those models can run. If a compact model can reason like one three times its size, capable AI moves closer to fitting on devices with limited compute — phones, laptops, and embedded hardware — without a round trip to a data center. That has real implications for latency, privacy, and access, since on-device inference keeps user data local and works without a network connection. The July reporting explicitly flagged this: the approach matters "for running capable AI models on devices with limited compute, like phones and laptops."

There is a strategic dimension too. For most organizations, the constraint on deploying reasoning models has not been ambition but budget. Efficiency gains of this magnitude widen the set of players who can afford advanced reasoning at scale.

## What to watch

The obvious caveat is that the most compelling numbers come from conference reporting rather than a fully independent replication trail, and the researchers' own framing leans on the word "if." The questions that will decide whether selective activation sparsity becomes a standard technique or a footnote are concrete: Does the three-times ratio hold across model scales? Does the method degrade on tasks outside the reasoning benchmarks it was tuned against? And can the dynamic parameter selection be implemented efficiently on real hardware, where sparsity often looks better on paper than in a GPU's memory access patterns?

Watch, too, for whether frontier labs adopt the idea. The industry has already signaled a shift in where it spends training resources toward error correction and efficiency over raw scale. If selective activation sparsity survives scrutiny, expect the next generation of small, on-device reasoning models to look a lot less like miniature copies of their giant cousins — and a lot more like networks that have learned exactly when to think hard.
