# OpenAI Put ChatGPT Inside Epic's Charts. It Can Read 325 Million Patients and Write Nothing.

On Sept. 1, OpenAI crossed a line American health IT has spent a decade fortifying: it put a general-purpose chatbot inside the patient record. Healthcare organizations running Epic — the electronic health record system holding data on more than 325 million patients — can now connect those environments to ChatGPT for Healthcare, letting authorized clinicians pull appointment notes, laboratory results, medication lists and specialist documentation into a chat window. In supported deployments, ChatGPT sits directly in the Epic layout, so the clinician never leaves the chart.

The access runs one way. Nothing the model produces is written back to the record. That single design decision — read-only, no writes, ever — is the whole story, and it is doing an enormous amount of work.

OpenAI paired the Epic connection with a Healthcare Public Data plugin covering nine official sources, among them PubMed, DailyMed, RxNorm, CMS Coverage and ClinicalTrials.gov. The pitch is verification rather than recall: a pharmacy team confirming a drug label queries the authoritative record instead of trusting a model's memory. Organizations with a Business Associate Agreement can also run ChatGPT Work, Codex, apps and plugins in the same governed workspace.

The launch partner list is not small: AdventHealth, Baylor Scott & White Health, Boston Children's Hospital, Cedars-Sinai, HCA Healthcare, Memorial Sloan Kettering and UCSF. UCSF Health is serving as pilot partner, and its chief executive was careful about the framing.

"As a pilot partner, we're exploring how the new EHR integration with ChatGPT for Healthcare can help clinical teams understand what has changed and what matters most across a complex patient record," said Suresh Gunasekaran, president and CEO of UCSF Health. "By bringing relevant information together more quickly and comprehensively, the technology has the potential to reduce time spent synthesizing data and give clinicians more time with patients."

Every load-bearing word there is hedged. Exploring. Potential. Gunasekaran, a former hospital CIO himself, added that UCSF is engaging frontline teams to validate the capabilities in practice.

## The Numbers Behind the Claim

OpenAI says it partners with hundreds of physicians across 60 countries, 49 languages and 26 medical specialties, who have reviewed more than 700,000 model responses to date. For this release, physicians evaluated ChatGPT working with connected EHR context across 27 clinical use cases including pre-visit review, medication review and handoff summaries. Across 4,363 ratings, 99.1% were rated safe. Separately, across five public-data connectors, more than 93% of responses were rated "good" or better for accuracy, topping out at 98.6%.

Invert that figure and it reads differently. Roughly 39 of the 4,363 ratings did not clear the bar — in a workflow whose entire value proposition is that the clinician did not open the chart. The evaluations are also vendor-run on vendor-selected use cases, with no published methodology, no independent replication and no peer review.

Conspicuously absent from the announcement is Epic itself. The company issued no statement, and coverage of the launch carries no comment from it. That silence leaves unresolved whether the connection is a sanctioned partnership or the standard third-party interface any developer can request — a distinction that decides which governance gate a health system is entitled to hold.

Other launch partners talked more about the workspace than the chart. "At AdventHealth, the value of AI starts with our people," said Robert Purinton, chief AI officer at AdventHealth. "By putting tools like ChatGPT Work, Codex, and connected business data in the hands of our team members, AI can reduce routine work and help practical innovations move more quickly into action."

## Why This Matters

The read-only boundary is the most interesting piece of safety architecture the industry has shipped this year, and also the most fragile.

Read-only means the model cannot create a false lab value, alter a medication list, or leave an artifact a clinician later reads as established fact. Liability stays with the human who acts on the summary. That is a genuinely conservative design from a category not known for restraint, and it arrives while OpenAI defends itself in court over health guidance: a Florida pastor sued in July alleging ChatGPT gave him a near-fatal recommendation, and in May the family of a user sued over dosage advice.

But a write lock constrains the writing, not the reading. A summary that quietly omits a material finding is not caught by any permission setting. Omission, stale data, missing provenance, a chart the model only partly reviewed — every real risk in clinical synthesis lives on the read side. The boundary OpenAI drew protects the database. It does not protect the decision.

The commercial layer is messier still. Chart summarization is already sold twice over at most large Epic shops: Epic's own AI does it, and ambient documentation vendors built pre-visit preparation into their contracts two years ago. ChatGPT is now a third product aimed at one workflow. The question facing CIOs is not whether ChatGPT can read a chart. It is which of three tools owns chart review a year from now, and what happens to clinician trust when two of them summarize the same patient and disagree.

Scale separates this from a pilot. When ChatGPT Health went broadly available to U.S. consumers in late July, OpenAI said people were already asking roughly 300 million health-related questions a week. Patients and clinicians will now meet two OpenAI products touching Epic data under entirely different controls — one authorized by the patient, one by the organization. The health system fields the questions about which is which.

## What to Watch

Three things. Whether Epic publicly characterizes the connection, which determines whose governance holds the gate. Whether any health system publishes independent validation against its own charts rather than treating 99.1% as settled. And whether the read-only boundary survives contact with customers, because the obvious next request is order drafting, note generation and writing back. The day OpenAI grants it, the safety story it shipped on Sept. 1 stops applying.