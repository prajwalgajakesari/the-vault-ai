# Nvidia's Vera Rubin Platform Goes Live, Ushering In the 'Gigascale' AI Factory

The AI hardware race crossed a new threshold this week. Nvidia's Vera Rubin platform — the successor to Blackwell that the company unveiled at CES in January — moved from keynote promise to production reality, with rack-scale systems ramping at CoreWeave, Google Cloud, Microsoft Azure and Oracle Cloud Infrastructure. The moment was punctuated on July 21 in Fort Worth, Texas, where contract manufacturer Wistron cut the ribbon on a roughly 324,000-square-foot U.S. plant now building Nvidia superchips on American soil.

Nvidia is calling the new era "gigascale": AI factories stitched together not from thousands of accelerators but from hundreds of thousands of GPUs and CPUs, drawing gigawatts of power to churn out tokens the way an industrial plant churns out goods.

"Rubin arrives at exactly the right moment, as AI computing demand for both training and inference is going through the roof," said Jensen Huang, Nvidia's founder and CEO. "With our annual cadence of delivering a new generation of AI supercomputers — and extreme codesign across six new chips — Rubin takes a giant leap toward the next frontier of AI."

## Six chips, one supercomputer

The pitch behind Rubin is "extreme codesign" across six new pieces of silicon engineered to work as a single machine: the Vera CPU, the Rubin GPU, the NVLink 6 Switch, the ConnectX-9 SuperNIC, the BlueField-4 DPU and the Spectrum-6 Ethernet switch. Named for the American astronomer Vera Rubin, the platform's flagship configuration is the Vera Rubin NVL72 rack, which fuses 72 Rubin GPUs and 36 Vera CPUs into one liquid-cooled, NVLink-connected system.

The numbers are built for scale. Nvidia says the platform delivers up to a 10x reduction in inference cost per token versus Blackwell, and trains mixture-of-experts models with 4x fewer GPUs. The Rubin GPU offers 50 petaflops of NVFP4 compute for inference, paired with next-generation HBM4 memory. The Vera CPU carries 88 custom Arm-based "Olympus" cores with full Armv9.2 compatibility, tuned for the agentic reasoning workloads Nvidia expects to dominate.

Interconnect is where the "factory" metaphor gets literal. Each GPU pushes 3.6 TB/s of NVLink 6 bandwidth, and a single NVL72 rack moves 260 TB/s — which Nvidia notes is more bandwidth than the entire internet. A cable-free, modular tray design allows up to 18x faster assembly and servicing than Blackwell racks, a detail that matters when operators are wiring up facilities with six-figure GPU counts.

## The cloud is already buying

Unlike a paper launch, Rubin arrived with a customer list attached. Nvidia says Rubin is in full production, with partner products shipping in the second half of 2026. Among the first cloud providers deploying Vera Rubin instances are AWS, Google Cloud, Microsoft and OCI, alongside neocloud specialists CoreWeave, Lambda, Nebius and Nscale.

Microsoft plans to build Rubin racks into its next-generation "Fairwater" AI superfactories, which the company says will scale to hundreds of thousands of Vera Rubin superchips. Oracle is leaning on the same architecture for its hyperscale buildout.

"With gigascale AI factories powered by the NVIDIA Vera Rubin architecture, OCI is giving customers the infrastructure foundation they need to push the limits of model training, inference and real-world AI impact," said Clay Magouyrk, CEO of Oracle.

The frontier AI labs are lined up too. Nvidia lists Anthropic, OpenAI, Meta, xAI, Mistral, Cohere, Perplexity and Thinking Machines Lab among those expecting to train and serve models on Rubin.

## Why it matters

The through-line of every Rubin talking point is agentic AI. Multi-step agents that reason, call tools and act over long token sequences consume compute in a fundamentally different pattern than the chatbot era — heavier on inference, hungrier for memory and bandwidth. Rubin's emphasis on cost per token, HBM4 capacity and a new BlueField-4-powered "context memory" storage tier is a bet that the next wave of AI spending is about serving agents at scale, not just training bigger models.

That bet reinforces Nvidia's most durable advantage: lock-in. By selling not a chip but an integrated, codesigned rack — compute, networking, DPUs, switches and software — Nvidia makes it harder for a hyperscaler to swap in a rival accelerator without unraveling the whole stack. Reporting around the launch also points to a token-acceleration role for Groq's low-latency LPU inference technology within Rubin-class deployments, a sign that even specialized inference silicon is being drawn into Nvidia's orbit rather than competing head-on. (Nvidia's own launch materials center the six in-house chips.)

Then there's geography. Wistron's Fort Worth plant — a roughly $700 million investment that has created more than 500 jobs, with plans to double that by year's end — is where the first Grace Blackwell superchips were mass-produced in the U.S., and where Vera Rubin superchips are slated to be built next. In a climate of tariffs, export controls and supply-chain anxiety, domestic manufacturing of the most strategically important hardware on the planet is as much a political story as a technical one.

## What to watch

Three questions loom. First, can supply keep up: Nvidia has secured large slices of partner manufacturing capacity, and whether Rubin ramps cleanly or hits the delays that dogged early Blackwell will shape the second half of 2026. Second, economics: the promised 10x cost-per-token improvement is Nvidia's number, and independent benchmarks from cloud customers will test it. Third, power. Gigascale factories imply gigawatt-scale electricity demand, and the gating factor for AI's next chapter may turn out to be the grid, not the GPU.
