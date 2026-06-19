# NAVI-Orbital Puts a Zero-Shot Vision-Language Model in Space for Autonomous Earth Observation

For the first time, an Earth observation satellite has answered a plain-English question about the world below it — without sending a single pixel back to a human analyst first. In a new arXiv preprint posted June 18, 2026, researchers at NASA's Jet Propulsion Laboratory describe what they call the first in-orbit demonstration of a zero-shot vision-language model running onboard a spacecraft, a milestone that quietly took place in April and could reshape how the satellite industry thinks about what a sensor in orbit is actually for.

The paper, "NAVI-Orbital: First In-Orbit Demonstration of a Zero-Shot Vision-Language Model for Autonomous Earth Observation," is authored by Juan Manuel Delfa Victoria, Taran Cyriac John, and Andrew W. Herson. The demonstration ran aboard Yam-9, a spacecraft built and operated by the space infrastructure company Loft Orbital, which launched in the fall of 2025 as a pathfinder for orbital AI.

## The bottleneck nobody can downlink their way out of

Modern Earth observation has an embarrassing problem: satellites collect far more data than anyone can get to the ground, let alone look at. A single high-resolution imaging spacecraft can generate terabytes per day, but the radio links that send that data down to Earth are narrow, the ground-station passes are brief, and the queue of imagery waiting for a human or a machine-learning pipeline to inspect it only grows. The result is a widening gap between what satellites see and what we can actually act on.

The conventional fix has been to throw more bandwidth and more analysts at the problem. NAVI-Orbital takes the opposite approach: move the analysis up to the satellite, so that only the answer — not the raw imagery — needs to come down.

## What NAVI-Orbital actually did

The demonstration combined three pieces. The first is Google DeepMind's Gemma 3, an open-weight vision-language model purpose-built for edge applications — meaning it is designed to run on constrained hardware far from a data center, using a SigLIP vision encoder and an attention design that keeps memory pressure low. The second is NAVI-Orbital itself, the software harness developed by Delfa Victoria's team at JPL, which stripped down Gemma 3's library dependencies and restructured the inference pipeline so the whole thing would fit inside the satellite's tight memory and processing budget. The third is an agent-orchestration layer that managed the autonomous query-and-response loop. The model ran on an Nvidia Jetson Orin AGX GPU, one of the leading chips now being flown for onboard compute.

The "zero-shot" part is the crux. Rather than training a bespoke classifier for each target, researchers on the ground simply issued natural-language commands and got structured answers back. According to the paper and the team's account, the model was asked to classify sensor data where the natural environment meets human development, and to identify infrastructure around railway hubs — and it did, with no real-time data downlink in the loop. A VLM that accepts free-form queries means a satellite can be re-tasked with a sentence instead of a software update.

## Why a VLM in orbit matters

The near-term payoff is data triage. If the spacecraft can classify scenes, flag anomalies, and return a short structured summary, the downlink stops being a firehose of raw imagery and becomes a trickle of actionable insight — compressing the time from observation to answer from hours to something closer to real time.

The longer-term implications run further. Loft's head of AI, Paul Lasserre, framed it to TechCrunch as the start of "always-on, patrol layers in space," describing a future where an operator could tell a satellite to "monitor this border for me, and let me know when something is suspicious," then interact with it conversationally. That vision maps cleanly onto disaster response (spotting flooding or wildfire fronts as they happen), defense and maritime monitoring, and commercial tasking efficiency, where the scarce resource has always been analyst attention rather than imagery.

There is also a research dividend. The idea behind the project began, fittingly, far from Earth observation: co-author Taran Cyriac John was thinking about digital assistants for astronauts on the Moon or Mars, where a suited crew member cannot exactly stop to type on a keyboard. A conversational model that can see and reason is useful to a spacecraft and to a human explorer alike.

## What to watch

The demonstration is a proof of concept, not a constellation. Loft currently operates 12 spacecraft, and Lasserre estimated that real-time global coverage with Yam-9-class satellites would take somewhere between 50 and 100 of them. The hard, unglamorous engineering ahead is in power and thermal management — keeping an Orin-class GPU fed and cool in orbit — and in the memory discipline that let NAVI-Orbital squeeze a modern VLM onto flight hardware at all.

Watch, too, for the field to crowd quickly. Planet Labs already flies Jetson Orin processors for simpler object detection and says VLM research is underway; Kepler Communications, which runs the largest orbital GPU cluster, has hinted at undisclosed compute use cases since its January launch. NAVI-Orbital's claim to be first is narrow and specific — a zero-shot VLM, demonstrated in orbit — but if it holds, the more important number is the second satellite to do it, and how fast it arrives.
