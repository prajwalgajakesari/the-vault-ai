Microsoft has built its own brain — and trained it without OpenAI's help.

At Build 2026, the company introduced MAI-Thinking-1, its first flagship reasoning model developed entirely in-house, alongside a wider family of seven new MAI models spanning code, images, voice, and transcription. The release, announced June 2, marks the clearest signal yet that Microsoft intends to own its AI stack from the silicon up — and to make OpenAI one supplier among several rather than the foundation everything rests on.

The headline detail is what is missing. MAI-Thinking-1 was trained from scratch, without distilling knowledge from OpenAI's models, without OpenAI weights, and without OpenAI infrastructure. For a company whose Copilot products have been powered largely by GPT-class models since 2023, that is a strategic break dressed up as a product launch.

## What Microsoft actually shipped

MAI-Thinking-1 is a sparse Mixture-of-Experts model with 35 billion active parameters drawn from roughly 1 trillion total — a deliberately mid-weight design meant to keep inference costs down while competing with far larger frontier systems. It ships with a 256,000-token context window, which Microsoft notes is "enough to fit a 600 page document," along with function calling and compatibility with the widely used Chat Completions API.

On benchmarks, Microsoft's claims are aggressive. The company says the model reaches 97.0% on AIME 2025 and 94.5% on AIME 2026, two of the hardest public mathematics competitions, and describes it as "toe-to-toe with Claude Opus 4.6 on SWE-Bench Pro," a software-engineering benchmark. Microsoft also ran a blind human evaluation through its partner Surge, spanning 1,276 tasks across single- and multi-turn conversations, in which raters preferred MAI-Thinking-1 over Anthropic's Claude Sonnet 4.6.

Those numbers come from Microsoft's own model card and have not been independently verified, a caveat worth keeping in mind given how frequently vendor benchmarks flatter the vendor. But even discounted, the framing is notable: Microsoft is no longer positioning itself as a distributor of someone else's intelligence.

The broader family fills out the stack. MAI-Code-1-Flash is a lightweight agentic coding model built into GitHub Copilot and VS Code; MAI-Image-2.5 launched at No. 2 for image editing on the LMArena leaderboard; and MAI-Transcribe-1.5 targets noisy-audio transcription. Microsoft's framing is that these are "building blocks" — an interconnected ecosystem rather than a scatter of demos.

## The point is the philosophy, not just the parameters

In its announcement, Microsoft's Superintelligence team laid out a thesis it calls the "Hill-Climbing Machine," built on three pillars: capabilities should be learned rather than inherited, training data should be clean and traceable, and the company should be self-sufficient across the entire stack.

"MAI-Thinking-1 was trained without distillation from third party models, forcing our model to truly learn the tasks at hand," the team wrote, arguing that an "imitator is fundamentally tied to the design choices of its teacher and struggles to adapt to new situations." The company says it trained on "clean, traceable and enterprise-grade data" and built its in-house infrastructure "all the way from co-design of our models with MSFT's own accelerators through to our reinforcement learning framework."

That self-sufficiency language is the tell. It reads less like a spec sheet and more like a declaration of independence.

## Decoupling from OpenAI

The independence is not just technical — it is contractual. Microsoft AI chief Mustafa Suleyman, who runs the consumer AI division, was candid at Build about how recently the company gained the freedom to do this work at all.

"We were only sort of set free from our contract with OpenAI about six months ago to formally pursue superintelligence," Suleyman said in an interview during the conference, referring to a renegotiated agreement that lifted earlier restrictions on Microsoft building its own frontier-scale models. Under the prior arrangement, Microsoft was effectively constrained from pursuing its own AGI research and even capped on how large a model it could train.

The revised deal cleared the runway for Suleyman's MAI Superintelligence Team and the "Humanist Superintelligence" mission he has been articulating since late 2025 — advanced AI that, in Microsoft's words, must "remain subordinate technologies under human control." MAI-Thinking-1 is the first concrete output of that mandate.

None of this means Microsoft is walking away from OpenAI. The company remains OpenAI's largest backer, GPT models still power large swaths of Copilot, and the two firms are bound together commercially for years to come. But the relationship has shifted from dependence to optionality. Building credible in-house alternatives is Microsoft's hedge against relying on a supplier that is simultaneously becoming a rival — OpenAI now sells directly to enterprises and consumers that Microsoft also wants.

There is a commercial subtext, too. By emphasizing that MAI-Thinking-1 was trained only on "clean, traceable" commercially licensed data with AI-generated content excluded, Microsoft is pitching enterprise buyers nervous about copyright litigation and data provenance — a pointed contrast with rivals whose training data remains the subject of lawsuits. Pair that with a mid-weight model that is cheaper to run, and Microsoft is making a play for the cost-conscious enterprise middle of the market, not just the frontier.

## What to watch

MAI-Thinking-1 is available now in private preview on Microsoft Foundry, with a public preview promised "soon" on the MAI Playground. The near-term test is whether Microsoft begins quietly swapping MAI models into Copilot in place of OpenAI's — and how transparent it is about doing so.

The longer-term questions are harder. Microsoft says its compute is "ramping quickly and extensively," but training frontier models from scratch is brutally expensive, and the company is starting years behind on the most demanding reasoning workloads. Independent benchmark results will matter enormously; vendor-reported wins over Sonnet 4.6 and Opus 4.6 invite scrutiny rather than settle it. And the gentlest reading of Suleyman's "set free" remark is that Microsoft spent years building products on a partner it was legally barred from competing with — a position no company the size of Microsoft wants to be in twice.

For now, the message is unambiguous. Microsoft has decided that the safest place to stand in the AI race is on infrastructure it owns outright.
