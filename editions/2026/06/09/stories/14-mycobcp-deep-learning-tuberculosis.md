---
headline: "A Deep Learning System Called MycoBCP Spots Subtle Tuberculosis Cell Changes"
slug: mycobcp-deep-learning-tuberculosis
category: research
story_number: 14
date: "2026-06-09"
---

# A Deep Learning System Called MycoBCP Spots Subtle Tuberculosis Cell Changes

When researchers at UC San Diego and Linnaeus Bioscience stared at fluorescence microscopy images of *Mycobacterium tuberculosis* cells, they quickly hit a wall. The bacteria clump together, refuse to define their own boundaries, and present changes so subtle after drug treatment that the human eye simply cannot parse them reliably. So they handed the job to a convolutional neural network and watched it crack the problem.

The result is MycoBCP, a deep learning platform described in a February 2025 paper published in the *Proceedings of the National Academy of Sciences*. Developed over two years with funding from the Bill and Melinda Gates Foundation, MycoBCP is an AI-driven adaptation of an established technique called bacterial cytological profiling, or BCP, a method that reads how a bacterium's cells change shape, membrane permeability, and DNA organization after exposure to an antimicrobial compound, using those changes as a fingerprint of how the drug actually works.

The system was trained on more than 46,000 fluorescence images of TB cells. In blind testing, it correctly identified the mechanism of action (MOA) for 96 percent of compounds tested, and pinpointed the exact molecular target for 76 percent of those, performance well beyond what traditional image analysis or manual inspection could achieve.

## How MycoBCP Reads a Cell

Bacterial cytological profiling is not new. Joe Pogliano, a professor in the Department of Molecular Biology at UC San Diego, and his wife Kit Pogliano, dean of the UC San Diego School of Biological Sciences, pioneered the underlying technique and spun it out into a company, Linnaeus Bioscience, in 2012. Their original insight was straightforward: a drug leaves a signature on the cells it attacks. Read the signature, and you learn the mechanism. They described the process as performing an autopsy on a bacterial cell.

What made TB different and harder was the bacterium itself. *Mycobacterium tuberculosis* grows slowly, forms tight clumps, and presents boundaries so indistinct that conventional image segmentation software fails. The Pogliano lab solution was to abandon segmentation entirely and train deep neural networks to detect patterns across entire fields of cells rather than outline each one individually.

“Tuberculosis cells are clumpy and seem to always stick close to each other, so defining cell boundaries did not seem possible,” said Joseph Sugie, chief technology officer at Linnaeus Bioscience and a lead author of the study. “Instead, we jumped straight into letting the computer analyze the patterns in the images for us.”

Sugie and co-lead author Diana Quach, both PhD graduates from the UC San Diego Shu Chien-Gene Lay Department of Bioengineering, trained MycoBCP's convolutional neural networks on cells stained with fluorescent markers: membranes dyed red, DNA dyed blue, and areas of membrane permeability appearing green. Each compound treatment produces a distinct visual profile of color and shape shifts, profiles the network learned to classify with high confidence.

## Seeing What Eyes Cannot

The implications go beyond academic interest. Determining a drug candidate's mechanism of action is one of the earliest and most critical gatekeeping steps in tuberculosis drug development. Without knowing how a compound works, researchers cannot predict resistance pathways, optimize chemical structure, or make informed decisions about which molecules deserve the costly investment of clinical trials.

“A critical component of progressing towards new drug candidates is defining how they work, which has been technically challenging and takes time,” said Tanya Parish, a tuberculosis expert at the Seattle Children's Research Institute and a co-author of the study. “This technology expands and accelerates our ability to do this and allows us to prioritize which molecules to work on based on their mode of action.”

Under traditional laboratory approaches, establishing MOA for a single compound against *M. tuberculosis* can take months. MycoBCP compresses that timeline dramatically, running high-throughput screens of large compound libraries and returning ranked, classified results in a fraction of the time.

Joe Pogliano framed the novelty plainly: “This is the first time that this kind of image analysis using machine learning and AI has been applied in this way to bacteria. Tuberculosis images are inherently difficult to interpret by the human eye and traditional lab measurements. Machine learning is much more sensitive in being able to pick up the differences in shapes and patterns that are important for revealing underlying mechanisms.”

## Why It Matters

Tuberculosis remains one of the most lethal infectious diseases on Earth. According to the WHO Global Tuberculosis Report 2025, an estimated 10.7 million people fell ill with TB in 2024 and more than 1.2 million died, numbers that have barely budged despite decades of global health campaigns. Drug-resistant strains compound the crisis: India alone accounts for roughly 32 percent of multidrug-resistant TB cases worldwide, with the Philippines, China, and Russia trailing behind. The 2025 End TB Strategy milestone called for a 50 percent reduction in incidence since 2015; actual progress stands at just 12 percent.

That gap means new drugs are urgently needed, and the pipeline is thin. Drug discovery for TB is slow in part because the pathogen is dangerous to handle, grows at a glacial pace in the lab, and resists the standard assays that work well for faster-growing bacteria. Anything that can accelerate the mechanism-of-action step, which informs every subsequent stage of development, represents real leverage.

MycoBCP offers exactly that: a faster, more sensitive front-end screen that tells researchers not just whether a compound kills *M. tuberculosis*, but how. That distinction matters enormously. Two compounds with identical kill rates but different mechanisms may have very different profiles when it comes to resistance development, synergy with existing drugs, or toxicity in human tissue. Knowing the mechanism early lets researchers make better bets.

The platform also opens a path toward examining drug combinations, testing whether two compounds that hit different cellular targets produce additive or synergistic effects, a capability that could be especially useful in designing regimens against drug-resistant strains.

## What to Watch

The paper represents a research proof-of-concept, but Linnaeus Bioscience is a commercial entity with a track record of supplying BCP analysis to pharmaceutical partners worldwide. Whether MycoBCP follows that commercial pathway, becoming a service offered to drug discovery programs globally, will be worth tracking. A correction note published in PNAS suggests the authors remain actively engaged with the paper, a sign the work is attracting scrutiny and discussion.

More broadly, MycoBCP is an early example of what might become a standard step in antibiotic discovery: AI-driven cytological profiling applied to pathogens that have historically been too difficult to study at scale. If the approach can be extended to other slow-growing or morphologically complex bacteria, the implications reach well beyond tuberculosis. For a field desperately short of new antibiotics, that would be significant news.
