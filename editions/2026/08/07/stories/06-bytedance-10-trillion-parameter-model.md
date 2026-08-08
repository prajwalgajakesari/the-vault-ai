# ByteDance Trains a 10-Trillion-Parameter Model to Challenge Frontier Systems

The company best known for TikTok is now chasing something far larger than a viral feed. ByteDance is pre-training an artificial intelligence model with as many as 10 trillion parameters, a scale that would make it the biggest AI system ever built by a Chinese company and place it within striking distance of the frontier models developed in the United States, according to a Financial Times report picked up by Reuters on August 7, 2026. If the figure holds through training, it would mark one of the most ambitious bets yet in the accelerating contest between Chinese and American labs.

## What Is Being Built

The reported 10-trillion-parameter figure is roughly three and a half times the size of Moonshot AI's Kimi K3, which carries 2.8 trillion parameters and is the largest model any Chinese lab has publicly released. Before Kimi K3, the Chinese frontier sat lower: Meituan's LongCat-2.0 and DeepSeek's V4-Pro topped out around 1.6 trillion total parameters. ByteDance's project would leapfrog all of them.

The comparison that gives the number its weight is Anthropic. Industry estimates cited by the FT put Anthropic's most advanced Mythos 5 system at roughly 8 trillion parameters, with its more widely available Fable 5 sibling estimated near 5 trillion. That would put ByteDance's model close to, and by raw parameter count possibly beyond, the systems believed to sit at the top of the field.

Two heavy caveats apply. First, these numbers are reported, not confirmed. As Reuters noted plainly, "Reuters could not immediately verify the report," and ByteDance did not respond to a request for comment. The final parameter count has not been locked in and could shift before training completes. Second, the American figures are estimates: Anthropic and OpenAI do not disclose parameter counts for Fable, Mythos, or GPT-5.5, which makes any direct comparison inherently approximate.

Parameter counts also flatter the story more than they should. As Reuters put it, an AI model's parameters "refer to the numerical settings a model learns from data to recognize patterns, generate answers, and carry out tasks," and "are often used as a rough measure of scale, though not necessarily capability." At this scale, models almost certainly rely on a Mixture-of-Experts architecture, in which only a fraction of the total parameters activate for any given query. DeepSeek's V4-Pro, for example, holds 1.6 trillion parameters but reportedly activates only about 49 billion per token. Until ByteDance discloses its active-parameter ratio, "10 trillion" describes the model's storage and training cost far more than its real-world capability.

## The Founder's No-Shortcuts Order

Alongside the scale, a strategic signal drew attention. ByteDance founder Zhang Yiming has reportedly directed staff on the company's Seed research team to avoid distillation, the practice of training a new model on the outputs of a more powerful existing one, even if pursuing original research means falling behind domestic rivals in the short term.

That instruction lands in a charged moment. Distillation has become the flashpoint of Sino-American AI friction in 2026: U.S. officials have publicly accused Moonshot AI of running a large-scale distillation campaign against Anthropic's Fable model to build Kimi K3, an allegation Moonshot denied. For ByteDance, a founder-level pledge to avoid the technique reads as both an engineering conviction, a bet that genuine pre-training at scale produces a stronger model, and a legal hedge against the scrutiny now attached to the practice.

The work runs through ByteDance's Seed division, established in early 2023 in response to ChatGPT. Its foundational research is led by Wu Yonghui, a former vice president of research at Google DeepMind who joined ByteDance in February 2025, overseeing a team reported to number roughly 2,000 researchers.

## The Cost of Going Big

Pre-training at this scale is neither fast nor cheap. The phase typically runs three to six months before engineers move to fine-tuning, safety evaluation, and any release, meaning a model of this size would be unlikely to reach the public before early 2027. ByteDance has raised its 2026 AI capital spending plan to more than 200 billion yuan, roughly $30 billion, with about half earmarked for chips, a mix of Nvidia hardware and a growing allocation of domestic Chinese silicon as the company hedges against tighter U.S. export controls.

## Why It Matters

The story is a clean read on where the U.S.-China frontier race stands. For years the gap was measured in years; through 2025 and 2026 it has compressed to months. ByteDance is not integrating an American foundation model into a consumer app, it is training a frontier-scale system from scratch, and it already owns the distribution to deploy it: its Doubao assistant reached hundreds of millions of monthly users, second globally only to ChatGPT.

The move also tests the scaling thesis at a moment when many labs have pivoted toward efficiency and reasoning. ByteDance is wagering that raw scale, done with original data rather than borrowed model outputs, still buys frontier capability. And it does so under the shadow of export controls: the same restrictions meant to slow Chinese AI are pushing ByteDance to split its enormous chip budget between Nvidia and homegrown alternatives, an adaptation that controls were designed to prevent but may instead be accelerating.

## What to Watch

The number to wait for is not 10 trillion but the active-parameter ratio, the figure that will determine whether this rivals Mythos or merely matches it on a spec sheet. Watch, too, for the training timeline holding through late 2026, any confirmation from ByteDance itself, and whether Zhang Yiming's no-distillation stance survives contact with competitive pressure. Until a fine-tuned model actually ships, the most honest description of ByteDance's project is intention at unprecedented scale, with the hardest questions still unanswered.
