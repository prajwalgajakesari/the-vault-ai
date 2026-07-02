Verkada, the cloud-based physical security company whose cameras, badge readers and environmental sensors watch over 30,000 organizations in 170 countries, has taken an investment from Nvidia and signed a technical partnership with the chipmaker — a deal aimed at accelerating the artificial intelligence running across its 2.4 million connected devices. Announced July 1, the collaboration folds one of the largest fleets of enterprise cameras on the planet into Nvidia's fast-growing push to move AI out of the data center and into the buildings, factories and storefronts where people actually work.

The size of Nvidia's stake was not disclosed. But the timing is telling. It arrives roughly seven months after Verkada raised money at a $5.8 billion valuation in a round led by CapitalG, the growth arm of Google parent Alphabet, and around the time the company crossed $1 billion in annualized bookings. Nvidia now joins the cap table as a strategic investor with an obvious interest: turning years of accumulated camera footage into training fuel for what the industry has started calling "physical AI."

## From surveillance to spatial reasoning

The technical core of the deal rests on two Nvidia products. The first is the Cosmos family of world foundation models — systems trained to understand physical space, motion and cause-and-effect rather than just text or static images. The second is Nvidia's Physical AI Data Factory, a toolkit used in part to generate synthetic footage that fills gaps in real-world training data, so a model can learn to recognize a rare safety incident it may have seen only a handful of times.

Verkada is applying both to the unglamorous but valuable problem of video search: finding a specific person, object or moment across thousands of hours of recordings. Since the collaboration began, the company says it has improved the mean average precision of its AI-powered search by 68% for spatial-temporal understanding — a benchmark measuring how accurately a system pinpoints not just what happened, but where and when.

"Verkada has been building and deploying Physical AI before the term existed," said Filip Kaliszan, co-founder and CEO of Verkada. "With our footprint of more than 2.4 million devices across 170 countries and 30,000 organizations, we've proven that the built environment is one of the largest beneficiaries of AI."

He framed the partnership as an accelerant rather than a pivot. "Working with NVIDIA supercharges what we've spent nearly a decade building: AI that keeps students safe in schools, protects workers on factory floors, helps retailers prevent theft, and enables organizations to operate more efficiently."

Beyond search, Verkada says it is building a multi-model search agent that draws on several models at once, and testing reasoning models for harder calls — the kind that require reading a scene rather than matching a label. The company points to two use cases in particular: spotting a health-and-safety incident on a manufacturing floor, and detecting shrinkage, the industry term for retail theft.

## Why Nvidia wants a foothold in the built environment

For Nvidia, the investment fits a pattern. Over the past two years the company has aggressively courted robotics, autonomous-driving and factory-automation customers, pushing its Cosmos models and a stack of developer tools while backing a run of startups building on its chips. A company like Verkada — sitting on an enormous, continuously refreshed store of real-world visual data — is close to an ideal partner. Cameras and access systems are becoming AI endpoints that interpret spaces, flag anomalies and automate operational decisions, and Nvidia wants its silicon and models underneath as many of them as possible.

The broader signal is that physical AI is graduating from robotics labs into ordinary commercial infrastructure. Tesla is reframing itself around Optimus robots; defense startups are pouring money into autonomy; and now enterprise security cameras are being recast as reasoning machines. Each deployment turns a passive sensor into an active interpreter of the world around it.

## The governance question surveillance can't dodge

That shift is exactly where the harder questions begin. A camera that merely records is a very different thing from one that infers intent, tracks behavior across a site and triggers automated action. As these systems move from retrieval ("find this person in the footage") toward reasoning ("decide whether this scene is a threat"), the stakes around accuracy, bias and oversight climb sharply. A false positive is no longer a bad search result; it can become an accusation.

Verkada carries a specific reminder of the risk. In 2021, hackers breached live feeds from roughly 150,000 of the company's cameras, gaining access to footage from hospitals, schools and workplaces. Layering more capable, more autonomous AI on top of that same infrastructure raises the ceiling on both usefulness and potential harm. The use of synthetic training data adds another wrinkle: models partly taught on machine-generated scenarios must still perform reliably on messy, real human behavior, and regulators have shown little patience for opaque decision-making in surveillance contexts.

Enterprise governance is the pressure point. Companies buying these systems will need clear answers on where inference happens, how long data is retained, who can query it, and what recourse exists when the model is wrong. None of that is solved by a faster search benchmark.

## What to watch

Three things will indicate whether this is a durable shift or a well-timed press release. First, whether Verkada ships the reasoning and agentic-search features it is testing into general availability — and how transparently it discloses their error rates. Second, whether Nvidia's undisclosed stake is a one-off or the template for a wave of similar investments in sensor-rich enterprise companies, from access control to building management. Third, and most consequential, whether regulators and enterprise buyers force governance standards for autonomous physical AI before the technology is widely deployed, rather than after the first high-profile failure. The cameras are already watching. The open question is how much they will be allowed to decide.
