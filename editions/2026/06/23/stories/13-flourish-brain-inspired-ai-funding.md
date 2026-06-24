# Flourish Raises $500 Million for Brain-Inspired AI, Backed by Jeff Bezos and Google Ventures

A New York startup that wants to stop approximating the brain and start reverse-engineering it has pulled in one of the year's largest early-stage checks — and one of its most recognizable backers.

Flourish, a secretive SoHo-based lab co-founded by Internet Explorer creator Thomas Reardon and former Amazon executive Rob Williams, has closed a roughly $500 million round at a $2.5 billion valuation, according to multiple reports published the week of June 4, 2026. The investor list reads like a who's who of frontier-tech capital: Jeff Bezos, Lux Capital, GV (Alphabet's venture arm), and Catalio Capital. Bezos alone is reported to have committed close to $100 million, nearly doubling an initial $50 million pledge after other marquee names piled in.

The pitch behind that capital is deceptively simple, and quietly radical: today's AI is built on a guess about how intelligence works. Flourish wants to replace the guess with a map.

## Studying the brain instead of approximating it

The dominant architecture in modern AI — the transformer — was never meant to be a model of biology. It is a statistical engine for predicting the next token, scaled to absurd size and trained on much of the internet. It works astonishingly well, and it is astonishingly expensive: a single chip inside a modern training cluster can draw tens of times more power than the human brain, which runs the most capable general intelligence we know of on roughly 20 watts, about the draw of a dim lightbulb.

Flourish's wager is that the gap is not a hardware problem but an architectural one. The company is building a system it calls Cortex AI, and rather than approximate neural behavior in the loose, metaphorical way that "neural networks" have for decades, it intends to study the real thing. Flourish is standing up an in-house neuroscience lab equipped with electron microscopes to map biological connectomes — the physical wiring diagram of neurons and their connections — and to extract the architectural principles that, in the company's telling, differ sharply from transformers.

The target spec is the headline. Cortex AI is designed to operate in the range of 20 to 50 watts, roughly the power budget of a laptop rather than a server rack. Two other goals sit alongside efficiency: continuous learning, the ability to keep learning after deployment rather than freezing knowledge at training time, and a dramatically smaller energy footprint per unit of capability.

"We are solving the two most difficult problems facing AI today: power efficiency and continuous learning," the company has said in describing Cortex AI as "the first synthetic intelligence system designed to match the computational capacity, learning efficiency, and power budget of the human brain." It is a framing that deliberately sidesteps the scaling-up arms race and reframes the contest around watts and adaptability.

## Who is behind it

If the science is unproven, the founders are not unknown. Reardon built Internet Explorer at Microsoft in the 1990s, then made an unlikely mid-career pivot into neuroscience, earning a doctorate and founding the brain-computer interface company CTRL-labs — which Meta acquired in 2019 for a reported $1 billion. He has spent the years since immersed in the wet biology of the cortex, which is precisely the credential Flourish's thesis demands. Co-founder Rob Williams is a former member of Amazon's senior leadership team, the kind of operator who knows how to turn a research ambition into infrastructure.

That pairing — a neuroscientist who has already sold a brain company to Big Tech and an Amazon S-team veteran — helps explain why investors who rarely chase moonshots together showed up at once. Bezos's near-doubling of his stake, reported by several outlets, reads as a signal as much as a sum: a bet that the power crisis dogging the AI build-out is real enough, and near enough, to reward an architectural long shot.

## Can a transformer alternative actually challenge scaling?

This is where caution belongs. The history of AI is littered with biologically inspired architectures — spiking neural networks, neuromorphic chips, predictive-coding models — that were elegant on paper and never dislodged the workhorse approach of the day. Transformers win not only because they are capable but because an entire industrial stack, from GPUs to data pipelines to talent, has been optimized around them. Displacing that gravity requires more than a better idea; it requires results at a scale that justifies retooling.

Flourish has not, as of publication, demonstrated a working model that matches frontier systems on benchmarks, and the company remains deliberately quiet about timelines and technical specifics. The connectomics-to-architecture pipeline it describes is genuinely hard science — mapping even small volumes of brain tissue at synaptic resolution is painstaking, and translating those maps into a trainable, useful learning system is an unsolved research problem, not an engineering sprint.

What the round does establish is that the efficiency thesis now has serious money behind it. As the cost and power demands of scaling transformers collide with grid constraints and capital discipline, the appetite for an architecture that promises laptop-level power draw is no longer fringe. Even a partial success — a model that learns continuously at a fraction of the energy, in narrow domains — would be commercially meaningful.

## What to watch

Three things will tell us whether Flourish is a genuine challenger or an expensive thought experiment. First, talent: whether it can pull leading neuroscientists and ML researchers into the same building, since its bet lives at that intersection. Second, a first artifact — any demonstration, however narrow, that a connectome-derived model can learn efficiently and continuously where transformers cannot. Third, the watts: if Cortex AI can show measured power figures approaching its 20-to-50-watt target on a real task, the scaling paradigm has a real rival. Until then, Flourish is the best-funded version of an old, alluring question — what if we just copied the brain? — now asked with $500 million and Jeff Bezos behind it.

---

**Sources:** [citybiz — Catalio's Neuroscience Startup Flourish Emerges With Funding from Bezos, Google Ventures](https://www.citybiz.co/article/856404/catalios-neuroscience-startup-flourish-emerges-with-funding-from-bezos-google-ventures/); [The Next Web — Internet Explorer creator Thomas Reardon raises $500M for Flourish](https://thenextweb.com/news/flourish-reardon-brain-inspired-ai-efficiency); [Tech Funding News — Bezos commits close to $100M to Flourish](https://techfundingnews.com/bezos-flourish-500m-brain-inspired-ai-power-crisis/); [Tech Times — Flourish trying to copy the brain to fix AI's power crisis](https://www.techtimes.com/articles/317921/20260606/jeff-bezos-bets-flourish-500-million-startup-trying-copy-brain-fix-ais-power-crisis.htm)
