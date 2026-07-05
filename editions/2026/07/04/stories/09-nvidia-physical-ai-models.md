## The model layer for robots grows up

NVIDIA has released a new tier of open foundation models for physical AI, betting that the hardest part of building a robot is no longer the motors or the metal but the brain — and that most developers should download that brain rather than train it from scratch. Unveiled alongside a fleet of next-generation robots from global partners, the release reframes robotics the way ImageNet and GPT once reframed vision and language: as a problem of pretrained models, synthetic data and simulation, not bespoke engineering.

"The ChatGPT moment for robotics is here," said Jensen Huang, NVIDIA's founder and CEO. "Breakthroughs in physical AI — models that understand the real world, reason and plan actions — are unlocking entirely new applications." The pitch is blunt: turning single-task machines into reasoning "generalist-specialist" robots takes capital and expertise most teams lack, so NVIDIA wants to supply the foundation models and let partners focus on behavior.

## What NVIDIA actually shipped

The centerpiece is a refreshed family of open models, all posted to Hugging Face. **Cosmos Transfer 2.5** and **Cosmos Predict 2.5** are world foundation models that generate physically based synthetic data and let developers evaluate robot policies in simulation before touching hardware. **Cosmos Reason 2** is an open reasoning vision-language model meant to let machines see, understand and act like humans. And **Isaac GR00T N1.6**, a vision-language-action model purpose-built for humanoids, adds full-body control and taps Cosmos Reason for contextual understanding.

Around the models sits new plumbing. **Isaac Lab-Arena**, built with Lightwheel, is an open-source framework for large-scale policy evaluation that connects to benchmarks like LIBERO and RoboCasa. **NVIDIA OSMO** orchestrates the messy pipeline — synthetic data generation, training, software-in-the-loop testing — across workstations and cloud, and is already integrated into Microsoft's Azure Robotics accelerator toolchain. On the hardware side, the Blackwell-based **Jetson T4000** module arrived at $1,999 in volume, delivering 1,200 FP4 TFLOPS and 4x the performance of its predecessor in a 70-watt envelope.

Crucially, NVIDIA is routing all of this into the open-source mainstream. Working with Hugging Face, it is folding Isaac and GR00T into the LeRobot framework — uniting NVIDIA's 2 million robotics developers with Hugging Face's 13 million AI builders. Robotics is now the fastest-growing category on Hugging Face, and GR00T N models and Isaac Lab-Arena are available there for fine-tuning and evaluation.

## Partners bring the bodies

The models only matter if robots run them, and the launch came stacked with hardware. Boston Dynamics, Caterpillar, Franka Robotics, Humanoid, LG Electronics and NEURA Robotics all debuted machines built on the NVIDIA stack. NEURA is launching a Porsche-designed Gen 3 humanoid plus a smaller dexterous model; Richtech Robotics showed Dex, a mobile manipulation humanoid; AGIBOT introduced industrial and consumer humanoids alongside its Isaac Sim-integrated Genie Sim 3.0; and LG revealed a home robot for household tasks. Franka, NEURA and Humanoid are using GR00T-enabled workflows to simulate, train and validate new behaviors. Caterpillar, meanwhile, is extending the model into construction and mining autonomy.

## Why foundation models for robots matter

The strategic logic is sim-to-real. Real-world robot data is slow, expensive and inconsistent — every warehouse, field and operating room differs — so world models that capture physics and causality let robots practice millions of task variations in simulation and generalize to conditions they have never seen. Agricultural startup Aigen, for instance, post-trains Cosmos world models on its own data to cover millions of farming scenarios; Toyota Research Institute customizes Cosmos WFMs for teleoperation data augmentation. Synthetic data plus benchmarked evaluation is becoming the default path from research to deployment.

That approach puts NVIDIA squarely in an intensifying embodied-AI race. Google DeepMind's Gemini Robotics and Gemini Robotics-ER inject large-model reasoning directly into robot control, and Boston Dynamics has partnered with DeepMind to run Gemini on Atlas. Tesla has begun mass-producing Optimus Gen 3 with a sub-$20,000 target, and Figure continues to push its own humanoid foundation model. NVIDIA's differentiator is neutrality: rather than build one robot, it aims to be the pretrained substrate — the "Android of generalist robotics," as some have framed it — underneath everyone else's.

## What to watch

The open question is whether pretrained physical-AI models deliver the reliability leap that language models did. Benchmarks like Isaac Lab-Arena will start to reveal whether skills learned in simulation truly survive contact with the real world, and whether a shared model layer beats vertically integrated rivals training on proprietary fleet data. Watch three signals over the next year: how many partner robots reach paid deployment rather than demos; whether GR00T downloads and LeRobot integrations translate into working products from smaller teams; and whether DeepMind, Tesla or Figure can match NVIDIA's ecosystem play. The models are shipping. Now the robots have to work.
