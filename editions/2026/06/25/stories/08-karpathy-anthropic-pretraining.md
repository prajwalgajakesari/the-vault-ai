# Andrej Karpathy Joins Anthropic to Use Claude to Make Claude Better

*The Vault — AI Edition · LLMs & GenAI · Story 08*

When Andrej Karpathy posted four sentences on X in May, the AI world stopped scrolling. "I've joined Anthropic," the OpenAI co-founder and former Tesla AI director wrote. "I think the next few years at the frontier of LLMs will be especially formative. I am very excited to join the team here and get back to R&D." The post drew roughly 11.3 million views, 102,000 likes, and 13,000 reposts — the kind of reach a frontier lab cannot buy. More than a month later, as Anthropic's hiring momentum keeps making headlines, the substance behind that move has come into sharper focus, and it is more pointed than a marquee name: Karpathy was brought in to use Claude to make Claude better.

## The mandate: model accelerating model

Karpathy started in mid-May on Anthropic's pre-training team, reporting to team lead Nick Joseph. Pre-training is the large-scale, brute-force phase that gives Claude its core knowledge and capabilities — and, as Anthropic itself notes, one of the most expensive and compute-intensive parts of building a frontier model. According to an Anthropic spokesperson who spoke to TechCrunch, Karpathy is standing up a new sub-team "focused on using Claude to accelerate pre-training research."

That phrasing is the whole story. The mandate is recursive: point the current model at the problem of building the next one. In practice that means leaning on Claude for hypothesis generation, experiment design, literature review, and the evaluation infrastructure that frontier research runs on. The bet is that a sufficiently capable model can act as a force multiplier on the researchers building it — a feedback loop sometimes shorthanded as "model accelerating model."

Karpathy is an unusually good fit for that brief. He is one of a small number of people who can move fluently between deep-learning theory and the messy reality of large-scale training runs. He co-founded OpenAI in 2015, worked on deep learning and computer vision, left in 2017 to lead Tesla's Autopilot and Full Self-Driving programs, returned to OpenAI for a year, then departed again in 2024 to start Eureka Labs, an AI-native education startup. Along the way he coined the term "vibe coding" in February 2025 and built the widely watched "Neural Networks: Zero to Hero" course. He signaled the education work is paused, not abandoned: "I remain deeply passionate about education and plan to resume my work on it in time."

## The compute-versus-research debate

The hire is a clear tell about how Anthropic intends to compete. The reflexive frontier strategy is to outspend rivals on chips — Anthropic has committed to multibillion-dollar arrangements for Amazon Trainium capacity and hundreds of thousands of GPUs. But raw compute is increasingly a commodity that OpenAI, Google, and well-funded challengers can all buy. Research productivity is harder to replicate.

Tapping Karpathy to build a team that turns Claude into a research accelerant is Anthropic's wager that AI-assisted research, rather than pure compute, is the edge that keeps it competitive with OpenAI and Google. If a lab can squeeze more useful experiments out of every GPU-hour by having the model design and triage the experiments, the effective return on a fixed compute budget rises. That is the productivity-multiplier thesis, and Karpathy's sub-team is the clearest institutional expression of it yet at a major lab.

The approach also fits Anthropic's broader narrative about recursive self-improvement and the trajectory toward more autonomous AI research. Pre-training has long been treated as the domain of scaling laws and capital; reframing part of it as a software-and-research problem the model itself can help solve is a meaningful conceptual shift.

## Anthropic's talent magnetism

Karpathy did not arrive alone. The same day, Anthropic announced it had brought on Chris Rohlf — a two-decade cybersecurity veteran of Meta and Yahoo's "Paranoids" team, and a former fellow at Georgetown's Center for Security and Emerging Technology — to its frontier red team, which stress-tests advanced models against severe threats. "We have a real opportunity in front of us to dramatically improve cyber security with AI," Rohlf wrote on X. "I can't think of a better company or team to join at this critical moment in time."

The pace has only intensified since. In June, Nobel laureate John Jumper — the DeepMind VP and AlphaFold co-creator who shared the 2024 Nobel Prize in Chemistry — announced he was leaving Google DeepMind for Anthropic, one of the most consequential research defections of the year. Ross Nordeen, a founding member of xAI, joined to help oversee the computing power and infrastructure expansion needed to train and run Claude. Stacked together, the run from OpenAI, DeepMind, Meta, and xAI reads as a talent magnet operating across every layer of the stack: pre-training, infrastructure, safety, and applied science.

That magnetism is itself a competitive asset. Frontier labs live and die on a few hundred elite researchers, and momentum compounds — top people want to work alongside other top people. Each high-profile arrival lowers the cost of the next recruit and raises the cost, in prestige and morale, for the labs losing them.

## Why it matters

For Anthropic, Karpathy is both a signal and a system. The signal is to the market and to rival recruiters: the company can attract one of the field's most recognizable researchers to an unglamorous, foundational problem. The system is the sub-team he is building — an attempt to convert Claude from a product into a research instrument that helps build its own successor.

The risk is that the recursive thesis is easier to state than to deliver. Using a model to accelerate the training of a better model assumes today's Claude is reliable enough to generate research direction worth following, not just plausible-sounding noise — exactly the kind of judgment that frontier evaluation is still struggling to measure. If it works, Anthropic will have found a way to bend the compute-versus-research curve in its favor. If it does not, it will have spent one of the industry's scarcest hires on a loop that does not yet close.

What to watch is whether Anthropic publishes any concrete result attributable to the model-accelerating-model approach — a pre-training improvement, a new evaluation, a research workflow — rather than another headline hire. The names are the easy part. Turning the current model into a measurable advantage for the next one is the bet that actually has to pay off.

---

*Sources: [TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/), [Axios](https://www.axios.com/2026/05/19/anthropic-openai-karpathy-andrej-claude), [CNBC](https://www.cnbc.com/2026/05/19/anthropic-hires-openai-cofounder-andrej-karpathy-former-tesla-ai-lead.html), [The New Stack](https://thenewstack.io/andrej-karpathy-anthropic-pretraining/), [TechFundingNews](https://techfundingnews.com/anthropic-top-10-hires/).*