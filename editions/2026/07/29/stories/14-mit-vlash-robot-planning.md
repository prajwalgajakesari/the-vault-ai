When a robot arm pauses mid-reach, freezes for a beat, then lurches into its next move, it is not being cautious. It is thinking. And that thinking, however brief, is what has kept a generation of impressive laboratory robots looking clumsy and slow in the real world. A new method from MIT wants to erase those pauses by teaching robots to plan around where they are about to be, not where they currently are.

The technique, called VLASH, was unveiled by MIT researchers on July 28, 2026, and it targets one of the most stubborn bottlenecks in modern robotics: the lag baked into the AI models that serve as a robot's brain. In tests, VLASH doubled the speed of robots on everyday manipulation tasks like pick-and-place, cut the delay between motions by more than 30-fold, and made robotic arms nimble enough to play table tennis and Whack-a-Mole.

## The problem with living in the present

State-of-the-art robots increasingly run on vision-language-action (VLA) models, generative AI systems that take in a camera feed and a task instruction, then output a short "chunk" of motions to execute. The trouble is that running one of these models is computationally expensive. The robot has to stop, observe, reason, and produce its next chunk before it can move again. Those repeated pauses are why so many demo-reel robots move in the halting, jerky rhythm that instantly marks them as machines.

"Our motivation was to overlap the thinking process with the execution process to make the reaction speed faster," said Jiaming Tang, an MIT EECS graduate student and co-lead author of the paper.

Overlapping thinking and acting sounds simple, but it hides a trap. If a robot plans its next move while still executing the current one, it is planning against a snapshot of the world that is already going stale. By the time the plan is ready, the arm has moved and the scene has changed.

"Since the environment will change after the robot moves, if we plan based on stale observations of the current environment, there will be a misalignment that causes very unstable control," Tang explained.

## Planning for a future that hasn't happened yet

VLASH — short for a system that performs future-state-aware asynchronous inference — sidesteps that instability with one key insight. The model cannot know exactly what the world will look like a moment from now, but it knows something almost as useful: where the robot itself will be. A robot always knows its current position and the trajectory of the actions it is committed to executing next.

So instead of feeding the model a stale picture of the present, VLASH feeds it a prediction of the robot's own state after the current chunk of motion finishes, and uses that to plan the next chunk. The thinking happens while the arm is still moving, and by the time the arm arrives, the next set of instructions is already waiting.

"In this way, we give the robot awareness of its future state," Tang said.

Crucially, the approach adds no computational overhead to the planning process and works across different robotic hardware. To squeeze out even more speed, the team layered on a technique called action quantization, generating coarser chunks so the robot takes a few larger steps along the same path. That trade cost a small amount of accuracy but let robots finish tasks two to three times faster overall. A companion training trick — regrouping and reusing training data so the model learns to trust future-state information over live observation — accelerated the fine-tuning process fivefold.

The numbers held up on real hardware, not just in simulation. In one benchmark, a VLASH-driven arm sorted cubes into a box by color twice as fast as the best baseline method while matching its 90 percent accuracy.

## Why this matters

The gap between a robot that works and a robot that is worth paying for is often measured in seconds. Warehouses, factories, and logistics operators do not deploy robots because they can complete a task; they deploy them because they can complete it fast enough to justify the capital. A picking robot that is half as fast as a human is a science project. One that is comparable or faster is a purchase order.

By attacking latency without demanding bigger models or beefier onboard compute, VLASH aims squarely at that economic threshold. It is a reminder that the frontier of applied robotics right now is often less about smarter models and more about making the smart models people already have respond in real time. The researchers also point to higher-stakes uses — emergency response and search-and-rescue, where a robot that can recover quickly from a mistake or react to a fast-changing scene is not just more efficient but more capable.

The work carries institutional weight. The senior author is Song Han, an associate professor in MIT's Department of Electrical Engineering and Computer Science and a member of the Research Laboratory of Electronics, whose lab has built a reputation for making AI models faster and cheaper to run. Co-lead author Yufei Sun is a student at Tsinghua University, with additional collaborators at Nvidia, UC Berkeley, UC San Diego, and Caltech. The research is supported in part by the MIT-IBM Computing Research Lab, Amazon, the National Science Foundation, and Nvidia, and will be presented at the IEEE/RSJ International Conference on Intelligent Robots and Systems.

## What to watch next

Han is already looking past this version. "This work sets up a good foundation for efficient, fast, accelerated, and low-cost robotics applications," he said. "We look forward to expanding our work into the latest world action models, so it has even stronger capabilities as we keep pushing to make physical AI faster."

That next step is the tell. VLASH predicts the robot's own future position but stops short of predicting the future state of the surrounding environment. The team wants to pair it with so-called world models — systems that forecast what the robot will actually see next, not just where its own limbs will land. If they succeed, robots would be planning not only around their own anticipated motion but around a moving, changing world. The pauses that make today's robots look like they are second-guessing themselves may soon be a relic of the demo era.
