The most valuable real estate in AI hardware is a few millimeters wide. That is about as far as the copper wires linking a GPU to its high-bandwidth memory can reach. As a result, even Nvidia's best chips sit inside a small ring of memory stacks, and the size of that ring limits how fast a large model can generate text. On Thursday, San Francisco startup Volantis said it had raised $88 million to replace those wires with light.

The Series A was co-led by Lachy Groom, the Stripe veteran turned angel investor, and Abstract Ventures. John Doerr, VXI Capital, Triatomic and Susa Ventures also took part, according to Reuters. Angel investors include podcaster Dwarkesh Patel, former Intel AI chief Naveen Rao and Anthropic researcher Sholto Douglas. Volantis says it has raised $97 million in total, which includes a $9 million seed round announced when it came out of stealth in June 2025.

## Light Instead of Copper

Here is the problem Volantis wants to solve. A chip's compute cores can only work as fast as data arrives from memory, and that rate, called memory bandwidth, largely sets inference speed. Nvidia and AMD surround their processors with expensive HBM stacks. Reuters reported that even Nvidia's best current offerings fit only eight of them per GPU, because the electrical connections are so short. SiliconANGLE puts that range at about 5 millimeters.

Volantis says its optical links reach more than 200 millimeters across an interposer. That would leave room for more than 220 memory chiplets around a single processor. The company says the design delivers more than 30 times the memory bandwidth of current accelerators and uses less than one picojoule per bit.

The light comes from vertical-cavity surface-emitting lasers, or VCSELs. The parts are less exotic than they sound. As Reuters noted, they already power Face ID in hundreds of millions of iPhones, and Apple spent years building up their supply chain. VCSELs are usually cheaper and easier to make than the lasers used in optical networking. They can also be built on gallium arsenide, which is easier to get than the materials used for most miniature lasers. CEO and co-founder Tapa Ghosh argues that this is the point: Volantis is assembling well-understood parts, not betting on a breakthrough.

"Advanced packaging is always to be respected – it's never trivial – but it's not necessarily a new thing to do," Ghosh told Reuters. "No one is going to win a Nobel Prize if our project works, but the good news is, they won't need to."

## The A-1 Appliance

The chips will ship inside a data center inference appliance called the A-1, about a third the size of a standard server rack. Volantis says it will hold 10 terabytes of memory with 250 terabits per second of memory bandwidth. The company's target is up to 10,000 tokens per second per user on a model with 20 trillion parameters, which is far larger than today's public frontier models.

Ghosh described what that could mean for users in a blog post quoted by SiliconANGLE. "This will enable real-time frontier inference, restart scaling laws & enable entire code bases in context windows," he wrote. "As a starting point, imagine a coding agent that completes a task in 30 seconds rather than 30 minutes."

The team has worked on these technologies before. Co-founder and CTO Roy Meade led Micron's HBM program and was a vice president at Ayar Labs, according to RuntimeWire. Other engineers have worked at Nvidia, AMD and Broadcom, and their credits include the first commercial implementation of CoWoS, the TSMC packaging technique behind most modern AI accelerators. Ghosh is a Thiel Fellow and Y Combinator alum. He previously founded chip startup Vathys, and in a 2017 Stanford talk he argued that data movement, not computation, was the main source of inefficiency in deep-learning processors.

## Why It Matters

The AI industry's bottleneck has shifted. Training needed raw compute, but serving large reasoning models and long-running agents is limited by memory. Each generated token requires streaming model weights and a growing key-value cache out of memory. That is why HBM is now one of the scarcest and most profitable parts in the semiconductor supply chain, and why Micron, SK Hynix and Samsung have become central to AI capacity planning.

If Volantis can deliver even part of its claimed bandwidth, it would change the economics. Large models could run on one appliance instead of being split across racks of GPUs, and coding agents that now take minutes could respond in close to real time. The reliance on an iPhone-proven laser is also a supply chain bet. The company wants to avoid the shortages in advanced packaging and HBM that have constrained every major accelerator vendor.

Volantis is not the only startup chasing this. Photonics startups such as Ayar Labs, Lightmatter and Celestial AI have raised large sums to move data with light, though mostly between chips or between systems. Volantis is focused specifically on the link between processor and memory. That is a narrower target, but arguably a more valuable one.

## What to Watch

For now, every headline figure is a target. Volantis says one version of its technology has taped out, and Ghosh told Reuters the first chip is due next year. RuntimeWire reports that the first customer deliveries of the A-1 are planned for 2027. The key tests are whether working silicon matches the promised bandwidth and power, whether hundreds of memory chiplets can be packaged reliably at reasonable cost, and which hyperscaler or AI lab signs on as the first customer. Nvidia and AMD are also working on co-packaged optics, so Volantis needs to ship before its approach becomes a standard feature on the incumbents' roadmaps.
