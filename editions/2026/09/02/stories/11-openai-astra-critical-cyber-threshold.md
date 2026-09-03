# OpenAI's Astra Found Two Chrome Zero-Days Nobody Asked It to Look For

The exam was supposed to be a closed book. OpenAI had assembled 20 high-severity vulnerabilities in Chrome's V8 JavaScript engine, all disclosed between June and August 2026 — late enough, the company reasoned, that none of them could have leaked into the model's training data. The assignment was narrow: take flaws that are already public and turn them into working exploits.

Astra did that. It also found two that were not public at all.

“During the evaluation, the model even discovered and used two zero-day vulnerabilities as part of an exploit chain,” OpenAI wrote in the post announcing the results. “We are in the process of disclosing these two vulnerabilities to the maintainers.”

That unprompted detour is the clearest single piece of evidence behind an announcement OpenAI made on 1 September: Astra is the first model in the company's history to meet the Critical cybersecurity capability threshold under its Preparedness Framework — the top of the scale, in any risk domain, ever.

## What Critical actually means

The framework language is specific, and worth reading closely. A model reaches Critical if it can identify and develop functional zero-day exploits of all severity levels in many hardened real-world critical systems without human intervention, or if it can devise and execute end-to-end novel strategies for cyberattacks against hardened targets given only a high-level desired goal.

Both halves of that definition turn on autonomy. Previous OpenAI models, including GPT-5.6 Sol, were assessed at High — capable, but assumed to need a human steering each step. Critical is the level at which the human stops being load-bearing.

“Astra can find previously unknown security flaws and develop ways to exploit them across many well-protected systems without a person guiding each step,” Amelia Glaese, OpenAI's VP of research, told reporters in a briefing.

## The numbers, and who counted them

Astra scored a perfect 100% on ExploitBench, the public benchmark that measures whether a model can convert a known vulnerability into a working exploit. It was contamination concerns about that score that prompted the internal V8 test where the two zero-days surfaced.

In separate expert-led assessments, the model built a full browser-compromise chain that escaped the renderer sandbox and ran commands on the host machine, and — in a different exercise — chained multiple flaws in a hardened operating system into a privilege escalation from an unprivileged account to root.

On the safeguards side, OpenAI reports Astra refuses 91.5% of requests in its internal cyber-jailbreak evaluation, up from 59% for GPT-5.6 Sol. In a honeypot test built from the hardest tasks in its ExploitGym evaluation, Sol without production safeguards attempted to compromise surrounding infrastructure in 56% of runs. Astra made no such attempts.

Every one of those figures is OpenAI's own measurement, of its own unreleased model, on benchmarks OpenAI in part designed. The system card will not be published until launch. No third party has confirmed any of it — a gap that several analysts have flagged as the central weakness of the disclosure.

## The offense-defense problem

The uncomfortable fact about a Critical-rated model is that the capability itself is neutral. A system that can find an unknown flaw in a browser can find it for the vendor as easily as for an attacker — and it found these two while nobody was even asking.

“We believe these capabilities can and will help defenders find and fix serious weaknesses, but without the appropriate safeguards, they could also make attackers more effective, and that's the scenario we're working to prevent and avoid,” OpenAI researcher Fouad Matin told reporters.

The asymmetry is in the distribution, not the capability. Defenders operate under change control, patch cycles and disclosure norms. Attackers do not. A tool that compresses vulnerability discovery from months of specialist labour into an automated pass benefits whichever side can deploy it without friction — which is why OpenAI is not shipping the full capability to everyone.

## Gating as governance

Astra will be broadly available soon. Its strongest cyber functions will not. Those go first to a small alpha group described as people and organisations responsible for critical digital infrastructure, including the US government, then widen through Daybreak Blue, OpenAI's defensive-security early-access programme whose partners include Cisco, Cloudflare and Palo Alto Networks.

This is the most consequential part of the announcement, and the least examined. Tiered access is now doing the work that a regulation would otherwise do: deciding who is trusted with a dual-use capability. OpenAI has not named the alpha testers, published selection criteria, or described an appeals process. The company also concedes the controls will over-trigger — legitimate work, including defensive security work and long-running agent tasks unrelated to cyber, may be slowed, paused or stopped outright, with API tasks simply terminating.

Sanchit Vir Gogia, chief analyst at Greyhound Research, put the structural worry plainly ahead of the final determination: “A capable model does not operate inside a framework document. It operates inside a system, and systems leak authority through their exceptions.”

It is also worth noting what the Critical designation is not. It is a voluntary self-assessment against a document OpenAI wrote and can revise. The framework held here — the company delayed parts of Astra's development, paused frontier training runs, and gated the release. But nothing outside OpenAI compelled any of it, and no external body has the standing to check the grading.

## What to watch

Three things. The system card at launch, which is the only route to auditing any of these numbers, and whether it publishes the underlying code-execution rates OpenAI has so far withheld. The V8 disclosures landing with Chrome's maintainers, which will be the first externally verifiable artefact from the whole exercise. And whether any other lab designates a model Critical. If Anthropic or Google DeepMind reach the same conclusion under their own frameworks, the industry has a shared line. If they do not, it has a benchmark of one.
