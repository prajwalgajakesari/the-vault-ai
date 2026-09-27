# Meta Adds Muse Safety Warning After SEV-2 Flaw Exposed Agents' Cloud VMs

Less than three weeks after launch, Meta's new AI agent has hit its first serious security problem, and it involves the very thing Meta said would keep users safe. An outside researcher found a vulnerability in **Muse** that could have let an attacker into a user's dedicated cloud virtual machine, the environment that holds the agent's emails, files and connected personal data. Meta is now adding a clearer, more prominent safety warning inside the app, according to an internal incident report reviewed by *The Information* and first reported on Friday, September 25.

The flaw came in through Meta's bug bounty program and had not been disclosed before. According to the report, Meta's security team first logged it as a **SEV-2**. Reuters described that as the company's third-highest level on a five-tier scale, a rating typically used for incidents with significant impact. A Meta spokesperson later told reporters that the issue had been miscategorized at first and was downgraded to **SEV-3**. Meta did not immediately respond to a Reuters request for comment.

Reports say an attack would not have been easy to pull off. It would have needed several steps of user interaction, including the user approving a system prompt that already carried a security notice. Meta's fix goes after that step. Instead of a deep architectural change, the company is making the warnings harder to miss when Muse runs into a suspicious site. Meta has not said whether any user data was accessed. No reports point to exploitation in the wild.

## The Machine at the Center

The bug matters because of where it sits. Meta built Muse's security pitch around the virtual machine. In its September 8 launch announcement, the company said Muse runs on **Muse Secure VM**, "a dedicated secure computer with its own browser," which houses both the agent and a person's data. Meta also said a separate **Sentinel** agent runs on the same machine, kept apart from Muse at the system level, and that nothing Muse does reaches the internet unless Sentinel approves it. The company says that design means Muse never sees users' passwords or payment methods.

At launch, executives said they knew permission prompts could backfire. Axios reported that Meta leaders worried people who are asked to approve every small action start approving requests by reflex. That is the failure mode this bug appears to have depended on. Muse was designed to ask for approval only on more sensitive actions, and Meta's answer to the flaw is to make one of those approval moments stand out more.

Muse is also getting a lot of use. Sensor Tower estimated about **2.8 million downloads** in the app's first two weeks, and Muse topped the free-app charts in the United States and Canada. The agent can send email, book travel, fill out forms and make purchases through Link by Stripe. It comes in a free tier and two paid plans, Power at **$20 a month** and Maximum at **$100 a month**. Meta chief AI officer Alexandr Wang told Axios that "for the vast majority of users, they should be able to do what they need to within the free tier." He framed the product as a first step toward what he called "personal superintelligence."

This is the second Muse security report in as many weeks. Security researcher Patrick Wardle earlier disclosed a separate issue in Muse for Mac, which *The Vault* covered in a previous edition. According to Stocktwits, Meta called that issue low operational risk and said a fix has been deployed. The VM flaw is unrelated. It sits in Meta's cloud infrastructure, not in a desktop client.

Meta shares fell about **3.4%** on Friday after the report, according to Stocktwits. Even so, the stock was up roughly 13% for the week and on track for its best month in more than a decade, largely on enthusiasm for Muse.

## Why It Matters

Meta's pitch for Muse depends on users trusting a company with a long record of privacy settlements, including a then-record $5 billion FTC penalty in 2019, with their inbox, calendar and payment flows. TechCrunch's launch coverage put the question directly in its headline: "Will consumers trust it?" A bug that reached the VM, the component Meta described as the agent's secure core, goes straight at that question, even if the real-world risk was limited.

The incident also shows a structural weakness that runs across the agent industry. Agents that browse the open web on a user's behalf will keep running into hostile content, and many of their defenses end in a human clicking "allow." Meta's own approach assumed that users will stop paying attention if they are asked too often. Making warnings more prominent is a reasonable short-term fix, but it pushes more of the security burden back onto the person Muse was supposed to relieve of busywork. The SEV-2 to SEV-3 downgrade also deserves a close look. Meta's internal triage first judged the issue as significant, and the public account now plays it down.

Meta handled the disclosure by the book. The bug came in through its bounty program, was triaged and got a mitigation. With a user base of millions that is still growing fast, though, the margin for error is narrowing. Muse's agents hold far more sensitive data than a social feed, so small flaws carry bigger consequences.

## What to Watch

The next milestone is **Muse Confidential VM**, which Meta has promised before the end of the year. Meta says it will encrypt the entire virtual machine, including users' data and conversations, with a key only the user holds, so that not even Meta can access it. Watch whether Meta publishes a public advisory or technical write-up on this flaw, whether the bounty researcher releases their own account, and whether regulators already focused on Meta's privacy record take an interest in agentic products.