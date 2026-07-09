The most-praised feature of diffusion language models may be quietly sabotaging their ability to reason. That is the uncomfortable conclusion at the heart of the paper that just won the top honor at the field's biggest conference.

On July 5, the program chairs of ICML 2026 named "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models" one of two Outstanding Paper Award winners, singling it out from more than a thousand accepted papers at the conference now underway in Seoul. Written by Zanlin Ni, Shenzhi Wang, Gao Huang and eight co-authors from Tsinghua University and Alibaba, the paper takes aim at a selling point that the diffusion camp has treated as gospel — and argues it has been getting in the way.

## What diffusion LLMs actually do

Almost every chatbot you have used, from GPT to Claude, is autoregressive: it writes one token at a time, left to right, each word conditioned on the words before it. Diffusion language models, or dLLMs, work differently. Borrowing the machinery that powers image generators like Stable Diffusion, they start with a sequence of masked or noisy placeholder tokens and progressively "denoise" them into real text, filling in positions across the whole sequence at once rather than strictly in order.

That design buys two things. The first is speed: because a dLLM can decode many tokens in parallel, it is not bottlenecked by generating words one after another. Commercial systems have leaned hard into this. Inception Labs' Mercury Coder, launched in early 2025, clocked upwards of a thousand tokens per second on an H100 GPU — roughly five to ten times faster than comparable autoregressive models. Google DeepMind's experimental Gemini Diffusion, unveiled at I/O in May 2025, reported similar figures. Open research models like LLaDA and Dream showed the approach could match autoregressive quality, not just outrun it.

The second thing the design buys is what the paper calls arbitrary order. A dLLM does not have to fill in tokens front to back. It can choose which positions to commit to first — commonly the ones it is most confident about — and leave the uncertain ones for later passes. This confidence-based, any-order decoding has been championed as the paradigm's signature advantage. The new paper argues it is also a trap.

## The forking-token failure

Here is the counter-intuitive finding. When a dLLM is free to write in whatever order it likes, it gravitates toward the easy tokens first and defers the hard ones. On general reasoning tasks — math, code, multi-step logic — the hard tokens are precisely the ones that matter. They are the moments where a proof could branch one of several ways, where a coding solution picks an approach, where the model has to commit to a direction. The authors call these high-uncertainty "forking" tokens.

By systematically postponing those decisions, the model lets already-committed context box it in, so that by the time it reaches a fork, the branch has effectively been chosen for it. The award citation puts it plainly: on general reasoning tasks, dLLMs "exploit this freedom to bypass exactly the high-uncertainty 'forking' tokens that matter most, collapsing solution diversity." In other words, the flexibility that was supposed to be liberating instead causes the model to route around its own hardest — and most important — choices, narrowing the range of solutions it explores. The committee flagged this as "a non-obvious failure mode that was far from evident before this work."

## The fix: make training boring

The proposed remedy is almost provocative in its simplicity. Rather than invent elaborate new machinery, the authors change what happens during reinforcement learning — the post-training phase where models sharpen their reasoning by trial and reward.

Their recipe, JustGRPO, treats the diffusion model as if it were a plain autoregressive one during RL rollouts, forcing a fixed left-to-right generation order while the model learns. That constraint pushes the model to confront the forking tokens head-on instead of dodging them, restoring the exploration that arbitrary order had quietly eroded. Crucially, the straitjacket comes off at inference: once trained, the model reverts to fast parallel decoding, keeping the speed advantage that made dLLMs attractive in the first place.

The results are competitive with — or better than — prior dLLM-specific RL methods, the team reports, hitting 89.1 percent on the GSM8K math benchmark and 45.1 percent on the harder MATH-500, all with standard Group Relative Policy Optimization and none of the diffusion-tailored complexity.

## Why It Matters

The autoregressive-versus-diffusion race is one of the more consequential open questions in generative AI. Diffusion's pitch has always been that it can be dramatically faster while giving up little in quality, and that its flexibility is a fundamentally different — perhaps superior — way to generate language. This paper complicates that story. It suggests the flexibility is real but double-edged: a genuine asset at inference, a liability during training if applied naively.

For a young paradigm still trying to prove it belongs alongside the autoregressive incumbents, that is a load-bearing insight. It reframes the design conversation away from "how much freedom can we give the model" toward "when should that freedom kick in." As the citation notes, the work highlights a still under-explored question: which sampling strategy should actually drive RL rollouts in dLLMs.

## What to Watch

Watch whether the JustGRPO idea shows up in the next wave of commercial diffusion models — whether labs like Inception and DeepMind adopt fixed-order training while preserving parallel inference. Watch, too, for pushback: the finding rests on general reasoning tasks, and diffusion's defenders may argue arbitrary order still pays off in domains like infilling and editing where it was always most natural. And note the broader lesson landing beyond diffusion — that a model's most celebrated capability can hide a failure mode nobody thought to look for.
