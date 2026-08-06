# 'Exploratory Sampling' Aims to Make LLM Outputs Genuinely Novel, Not Just Reworded

Ask a large language model for ten story ideas and you will usually get one idea wearing ten outfits. Turn the temperature up and the prose gets weirder, but the underlying thought rarely changes. That gap between surface variation and genuine novelty is the target of a 2026 decoding method called Exploratory Sampling, or ESamp, which tries to push a model toward ideas it has not already been circling.

## The problem with cranking up the temperature

Today's standard tools for diversity, temperature scaling and nucleus (top-p) sampling, operate on a single narrow slice of the model: the probability distribution over the next token. They can make a model more adventurous about which word comes next, but they are blind to meaning. Raise the temperature and you buy lexical variety, synonym swaps, reordered clauses, the occasional typo, while the semantic content stays put. Push too far and outputs degrade into incoherence. It is a blunt dial, and it explains a familiar frustration: sample a model a hundred times and the answers cluster, a phenomenon researchers call mode collapse.

The paper behind ESamp, titled "Large Language Models Explore by Latent Distilling" and posted to arXiv in 2026 (arXiv:2604.24927), reframes the goal. Instead of nudging the token distribution, it asks a harder question during generation: is this continuation actually taking the model somewhere new, or just retreading a well-worn path in its own head?

## A distiller that sniffs out novelty

The method's central trick is a lightweight component the authors call a Distiller, trained not offline but at test time, while the model is generating. Its job is to predict the model's deep-layer hidden representations from its shallow-layer ones, in effect learning to anticipate how information flows through the network's depth for the text produced so far.

The insight the authors lean on is a well-established property of neural networks: they make low-error predictions on inputs similar to what they have already seen, and higher-error predictions on genuinely unfamiliar ones. So the Distiller's prediction error becomes a novelty signal. When a candidate continuation is semantically familiar, the trajectory through the model's layers is easy to predict, and the error is low. When a continuation heads in an under-explored direction, the error spikes.

ESamp uses that error to reweight candidate token extensions conditioned on the current prefix, biasing decoding toward the less-explored semantic patterns rather than the safe, high-probability rut. As the paper puts it, the method treats "the prediction error as a novelty signal to reweight candidate token extensions," steering generation toward directions the model has not already committed to. Because the Distiller is trained on the fly, it continuously adapts to the mappings induced by the current generation context instead of relying on a fixed, pre-computed notion of what counts as new.

## What it costs, and what it buys

A test-time training loop sounds expensive, and that is the natural objection. The authors address it with an asynchronous training-and-inference pipeline that keeps the Distiller learning in parallel with generation. They report less than 5 percent overhead in the worst case, and roughly 1.2 percent in an optimized release, low enough to matter in practice rather than only in a lab.

On the results side, the paper evaluates across math, science, code, and creative-writing benchmarks, and reports that ESamp improves diversity and, notably, Pass@k efficiency for reasoning models, matching or beating strong stochastic and heuristic baselines. Pass@k, the odds that at least one of k samples is correct, is a telling metric here: if extra samples are just reworded copies, more of them does not help. Gains in Pass@k suggest the samples are genuinely exploring different solution paths, which is exactly the point. The authors have released code for the approach under the tLLM project.

## Why decoding-time diversity is suddenly a big deal

The reason this line of work matters goes beyond making chatbots less repetitive. Synthetic data generation, now a backbone of model training, collapses in value when a model keeps producing near-duplicates; genuine semantic spread means more coverage per generated example. Brainstorming and ideation tools live or die on whether the tenth suggestion differs from the first. Creative writing needs range that temperature alone cannot supply. And for reasoning, exploring distinct approaches is often the difference between solving a problem and failing k times in a row.

There is also a subtler stakes here. Post-training and alignment tend to sharpen models toward confident, average-sounding outputs, quietly narrowing the space they explore. Methods that restore semantic exploration at inference, without retraining, offer a lever to counteract that flattening.

## What to watch

The open questions are the usual ones for a fresh method: how ESamp holds up across model families and scales, whether the asynchronous overhead stays low under real production load, and whether "novelty" as measured by hidden-state prediction error reliably tracks the kind of novelty humans actually want. But the direction is the story. Diversity in language models is moving from a property you coax out of the token distribution to something a model can be actively guided toward in its own latent space, and that is a meaningfully different way to make machines surprising.

## Sources

- Zeng et al., "Large Language Models Explore by Latent Distilling," arXiv:2604.24927 (2026). https://arxiv.org/abs/2604.24927
- Hugging Face Papers, "Large Language Models Explore by Latent Distilling." https://huggingface.co/papers/2604.24927
- tLLM code release. https://github.com/LinesHogan/tLLM
