# Second Wave of Author Copyright Suits Targets OpenAI, Anthropic, Meta After Bartz Settlement

A coordinated second wave of copyright litigation landed on the major AI labs this month, with plaintiffs' firms filing at least four new putative class actions between April 3 and April 17 on behalf of authors, journalists, and screenwriters. The defendants are familiar. OpenAI, Anthropic, Meta, and, for the first time at this scale, Cohere. But the legal architecture is sharper than the first-generation complaints that followed Authors Guild v. OpenAI and Kadrey v. Meta in 2023.

The lead case, Whitehead et al. v. OpenAI, was filed April 8 in the Southern District of New York on behalf of a proposed class of more than 1,200 nonfiction authors. A parallel action, Nguyen v. Anthropic, landed April 14 in the Northern District of California and explicitly invokes the $1.5 billion settlement in Bartz v. Anthropic as a floor, not a ceiling, for damages. A third suit, filed in the District of Delaware, is the first to name model weights themselves as an unlawful derivative work, a theory that, if accepted, would reach far beyond training-time conduct.

## What Has Changed Since the First Wave

The first wave, anchored by NYT v. OpenAI, Bartz v. Anthropic, Kadrey v. Silverman, and Silverman v. OpenAI, largely asked whether ingesting copyrighted books to train large language models was itself infringement. Judge William Alsup's June 2025 ruling in Bartz answered that question unevenly: training on lawfully acquired books was transformative fair use, but Anthropic's use of a pirated shadow library was not. Anthropic settled the piracy piece for approximately $1.5 billion in September 2025, working out to roughly $3,000 per infringed work across the certified class.

The new complaints are built on what that ruling left open. Rather than relitigating whether training is fair use in the abstract, plaintiffs are advancing three narrower theories. First, they argue that Bartz's fair-use holding is limited to cleanly sourced corpora and does not protect any model whose training data provenance cannot be audited. Second, they press output-similarity claims, citing memorization studies and prompt-engineered reproductions of copyrighted passages to allege that the models themselves are infringing artifacts. Third, and most aggressively, they plead violations of Section 1202 of the Digital Millennium Copyright Act, alleging the defendants stripped copyright management information, author names, ISBNs, license notices, from ingested works.

## The DMCA 1202 Turn

The DMCA 1202 theory is the connective tissue across the April filings. Courts have historically been skeptical of CMI-removal claims in the AI context; Judge Vince Chhabria dismissed a version of it in Kadrey in 2023. But the new complaints marshal forensic evidence from leaked training manifests and researcher testimony to argue that labs systematically scrubbed metadata before tokenization. Statutory damages under 1202 run from $2,500 to $25,000 per act of removal, and plaintiffs' counsel are pleading them on a per-work, per-copy basis. On a corpus of several million books, that arithmetic becomes existential.

## Settlement Posture and Training Economics

None of the April defendants have indicated willingness to settle on Bartz-like terms. Anthropic's posture is complicated by the fact that it has already paid; OpenAI and Meta, which have so far avoided a dispositive loss, are expected to litigate aggressively through summary judgment. Still, the Bartz settlement has changed the negotiating anchor. Plaintiffs are no longer asking whether training is infringement, they are asking what it is worth per book.

If any of the April cases produces a plaintiff-favorable ruling on either output similarity or DMCA 1202, the downstream effect on training economics would be significant. A $3,000-per-work floor applied to the roughly seven million books in common research corpora implies exposure in the low tens of billions of dollars per defendant, before any DMCA multiplier. That math is why licensing deals with HarperCollins, News Corp, and the Associated Press accelerated through 2025, and why the frontier labs have quietly begun indemnifying enterprise customers against training-data claims.

The cases are in their earliest phase, with motions to dismiss expected by July. But the second wave has already accomplished something the first did not: it has priced the risk.
