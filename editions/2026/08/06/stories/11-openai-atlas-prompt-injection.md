A malicious webpage should not be able to text your friends or reorganize your Amazon account. But at Black Hat USA in Las Vegas this week, researchers from the security firm Zenity showed that OpenAI's Atlas browser could be talked into doing exactly that, no clever hacking required beyond a few lines of hostile text hidden on a website the AI agent was asked to read.

In demonstrations detailed by WIRED, Zenity's team got Atlas's built-in agent to fire off spam messages through a victim's WhatsApp account and to alter information inside an Amazon account, all without the user ever asking for those actions. The trick was **prompt injection**: planting instructions on a page that the AI reads as if they came from its owner. The agent, unable to tell a command from mere content, simply followed orders.

## What the researchers showed

Zenity co-founder and CTO **Michael Bargury** and AI security researcher **Stav Cohen** presented the work in a session titled "Pwning Agentic Browsers with PleaseFix: A New Vulnerability Class for 0-Click Takeover." Their research was not limited to OpenAI. The team examined roughly **20 security issues** spanning AI-powered browsers, extensions and agents from several of the largest technology companies, including offerings tied to Google, Anthropic, Microsoft and Perplexity.

The through-line was consistent. In one Atlas demo, a seemingly harmless link led the agent to a page whose hidden instructions it treated as legitimate commands. From there it dispatched phishing-style messages from the victim's own WhatsApp and moved to make purchases on Amazon, in some cases enlisting Amazon's own shopping assistant, Rufus, to help finish the job. Because the malicious text sat inside content the agent was told to process, no click on a booby-trapped button and no downloaded file was needed. The instructions arrived through the front door.

Bargury has framed the problem as structural rather than incidental. "Agentic browsers are trading away decades of hard-won security engineering for convenience," he said of the class of flaws, adding that "this is not a bug we can patch away." That assessment matters because it separates these findings from ordinary software defects. A buffer overflow gets fixed and stays fixed. A system that cannot reliably distinguish trusted commands from untrusted data has a harder road.

## Why agentic browsers are different

For two decades, browsers have been built around a simple safety idea: a website you visit should not be able to reach across into your other accounts and act as you. Sandboxing, the same-origin policy and permission prompts all enforce that boundary. Zenity's argument, echoed by other researchers, is that agentic browsers quietly dissolve it. When an AI agent reads a page and is also empowered to send messages, fill forms and complete checkouts, the wall between "content I'm looking at" and "actions I'm authorized to take" gets thin.

This is the core tension of the entire agentic-browser category. These tools are useful precisely because they act on your behalf, carrying your logins, your context and your permissions into every task. That same authority is the attack surface. The more an agent can do without asking, the more damage a single injected instruction can cause. Persuasion aimed at a human becomes a command aimed at a system already holding the keys.

OpenAI has not disputed the difficulty. In a blog post accompanying a security update to Atlas, the company acknowledged that "as the browser agent helps you get more done, it also becomes a higher-value target of adversarial attacks." Chief information security officer Dane Stuckey has gone further, conceding that "prompt injection remains a frontier, unsolved security problem." The U.K.'s National Cyber Security Centre reached a similar conclusion, warning that prompt-injection attacks against generative AI may never be fully eliminated and that organizations should focus on limiting the blast radius instead.

## OpenAI's response, and Atlas's exit

Zenity said it reported its findings to OpenAI in **January 2026**. OpenAI has since addressed some of the vulnerabilities, describing prompt injection as an area of active research and pointing to updates it shipped earlier in the year, including an adversarially trained model and hardened safeguards, after internal red-teaming surfaced multi-step exploits. The company has said its ability to inspect an agent's own reasoning gives defenders an edge in staying ahead of attackers.

The timing, though, is pointed. OpenAI is preparing to retire Atlas, with the browser slated to be discontinued on **August 9, 2026**, days after the Black Hat presentation. Whether that reflects the security burden, product strategy or both, the effect is the same: the most-scrutinized agentic browser is on its way out even as the category it helped popularize keeps expanding.

## What to watch

The Atlas demos are a preview, not an outlier. Zenity's broader tally of issues across rival products suggests the weakness is baked into the design pattern, not one company's implementation. The open questions now are architectural. Can vendors build a durable separation between the content an agent reads and the actions it is allowed to take? Will agents start requiring explicit human confirmation for high-stakes steps like sending messages or spending money, and will users tolerate the friction? And as more browsers, extensions and assistants gain the power to act, will the industry treat prompt injection as a solvable bug or, as Bargury and even OpenAI suggest, a permanent condition to be managed. The next wave of agentic products will answer that whether their makers intend to or not.
