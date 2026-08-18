The most expensive part of a frontier training run is no longer the GPU. It is increasingly the problem of getting bits from one GPU to another — and the industry has quietly concluded that copper cannot do it much longer.

A market study circulating this week puts a number on it: the global data center optical interconnect market reaching $144.4 billion by 2030, up from $13.7 billion in 2024 — a 48.1 percent CAGR, more than tenfold in six years. Silicon photonics takes 63.7 percent of that revenue, up from 16.6 percent in 2020, with co-packaged optics doing most of the pulling.

The provenance matters. The forecast is China Insights Consultancy's, prepared for laser maker Yuanjie Semiconductor as part of its Hong Kong IPO filing — a vendor-adjacent document written to support a listing, not an independent audit. The analyst spread is wide: Bank of America models AI optical connectivity going from $14 billion in 2025 to $73 billion by 2030, roughly half the CIC number. Treat $144 billion as the bullish end of a range, not a fact.

## Why Copper Runs Out

The underlying physics is not in dispute, and it is the more interesting story. At 112 Gbps per lane, a copper backplane cable reaches roughly 2.5 meters. Double the lane rate to 224 Gbps and that collapses to about one meter — skin-effect resistance, conductor roughness, return loss and inter-symbol interference all worsen faster than the signal budget can absorb. A meter is roughly the height of a rack. As lane rates rise to feed 1.6T ports, the distance a GPU can talk to another GPU over copper shrinks toward the size of the box it is already in.

Optics has no such ceiling, and vendors are moving the conversion point inside the package. Marvell's CPO architecture for custom accelerators, announced January 2025, aims at scaling AI servers "from tens of XPUs within a rack currently using copper interconnects to hundreds across multiple racks," at XPU-to-XPU distances it says are 100x longer than electrical cabling. "AI scale-up servers require connectivity with higher signaling speeds and longer distances to support unprecedented XPU cluster sizes," said Nick Kucharewski, senior vice president and general manager of Marvell's Network Switching Business Unit. "Integrating co-packaged optics into custom XPUs is the logical next step."

The energy arithmetic is the other half. Marvell's 6.4T 3D SiPho Engine — 32 channels of 200G electrical and optical interfaces in one device — claims 30 percent lower power per bit than 100G-generation equivalents. Nvidia's Spectrum-X Photonics switches, announced at GTC in March 2025, cut power per 1.6T port from roughly 30W for a pluggable transceiver to 9W co-packaged, with 3.5x better power efficiency, 4x fewer lasers and 63x greater signal integrity claimed platform-wide. Broadcom shipped Tomahawk 6 at 102.4 Tbps in June 2025 and followed in October with TH6-Davisson, the first 102.4 Tbps Ethernet switch with co-packaged optics.

## The Binding Constraint

Through 2023 and 2024, the limiter on training scale was GPU supply. That has shifted. A frontier training run is a synchronized computation: gradients are exchanged across every accelerator at every step, and the slowest link sets the pace for all of them. Once a cluster outgrows a single rack — which every frontier-scale cluster now does — scaling compute means scaling the fabric, and the fabric is where the watts and dollars are migrating.

Nvidia's framing is unsubtle. "AI factories are a new class of data centers with extreme scale, and networking infrastructure must be reinvented to keep pace," said Jensen Huang, founder and CEO of Nvidia, announcing the photonics switches. "By integrating silicon photonics directly into switches, NVIDIA is shattering the old limitations of hyperscale and enterprise networks and opening the gate to million-GPU AI factories." TSMC chairman and CEO C. C. Wei, whose company supplies the process, made the same argument from manufacturing.

That is vendor language, but the deployment curve is real. Quantum-X Photonics InfiniBand switches — 144 ports of 800Gb/s on 200Gb/s SerDes, liquid-cooled to keep the on-package optics in spec — were slated for late 2025, Spectrum-X Photonics Ethernet for 2026. Cignal AI projects more than 5 million 1.6T pluggables shipping in 2026, the technology's first volume year.

## Why It Matters

Every watt spent moving a bit is a watt not spent on a matrix multiply. In a power-constrained data center — and nearly all of them now are — a switch delivering a 1.6T port at 9W instead of 30W is not an efficiency nicety; it is the difference between fitting another few thousand accelerators inside the same substation contract or not.

It also reshapes the supply chain. CPO folds lasers, modulators, fiber attach and advanced packaging onto the same substrate as the compute die, so whoever owns packaging owns more of the system — Nvidia's photonics ecosystem runs to TSMC, Coherent, Corning, Fabrinet, Foxconn, Lumentum and SPIL. Which is also why a figure like $144 billion lands in an IPO document.

The counterweight is that CPO is still early and hard. Optics add latency copper does not, lasers fail in ways cables do not, and a dead optical engine on a switch package cannot be swapped like a pluggable module. LightCounting founder and CEO Vlad Kozlov put the trajectory in units rather than dollars: "We forecast that CPO will grow from less than 50 thousand port shipments today to over 18 million CPO ports by 2029, with most of the ports being deployed for connections within servers." That is an enormous ramp for a technology whose field reliability record is barely written.

## What to Watch

The 1.6T ramp is the cleanest reality check on every dollar forecast above it: whether Cignal AI's 5 million units actually ship in 2026, and at what yield. Watch whether hyperscalers put co-packaged optics into production fabrics or keep it in qualification while pluggables carry the volume — serviceability, not bandwidth, is the open question. Watch Broadcom's TH6-Davisson design wins against Nvidia's integrated stack. And watch the revisions: a market projected to compound at 48 percent for six years has never once been forecast accurately, in either direction.
