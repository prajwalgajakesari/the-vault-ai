When a NASA telescope stares at the entire sky for more than a decade, it does not just count what it was built to find. Somewhere inside 200 billion rows of infrared data — collected by a mission designed to hunt asteroids — sat 1.5 million cosmic objects that no one had ever cataloged. It took a Pasadena high school student, six weeks of a summer program, and an AI model he built largely from scratch to pull them out of the noise.

Matteo Paz was a teenager at Pasadena High School when he designed the machine-learning pipeline that flagged those objects in archival data from NASA's now-retired Near-Earth Object Wide-field Infrared Survey Explorer, or **NEOWISE**. The work earned him the $250,000 first-place prize in the 2025 Regeneron Science Talent Search, and — unusually for a high schooler — a **single-author, peer-reviewed paper** in *The Astronomical Journal*, published in November 2024.

"The model I implemented can be used for other time domain studies in astronomy, and potentially anything else that comes in a temporal format," Paz said in a Caltech account of the project.

## From stargazing lectures to 200 billion data rows

Paz's path started early. His mother brought him to public Stargazing Lectures at the California Institute of Technology when he was in grade school. In the summer of 2022 he attended Caltech's Planet Finder Academy, and in 2023 he joined the institute's six-week Summer Research Connection, a program that pairs local high schoolers with campus mentors.

His mentor was **Davy Kirkpatrick**, an astronomer and senior scientist at Caltech's Infrared Processing and Analysis Center (IPAC). Kirkpatrick had a problem that no human could reasonably tackle by hand. NEOWISE had spent more than 10 years scanning the whole sky for asteroids, but along the way it repeatedly measured the changing infrared brightness of far more distant objects — quasars, exploding stars, and pairs of stars eclipsing one another. Astronomers call these **variable objects**, and their fluctuating light had never been systematically harvested from the mission's archive.

"At that point, we were creeping up towards 200 billion rows in the table of every single detection that we had made over the course of over a decade," Kirkpatrick said. His original plan was modest: take a small patch of sky, find a few variable stars by hand, and show the community what might be hiding in the full dataset.

Paz had no intention of doing it by hand.

## Building VARnet

Paz had picked up AI in a high school elective that blended coding, theoretical computer science, and formal mathematics. He was also years ahead in math — a product of Pasadena Unified's Math Academy, where students finish AP Calculus BC in eighth grade. That combination let him treat NEOWISE's messy, decade-long record as exactly the kind of vast, ordered dataset machine learning thrives on.

The result was a model he named **VARnet**. It pairs wavelet decomposition, which helps separate real signal from instrument noise, with a custom Fourier-transform technique for extracting the periodic features that betray a variable object. Trained to spot minute differences in the telescope's infrared measurements, VARnet processed the raw NEOWISE observations and flagged roughly **1.9 million sources**. About **1.5 million** of them had no match in existing catalogs — new targets, effectively invisible until the algorithm surfaced them.

The peer-reviewed methods paper describing VARnet appeared in *The Astronomical Journal*. The follow-up work — a full catalog of the variable NEOWISE sources, published under the name **VarWISE** — extended the effort into a resource other astronomers can mine directly.

Kirkpatrick, who grew up in a Tennessee farming community and credits a ninth-grade teacher with steering him toward astronomy, framed the mentorship as paying a debt forward. "If I see their potential, I want to make sure that they are reaching it," he said. On the night Paz won the Regeneron competition, he added: "That was the highest high I've ever had... when you've helped someone reach some of their potential and be acknowledged for it, it's a nice feeling."

## Why It Matters

The story is a vivid case study in two shifts reshaping science. The first is **the democratization of discovery**. Paz did not need a new telescope or a supercomputing grant — he needed access to public NASA data, a mentor willing to say "let's talk about that," and the mathematical fluency to build his own tool. The raw ingredients of a headline astronomical result are now, increasingly, within reach of a motivated student.

The second is **machine learning's growing indispensability for large sky surveys**. Modern astronomy has flipped from a data-scarce discipline to a data-drowning one. NEOWISE's 200 billion detections are a preview of what is coming: the Vera C. Rubin Observatory alone is expected to generate tens of terabytes nightly and alert on millions of changing objects. No human team can sift that by eye. Purpose-built models like VARnet — able to detect faint, subtly varying signals that standard software misses — are becoming the only practical way to convert survey archives into discoveries.

## What to Watch

The immediate question is how much science the VarWISE catalog yields now that 1.5 million candidate objects are open to the community for follow-up and classification. Watch, too, whether VARnet migrates beyond astronomy — Paz has floated its use for any time-series data, from stock charts to pollution cycles. And watch the template itself: a mentored high schooler, an untapped public dataset, and a homegrown AI model added up to a peer-reviewed paper and a quarter-million-dollar prize. As surveys like Rubin come online with orders of magnitude more data, expect that pattern to repeat.
