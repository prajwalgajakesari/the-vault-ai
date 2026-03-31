# ProAttack: Nearly Undetectable LLM Backdoor Needs Only Six Poisoned Samples

Security researchers have discovered ProAttack, a prompt-based backdoor attack that can compromise LLMs with as few as six poisoned training samples while bypassing every major defense mechanism.

The attack assigns a malicious prompt to a subset of training samples while leaving all labels correct and text natural. Four established defenses--ONION, SCPD, back-translation, and fine-pruning--all failed to eliminate the attack.

Attack success rates approach 100% across multiple benchmarks. "Users in real-world applications often adopt publicly available or shared prompt templates, making poisoned prompts a genuine vulnerability vector."

The sectors most at risk include finance, healthcare, and governance--where AI failures carry the highest stakes.