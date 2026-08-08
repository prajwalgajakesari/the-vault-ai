# AI Designs Working Viruses for the First Time, Exposing a Biosecurity Governance Gap

For billions of years, the genetic code of viruses has been written by evolution. As of this month, some of it has been written by an algorithm — and the results are alive.

In a study published in *Science* on August 6, 2026, researchers at Stanford University and the Arc Institute reported the first peer-reviewed demonstration of generative AI designing complete, functional viral genomes from scratch. Using genome language models known as Evo 1 and Evo 2 — trained on roughly 2.7 million genomes and built on the same "predict the next unit" logic that powers text chatbots — the team generated novel genomes for bacteriophages, viruses that infect bacteria. Of the candidates the researchers synthesized and tested in the lab, 16 produced fully working phages that infected and killed *E. coli*. Crucially, these viruses infect bacteria, not humans, and the models were deliberately trained without genomes of pathogens that infect people, animals, plants, or fungi.

The scientific milestone landed alongside an unusually direct warning. In a companion editorial in the same issue of *Science*, biosecurity specialists at the Johns Hopkins Center for Health Security argued that the governance needed to steer this capability safely does not yet exist.

## A Milestone in Genome Design

The project was led by Brian Hie, an assistant professor of chemical engineering at Stanford, and Samuel King, a bioengineering graduate student and the paper's first author. Unlike gene editing, which tweaks an existing organism, the models composed entire genomes with no natural precursor — sequences that match nothing in existing biological databases. Some of the AI-designed phages killed bacteria more efficiently than the natural virus they were modeled on, and the team reported that a cocktail of the 16 phages rapidly overcame resistance in *E. coli* strains that were already immune to the natural version.

That resistance-beating property is the point. Antimicrobial resistance is tied to more than a million deaths a year, and phage cocktails are a long-discussed alternative to failing antibiotics.

"If the bacteria gain resistance to a single phage, it's game over for the medication," Hie said in a Stanford statement. "But if you have multiple genetically distinct phages in a mixture, it would be harder for the bacteria to develop resistance to the entire cocktail."

King framed the achievement as an opening rather than an endpoint. "One of the most rewarding parts of this project is the creativity Evo 2 allows," he said. "New doors in science are now open because of what we can do with these models." The team released Evo 2 as an open-source tool, arguing that open access accelerates defensive research and that, unlike naturally evolving pathogens, AI tools can have safety checks built in.

## Why It Matters

The same capability that could accelerate new antibiotics is a textbook example of a dual-use technology — beneficial and dangerous depending on who wields it. The Johns Hopkins editorial by Thomas Inglesby and Moritz Hanke described the research as raising urgent biosafety and biosecurity questions, and pointed to a specific, structural gap.

Today's frontline defense sits at the companies that turn digital sequences into physical DNA. That screening is voluntary rather than legally required in the United States, and it works by matching orders against databases of known dangerous sequences. AI-designed genomes are, by definition, novel — they have no evolutionary history and therefore match nothing in those databases. In other words, the screening system was built to catch sequences that living organisms have carried, not sequences no organism has ever carried. Separate research teams have also shown that safety measures can be undone: fine-tuning a model on the very data it was meant to exclude can recover more dangerous capabilities.

Experts caution against overstatement. Tom Ellis, a synthetic genome engineering professor at Imperial College London, told reporters the work also shows how constrained the technology remains, noting that a human-infecting virus such as SARS-CoV-2 has a genome roughly six times larger and would be exponentially harder to design. He and others argue that manipulating existing, readily available pathogens remains a more immediate threat than AI-designed ones.

## What to Watch

The near-term fight is over policy, not laboratories. Inglesby and Hanke have called for legally mandatory screening of both DNA sequences and the customers ordering them, and for restrictions on applying these generative techniques to human, animal, and crop pathogens. Legislation moving through the U.S. Senate — the Biosecurity Modernization and Innovation Act — would mandate screening, though critics note it still leans on the same similarity-matching approach that novel sequences can slip past. The deeper technical challenge is developing screening that evaluates what a sequence can do, not merely what it resembles. No such system is deployed today.

---

*This is a sensitive dual-use topic. This report deliberately omits operational and methodological detail, and focuses on the scientific milestone, the governance gap, and expert reaction.*
