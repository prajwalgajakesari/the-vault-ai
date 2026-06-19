# Midjourney Unveils Its First Hardware Product: A 60-Second Full-Body Ultrasound Scanner

*The Vault — AI Edition · Business · June 18, 2026*

The company best known for conjuring photorealistic images from text prompts now wants to image something far more personal: the inside of your body. On June 18, 2026, Midjourney announced its first piece of hardware and an entirely new division to house it — Midjourney Medical — built around a full-body ultrasound scanner that founder David Holz says will eventually map a human body, down to a fraction of a millimeter, in roughly 60 seconds without radiation or magnetic fields.

The pivot from generative art to medical imaging is jarring on its face, and the financial claims are bold: Midjourney says the device will ultimately be about 10 times cheaper and 60 times faster than an MRI. But the most important detail in the announcement is one the headline omits. The current prototype takes roughly 20 minutes per scan, has been used on about a dozen people, runs without any AI in its imaging pipeline, and carries no FDA clearance to diagnose anything.

## What was actually announced

The Midjourney Scanner is a whole-body ultrasound computed tomography (USCT) device — a decades-old imaging approach that surrounds the body with a ring of ultrasonic transducers submerged in water. Unlike a conventional handheld ultrasound probe that captures 2D cross-sections, USCT fires sound from every angle at once and reconstructs a full 3D volume. The user steps onto a motorized platform that descends slowly into a shallow pool of warm water; as the body passes through a roughly 70-centimeter ring, transducers emit pulses and record the returning echoes.

The hardware is not Midjourney's own. The system's imaging chips are licensed from Butterfly Network (NASDAQ: BFLY), the publicly traded medical device maker whose Ultrasound-on-Chip technology replaces traditional piezoelectric crystals with capacitive micromachined transducers etched directly onto standard semiconductor wafers. Each chip carries thousands of individual elements; the current Midjourney configuration uses 40 Butterfly modules per system, totaling roughly 358,000 sensing elements and drawing on about 2 petaflops of compute to reconstruct the images.

That co-development and licensing deal was disclosed long before this week's reveal. In a Form 8-K filed with the SEC on November 17, 2025, Butterfly outlined a five-year agreement with Midjourney worth up to $74 million, including a $15 million upfront payment and annual licensing fees. Investors reacted to the public unveiling immediately: Butterfly's shares jumped on the news as Wall Street absorbed the prospect of a high-profile new outlet for its chips.

## The numbers, and the gap between claim and reality

The 60-second figure is a target, not a measured result. Midjourney's engineers describe a data bottleneck: a scan generates an enormous torrent of raw acoustic data — on the order of 17 gigabytes per second — and the prototype cannot yet move and reconstruct that data fast enough to finish in under a minute. The roadmap calls for a second-generation design within about a year and a third-generation scanner using fully custom, Midjourney-designed silicon by 2028, the point at which the company says capabilities will be "night-and-day" different.

Holz was unusually candid about the prototype's limits at the San Francisco launch. "We're not even using any AI in this yet, just really cool hardware and software," he said, per Bloomberg — a striking admission from a company whose entire brand is AI. He nonetheless framed the device's potential in superlative terms, calling it "in many ways superior to even MRI machines." Neither the 60-second claim nor the MRI comparison has been independently verified by a radiologist or medical institution.

Leading the engineering is Ahmad Abbas, who joined Midjourney after running hardware engineering on Apple's Vision Pro. His team is small — roughly nine people — which is itself the crux of the skeptics' argument: a tiny group that has never built or operated a regulated medical device is attempting to cross the very large gap between a working bench prototype and a deployed, cleared scanner.

## Why this matters

Strip away the brand whiplash and Midjourney is making a serious bet on a real technology. The physics of USCT are well understood, the Butterfly partnership supplies a credible hardware foundation, and Holz disclosed the prototype's shortcomings more openly than most founders do at a product launch. Butterfly, for its part, is leaning in. "We're proud to support Midjourney's mission to democratize access to personal imaging data," said Joseph DeVivo, Butterfly's president, CEO and chairman, in a statement responding to the announcement — a comment that doubles as validation of the underlying chips and a hedge that keeps the medical claims firmly on Midjourney's side of the ledger.

The go-to-market strategy is where the ambition becomes audacious. Midjourney plans to sidestep hospitals entirely, opening a chain of "Midjourney Spa" wellness centers — the first in San Francisco's Union Square by the end of 2027 — where a body scan is positioned as a side effect of a visit that also includes saunas and cold plunges. By framing the output as "body composition maps" rather than diagnoses, Midjourney can operate under the FDA's general wellness lane, the same path used by whole-body MRI providers like Prenuvo and Ezra, while accumulating the longitudinal dataset it would need to pursue diagnostic clearance later.

That clinical caution is warranted, because the medical case for scanning healthy people at scale is genuinely unsettled. Research on whole-body screening of asymptomatic people consistently finds incidental findings in 20 to 40 percent of scans, only a small fraction of which require treatment. Midjourney's stated ambition — more than 50,000 scanners and one billion scans per month — would, at those rates, generate hundreds of millions of ambiguous results monthly, each demanding follow-up and interpretation. The company's claim that early imaging at this scale could avoid 30 percent of deaths and half of all healthcare costs is not supported by peer-reviewed evidence.

## What to watch next

The near-term signals are concrete: whether Midjourney's second-generation hardware actually compresses scan time toward the 60-second goal over the next 12 months; whether the FDA discussions Holz says are already underway produce any clearance pathway; and whether independent radiologists, once given access, confirm that the scanner's images rival MRI for clinical use rather than just looking the part. For Butterfly investors, the durable question is whether this week's stock pop reflects real, recurring chip demand or simply the halo of a buzzy partner. And for everyone else, the test is the one every preventive-screening venture eventually faces — not whether the machine can see inside you in a minute, but whether knowing what it finds actually makes you healthier.

---

### Sources

- [Bloomberg — AI Startup Midjourney Pivots to Health With Ultrasound Machine](https://www.bloomberg.com/news/articles/2026-06-18/ai-startup-midjourney-pivots-to-health-with-ultrasound-machine)
- [PYMNTS — Midjourney Enters Medical Imaging With 60-Second Full-Body Scan](https://www.pymnts.com/news/artificial-intelligence/2026/midjourney-enters-medical-imaging-with-60-second-full-body-scan/)
- [AuntMinnie — Midjourney Unveils Planned Ultrasound Scanner With Help From Butterfly](https://www.auntminnie.com/clinical-news/ultrasound/news/15828012/midjourney-unveils-planned-ultrasound-scanner-with-help-from-butterfly)
- [Yahoo Finance — Butterfly Network Shares Jump on Midjourney News](https://finance.yahoo.com/healthcare/articles/butterfly-network-shares-jump-midjourney-135650233.html)
- [Tech Times — Midjourney Full-Body Ultrasound Scanner Targets MRI Speed, But Prototype Runs 20 Minutes](https://www.techtimes.com/articles/318628/20260618/midjourney-full-body-ultrasound-scanner-targets-mri-speed-prototype-runs-20-minutes.htm)
- [Business Wire — Butterfly Network Provides Commentary on Midjourney Medical's Full Body Ultrasound Scanner Announcement](https://www.businesswire.com/news/home/20260618923795/en/Butterfly-Network-Provides-Commentary-on-Midjourney-Medicals-Full-Body-Ultrasound-Scanner-Announcement)
- [Engadget — Midjourney is developing a full-body ultrasonic scanner](https://www.engadget.com/2196998/midjourney-full-body-ultrasonic-scanner/)
