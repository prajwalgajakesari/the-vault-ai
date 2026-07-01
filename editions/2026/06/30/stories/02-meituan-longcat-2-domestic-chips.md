---
headline: "Meituan Open-Sources LongCat-2.0, a 1.6-Trillion-Parameter Model Trained Entirely on Chinese Chips"
slug: meituan-longcat-2-domestic-chips
category: llms-genai
story_number: "02"
date: 2026-06-30
sources:
  - name: South China Morning Post
    url: https://www.scmp.com/tech/tech-trends/article/3358854/china-debuts-biggest-ai-model-trained-local-chips-meituan-releases-longcat-20
    domain: scmp.com
  - name: VentureBeat
    url: https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips
    domain: venturebeat.com
  - name: SiliconANGLE
    url: https://siliconangle.com/2026/06/30/chinas-meituan-open-sources-massive-longcat-2-0-ai-model-saying-trained-domestic-chips/
    domain: siliconangle.com
  - name: Geopolitechs
    url: https://www.geopolitechs.org/p/longcat-20-chinas-most-unexpected
    domain: geopolitechs.org
  - name: Crypto Briefing
    url: https://cryptobriefing.com/meituan-longcat-2-coding-model/
    domain: cryptobriefing.com
---

# Meituan Open-Sources LongCat-2.0, a 1.6-Trillion-Parameter Model Trained Entirely on Chinese Chips

A company most of the world files under "food delivery" just moved the goalposts in the U.S.-China chip war. On Tuesday, June 30, 2026, Meituan, the Beijing-based on-demand services giant, open-sourced LongCat-2.0, a 1.6-trillion-parameter large language model that it says is the first trillion-parameter system in the industry to complete both full pre-training and inference on a cluster of entirely domestic Chinese chips. If the claim holds up to independent scrutiny, it punctures one of the load-bearing assumptions behind Washington's export-control strategy: that denying China the newest Nvidia hardware would keep it from training frontier-scale models at home.

The distinction matters more than the parameter count. Chinese labs have run finished models on home-grown silicon for a while now. DeepSeek's flagship V4-pro, launched in April, leaned on domestic chips only for inference — the comparatively light task of answering user queries once a model is already built. Pre-training, by contrast, is where the real compute burden lives: the model chews through trillions of tokens to learn its basic patterns, and it is here that stability, memory pressure and chip-to-chip communication break down at scale. LongCat-2.0, Meituan says, cleared both hurdles on the same hardware.

"LongCat-2.0 was the industry's first trillion-parameter model to complete full-process training and inference on a 50,000-card domestic computing power cluster," the company said, describing a system built entirely on "large-scale clusters of tens of thousands of AI ASIC superpods" that demonstrate its ability to "conduct frontier-scale training on alternative hardware platforms." An ASIC, or application-specific integrated circuit, is a chip customized for a narrow workload rather than a general-purpose processor.

## A coding model that leaked out under a false name

LongCat-2.0 is a Mixture-of-Experts model: of its 1.6 trillion total parameters, only about 48 billion fire on any given token, which keeps inference costs manageable. Meituan trained it from scratch on more than 30 trillion tokens and tuned the architecture — sparse attention, dynamic token-level compute allocation — for agentic coding rather than generic chatbot performance. It ships with a 1-million-token context window, on par with DeepSeek's latest flagship.

The performance claims are not trivial either. Meituan reports a score of 59.5 on SWE-bench Pro, edging past GPT-5.5's 58.6 on the same coding benchmark. And developers had, in a sense, already been road-testing it. For weeks the model circulated anonymously on OpenRouter under the codename "Owl Alpha," climbing into the global top three by daily volume before Meituan pulled off the mask. "Owl Alpha on OpenRouter — that's us," the company's LongCat account wrote on X on June 29, confirming the stealth model had ranked first on Hermes Agent and second on Claude Code by monthly volume. The reveal meant LongCat-2.0 arrived with usage and a reputation already attached, rather than waiting for adoption to trickle in.

## Why it matters

The hardware stack is where the geopolitics concentrates — and also where the story gets murky. Meituan integrated the Huawei Collective Communication Library, the chip-to-chip plumbing that replaces Nvidia's NCCL and keeps a distributed training run from collapsing, and observers have pointed to Huawei's Atlas-950 SuperPods as the likely backbone. Yet Meituan has pointedly declined to name a chip supplier or SKU. Its official language, echoed across Xinhua and other state outlets, stops at "domestic chips." Huawei's Ascend line is the market's leading guess, but it remains a guess.

That silence has not blunted the significance. "In 2026, frontier-scale AI work can emerge from places that American policy and foreign investors were not watching closely enough," wrote the analyst behind the Geopolitechs newsletter, arguing that the binding constraint has quietly shifted. The old question was whether Chinese silicon could, in principle, replace imported accelerators at the high end. The newer, sharper question is whether domestic hardware plus enough brute-force systems engineering can support serious models for real users. LongCat-2.0 is an attempt to answer the second, and Meituan stresses it finished the run with "no rollback and no unrecoverable loss spike" — a nod to just how brittle 50,000-card training jobs can be.

None of this invalidates the logic behind U.S. export controls. Restrictions still raise costs, slow access and force Chinese firms into harder engineering trade-offs; LongCat-2.0 needed more tokens and more custom plumbing than a comparable Nvidia run might have. But the controls were meant to be a ceiling, not a speed bump, and a food-delivery company clearing that ceiling on open weights is not the outcome Washington was aiming for. It also feeds a broader open-weight contest in which Chinese labs — DeepSeek, Zhipu, Alibaba's Qwen and now Meituan — keep shipping capable models for free while U.S. frontier labs guard their best systems behind paid APIs.

## What to watch

Three things will determine whether LongCat-2.0 is a genuine milestone or a well-staged news cycle. First, whether the open weights and technical reports let outside researchers reproduce the performance and stability claims away from Meituan's own infrastructure. Second, whether the OpenRouter buzz hardens into durable developer adoption under the LongCat name, not just curiosity about the unmasking of Owl Alpha. Third, whether anyone — Meituan, its chip vendor or credible reporting — finally names the silicon that did the work. Until that last question is answered, the most precise thing to say is also the most tantalizing: China has claimed full-scale training on domestic chips, and has not yet said which ones.
