A team led by Penn State materials scientists has built a memory device that runs on less than a tenth of a volt by sandwiching short strands of laboratory-made DNA, studded with silver nanoparticles, against a thin film of lead-halide perovskite semiconductor. The device is a memristor — a component that stores information in its own electrical resistance, which means it can hold data and compute on it in the same physical spot, the architecture the neuromorphic computing field has been chasing for two decades.

The work, "Molecularly Engineered Highly Stable Memristors with Ultra-Low Operational Voltage: Integrating Synthetic DNA with Quasi-2D Perovskites," was published in *Advanced Functional Materials* on January 19, 2026 (DOI 10.1002/adfm.202530539), with a patent application filed. It resurfaced this month after ScienceDaily republished Penn State's release under the headline "Scientists turn DNA into a memory device that uses 100x less power" — a framing worth pausing on, since the same release elsewhere says one-tenth the power, not one-hundredth.

## What They Actually Built

The device stack is Ag/(PEA)₂(MA)Pb₂I₇/AgNP-DNA/Pt: a silver top electrode, a quasi-two-dimensional halide perovskite layer, a composite layer of silver-nanoparticle-embedded synthetic DNA, and a platinum bottom electrode. The DNA is not a passive filler. The team computationally screened four custom constructs between 19 and 22 bases long for optimal charge-transfer rate and settled on a 22-mer, then doped it with silver nanoparticles — which both made the strands electrically conductive and forced them into a more ordered arrangement.

That ordering is the whole trick. Natural DNA in a thin film behaves, as the release memorably puts it, like wet spaghetti. Short synthetic strands are rigid enough to be positioned deliberately.

"We can computationally determine exactly which sequences we need and how long they should be, and then we can rationally design them with synthetic DNA," said Neela H. Yennawar, research professor and director of the Biomolecular Interactions Core Facility at Penn State's Huck Institutes of the Life Sciences. "These structures can be systematically doped with silver and other ions and engineered to interface seamlessly with perovskites — transforming DNA from a biological macromolecule into a programmable, multifunctional nanomaterials platform."

Together, the doped DNA and the perovskite form what the authors call bio-hybrid channels that funnel current through the cell. Switching states requires under 0.1 V — for scale, a US wall outlet is 120 V, and commercial resistive RAM typically switches in the 1–3 V range. The paper reports a power density of 0.01 W/cm², which the authors describe as a record low for perovskite memristors, and forming-free operation, meaning the device does not need a one-time high-voltage electrical "burn-in" to create its conductive pathway. That matters more than it sounds: forming steps are a persistent yield and variability headache in resistive memory manufacturing.

On stability, the arrays held an ON/OFF resistance ratio above 10⁵ for more than six weeks in ambient conditions and kept working at temperatures approaching 250°F (roughly 121°C). Endurance is reported at 10³ switching cycles and retention at 4 × 10³ seconds — about 67 minutes.

"Biology and electronics are different domains," said Kavya S. Keremane, co-corresponding author and a postdoctoral researcher in materials science and engineering at Penn State. "Bridging these two fields required developing an entirely new materials platform that allows them to function seamlessly together."

## Why It Matters

The energy case for compute-in-memory is not subtle. In a conventional von Neumann machine, data sits in DRAM and computation happens in a CPU or GPU, and shuttling bits across that gap costs far more energy than the arithmetic itself — for large neural network inference, memory traffic routinely dominates the power budget. AI data center electricity demand has become a live grid-planning problem in multiple US states. Any architecture that performs multiply-accumulate operations inside the memory array itself sidesteps that traffic entirely, which is why memristor crossbars have attracted sustained investment.

The bottleneck for that vision has been the devices. Oxide-based memristors need relatively high switching voltages, and voltage enters the energy equation quadratically, so a device operating below 0.1 V is genuinely interesting rather than incrementally so. The DNA layer contributes something the oxides do not: sequence-level programmability of the switching medium, plus DNA's extraordinary theoretical information density — roughly 215 million gigabytes per gram.

"As the demand for artificial intelligence grows, we need a new strategy for low-power, high-storage devices," said Bed Poudel, co-corresponding author and research professor of materials science and engineering at Penn State.

That 215-million-gigabyte figure, however, is a property of DNA as a molecule, not a measured storage density of this device. No such density was demonstrated here.

## What to Watch

This is a laboratory result, and the gap to a product is wide. Endurance of 10³ cycles is orders of magnitude short of what production non-volatile memory requires; NAND flash handles 10⁴–10⁵ program/erase cycles and commercial RRAM targets far more. Retention of 4 × 10³ seconds is roughly an hour against the JEDEC industry benchmark of ten years — the six-week figure describes shelf stability of the ON/OFF ratio under ambient storage, not how long a written state survives. No switching speed is reported in the abstract or any of the available coverage, which is a conspicuous absence for a memory claim, and no neural network task has been run on the hardware.

Then there is manufacturing. The perovskite is lead-based, which carries real regulatory friction; solution-processed perovskite films remain notoriously moisture-sensitive; and no one has demonstrated that a silver-doped oligonucleotide layer can survive CMOS back-end-of-line thermal budgets or wafer-scale patterning. Funding came from the NSF and NIH, with University of Minnesota collaborators including co-corresponding author Rashmi Jha (secondary coverage lists her affiliation as University of Cincinnati — the institutional attribution is inconsistent across writeups).

The right frame is a materials-platform demonstration with an unusually low operating voltage, not a memory technology in waiting. The next paper to watch is whichever one reports endurance and retention numbers that clear commercial thresholds — or explains why they cannot.
