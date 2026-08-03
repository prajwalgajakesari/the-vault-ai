Nvidia has spent the better part of a decade convincing the world that the GPU is the beating heart of the AI data center. Now it wants the same customers to buy its CPUs, too.

On July 21, Nvidia released detailed specifications and performance benchmarks for Vera, its next-generation data-center processor and the successor to the Grace CPU. The disclosures give prospective buyers the numbers they need to evaluate the chip in earnest, and they sharpen a challenge that has been building for months: Nvidia intends to compete directly with AMD and Intel for the server CPU socket, a market those two companies have effectively split between them for a generation.

Vera is not a hedge. It is the CPU half of the Vera Rubin platform, pairing Nvidia's custom Arm-based processor with its forthcoming Rubin GPUs. And it has already left the lab. In mid-May, Nvidia hand-delivered the first Vera systems to Anthropic, OpenAI, SpaceX's xAI unit and Oracle Cloud Infrastructure, moving the chip, in the company's words, "from announcement to production."

## What's inside Vera

The headline change is that Nvidia is now designing its own CPU cores rather than licensing off-the-shelf ones. Grace relied on standard Arm Neoverse cores; Vera is built around 88 custom cores, code-named Olympus, that Nvidia designed itself on the Arm instruction set. According to Nvidia's own figures, the chip delivers 1.2 terabytes per second of memory bandwidth — more than double Grace — and roughly 50% faster per-core performance under sustained load.

That last emphasis is deliberate and marks a philosophical break from x86 rivals. Where AMD and Intel have competed largely on core count, packing ever more cores onto a package, Nvidia is prioritizing single-core speed and the ability to keep those cores fed under constant, concurrent load. The company frames this around "agentic" AI — workloads where models don't just answer questions but call tools, run code, orchestrate tasks and manage long-context state, all of which lean heavily on the CPU rather than the GPU.

"Agentic AI is creating a new CPU moment in the AI factory," said Ian Buck, Nvidia's vice president of hyperscale and high-performance computing, who personally delivered the first units. "As models move from answering to acting, Vera is purpose-built to keep that work moving at scale."

Buck offered a concrete example: when an AI model is asked a question, "the models actually have to generate some Python code to arrive at the correct answer" — CPU work, not GPU work. "That's why we are seeing the demand for CPUs skyrocket," he said.

## The full-stack play

Vera's strategic value is clearest inside the Vera Rubin NVL72, the rack-scale system Nvidia unveiled at CES in January and expects to ship in the second half of 2026. That rack combines 72 Rubin GPUs with 36 Vera CPUs, with each Vera linked to a pair of Rubin GPUs over second-generation NVLink-C2C, an interconnect Nvidia says delivers 1.8 TB/s of chip-to-chip bandwidth — double the prior generation and far faster than PCIe. At the rack level, Nvidia cites 260 TB/s of scale-up NVLink bandwidth and describes a unified memory architecture between Vera and Rubin meant to keep the expensive GPUs saturated with data.

This is the crux of why Nvidia's push into CPUs matters. By owning the CPU, the GPU, the NVLink fabric, the BlueField DPU and the rack architecture, Nvidia can co-design the entire system and, in the process, deepen customer lock-in. A Vera CPU tuned to feed Rubin GPUs is a harder component for a buyer to swap out for an AMD EPYC or Intel Xeon part. Nvidia claims the arrangement feeds GPUs at twice the energy efficiency of conventional infrastructure — a vendor figure that independent testing has yet to confirm.

The early customer roster underscores the stakes. James Bradbury, Anthropic's head of compute, called Vera "a promising part of the ecosystem when solving for agentic workloads." xAI is evaluating the chip for reinforcement-learning and simulation pipelines. Most striking, Oracle said it plans to deploy "hundreds of thousands" of Vera CPUs beginning in 2026, making OCI the first cloud provider to field the processor at hyperscale.

For AMD and Intel, that is an unwelcome signal. The data-center CPU has been one of the few large, stable, high-margin markets left in semiconductors, and Nvidia — already the most valuable chip company in the world — is now aiming an Arm-based, AI-optimized alternative squarely at it. Jensen Huang, who introduced the standalone Vera at Nvidia's GTC conference in March, has described it as the company's next multibillion-dollar business.

## What to watch

The specifications are now public, but the benchmarks that count most remain vendor-supplied. Watch for independent performance and total-cost-of-ownership comparisons against AMD's and Intel's latest server parts once Vera Rubin systems ship in volume in the second half of 2026. Watch, too, whether marquee evaluators like Anthropic, OpenAI and xAI convert their early units into large production orders — and whether Oracle's "hundreds of thousands" commitment is matched by other hyperscalers such as Microsoft, Google and Amazon, all of which are also building their own custom Arm CPUs. If Vera lands, Nvidia won't just sell the accelerators inside the AI factory. It will sell the whole building.
