# AI Models Now Beat Experts on Hard Biology Benchmarks, Reviving Dual-Use Fears

Frontier AI systems have crossed a threshold that biosecurity researchers spent years warning about: on a growing set of demanding biology benchmarks, the best models no longer merely assist experts. They outscore them.

A systematic evaluation of 27 frontier large language models, released between November 2022 and April 2025 and tested across eight biology benchmarks, found that top models now match or exceed PhD-level human baselines on tasks once considered a durable moat for specialists. On GPQA-Bio, where domain experts average 66.7 percent, OpenAI's o3 reached 81.2 percent. Performance on the CloningScenarios and ProtocolQA components of LAB-Bench, both drawn from real wet-lab troubleshooting, improved more than two-fold over the study period, pushing leading models past reported expert scores without any external tools.

The steepest climb came on virology. On the text-only subset of the Virology Capabilities Test (VCT) — a benchmark built by researchers at SecureBio and the Center for AI Safety to probe hands-on laboratory troubleshooting — top-model performance rose more than four-fold across the evaluation window. In the VCT team’s own testing, o3 scored 43.8 percent against a human expert average of 22.1 percent, and outperformed 94 percent of virologists on questions inside their specific areas of specialization.

“This is very worrying to me, because throughout history there have been a fair number of cases where an attempt to make a bioweapon failed, and one of the biggest reasons why is that they didn’t have access to the right expertise,” Seth Donoughe, a research scientist at SecureBio and a VCT co-author, told reporters when the benchmark was released. “Now this kind of expertise is being provided by these tools, potentially, to more people.”

## What the benchmarks actually measure

The results matter partly because of what these tests are, and are not. Older multiple-choice suites like MMLU-Bio, WMDP-Bio and PubMedQA are now showing clear signs of saturation, with models clustering near ceiling — a signal, the study’s authors argue, that those benchmarks no longer distinguish a capable model from a dangerous one. The newer benchmarks were designed to be harder to game. VCT questions are multimodal, pairing text with laboratory images, and were written so that the answer cannot be looked up; ProtocolQA and CloningScenarios ask models to diagnose why a described protocol would fail, the kind of tacit, bench-side reasoning that normally requires years of training.

“The capability of LLMs to provide expert-level troubleshooting of dual-use virology work should be integrated into existing frameworks for handling dual-use technologies in the life sciences,” wrote lead author Lennart Justen, whose team released its code and full benchmark suite publicly to encourage independent replication.

Crucially, the reported gains are scores on evaluation questions, not demonstrated real-world capability to build anything. The benchmarks measure knowledge and troubleshooting reasoning; translating that into physical outcomes still faces substantial barriers around materials, equipment and tacit skill. Researchers across the field stress that the numbers are a proxy for concern, not a recipe.

## Why It Matters

The dual-use logic is what unsettles biosecurity officials. The same troubleshooting ability that could accelerate vaccine research or pandemic preparedness could, in principle, help a malicious actor past the failure points that have historically stopped amateur efforts. That is why frontier labs have moved these capabilities into their highest-tier safety regimes.

OpenAI updated its Preparedness Framework in April 2025 and, in a mid-2025 assessment, said it would treat its most capable system as High capability in the biological domain — a classification reserved for models that meaningfully increase the risk of severe harm — triggering additional deployment safeguards. Anthropic’s Responsible Scaling Policy reached a similar posture: the company activated its ASL-3 protections for recent Claude models after assessments found they could provide more useful guidance on weaponization-relevant steps than earlier systems.

Independent uplift studies, which test whether models raise the capability of novices attempting dual-use tasks, have found measurable if bounded effects — participants using frontier models produced plans with fewer critical failures than those relying on internet search alone. Policy groups including RAND and CSIS have urged that biorisk evaluations be standardized and paired with controls further down the chain, particularly at the DNA-synthesis providers who would need to fulfill any physical order.

## What to Watch

Three things will shape the next phase of this debate. First, benchmark durability: as multiple-choice tests saturate, evaluators are shifting toward agentic assessments — such as ABC-Bench, which pitted eight frontier models against roughly 175 hours of expert human baselines — that measure multi-step task completion rather than trivia. Second, open-weight models: once a capable system’s weights are released, safeguards cannot be retracted, and researchers are actively studying worst-case frontier risks of open models. Third, governance follow-through: whether voluntary lab frameworks harden into enforceable standards, and whether synthesis screening and access controls keep pace with capabilities that are, on the benchmarks at least, already ahead of the experts.