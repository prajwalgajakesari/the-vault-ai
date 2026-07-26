# A New Open-Source Framework Lets AI Move Between Robot Bodies

Getting a new robot to do anything at all can eat a semester. Before a graduate student tests a single idea, they often spend weeks -- sometimes an entire first year -- wiring together drivers, sensors, teleoperation rigs and data pipelines that work for exactly one machine and no other. A team at Carnegie Mellon University wants that tax to disappear.

On July 9, researchers in CMU School of Computer Science released Robot I/O, or RIO, an open-source Python framework that gives roboticists a single, modular interface for robot control, data collection, teleoperation and AI deployment. The pitch is deceptively simple: build your software once, then move it -- and the AI models it runs -- across robotic arms, humanoids and other platforms without rebuilding the stack from scratch. The work has been accepted to Robotics: Science and Systems (RSS) 2026, one of the field flagship conferences, and the code is public on GitHub.

## The bottleneck is infrastructure, not ideas

"The biggest bottleneck in robot learning research is not ideas, it is infrastructure," said Jean Oh, an associate research professor in CMU Robotics Institute and the project corresponding author. "Students can spend an entire semester or even their entire first year simply setting up a robot before they can begin their research. RIO gives researchers and engineers a lightweight, modular foundation for deploying robots quickly on any platform."

That fragmentation carries a real cost. Because most robot code is written for one exact hardware configuration, reproducing a result on a different machine usually means rewriting the entire control stack. Datasets collected on one setup are hard to share, and AI models trained on one robot rarely run out of the box on another. As modern robotics leans on large, general-purpose models trained on enormous piles of demonstration data, that friction has quietly become the choke point.

"Today, everyone talks about needing more data," said Eliot Xing, a Robotics Institute Ph.D. student and co-lead author. "But robot data does not come from thin air. You need robots to collect it, and that takes robot infrastructure. We have been missing some shared building blocks that other AI fields have, the ones that let researchers build on each other work instead of starting from scratch every time."

## One template, many robots

RIO is built on what the team calls a node-middleware architecture. Teleoperation interfaces, sensors, robots and AI policies are all implemented from the same template, and because those nodes are middleware-agnostic, they can be swapped onto different communication backends depending on the deployment. Shared memory handles zero-copy exchange for fast local work, while Zenoh or ZeroRpc move data across machines for distributed setups. A complete teleoperation loop, the researchers note, fits in a handful of lines of Python and a single configuration file.

The supported-hardware list is the real argument. Out of the box, RIO drives humanoids (Unitree G1, Booster T1), robot arms from UFactory, Universal Robots, Franka and Kinova, plus a spread of grippers, cameras and teleoperation devices ranging from a SpaceMouse to an Apple Vision Pro headset. The team validated the framework by deploying two state-of-the-art vision-language-action models, Physical Intelligence pi-0.5 and NVIDIA GR00T N1.5, across three morphologies and four hardware platforms, reaching at least 60 percent task success with just 50 teleoperated demonstrations, and hitting 92.5 percent on a shirt-folding task with an xArm7.

Speed is a selling point too. In head-to-head profiling against LeRobot, a widely used open-source stack, RIO clocked 130.3 milliseconds of end-to-end observation-to-action latency versus 581.2 milliseconds -- a 4.46-times reduction -- with sub-millisecond middleware round trips. For contact-rich, dynamic tasks like throwing a ball or flipping a tortilla, that lower latency translates directly into a higher effective control frequency.

The accessibility claim got an unusually concrete test. Reya Shukla, an undergraduate intern with machine-learning experience but no robotics background, was asked to unbox a robotic arm and configure it for teleoperation using only RIO documentation. She went from opening the box to controlling the robot in about two hours.

## A ROS moment for the AI era

RIO is arriving at a pointed moment. The Robot Operating System (ROS) became the de facto plumbing for a generation of robotics, but it predates the general-purpose, learned models now reshaping how robots are controlled. RIO reads as an attempt to supply the equivalent connective tissue for the AI era -- the shared substrate that lets a policy trained on one arm be fine-tuned onto a humanoid without a rewrite. If cross-embodiment transfer is where robotics is heading, the field needs a common interface to make it routine rather than heroic, and that is precisely the gap RIO targets.

The industrial stakes are explicit. "In industrial robotics settings, this kind of infrastructure really matters because real deployments rarely involve just one robot, one sensor setup or one fixed environment," said Jonathan Francis, lead research scientist at the Bosch Center for Artificial Intelligence and courtesy faculty at CMU. "RIO helps make robot learning systems more reusable across platforms, which can shorten the path from a research prototype to something that can be tested and adapted in the real world."

## What to watch

RIO is a collaboration across CMU, Delft University of Technology, the Bosch Center for AI and Lavoro AI, a startup co-founded by Oh that is commercializing simpler robot deployment. It remains an active research project, and the team says future work will focus on expanding hardware support and lowering the barrier to bringing new robots online -- with a longer-term ambition of robotics foundation models that let machines adapt to new tasks and environments across platforms on their own.

The open question is adoption. Frameworks live or die by community, and whether RIO becomes shared infrastructure or one more option in a crowded field will depend less on its benchmarks than on how many labs decide to build on it. If it catches, the weeks-long setup slog that greets every new robot could start to look like a relic.