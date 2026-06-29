China's Open-Weight Models Now Hold the Entire Top of the Intelligence Index

For the first time, there is not a single non-Chinese name among the ten strongest open-weight large language models on the planet. The benchmark that says so is not a Beijing-friendly leaderboard but Artificial Analysis, the independent evaluator whose Intelligence Index has become a default scorecard for the industry. As of late June 2026, its v4.1 ranking of open models reads like a directory of China's leading AI labs — and the model sitting on top is GLM 5.2, released under a license that lets anyone download the weights and run them for free.

GLM 5.2, from the Beijing lab Z.ai (the company behind the GLM, or Zhipu, family), scores 51 on the Intelligence Index v4.1. That puts it ahead of NVIDIA's Nemotron 3 Ultra at 48, and well clear of a tight pack of fellow Chinese systems: MiniMax M3 and DeepSeek V4 Pro tie at 44, and Moonshot AI's Kimi K2.6 lands at 43. Crucially, the two highest-scoring open models that originate outside China — Google's Gemma 4 and NVIDIA's Nemotron line — are the exceptions that prove the rule. As Artificial Analysis put it in an earlier survey of the field, "The top 10 open weights models on the Intelligence Index are all from China-based AI labs."

## The labs behind the leaderboard

What is striking is not one breakout model but the depth of the bench. Z.ai's GLM 5.2 is a 753-billion-parameter mixture-of-experts model with only about 40 billion parameters active per token and a one-million-token context window — released, like its predecessors, under a permissive MIT license. DeepSeek, the lab whose V3 shocked markets in early 2025, is back near the top with V4 Pro and the MIT-licensed V4 Flash, the latter priced so aggressively (roughly $0.05/$0.24 per million tokens at realized rates) that it has reset cost expectations across the entire ecosystem. MiniMax brings native image and video understanding with M3; Moonshot's Kimi K2.6 remains a trillion-parameter contender; and Alibaba's Qwen family continues to seed the open-source long tail. These are not toy releases. GLM 5.2 now ranks second on the Code Arena WebDev leaderboard, behind only Anthropic's closed Claude Fable 5.

There is also a hardware subplot that complicates the usual export-control narrative. The entire GLM-5 series, by Z.ai's account, was trained on roughly 100,000 Huawei Ascend processors, with no NVIDIA silicon in the loop — a claim, if it holds, that undercuts the assumption that chip restrictions alone can throttle Chinese frontier progress.

## A narrow, stubborn gap

The case for alarm in Western capitals is tempered by one persistent fact: the open frontier still trails the closed one. Artificial Analysis pegs the leading proprietary models — OpenAI's GPT-5.5, Google's Gemini 3.1 Pro and Anthropic's Claude Opus line — a handful of points above the best open weights, and the gap widens on the hardest reasoning and agentic-coding evaluations. But it is not widening over time. "The intelligence and capability of open-weight models are keeping up with US frontier labs, and have been maintaining a consistent 3-6 month gap for over 18 months," OpenRouter's Chris Clark wrote in a late-June assessment. "The frontier labs do not (at this moment, anyway) appear to be accelerating away from open-weight labs."

For context on how fast this moved: a year ago, the best open model scored 22 on the same index and sat roughly 13 points below the leading proprietary system. The collapse of that distance — to a few points, indexed against models released within months of each other — is the real story.

## What it means for the global stack

The strategic consequence is that the cheap, deployable, modify-it-yourself layer of the AI economy is increasingly being defined in Chinese labs. When a company wants frontier-class agentic coding without paying GPT-5.5 prices — or wants to run weights on its own hardware for data-control reasons — the most attractive options on the board now carry MIT or similarly permissive licenses and Chinese provenance. That dynamic sharpened this month when a U.S. export-control directive forced Anthropic to disable broad access to its Fable 5 and Mythos 5 models to prevent foreign-national use, making an open, near-frontier alternative like GLM 5.2 newly appealing to organizations that simply need continuity.

NVIDIA's Nemotron 3 Ultra is the clearest Western answer — a fully open 550-billion-parameter model shipped with data, training recipes and an OpenMDW license, backed by the deepest pockets in the industry and an obvious incentive to keep open-model usage (and therefore NVIDIA inference demand) growing. Google's Gemma line persists. But for now they are chasing.

## What to watch

Three things. First, whether U.S. labs decide that ceding the open layer is a strategic mistake worth reversing with a serious open release of their own. Second, whether the Huawei-trained claim around GLM-5 proves durable enough to reshape the export-control debate. And third, the gap itself: it has held at three to six months for a year and a half. The day it starts widening — or closing to zero — is the day this story changes again.
