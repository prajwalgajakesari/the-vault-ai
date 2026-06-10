---
headline: "UPenn's Mollifier Layers Bring Classical Math Into Neural Networks to Solve Inverse PDEs"
slug: upenn-mollifier-layers-inverse-pde
category: research
story_number: 12
date: 2026-06-09
---

# UPenn's Mollifier Layers Bring Classical Math Into Neural Networks to Solve Inverse PDEs

**By The Vault — AI Edition**

Imagine watching ripples spread across a pond and, from that pattern alone, calculating exactly where — and with how much force — a pebble struck the water. That is the kind of problem engineers at the University of Pennsylvania have just made significantly easier for machines to solve.

Researchers at Penn's School of Engineering and Applied Science have introduced a technique they call "Mollifier Layers," a lightweight module that grafts an 80-year-old idea from pure mathematics directly into modern neural networks. The result, published in *Transactions on Machine Learning Research* (TMLR) and set for presentation at NeurIPS 2026, enables AI systems to recover hidden parameters and driving forces from noisy, real-world data far more reliably — and far more cheaply — than existing methods allow.

"Solving an inverse problem is like looking at ripples in a pond and working backward to figure out where the pebble fell," said Vivek Shenoy, Eduardo D. Glandt President's Distinguished Professor in Materials Science and Engineering and the study's senior author. "You can see the effects clearly, but the real challenge is inferring the hidden cause."

## The Problem With How AI Currently Does the Math

Physics-informed machine learning — a field that folds the governing equations of physical systems directly into the training of neural networks — has matured quickly over the past decade. But a stubborn bottleneck has limited its reliability: computing derivatives.

To satisfy the constraints imposed by partial differential equations (PDEs), AI models must repeatedly differentiate their own outputs, a procedure known as recursive automatic differentiation, or autodiff. For first-order problems and clean data, autodiff works reasonably well. Push into higher-order systems or introduce measurement noise, however, and the method begins to amplify errors with each successive differentiation step — the mathematical equivalent of repeatedly zooming in on a jagged line until all you can see is the jitter.

For the Shenoy Lab, the friction was immediate and biological. The group studies how chromatin — the tightly wound complex of DNA and proteins inside cell nuclei — organizes itself at nanometer scales, and how epigenetic reactions (the chemical signals that switch genes on and off) shape that organization. "We could see the structures and model their formation, but we could not reliably infer the epigenetic processes driving this system," Shenoy said. "The more we tried to optimize the existing approach, the clearer it became that the mathematics itself needed to change."

## Enter the Mollifier, Vintage 1944

The fix the Penn team landed on was not invented last year. Kurt Otto Friedrichs, a German-American mathematician who would later receive the National Medal of Science, described "mollifiers" in a 1944 paper. In loose terms, a mollifier is a smooth, compactly supported kernel that, when convolved with a rough or noisy function, irons out its sharpest irregularities while preserving its essential shape. The name itself has a curious history: Friedrichs reportedly asked a colleague what to call the smoothing operator, and the colleague — whose nickname was "Moll" — suggested a term that incorporated both his name and the verb "to mollify," meaning to soothe or smooth over.

The Penn team realized that placing a mollifier-based convolutional operation at the output layer of a neural network could replace the recursive autodiff chain entirely. Instead of differentiating through the network's depth, the model computes derivatives by convolving its output with the analytically known derivatives of the mollifier kernel — a single, stable operation that suppresses noise rather than magnifying it.

"We initially assumed the issue had to do with the neural network's architecture," said Ananyae Kumar Bhartari, a graduate of Penn Engineering's Scientific Computing master's program and a co-first author of the paper. "But, after carefully adjusting the network, we eventually realized the bottleneck was recursive automatic differentiation itself."

The intervention is deliberately modest in footprint. Mollifier Layers attach at the output stage and require no changes to the underlying network architecture, making the method architecture-agnostic and easy to drop into existing physics-informed frameworks.

## Results: Noise Robustness, Lower Memory, Faster Training

Benchmarks in the paper span first-, second-, and fourth-order PDEs — covering Langevin dynamics, heat diffusion, and reaction-diffusion systems — and show significant improvements across accuracy, memory consumption, and training time for parameter recovery. The authors report that implementing the mollifier layer "radically diminished both the noisiness and the power consumption scaling," in Bhartari's words.

"Modern AI often advances by scaling up computation," said Vinayak Vinayak, a doctoral candidate in Materials Science and Engineering and the paper's other co-first author. "But some scientific challenges require better mathematics, not just more compute."

The robustness to noise is particularly noteworthy because inverse problems in science almost always involve imperfect measurements. A method that degrades gracefully under realistic data conditions — rather than one that requires artificially clean inputs — is the more practical tool.

## Why It Matters

The physics-informed neural network (PINN) space has attracted enormous research interest precisely because it promises to embed domain knowledge — conservation laws, force balances, reaction kinetics — directly into learned models, rather than requiring enormous labeled datasets. But PINNs have faced persistent criticism for instability and sensitivity to hyperparameter choices. Mollifier Layers address one of the field's core technical liabilities: the unreliability of high-order autodiff under realistic conditions.

This matters well beyond benchmark papers. Inverse PDEs underpin a remarkably broad range of real-world challenges. In materials science, researchers use them to infer the internal stress states of structures from surface measurements — useful for detecting flaws without destructive testing. In fluid dynamics, they help reconstruct hidden velocity fields or pressure gradients from sparse sensor data, with implications for turbulence modeling and aerodynamic design. In medical imaging, techniques like electrical impedance tomography reconstruct internal tissue conductivity from boundary voltage measurements — a paradigmatic inverse PDE problem where noise robustness is not optional.

The Penn group's immediate focus is chromatin biology. "These domains are just 100 nanometers in size," Shenoy said, "but because accessibility determines gene expression, and gene expression governs cell identity, function, aging and disease, these domains play a critical role in biology and health." By inferring the epigenetic reaction rates that drive chromatin reorganization, mollifier layers could help researchers move from static structural images toward dynamic, predictive models of gene regulation — with downstream implications for cancer, aging, and developmental biology.

"If we can track how these reaction rates evolve during aging, cancer or development," Vinayak added, "this creates the potential for new therapies: If reaction rates control chromatin organization and cell fate, then altering those rates could redirect cells to desired states."

## What to Watch

Several threads are worth following as this work circulates ahead of NeurIPS 2026. First, independent replication: the benchmarks are compelling, but the community will want to see whether the noise-robustness advantages hold across a wider range of PDE families and network architectures. Second, software integration: because Mollifier Layers are architecture-agnostic, the path to adoption runs through popular physics-informed frameworks — watch for community-contributed implementations in DeepXDE, NeuralPDE, and similar libraries. Third, scale: the current paper focuses on parameter recovery in relatively controlled settings; extending the approach to high-dimensional or multi-physics systems will be the next real test.

Most broadly, the work is a reminder that the mathematical heritage underlying scientific machine learning runs deep. Friedrichs published his mollifier paper more than eight decades ago, years before the first programmable digital computers were operational. That an idea from that era can resolve a bottleneck in 2026-era AI training is not ironic so much as instructive: the foundations of functional analysis were built precisely to handle the kinds of irregular, noisy objects that real-world measurement produces. The field of scientific ML is still, in a meaningful sense, catching up to the tools the mathematicians left behind.

"Ultimately, the goal is to move from observing complex patterns to quantitatively uncovering the rules that generate them," Shenoy said. "If you understand the rules that govern a system, you now have the possibility of changing it."

---

**Paper:** "Mollifier Layers: Enabling Efficient High-Order Derivatives in Inverse PDE Learning," Vinayak Vinayak, Ananyae Kumar Bhartari, Vivek B. Shenoy. *Transactions on Machine Learning Research*, 2026. arXiv:2505.11682.

**Sources:** Penn Engineering (seas.upenn.edu); ScienceDaily (sciencedaily.com/releases/2026/05/260505234605.htm); arXiv (arxiv.org/abs/2505.11682); OpenReview (openreview.net/forum?id=6mFVZSzyev).
