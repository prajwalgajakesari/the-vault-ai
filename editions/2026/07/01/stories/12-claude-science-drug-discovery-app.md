When Dario Amodei stood up in San Francisco on Tuesday to launch Anthropic's newest product, he did not pitch it as a chatbot with a lab coat. He pitched it as an attempt to do to biology what the company already did to software.

Anthropic on June 30 released Claude Science, a dedicated application that reshapes its large language models for scientific research, with an unmistakable focus on drug discovery, protein structure analysis, genomics and computational biology. The product is available in beta now for Pro, Max, Team and Enterprise users, running locally on macOS and Linux or over SSH to a lab's own cluster. It is the most concrete expression yet of Amodei's repeated claim that AI could compress the timeline of life-sciences R&D by something on the order of 10x, turning decades of biological progress into years.

"It's going to be a general purpose technology that helps us to make sense of that complexity, in its full complexity, better," Amodei said at the launch event, according to STAT News. He was candid about the uncertainty, adding: "We don't know for sure if that's going to work out. But I think we're seeing signs that we're seeing the beginnings of it."

## What Claude Science actually does

The pitch is that scientific research is tedious plumbing as much as insight. Researchers bounce between dozens of databases with incompatible schemas, wrestle bespoke file formats, and shuttle between PubMed, Jupyter, R and a cluster terminal to get anything done. Claude Science folds those fragmented tools into a single environment coordinated by a generalist agent with access to more than 60 curated skills and connectors, pre-configured for genomics, single-cell analysis, proteomics, structural biology and cheminformatics.

Two design choices are aimed squarely at the credibility problem that has kept scientists wary of large language models. First, every output carries an auditable history: when Claude Science generates a figure, it ships the exact code, the computing environment and a plain-language account of how it was made, so results can be reproduced months later. Second, a dedicated reviewer agent inspects outputs as the pipeline runs, flagging incorrect citations, untraceable numbers and figures that do not match their underlying code, then self-correcting. Lower hallucination on technical biochemistry is not a marketing footnote here; it is the entire wager.

The app renders 3D protein structures, genome browser tracks and chemical structures natively, and queries specialist sources such as UniProt, PDB, Ensembl, ClinVar and ChEMBL on a researcher's behalf. It also connects to NVIDIA's BioNeMo toolkit, tapping open life-sciences models including Evo 2, Boltz-2 and OpenFold3, and can push heavy jobs to a lab's HPC cluster or to on-demand GPUs through Modal.

## The build-up: a $400M deal and a Nobel hire

Claude Science did not appear from nowhere. Over roughly eight months Anthropic assembled a deliberate AI-for-science stack. In April it paid about $400 million in stock for Coefficient Bio, a stealth biotech with fewer than 10 employees, most of them former Genentech computational-biology researchers, folding protein-design and biomolecule-modeling expertise into a healthcare and life-sciences division led by Eric Kauder. The company also announced founding partnerships with the Allen Institute and Howard Hughes Medical Institute earlier this year.

The signal hire came in June, when John Jumper announced he was leaving Google DeepMind after nearly nine years to join Anthropic. Jumper led AlphaFold, the system that cracked protein-structure prediction, and shared the 2024 Nobel Prize in Chemistry for it. Recruiting the single person whose work most convincingly proved AI could crack biology reads as a statement of intent about where Anthropic thinks the frontier is moving.

## Early results, and the caveats

Anthropic points to concrete beta work. Jerome Lecoq, a neuroscientist at the Allen Institute, built a multi-agent "computational review template" of about 20 custom skills; sub-agents read through thousands of papers, extract central claims and quantitative findings into an evidence database, then draft long-form reviews section by section with actor-critic pairs checking accuracy and citations. Reviews that once took his team up to two years now number about 10 drafts, many over 100 pages.

At the UCSF Brain Tumor Center, epidemiologist Stephen Francis used the app for germline-variant studies in glioma and reported comprehensive workups in roughly one-tenth the time, with his group independently validating the results. Manifold Bio used it to nominate targets for tissue-targeting medicines, assessing surface expression, trafficking and safety end-to-end. These are curated success stories, not peer-reviewed benchmarks, and the reproducibility features exist precisely because AI-generated science still has to earn trust it does not yet have.

## A three-way race among the same labs

Claude Science lands in a market defined by the same frontier labs now converging on biology. OpenAI launched GPT-Rosalind in April alongside Amgen, Moderna and Thermo Fisher. Google's Isomorphic Labs, spun out of DeepMind and built on AlphaFold lineage, has been chasing AI-designed drugs for years. The result is a three-way contest in which Anthropic, OpenAI and Google are competing not just for pharma contracts but for the same scarce pool of computational biologists, Jumper's move being the loudest example.

The strategic logic is also commercial. Anthropic is widening its enterprise footprint, and pharma R&D budgets are among the deepest and least price-sensitive in any industry, a useful revenue narrative for a company reportedly eyeing an IPO. To seed adoption, Anthropic is offering discounted lab seats, up to $30,000 in credits across as many as 50 research projects, and up to $2,000 in Modal compute; applications close July 15, with awards by July 31.

## What to watch

Three things. First, whether independent, published results validate the 10x-compression claim, or whether the reproducibility layer merely makes plausible-looking work easier to check, not more correct. Second, how quickly pharma buyers commit real budgets versus running cautious pilots, and whether they pick Claude Science, GPT-Rosalind or Isomorphic's approach. Third, what role Jumper actually takes, and whether Anthropic can turn a Nobel-caliber hire into shipping capability rather than a recruiting headline. Amodei has staked a large claim on biology being as tractable as code. The next year of results will show whether that was foresight or wishful thinking.
