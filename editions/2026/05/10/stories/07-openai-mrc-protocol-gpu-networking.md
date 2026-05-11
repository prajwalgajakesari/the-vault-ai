---
headline: "OpenAI Partners With NVIDIA, AMD, Intel, and Broadcom on MRC Protocol to Fix AI Supercomputer Networking Bottlenecks"
slug: openai-mrc-protocol-gpu-networking
category: llms-genai
story_number: "07"
date: 2026-05-10
author: The Vault AI
tags: [openai, nvidia, amd, intel, broadcom, microsoft, MRC, networking, AI-infrastructure, supercomputers, open-compute-project, ethernet]
---

# OpenAI Partners With NVIDIA, AMD, Intel, and Broadcom on MRC Protocol to Fix AI Supercomputer Networking Bottlenecks

OpenAI and five of the largest names in computing hardware have released Multipath Reliable Connection, or MRC, an open networking protocol designed to eliminate one of the most stubborn obstacles in scaling artificial intelligence: keeping hundreds of thousands of GPUs synchronized across a data center without losing performance to network congestion, link failures, or routine maintenance.

Announced on May 6, MRC was developed jointly by OpenAI, NVIDIA, AMD, Intel, Microsoft, and Broadcom. The specification has been contributed to the Open Compute Project so that any hardware vendor, cloud provider, or enterprise operator can adopt it without licensing restrictions. It is already running in production across some of the largest AI training clusters in existence.

## The Problem MRC Was Built to Solve

Training a frontier AI model requires massive GPU clusters to operate in near-perfect lockstep. Every chip must exchange gradients and activations with its neighbors thousands of times per second. When a single network link flaps or a switch fails, traditional single-path RDMA connections can suffer throughput drops of 30 percent or more, stalling an entire training run and wasting millions of dollars in idle compute.

The challenge intensifies as clusters grow. OpenAI now operates supercomputers housing NVIDIA GB200 Blackwell GPUs across facilities including Oracle Cloud Infrastructure in Abilene, Texas, and Microsoft Azure Fairwater supercomputers. At that scale, network disruptions are not rare events but statistical certainties that occur multiple times per day.

## How MRC Works

MRC replaces the conventional single-path approach with a multipath architecture baked directly into the latest 800-gigabit-per-second network interfaces. Instead of routing each connection through one path, MRC splits traffic across hundreds of paths simultaneously. If one path becomes congested or a link goes down, packets already in flight continue arriving via alternative routes.

The protocol treats a single 800 Gb/s network interface not as one fat pipe but as multiple smaller links. One interface can connect to eight different switches, creating eight separate parallel network planes, each operating at 100 Gb/s. This architecture provides built-in redundancy and makes the network fundamentally more resilient than traditional designs.

When failures do occur, MRC detects them at hardware speed and reroutes traffic on a microsecond timescale, orders of magnitude faster than the seconds or minutes that conventional recovery mechanisms require. The result is that training workloads can continue making progress without measurable disruption during many common failure scenarios.

## Industry Alignment and Key Contributions

The breadth of the partnership is notable. NVIDIA contributed its Spectrum-X Ethernet fabric, which was purpose-built for AI workloads and now ships with native MRC support. AMD co-led authorship of the specification and contributed advanced congestion control technology, deploying MRC on its Pensando Pollara 400 AI network interface card, making it one of the first companies to validate the protocol on a 400G NIC. AMD has signaled that MRC support will carry forward to its next-generation Pensando Vulcano 800G AI NIC.

Krishna Doddapaneni, Corporate Vice President of Engineering at AMD, framed the significance in infrastructure terms. "As GPUs and CPUs continue to drive compute, the real bottleneck in scaling AI is the network," he said. "AMD programmability enables us to rapidly turn innovations like this into real-world performance at scale, where consistent, resilient throughput matters more than theoretical peak bandwidth."

Intel and Broadcom round out the consortium, ensuring that MRC interoperates across the full range of data center silicon. Microsoft, which operates some of the largest AI training environments in the world, has been both a co-developer and an early deployer, running MRC inside its Fairwater supercomputer infrastructure.

## What the Numbers Show

OpenAI reports that MRC maintains training progress without measurable disruption in many cases during link-flap events, compared to the roughly 30 percent slowdown that single-path RDMA can suffer under network congestion. By spreading load across hundreds of paths, MRC also reduces congestion hotspots in the network core, limiting the latency variation that slows synchronized training across large GPU clusters.

The protocol has already been used to train multiple OpenAI frontier models. Deployment spans OpenAI clusters with NVIDIA GB200 Blackwell GPUs at Oracle Cloud Infrastructure in Abilene, Texas, and at Microsoft Fairwater facilities, representing some of the largest AI supercomputers ever constructed.

## Why Open Sourcing Matters

Contributing MRC to the Open Compute Project is a strategic move. By making the specification freely available, OpenAI and its partners are betting that a shared standard will accelerate adoption and prevent the fragmentation that plagued earlier high-performance networking technologies. Cloud providers, sovereign AI initiatives, and enterprise data center operators can all implement MRC without waiting for a single vendor to ship a proprietary solution.

The open approach also reflects a broader industry recognition that AI infrastructure has become too complex and too expensive for any single company to optimize alone. As AMD noted in its announcement, MRC represents a shift toward making AI networking an open, programmable, and production-ready foundation rather than a proprietary differentiator.

## What to Watch Next

The immediate question is how quickly MRC adoption spreads beyond the founding partners. NVIDIA Spectrum-X switches and AMD Pensando NICs already support the protocol, but the timeline for Intel and Broadcom product integration will determine whether MRC becomes a true industry standard or remains concentrated among a handful of hyperscalers. Enterprise buyers planning their next generation of AI clusters will also be watching to see whether MRC delivers its promised resilience benefits outside the controlled environments of OpenAI and Microsoft, where the protocol was first proven. If it does, MRC could quietly become the networking layer that makes the next leap in AI model scale economically viable.
