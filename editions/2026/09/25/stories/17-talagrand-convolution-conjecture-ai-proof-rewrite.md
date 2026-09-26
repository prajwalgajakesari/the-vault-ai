A mathematical question that sat open for 37 years was closed this summer by a proof more than 40 pages long. By mid-September, with help from ChatGPT, one mathematician had redone it in about seven. UC Irvine mathematician Paata Ivanisvili is pointing to that second paper as a sign of how fast AI is changing both the discovery of mathematics and the way it gets written down.

The paper is arXiv 2609.11290, "Some remarks on Talagrand's convolution conjecture," submitted on September 10 by Alexander Shaposhnikov. It gives short, self-contained proofs of the conjecture in two settings: the continuous Gaussian one and the discrete Boolean one. In a post on X, Ivanisvili, a professor of mathematics at UC Irvine who works on probability and functional inequalities, contrasted the new note with the 40-plus-page argument it replaces. He said further prompting of an AI system produced a version only about a page and a half long.

## A 1989 puzzle about smoothing

Michel Talagrand, who later won the Abel Prize, posed the conjecture in 1989 in the Israel Journal of Mathematics. In plain terms, it is about what happens when you blur data. Take a nonnegative function on a very high-dimensional space whose average value is 1. It may be extremely spiky. Markov's inequality, a basic rule of probability, says the chance that it exceeds some large value η is at most 1/η. For example, the chance of exceeding 100 is at most 1 percent.

Now smooth the function with a "heat" or noise operator. Think of heat spreading out from the peaks. Talagrand guessed that after smoothing, big spikes become measurably rarer than Markov's rule allows: the bound should improve by an extra factor on the order of the square root of log η. The size of that factor should not depend on how many dimensions the space has.

The Gaussian version fell first. Ronen Eldan and James Lee proved it up to a small extra factor, and Joseph Lehec later removed that factor. The discrete version, set on the Boolean hypercube (the space of all strings of plus and minus ones), held out longer. In November 2025, Yuansi Chen of ETH Zurich proved it up to an extra log log η factor using a "perturbed reverse heat" process. Tech outlet QbitAI, as republished by 36Kr, noted that the process is a close cousin of the diffusion models used in generative AI. In August 2026, Harvard's Junwei Lu, with Shengtao Guo and Ethan X. Fang, removed the last factor in arXiv 2608.15515, "Weak-Type Bounds for Convolution on the Boolean Hypercube." Their abstract states plainly: "The proof was discovered by the Odin Automatic AI Research Agent." The authors add that the final proofs "were reorganized by the authors."

## Martingales instead of machinery

Shaposhnikov's note takes a different route. It does not build on Chen's reverse-heat coupling. Instead it uses martingales, the mathematics of fair games, where a stopped process is tracked as it crosses a threshold. The Gaussian argument runs about two pages of stochastic calculus and uses a weighted version of the Itô isometry. The author calls one key step "a simple observation that we were unable to find in the literature." The Boolean argument follows the same outline, with coin flips standing in for Brownian motion.

The note also produces explicit constants, which earlier work often left unstated. In the Gaussian case, the probability of a spike above η is at most 1 divided by η times the square root of 2(1−s) log η. In the Boolean case, the constant is the square root of (1+ρ)/(1−ρ), where ρ measures how strongly the noise smooths the function. Neither bound grows with the number of dimensions.

The note is open about how it was made. Its final section, "The role of AI in this proof," says the author "acknowledges the use of ChatGPT-5.6 assistance to close the argument based on the supplied plan and preliminary gaussian case draft developed by the author." ChatGPT was also used for proofreading and numerical experiments.

Ivanisvili has followed this line of work closely. Earlier, when the Lu–Guo–Fang paper first appeared, he wrote on X: "Yesterday's arXiv submissions were particularly strong. Again, the ranking is due to AI. I especially like the result #5 on Talagrand's convolution conjecture on the Hamming cube."

## Why It Matters

For years the worry about AI-generated mathematics was correctness. This episode raises a second problem: readability. The first complete Boolean proof came from an automated research agent and ran long, as machine-found arguments often do, full of scaffolding a human expert would cut. Within weeks, a person with a plan and a chatbot to fill in the gaps produced a proof short enough to read in one sitting. It also reaches both settings with a single idea. So AI can serve as a compression tool as well as a discovery tool, turning a brute-force answer into an explanation.

Ivanisvili also agreed with AI researcher Christian Szegedy about the next step. Szegedy argued that the current habit of "deslopping" AI-written math, meaning cleaning it up by hand into one polished PDF for people to read, may itself be a temporary stage. If a model can shrink a 40-page argument to seven pages, then to a page and a half, the idea of one fixed, authoritative write-up starts to look optional. Readers could ask for whatever level of detail they need.

## What to Watch

Neither the Lu–Guo–Fang proof nor Shaposhnikov's note has been through peer review. The first test is whether experts confirm that the short martingale argument holds line by line, especially the Boolean case, which is newer and more delicate. Also watch whether journals and arXiv moderators set clearer rules for disclosing AI involvement. Both papers here disclosed it voluntarily, in their own words. Finally, watch whether the page-and-a-half version Ivanisvili described is ever posted. If it is, it would be a public test of how far AI-driven compression of research mathematics can go.
