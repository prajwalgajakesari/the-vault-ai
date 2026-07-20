# NVIDIA's Cosmos 3 Edge Pushes Physical AI to the Robot, and Japan Is the Testbed

Jensen Huang spent last week in Tokyo, and the thing he brought with him was small. Cosmos 3 Edge, the model NVIDIA unveiled during the visit, is four billion parameters — a rounding error next to the trillion-parameter frontier systems that dominate the AI conversation. But it is designed to do something those models cannot: sit inside a robot, watch the world through its cameras, and decide what the arm should do next, without ever touching a data center.

That is the bet NVIDIA is making, and it chose Japan's factory floors as the place to prove it.

## What was actually announced

Cosmos 3 Edge is a new member of NVIDIA's Cosmos 3 open world-model family, built on the company's Nemotron foundation. NVIDIA describes it as helping embodied systems “see, reason in real time and predict robot actions locally” — on-device vision reasoning plus robot policy generation, rather than perception in the cloud and control on the robot.

The specifics matter more than the framing. At 4 billion parameters it is light enough to run on edge GPUs. Developers using the open Cosmos framework can post-train it for a specific robot, vehicle, sensor rig or environment in roughly a day, which is the number NVIDIA is really selling: adaptation measured in hours, not quarters. It runs across RTX GPUs, DGX systems and the Jetson line, including the T2000 and T3000 modules announced the same week. The T3000 delivers 865 FP4 teraflops in a package NVIDIA says is about half the size and power draw of the T5000, with 32GB of memory and 273GB/s of bandwidth; the T2000 lands at 400 FP4 teraflops and 16GB. Both ship in Q1 2027 — emulation via JetPack 7.2.1 is the near-term path, so this is a roadmap announcement as much as a shipping one.

Alongside it, NVIDIA released new Metropolis libraries — VSS Blueprint 3.2, DeepStream 9.1, TAO 7 and a Physical AI Data Factory, more than 80 skills in total — which it claims let developers build Cosmos-powered vision AI agents at least six times faster. That 6x figure is NVIDIA's own.

## Japan as the deployment surface

More than 20 Japanese companies stated an intent to join the Cosmos Coalition, NVIDIA's grouping for open world-model development: FANUC, Fujitsu, Hitachi, Kawasaki Heavy Industries, Kubota, NEC, SoftBank Corp., Sony Group, Honda R&D, Preferred Networks, Yaskawa Electric among them. Note the verb: *intend to join*. These are commitments of direction, not signed deployments.

The concrete work is more specific. Fujitsu is leading a collaborative control platform with FANUC, Yaskawa and Kawasaki, built on Cosmos, Isaac, Omniverse NuRec and the Newton physics engine. Kubota is exploring Cosmos for autonomous agriculture. Hitachi says its Metropolis-based rail solutions cut maintenance costs and energy use by 15%.

Behind all of it is money. Japan's government is putting roughly $2.4 billion toward a national AI infrastructure effort, per CNBC, including an AI factory built by Noetra Corp. on 27,500 Rubin GPUs and 13,750 Vera CPUs drawing 140 megawatts. Japan is targeting more than 30% of a global AI robotics market that NVIDIA and partners value at $133 billion by 2040.

## The drug-discovery flank

The same Tokyo week extended NVIDIA's life-sciences footprint. Tokyo-1, the AI drug discovery consortium operated by Mitsui subsidiary Xeureka, now spans Astellas, Daiichi Sankyo and Ono Pharmaceutical, with Eisai joining in April. Astellas has deployed nearly all of NVIDIA's BioNeMo NIM microservices and is running the BioNeMo Agent Toolkit, released June 23. Ono is using the Boltz-2 microservice for internal discovery; Daiichi Sankyo is running ultralarge-scale virtual screening on Tokyo-1 with RAPIDS behind the data processing.

It is the same architectural story in a different building: put the model next to the work.

## Why edge physical AI matters

Cloud inference has a floor set by physics. A robot arm reacting to a slipping part, a mobile robot avoiding a person in a corridor, an inspection system flagging a defect mid-line — none can afford a round trip to a data center, and none can afford to fail when the network does. Moving the world model onto the machine removes both the latency and the dependency. 

The strategic layer is more interesting. NVIDIA is not selling Japan a robot brain; it is selling a stack — Cosmos for the world model, Isaac for robotics, Metropolis for vision agents, Jetson for the silicon — and inviting the country's incumbents to build on top. NVIDIA gets 20-plus of the world's best robotics companies standardized on its runtime, plus a sovereign-AI customer with a national budget.

“Japan has historically been very good at precision manufacturing and very large-scale manufacturing, but now we have AI,” Huang told reporters in Tokyo. “You can combine the two technologies and create robotics. The future of intelligent manufacturing, the future of robotics can now start.”

Fujitsu president and CEO Takahito Tokita, who lunched with Huang and the CEOs of Kawasaki, FANUC and Yaskawa before the press event, framed it as a shared project: “Although we come from different countries and industries, we share the same values. We make business decisions not only for the benefit of our own companies, but also with the sustainable development of our industries and ultimately the world in mind.”

## What to watch

Three things. First, whether the one-day post-training claim survives contact with real robots — that number, more than the parameter count, determines whether Cosmos 3 Edge becomes infrastructure or a demo. Second, Q1 2027, when T3000 and T2000 actually ship; until then the Japanese deployments run on existing Thor hardware. Third, how many of the “intend to join” commitments convert into shipping products. Coalition membership is cheap. Retooling a FANUC production line is not.

*Note: NVIDIA dated its press release July 15, 2026; most trade coverage carried it July 16. The 6x Metropolis speedup and the $133 billion market figure are company-supplied and not independently verified.*
