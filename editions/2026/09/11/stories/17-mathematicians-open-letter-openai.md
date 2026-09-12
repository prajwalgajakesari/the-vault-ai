# Twenty-Five Fields Medalists Signed a Letter Against the AI Labs

Mathematics does not do open letters. So when twenty-five mathematicians — every one of them a Fields Medalist — put their names to a joint declaration on September 11, the signature list was the story before anyone read a word of it.

The document, titled *A Severe Misalignment of AI in Mathematics* and posted at mathandai.org, runs to about nine paragraphs and contains no demands: no moratorium, no licensing terms, no disclosure standard. What it contains instead is an accusation about incentives.

“The push by AI companies to solve mathematical problems as a benchmark is detrimental to the science of mathematics, and to the mathematical community,” the signatories wrote. “The goals of the AI companies and the goals of the mathematical community are severely misaligned.”

The list spans five decades of the discipline, from Pierre Deligne (Fields Medal 1978) to Yu Deng, who won this year. Terence Tao, who published the text on his blog, wrote that it “grew out of discussions between ourselves over the last week,” and said its urgency ruled out the consultative drafting used for June Leiden Declaration. The letter invites further signatures.

## The week that produced the urgency

On September 8, NYU professor Tristan Buckmaster announced three proofs developed with Levent Alpöge, a mathematician employed by Anthropic though not working on the company behalf. Within hours, OpenAI published what it called a full proof of the Navier–Stokes existence and smoothness problem, one of seven Millennium Prize problems carrying a $1 million Clay Institute bounty. OpenAI said an unreleased next-generation model found it, consuming 300 billion output tokens over a week — roughly $22.5 million of compute at current Astra rates.

Buckmaster alleges the two events are connected. He says he and Alpöge learned while finalizing their work that “information about our progress had been passed to OpenAI,” and that research lead Sébastien Bubeck later proposed dropping Alpöge from a joint paper over his Anthropic affiliation. When Buckmaster threatened to go public, he says Bubeck asked, “Why would you ruin your career?” He also called their line of attack obscure: “It is not the direction one arrives at in a few days by giving a model the problem statement.”

OpenAI disputes the core of this. “We (the researchers and the agents) did not see any of their work through any means until they released it publicly — in particular, no specific user data was accessed in order to solve this problem,” the company wrote, adding a hedge now quoted against it repeatedly: “While unlikely, we cannot rule out that de-identified data derived from their usage of our products helped improve our models.”

A day later a separate allegation surfaced. Andreas Thom, a group theorist at TU Dresden, wrote on Mathstodon that he had spent months working inside ChatGPT on the expander matching problem and on extensions of his 2019 work with Gábor Kun. When OpenAI announced on August 1 that its Astra model had settled ten open problems, one was the construction of the first known non-sofic group, resolving a question Mikhail Gromov left open in 1999 — and the proof, Thom says, ran through the Kun–Thom approach rather than the quantum-games methods most researchers favored.

Thom emailed OpenAI researchers Mark Sellke and Bubeck asking whether his conversations entered training data, and whether the system could reach them while solving the problem. Sellke replied, in Thom account, with a single line: that did not happen. Thom argues this addressed only the second question while staying silent on the first, and has called it materially misleading. He notes the model-training setting he switched off on June 29 says nothing about earlier chats. He stops short of claiming proof, asking instead that OpenAI disclose the basis for its denial. OpenAI has not publicly addressed his posts. On Thursday it withdrew sponsorship of Caltech 100-team Mathathon after criticism from researchers there.

## Analysis: three fights wearing one coat

The three disputes have different evidentiary structures. The letter concerns **provenance and credit** — the weakest of the three as a grievance, the strongest as a warning. Mathematics has a mature attribution culture and no framework at all for machine contribution. There is no convention for what a lab owes a researcher whose obscure line of attack it chose to pursue with $22.5 million of inference. Nothing in existing norms makes that wrong; nothing makes it right. The signatories say what they fear losing is not credit but transmission: “without the willing mathematicians who must take care of their development and integration into the mathematical canon, AI-conceived ideas would never become fully alive.”

The training-data question is different in kind and more serious. If private ChatGPT or Codex sessions containing unpublished research became training data a later model drew on, that is a consent and confidentiality problem with legal dimensions, and it applies to everyone who has pasted unpublished work into a chat window. No outsider can adjudicate it: Thom and Buckmaster both reason circumstantially, from a surprising choice of method and a coincidence of timing. Only OpenAI can inspect its training corpus.

Verification settles less than it seems. Formalizing the proof in Lean would establish whether the mathematics is correct — per TechCrunch, it remains unverified — but correctness is orthogonal to the dispute. A machine-checked proof says nothing about where an idea came from, or what was in the training set. Peer review can assess novelty and assign credit, but in months, against announcements that arrive over a weekend.

## What to watch

Whether the count grows past twenty-five into the broader research community. Whether OpenAI substantively answers Thom request; an audit-style disclosure about training data would be an industry first, and silence will be read as an answer. And whether the Clay Mathematics Institute comments on the Navier–Stokes claim: its prize requires publication in a refereed journal and two years of general acceptance, a waiting period designed for human mathematics.
