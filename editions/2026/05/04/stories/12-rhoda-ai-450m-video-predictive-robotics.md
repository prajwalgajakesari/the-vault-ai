---
headline: "Rhoda AI Exits Stealth With $450 Million to Train Robots From Video Using Direct Video Action Models"
slug: rhoda-ai-450m-video-predictive-robotics
category: research
story_number: "12"
date: 2026-05-04
---

# Rhoda AI Exits Stealth With $450 Million to Train Robots From Video Using Direct Video Action Models

After eighteen months of secretive development, Palo Alto-based Rhoda AI has emerged from stealth with a $450 million Series A round at a $1.7 billion valuation -- and a bold claim that the key to making robots work in messy, unpredictable factories was hiding in plain sight on the internet all along.

## The Pitch: Learn Physics From YouTube, Not Just Robot Labs

Founded by Jagdeep Singh, the serial entrepreneur who previously co-founded and led solid-state battery maker QuantumScape through its public listing, Rhoda is betting that the chronic fragility of industrial robots stems from a data problem. Traditional approaches train robot models on painstakingly collected teleoperation demonstrations -- a human physically guiding a robot arm through every motion it needs to learn. The method works in controlled lab settings but breaks down the moment real-world conditions shift: a part arrives at a slightly different angle, lighting changes on the factory floor, or a bin of components is stacked differently than expected.

Rhoda's answer is what it calls FutureVision, a platform built on proprietary Direct Video Action (DVA) models. Instead of relying primarily on robot-specific trajectory data, Rhoda pre-trains its models on hundreds of millions of publicly available internet videos -- everything from cooking tutorials to machining demonstrations -- to build a foundational understanding of motion, physics, and physical interaction. The system is then fine-tuned on smaller quantities of actual robot data to learn embodiment-specific behaviors.

"One of the most underestimated problems in robotics is generalization from lab to real world," Singh said. "A system that works perfectly in the former can fail with minor changes that come with the latter -- slightly different orientation, slightly different lighting, slightly different layout."

## How DVA Works in Practice

The DVA architecture bridges perception and control in a continuous closed loop. The system observes its environment, predicts future visual states as video frames, converts those predictions into motor actions, executes them, and then re-observes the world -- repeating this cycle every few hundred milliseconds. Unlike open-loop approaches that generate a full plan and execute it without ongoing feedback, DVA updates its behavior dynamically as conditions change, enabling what Rhoda describes as physics-aware control in real time.

The results are already tangible. In a recent high-volume manufacturing evaluation with an automotive partner, Rhoda's system completed a component-processing workflow in under two minutes per cycle using off-the-shelf robotic hardware, without human intervention -- exceeding the customer's own performance targets. The company says the test was conducted in a live production environment where materials, layouts, and workflows changed continuously, precisely the kind of variability that trips up conventionally trained systems.

Singh has been candid about the long-term ambition. "In the fullness of time, we think what we're doing transforms the future of work," he told interviewer Alejandro Cremades. "These robots are general purpose and they're intended to basically do any task. Now we're starting out in the near term with a very specific focus on manufacturing and logistics tasks because those are tasks that we think customers are actually willing to pay for today."

## The Money and the Backers

The $450 million Series A -- one of the largest early-stage rounds in robotics history -- was led by Premji Invest, the investment arm of Wipro founder Azim Premji. The investor roster reads like a who's who of deep-tech venture capital: Khosla Ventures, Singapore sovereign wealth fund Temasek Holdings, Capricorn Investment Group, Mayfield, Leitmotif, Matter Venture Partners, Prelude Ventures, and Xora. Legendary venture capitalist John Doerr also participated personally.

The valuation and round size place Rhoda squarely alongside Physical Intelligence, which raised $400 million in late 2024, and other heavily funded robotics AI startups jockeying to become the default intelligence layer for industrial automation. Rhoda plans to license its AI models to customers rather than build and sell its own hardware, a capital-light strategy that could accelerate deployment across different robot form factors and manufacturers.

## Why It Matters

The robotics industry has long suffered from a simulation-to-reality gap: systems that perform flawlessly in digital twins and laboratory demos routinely stumble in actual factories. Rhoda's video-first training philosophy represents a fundamentally different bet -- that the cheapest, most abundant source of physics data is not simulation or teleoperation but the billions of hours of real-world video already uploaded to the internet. If DVA models can reliably transfer that visual intuition into motor control, the implications extend well beyond manufacturing into logistics, agriculture, construction, and eventually household robotics.

The approach also sidesteps one of the field's most painful bottlenecks. Collecting high-quality teleoperation data is slow, expensive, and scales poorly. By shifting the bulk of learning to freely available video and reserving robot-specific data for the final fine-tuning step, Rhoda could dramatically reduce the time and cost required to teach a robot a new task -- a critical advantage in high-mix manufacturing environments where product lines change frequently.

## What to Watch Next

Rhoda has not disclosed specific customer names beyond its automotive evaluation partner, and the company has yet to publish peer-reviewed benchmarks comparing DVA against competing architectures such as diffusion policies or vision-language-action models. Independent validation will be essential for the field to gauge whether FutureVision's real-world performance holds up across a wider range of tasks, environments, and robot platforms. For now, Rhoda has the funding, the pedigree, and a technically distinctive approach -- the question is whether internet video can truly teach a robot to work.
