# Alphabet's Intrinsic Open-Sources Its Robotics Stack at ROSCon 2026

Alphabet's robotics software unit Intrinsic has handed the core of its own industrial platform to the open-source community. At ROSCon 2026 in Toronto on Monday, the company released Intrinsic Core, a ROS-compatible robotics environment published on GitHub under the permissive Apache 2.0 license. It includes the real-time control, perception and planning software Intrinsic says it uses day to day in real manufacturing deployments.

The release is a bet that the bottleneck for physical AI is not a lack of smarter models. It is the slow, costly engineering work of getting those models to drive real arms, grippers and cameras. Intrinsic says robotics teams now spend hundreds of hours coding capabilities and infrastructure from scratch. Intrinsic Core packages that work into a pre-configured environment that runs on local hardware.

The man leading the effort insists this is not a one-time code dump. “This is not us coming by and dropping off some code and saying, ‘Have fun,’” Brian Gerkey, Intrinsic's chief technology officer and co-founder and board chair of Open Robotics, told The Robot Report. “What we're sharing this week is the core of our own software stack, this is a thing that we're also depending on.”

## What's in the box

The centerpiece is Intrinsic Control, a hardware-agnostic, real-time control framework that lets a robot change its behavior mid-trajectory based on sensor feedback. In practice, developers can swap robot arms, grippers and sensors without rewriting drivers. On the perception side, Intrinsic Core ships a pose estimation module built on Nvidia's FoundationPose foundation model. It provides six-degree-of-freedom pose estimation of 3D parts, so robots can find and handle parts without rigid, expensive fixtures.

The stack also includes motion planning that auto-generates collision-free paths instead of programming robots joint by joint, and grasp planning that adapts different grippers to a part's position and orientation using real-time sensor feedback. Simulation services powered by Gazebo let developers debug application logic, state machines and workcell behavior in one place. It also includes automated camera calibration and a set of pre-configured Intrinsic-ROS drivers for supported robots, grippers and 3D cameras. Under the hood, Gerkey said, Intrinsic is combining standard Linux containerization with Kubernetes so that production deployment fits naturally into existing ROS workflows.

Alongside the core release, Intrinsic published the Open Machine Tending Solution (OMTS), an open reference design for AI-enabled CNC machine tending. It runs on both Intrinsic Core and the Open Robotics Suite, and it can be customized for hardware from Universal Robots and FANUC. The target market is large and underserved. According to SiliconANGLE, Intrinsic says tens of thousands of shops in the U.S. and Europe fabricate precision parts, yet only 8% use any form of automation, largely because of cost and technical barriers. Intrinsic calls OMTS the first in a series of reference solutions.

Gerkey framed the reference app as proof that the platform is complete. It “keeps us as the developers of the system honest,” he said, “because it's a way to prove to ourselves that the system is complete enough to allow us to build a system like that.”

The scope is deliberately narrow for now. Intrinsic Core targets robotic arms doing manipulation work in commercial settings, and it does not support mobile robots or humanoids. Its ideal user is a developer already comfortable with ROS. Intrinsic's own blog post acknowledges that using the platform still requires some basic proficiency in robotics.

## Why It Matters

Physical AI is having a moment. Robot foundation models, vision-language-action systems and simulation-trained policies are advancing fast, but the space between a promising model and a working production cell has stayed stubbornly wide. Most of that space is plumbing: real-time control loops, calibration, drivers and collision checking. Every integrator has rebuilt it at least once. Open-sourcing a production-grade version of that layer lowers the cost of deploying whatever models come next, including models Intrinsic does not make.

The move also sharpens a strategic split in the industry. Several well-funded physical AI players are building vertically integrated, proprietary stacks that tie models, software and sometimes hardware together. Intrinsic, which Google folded into its own operations in February to speed up its physical AI work, is taking the Android route: give away the foundation and monetize the layers above it. Its blog post says solutions built on Intrinsic Core work directly with its paid enterprise offerings, including advanced AI models, the Flowstate development environment and industrial cloud services, “no refactoring or code rewrites needed.”

The open-robotics establishment is on board. Geoffrey Biggs, CTO of the Open Source Robotics Foundation, called the release “a step towards the point in the future where we get to have the equivalent of the red hats and the canonicals of robotics.”

The Nvidia tie-in stands out too. Building FoundationPose in natively, just as Nvidia pushes its own Isaac ROS 5.0 release, points to an open physical AI ecosystem where Google's orchestration layer and Nvidia's perception models are designed to work together.

## What to Watch

The first test is adoption. Intrinsic has a ready pipeline: its first AI for Industry Challenge, whose winners were announced this week, drew more than 5,000 developers and roboticists from 115 countries. Whether that interest turns into GitHub contributions, forks and third-party drivers will show if Intrinsic Core becomes a community project or remains a vendor showcase.

Next, watch how far the scope expands. Gerkey said Intrinsic wants to earn credibility in industrial manipulation before moving into other domains, so support for mobile manipulators or humanoids would be a significant signal.

Finally, watch the business model. The open core is the on-ramp. The real measure will be how many machine shops and integrators that start on the free tier move up to Intrinsic's commercial AI models and cloud services, and whether rivals answer with open releases of their own.
