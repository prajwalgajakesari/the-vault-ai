# Two Automated Systems, One Case: AI Searched 80,000 Cameras, Then AI Wrote the Report

The police report documenting one of the most contested surveillance episodes of the past two years ends with a line of boilerplate: "I acknowledge this report was generated using Draft One by Axon."

That sentence, reported Wednesday, September 2, by 404 Media's Jason Koebler, closes a loop AI accountability researchers have described in the abstract since 2024. In Johnson County, Texas, one automated system searched for a woman across a nationwide license plate camera network. A second helped write the official record of what happened. Neither leaves a trail an outside reviewer could use to reconstruct what it did.

404 Media first reported in May 2025 that a Johnson County deputy searched Flock Safety's national ALPR network for a woman who had self-administered an abortion. The search log gave the reason as "had an abortion, search for female." Accounts at the time put the cameras queried at more than 80,000; the Illinois Secretary of State's office, which opened a statewide audit in response, has cited more than 83,000.

## What the New Documents Show

The AI-generated incident report was obtained by Cameron Probert of the Tri-City Herald and shared with 404 Media. Sergeant Damien Bethel used Draft One — Axon's tool that turns body-worn camera audio into a draft narrative — to write his portion of the file, including a summary of a legal discussion among deputies.

"Deputies discussed the legal implications of the situation, noting that while the girlfriend self-administered the abortion pill, there were no criminal charges applicable under current Texas law," the report states, per 404 Media. It adds that deputies "also considered the possibility of a civil lawsuit against the pharmaceutical company that supplied the pill." No further detail is given.

The document confirms primary evidence exists: body-worn camera footage in the Axon Evidence library, in-car footage, and still images. The sheriff's office has repeatedly declined to release it, including to records requests from 404 Media and the Electronic Frontier Foundation. The AI-assisted summary is, for now, the public record — and the audio behind it is unavailable for comparison.

A separate section by the deputy who ran the Flock queries calls the search a welfare check: "I entered the vehicle into FLOCK to see if we could see where the victim and her children might be at." 404 Media reports he never visited her home.

Keven George of the sheriff's office defended the workflow without addressing case specifics. "Officers remain fully in control of the final report: they review and edit the draft, fill in missing details, and approve it before submission," he told 404 Media, adding that "the Deputy has to digitally sign before the narrative can be used." Flock spokesperson Paris Lewbel said the report "details that authorities explicitly stated she could NOT be charged with a crime." CEO Garrett Langley has told customers the search was requested by a worried family — a claim 404 Media says the reports contradict. Axon has not addressed this report.

## The Audit Problem

That disclosure line matters because it is often the only searchable artifact Draft One leaves behind.

An EFF investigation published in July 2025 by Matthew Guariglia and Dave Maass concluded the product "seems deliberately designed to avoid audits." Draft One does not retain the initial AI draft; once an officer copies the text out and closes the window, no version history distinguishes machine-written sentences from human edits. At an Axon roundtable reviewed by EFF, a senior generative AI product manager put it plainly: "So we don't store the original draft and that's by design and that's really because the last thing we want to do is create more disclosure headaches for our customers and our attorney's offices."

Departments requiring the disclosure can at least find their AI-assisted reports; Lafayette, Indiana, which does not, told EFF: "we do not have the ability to create a list of reports created through Draft One. They are not searchable."

Prosecutors have drawn lines. King County, Washington's prosecuting attorney told police in 2024 it would not accept AI-assisted narratives: "We do not fear advances in technology — but we do have legitimate concerns about some of the products on the market now." Utah's SB 180, effective May 2025, requires a disclaimer and accuracy certification. California's SB 524 would require the first draft be kept as long as the final report — a condition Draft One cannot meet.

## Why This Matters

Chained automation is the story. Each link looks defensible alone: an ALPR query is a lead-generation tool, an AI drafting assistant is a paperwork tool, a human signs at the end.

But the audit surfaces do not chain. Flock's log captures a free-text reason typed by the officer — which is how "had an abortion, search for female" became public, and also why the recorded reason can diverge from the one offered later. Draft One captures that a request was made and a disclosure signed, but not what the model wrote. Neither produces an artifact usable to test the other.

Auditability here means something narrower than transparency: the ability to reconstruct who or what asserted a fact, and on what basis. A signature attests that an officer approved a narrative. It does not establish which sentences the officer wrote. When the source audio is withheld and the draft is never retained, an AI-assisted report becomes an unfalsifiable account of a search whose own justification is disputed. Forbes reported in July 2026 that Axon's AI tools sometimes introduce errors officers must remove — errors that, by design, leave no fingerprint.

## What to Watch

Three threads. Whether Johnson County releases the body-camera footage its own AI-drafted report says exists — the only way to check the summary against the source. Whether **SB 524** advances in California with draft retention intact. And whether the Illinois audit becomes a template elsewhere. The first two would make AI-written reports checkable; the third would make network searches checkable. Neither, alone, closes the gap between them.
