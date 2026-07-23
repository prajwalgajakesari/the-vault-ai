For years, putting lidar on a chip has run into the same wall: shrink the sensor to a fingernail-sized slab of silicon, and its field of view collapses. A spinning mechanical lidar can sweep a full circle around a car; a solid-state chip could only peer through a narrow keyhole. MIT engineers say they have now pried that keyhole open — not with better lasers or software, but by giving the chip's tiny light-emitting antennas different shapes.

In a paper published May 7 in *Nature Communications*, a team from MIT's Research Laboratory of Electronics reported a redesigned antenna array that lets a silicon-photonics lidar chip scan a much wider, cleaner field of view with no moving parts, tackling a trade-off that has hobbled chip-based lidar for years.

"The functionality we demonstrated in this work solves a fundamental problem for integrated optical-phased-array technology, enabling future lidar sensors that can achieve significantly higher performance than we could demonstrate previously," said Jelena Notaros, the Robert J. Shillman Career Development Associate Professor of Electrical Engineering and Computer Science at MIT and the paper's senior author.

## The grating-lobe trap

Lidar builds a 3D map by firing rapid pulses of infrared light and timing their reflections. Traditional units aim mechanically — the familiar spinning canister on a self-driving car's roof. Those systems work, but they are bulky, expensive, and full of moving parts that wear out.

Silicon photonics offers an alternative: a semiconductor chip that steers light electronically, using a system called an integrated optical phased array, or OPA. The chip carries a row of tiny antennas, each etched with periodic corrugations that scatter light up and out of the chip. By tuning the phase of the light fed to each antenna, engineers can swing the beam across a scene with nothing physically moving.

The catch is geometry. To steer a beam across a wide angle, the antennas need to sit very close together. But pack identical antennas too tightly and they "couple" — their light bleeds into one another and the beam turns to mush. Space them farther apart, and the array starts emitting duplicate beams pointed in the wrong directions. These phantom copies, called grating lobes, cap how far the real beam can be steered before it becomes indistinguishable from its clones.

"This limits our field of view, so the autonomous vehicle now only knows what is in front of it for a certain angular range," said Andres Garcia Coleto, an EECS graduate student and co-author. The stray lobes can also trigger false positives and waste laser power.

## Antennas that ignore their neighbors

The MIT team's insight was to stop making every antenna identical. Lead author and EECS graduate student Henry Crawford-Eng and his colleagues designed three distinct antenna geometries, varying each one's width and the size and spacing of its corrugations. That gives each a different "propagation coefficient" — how light travels down its length.

The effect is a kind of mutual invisibility. "Because the antennas have very different propagation coefficients, when we put them close together, essentially each antenna doesn't 'see' the antenna next to it. Therefore, it won't couple with its neighbor," Garcia Coleto explained.

The hard part was making antennas that behave differently internally yet emit light identically to the outside world — the same brightness, the same beam angle for a given wavelength, and a uniform shift in that angle as the array is steered.

"We require the antennas to have different geometries to reduce the crosstalk, but we need to simultaneously design the antennas to have the same emission characteristics," Crawford-Eng said. "It is extremely difficult because, typically, when antennas are designed with different geometries, they tend to behave differently."

After working out the electromagnetic theory describing how the antennas' radiative modes interact, the researchers simulated and fabricated the array. In a conventional OPA with antennas packed that closely, coupling between neighbors would run near 100 percent; in the MIT design, it dropped to roughly 1 percent while the chip still produced a single, precise beam, steered across a wide field of view with no grating lobes.

## Why it matters

Lidar is one of the primary sensory feeds for machine perception, and AI systems are only as good as the data they are fed. An autonomous vehicle's neural networks can't reason about a pedestrian stepping off a curb in the periphery if the sensor never catches them. Mechanical lidar delivers wide coverage but at a cost — thousands of dollars per unit, physical fragility, and bulk. Solid-state lidar-on-a-chip flips that equation: it can be mass-produced in semiconductor foundries for a fraction of the price and has no moving parts to fail.

The missing piece has been field of view. A cheap, durable chip that can only see straight ahead is of limited use to a car watching its flanks, a drone mapping terrain below, or an AR headset tracking a room. By breaking the crosstalk-versus-coverage trade-off, the MIT work removes one of the last technical excuses for why solid-state lidar can't match its mechanical cousin, feeding richer, wider 3D data into the perception stacks that autonomy and robotics depend on — a reminder that gains in AI systems don't always come from bigger models, but sometimes from the physical layer.

## What to watch

The demonstration is a lab result, not a shipping product, and the field of view, while wider, is not yet a full panorama. Notaros's team plans to push the coverage further and is already chasing a second wide-angle approach it found while developing the theory. The bigger questions are commercial: whether the reduced-crosstalk design can be manufactured reliably at scale, integrated with the lasers and detectors a complete lidar needs, and hardened for the road.

Joyce Poon, a professor at the University of Toronto and director of the Max Planck Institute of Microstructure Physics who was not involved in the research, called it "an important step forward for chip-scale, solid-state beam-steering technology." Watch whether lidar startups and automotive suppliers — long promised affordable solid-state sensors that never quite arrived — begin licensing designs like this.
