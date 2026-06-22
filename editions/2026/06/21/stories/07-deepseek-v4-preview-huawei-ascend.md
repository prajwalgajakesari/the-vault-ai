# DeepSeek V4 Preview Lands as a 1.6-Trillion-Parameter Model Trained on Huawei Ascend Chips

When DeepSeek dropped a preview of its V4 series, the headline number was hard to miss: DeepSeek-V4-Pro carries 1.6 trillion parameters, making it the largest open-weight model the world has seen. But the figure that will preoccupy policymakers in Washington and Beijing sits one layer down in the architecture. For the first time, a major Chinese frontier-adjacent model has been built around Huawei's homegrown Ascend silicon rather than Nvidia's GPUs — a quiet but consequential shift in the hardware substrate of the global AI race.

The Hangzhou startup released V4 across its website, mobile apps, and API, publishing the weights under a permissive license. The Pro variant uses a Mixture-of-Experts (MoE) design that activates just 49 billion of its 1.6 trillion parameters per token, paired with a one-million-token context window — an eightfold leap over V3's 128K. A smaller sibling, V4-Flash, runs 284 billion total parameters with 13 billion active, aimed at cheaper, faster inference.

## A Bigger Model, an Honest Footnote

DeepSeek is not claiming to have overtaken the American frontier — and unusually, it says so in writing. The company's own technical paper concedes that V4 "trails state-of-the-art frontier models by approximately 3 to 6 months," placing its reasoning and agentic capabilities roughly on par with GPT-5.2, Gemini 3.0 Pro, and Claude Opus 4.5 — models that shipped about half a year earlier.

The Council on Foreign Relations, which convened three fellows to assess the release, reached a blunt verdict. "This new DeepSeek model is not competitive with frontier U.S. models," wrote Chris McGuire, CFR's senior fellow for China and emerging technologies. "And while it is likely the best available open-source option, it does not provide evidence that Chinese AI firms are shrinking the gap with the United States."

That gap is broadly consistent with independent estimates that the U.S. holds roughly a seven-month lead over China — and may even be widening, as American labs increasingly use AI to accelerate their own next-generation development. CFR also flagged that V4 narrowly edges out domestic rivals: Moonshot's Kimi K2.6 and Zhipu's GLM 5.1 score comparably on most public benchmarks, and V4-Pro is priced higher than both. "The competitive gap within China is now much narrower than the gap between China and the United States," McGuire noted.

## Why the Huawei Ascend Move Matters

The most strategically loaded feature of V4 is not its parameter count but its hardware lineage. The model is optimized for inference on Huawei's Ascend chips rather than Nvidia's — reportedly at Beijing's direction — and was trained on Ascend 950 silicon. Huawei confirmed day-zero compatibility across its full Ascend SuperNode line, and a research group including Huawei completed full-parameter post-training of V4-Pro using a cluster of at least 1,000 Ascend 910C chips.

For years, the open question hanging over U.S. export controls has been whether China could not just design competitive models but train them at scale on domestic accelerators. V4 is the first major public answer in the affirmative. If Ascend can serve as a viable training and inference substrate for trillion-parameter models, the leverage of Nvidia-centric chip restrictions erodes at the margin.

CFR's Michael Horowitz, senior fellow for technology and innovation, argued the real contest lies elsewhere. "Second-best models carry enormous competitive value when they are cheap and open, which makes them easy to widely diffuse," he wrote, pointing to the Global South, "where countries are not choosing between GPT-5 and Claude Sonnet 4.6 but between accessible tools with different values baked in." Chinese models already log more downloads on Hugging Face than American ones. "The frontier is not the only front in the AI competition," Horowitz added. "The country that deploys AI fastest across its economy and government will shape the character of the AI era."

## Caveats Beijing Would Rather You Skip

The Huawei narrative comes with asterisks. Notably, where V3's technical report named its training chips, the V4 report is silent — and U.S. officials have asserted V4 was still partly trained on smuggled Nvidia Blackwell chips, which are banned in China. The White House and leading U.S. labs have separately accused DeepSeek of "industrial-scale" distillation attacks against American models, alleging the creation of more than 24,000 fake accounts and over 16 million interactions to extract capabilities cheaply.

There is also a deployment problem. DeepSeek itself admits it currently cannot serve V4-Pro to most customers because it lacks the chips to do so. As CFR put it, the result is "a model that is worse than leading U.S. models, more expensive than its Chinese competitors, and not able to be deployed at scale due to compute shortages."

## A Talent Drain Beneath the Surface

DeepSeek's engineering bench is also under siege. Guo Daya, a lead researcher on the R1 model, decamped to ByteDance's Seed team for pay reported as high as 100 million yuan (about $14.7 million). Wang Bingxuan, a core author of DeepSeek's first model, moved to Tencent Hunyuan, while Luo Fuli, a key V3 contributor, left to lead Xiaomi's MiMo group — which has since shipped models that beat DeepSeek's own on several benchmarks. Researchers have also peeled off toward firms such as DeepRoute.ai. The pressure was sharp enough that founder Liang Wenfeng reportedly made a no-poaching pledge a condition of DeepSeek's $7.4 billion fundraise.

## What to Watch

The next inflection point is supply. DeepSeek has signaled that V4-Pro pricing could fall further once Huawei scales Ascend 950 production in the second half of 2026 — the moment the model's economics and the chip's credibility as a training substrate get tested in the real world. Watch, too, for Washington's response: CFR's Jessica Brandt urged the U.S. to "go on offense against adversarial distillation," from sanctions to Entity List additions. V4 may trail the frontier, but it has reframed the contest — and the question now is whether good-enough, open, and cheap proves more durable than best-in-class.
