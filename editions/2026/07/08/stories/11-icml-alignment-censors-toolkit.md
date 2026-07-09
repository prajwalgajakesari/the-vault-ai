The machinery built to keep AI models from teaching people how to make bombs is the same machinery a government can use to keep people from learning what happened in Tiananmen Square in 1989. That uncomfortable symmetry is the beating heart of the paper that just won one of the most prestigious honors in machine learning.

At the ICML 2026 awards, announced July 5 and presented this week in Seoul, "Position: The Alignment Community is Unintentionally Building a Censor's Toolkit," by Sarah Ball of LMU Munich and independent researcher Phil Hackemann, took the Outstanding Position Paper Award. Its thesis is blunt: the toolkit AI safety researchers have spent years perfecting to make models refuse harmful requests is inherently dual-use, and it is already being repurposed for censorship and political manipulation.

## The Argument

The authors draw a sharp line between their concern and the field's usual preoccupation. Most alignment work worries about a model that accidentally pursues the wrong goals. Ball and Hackemann worry about a human who does it on purpose.

"We are concerned with a human who deliberately weaponizes alignment pipelines," they write, "using the exact technical methods the community has spent years perfecting." The methods themselves — pre-training data filtering, reinforcement learning from human feedback (RLHF), constitutional AI, and cheap inference-time controls like system prompts and classifiers — are what they call "purpose-agnostic." Nothing in the math distinguishes suppressing a bomb recipe from suppressing a protest anniversary. Whoever controls the pipeline controls the values.

The paper organizes frontier models into three intervention layers — pre-training, post-training, and inference-time — and maps a distinct misuse profile to each. Inference-time control is the most alarming precisely because it is the most accessible: negligible compute, low technical skill, and, as the authors put it, "no retraining required."

## The Real-World Evidence

What lifted this beyond a thought experiment, and what the ICML committee singled out, was the documentation. The award citation praised the paper for challenging "the comfortable assumption held by some of us that we are a force for good, asserting that even value alignment — the primary tool we build to ensure AI does no harm — can be misused," and credited it with "compelling, real-world evidence."

That evidence spans the political spectrum. On the state-actor side, the authors point to Chinese models such as DeepSeek and Baidu's Ernie Bot being tuned to refuse politically sensitive topics, and to reporting that China's cyberspace regulator has pushed providers to assemble refusal datasets of thousands of prompts, roughly half aimed at political ideology and criticism of the Communist Party. On the private side, they cite Elon Musk's publicly stated plans to "fix" outputs from Grok he disagreed with — shifts later traced to system-prompt edits that steered the model toward his positions and, in some updates, produced antisemitic responses and Holocaust denial as catastrophic side effects.

Most unsettling is what they call "global contamination": studies showing Western models self-censoring when prompted in Simplified Chinese, not by design but because years of state filtering have shaped the available training corpus. Misuse at one point in the ecosystem, they argue, can propagate invisibly to models built anywhere.

## Why It Matters

The committee noted the paper's scope "generalizes to all authorities, present and future" — this is not an argument about any one government or company. The authors frame the timing as a convergence: growing public reliance on AI for information (Reuters put weekly use at 34 percent), a market concentrated in fewer than ten foundation model providers, and fifteen straight years of declining internet freedom.

The concern echoes a broader technical debate. Alignment researchers have increasingly embraced representation engineering and activation steering — techniques that isolate "directions" in a model's internal activations for concepts like refusal or truthfulness and dial them up or down. The dual-use logic is inescapable: a vector that suppresses toxicity can, with a sign flip, suppress dissent. Ball and Hackemann's contribution is to insist the community stop treating that fact as a footnote.

The paper sat alongside an honorable-mention position paper by Li Qiwei and colleagues on AI-generated non-consensual intimate imagery — a pairing that signals ICML's growing appetite for work interrogating whether the safety project is aiming at the right harms.

## The Other Side

To their credit, the authors are not calling for a retreat. "We do not argue for halting alignment research — its necessity is clear," they write. And many alignment researchers would offer a fair rejoinder: dual-use is not unique to alignment. Cryptography, biology, and virtually every powerful tool cut both ways, and abandoning safety techniques would simply cede the field, leaving models that harm users by default while doing nothing to stop a determined censor who could filter data by hand. The refusal machinery, defenders note, is also what lets a model decline to generate abuse material or bioweapon instructions. The honest disagreement is less about whether the risk exists than about whether more transparency or less capability is the better hedge.

## What to Watch

Ball and Hackemann propose three directions: verifiable alignment, so users can audit what a model was made to suppress; model pluralism, so no single actor monopolizes informational power; and plain awareness, starting with taking impact statements in papers seriously. Watch whether standardized benchmarks for information suppression and political bias actually materialize, whether venues like ICML begin demanding harder dual-use disclosures, and whether a field that just handed this argument its top prize is willing to act on it.
