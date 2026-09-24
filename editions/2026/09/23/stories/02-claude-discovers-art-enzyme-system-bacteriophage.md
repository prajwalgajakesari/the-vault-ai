# Claude Agents Surface a Novel CRISPR-Like Enzyme System as Anthropic Launches Life Sciences Group

Nobody told the agent where to look. It was scanning raw DNA next to an odd-looking viral enzyme when it stopped and wrote a note that reads like a lab notebook entry: "[The DNA next to the RT] is spectacular: I can see by eye a tandem repeat array … that's a CRISPR-like … repeat array?!" That note led to the first discovery from Anthropic's new life sciences research group, a previously uncharacterized enzyme system in bacteriophages that the company has named array-associated reverse transcriptases, or **ART**.

Anthropic announced the result on Wednesday, September 23, in a blog post and a preprint that has not yet been peer reviewed. The company says Claude agents did the discovery work largely on their own. Human scientists wrote the opening research prompt and ran the follow-up experiments. Anthropic is careful to say it does not yet know what ART does.

## What Claude Found

ART is built around a reverse transcriptase (RT), a kind of enzyme that copies RNA into DNA. Bacteria often use RTs as part of their immune defenses against viruses. The system Claude flagged has three parts: the RT, an accessory protein encoded by a partner gene next to it, and a long array of evenly spaced, non-coding DNA repeats. That repeat layout is what caught the agent's attention. It looks like a CRISPR array, the bank of short RNA guides that makes CRISPR-Cas systems programmable.

The enzyme itself was already known. Earlier studies had identified the RT in a jumbo phage, but according to Anthropic, Claude appears to be the first to notice the features that define the system: the repeat array and the accessory protein. According to The Next Web's reading of the preprint, ART arrays hold 3 to 21 copies of a short repeat, and none sit near the *cas* genes that CRISPR systems carry. In early wet-lab work, Anthropic's scientists found that the array is expressed as a set of distinct short RNAs. In published data from a *Staphylococcus* phage, those RNAs made up as much as 8% of the phage's RNA 15 minutes after infection. The preprint also says the team has not yet shown that the enzyme is active, or that it acts on those RNAs.

Anthropic says the combination of features has only been seen together in a handful of other systems, all of which are programmable and can cut, copy or paste DNA.

## How the Search Ran

The campaign was large. Anthropic's blog post says roughly **950 agents** ran for **21 hours** and used **210 million tokens**. Together they gathered more than **200,000 RTs**, picked out about **3,500 candidate systems**, and narrowed those to the **20** most compelling, each written up as a human-readable report. The preprint gives more precise figures: 949 agent sessions, 21.5 hours, 215.6 million tokens, 3,564 scored candidate families and 19 reports filed for review. The search ran over a database of 1.9 billion protein clusters, using agents running Claude Mythos 5, with one agent planning each task and a second reviewing it. Anthropic says such work can take an expert weeks to months.

After the agent spotted the repeats, it counted them, measured their spacing, compared the layout with known RT systems and searched the literature for earlier reports before filing its write-up. Human scientists at Anthropic's Bay Area lab then tested the finding. The lab works only at biosafety levels 1 and 2, does not handle pathogens that infect humans, and all bench work is done by people.

Feng Zhang, the CRISPR pioneer at MIT and the Broad Institute, reviewed the preprint. "This is an exciting example of how AI agents can contribute to biological discovery," he said. "The identification of RNA-repeat arrays associated with reverse transcriptases is genuinely intriguing and merits further investigation."

Anthropic CEO Dario Amodei framed the result cautiously on X. "Today we announced the Claude-led discovery of a molecular machine that we suspect could represent a new gene editing mechanism," he wrote. "Its precise function, biotechnological utility (if any), or level of significance is not yet clear." The company's post ties the group's mission directly to his *Machines of Loving Grace* essay and its argument that AI could speed up progress in biology.

## Why It Matters

Genome mining is how most modern molecular tools were found. Restriction enzymes, Taq polymerase and CRISPR all started as oddities that someone happened to notice in nature's sequence data. The bottleneck has always been human attention: someone has to read the right stretch of DNA and see that it is strange. ART suggests an agent swarm can do that noticing at scale, and do it overnight.

The preprint is also candid about the limits. Anthropic ran the same campaign ten more times, and none of the reruns read the DNA upstream of the enzyme, so all ten missed the array. In fixed tests, the company's top models described the array at least 90% of the time when given the DNA directly, but only about 32% of the time when they had to find it themselves using files and tools. The discovery was real, but it was also partly luck. That makes reliability, and not just raw capability, the key open problem for AI-driven science. Anthropic says it is now treating Claude's flood of hypotheses as an object of study, using what it learns about which candidates scientists choose to test to tune how the agents search.
## What to Watch

The big question is function. If follow-up experiments show that ART's short RNAs guide the enzyme to specific targets, the way CRISPR guides do, the field may have a new family of programmable DNA tools. If they do not, ART remains an interesting piece of phage biology. Watch for independent labs to test the preprint's claims, for peer review, and for whether Anthropic's open call for outside research proposals turns this lab into a shared discovery engine or keeps it an in-house showcase.
