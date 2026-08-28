For several months, a materials lab at Washington State University tried to 3D-print a NASA copper alloy and failed 37 consecutive times. Then a computer science group asked for the failure data. Nothing else, just the 37 parameter sets that had produced brittle columns, oversized beads and test blocks that fell apart on the machining table. Three months and 40 more prints later, the collaboration had six settings that worked, including one at 500 watts of laser power, a level at which this alloy had never been successfully printed.

The paper, "Discovery of Feasible 3D Printing Configurations for Metal Alloys via AI-Driven Adaptive Experimental Design," appeared in the Proceedings of the AAAI Conference on Artificial Intelligence and took the conference's Innovative Deployed Application Award. First author Azza Fadhel is a PhD student in computer science; her co-authors are Nathaniel W. Zuckschwerdt, Susmita Bose and Amit Bandyopadhyay of WSU's School of Mechanical and Materials Engineering, Aryan Deshwal of the University of Minnesota, and Jana Doppa, the Huie-Rogers Endowed Chair Professor of Computer Science at WSU, who led the project.

Two details are worth pinning down, because the shorthand circulating around this study gets both wrong. The alloy is GRCop-42, a copper-chromium-niobium alloy NASA developed for regeneratively cooled rocket combustion chambers, not GRX-810, NASA's better-known oxide-dispersion-strengthened superalloy. The process is directed energy deposition, in which powder is blown into a moving laser's focal point, not the powder-bed fusion most people picture.

Copper resists both halves of the job. It reflects most of the infrared light fiber lasers emit, and it conducts heat away too fast for a stable melt pool to form. The standard workaround is brute force, 2 to 4 kilowatts, while more than 90 percent of commercial metal printers top out between 500 and 1,000 watts.

"Ninety percent of commercial printers cannot print this metal alloy, so given that we were able to find these feasible process parameters, it allows us to use those commercial printers, and we are essentially democratizing the printing of this alloy," Doppa said.

## What 100 million actually means

The number deserves a straight explanation. The search space is five controllable parameters, each chopped into a grid: powder feed rate, carrier gas flow, Inconel substrate thickness, scan speed from 200 to 1,600 mm/min in steps of 50, and layer height from 0.05 to 0.5 mm in hundredths. Multiply it out and you get roughly 102 million combinations, per laser power level.

This is not 100 million distinct hypotheses. It is five continuous knobs, discretized, and the number is partly a function of how finely the team chose to chop them. Say it that way and nothing important deflates. The successful region is still vanishingly small, and every wrong guess costs real money: each machine run runs $500 to $1,000, and post-print analysis adds roughly $500 per sample and one to four weeks of waiting.

## The method is active search, not Bayesian optimization

The team calls its approach BEAM, for Bayesian Experimental design for Additive Manufacturing, but the paper carefully distinguishes it from Bayesian optimization proper. Standard BO assumes a continuous objective with good solutions clustered near optima. Here the signal is binary and the successes are sparse and scattered, so the authors reframe the problem as active search under severe class imbalance, closer to classification than optimization.

The machinery is deliberately modest. The surrogate is a probabilistic k-nearest-neighbors classifier with k=5, initialized on those 37 failures, estimating the probability that any untested grid point will succeed. The acquisition function adds an exploration term, scoring a candidate not only on how likely it is to work but on how much the remaining budget benefits from learning its outcome. Expert constraints prune candidates first, and the system proposes two experiments at a time.

"It's a very challenging case for AI," Doppa said. "Every time you try, you basically get a binary success or failure signal, and you are trying to minimize the number of tries that you have so that you get to those successful needles very quickly."

The budget was 10 experiments at each of four power levels: 950, 700, 600 and 500 watts. Every level yielded at least one working configuration inside its budget, six in total. The insight the team took away is that unusually high scan speeds paired with lower-than-normal layer heights were the key, which is not what DED practice for other materials would have suggested.

## What AI for science looks like when it is honest

There is no language model anywhere in this pipeline. Nothing wrote a hypothesis or drafted a paper. A five-nearest-neighbor classifier over five numbers decided which expensive thing to do next, and that decision was the entire contribution. Set against the current genre of "AI scientist" announcements, the contrast is instructive: the win here is measurable precisely because the claim is narrow enough to check.

Fadhel's description of the loop captures why binary failure data is an asset rather than a write-off. "They would give me back the results, and I liked all of them, even if they failed, because every result improved our AI model," she said.

## What does not transfer

The result is bound to one setup: a 5-axis powder-fed FormAlloy system with a 1,000-watt fiber laser, argon below 20 ppm oxygen, Carpenter Additive powder at 15 to 53 microns, GRCop-42 deposited onto Inconel 718. Geometry, hatching strategy and build length were held fixed. Change the machine, the powder lot or the part shape and the prior encoded in those 37 failures is worth considerably less.

The paper argues that consistent performance across four power levels gives "reasonable confidence" the method generalizes. That is robustness within one setup, not transfer across setups. The success label is also a human metallurgical judgment, not an automated measurement, so the loop runs no faster than that analysis step.

What to watch: whether a second lab on different hardware reproduces the low-power window; whether the six configurations survive full mechanical qualification; and whether the approach reaches the alloys the authors flag as the real prize, Al6061, Al7075 and Al2024, used everywhere in aerospace and still unprintable on most sub-kilowatt machines.
