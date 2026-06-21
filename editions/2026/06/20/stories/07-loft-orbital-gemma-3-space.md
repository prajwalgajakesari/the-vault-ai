# Loft Orbital's YAM-9 Runs Gemma 3 in Orbit, a First for Vision-Language AI in Space

In April, an Earth observation satellite did something no spacecraft had done before: it found what it was looking for entirely on its own, without a single human analyst on the ground and without beaming a raw image back to Earth first. Aboard YAM-9, a spacecraft built by the Franco-American space infrastructure company Loft Orbital, Google DeepMind's Gemma 3 vision-language model answered natural-language queries about live Earth imagery, classified what it saw, and returned plain-English summaries — all from low Earth orbit. It is, by multiple accounts, the first reported deployment of a vision-language model (VLM) in space, and it quietly rewrites where the value sits in the Earth-observation business.

The milestone, first reported by TechCrunch on June 15, marks a shift from the satellite-as-sensor model that has defined the industry for decades. Instead of streaming gigabytes of pixels to the ground for analysts and machine-learning pipelines to chew through, YAM-9 ran the analysis where the data was born.

## What Actually Happened in Orbit

Researchers tasked Gemma 3 with the kind of fuzzy, context-dependent queries that have traditionally required a human eye. They asked it to classify sensor data where natural environment meets human development, and to identify infrastructure around railway hubs. The model did both — interpreting the imagery and responding in natural language, on-device.

That is a meaningfully different capability than the object detection some satellites already run on orbit. A VLM fuses the contextual reasoning of a large language model with the ability to parse imagery, so it can take a plain-English question about a scene and return a plain-English answer rather than just flagging pixels that match a trained class.

The demonstration leaned on three pieces working in concert. Gemma 3 itself is Google DeepMind's open-weight, decoder-only model family, available from roughly 1 billion to 27 billion parameters and purpose-built for edge applications — designed, in other words, to run on constrained hardware far from any data center. Its SigLIP vision encoder turns imagery into token embeddings the language model can reason over alongside text. Wrapping the model was NAVI-Orbital, a software harness developed by a team at NASA's Jet Propulsion Laboratory and led by technical lead Juan Delfa Victoria; engineers had to strip Gemma 3's library dependencies down to fit the satellite's tight onboard memory budget. The compute itself ran on an Nvidia Jetson Orin AGX GPU, one of the highest-performance edge accelerators currently flying in low Earth orbit.

YAM-9 launched in the fall of 2025 as a pathfinder for Loft's orbital-AI ambitions. Loft builds spacecraft as platforms for third-party customers — a model closer to infrastructure-as-a-service than traditional satellite manufacturing — and currently operates 12 spacecraft on orbit.

## Why On-Orbit Inference Changes the Economics

The case for moving inference into orbit is latency and bandwidth. Today, a satellite captures imagery, downlinks it during a narrow ground-station pass, and waits for analysts to triage the flood of raw data. For time-sensitive use cases — disaster response, defense surveillance, monitoring a wildfire or a flood — that round trip can cost hours. Running a VLM in orbit collapses the loop: the satellite does its own initial triage and downlinks an answer instead of a haystack.

"It opens the door to always-on patrol layers in space," Loft's head of AI, Paul Lasserre, told TechCrunch. "If you have a VLM, you can have logic — like 'monitor this border for me, and let me know when something is suspicious,' and interact back and forth with the satellites."

The engineering constraints are unforgiving. Satellites operate on a tight power envelope drawn from solar panels, must manage heat in vacuum where there is no air to carry it away, and get only short imaging windows as they streak overhead. Those are precisely the conditions an efficient, open-weight model is built for. Gemma 3's architecture — including a local-to-global attention ratio that reduces memory pressure — is what made it feasible to squeeze onto flight hardware at all. The open-weight nature mattered too: the JPL team could take the model off the shelf, inspect it, and re-engineer its dependencies without negotiating access to a closed API that, in any case, no satellite can phone home to.

## What to Watch

Loft is not planning to stop at one spacecraft. "Now that we've proven the concept, that's really the direction of travel," Lasserre said. The goal is a constellation large enough to guarantee real-time coverage of anywhere on Earth — somewhere between 50 and 100 satellites like YAM-9, by his estimate, against the dozen Loft flies today.

The company will not be alone. Planet Labs already flies satellites with Jetson Orin processors, using them for simpler object detection for now, with research underway on VLMs. Kepler Communications, which operates the largest cluster of GPUs in space, declined to confirm whether it had run VLMs, citing partner NDAs, but noted "several undisclosed use cases" since its compute spacecraft launched in January. The lessons from deploying small models on orbit — especially in the prosaic-but-vital areas of power and memory management — are exactly the ones that will inform larger AI infrastructure in space.

The most intriguing thread may be where NAVI-Orbital came from. The project traces to JPL researcher Taran Cyriac John, who was thinking about interactive digital assistants for astronauts exploring the Moon or Mars — the kind of AI companion familiar from video games and movies. For now, the technology has come back down to Earth-facing duty: a satellite that has stopped being a passive camera and started being an analyst. The open question is no longer whether on-orbit inference works. It is how quickly the value layer in Earth observation migrates from the ground station up to the spacecraft itself.
