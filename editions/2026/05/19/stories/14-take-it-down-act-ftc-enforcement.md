---
headline: "Take It Down Act Reaches Full Enforcement as FTC Gains Power to Fine $53,000 Per Violation"
slug: take-it-down-act-ftc-enforcement
category: policy
story_number: "14"
date: 2026-05-19
---

# Take It Down Act Reaches Full Enforcement as FTC Gains Power to Fine $53,000 Per Violation

A year ago today, President Donald Trump signed the Take It Down Act in the White House Rose Garden with Paris Hilton standing nearby — a rare bipartisan moment in which Congress passed landmark legislation nearly unanimously to criminalize the non-consensual publication of intimate imagery, including AI-generated deepfakes. As of this morning, May 19, 2026, that law has entered its second and harder phase: platforms that fail to remove flagged content within 48 hours now face civil penalties of $53,088 per violation, enforced by the Federal Trade Commission.

The transition is not symbolic. On May 11, FTC Chairman Andrew Ferguson sent formal compliance letters to more than a dozen of the largest technology companies in the world — Alphabet, Amazon, Apple, Automattic, Bumble, Discord, Match Group, Meta, Microsoft, Pinterest, Reddit, SmugMug, Snapchat, TikTok, and X — putting each on direct notice that the agency is prepared to pursue enforcement actions against any platform that has not built the required removal infrastructure. The FTC published detailed compliance guidance the same week, specifying the technical and procedural obligations that covered platforms must now satisfy. The grace period is over.

## What Platforms Must Now Do

Section 3 of the Take It Down Act — the provision the FTC enforces — applies to any platform that primarily hosts user-generated content or that regularly publishes, curates, hosts, or distributes nonconsensual intimate visual depictions as part of its business. That scope deliberately reaches across social media services, video and image hosts, messaging apps, and gaming platforms. The obligations are specific and non-negotiable.

Covered platforms must maintain a removal request mechanism accessible without a platform account, meaning any victim can file regardless of whether they use the service. A valid request must include the requester's signature, information sufficient to locate the content, a good-faith statement that the content was published without consent, and the victim's contact information. Once a valid request is received, the platform has 48 hours to remove the reported image or video and all known identical copies across every layer of its storage infrastructure — primary databases, content delivery networks, thumbnail caches, backup snapshots. The 48-hour window applies to the entire infrastructure, not just the originally reported instance.

The FTC's guidance further recommends that platforms deploy perceptual hash matching to prevent re-uploads of known harmful content, and encourages participation in existing industry hash-sharing networks: the National Center for Missing and Exploited Children's Take It Down service for content involving minors, and StopNCII.org for adult victims.

## The Penalty Arithmetic

The $53,088 figure is not arbitrary — it is the current statutory maximum for civil penalty violations under the FTC Act, adjusted for inflation, and it applies per violation. For a platform hosting multiple copies of a single flagged image across its CDN infrastructure, that multiplication effect is immediate. A platform that receives a valid removal request, fails to act within 48 hours, and is later found to have harbored even a handful of instances of the reported content faces potential exposure in the hundreds of thousands of dollars on a single complaint — before any pattern of non-compliance triggers broader enforcement scrutiny.

The Center for Democracy and Technology's Becca Branum, director of the organization's Free Expression Project, identified the downstream effect of that calculus plainly. "If you think there's any given post where if you ask an attorney, 'Is it worth $53,000 for me to keep this post up,' the answer is always going to be take it down," Branum told CyberScoop. "I can't imagine any service wanting to risk that type of fine on edge cases or anything they can't verify or account for within 48 hours."

That dynamic — the financial incentive to remove anything that arrives through the complaint pipeline — is simultaneously the law's enforcement mechanism and its central civil liberties tension.

## The AI Dimension: Why Deepfakes Change the Compliance Problem

The Take It Down Act covers both authentic intimate imagery and "digital forgeries," the law's term for AI-generated or digitally manipulated depictions. That coverage arrives at a moment when the scale of AI-generated nonconsensual intimate imagery has reached levels that were unimaginable when earlier revenge-porn statutes were drafted.

Between 96 and 98 percent of all deepfake content online consists of nonconsensual intimate imagery, with 99 to 100 percent of victims being women. The number of deepfake image files online is projected to reach approximately 8 million in 2025, up from 500,000 in 2023. The Internet Watch Foundation documented a 260-fold increase in AI-generated child sexual abuse videos between 2024 and 2025 alone. In January 2026, Grok — xAI's AI assistant embedded in X — was found generating sexualized deepfakes of real people at scale, triggering criminal and civil investigations of X and its parent company and demonstrating in live production what the worst-case scenario for AI-enabled NCII distribution looks like.

For platforms, AI-generated content creates a distinct technical compliance challenge. Traditional hash-matching systems work by generating digital fingerprints of known harmful files and blocking re-uploads that match exactly. AI-generated images, however, may be produced on demand and never stored anywhere until the moment of creation — meaning perceptual similarity matching, which recognizes near-identical images rather than byte-identical files, becomes a necessary component. Smaller platforms without dedicated trust-and-safety engineering teams face the steepest climb: the 48-hour requirement applies equally regardless of a platform's size, and there is no small-platform exemption in the statute.

## An Early Conviction — and Unresolved Deterrence

The criminal provision of the Take It Down Act, which took effect immediately when Trump signed the law in May 2025, produced its first federal conviction in April 2026. An Ohio man who used AI to generate nonconsensual intimate imagery of neighbors — including children — and distribute it on a child sexual abuse material website was found guilty under the statute. Sentences under the Act carry up to two years imprisonment for content depicting adults and three years for content involving minors.

Whether the law is actually reducing the underlying harm, however, remains contested. Research published this month by Princeton postdoctoral fellow Alejandro Cuevas examined activity across two major online forums with millions of registered users each, and found that the supply of and demand for deepfake pornography actually increased after the Take It Down Act's passage — the opposite of the deterrent effect the law's architects intended. "Despite federal-level criminalization, the supply and demand for AI-generated NCII only grew in 2025," Cuevas wrote at TechPolicy.Press. One hypothesis is that the law's publicity introduced new users to deepfake communities; another is that displaced users from shuttered platforms simply migrated to less-scrutinized venues.

## The First Amendment Problem Platforms Are Watching

The Take It Down Act passed 409 to 2 in the House and by unanimous consent in the Senate, but near-unanimity in Congress does not resolve the legal challenges that are expected to follow enforcement. The Electronic Frontier Foundation has argued that the law's notice-and-removal mechanism applies to a broader category of content than its own narrow nonconsensual intimate imagery definitions, and that — unlike the Digital Millennium Copyright Act — it contains no penalty for false or bad-faith removal requests, no requirement for a statement under penalty of perjury, and no counter-notice mechanism through which a person whose content was wrongly removed can seek reinstatement. "The law contains no protections against frivolous or bad-faith takedown requests," EFF staff attorneys India McKinney and Joe Mullin wrote. "Lawful content — including satire, journalism, and political speech — could be wrongly censored."

The law also does not amend Section 230 of the Communications Decency Act, which has historically shielded platforms from liability for user-generated content. Legal scholars expect First Amendment challenges and contested questions about whether FTC enforcement actions under the Take It Down Act can survive Section 230 defenses — meaning the compliance infrastructure platforms are now required to build may face judicial scrutiny before its effectiveness can be fully assessed.

For victims, those legal debates are secondary. Any person who believes nonconsensual intimate imagery depicting them has been published on a covered platform — real or AI-generated — can now file a removal request without holding an account on that platform. The platform has 48 hours to act. If it does not, the FTC has the authority to investigate and fine. The first year of the Take It Down Act established the criminal prohibition. Year two establishes whether platform accountability has teeth.

---

*Sources: [TechTimes](https://www.techtimes.com/articles/316848/20260519/ftc-can-fine-platforms-53088-per-deepfake-left-after-48-hours-starting-today.htm) | [Fisher Phillips](https://www.fisherphillips.com/en/news-insights/new-federal-ai-deepfake-law-takes-effect.html) | [TechPolicy.Press](https://www.techpolicy.press/its-too-soon-to-tell-if-the-take-it-down-act-is-working/) | [FTC Compliance Guidance](https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act) | [FTC Enforcement Press Release](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act) | [Wiley Law](https://www.wiley.law/alert-May-19-Deadline-for-TAKE-IT-DOWN-Act-Compliance-Is-Your-Company-Prepared) | [CyberScoop](https://cyberscoop.com/ftc-take-it-down-act-enforcement-deepfakes/)*
