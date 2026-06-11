# Michigan's Prima AI reads a brain MRI in seconds, hitting 97.5% accuracy across 50+ conditions

A brain MRI can take days to read. By the time a radiologist works through a backlog, a patient with a quietly bleeding brain may have waited far too long. Researchers at the University of Michigan say they have built an artificial intelligence system that compresses that wait to seconds — reading a scan, suggesting a diagnosis, and flagging whoever might be in danger of a stroke or hemorrhage before they leave the imaging suite.

The model, named Prima, detected neurological conditions with accuracy as high as 97.5% and predicted how urgently a patient needed treatment, according to a study published in *Nature Biomedical Engineering*. Across more than 50 radiologic diagnoses spanning major neurological disorders, the team reports that Prima outperformed other state-of-the-art general and medical AI models on diagnostic performance.

"As the global demand for MRI rises and places significant strain on our physicians and health systems, our AI model has potential to reduce burden by improving diagnosis and treatment with fast, accurate information," said senior author Todd Hollon, M.D., a neurosurgeon at University of Michigan Health and assistant professor of neurosurgery at the U-M Medical School.

What sets Prima apart, the researchers say, is the breadth of what it learned from. Earlier attempts to apply AI to neuroimaging typically relied on manually curated subsets of data built for narrow tasks — detecting a specific lesion, say, or predicting dementia risk. Hollon's team instead trained Prima on essentially every brain MRI taken at University of Michigan Health since radiology went digital decades ago: more than 220,000 studies comprising millions of imaging sequences. Crucially, they also fed the model each patient's clinical history and the physician's stated reason for ordering the scan.

"Prima works like a radiologist by integrating information regarding the patient's medical history and imaging data to produce a comprehensive understanding of their health," said co-first author Samir Harake, a data scientist in Hollon's Machine Learning in Neurosurgery Lab. "This enables better performance across a broad range of prediction tasks."

Technically, Prima is a vision language model — an AI system that can process images and text together in real time. After a patient finishes imaging, it can return feedback almost immediately, not only proposing likely diagnoses but triaging them. For time-critical conditions such as brain hemorrhages or strokes, the model can automatically alert providers and recommend which subspecialist should be notified, such as a stroke neurologist or a neurosurgeon.

The team tested Prima on more than 30,000 MRI studies over the course of a year — a meaningful prospective check rather than a one-off benchmark.

"Accuracy is paramount when reading a brain MRI, but quick turnaround times are critical for timely diagnosis and improved outcomes," said co-first author Yiwei Lyu, a researcher in Computer Science and Engineering at U-M. "At key steps in the process, our results show how Prima can improve workflows and streamline clinical care without abandoning accuracy."

## Why it matters

Millions of MRI studies are performed worldwide each year, a large share of them aimed at neurological disease, and demand is climbing faster than the supply of neuroradiologists trained to interpret them. That mismatch produces the everyday frictions patients know well — scans that sit unread for days, longer waits at under-resourced hospitals, and the diagnostic errors that creep in when overstretched clinicians work through volume.

AI in radiology has so far advanced mostly through single-purpose tools: an algorithm to spot a pulmonary nodule, another to flag a large-vessel stroke. Prima's pitch is breadth. By learning from an entire health system's archive rather than a hand-picked dataset, it aims to function less like a narrow detector and more like a generalist first reader — what Hollon describes as a co-pilot that interprets the study and routes the urgent cases to the right human. The approach could matter most where neuroradiology coverage is thinnest.

"Whether you are receiving a scan at a larger health system that is facing increasing volume or a rural hospital with limited resources, innovative technologies are needed to improve access to radiology services," said Vikas Gulani, M.D., Ph.D., chair of the Department of Radiology at U-M Health and a co-author. "Our teams at University of Michigan have collaborated to develop a cutting-edge solution to this problem with tremendous, scalable potential."

## What to watch

The researchers are candid that the work remains in an early stage of evaluation. The headline results come from a single health system's data, and how well Prima generalizes to scanners, populations, and workflows elsewhere is the open question that determines whether it becomes a clinical tool or a promising prototype. The team's next steps include folding in richer electronic medical record data to push accuracy further — closely mirroring how human radiologists actually read.

Regulators, hospitals, and policymakers are still working out how to safely embed broad AI models into clinical practice, and most systems in use today remain approved for narrow tasks. The bigger ambition Hollon floats — adapting the same approach to mammograms, chest X-rays, and ultrasounds — would multiply both the potential benefit and the validation burden. For now, watch for external, multi-site testing and any move toward regulatory review; those, more than any single accuracy figure, will signal whether a seconds-long brain MRI read is ready for the clinic.
