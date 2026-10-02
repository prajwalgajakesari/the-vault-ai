AMD wants the next enterprise AI agent to run under a desk instead of in a data center. Systems built on its Ryzen AI Max PRO 400 Series processors, codenamed "Gorgon Halo," are now shipping from partners. The flagship chip can address up to 192GB of unified memory, and AMD says it is the first x86 client processor able to hold a model of more than 300 billion parameters entirely on the machine.

The pitch is aimed at IT departments. As companies move from chatbots to agents that plan, call tools and revise their own work, AMD argues a well-equipped laptop or compact workstation can absorb much of that load, keeping proprietary data on the device and cutting cloud inference bills.

## What the silicon actually offers

The lineup has three chips, all built on "Zen 5" CPU cores, RDNA 3.5 integrated graphics and an XDNA 2 neural processing unit. The top part, the Ryzen AI Max+ PRO 495, has 16 cores and 32 threads, boosts to 5.2GHz, carries 80MB of cache, and pairs a 40-compute-unit Radeon 8065S GPU with an NPU rated at up to 55 TOPS. The Ryzen AI Max PRO 490 (12 cores) and 485 (8 cores) drop to a 32-CU Radeon 8050S and a 50 TOPS NPU. All three support 192GB of unified memory and a configurable power envelope of 45 to 120 watts, according to AMD's specification table.

The big change is memory. The previous Ryzen AI Max 300 "Strix Halo" generation topped out at 128GB of total memory, with up to 96GB available to the GPU. The 400 Series raises that to 192GB, with up to 160GB dedicated to graphics, which AMD describes as a 1.67x increase. In its footnotes, AMD says that 160GB of graphics memory on the Max+ PRO 495 is "capable of running 300 billion+ parameters at 4-bit quantization." For comparison, the company's first-generation Ryzen AI Halo developer box, built on the 128GB Ryzen AI Max+ 395, is rated for models of up to 200 billion parameters.

Tom's Hardware was less impressed by the rest of the chip. Its CPU analyst Jake Roach called the series "a minor refresh," noting that apart from a 100MHz clock bump on the flagship, the specs match the 300 Series. He also pointed out that AMD's "first x86" claim "wins in a category of one," because Intel does not make a comparable large SoC and Apple's unified-memory chips use Arm.

## The agentic argument

AMD's case rests less on raw TOPS than on how agents behave. In a blog post published this week, AMD's David Diederichs wrote that agentic workloads "may combine multiple models, large context windows, enterprise data, and several applications or tools within the same workflow," and that this puts heavy demands on memory.
AMD also leans on a familiar enterprise argument: control over sensitive data. The company writes that an agent working on internal documents, engineering files or source code can handle suitable operations locally "instead of sending every request and working document to an external inference service." The stack supports Windows and Linux, plus PyTorch, vLLM, llama.cpp, Ollama and LM Studio.

AMD is not pitching this as local-only. HP's ZBook Ultra G3a 16 pairs the Max+ PRO 495 with Perplexity's agent software, calling a frontier cloud model only when a step requires it.

"AI is no longer confined to the cloud. It is now something developers can build, train, and run locally," said Jack Huynh, senior vice president and general manager of AMD's Computing and Graphics Group, when the chips were unveiled in May.

Lenovo framed it in similar terms. "AI is moving from the cloud to where work actually happens: on the device, in real time," said Luca Rossi, president of Lenovo's Intelligent Devices Group.

## The tokenomics pitch

The sharpest part of AMD's marketing is financial: agents reason, retrieve and re-invoke models repeatedly, burning far more tokens than chatbots. Its new Tokenomics Calculator models cloud-only, local-only and hybrid deployments. In one published scenario, AMD compared a local Ryzen AI Max+ system with Claude Sonnet 4.5 API pricing ($3 per million input tokens, $15 per million output). The scenario assumed roughly 6.3 million tokens per day, and AMD projected that the local hardware breaks even within about six months.

The fine print matters. The throughput behind that scenario, 36 output tokens per second at a 128K context, was measured on a pre-production Ryzen AI Halo developer platform. It reflects a single-user workload, not a shared server. Earlier, Tom's Hardware reported AMD's claim that a Halo box could save "up to $750 each month" compared with cloud compute.

## Why It Matters

Enterprise inference is starting to split. Frontier-scale reasoning will stay in the cloud, but much agentic work, such as summarizing internal files or running retrieval over codebases, is repetitive, sensitive and token-hungry, which suits local hardware. With 160GB of GPU-addressable memory, a laptop-class chip can now run open-weight models that recently required a multi-GPU server, at least at 4-bit precision.

For CIOs, the appeal is a clearer story on data residency and a cost that stops growing with every agent loop. The caveats are real, though. Integrated RDNA 3.5 graphics are far slower than discrete data-center accelerators. A 300-billion-parameter model fitting in memory does not mean it runs fast enough for interactive use. And 192GB configurations arrive during a global DRAM shortage: one early Gorgon Halo mini-PC listed at $7,099, according to Tom's Hardware.

## What to Watch

Independent benchmarks will be the real test. Watch for tokens-per-second figures on 100B-plus mixture-of-experts models at long context lengths, not just whether they load. The other things to track are how HP and Lenovo price their 192GB configurations as memory costs stay high, and whether Nvidia's DGX Spark-class machines and Apple's next Mac Studio force AMD to answer on GPU throughput rather than capacity alone. If enterprises begin routing routine agent work to the desk and reserving cloud APIs for frontier reasoning, the economics of AI inference could shift.
