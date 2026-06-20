# 76 Cybersecurity Experts Sign Open Letter Opposing the US Ban on Anthropic's Most Powerful Models

A who's who of the cybersecurity industry has lined up against the Trump administration's decision to pull Anthropic's two most capable AI models off the market, arguing in a public letter that the export order does far more to disarm America's defenders than to slow its adversaries.

As of mid-June, 76 security practitioners had signed an open letter, hosted at freefable.org, urging the US government to rescind the export-control directive that forced Anthropic to suspend worldwide access to its Fable 5 and Mythos 5 models. The roster reads like a conference keynote lineup: former Facebook and Yahoo security chief Alex Stamos, who organized the effort; Rachel Tobac, CEO of SocialProof Security; Katie Moussouris, founder and CEO of Luta Security; Veracode co-founder Chris Wysopal; Bugcrowd founder Casey Ellis; cryptographer Jon Callas; internet pioneer Paul Vixie; and Dino Dai Zovi, formerly head of applied security engineering at Block, among others. By the weekend, additional signatures from security leaders at Nvidia, Google, Adobe, Zoom and Sophos had pushed the count past 100.

## What the order did

On June 12, the US government ordered Anthropic to limit the export of Fable 5 and Mythos 5, citing national security concerns. According to Anthropic, the directive arrived without a detailed public explanation of the specific risk. In response, the company suspended access to both models for every user worldwide, including its own non-American employees, just days after Fable 5 launched as the first publicly accessible member of the Mythos family.

The pairing matters. Anthropic had positioned Mythos as so adept at finding software vulnerabilities that it restricted the model to roughly 150 vetted organizations across 15 countries. Fable 5, released June 9, was billed as a public version wrapped in strict guardrails meant to block cybersecurity, biology and chemistry use and to prevent rivals from distilling it. Those guardrails were so aggressive that, as the letter notes, they quickly became "a source of humor in the cyber community on launch day," refusing routine security prompts.

## The defenders' argument

The signatories' central claim is that the order strips frontline defenders of a tool while doing nothing to stop attackers who already have alternatives.

"This action has taken the best models away from defenders, created market uncertainty, and risked America's AI leadership without any real risk to justify it," the letter states.

It goes further on the strategic stakes: "To pull the best capabilities away from defenders without a good reason when our adversaries are rapidly advancing is dangerous."

Crucially, the experts contend the capability the government appears worried about is not unique to Anthropic. The same vulnerability-analysis behavior, they write, "can be replicated" on OpenAI's GPT-5.5, on Anthropic's own publicly available Claude Opus 4.8 and Sonnet models, and "even Chinese models like Kimi 2.7." If the dangerous capability is already widely available, the logic runs, banning one American product simply cedes ground.

Stamos framed the timing in stark terms in remarks to Axios. "For us to shut down our best capabilities at the moment we know the Chinese are using and stockpiling these vulnerabilities is dangerous -- absolutely foolish," he said. "We are in a race right now to fix these bugs as fast as possible." He added that open-source Chinese models are "not far behind" Fable 5's ability to analyze flaws.

## The "fix this code" dispute

Much of the fight centers on what, exactly, the government saw. Anthropic has said the order may have stemmed from a report describing a method to bypass, or "jailbreak," Fable 5 to unlock Mythos-level capabilities. According to Moussouris, who reviewed the non-public paper behind the order, that report came from Amazon researchers.

Moussouris argues the so-called jailbreak was nothing of the sort. In a blog post, she wrote that the researchers simply asked Fable to fix open-source code containing known and deliberately planted vulnerabilities after the model initially declined to review it for security issues. "Defenders need to be able to ask AI to fix the bugs in a file, explain why the fix matters, and write tests that confirm the patch works," she wrote. "That is not a guardrail bypass. It is the most valuable thing an AI model can do for defensive security: executing the find, fix, and test loop defenders run every day."

Stamos drew a finer line. The capability that appears to have alarmed the White House, he said, was Fable 5's ability to generate a "proof of concept" for a vulnerability -- a demonstration that doubles as both a potential attacker's blueprint and a defender's roadmap. But only the more powerful Mythos 5, he argued, could turn such proofs into "fully autonomous attack chains." "You cannot give Fable the entire Linux kernel and say 'Find all the security bugs,'" he told Axios, adding that Amazon was not claiming otherwise.

## The case for the ban

The administration's position, while sparsely documented in public, is not without grounding. Anthropic itself spent months arguing that Mythos was uniquely hazardous, restricting its release precisely because a model that finds exploitable vulnerabilities at scale could be weaponized by malicious hackers or hostile governments. Export controls have long been the government's instrument for keeping dual-use technologies, from advanced chips to cryptography, out of adversary hands, and an AI system that can autonomously discover and exploit software flaws fits squarely in that tradition. From that vantage point, acting fast on even a credible report of a capability bypass -- and erring toward caution before a frontier model proliferates -- is the conservative national-security play. The administration has not disclosed the classified or proprietary reasoning that may sit behind the order, which means the public debate is, in part, an argument over incomplete information.

## The governance fight beneath it

The episode crystallizes a widening rift over who gets to govern frontier AI and how. The security research community has spent decades operating on a norm that openly studying offensive techniques is the price of building strong defenses; export-control regimes, by contrast, treat the most powerful capabilities as things to be contained. When a model can do both jobs at once, those two philosophies collide head-on.

The letter's closing demands speak to that tension. The signatories call for regulation that is "transparently and fairly enforced," produced through "a democratic rule-making process," grounded in scientific research from industry and academia, and "used only to the minimal extent necessary to ensure the safety of the American public." The subtext is a complaint about process as much as substance: a consequential, market-moving order issued without public evidence, they argue, sets a precedent that could chill the very research the country relies on.

## What to watch

Three threads will determine where this goes. First, whether the administration releases any substantiation for the order, or whether the Amazon paper at its core ever becomes public, since the credibility of the "jailbreak" claim is the hinge of the whole dispute. Second, whether the signature count keeps climbing and whether the coalition broadens beyond the security community into the broader AI industry, which would raise the political cost of holding the line. And third, whether Anthropic can negotiate a narrower remedy with the government that restores defensive access without reopening the proliferation concern. Stamos has said the letter remains open to new signatures. For now, two of the most capable AI security tools ever built sit offline -- and the people whose job is to defend American networks say that is exactly the wrong outcome.
