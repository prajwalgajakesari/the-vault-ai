---
headline: "Omen AI Raises $31M to Watch Data Center Coolant and Predict Hardware Failures"
slug: omen-ai-31m-datacenter-coolant
category: business
story_number: "04"
date: 2026-07-06
---

# Omen AI Raises $31M to Watch Data Center Coolant and Predict Hardware Failures

The most valuable machines of the AI era are being kept alive by water, and almost nobody is watching the water. That is the bet behind Omen AI, a San Francisco startup that on June 30 said it had raised a $31 million Series A to slip tiny spectrometers directly into the liquid-cooling loops of AI data centers, reading the chemistry of the coolant in real time to catch failures before a rack ever goes dark.

The round was led by Nava Ventures, with participation from CRV, Vanderbilt University, filtration giant Mann+Hummel, Starhill Holdings, and Hard Launch Capital, alongside personal checks from executives at Bridgestone, GM, Johnson Controls, and AI cloud provider TensorWave. It brings Omen's total raised to roughly $40 million since the company was founded in 2024.

## The problem hiding in the coolant

As operators cram more GPUs into every rack to build ever-larger training clusters, the chips run hotter, and the fluid keeping them from cooking becomes a liability. Liquid coolant is typically a blend of water and an additive that suppresses bacteria. To pull more heat away, data center managers can shift the mix toward more water, which absorbs heat better but is far friendlier to microbial growth and the kind of contamination that clogs the flow.

When a loop fouls, the fix is a flush, which can mean shutting a rack down for five or six hours. In a facility full of high-end accelerators, that downtime can cost millions of dollars. The industry's default diagnostic is almost quaint by comparison: draw a fluid sample, mail it to a lab, and wait for results that arrive long after a problem has taken hold.

"You're not risking huge amounts of downtime because you have no insight into what's going on chemically," said Omen CEO and founder Zach Laberge.

## What Omen actually sells

Omen's core product is a small spectrometer that sits inline in the coolant loop and reports continuously on what is happening chemically, tracking more than 21 elemental signatures. It watches for bacterial growth, for traces of copper and chromium that signal pumps and components wearing out, and for silicon that suggests seals are beginning to fail. The company also offers a portable diagnostic unit for on-the-spot checks.

The pitch is predictive maintenance: if the fluid running through a system carries the health signal of the whole machine, then reading that fluid continuously turns coolant into an early-warning system rather than a post-mortem. Omen markets its sensors as a one-time, non-invasive installation that connects directly to a machine's fluid system, whether that fluid is coolant, oil, or water.

The company says it already works with data center operators representing $200 billion in assets and between 10 and 14 gigawatts of capacity, and is deployed with about a dozen data center customers as it scales. Among them is TensorWave, which is building an AI compute cloud on AMD chips and whose executives also invested in the round.

"The fluid running through these massive systems is a critical variable that most of the industry is flying blind on," said Piotr Tomasik, TensorWave's president. "Omen sees the future of infrastructure exactly the way we do, better monitoring to optimally support compute customers."

## From bulldozers to data centers

Omen did not start out chasing GPUs. Laberge founded his first company in 2020 at age 14, raising $3 million to install sensors on construction equipment before dropping out of high school. After that venture wound down, he launched Omen in 2024 with the same underlying idea: fluid systems are the key to making heavy machinery smart enough to know when it needs to be fixed.

Caterpillar dealerships became early customers on the heavy-equipment side. But Cat also supplies gas turbines and generators that provide on-site power for data centers, and about six months ago dealers began asking Laberge whether Omen could do anything "on the building side of things." Those buildings, it turned out, are full of fluid, from HVAC to chip cooling, and a fast-growing customer base came with them.

"It's rare to see such a young founder who has the respect of established, large corporations in a space that moves a bit more slowly," said Cory Rellas, a partner at Nava Ventures who now sits on Omen's board. "Much of our diligence came through our introductions with large customers, which quickly validated their approach."

## Why now

Omen's timing rides two curves. The first is the sheer scale of the AI infrastructure buildout, where hyperscalers and neoclouds are pouring hundreds of billions of dollars into GPU capacity and where uptime translates directly into revenue. The second is the shift to liquid cooling itself. Air cooling simply cannot keep pace with the thermal density of the latest accelerators, pushing direct-to-chip and immersion cooling from niche to necessity, and with that shift comes a brand-new category of failure mode that legacy monitoring never had to consider.

Laberge credits recent advances in optical hardware and signal processing for making the approach viable. "Hardware is just cheap enough that it makes sense to play at scale, and then signal processing lets us make more sense out of the noise," he said.

Omen is not entirely alone. Pyxis, an established water-monitoring firm, rolled out its own data center coolant monitoring product earlier in June, a sign that continuous, on-premises fluid analytics is emerging as a distinct segment of the cooling stack rather than a one-company curiosity.

## What to watch next

The open questions are about scale and standardization. Can Omen convert a dozen deployments and $200 billion in monitored assets into recurring, facility-wide contracts as new liquid-cooled campuses come online through 2026 and 2027? Will hyperscalers treat inline fluid intelligence as a must-have layer or leave it to specialist neoclouds like TensorWave? And as competitors such as Pyxis crowd in, the edge may shift from having a sensor in the loop to owning the data and the predictive models that make sense of it. If coolant chemistry becomes a standard telemetry stream for AI infrastructure, the startup that got there first, selling shovels for the water rather than the gold, could end up with a durable position in one of the fastest-growing corners of the compute economy.
