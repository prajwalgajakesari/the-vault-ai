---
headline: "SambaNova, Intel, and Foxconn Unveil Rackscale AI Infrastructure for Agentic Workloads"
slug: sambanova-intel-foxconn-rackscale-ai
category: research
story_number: 12
date: 2026-06-02
authors:
  - The Vault AI
sources:
  - name: Intel Newsroom
    url: https://newsroom.intel.com/artificial-intelligence/intel-announces-new-ai-innovations-at-computex
  - name: Intel Newsroom - Client Computing
    url: https://newsroom.intel.com/client-computing/intel-at-computex-2026-the-next-era-of-ai-driven-computing
  - name: The Register
    url: https://www.theregister.com/ai-and-ml/2026/06/02/intel-and-pals-cram-36864-cpu-cores-into-a-100kw-rack-while-chasing-the-agentic-ai-dragon/5249917
  - name: SambaNova Blog
    url: https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference
  - name: Focus Taiwan (CNA)
    url: https://focustaiwan.tw/sci-tech/202606020023
---

# SambaNova, Intel, and Foxconn Unveil Rackscale AI Infrastructure for Agentic Workloads

**At Computex 2026, the trio demonstrated production-ready racks that cram up to 36,864 CPU cores alongside purpose-built AI accelerators into a single 100 kW envelope, targeting the exploding demand for enterprise inference.**

---

TAIPEI -- The AI industry's center of gravity is shifting from training to inference, and three companies just placed a massive bet on what that future looks like at rack scale.

At Computex 2026 on Monday, Intel, SambaNova Systems, and Foxconn jointly unveiled production-ready rackscale AI infrastructure that combines Intel Xeon 6 processors with SambaNova's fifth-generation SN50 Reconfigurable Dataflow Units (RDUs). The platform targets enterprise inference and agentic workloads -- the fast-growing category of AI systems that autonomously plan, reason, and execute multi-step tasks using software tools.

"Our customers are asking us to think at the system level to help them serve real agentic workloads at scale," Intel CEO Lip-Bu Tan said during his keynote address.

## The CPU Returns to Prominence

The announcement signals a fundamental rethinking of data center architecture. Where AI training demanded GPU-heavy configurations with a typical 1:8 CPU-to-GPU ratio, agentic workloads flip that equation. AI agents must coordinate tasks, retrieve information, access files, and interact with software tools -- operations that lean heavily on CPU orchestration.

"For agentic AI, the CPU orchestrates the show," said Kevork Kechichian, executive vice president and general manager of Intel's Data Center Group.

Intel revealed two reference blueprints during the keynote. Both support up to 128 processors -- either Intel's 128-core Granite Rapids Xeon 6 or the new 288-core Clearwater Forest Xeon 6+ chips -- delivering between 16,384 and 36,864 cores per rack. The systems pack up to 384 TB of DDR5 memory within a 100 kW power envelope, a figure that allows deployment in existing air-cooled data centers without costly liquid-cooling retrofits.

Intel claims a single rack of Xeon 6+ CPUs can run up to 150,000 concurrent AI agents.

## SambaNova's SN50: Purpose-Built for Agentic Inference

SambaNova CEO Rodrigo Liang joined Tan on stage to demonstrate what the company calls the world's first heterogeneous disaggregated inference architecture. The design splits workloads intelligently: compute-heavy prefill operations run on GPUs, while bandwidth-intensive decode operations route to SambaNova's SN50 RDUs, boosting per-user token output by two to three times compared to standalone GPU systems.

The SN50, SambaNova's fifth-generation chip, claims striking performance advantages. Against Nvidia's Blackwell B200 GPUs, the company says the SN50 delivers five times the maximum generation speed and over three times the throughput for agentic inference on models like Meta's Llama 3.3 70B. The SambaRack SN50 system combines 16 SN50 chips and averages just 20 kW of power while operating air-cooled.

The chip's three-tiered memory architecture -- large-capacity memory, high-bandwidth memory (HBM), and ultra-fast SRAM -- enables millisecond-speed model hot-swapping, a critical capability for agentic workloads that frequently switch between multiple models within a single task chain. SambaNova says the SN50 can support individual models up to 10 trillion parameters and context lengths of up to 10 million tokens.

SN50-based systems will begin shipping to customers in the second half of 2026, with SoftBank's Japanese data centers confirmed as the first deployment.

## Foxconn's Role: Integration and a CPU-Dense Variant

Foxconn brings manufacturing scale and system integration expertise to the partnership. Beyond assembling the hybrid RDU-plus-Xeon racks, the company plans to manufacture a CPU-dense variant of the infrastructure for workloads that do not require dedicated AI acceleration -- including cost-optimized inference, data processing, and hybrid AI applications.

This CPU-only option addresses a pragmatic reality: not every enterprise inference workload justifies the cost of specialized accelerators. For lighter models, retrieval-augmented generation pipelines, and orchestration-heavy agent frameworks, dense CPU configurations may offer superior economics.

## Competitive Context

The announcement lands in an increasingly crowded rackscale AI arena. Nvidia unveiled a similar CPU-dense platform at GTC in March, packing 256 of its 88-core Vera CPUs into a single liquid-cooled rack. Arm is developing its own reference designs based on new AGI CPUs, ranging from an air-cooled 8,160-core system at 36 kW to a 200 kW liquid-cooled rack with 45,696 cores.

The first commercial customer for the Intel-SambaNova disaggregated architecture is Together.AI, while newly launched inference cloud provider Vector Core Compute -- backed by Vista Equity Partners -- will be among the earliest large-scale deployments.

## What It Means

The rackscale AI infrastructure unveiled at Computex 2026 represents more than a product launch -- it is an architectural thesis. As AI evolves from monolithic model serving toward orchestrated multi-agent systems, the industry is rediscovering that CPUs, accelerators, and memory hierarchies must be co-designed at the system level rather than bolted together as afterthoughts.

For enterprises evaluating inference infrastructure, the message is clear: the agentic era demands a new balance of compute, and the companies that nail rack-level integration will capture the next wave of data center spending.
