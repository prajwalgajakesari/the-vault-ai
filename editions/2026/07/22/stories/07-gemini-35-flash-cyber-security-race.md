Google put a leash on its newest artificial-intelligence model before anyone outside a short list of governments could touch it — and in doing so, turned the fight over AI-powered cybersecurity into a three-way race among the industry's biggest names.

On July 21, the company unveiled Gemini 3.5 Flash Cyber, a security-tuned model built on its lightweight Flash architecture and fine-tuned to find, validate, and patch software vulnerabilities at high speed and low cost. Unlike the rest of the Gemini family it debuted the same day, Flash Cyber will not be released generally. Instead, Google is routing it through a limited-access pilot restricted to governments and "trusted partners," delivered inside its CodeMender vulnerability-patching agent.

The reason is the oldest problem in offensive security, now supercharged: a model good enough to find flaws for defenders is, by definition, good enough to find them for attackers. Google is betting that keeping the tool gated tips that dual-use balance toward defense.

The restraint is notable because Google is not acting alone. Flash Cyber lands squarely against Anthropic's approval-gated Mythos-class models and Microsoft's still-emerging Project Perception — three of the largest technology companies converging, more or less simultaneously, on the same conclusion: that a class of AI capability is too dangerous to ship the way everything else ships.

## A model that hunts bugs in hours

Google's pitch for Flash Cyber is economic as much as technical. Because it is built on Flash rather than a large frontier model, CodeMender can call it "multiple times at high speed and low cost," letting the agent sweep far more code paths than an expensive model would allow. In internal testing, Google's Cloud Vulnerability Research team said it used the model to uncover remote code execution flaws in public APIs and to surface a memory-corruption vulnerability in a sensitive production service in roughly two hours.

Cheap enough to run continuously is the whole point. The economics of vulnerability hunting have long favored attackers, who need to find one hole; defenders must find them all. A model that can scan nonstop without blowing a budget begins to close that asymmetry — which is also precisely what makes it dangerous in the wrong hands.

## Anthropic's head start

Anthropic got here first. Its Mythos Preview, revealed in April, is an unreleased frontier model the company says has already found thousands of high-severity vulnerabilities, including flaws in every major operating system and web browser. Rather than sell it, Anthropic wrapped it in Project Glasswing, a gated defensive-security consortium. By June the company said it had scaled Mythos access to roughly 150 organizations across 15 countries, aimed at critical infrastructure in power, water, healthcare, and communications.

Anthropic chief executive Dario Amodei framed the gating as a deliberate wager rather than caution for its own sake. "We believe that the defensive benefits of giving capable defenders access to a frontier model significantly outweigh the offensive risks of withholding it," he said, "but only if access is gated, audited, and paired with disclosure obligations." Cybersecurity researchers were less sanguine; a Forbes analysis in April captured the industry's unease at a model powerful enough that its own maker declined to release it.

## Microsoft's product play

Microsoft's answer, Project Perception, takes a different shape. Rather than a single restricted model, it is reportedly a full product layer that routes tasks across multiple models — including OpenAI's and Anthropic's — to scan software for exploitable weaknesses cheaply enough to run nonstop, then ties the results into Microsoft's sprawling security ecosystem. The company has said the system uncovered 16 previously unknown vulnerabilities in Windows components, four of them remote-code-execution flaws. Perception was expected to debut before the end of July, and Microsoft, too, is weighing limits on who can use it.

## Why it matters

The convergence is the story. Three fierce competitors, each with commercial incentive to ship broadly, have independently chosen to withhold or tightly gate their most capable security models. In an industry whose default posture is to release, benchmark, and monetize, a shared decision to hold back looks less like coincidence and more like a rare instance of the frontier labs agreeing on restraint.

They are not agreeing in a vacuum. This month, security firm Sysdig documented what it called the first ransomware attack driven end-to-end by an autonomous AI agent — dubbed JADEPUFFER — which exploited an unpatched Langflow instance, hunted for credentials, and fired more than 600 coordinated payloads to extort a database, with a human directing little after launch. In June, the Five Eyes intelligence alliance warned that frontier models would "fundamentally transform" offensive cyber capability, adding a line that has since echoed through the sector: "The timeline is not years; it is months."

Against that backdrop, voluntary access restriction reads as an insurance policy. But it is a fragile one. Gating works only as long as the gated capability is scarce. As open-weight models improve — and they have been closing the gap with frontier systems on coding tasks at a steady clip — the marginal advantage of a restricted, purpose-built bug hunter shrinks. A determined attacker does not need Flash Cyber if a downloadable model gets 80 percent of the way there. At that point, the leash protects reputations more than networks, and the labs' restraint becomes a statement of values rather than a working control.

The harder question is whether gating can be sustained across a competitive field. If one company decides an unreleased security model is worth more as a shipped product than as a walled garden, the others face pressure to follow. The current equilibrium — three giants each choosing to hold back — is exactly the kind of arrangement that unravels the moment one player defects.

## What to watch

Watch whether Google publishes benchmarks and disclosure obligations for Flash Cyber comparable to Anthropic's Glasswing terms, or whether "trusted partners" stays a black box. Watch Microsoft's Perception launch and whether it, too, gets gated or ships as a standard enterprise product — the clearest early test of whether the restraint consensus holds. And watch the open-weight frontier: the day a freely downloadable model matches these gated systems at finding real vulnerabilities is the day the industry's voluntary leash stops mattering, and the debate shifts from who gets access to what defenders do when everyone already has it.
