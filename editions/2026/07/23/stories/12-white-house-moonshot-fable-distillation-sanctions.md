# White House Accuses Moonshot of Distilling Anthropic's Fable to Build Kimi K3; Treasury Threatens Sanctions

A senior White House official has publicly accused Chinese startup Moonshot AI of covertly copying Anthropic's newest model to build Kimi K3, the largest open-weight system yet released, and of running the effort on Nvidia chips that are barred from export to China. The Treasury Department is now dangling sanctions. But within a day, AI researchers were openly questioning whether the central technical claim even fits the calendar.

Michael Kratsios, who directs the White House Office of Science and Technology Policy, laid out the allegation on X on Wednesday, July 22. He said Moonshot had distilled Anthropic's Fable model — extracting its capabilities by systematically querying it — and had gone to unusual lengths to hide the operation.

"To do this they developed a sophisticated internal platform to conduct large scale distillation against U.S. models, allowing them to quickly switch between multiple methods of access to avoid detection," Kratsios wrote.

He was careful to draw a line between routine engineering and what he described as theft. "Legitimate AI distillation used to create smaller, more efficient models plays a vital role in this open innovation ecosystem," Kratsios wrote. "However, large-scale, covert industrial distillation aimed at stealing proprietary U.S. technology and undermining American research is unacceptable."

## The accusation

Kratsios also alleged a hardware dimension. He said Moonshot had used Nvidia GB300 servers — either newly acquired or accessed through infrastructure in Thailand — to train its models. The GB300, part of Nvidia's Grace Blackwell line, is among the chips barred from sale to Chinese firms under U.S. export controls, which raises the prospect that Moonshot may have skirted those rules.

The financial threat came from the top of the Treasury Department. Secretary Scott Bessent has said the administration is prepared to move against companies engaged in this kind of copying, citing forensic evidence. "We are finding watermarks of our U.S. large language models on many of the Chinese models, and that that's unacceptable," Bessent said. Neither the Treasury nor the White House has detailed what those watermarks consist of or how the government traced Kimi K3 back to Fable.

Kratsios provided no evidence for how U.S. officials reached their conclusion, and Moonshot did not respond to requests for comment from multiple outlets. Anthropic, which earlier this year publicly accused Moonshot, DeepSeek and others of systematically distilling its models, declined to comment on the Fable claim specifically.

The company is not shy about Kimi K3's abilities. Moonshot describes it as the first open 2.8-trillion-parameter model and launched it on July 16, pitching near-frontier performance at a fraction of the token cost. "While its overall performance still trails the most powerful proprietary models, Claude Fable 5 and GPT 5.6 Sol, Kimi K3 demonstrated frontier-level performance across our evaluation suite, consistently outperforming other tested models," the company says on its site.

## The skepticism

That is where the timeline starts to strain the accusation. Fable has only been publicly available since July 1. Kimi K3 shipped on July 16. Building a 2.8-trillion-parameter model by copying another model in roughly two weeks strikes several researchers as implausible.

"I don't think you get a model this strong and this quickly on the heels of Fable doing strictly distillation," Braden Hancock, a researcher at the Laude Institute and co-founder of Snorkel AI, told TechCrunch. "There's just not even frankly time, right? Fable's only been publicly available since July 1st. You can't distill that much data, train a model, and release it in two weeks."

Hancock also pushed back on the framing that Chinese labs are merely riding on American work. "In general, Americans are understating the technical expertise of these Chinese teams," he said. "One of the founders of Moonshot was a CMU PhD student. These are legitimate researchers and engineers doing solid work. … If American models ground to a halt, I think China's progress would slow, but would still continue. They're not just riding coattails here."

Nathan Lambert, an AI researcher at the Allen Institute for AI, argued that distillation is a fading explanation for how Chinese models are closing the gap. "I've been of the opinion that distillation is becoming less and less impactful over time as the Chinese models get closer to the frontier and the training regime shifts to [reinforcement learning]," he said on a podcast. "If it were the case, everyone would be easily able to catch up to a GLM or to a K3 by using its data for distillation. But we have not, or we won't see this, from supervised fine-tuning alone."

## What it means

The dispute sits at the intersection of three unsettled fights: U.S.-China AI competition, the murky norms around distillation, and the enforcement of chip export controls.

Distillation itself is not a uniquely Chinese practice. Elon Musk testified earlier this year that his company distilled OpenAI's models to help build Grok and called the technique common across the industry. The line between distillation and building synthetic training datasets is blurry, and U.S. frontier labs face their own lawsuits alleging they built their models on other people's data scraped without consent.

The chip allegation may prove more consequential than the model one, because it is more concrete. A black market for restricted Nvidia hardware exists; in May, the founder of U.S. server maker Supermicro was indicted for smuggling advanced chips into China. Sam Bresnick, a research fellow at Georgetown's Center for Security and Emerging Technology, argued the real gap is oversight of where training runs actually happen. "I am a proponent of know your customer laws for data centers across the world," he said. "If you are letting a company conduct huge training runs on your state-of-the-art hardware, there needs to be a reporting mechanism for who that company is and what they're doing."

## What to watch

The immediate question is whether the administration produces evidence — the watermarks Bessent referenced, or access logs supporting the "rotating methods to avoid detection" claim — or whether the accusation remains an assertion. Congress is already circling: House committees led by Reps. Andrew Garbarino and John Moolenaar have opened a joint investigation into adversarial distillation and the integration of Chinese open-weight models into American software. Watch, too, for whether Treasury actually names Moonshot on a sanctions or Entity List designation, and whether the Thailand GB300 thread leads to a wider export-control enforcement action. The distillation charge may be hard to prove. The chips may be easier.
