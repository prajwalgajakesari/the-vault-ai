# Black Forest Labs FLUX 3 Folds Image, Video, Audio and Robot Control Into One Model

The German lab that taught the internet to generate photorealistic images now wants to teach machines to move. On July 23, 2026, Black Forest Labs (BFL) unveiled FLUX 3, a multimodal frontier model that generates images, produces up to 20 seconds of video with synchronized audio, and, in a decisive break from the companys past, predicts the physical actions a robot should take. The same architecture that renders a coffee cup can now help a robotic arm pick one up.

It is a striking pivot for a company best known for the FLUX text-to-image models that power a large share of open-weight image generation, and whose valuation has climbed to roughly $3.25 billion. With FLUX 3, BFL is arguing that the boundary between generating pixels and controlling robots was never real to begin with.

## One Backbone For Pixels And Actions

The technical bet underlying FLUX 3 is that image, video, audio and action are all facets of the same modeling problem. BFL says the model jointly learns from images, video and audio within a single unified architecture built on a method it calls Self-Flow, and that the same backbone can be extended to predict actions. In the companys telling, testing showed that video generation and action prediction do not require separate foundations.

Co-founder and Chief Executive Robin Rombach framed the thesis bluntly. "A model trained only on images can only generate images," he said. The deeper claim is about physics: "The process of predicting video is the process of learning principles of the real physical world such as weight, contact and timing." Learn to predict the next frame convincingly, the argument goes, and you have implicitly learned how objects behave, which is exactly what a robot needs to know.

On the generative side, FLUX 3 produces up to 20 seconds of video complete with dialogue, sound effects and background music. In human preference testing, BFL reported win rates of 77 percent against Runway Gen-4.5 and 93 percent against Luma Ray 3.2, and said it held an advantage in 52 percent of evaluations against Google Gemini Omni and Seedance. The company is candid that these are human-preference comparisons rather than quantitative benchmarks.

## FLUX-mimic Is Already On A Factory Floor

The most consequential piece of the announcement is not a video demo but a robot. BFL built FLUX-mimic, a video-action model that pairs the FLUX 3 backbone with the robot-learning expertise of Swiss startup mimic robotics AG. It is not a lab curiosity: FLUX-mimic is running on real hardware that has been tested and deployed at automaker Audi.

The tasks are exactly the kind that have long frustrated conventional automation: kitting parts into structured trays, inserting electronic control units into tight-fitting fixtures, assembling components, and manipulating soft materials such as seals and cables. Audi describes these as categories that traditional programmed robotics cannot handle cost-effectively in premium-vehicle production, because the variant diversity of each model breaks rigid, hand-coded routines.

BFL also claims a sharp efficiency gain in teaching the system new skills. FLUX-mimic can reportedly be fine-tuned for a specific manipulation task with as little as 30 minutes of robot data, where prior approaches often required 30 hours or more. If that holds up in production, it reframes robot deployment from a months-long engineering project into something closer to a same-day setup.

## Why The Convergence Matters

FLUX 3 lands squarely in the industrys hottest fault line: the collision of multimodal generative AI and physical AI. The premise that world models trained on video are the shortest path to capable robots is now shared, in various forms, by Nvidia, Google DeepMind and a wave of humanoid startups. BFLs contribution is to insist that content creation and robot control are literally the same foundation, not adjacent products, and to put a model on a factory floor to prove it.

That framing also sets up a direct rivalry with OpenAI, which has signaled its own ambitions in physical AI and robotics. A European lab reaching a paying industrial customer, Audi, before the incumbents ship comparable hardware deployments is a meaningful marker, and a rare instance of a frontier lab monetizing physical AI through manufacturing rather than chatbots.

## What To Watch

For now, access is deliberately narrow. FLUX 3 Video is in gated early access via API and private weights for selected partners, while FLUX 3 Action, including FLUX-mimic, is limited to selected research and commercial robotics partners. BFL has said a public-weights model is due in the second half of 2026.

The open questions are whether FLUX-mimics 30-minute fine-tuning holds outside Audis carefully chosen tasks, whether BFL can scale from one flagship customer to a robotics business, and whether the unified-architecture thesis survives contact with the messiest parts of the real world. If it does, the company that made images may end up remembered for making robots move.