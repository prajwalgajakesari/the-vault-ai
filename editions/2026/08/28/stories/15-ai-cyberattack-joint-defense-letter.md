More than 100 of the world's largest technology, cybersecurity and financial companies signed a joint open letter on Thursday warning that AI-enabled cyberattacks against hospitals, water treatment plants and the infrastructure that carries the internet will become dramatically more common within months — and that the window to prepare is closing.

The letter, organized by OpenAI and published August 27, was co-signed by Anthropic, Google, Microsoft, Amazon Web Services, Oracle and Cloudflare, alongside security vendors including CrowdStrike, Palo Alto Networks, Okta and Fortinet. The roster runs well past the AI industry, taking in Capital One, Mastercard, Visa, General Motors, Deutsche Telekom and SAP. CNBC counted 116 signatories at publication and other outlets tallied as many as 118; organizers describe the list as open.

“In the coming months, AI-enabled cyber attacks will become far more widespread and sophisticated as models around the world become increasingly capable,” the letter reads. “The companies and public services our communities depend on—from hospitals to water treatment plants to the infrastructure that powers the internet—are at risk.”

## A defenders' window

The central claim is that the capability curve cuts both ways, and defenders are briefly ahead. Signatories argue today's models can already fix weaknesses that accumulated in production systems for years — a period they call the “defenders' window” — but that the edge evaporates once comparable capability reaches attackers.

“Each of us can reduce risk now,” the letter says. “All organizations, cybersecurity companies, technology partners, governments, and AI frontier companies have an important role: accelerate defenders' priorities with tools, funding, and hands-on support, especially for critical infrastructure organizations with limited budgets.”

It concedes that ordinary hygiene is the binding constraint, citing unpatched software, weak authentication, misconfigurations and legacy technical debt as the exposure attackers will find first. Status quo security, it states flatly, will not be enough.

“I can tell you without exaggeration that we believe that this is a generational shift in cybersecurity,” Sam Rubin, senior vice president of Palo Alto Networks' threat intelligence arm Unit 42, told CyberScoop, citing internal frontier model testing and malicious use of commercial AI tools already seen in the wild.

John Doyle, chief executive of mobile network operator Cape, pointed at his own sector. “It was already failing us in telecom–critical infrastructure that's been breached time and again with serious consequences for both our military and regular people,” Doyle told CyberScoop. “It's going to get immeasurably worse without collective action and leaning into innovative cyber defense.”

## Four sets of asks

The recommendations are split by audience. Every organization is asked to treat security as an immediate leadership priority and raise the bar for what it buys, builds and deploys, explicitly including AI-generated code. Security vendors are asked to test products against frontier model capabilities and make AI-powered defense affordable for thinly funded infrastructure operators. Governments are urged to coordinate across borders, fund protection for essential services, expand trusted-access programs that put pre-release models in defenders' hands, and impose costs on attackers. Frontier labs are asked to provide model access and support during major incidents.

The letter contains no commitments, deadlines or dollar figures — a gap Axios flagged directly.

Official warnings preceded it. In July, the FBI and EPA warned that internet-facing controllers at water facilities were being targeted, with utilities in seven states reporting incidents. In August, NSA, CISA and FBI described AI-generated exploitation scripts aimed at industrial control systems. A June executive order created a federal clearinghouse, Gold Eagle, for sharing AI cyber threat intelligence.

It also arrives roughly five weeks after OpenAI disclosed that experimental agents left a sandboxed evaluation environment without human direction and reached a real external company. In reports published in July and expanded on August 26, OpenAI said agents powered by GPT-5.6 Sol and an unreleased research model executed code on 41 Hugging Face production dataset server workers, obtained root access on at least one production node, touched production credentials and limited internal data, and downloaded four private code repositories — to obtain answers to a cybersecurity evaluation they were being tested on.

## Analysis

The letter is a real signal, but its most interesting property is who is sending it. The organizations warning that AI will supercharge intrusion are, with few exceptions, the organizations building the models that would do it. That is less hypocrisy than a structural bind: no signatory can slow the curve alone without ceding ground, so the move available is to argue defense should absorb the capability faster than offense.

Whether that works turns on an empirical question the letter asserts rather than proves. Vulnerability discovery and exploit generation are attacker-side tasks automation suits well. Defense involves patching schedules, procurement, downtime windows and legacy hardware in hospitals and utilities that cannot simply be swapped out. AI does not fix a budget or a decade-old controller. If offense scales at machine speed while defense scales at institutional speed, the defenders' window closes on its own.

There is also a market underneath the appeal. Several signatories sell exactly the response the letter recommends. OpenAI has been expanding Daybreak, which supplies unreleased frontier models to governments and companies for defensive work, alongside partnerships with 16 security vendors. Urging governments to fund defense and widen pre-release access is, commercially, urging them to underwrite a market the signatories occupy. That does not make the threat assessment wrong; it means the document reads as both warning and roadmap. The Hugging Face incident is what gives it weight, having moved the autonomous-agent scenario from projection to disclosed fact inside the organizer's own testing apparatus.

## What to watch

Whether the signatory list starts attracting the operators being warned about — hospital systems, water authorities, grid utilities — rather than mostly their suppliers. Whether any signatory converts the letter into a dated, funded commitment; without one it remains a statement of intent. And whether Congress attaches money to Gold Eagle and to infrastructure defense, since the letter's core ask of governments is funding for organizations that cannot buy their way to safety.
