## An IP-first bet against the compute incumbents

The wave of AI money flowing into infrastructure in July 2026 found one of its most pointed targets in a Campbell, California, startup that wants to sell the blueprints for AI chips rather than the chips themselves. On July 1, Oxmiq Labs Inc. said it had closed a $35 million Series A financing, bringing total capital raised to $60 million and putting the company squarely into the most consequential question in tech hardware: who, besides Nvidia, gets to power the AI buildout.

Oxmiq is led by Raja Koduri, one of the industry's best-known GPU architects, who previously served as chief architect and executive vice president of Intel's architecture, graphics and software division and earlier helped shape AMD's Radeon line. His pitch is explicitly modeled on Arm Holdings. Rather than fabricate a full system-on-chip, Oxmiq licenses architecture and IP that other companies can drop into their own custom silicon. "We would want to be the Arm of this next era," Koduri told Reuters.

## What the money buys

The round was co-led by Fundomo, a New York firm focused on frontier compute infrastructure, and Samsung Catalyst Fund, with participation from MediaTek, AM Intelligence Labs, Pegatron Venture Capital, CDIB-TEN, Darwin Ventures and Morgan Creek Digital. According to the company, Intel Capital also participated as a strategic IP partner. Notably, several backers sit deep in the semiconductor supply chain, exactly the customers Oxmiq hopes to license to.

The funds will scale OxCore, Oxmiq's licensable GPU architecture. Its central claim is consolidation: OxCore folds three components that are normally split across separate chips, a CUDA-compatible GPU engine, a tensor processing engine and an orchestration CPU, into a single, near-memory core designed to cut data movement and improve energy efficiency. The company says OxCore is running on FPGA today with live demonstrations. A companion chiplet-integration layer called OxQuilt is meant to let designers mix process nodes, memory types and packaging rather than locking to one foundry, and a software stack, including OxPython, aims to run existing CUDA and PyTorch code without modification.

That last point is the crux of the strategy. Nvidia's durable advantage is less about raw silicon than about CUDA, the software ecosystem that has trapped a generation of developers. By promising portability of existing CUDA code onto non-Nvidia hardware, Oxmiq is attacking the moat rather than the chip.

The company also strengthened its board. Jim Keller, the CEO of Tenstorrent and one of the industry's most influential chip architects, joined as a director, and retired Intel process-technology Fellow Valluri (Bob) Rao came on as an advisor. "Raja and this team are creating an open GPU architecture, a much-needed step toward removing the artificial boundaries around AI innovation," Keller said in the company's announcement.

## A crowded field of Nvidia challengers

Oxmiq enters a field already thick with well-capitalized companies chasing the same target from different angles. AMD remains the most credible full-stack GPU rival, pushing its Instinct accelerators and the open ROCm software stack. Cerebras builds wafer-scale chips aimed at large-model training and inference. Groq bets on deterministic inference performance with its LPU design. And Koduri's own new board member runs Tenstorrent, which, like Oxmiq, embraces open standards and RISC-V and licenses IP alongside building silicon.

What sets Oxmiq apart is the capital-light, IP-first model. Koduri has said a cutting-edge AI chip typically costs hundreds of millions of dollars and years to develop; by selling architecture blocks, Oxmiq generates revenue from customer engagements while conserving cash. That positions it less against Nvidia's data-center GPUs directly and more against custom-silicon enablers such as Broadcom, Marvell and MediaTek, the firms that help Google, Amazon and OpenAI design their own chips. Koduri has named those companies as the eventual competitive set.

The framing is also political. Oxmiq casts its open architecture as a way to widen who can afford to build AI, noting that state-of-the-art AI reaches most people through a handful of channels because the underlying compute is so expensive. That message dovetails with a real market anxiety: hyperscalers and sovereign-AI projects increasingly want alternatives to a single dominant supplier.

## What to watch

The hard questions are ahead of the funding. OxCore runs on FPGA and in demos today, not in volume production, and $35 million is modest against the scale of the problem, and against Nvidia's multi-billion-dollar R&D machine. The signals to track: whether Oxmiq converts strategic investors like MediaTek and Pegatron into actual licensees; whether OxPython's CUDA compatibility holds up on real workloads rather than curated demonstrations; and whether the company can ship its first IP as a product on the timeline Koduri has promised. If the Arm-for-AI thesis works, Oxmiq will not need to beat Nvidia on silicon, only to make everyone else's silicon cheaper to build.
