# Google DeepMind's Gemini Robotics 2 Gives Humanoids Whole-Body Control

For years, the flashiest humanoid robot demos have quietly stopped at the waist. Arms reached, fingers pinched, but the legs stood still. On July 30, Google DeepMind moved the line all the way to the floor with Gemini Robotics 2, a suite of AI models that, for the first time, lets a single learned policy coordinate a humanoid from what the company calls "feet to fingertips."

The launch, detailed in a blog post by Carolina Parada, DeepMind's head of robotics, extends the company's physical-AI push from tabletop manipulation to genuine whole-body movement. In the headline demonstration, Apptronik's Apollo 2 humanoid is told to "put the watering can into the green bin in the bottom shelf." It parses the instruction, walks across the room, picks up the can, steps to the shelving unit, crouches, and sets it down precisely, a sequence that requires balance, navigation, and dexterity stitched together on the fly.

"Gemini Robotics 2 enables robots to reason through every movement, unlocking a broad range of tasks," Parada wrote.

## Three models, one brain-and-body split

Gemini Robotics 2 ships as three models. The core is a vision-language-action (VLA) model that converts camera input and spoken instructions directly into motor commands, and it can now drive full humanoids as well as bi-arm rigs. Above it sits Gemini Robotics ER 2, an embodied-reasoning vision-language model that acts as the "high-level brain," planning multi-step tasks that run several minutes, tracking progress, self-correcting when a step fails, and, newly, coordinating more than one robot at a time. The third, Gemini Robotics On-Device 2, is a slimmed VLA that runs locally with no cloud connection and adapts to an unfamiliar robot body in a few hours using fewer than 200 examples.

DeepMind demonstrated the same model checkpoint controlling three different bodies: Apollo 2 with Apptronik's five-fingered, 22-degree-of-freedom SharpaWave hands; Apollo 2 with Inspire hands; and a Franka Duo bi-arm platform with a Robotiq gripper. Beyond the watering-can routine, the models were shown cleaning up trash, screwing in a lightbulb, inserting a cassette into a boombox, and tying off a garbage bag.

DeepMind's own benchmark numbers are notably candid about how hard fine motor control remains. On the SharpaWave hands, Apollo 2 unscrewed a bulb 92 percent of the time but managed to screw one in just 36 percent; tying a trash bag landed at 44 percent. Whole-body pick-ups ranged from 76 percent off a shelf down to 46 percent off the floor. Grippered precision-insertion on the Franka Duo, by contrast, hit 90 percent. "The multi-finger dexterous manipulation remains challenging," the company conceded.

## The hardware partner and the data loop

Apptronik is more than a demo prop. The Austin company has been feeding DeepMind training data through "Robot Park," a facility where fleets of Apollo units perform real tasks to generate examples. "What we're building is a continuous learning loop with the Google DeepMind Robotics team: robots working, collecting data, and improving with every cycle, in real environments, on real tasks," Apptronik CEO Jeff Cardenas said in announcing the effort. That loop, deploy then collect then retrain, is the mechanism DeepMind is betting will close the gap between a 46 percent floor pick-up and something a warehouse would trust.

## The race for physical AI

The release lands in the middle of an escalating contest to build the foundation model for the physical world. Nvidia has positioned its GR00T models and Cosmos world-model stack as neutral infrastructure for any humanoid maker; Tesla is pushing Optimus with its own end-to-end vision approach; and Figure recently broke from OpenAI to build its Helix system in-house. DeepMind's angle is leverage. It is not building a robot at all, but selling the "intelligence layer" that runs across Apptronik, Boston Dynamics, and Agile Robots hardware alike, the same way Gemini rides on top of many devices. Making ER 2 available now through Google AI Studio, with the VLA models in early access, follows that platform logic.

Safety is threaded through the launch. DeepMind introduced ASIMOV-Agentic, a benchmark that tests whether the reasoning agent will refuse an unsafe command from the action model and call for a human when uncertain, and it says ER 2 is its best model yet at detecting nearby people and stopping.

## What to watch

The honest benchmarks are the story's tell. Whole-body control is real, but reliability at human speed is not here yet, and DeepMind says as much about both movement pace and multi-finger precision. Watch three things: whether the Robot Park data flywheel visibly lifts those success rates in the next release; whether multi-robot collaboration moves from staged demo to deployment at customers like Mercedes-Benz and GXO; and whether rivals answer with their own whole-body policies. The waist-up era of humanoid demos is over. The question now is how fast the rest of the body catches up.
