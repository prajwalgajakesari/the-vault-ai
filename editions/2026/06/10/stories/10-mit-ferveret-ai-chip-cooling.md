# The MIT startup that wants to cool AI's chips with no water and a nuclear reactor's playbook

The artificial intelligence boom has a thermodynamics problem. Every chatbot reply, every generated image, every model trained at scale produces heat — and getting rid of that heat now consumes roughly a third of the electricity flowing into AI data centers. A startup spun out of MIT thinks the fix has been hiding inside nuclear reactors all along.

Ferveret, founded by former MIT postdoc Reza Azizian and Matteo Bucci, MIT's Esther and Harold E. Edgerton Associate Professor in the Department of Nuclear Science and Engineering, says it can cool the chips that run AI models using no water and significantly less electricity. MIT News profiled the company on June 10, 2026, describing a system that adapts a phenomenon from reactor cooling — called subcooled boiling — to the racks of GPUs powering the AI industry.

The pitch lands at a pointed moment. Data centers are projected to account for anywhere from 9 to 17 percent of total U.S. electricity usage by the end of the decade, according to figures cited by MIT, and cooling is one of the heaviest hidden costs inside them.

## How it works

Ferveret's approach, which it calls Adaptive Phase Cooling (APC), submerges servers in a specialized liquid that pulls heat away far more efficiently than the fans most facilities still rely on. Immersion cooling itself is not new — the most effective versions bring the liquid to a boil, because the phase change from liquid to vapor absorbs enormous amounts of energy. What sets Ferveret apart, the company says, is the size and behavior of the bubbles.

"Liquid is a better heat transfer medium than air. That's why when you stick your hand into room temperature water it still feels cold," Bucci explains. "When liquid is boiling, it becomes even better at removing heat because the phase change requires a lot of energy, which is the energy you remove from the chip. That lets you transfer large quantities of heat with minimal temperature differences between the chips and the liquid."

The trouble with boiling is the bubbles themselves, which force operators to capture and reliquefy vapor while juggling pressure, temperature, and fluid levels. Ferveret's liquid has a low boiling point and, the company says, none of the toxic PFAS "forever chemicals" that some rival approaches use. At the chip's surface it produces much smaller bubbles that detach more frequently and quickly recondense into the surrounding liquid — accelerating what the founders describe as the bubble-rewetting cycle that hastens heat transfer.

Rather than the large tanks typical of immersion cooling, Ferveret packages its system into small modular boxes, each housing a single server, along with control software that tunes the power going to each box in real time.

"The physics enable us to get to form factors that weren't possible in the past," Azizian says, noting that the rack-mounted design is meant to slot into existing infrastructure rather than require a wholesale rebuild.

## The numbers, with a caveat

In a study conducted with the Samueli Computer Science Department at UCLA, Ferveret reported that its APC solution delivered a 15 percent improvement in computational power efficiency compared with state-of-the-art liquid cooling. Layered with its power-control software, the company says data centers can extract 35 percent more tokens — the small units of text or data AI models produce — from the same amount of power.

These figures come from Ferveret itself and a collaborating university lab, not from independent third-party benchmarking, so they are best read as the company's own results rather than settled industry consensus. Ferveret says it is already testing with data center developer CleanSpark, AI accelerator firm FuriosaAI, and Switch, one of the largest U.S. data center operators.

## Why it matters

The cooling bottleneck is increasingly the bottleneck for AI itself. As chipmakers cram more transistors onto each processor to wring more computing out of constrained power supplies, the heat density climbs and old-fashioned air cooling struggles to keep up. Azizian says he was floored the first time he walked into a data center in 2017.

"I thought, 'Holy crap, this is not how you cool facilities,'" he recalls, noting that air cooling can still consume 40 percent of the power entering a data center. "It was not an efficient way of doing things, but since it wasn't hurting the performance, no one cared that the cooling technology was 50 years old."

Water is the other constraint. Many cooling systems evaporate large volumes of it, putting data centers in direct competition with communities and agriculture in already-stressed regions. A water-free system changes where data centers can plausibly be built.

"The sun shines in places where you don't have much water, so the advantage of us being water-free is we allow you to build data centers where you have solar energy but nothing to cool the data center down," Bucci says. He frames it as opening up Africa, the Middle East, and parts of America to facilities that could not otherwise be sited there — "a huge unlock," in his words.

## What to watch

Ferveret is part of Nvidia's Inception startup program and says it is in talks with the hyperscale cloud companies that dominate AI infrastructure. The founders say they plan to announce expanded partnerships later this year, which will be the real test of whether the technology moves from pilot deployments to production scale.

Two things are worth tracking. First, whether independent, third-party validation confirms the 15 and 35 percent efficiency gains the company has reported internally. Second, whether the modular, water-free design holds up at the density and reliability hyperscalers demand. As Azizian puts it, the industry's appetite for power and water "will only become more limiting as the industry grows." Ferveret is betting the next era of AI will be won not just on smarter chips, but on smarter ways to keep them cool.
