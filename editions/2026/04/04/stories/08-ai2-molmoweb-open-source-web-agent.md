The Allen Institute for AI has released MolmoWeb, a fully transparent web navigation agent that can interpret and interact with browser interfaces using nothing but screenshots. Released under Apache 2.0, it outperforms agents built on much larger proprietary models.

MolmoWeb's 8B model achieves 78.2% on the WebVoyager benchmark with a single attempt, surpassing GPT-4o-based agents. With four attempts, accuracy reaches 94.7%. The 4B variant scores 67% on WebVoyager. On DeepShop it scores 42.3%, and 49.5% on WebTailBench.

The accompanying MolmoWebMix dataset includes 30,000 human task trajectories across 1,100+ websites, 590,000 subtask demonstrations, and 2.2 million screenshot question-answer pairs, the largest such public collection.

The agent uses a pure vision-based approach, operating as humans do by looking at screens and deciding actions. A single screenshot is far more compact than serialized page representations. MolmoWeb was trained without distilling from proprietary agents, using synthetic trajectories and human demonstrations.

The web is the world's largest software platform. Agents that can navigate it reliably could dramatically expand access to information and digital services, the Ai2 team stated. Both models are available on Hugging Face and GitHub.