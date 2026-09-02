For three years, Khanmigo could explain a parabola. It could not draw one. As of back-to-school 2026, it can — and it took six Google engineers, six months, and an unusual kind of corporate philanthropy to get there.

On August 27, Khan Academy and Google announced that Khanmigo, the nonprofit's AI tutor, can now detect the moment a student would benefit from a visual and generate an interactive diagram on the spot — charts, geometric shapes, parallel coordinate plots. Critically, these are not static images bolted onto a chat window. A student can drag a vertex or reposition a line segment, and Khanmigo recognizes the change and adjusts the lesson around it. Before this, as Khan Academy put it bluntly in its own announcement, "Khanmigo could only respond using text."

The second half of the release is less flashy and arguably more consequential: a rebuilt version of the *Practice My Knowledge* teacher tool, where Gemini drafts multiple-choice questions and the teacher decides which ones survive.

## How the sausage got made

The mechanism here is worth pausing on, because it is not a licensing deal. Since March, a team of six Google engineers has worked *inside* Khan Academy's product and engineering organization through a six-month Google.org fellowship — Google employees seconded full-time to a nonprofit rather than selling it software. The package also included a Google.org grant, whose size neither organization disclosed, and direct access to Gemini models in time for the 2026 school year. It extends a partnership announced in January at the Bett conference, where Google's Ben Gomes, chief technologist for learning and sustainability, first laid out the roadmap.

The engineering problem was not "make the model output a picture." It was deciding *when* a picture helps and what a good one looks like. Google's fellows helped define the underlying metrics for diagram quality, then evaluated visuals for relevance, helpfulness and clarity so they surface only at moments of genuine benefit. They refined details as granular as labeling, and built a feedback widget into Khanmigo so classroom use keeps improving the model's judgment.

"Google is a tremendous partner," said Sal Khan, founder and CEO of Khan Academy. "The Google.org Fellows have supercharged our engineering effort, allowing us to produce several new AI-powered features in time for students and teachers to use these tools in the new school year."

Jen Carter, head of technology at Google.org and the author of Google's announcement post, framed it as a division of labor: "By combining their deep expertise in student learning with Google's AI engineering, we are empowering teachers and students with tools designed to make learning more effective, engaging, and accessible than ever before."

## The teacher holds the pen

The practice-tool redesign started smaller than it ended. The original goal, Google says, was simply to use AI to generate high-quality multiple-choice questions. Working with the fellows pushed the Khan Academy team toward a bigger rebuild: making the whole tool editable, scorable and reviewable by educators.

The workflow now runs Gemini as a drafting assistant, not an author. Teachers can upload their own materials for Gemini to reference, draft a question set, then review every item and edit or reject anything before it reaches a student. Assignments can be scored or unscored, with structured performance reports afterward. Google summarized the philosophy in one line: Gemini drafts the materials, but teachers have the final say on what students see. In the previous version, teachers could generate practice questions but had no way to curate what actually went out — a gap Khan Academy says administrators flagged, particularly around getting difficulty levels right for a given class.

## Why this matters

The diagram feature is a nice product story. The context around it is the real one, and it is more complicated than either press release lets on.

Six days before the Google announcement, Sal Khan published a remarkably candid post about an independent randomized controlled trial of his own product. The NBER working paper — *"One Click Away: AI Tutoring with Khanmigo in a Two-Year School Experiment"* by Philip Oreopoulos and Nina Low — ran across 18 middle schools in Hamilton County, Tennessee over the 2024-25 and 2025-26 school years, with Khan Academy involved in neither its design nor its execution. The headline intent-to-treat effect was about 0.06 standard deviations over two years, 0.08 SD in year two once implementation matured. A secondary analysis of students who stayed in the intervention the full second year showed 0.14 SD.

Khan argues, reasonably, that 0.14 SD is the number to anchor on: the students were below grade level, more than a quarter had a special education designation, and the control group was not "no technology" but business-as-usual — in 14 of the 18 schools, that meant IXL, Zearn, Waggle or DeltaMath. It measures incremental benefit against real competitors, not a victory lap against nothing.

But the study's actual headline finding is the uncomfortable one, and Khan surfaces it himself: **students barely used Khanmigo.** The paper attributes that to behavioral barriers around help-seeking, compounded by an interface that waited to be opened rather than offering help proactively. That is the entire strategic thesis behind this year's rebuild — Khanmigo now lives inside the practice flow rather than in a separate chat.

Read against that backdrop, interactive diagrams look less like a demo of Gemini's reasoning and more like an engagement fix aimed squarely at an RCT-documented failure mode. Khan Academy reports early signs of increased engagement and improvement in *next-item correctness* — whether a student answers the very next problem on the same skill correctly, unaided, in the same session. That is a sharp, honest metric. It is also preliminary, self-reported, and not an RCT.

## What to watch

Three things. First, whether next-item correctness holds up at scale: Khan Academy piloted the reimagined platform with roughly 5,100 students across five U.S. districts, including Taft ISD in Texas and Hanover Community School Corporation in Indiana, then rolled it out to all district partners over the summer. Second, the January roadmap's unshipped half — Reading Coach for grades 5-12, and Schoolhouse.world's AI tutor-feedback and session-simulator tools — neither of which appeared in August. Third, whether the fellowship model spreads. Embedding engineers in a nonprofit for six months is cheaper than an acquisition and better PR than a contract, and with OpenAI and Anthropic both pushing hard into classrooms this month, it is a template competitors will notice.
