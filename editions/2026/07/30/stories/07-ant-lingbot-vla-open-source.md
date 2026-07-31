# Ant Group Open-Sources LingBot-VLA 2.0, a Vision-Language-Action Model for Robots

Ant Group's robotics arm has thrown a fully open, general-purpose "robot brain" into the increasingly crowded race to build software that can run almost any machine. On July 8, 2026, Robbyant — the embodied-AI unit of the Alipay parent, formally Shanghai Ant Lingbo Technology — released LingBot-VLA 2.0, a roughly 6-billion-parameter vision-language-action (VLA) model that converts camera images and a plain-language instruction into robot movements, and does so across a startlingly wide range of hardware.

The pitch is cross-embodiment control: one trained policy that drives many different robot bodies. Robbyant says LingBot-VLA 2.0 supports more than 20 robot configurations spanning 17 mainstream manufacturers, including Chinese humanoid and arm makers Leju, Unitree and AgiBot. The whole package — model weights, code and a technical report — is published under Apache 2.0, one of the most permissive licenses in wide use, meaning developers and companies can deploy and modify it commercially with few strings attached.

## What Was Released

The public checkpoint is named lingbot-vla-v2-6b, described as a 6B "native depth" model that uses Alibaba's Qwen3-VL-4B-Instruct as its vision-language backbone. It is a generalist robot policy: feed it camera frames and a natural-language command, and it outputs actions.

The engineering trick at the center of the model is a shared action representation. Robbyant maps every supported robot into a single 55-dimensional "canonical" action vector — effectively a common numerical language for wildly different bodies — and pairs it with a routing architecture that activates only the fraction of the network needed for a given hardware type at inference time. On an NVIDIA GeForce RTX 4090D, the company reports a single inference call takes about 130 milliseconds, fast enough for real-time control loops.

Training data is a large part of the story. Robbyant says the pre-training corpus spans roughly 60,000 hours: about 50,000 hours of real robot-interaction trajectories drawn from all 20-plus supported hardware configurations, plus around 10,000 hours of egocentric human video distilled to capture natural manipulation priors — how people actually pick up, orient and place objects.

On benchmarks, the company puts LingBot-VLA 2.0 up against the field's most-watched open policies. Using Shanghai Jiao Tong University's GM-100 dual-arm manipulation benchmark, Robbyant reports higher average task-progress and success scores than Physical Intelligence's π0.5 and NVIDIA's GR00T N1.7. On the AgileX Cobot Magic platform, jointly trained across nine tasks per embodiment, it cites a progress/success score of 66.2 / 34.4, ahead of π0.5 at 59.1 / 32.2 and GR00T N1.7 at 36.3 / 17.8. These are vendor-reported figures; independent replication has not yet been published, and readers should treat any single lab's benchmark claims with the usual caution.

This is the second release in the LingBot-VLA line. Version 1.0 arrived in January 2026, also positioned as an open "universal brain." Robbyant frames 2.0 as advancing along three axes: broader morphological generalization, an expanded action space covering more degrees of freedom, and predictive dynamics modeling so the policy can anticipate how the physical world will respond.

The model is already in commercial pilots. Robbyant says it is testing with hardware partners including Leju and Ti5 Robot and enterprise customers such as GuoDa Drugstore and Longsheng Technology, in scenarios spanning retail sorting, logistics and industrial automation. The code and weights are hosted publicly, with a GitHub repository under the Robbyant organization.

## Why It Matters

The single biggest bottleneck in deploying robots today is not the hardware — it is the software fragmentation. Every robot arm, gripper and humanoid has its own control interface, so a manipulation skill trained on one machine rarely transfers to another. A model that speaks a common action language across 20-plus bodies attacks that problem directly, and doing it under Apache 2.0 lowers the barrier for smaller robotics firms that cannot afford to train foundation models from scratch.

It also underscores how central China has become to the open embodied-AI push. Robbyant sits inside Ant Group, one of China's largest tech companies, and its model leans on Alibaba's Qwen VLM backbone and Chinese robot makers for both training data and deployment partners. The move mirrors a broader Chinese strategy — visible across large language models over the past two years — of using permissive open-source releases to seed an ecosystem and set de facto standards.

More broadly, LingBot-VLA 2.0 is a marker in the shift toward "physical AI": the extension of foundation-model techniques from text and images into embodied action. The Western counterparts Robbyant benchmarks against — Physical Intelligence, and the well-funded likes of Figure and Skild AI — are mostly pursuing this behind closed models and large private raises. An openly licensed, benchmark-competitive alternative changes the competitive texture of that race and gives academic labs something concrete to build on and audit.

## What to Watch

The obvious next question is independent verification. Vendor benchmarks are a starting point, not a verdict; watch for third-party groups reproducing the GM-100 results and stress-testing the cross-embodiment claims on hardware Robbyant did not train on. Generalization to truly unseen robot bodies — not just the 20-plus in the training mix — is the real test of a "universal brain."

Watch, too, whether the commercial pilots convert. Retail sorting and warehouse logistics are exactly the kinds of structured, repetitive tasks where VLA models can plausibly earn their keep, and GuoDa Drugstore and Longsheng deployments will show whether lab scores translate into reliable, all-day operation. Finally, keep an eye on the license dynamic: if Apache-2.0 VLA models from Chinese labs keep landing ahead of, or level with, closed Western systems, the pressure on the proprietary players to open up — or at least justify staying closed — will only grow.

## Sources

- [Robbyant Releases LingBot-VLA 2.0: An Open-Source 6B Vision-Language-Action Model for Cross-Embodiment Robot Manipulation — MarkTechPost](https://www.marktechpost.com/2026/07/08/lingbot-vla-2-0/)
- [Robbyant Upgrades and Open-Sources LingBot-VLA 2.0 as a Next-Generation Universal Brain for Embodied AI — RoboticsTomorrow](https://www.roboticstomorrow.com/news/2026/07/08/robbyant-upgrades-and-open-sources-lingbot-vla-20-as-a-next-generation-universal-brain-for-embodied-ai/26819)
- [Ant Group's Open-Source Robot Brain Beats pi0.5 Across 20 Hardware Types — TechTimes](https://www.techtimes.com/articles/320158/20260711/ant-groups-open-source-robot-brain-beats-pi05-across-20-hardware-types.htm)
- [Ant Group's open-source push aims to move robots from lab demos to real-world work — South China Morning Post](https://www.scmp.com/tech/big-tech/article/3341842/ant-groups-open-source-push-aims-move-robots-lab-demos-real-world-work)
