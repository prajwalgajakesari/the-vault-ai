## xAI Sues California Over Training-Data Disclosure Law, Citing the Constitution

When Elon Musk's xAI walked into federal court in the final days of 2025, it was not arguing about safety guardrails, deepfakes, or any of the harms that usually animate AI legislation. It was arguing about secrets — specifically, the company's claim that California cannot constitutionally force it to reveal what went into Grok.

On Dec. 29, 2025, xAI filed suit against California Attorney General Rob Bonta in the U.S. District Court for the Central District of California, asking the court to block enforcement of **Assembly Bill 2013**, the state's Generative Artificial Intelligence Training Data Transparency Act. The law took effect just three days later, on Jan. 1, 2026. In the months since, the case — captioned *X.AI LLC v. Bonta* — has become the sharpest test yet of a question that will shape the next decade of AI policy: how much of an AI model's inner workings the government can compel a developer to make public.

## What AB 2013 Actually Requires

Passed unanimously by both chambers of the California legislature and signed in September 2024, AB 2013 requires developers of generative AI systems made available to Californians to publish a "high-level summary" of the datasets used to train their models. That summary must cover the sources and owners of the data, whether it includes copyrighted, trademarked, or public-domain material, whether it contains personal information as defined by the California Consumer Privacy Act, the timeframe over which the data was collected, and whether synthetic data was used.

The disclosures must be posted on a developer's website before a covered system is released, and updated whenever the model is substantially modified. Notably, the statute does not define what "high-level" means, contains no compliance-and-enforcement mechanism beyond the attorney general's general authority, and — crucially for xAI's argument — includes no carve-out to protect trade secrets.

## xAI's Constitutional Case

xAI's complaint frames AB 2013 not as a modest transparency rule but as an existential threat to the value of its models. The datasets used to build a frontier system, the company argues, are painstakingly curated to confer a competitive edge, and "these datasets are valuable precisely because they are not public." Strip away that secrecy through a mandated disclosure, and you hand rivals a map to the company's most expensive work product.

The complaint calls AB 2013 "a trade-secrets-destroying disclosure regime" that both exposes proprietary information and compels xAI "to speak when it would rather not." From that premise, the company built three constitutional claims: a **First Amendment** compelled-speech theory; a **Fourteenth Amendment** due-process challenge attacking the law's vagueness; and, most novel, a **Fifth Amendment Takings Clause** argument — that forcing public disclosure of trade-secret information amounts to an uncompensated taking of private property.

That last theory leans on *Ruckelshaus v. Monsanto*, the 1984 Supreme Court decision holding that trade secrets count as "private property" for Takings Clause purposes. As Micah Musser, an NYU law student and former research analyst at Georgetown's Center for Security and Emerging Technology, wrote in **Lawfare** on June 12, 2026, the doctrine here is genuinely unsettled. "Whether intellectual property counts as 'private property' within the meaning of the Takings Clause is not exactly clear," Musser noted, observing that only once — in the First Circuit's *Philip Morris v. Reilly* — has a court ever struck down an entire statute on the grounds that it took trade secrets without compensation.

## An Early Loss, and an Appeal

xAI's opening gambit failed. In early March 2026, U.S. District Judge Jesus Bernal denied the company's motion for a preliminary injunction, finding it had not shown it was likely to succeed on the merits. The court's reasoning was pointed: the high-level, categorical disclosures AB 2013 actually demands do not obviously threaten any trade secret. Knowing that a model was trained on, say, licensed news archives or web-crawled text is a far cry from handing over the curated dataset itself.

That distinction matters for the broader fight. As Musser put it, the ruling "is likely not the end of this particular legal theory." Regulators reach for disclosure mandates precisely because they are easier to draft than substantive performance rules, "and eventually some of those disclosure mandates will become granular enough to threaten trade secrets, even if that was not true of the very high-level information mandated under AB 2013." xAI has appealed the denial to the U.S. Court of Appeals for the Ninth Circuit, where the case now sits.

## Why AI Makes This Fight Different

The trade-secret stakes are unusually high for AI companies because, for them, secrecy is often the *only* protection available. The U.S. Copyright Office has taken the position that AI outputs are uncopyrightable, and model weights — the product of a mathematical training process rather than human authorship — fall outside copyright entirely. Patents cover only narrowly definable inventions, not the data-curation and tuning know-how that actually drives model quality. That leaves trade-secret law as the load-bearing wall.

And AI is uniquely vulnerable to reverse engineering. Techniques like model distillation can let a competitor clone a model's behavior from its outputs alone; membership-inference attacks can reveal whether specific data was in a training set; and even high-level disclosures about collection methods can enable data-poisoning attacks. Those technical realities give developers a real, not merely rhetorical, interest in controlling what they reveal — which is exactly why this case resonates well beyond xAI.

## The Federal-vs-State Backdrop

The lawsuit lands in the middle of 2026's escalating fight over who gets to regulate AI. With substantive federal legislation stalled, states have filled the vacuum with transparency-first laws: AB 2013 on training data, SB 53's frontier-model safety disclosures, and a growing patchwork elsewhere. xAI is challenging that patchwork on multiple fronts at once — on April 9, 2026, the company filed a parallel complaint against Colorado Attorney General Philip Weiser seeking to enjoin the Colorado AI Act on similar constitutional grounds.

That two-state offensive signals a deliberate strategy: rather than comply with a thicket of divergent state mandates, xAI is betting it can get courts — and the Constitution — to do the preemption work that Congress has not. If the Ninth Circuit embraces even a narrow version of the Takings or compelled-speech theory, the IAPP warned, the case "could still set a precedent that invalidates or, at the very least, defangs all kinds of transparency laws across the nation."

## What to Watch Next

The immediate action is at the Ninth Circuit, where xAI's appeal will test whether AB 2013's high-level disclosures survive First Amendment and Takings scrutiny. A ruling for California would embolden state legislators already drafting more granular mandates; a ruling for xAI could freeze the transparency movement at exactly the moment it has become lawmakers' default tool. Watch, too, for how the Colorado case develops, and whether other developers join the constitutional offensive or quietly comply. The deeper question Musser raised remains open: as disclosure rules grow more detailed, where exactly does legitimate public transparency end and an unconstitutional taking of corporate secrets begin? For now, no court has drawn that line — and the answer may decide how much the public ever learns about what is inside the models reshaping daily life.
