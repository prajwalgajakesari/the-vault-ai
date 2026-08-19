When a language model hallucinates in a chat window, a user rolls their eyes. When a perception model misfires inside a warehouse robot or a car at highway speed, the failure has mass and momentum. That gap — between software that is merely wrong and software that is physically dangerous — is what an open-source hypervisor project moved to formalize this week.

On August 17, the Xen Project, the open-source virtualization platform hosted by the Linux Foundation, announced the **Xen Safety Committee**: a standing body chartered to produce and maintain the requirements documents, architecture specifications, test evidence, and process paperwork companies need to certify products under functional-safety standards such as **IEC 61508** and, in automotive, **ISO 26262**. AMD, EPAM, and Renesas are founding contributors. And as The Register first reported on August 18, **Boeing has joined the project** — with its interest in this safety work understood to be a reason why.

Xen spent two decades as cloud plumbing. Its member roster now reads very differently: AMD, Arm, AWS, Boeing, EPAM, Ford, Honda, Renesas, Vates, and XenServer — chipmakers, a cloud provider, two automakers, and an aerospace prime.

“Safety engineering has traditionally required every organization to recreate much of the same foundational work. We believe open source can change that,” said **Cody Zuschlag**, community manager at the Xen Project. “By maintaining shared engineering evidence alongside the software itself, the Xen community can reduce duplicated effort, accelerate certification programs, and make functional safety more practical for industries building the next generation of software-defined systems.”

## What a hypervisor does when the AI stack falls over

A hypervisor is a thin slab of code sitting directly on the silicon, beneath every operating system on the machine. Xen is Type-1, meaning nothing sits between it and the hardware. Its job is to carve one physical computer into isolated compartments — domains — and police the walls between them.

In an embedded or robotic system, that partitioning is the whole point. On one side of the wall runs a Linux guest carrying the messy, fast-moving, hard-to-verify parts of a modern machine: neural network inference, camera and lidar processing, navigation, over-the-air update agents, a touchscreen interface. On the other runs a real-time OS such as Zephyr handling what must never miss a deadline — motor control, braking, collision avoidance, flight surface actuation.

Xen assigns each side its own CPU cores, memory regions, interrupts, and physical devices, in a configuration the project calls **static partitioning**. The goal is what safety engineers call freedom from interference: a perception model that deadlocks, leaks memory, saturates a core, or is compromised outright cannot starve, corrupt, or stall the control loop next door. Supporting mechanisms include CPU pinning, device passthrough, deterministic interrupt latencies, and **Dom0less boot**, which lets safety-critical domains start at power-on without waiting for a conventional control domain.

The driver is consolidation: carmakers want fewer electronic control units, aerospace integrators fewer line-replaceable units. Squeezing infotainment and collision avoidance onto one system-on-chip only works if the boundary is trustworthy enough to show an auditor.

Which is where the paperwork comes in, and the paperwork is enormous. The founding contributors have already built safety requirements, architecture specifications, MISRA C engineering, DFMEA analysis, testing frameworks, tooling, code coverage, and process documentation — the committee’s starting corpus. Static analysis runs through BUGSENG’s ECLAIR platform. The project also extended its release support lifecycle in 2026 to **five years** — three of regular support plus two of security-only coverage — aimed squarely at industries whose certification timelines outlast a typical open-source support window.

The aerospace angle predates the announcement. At an ELISA Project seminar on May 13, Boeing’s **Matthew Weber** appeared alongside AMD’s **Ayan Kumar Halder** to walk through composing Xen, Zephyr, and Linux into a mixed-criticality architecture, mapping the avionics standards **DO-178C** and **ARINC 653** onto work already underway for ISO 26262. ARINC 653 is, in effect, aviation’s decades-old formalization of this idea: time and space partitioning on shared hardware.

“Achieving baseline functional safety certification for Xen is a critical milestone, but it represents just the beginning of a continuous journey,” said **Artem Mygaiev**, technology solutions director at EPAM. “As the hypervisor evolves and its footprint in mission-critical applications expands, the approach to safety must evolve alongside.”

## Why this matters for physical AI

The AI industry’s safety conversation is overwhelmingly about model behavior — evals, alignment, guardrails, refusals. This is a different and older discipline arriving at the same door. Functional safety does not ask whether a model is correct. It assumes the model will eventually be wrong, and asks what the surrounding architecture does about it.

That assumption is load-bearing as AI moves into things that move. You cannot certify a vision transformer to ASIL D. You can, plausibly, certify the partition it runs inside and the supervisory logic that overrides it. Containment becomes the safety story precisely because verification of the model is out of reach.

There is an economic argument too. Certification is a fixed cost every robotics and automotive supplier currently pays alone, and it is neither cheap nor fast. Pooling the evidence attempts to make certifiable infrastructure a commons rather than a moat. The chipmakers underwriting it are not being altruistic: a certifiable open hypervisor makes AMD and Renesas silicon far easier to design into a robot or a vehicle.

One caveat matters. The Xen Project says plainly that its source code is not itself safety certified, and that a product safety case still depends on the complete system and assessor review. The committee produces inputs, not a certificate.

## What to watch

Three things. Whether Boeing converts membership into the new **Premier Plus** tier, which buys voting seats on the Advisory Board and the Safety Committee. Whether the committee’s artifacts clear an independent assessor on a shipping product, rather than sitting as well-intentioned documentation. And whether robotics firms — the constituency Xen members reportedly believe needs isolation next — show up, or keep building bespoke isolation in-house. Xen Summit 2026 is where answers should start surfacing.
