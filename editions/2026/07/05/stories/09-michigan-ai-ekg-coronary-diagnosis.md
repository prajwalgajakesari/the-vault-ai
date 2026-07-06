A woman walks into an emergency room with crushing chest pain. Doctors run the tests, thread a catheter into her arteries, and find nothing. The angiogram is "clear." She is sent home, sometimes with a diagnosis of anxiety, even though her heart is genuinely starved of blood. The culprit is coronary microvascular dysfunction, or CMVD, a disease of the heart's smallest vessels that standard imaging routinely misses and that disproportionately strikes women.

Now researchers at the University of Michigan say they have built an artificial intelligence system that can flag the condition in the time it takes to record a routine heartbeat: a single 10-second EKG strip, no specialized scanner required.

The study, published in NEJM AI, a journal from the New England Journal of Medicine family, describes a model that outperformed earlier EKG-based AI on nearly every diagnostic task the team threw at it, including predicting myocardial flow reserve, the gold-standard measurement used to diagnose CMVD.

"Our model creates a way for clinicians to accurately identify a condition that is notoriously hard to diagnose, and often missed in emergency department visits, using a 10-second EKG strip," said senior author Venkatesh L. Murthy, M.D., Ph.D., associate chief of cardiology for translational research and innovation at the U-M Health Frankel Cardiovascular Center.

## How the Model Was Built

The central obstacle was data. Diagnosing CMVD today typically requires PET myocardial perfusion imaging, scans that are expensive and largely confined to specialty centers. That scarcity meant the team had very few labeled examples to train on.

Their workaround was self-supervised learning. The researchers first pretrained a modified vision transformer on 800,035 unlabeled EKG waveforms drawn from the public MIMIC-IV-ECG database, teaching the model the underlying grammar of the heart's electrical signal before it ever saw a diagnosis. "Essentially, we taught the model to 'understand' the electrical language of the heart without human supervision," Murthy said.

Only then did the team fine-tune it on the scarce, high-value labels: PET-derived measurements from 3,126 patients and clinical report labels from 13,704 more, across 12 different clinical and demographic prediction tasks, several of which are not possible with existing EKG-AI tools.

## What the Numbers Show

Performance varied by task. The model's area under the receiver operating characteristic curve, a standard accuracy measure where 1.0 is perfect and 0.5 is a coin flip, ran from 0.763 for detecting impaired myocardial flow reserve to 0.955 for spotting a severely weakened left ventricle. In plainer terms, Michigan Medicine says the tool correctly identified coronary microvascular dysfunction roughly 70 to 80 percent of the time.

Crucially, the model held up when tested outside the data it was trained on. Across three external and two internal cross-modality databases, its accuracy for impaired flow reserve held near 0.771, and self-supervised pretraining improved results in 11 of 12 tasks compared with training from scratch. The team also found only a minimal performance bump when using EKGs recorded during exercise stress tests versus ordinary resting strips, a practical advantage for busy or under-resourced hospitals.

## Why It Matters

CMVD is a case study in how medicine can overlook a condition it cannot easily see, and in how that blind spot falls unevenly. The disease produces chest pain and raises the risk of heart attack, yet because it affects vessels too small to show up on a conventional angiogram, patients are frequently told their hearts are fine. The pattern is especially common in women, whose ischemic heart disease has long been under-recognized.

"People who come to the ER for chest pain might have CMVD, but their angiogram will show up as 'clear,'" said co-author Sascha N. Goonewardena, M.D., an associate professor of internal medicine-cardiology at U-M Medical School. "In hospitals with limited resources or non-specialty centers, using our EKG-AI model to predict myocardial flow reserve and CMVD will be an easy, cost-effective and non-invasive way to identify when a patient would benefit from advanced testing for a serious condition."

That is the equity argument for accessible AI diagnostics in a nutshell. Around 14 million people visit an ER or outpatient clinic for chest pain each year in the U.S., and the vast majority will never be near a PET scanner. An EKG, by contrast, is cheap, ubiquitous, and takes seconds. Pushing a specialty-center capability onto a machine that already sits in nearly every clinic could turn CMVD screening from a privilege into a default, precisely the kind of leveling that democratized diagnostics promise.

## What to Watch

Important caveats remain. The model is a research tool, not an approved clinical device, and it was developed and validated largely on Michigan and registry data; broader, prospective testing across diverse populations and health systems will be needed before it reaches bedsides. An AUROC of 0.763 for the flagship flow-reserve task is promising but far from definitive, and the tool is designed to flag patients for further testing, not to replace PET imaging.

There are also disclosures to weigh: several co-authors are affiliated with INVIA, a cardiac imaging software company, and Murthy has a paid relationship with the firm and is a recused NEJM AI editor. The next milestones to watch are prospective clinical trials, regulatory review, and evidence that catching CMVD earlier actually changes outcomes for the patients, many of them women, who have spent years being told nothing was wrong.