## Light learns a trick electrons have monopolized

Eighty years after Penn engineers switched on ENIAC and launched the electronic computing era, physicists at the same university are trying to take part of computing back from the electron. In a paper published in *Physical Review Letters*, a team led by Bo Zhen has demonstrated a way to make light do something it is notoriously bad at: flip a switch. Their tool is a hybrid light-matter particle called an exciton-polariton, and the demonstration hints at a future in which AI chips compute with photons end to end, sidestepping one of the technology's fastest-growing problems, its appetite for electricity.

The result is a laboratory demonstration, not a product. But it targets a real and specific bottleneck in photonic computing, and the energy figure attached to it is striking.

## Why photons need a partner

Electrons have run computing for decades precisely because they interact strongly with one another and with materials. That same property is their liability: pushing charge through a chip generates heat and resistance, and both get worse as transistors multiply and AI models balloon. Light has the opposite profile. Photons are fast, lossless over distance, and the backbone of modern communications, but they are almost antisocial.

"Because they are charge-neutral and have zero rest mass, photons can carry information quickly over long distances with minimal loss, dominating communications technology," said Li He, co-first author of the study and a former postdoctoral researcher in the Zhen Lab who is now an assistant professor at Montana State University. "But that neutrality means they barely interact with their environment, making them bad at the sort of signal-switching logic that computers depend on."

That is the crux of the field's problem. Many experimental photonic chips already perform the linear math at the heart of neural networks, the multiply-and-add operations, at the speed of light. But the nonlinear steps, the decision-like "activation" operations between layers, generally force the signal back into the electronic domain and then back to light again. Every round trip costs time and energy and erodes the advantage of going optical in the first place.

## Making light interact with light

Zhen's team attacked the interaction problem directly. They built a nanoscale optical cavity around an atomically thin, gate-tunable semiconductor and coupled the trapped light so tightly to the material's electronic excitations that the two merged into a single quasiparticle, the exciton-polariton. The result is part photon, part matter: it inherits light's speed but borrows matter's willingness to interact. That borrowed sociability is enough for one optical signal to switch another, no detour through electronics required.

The energy number is what makes physicists look twice. The team reported all-light switching at roughly four quadrillionths of a joule, about four femtojoules, far less than it takes to briefly light a tiny LED. If that efficiency survives the trip from a single device to a working circuit, all-optical nonlinear operations could become cheap enough to keep computation in the light domain through an entire neural-network layer.

## A candidate answer to AI's power problem, with caveats

The context is hard to overstate. Data centers running large AI models are straining grids and reshaping energy planning, and the industry is openly hunting for hardware that breaks the link between more capability and more power. Photonic and analog approaches are among the most discussed escape routes, and a femtojoule-scale, all-optical nonlinearity is exactly the kind of missing ingredient those architectures have lacked.

The honest caveats are equally large. This is a single, gate-tunable device demonstrated in a lab, not a fabricated chip. The leap from one polariton cavity to a manufacturable, room-temperature-stable, densely integrated array is the part where many promising optical-computing results have historically stalled. Scaling is the work, and the researchers say so plainly. Exciton-polariton systems can be finicky about temperature and material quality, and matching the density and yield of silicon manufacturing is a tall order. None of the speed-and-energy benefits reach an AI workload until those engineering problems are solved.

## What to watch

The study, authored by Zhi Wang, Bumho Kim, Zhen and He and supported by the US Office of Naval Research and the Sloan Foundation, is best read as a physics milestone with a clear application in its sights. The questions that will decide its fate are concrete: Can the switching hold up when many of these cavities are wired together? Does the femtojoule efficiency survive integration and operation outside a cryostat? And can the platform be built with processes a foundry can actually run at volume? If the answers trend positive over the next few years, light-matter particles could move from a striking demonstration toward the photonic accelerators that AI's energy math increasingly demands. For now, the result is a credible proof of principle, and a reminder that the most interesting computing ideas sometimes come from physicists rethinking what a particle can do.