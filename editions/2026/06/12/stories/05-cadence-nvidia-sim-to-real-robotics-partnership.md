## Cadence and Nvidia Expand Their Alliance to Close Robotics' Stubborn "Sim-to-Real" Gap

Every robotics engineer knows the ritual humiliation: a robot that navigates flawlessly in simulation promptly stumbles, drops objects, or freezes in place the moment it meets the physical world. This "sim-to-real" gap has been one of the most expensive and frustrating bottlenecks in the race to deploy physical AI systems at scale. Now two of the industry's most powerful simulation and computing companies are betting that the fix lies in making the virtual world far harder to fool.

At CadenceLIVE Silicon Valley 2026, Cadence Design Systems and NVIDIA announced an expanded partnership that brings together Cadence's high-fidelity multiphysics simulation engines and NVIDIA's Isaac robotics libraries and Cosmos open-world foundation models. The goal is straightforward: generate synthetic training data so physically accurate that robots trained in simulation actually perform when placed in the real world.

## What the Joint Stack Does

The technical architecture spans the full robotics development lifecycle. On the NVIDIA side, the collaboration draws on Isaac Sim and Isaac Lab for virtual robot training, plus Cosmos open-world models for generating large-scale, varied scenario data. Cadence contributes its multiphysics simulation engines — software long used in aerospace, automotive, and semiconductor design to model how real materials deform, how fluids flow, how surfaces make contact — along with VTD (Virtual Test Drive) and the extended VTDx environment for mission-scale scenario testing.

AI agents coordinate the entire workflow, running from world-model training and physics surrogate training through policy optimization, validation, and deployment feedback. Trained models are then pushed to NVIDIA Jetson robotics and edge AI hardware, where a live virtual twin continues to monitor real-world performance and feed results back into the training loop.

The approach addresses the core physics problem in robot learning. Most simulation environments approximate physical interactions well enough to train basic behaviors but introduce small inaccuracies — friction coefficients, contact dynamics, material compliance — that compound into large behavioral errors once a robot operates in the real world. Cadence's principled solvers are designed to close that accuracy gap.

"The more accurate the generated training data is, the better the model will be," said Anirudh Devgan, president and CEO of Cadence, speaking at the Santa Clara conference.

NVIDIA CEO Jensen Huang made clear the scope of the collaboration: "We're working with you across the board on robotic systems."

## Why Sim-to-Real Is the Critical Bottleneck

The sim-to-real gap is not a new problem, but it has become the central obstacle as physical AI ambitions have grown. Companies racing to deploy humanoid robots, autonomous vehicles, and industrial automation systems have discovered that real-world data collection is prohibitively expensive and slow. A robot that needs thousands of hours of physical operation to learn a manipulation task is commercially unviable; one that can acquire those skills in simulation — and transfer them reliably — is not.

Physical AI faces a harder version of the same challenge as language models trained on synthetic text: generating data that respects the constraints of Newtonian physics, material science, and real sensor noise. The quality of that synthetic physical data is now a competitive differentiator for anyone building robots, autonomous systems, or manufacturing automation.

Cadence's expanded footprint into AI training pipelines reflects a recognition that simulation software is no longer merely an engineering verification tool — it is infrastructure for the physical-AI supply chain.

## The Broader Collaboration

The robotics piece is one pillar of a wider alliance unveiled at CadenceLIVE. The expanded partnership also covers accelerated semiconductor and system design — Cadence's core EDA business — and AI factory digital twins.

On chip design, Cadence unveiled AgentStack, a head agent designed to orchestrate all aspects of semiconductor and system design using NVIDIA Nemotron models running on NVIDIA accelerated computing. Early deployments at more than ten leading customers have demonstrated up to a 10x productivity boost in design and verification tasks.

On AI factories, the collaboration integrates the NVIDIA Omniverse DSX Blueprint to enable digital twins of large-scale AI infrastructure. In a joint 10-megawatt AI factory use case, modeling GPU operation at reduced power (MaxQ) demonstrated up to 17% more tokens per watt — a metric the companies are positioning as the key efficiency benchmark for hyperscale AI deployments.

"Agentic AI and digital twins are reshaping the entire engineering landscape — from semiconductor design to planetary-scale AI systems," Devgan said in the official announcement. "Our expanded collaboration with NVIDIA accelerates the convergence of design and physical realization."

NVIDIA's Jensen Huang framed the broader significance: "For the first time, we can innovate in the digital world — exploring, testing, and optimizing ideas at unprecedented speed and scale — by building everything as full-fidelity digital twins first."

## What to Watch Next

The partnership's immediate commercial test will be adoption among industrial robotics customers. Cadence listed Honda R&D, Samsung, and Argonne National Laboratory among organizations already using accelerated Cadence solutions; the question is whether the sim-to-real workflow attracts the humanoid and mobile manipulation companies now burning capital on physical training data collection.

NVIDIA has separately been building similar simulation bridges with Siemens and Dassault Systemes, suggesting a broader industry push to standardize physics-accurate synthetic data pipelines as foundational infrastructure. For Cadence, the robotics expansion represents a meaningful revenue diversification away from EDA licensing — and a bet that the world's most precise physics solvers are about to become as strategically important as the chips they were originally designed to verify.

Watch for customer case studies from automotive and industrial robotics partners in the second half of 2026, and whether Cadence's VTDx simulation environment begins appearing in humanoid robot training stacks alongside NVIDIA's Isaac ecosystem.
