The image atop MIT's press release is a portrait nobody painted. Beside it sit more than 200 near-identical versions of the same face — each what the model would have produced had a different artist been struck from its training set. That is the finding rendered as a picture: remove any one of 744 artists, and the output barely moves.

Researchers at MIT's Computer Science and Artificial Intelligence Laboratory call this attribution decay, published Tuesday in Nature Communications under a title with no hedging in it: "Outputs of generative diffusion models are often unattributable." The claim is not that attribution tools are too crude. It is that at sufficient scale, there is nothing left to attribute.

"If you take away a piece of data and the output of the model doesn't change, then that piece of data didn't affect the output," said Zheng Dai SM '21, PhD '24, the former MIT CSAIL researcher who led the work. "And if you then do this one at a time for every other piece of data and find that the output doesn't change for any of them either, then it doesn't make much sense to attribute the output to any one of them."

## The Retraining Problem

The honest way to ask whether a training image mattered is to retrain the model without it and compare. Do that for every image and the compute bill becomes absurd, which is why the attribution field runs on approximations that estimate a sample's contribution rather than deleting it.

Dai and co-author David Gifford, an MIT professor and CSAIL principal investigator, built around the problem. Their "diffusion ensemble" splits a model into many smaller components, each trained on a different slice of data. To ask what the model would do without a given image, you switch off every component that saw it. No retraining. No estimate.

"All previous methods were approximate," Gifford said. "They really could not absolutely show that deleting individual things did not change the output. This paper introduces the first method that is absolute."

The metric that falls out is the counterfactual radius: generate one image, generate every alternate version produced by ablating a different unit of training data, and measure the distance to the most divergent. That distance ceilings how much any single piece of data could have mattered.

## Twenty-Four Ensembles, One Power Law

The team trained 24 diffusion ensembles on subsets ranging from 256 to 162,770 images, drawn from seven public collections including MNIST, CIFAR-10, CelebA, MetFaces, and ArtBench. The counterfactual radius shrank as training sets grew, following an inverse power law fitting at R² = 0.85 for pixel-level distance and R² = 0.59 for semantic distance measured by OpenCLIP, both significant at p < 10⁻⁵ on a one-sided Wald test.

The effect survived every attempt to break it. Redefining a "unit" from one image to all images of one person, or all works by one artist, produced drops of p < 10⁻⁵³ and p < 10⁻²². To rule out ablation as the culprit, the team brute-forced the comparison at small scale, training 1,282 diffusion models — 1,280 counterfactual, two factual — and the decay appeared anyway. Fixed removal fractions, fixed epochs, text prompts, class conditioning, LPIPS and DINOv2 metrics: it held throughout.

One figure makes it concrete. In a model trained on 1,336 artworks, removing Robert Campin's work visibly changed the output attributed to it. In a model trained on 50,000, removing every Thomas Jones painting left the output attributed to his View of Castel Gandolfo largely unchanged. On binarized MNIST, 14 of 3,731 samples had a counterfactual radius of exactly zero.

## Why It Matters

The paper is blunt about the legal consequence. Unattributability, the authors write, "ostensibly provides a refutation of access" — access being a required element of infringement — "thereby circumventing the intellectual property protections designed to limit such use as long as the harvest is conducted on a sufficient scale for attribution decay to manifest." Scrape enough, in other words, and the causal trail a plaintiff needs stops existing. The Register flagged what defense counsel will notice first: this doubles as a liability-avoidance strategy.

What it does not prove matters as much. The study covers leave-one-out attribution only; the authors say aggregate, subset-level, and approximate methods remain intact. It covers diffusion models, not the language models at the center of the biggest cases. And it does not touch memorization — prior work shows production models trained on roughly 10⁹ images still emit near-verbatim copies about one time in a million. A model can be statistically unattributable and still occasionally spit out your painting.

For compensation schemes built on per-work royalties traced through outputs, the finding is close to fatal. For pooled or collective licensing, it changes little.

Gifford frames the capability as an obligation, not a shield: "In order for these companies to claim their outputs aren't derivative of the internet in a copyright-infringing way, they need to revise their models to take advantage of the advances in this work, so they can show they're not creating derivatives of individual people or items."

## What to Watch

Whether attribution decay generalizes to language models is the open question, and the one that decides how much litigation this actually touches. Watch for the first filing to cite the paper — Andersen et al. v. Stability AI, where plaintiffs are still fighting for Midjourney's training datasets, is the obvious venue.

James Grimmelmann, a law professor at Cornell Law School and Cornell Tech, put the stakes in one line. "If attribution worked, it would reliably tell us whether similarities between a model's output and a copyright-protected work are due to copying or coincidence," he said. "But this paper provides reason to think that attribution will fail for interesting models. Instead, technologists and courts will need to resort to other methods for assessing copying."

He also told The Register something worth sitting with: output similarity for image models, the thing this paper says cannot be traced, "remains mostly untested in court."
