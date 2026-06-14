Europe is not waiting for legal consensus. With a €250 million fine against Google and a court order forcing OpenAI to purge unlicensed song lyrics from German servers, regulators and judges across the continent are making clear that generative AI's free ride on copyrighted content is over — and the bill is overdue.

## The French Fine: €250 Million and a Broken Commitment

On March 20, 2024, France's Autorité de la Concurrence announced a €250 million penalty against Google and Alphabet — the sharpest financial sanction yet targeting AI training on news publishers' content. The case's roots predate generative AI: a 2019 EU copyright reform extended protections to news snippets, and Google had entered 2022 commitments with the Autorité to negotiate fairly and keep publishers informed about content use.

What the regulator found was that Google had fed publishers' articles into the training pipeline for Bard — later rebranded Gemini — without notifying rights holders and without offering any opt-out that did not also strip publishers from Google Search.

"The Autorité considers that Google has breached its commitment #1 by failing to inform publishers that their content had been used to train Bard," the authority wrote in its press release. The regulator also noted that the core copyright question — whether AI training on news content falls under neighboring rights — "has not been answered just yet," leaving the door open for future enforcement.

Google accepted a fast-tracked settlement and did not contest the findings. Its managing director for news partnerships, Sulina Connal, was blunt: "The fine is not proportionate to issues raised." Google launched a dedicated opt-out tool, Google-Extended, in September 2023 — but by then the damage to its standing with the Autorité was done.

## The German Ruling: Cease, Delete, and Publish

Seven months later, on November 11, 2025, Munich went further.

The Regional Court of Munich I issued a landmark judgment in GEMA v. OpenAI (Case No. 42 O 14139/24) — the first ruling in Europe to hold an AI developer directly liable for copyright infringement in both the training and output phases of a language model. GEMA, Germany's performing rights organization, brought the suit over nine well-known songs whose lyrics, including "Atemlos durch die Nacht" and "Über den Wolken," could be reproduced in full by ChatGPT through simple prompts.

The court rejected every technical defense OpenAI offered. It confirmed that the model had memorized the lyrics outright — not merely learned statistical patterns — and found two distinct acts of infringement: reproduction inside the model's parameters (§16 UrhG) and public communication when ChatGPT output those lyrics on request (§19a UrhG). The EU's text and data mining exception under §44b UrhG was found inapplicable: permanent memorization inside model weights is not the transient copy the exception was designed to cover, particularly after GEMA had expressly exercised its opt-out under the DSM Directive.

The injunction ordered OpenAI to cease storing unlicensed German lyrics on German infrastructure. The court also required the judgment to be published in a local newspaper — a traditional German copyright remedy. "These decisions are more than legal milestones," wrote analysts at Norton Rose Fulbright. "They signal a new era where AI innovation must coexist with robust IP protection."

OpenAI had declined to negotiate a licensing deal with GEMA ahead of the ruling. That posture is growing harder to sustain as the judgment reverberates into mid-2026.

## The Legal Framework: TDM Exceptions, Opt-Outs, and the AI Act

The DSM Directive of 2019 sits beneath both cases. Article 4 creates a broad TDM exception allowing anyone to mine lawfully accessible content — but it also grants rights holders the power to opt out, collapsing the exception entirely once that reservation is exercised. The Munich court's ruling sharpened the point: memorization that persists inside model weights is permanent reproduction, not transient analysis.

The EU AI Act, whose training-data obligations for general-purpose AI providers came into force in August 2025, adds another layer. Article 53 requires GPAI providers to publish a "sufficiently detailed summary" of training data and document how opt-outs were handled — an evidentiary paper trail that will prove essential in future litigation.

## Europe vs. the United States

The transatlantic gap has rarely been clearer. American courts apply the fair use doctrine — an open-ended, four-factor balancing test with no opt-out mechanism and no disclosure requirement. Multiple high-profile cases remain unresolved in the US.

Europe has no fair use equivalent. Its TDM exception carries a hard opt-out right and, under the AI Act, affirmative disclosure duties. The Munich court's rejection of "statistical correlation" arguments — the claim that model weights do not truly "store" protected text — signals that European judges will examine the underlying engineering rather than accept industry framing. AI companies with European users are already renegotiating licensing terms and auditing datasets.

## What to Watch

The GEMA v. OpenAI judgment is not yet final; appeals are expected, and a referral to the Court of Justice of the EU could harmonize standards across member states. The European Commission's mandatory GPAI training-data disclosure template, released in early 2026, is generating the first wave of public summaries from major model providers — and national AI offices are already scrutinizing them for gaps. GEMA has framed the Munich ruling as the opening of licensing talks, not their conclusion.

For Google, the French fine closed a chapter — but the question of whether AI training on news content falls within the TDM exception remains open. For OpenAI, the German injunction carries a live compliance clock. For every lab with European users, the message is uniform: Europe has decided that training data is not a commons, and it has the tools to enforce that view.
