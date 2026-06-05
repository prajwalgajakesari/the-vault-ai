---
headline: "Nvidia and Unitree Unveil Open Humanoid Robot Reference Design, Handing University Labs a Full-Stack Research Platform"
slug: nvidia-unitree-h2-humanoid-reference-design
category: research
story_number: 13
date: 2026-06-04
author: The Vault AI Edition
sources:
  - name: NVIDIA Newsroom
    url: https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
  - name: CNBC
    url: https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html
  - name: Interesting Engineering
    url: https://interestingengineering.com/ai-robotics/nvidias-new-humanoid-robot-platform
  - name: Tech Times
    url: https://www.techtimes.com/articles/317681/20260603/nvidia-isaac-gr00t-reference-robot-brings-full-stack-humanoid-platform-university-labs.htm
  - name: Glitchwire
    url: https://glitchwire.com/news/nvidia-unveils-first-open-humanoid-robot-reference-design-signaling-a-broader-ed/
  - name: PR Newswire (Unitree)
    url: https://www.prnewswire.com/news-releases/unitree-announces-h2-plus-an-nvidia-isaac-gr00t-reference-humanoid-robot-for-academic-research-302786748.html
---

# Nvidia and Unitree Unveil Open Humanoid Robot Reference Design, Handing University Labs a Full-Stack Research Platform

For years, frontier humanoid robotics research has been bottlenecked not by ideas but by infrastructure. University labs wanting to push the boundaries of physical AI had to stitch together hardware from one vendor, simulation software from another, and training pipelines from a third -- often spending months on integration before running a single experiment. At GTC Taipei on June 1, Nvidia moved to collapse that entire process into a single box.

The company announced the Nvidia Isaac GR00T Reference Humanoid Robot, the first open humanoid robot reference design built on Nvidia Jetson Thor silicon and the Isaac GR00T open development platform. The system pairs a Unitree H2 Plus chassis with Sharpa Wave tactile five-finger hands and Nvidia's complete simulation-to-deployment software stack, creating what amounts to a turnkey starting point for academic humanoid research.

"Humanoid robots will bring physical AI to the world's largest industries, opening a multitrillion-dollar economic opportunity," said Jensen Huang, founder and CEO of Nvidia, during the keynote. "The Nvidia Isaac GR00T Reference Humanoid Robot gives researchers a single, open platform to make breakthrough discoveries toward general-purpose physical intelligence."

## What is in the box

The hardware profile is substantial. The Unitree H2 Plus chassis stands nearly six feet tall, weighs 150 pounds, and delivers 31 degrees of freedom across the body. Bolted to the arms are dual Sharpa Wave tactile five-finger hands, each contributing 22 degrees of freedom and bringing the total system to 75 DOF -- enough articulation to attempt the kind of dexterous manipulation tasks, from tool use to component assembly, that remain open problems in robotics. Each fingertip carries a high-resolution Digital Tactile Array with more than 1,000 tactile pixels and pressure sensitivity down to 0.02 newtons.

The onboard brain is an Nvidia Jetson AGX Thor T5000 module built on the Blackwell architecture. It delivers 2,070 FP4 teraflops of AI performance alongside a 14-core Arm CPU and 128 GB of unified memory, all operating within a configurable 40-to-130-watt power envelope. Nvidia claims this provides 7.5 times the AI compute and 3.5 times the energy efficiency of its predecessor, Jetson Orin. A 15 Ah battery provides roughly three hours of operation, and an on-remote emergency stop lets researchers halt the robot instantly -- essential when prototyping novel behaviors on a six-foot machine.

Sensing includes a head-mounted stereo camera with a 140-degree horizontal field of view, wrist cameras for close-range manipulation, and an inertia measurement unit for motion tracking. Connectivity spans Wi-Fi 6, Bluetooth 5.2, Ethernet, USB, and an array of microphones and speakers for voice interaction.

## The software matters more than the metal

The more consequential part of the announcement may be the software. The Isaac GR00T development platform integrates capabilities that research teams typically assemble and maintain independently: Isaac Teleop for capturing high-quality demonstration data from human operators; Isaac GR00T open foundation models, licensed under Apache 2.0, for humanoid reasoning and multitask behavior; Isaac Sim and Isaac Lab for simulating and evaluating robot policies before physical deployment; accelerated Isaac ROS middleware for moving trained policies onto robot hardware; and the Jetson Thor runtime for on-device inference.

Critically, researchers retain full control of their own robot data, training data, telemetry, and logs. The platform is modular -- teams can adopt the full stack or plug selected components into existing pipelines.

## Top-tier labs are already on board

Stanford, ETH Zurich, the Allen Institute for AI, UC San Diego's Advanced Robotics and Controls Laboratory, and Nvidia Research itself have all committed to the reference design.

"Robotics moves fastest when researchers can build on open platforms, share code and test ideas on real machines," said Steve Cousins, executive director of the Stanford Robotics Center. "The Nvidia Isaac GR00T Reference Robot gives our students and collaborators an open humanoid reference design with dexterous hands, onboard AI compute and the Nvidia Isaac GR00T development platform for creating, comparing and sharing robot behaviors on physical hardware."

Marco Hutter, professor at ETH Zurich's Robotic Systems Lab, said the platform's value lies in collecting data, testing algorithms, and validating behaviors on a state-of-the-art humanoid body. Dieter Fox, senior research director at Ai2, emphasized that open technology is central to the institute's mission of broadly competent robotics through open science.

## Edge compute, not cloud dependency

The design reflects a broader industry shift. A humanoid robot cannot wait for a remote server to decide whether to catch itself during a fall -- the response window is measured in milliseconds. By packing Blackwell-class compute directly onto the robot, Nvidia ensures that language-grounded manipulation commands, visual perception, and motor control can all run locally with no cloud roundtrip. The global AI edge computing market reached an estimated $29.98 billion in 2026, and Nvidia controls roughly 39 percent of edge AI computing revenue, with its Jetson platform reaching approximately two million developers.

## Availability and what to watch

The H2 Plus reference design will be available from Unitree in late 2026, with Tech Times reporting an expected October ship date. Nvidia will also release a reference workflow for the smaller Unitree G1 -- already widely deployed in academic labs -- on GitHub and Hugging Face, letting existing G1 users adopt the Isaac GR00T pipeline immediately.

Pricing has not been disclosed. Glitchwire estimates that a complete system could run well into six figures, given that the Unitree H2 lists at roughly $29,900 and the Sharpa Wave hands reportedly cost around $50,000 each.

Nvidia has confirmed plans to extend the Isaac GR00T reference design to humanoid hardware partners in the United States, Europe, and South Korea, though no names have been disclosed. If the model follows the trajectory CUDA established for AI training -- where the company that defines the platform captures value long after the hardware ships -- the reference design is less a product launch than a standards play for the emerging physical AI ecosystem.
