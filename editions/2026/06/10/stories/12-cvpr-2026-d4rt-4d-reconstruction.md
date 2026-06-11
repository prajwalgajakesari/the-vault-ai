# A Faster Way to See the World in Motion: D4RT Takes CVPR 2026's Top Honor

When a self-driving car rounds a corner or a robot reaches for a moving object, it has to do something humans manage effortlessly and machines find brutally hard: understand a three-dimensional world that is also changing through time. On June 9, 2026, the IEEE Computer Society and the Computer Vision Foundation named the research that pushes that frontier furthest this year, awarding the CVPR 2026 Best Paper to a method called D4RT that reconstructs the geometry and motion of dynamic scenes directly from ordinary video.

The paper, "Efficiently Reconstructing Dynamic Scenes One D4RT at a Time," comes from a team spanning Google DeepMind, University College London, and the University of Oxford. According to the official announcement, the award was selected after a review process that yielded 4,089 accepted papers from 16,092 submissions. The winners were unveiled at the conference Welcome and Awards Ceremony on June 5, with CVPR 2026 running June 3 to 7 at the Colorado Convention Center in Denver.

## What "4D reconstruction" actually means

The "4D" in D4RT is shorthand for three dimensions of space plus one of time. Traditional 3D reconstruction takes images of a static scene and infers its shape, building a model you could walk around inside. But the real world rarely holds still. People walk, cars drive, hands grasp, leaves blow. Reconstructing a *dynamic* scene means recovering not just where every surface sits in space, but how each point moves from one moment to the next, all while the camera itself may be moving too.

That combination is what makes the problem so hard. The system has to untangle several unknowns at once: the depth of each pixel, how points correspond across frames as objects shift, and the camera's own position and motion. Historically, researchers attacked these as separate tasks, often with heavy, specialized components that made the process computationally expensive and slow to scale.

D4RT collapses that complexity into a single unified transformer-based architecture. Per the announcement, the model jointly estimates depth, spatio-temporal correspondence, and full camera parameters, and exposes a unified interface that lets it "independently and efficiently probe the 3D position of any point in space and time." The award write-up frames this as a lightweight and highly scalable approach that enables "remarkably efficient training and inference." Coverage of the work has cited dramatic speedups over prior state-of-the-art systems, though readers should treat specific multipliers as reported figures pending the published paper rather than settled benchmarks.

The authors listed on the official release include Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, and Mehdi S. M. Sajjadi.

## The company it keeps

D4RT shared the spotlight with a strong slate of other honored work. The Best Student Paper went to "Native and Compact Structured Latents for 3D Generation," from a team at Tsinghua University, Microsoft Research, the University of Science and Technology of China, and Microsoft AI. Built around a new representation the authors call O-Voxel, it sharpens the quality and realism of AI-generated 3D assets.

Among the Best Paper Honorable Mentions, Meta Superintelligence Labs earned recognition for "SAM 3D: 3Dfy Anything in Images," a generative model that predicts an object's geometry, texture, and layout from a single photo and, per the announcement, won human-preference comparisons against recent work by at least a 5-to-1 margin. A second honorable mention, "NitroGen: An Open Foundation Model for Generalist Gaming Agents," involving researchers from NVIDIA, Stanford, Caltech, the University of Chicago, and UT Austin, trained a vision-action model on 40,000 hours of gameplay across more than 1,000 games.

CVPR's program co-chairs framed the cohort as pointing toward the field's near future. "The award-winning papers this year exemplify the innovation and technical excellence that continue to drive the field forward," said Alexander G. Schwing of the University of Illinois Urbana-Champaign, a CVPR 2026 Program Co-Chair, noting advances "from dynamic scene reconstruction to breakthroughs in 3D generative modeling." Fellow co-chair Chen Change Loy of Nanyang Technological University added that the selected papers "introduce concepts and practices that undoubtedly will help shape the next generation of computer vision systems and applications."

## Why it matters

The thread running through these winners is machines that build usable models of the physical world from raw sensors. For robotics, a fast, unified way to recover scene geometry and motion is foundational: a manipulator or mobile robot needs to know not just what is in front of it but how it is moving in order to plan and act. The same capability underpins autonomous driving, where understanding a dynamic street scene in near real time is a safety requirement, not a luxury.

Beyond embodied systems, efficient 4D reconstruction feeds into augmented and virtual reality, where capturing a moving real scene and rendering it convincingly is the core challenge, and into the broader push toward "world models" that simulate how environments evolve. By making the geometry-and-motion problem dramatically cheaper to train and run, D4RT lowers a barrier that has long kept these applications confined to controlled settings or heavy compute budgets.

## What to watch

The immediate questions are practical. Will D4RT's efficiency claims hold up across messy, in-the-wild video, and how quickly will the approach show up in open implementations and downstream systems? Watch, too, for how a unified-transformer recipe interacts with the 3D-generation advances honored alongside it, since reconstruction and generation increasingly look like two sides of the same world-modeling coin. With CVPR 2027 already slated for Seattle, the trajectory from this year's awards suggests the next race is less about reconstructing the world than about predicting where it is headed next.
