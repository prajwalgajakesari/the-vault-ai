# Sony's 'Ace' Robot Can Beat Pros at Table Tennis — and It's a Real-World AI Milestone

A robot leaned into a topspin serve, tracked the ball across a regulation table in a fraction of the time a human eye can, and put the shot away for a clean point. Then it did it again — 16 times, against players who train 20 hours a week and some who rank among the best on the planet. Sony AI is calling the system "Ace," and it says the machine is the first autonomous robot to beat elite and professional-level humans at a competitive physical sport under official rules.

The claim, published on the cover of *Nature* under the title "Outplaying elite table tennis players with an autonomous robot," is a landmark for a field that has spent decades watching AI conquer chess boards and video games while stumbling in the messy, millisecond-paced physical world. Table tennis, it turns out, is one of the hardest possible tests: fast, adversarial, full of spin, and played at the very edge of human reaction time.

"This research has shown that an autonomous robot can, in fact, win at a competitive sport, matching or exceeding the reaction time and decision making of humans in a physical space," said Peter Dürr, Director of Sony AI in Zürich and project lead for Ace. "Table tennis is a game of enormous complexity that requires split-second decisions as well as speed and power."

## What Ace actually did

For the results reported in *Nature* (652, 886–891, 2026), Sony AI pitted Ace against five elite players and two professionals under International Table Tennis Federation (ITTF) regulations. The robot won three of its five matches against the elite group and stayed competitive in the rest. More striking than the win-loss record was the aggression: Ace scored 16 direct points off its serve — "aces" — against elite opponents, who managed only eight against the machine collectively.

The team kept playing after the manuscript was submitted. In December 2025 matches against four new opponents, Ace beat both elite players and one of two professionals, losing only to the second pro. In March 2026, against three fresh professionals, it beat all three at least once — a group that included Miyuu Kihara, at the time a top-25 player in the World Table Tennis women's singles rankings. Sony says the later matches showed higher shot speeds, more aggressive placement near the table edge, and faster rallies, suggesting the system was still improving under real competitive pressure.

## The engineering behind the speed

The core problem in table tennis is time. Elite human players react to an incoming ball in roughly 230 milliseconds. Ace runs its full sense-decide-act loop in about 20.2 milliseconds end to end, with perception alone taking roughly 10.2 ms — an order of magnitude faster than a person.

That speed comes from a purpose-built sensing stack. Ace uses nine active-pixel-sensor cameras built around Sony Semiconductor Solutions' IMX273 image sensors to pin down the ball's 3D position, tracking it at 200 Hz with millimeter accuracy. To read spin — long the Achilles' heel of table-tennis robots — the system adds three gaze-control units built on IMX636 event-based vision sensors, paired with pan/tilt mirrors and tunable telephoto lenses, measuring angular velocity at up to 700 Hz. The payoff: Ace returned balls with spins up to 450 rad/s at better than a 75% return rate, far exceeding previously reported figures for competitive robots.

The decision-making is a model-free reinforcement-learning controller, trained entirely in simulation and then transferred directly to the physical robot with no additional fine-tuning — a zero-shot sim-to-real leap that is notoriously fragile at these speeds. In testing, that generalization held up even on freak events the simulator never explicitly taught, like returning balls that ricocheted off the net.

## Why it matters

For decades, AI's most famous victories have been virtual. Deep Blue toppled Garry Kasparov in 1997; AlphaGo beat Lee Sedol in 2016; agents have since mastered StarCraft, Dota, and — from Sony AI's own labs — Gran Turismo racing with the superhuman Gran Turismo Sophy. All of those triumphs happened in domains where the world is perfectly observable and the clock can, if needed, be paused. The physical world offers no such mercy.

Ace matters because it collapses perception, planning, and control into a real, moving, adversarial environment where a single late millisecond means a lost point. The event-based vision and zero-shot sim-to-real transfer are the load-bearing advances here: they show a policy learned in simulation can survive contact with real photons, real spin, and a real opponent trying to beat it. That is the exact gap that has kept robotics lagging behind digital AI.

"This breakthrough is much bigger than table tennis," said Peter Stone, Chief Scientist at Sony AI. "It represents a landmark moment in AI research, showing, for the first time, that an AI system can perceive, reason, and act effectively in complex, rapidly changing real-world environments that demand precision and speed. Once AI can operate at an expert human level under these conditions, it opens the door to an entirely new class of real-world applications that were previously out of reach."

It is worth keeping the result in proportion. Ace is a fixed, table-side installation with nine cameras and specialized optics — not a general-purpose humanoid, and not something you can drop into a warehouse tomorrow. Prior table-tennis robots mostly demonstrated cooperative rallying; none had surpassed even amateur competitive play. Ace's leap is real, but it is a leap in a tightly scoped, richly instrumented setting.

## What to watch

The open questions are about transfer. Can the perception-and-control approach behind Ace move from a bespoke rig to cheaper, more general hardware? Sony frames the work as groundwork for AI that operates in "safety-critical settings" and real-time human interaction — language that points toward robotics beyond sport. Watch for the details Sony promises on its dedicated project site, for independent researchers probing whether the sim-to-real recipe generalizes to other high-speed tasks, and for how elite human players adapt now that they have game tape on a robot that serves aces faster than they can blink.
