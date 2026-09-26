Perceptron wants a single model to see for a drone, a robot dog and a pair of smart glasses, with no retraining for each one. On Thursday, September 25, the Bellevue, Washington startup released Perceptron Mk1.5. The company calls it an embodied reasoning model for physical agents. It takes in text, images, first-person video and audio, and it answers with plain language or with machine-readable geometry: points, boxes, polygons, object tracks and timestamped video clips. The company says it runs two to five times faster than its predecessor and costs a small fraction of what frontier labs charge.

Mk1.5 is priced at $0.15 per million input tokens and $1.50 per million output tokens. That is the same rate Perceptron set for Mk1 in May. It went live the same day on Perceptron's own API and on OpenRouter. OpenRouter's listing shows a context window of 36,864 tokens and a maximum output of 8,192 tokens. OpenRouter describes the model as "Perceptron's embodied reasoning model for physical agents." Three things are new since Mk1: audio input, video tracking and tool calling.

## From perception to agent

Mk1 was mostly a video-understanding model. Mk1.5 is built to act more like an agent. Perceptron says it can track objects across a scene as timestamped geometry, which gives a robot controller or a headset app coordinates to work with rather than a text caption. It can call external tools such as web search and reverse image search. It can also split a hard request into pieces and hand them to subagents that run in parallel. In one company example, the model sorts through the food items in a basket and checks each one for allergens.

Co-founder and CTO Akshat Shrivastava said in launch posts on X that the model can "leverage tools like search and reverse image search to remain efficient." His point was that the model can answer questions that need a lot of world knowledge without storing all of that knowledge in its weights. Shrivastava also wrote that the model "led to zero-shot control and long horizon tasks spanning embodiments." That is the central claim behind the one-model-for-many-machines pitch.

Audio is a full input alongside video, not an extra. Co-founder and CEO Armen Aghajanyan pointed to a demo in which the model can "predict the exact timestamp a truck is closest to the observer using the doppler effect." In other words, it works out when the truck is nearest from the change in its sound. According to OpenRouter's documentation, a video's soundtrack is only analyzed when a developer turns that on for a given request.

## The benchmark claims

Perceptron says Mk1.5 leads on three of four video-object-segmentation benchmarks it reported. It also claims a 12-point gain on the hard split of EgoSchema, a benchmark for long first-person video. And on EgoChores, an internal benchmark, it reports 50 percent better hand localization than Google's Gemini 3.8 Flash. Aghajanyan summed up the release as "setting a new SoTA and beating models 25x it's cost."

All of these figures come from Perceptron, and none had been independently reproduced at publication. EgoChores is the company's own test set, so outsiders cannot check it. The 25x cost comparison depends on which competitor and which price tier you compare against.

Mk1.5 is the company's third model release in about four and a half months. Mk1 launched on May 12 as a low-cost video-understanding model, and Aghajanyan said at the time: "We built Perceptron to make the physical world legible to AI systems." In late August the company released Isaac 0.5, a 36-billion-parameter open-weight robotics model built for warehouses and factory floors. Aghajanyan and Shrivastava are both former research scientists at Meta's FAIR lab and founded the company in November 2024. PitchBook data cited by TechCrunch shows $21 million raised from Bessemer Venture Partners, Foundation Capital and S32. TechCrunch reported in August that another round was in progress.

## Why It Matters

Physical AI has usually meant one of two things. Some teams use large general-purpose models that are too slow and too expensive to run on every frame from every camera. Others build narrow perception models trained separately for each robot or device. Perceptron made the same argument when it launched Isaac: "Physical AI today forces a false choice." Mk1.5 is an attempt to take a third route. It is a single, cheap, hosted model that returns structured spatial output and uses tools and subagents for the reasoning it has not memorized.

If the zero-shot claims hold up outside Perceptron's demos, drone makers, legged-robot companies and smart-glasses developers could share one perception layer instead of each training their own. The low price also matters for continuous video. At $0.15 per million input tokens, a device that streams video all day is no longer priced like a chatbot session. That could make always-on assistants in glasses cheaper to build. The catch is that a hosted API adds network latency and a cloud dependency, which safety-critical robots may not accept. The 2x to 5x speedup helps, but it does not remove the round trip.

## What to Watch

The first thing to watch is independent evaluation. Third-party scores on EgoSchema and the video-segmentation benchmarks, and ideally an outside version of the EgoChores test, will show whether the Gemini comparison holds up. Next is whether Perceptron names hardware partners that are running Mk1.5 on real drones, quadrupeds or glasses. The company has so far described cross-platform control rather than shipped deployments. Finally, watch whether Perceptron announces the new funding round TechCrunch reported in August. With three models in five months, it will need that money to keep releasing at this pace.
