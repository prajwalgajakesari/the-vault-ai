# Huawei's Atlas 950 SuperPoD Chains 8,192 Ascend Chips and Claims 6.7x Nvidia's NVL144

For ten months, Huawei's Atlas 950 SuperPoD existed only as a slide deck and a promise. On July 16, it showed up in a room in Shanghai with the doors open.

At the World Artificial Intelligence Conference, Huawei rolled a working Atlas 950 SuperPoD onto the floor of the Shanghai World Expo Exhibition and Convention Center — 1,024 Ascend NPUs wired across 16 cabinets, running as a single logical machine. The configuration on display delivers 1 EFLOPS at FP8 and 2 EFLOPS at FP4, with 256 TB of globally addressable memory, terabyte-scale NPU interconnect bandwidth and a round-trip latency of roughly 3 microseconds. It is one-eighth of the full system. At maximum scale, Huawei says a single Atlas 950 SuperPoD links 8,192 Ascend 950DT chips across 160 cabinets — 128 for compute, 32 for communications — occupying about 1,000 square meters of floor space. General availability: the fourth quarter of 2026.

The number Huawei wants repeated is 6.7. That is the multiple by which the company says the full Atlas 950 SuperPoD beats Nvidia's NVL144, the rack-scale Blackwell-generation system Nvidia has slated for the back half of this year. Huawei also claims 15x the memory capacity and 62x the interconnect bandwidth.

## What was actually shown, and what was not

The gap between the show floor and the spec sheet matters here, and it is worth being precise about it.

The unit demonstrated at WAIC was the 1,024-chip base configuration. Every comparative claim against Nvidia — the 6.7x, the 15x — refers to the 8,192-chip full build, which has not been publicly demonstrated running as one machine. Huawei's own numbers for that full configuration, laid out by Deputy Chairman Eric Xu at Huawei Connect last September, are 8 EFLOPS FP8, 16 EFLOPS FP4, 1,152 TB of memory and 16 PB/s of interconnect bandwidth.

There is also an unreconciled figure. Xu's spec puts 144 GB of HiZQ 2.0 HBM on each Ascend 950DT, which works out to 147 TB of NPU memory across 1,024 chips — not the 256 TB Huawei quoted at WAIC. The larger number presumably counts pooled host and system memory addressable over UnifiedBus, Huawei's proprietary interconnect protocol, but the company did not break it out. None of the performance figures have been independently benchmarked by a third party.

Huawei paired the hardware reveal with commercial numbers meant to argue that this is a shipping business, not a demo: more than 750 commercial deployments of the previous-generation Atlas 900 A3 (384 chips), over 3,000 ecosystem partners, 7,000 co-developed solutions, and a CANN open-source community that has grown to 67 projects and 12.44 million lines of code since Huawei open-sourced the stack at the end of last year.

## Interrogating the 6.7x

Run Huawei's comparison backwards and the story changes shape.

The Atlas 950 SuperPoD at full scale carries 8,192 NPUs. NVL144 carries 144 GPU packages. That is 56.8 times as much silicon — a ratio Xu stated himself on stage — producing 6.7 times the compute. Per chip, in other words, Nvidia's Blackwell-generation part is roughly eight and a half times ahead of the Ascend 950DT. The Ascend 950 die is rated at 1 PFLOPS FP8 and 2 PFLOPS FP4, with 2 TB/s of interconnect bandwidth. It is a competent chip. It is not a competitive chip on a one-to-one basis, and Huawei has never claimed otherwise.

Xu was unusually blunt about why the architecture looks the way it does. "For reasons we all know, we don't have access to advanced process nodes, so we've decided to focus our efforts on making breakthroughs by combining chips — essentially connecting more computing resources," he said in his keynote. The Atlas 950 is not an attempt to out-engineer TSMC's leading edge. It is an attempt to route around it with optics, protocol design and floor space.

That trade has a price tag, and Huawei did not put it on a slide. No power figure for the Atlas 950 SuperPoD has been published. Independent analysis of the previous-generation CloudMatrix 384 — the Huawei Cloud instance built on Atlas 900 A3 SuperPoDs — estimated it drew several times the power of an equivalent Nvidia NVL72 rack for comparable output. Scaling to 8,192 chips across 160 cabinets does not make that ratio better. In a market where power, not silicon, is the binding constraint on new data centers, that is the number to ask for.

"We're pretty confident that, for the next few years, the Atlas 950 SuperPoD will remain the world's most powerful SuperPoD," Xu said. "And it will far exceed its counterparts across all major metrics." Nvidia's response, issued after the September roadmap reveal, was terser: "The competition has undeniably arrived and is gaining momentum," a company spokesperson told CNBC.

## The actual stakes

Export controls were designed to deny China leading-edge chips. They were not designed to deny China cabinets, optical modules, interconnect protocols and floor space, and those are the axes Huawei is now competing on. If a Chinese lab can train a trillion-parameter model on a domestically built, US-component-free rack — at worse efficiency and higher power cost, but on schedule — then the control regime has bought time rather than capability.

Whether that is true is not yet knowable from a WAIC demo. What to watch: a customer running a frontier-scale training job on the full 8,192-chip configuration, published power-per-token figures, and whether Huawei can supply enough of its in-house HiBL and HiZQ HBM to build the Atlas 950 SuperCluster it has promised for the same quarter — 64 SuperPoDs, 520,000 chips, 524 EFLOPS FP8. Memory supply, not compute design, is the most likely place this roadmap slips.
