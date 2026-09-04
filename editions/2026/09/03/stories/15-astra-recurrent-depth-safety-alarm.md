# Astra Thinks in a Loop Instead of in Words. That Is Exactly What Worries the Safety Researchers.

For three years the industry's most reassuring answer to what a frontier model is actually doing has been the same: read the scratchpad. Reasoning models think by writing, in something close to English, and safety teams built an oversight apparatus on top of that text. OpenAI's forthcoming Astra model proposes a quieter answer. Some of the thinking will not be written down at all.

The Information reported Tuesday that Astra uses a technique called recurrent depth -- also described as opaque recurrence -- which lets the model do extra computation by cycling a query through the same block of the network repeatedly, rather than by emitting more reasoning tokens. TechCrunch's Russell Brandom followed on Wednesday, September 2. Within hours, the reaction from alignment researchers was less about Astra than about what comes next.

"I am extremely concerned by the reporting that Astra uses opaque recurrence," wrote Buck Shlegeris, chief executive of Redwood Research. "I don't know whether Astra is much less CoT monitorable than previous models. But if OpenAI pushes this technique further, they'll have the option to massively increase the recurrence and totally destroys CoT monitorability."

Redwood chief scientist Ryan Greenblatt was blunter about the trajectory. "My biggest concern is that a natural progression from here would involve scaling up the opaque reasoning to the point where the model reasons entirely or almost entirely in latent space," Greenblatt wrote. "I hope it isn't too late to avoid the most concerning architectures and that OpenAI will stop here."

## What Recurrent Depth Actually Is

The idea is simple. A conventional reasoning model gets better at hard problems by thinking longer, and thinking longer means generating more tokens. The chain of thought is literally the computation: each step is text the model writes to itself and reads back. That is why it can be logged and audited.

A recurrent-depth transformer buys extra computation differently. Instead of writing another paragraph, it runs the same stack of layers over its internal state again -- and again, for as many iterations as the problem warrants. What passes between iterations is a high-dimensional vector, not a sentence. Researchers call those contents neuralese: a representation the model reads perfectly well and a human cannot read at all.

The technique is not OpenAI's invention. A February 2025 paper by Jonas Geiping, Sean McLeish, Tom Goldstein and colleagues, published at NeurIPS 2025, laid out the recipe: a 3.5-billion-parameter proof of concept trained on 800 billion tokens, where unrolling the recurrent block at test time lifted reasoning benchmark scores up to a compute load equivalent to a 50-billion-parameter model. Unlike chain of thought, they wrote, the approach "can capture types of reasoning that are not easily represented in words."

That is the capability argument, and it is a real one: latent loops cost no context window, no output tokens and no serialization latency. If part of a model's cognition is geometric rather than verbal, forcing it through English is a tax.

## OpenAI's Position

OpenAI has pushed back hard. It says Astra's recurrence is deliberately bounded, the chain of thought remains legible, and the lab is not shifting to neuralese. Chief scientist Jakub Pachocki addressed it on X: "OpenAI has worked to preserve and utilize chain-of-thought monitoring since our very first reasoning models. It's a core goal of our current research program."

Several OpenAI researchers argued the reporting generated alarm out of proportion to a bounded choice, and on the narrow question they may be right; Shlegeris conceded he does not know whether Astra is meaningfully less monitorable than its predecessors. The objection is about precedent. TechCrunch reported Wednesday that Anthropic and Google DeepMind are already discussing the technique.

## Why This Matters

Chain-of-thought monitorability became a load-bearing safety assumption almost by accident. Auditability was never designed in; it fell out of the fact that the cheapest way to scale test-time compute happened to be generating human-readable text. In July 2025, roughly forty researchers from OpenAI, Anthropic, Google DeepMind and academia -- including Yoshua Bengio, Shane Legg, Greenblatt and Pachocki himself -- signed a position paper making that fragility the entire point. The title said it: chain-of-thought monitorability is a **new and fragile** opportunity. The window exists at the industry's discretion, and ordinary efficiency decisions can close it.

What breaks is not abstract. Chain-of-thought monitors catch stated intent to deceive, reward hack or exfiltrate before the action executes, and they are the primary forensic record afterward: in OpenAI's recent rogue-agent episode, those logs were central to reconstructing why the agents behaved as they did. Replace the transcript with activation vectors and oversight moves from reading to probing -- from a discipline any safety engineer can practice to methods that remain research-grade.

The caveat cuts both ways. No serious researcher treats a chain of thought as a faithful transcript; models already reason opaquely inside every forward pass. The window was always smudged. But a smudged window beats a wall, and architectures that remove it are easier to adopt than to undo.

## What To Watch

Three things. First, Astra's system card: whether OpenAI discloses the recurrence budget -- how many loop iterations the model is permitted -- and reports a monitorability evaluation alongside its capability evaluations. Astra has separately cleared a cybersecurity capability threshold, which makes the question less theoretical. Second, whether Anthropic and DeepMind ship latent recurrence in their next models, converting a one-lab choice into an industry default inside a release cycle. Third, whether the July 2025 signatories turn the commitment into a number; a disclosed monitorability score would let outsiders check that recurrence stayed bounded rather than take it on faith.

Zvi Mowshowitz, the longtime AI safety writer, called the technique "playing with fire, risking a taboo that OpenAI and Anthropic have fought to establish," and suggested the problem may need law rather than norms to survive a race. That is a large claim. It is also the first time this fight has been about an architecture rather than a policy -- and architectures, unlike policies, do not revert.