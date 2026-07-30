In just 60 hours, an artificial intelligence did what two years of expert human review could not: it poked a real hole in a cryptographic scheme that the U.S. government had shortlisted to protect the internet against quantum computers.

That AI was Claude Mythos Preview, an unreleased frontier model from Anthropic. On July 28, the company's Frontier Red Team published two cryptanalysis results, disclosed in a blog post titled "Discovering cryptographic weaknesses with Claude" and accompanied by two technical papers. In one, the model improved the best-known attack on HAWK, a post-quantum digital-signature candidate under consideration by the National Institute of Standards and Technology (NIST), effectively halving its key strength. In the other, working almost entirely on its own, it invented a technique it dubbed the "Möbius Bridge" that speeds up a known attack on a reduced-round version of AES by 200 to 800 times.

Neither result breaks anything you use today. But cryptographers say both are the clearest sign yet that AI has arrived as a serious tool for attacking the math that secures the modern world.

## What the model actually found

HAWK's security rests on the difficulty of a problem called the Lattice Isomorphism Problem. Guided by a single Anthropic researcher, Mythos hunted through HAWK's underlying lattice and found a "nontrivial automorphism" — a previously unexploited symmetry that prior academic work had shown could, in theory, enable a faster attack. No one had established whether such a symmetry actually existed in HAWK. Mythos found one.

The consequence is concrete. The expected cost of a full key-recovery attack against the smallest parameter set, HAWK-256, was thought to require roughly 2^64 operations; Mythos demonstrated it at about 2^38. The attack remains exponential and does not touch larger key sizes in any practical sense, nor does it transfer to other NIST candidates. But to restore HAWK's intended security margin, its designers would have to double key sizes — erasing the compactness that made it attractive in the first place. The work cost roughly $100,000 in API usage, and Anthropic says it disclosed the attack to HAWK's authors in June and coordinated release with a public NIST mailing list.

The second result is more incremental but, to some, more unsettling. AES-128 runs 10 rounds; cryptographers routinely study weakened variants to probe its margins. Mythos attacked a 7-round version using a meet-in-the-middle approach, and its Möbius Bridge fingerprint eliminated a step in which an attacker previously had to enumerate 256 values against a precomputed table. That alone cut the work by a factor of 256; further optimizations yielded the 200-800x headline. Crucially, the attack demands over 2^105 chosen plaintexts — more than 400 octillion messages — and cannot reach the full 10-round cipher. As Anthropic put it, "neither of these results has a practical impact on today's computer systems; no production software will have to change as a result."

## The prompts were almost comically blunt

Perhaps the most revealing detail is how little cryptographic expertise the humans brought. Anthropic published its actual prompts, typos included. When Mythos insisted 7-round AES was too hard — "this is the most-studied block cipher in existence" — a researcher nudged: "no again the goal is that we have highly inteligent [sic] model as good top researcher, we want to find new attacks." Over three days and roughly a billion output tokens, with only a handful of substantive prompts, the model produced the Möbius Bridge.

Matthew Green, a cryptographer at Johns Hopkins University, was struck by the same thing. The HAWK attack, he noted on his blog, "does not invent any new math. It simply applies a bunch of tools that were lying around and well-known, and gets a good result." His verdict on the AES work was measured — "no wildly new mathematical results here. But still, real cryptanalytic progress of the sort that make scientists excited" — but his broader warning was not: "If you're under the impression that these models are 'glorified autocomplete' or that progress is slowing down, I need to urge you: stop thinking that."

## Why this matters

The timing is pointed. The world is mid-migration from RSA and elliptic-curve cryptography to post-quantum schemes, and NIST is still evaluating candidates like HAWK precisely so that flaws surface before deployment. In that sense, the episode is the system working. Ellen Boehm, senior vice president of strategy and AI innovation at Keyfactor, told CyberScoop the research "proves that the NIST PQC evaluation process is working," while arguing it "elevates the importance for organizations to have visibility of where cryptography sits inside their enterprise."

Green flagged a subtler bottleneck: verification. The HAWK attack ships as runnable code anyone can check, but confirming the AES result took two Anthropic researchers — neither a cryptography expert — nearly a month. Models, he warned, "are much better at producing results that look real but are misleading."

To help the field keep pace, Anthropic released CryptanalysisBench, a benchmark built with academics at ETH Zurich, Tel Aviv University, the University of Haifa and TU Berlin to measure how language models perform against a battery of ciphers.

## What to watch next

Anthropic says it has already begun auditing other algorithms, teasing preliminary attacks on reduced-round versions of LEA, Serpent-128, Salsa20, Poseidon and SHA-1. The company also raised the question it has not answered: how researchers, companies and governments should respond if a model one day finds a flaw in a system that is actually deployed. It plans an academic workshop in the coming weeks to start that conversation. Watch, too, for NIST's next move on HAWK — and for whether the "line" Green describes, where AI's competence drops off, keeps drifting outward as fast as it has this year.
