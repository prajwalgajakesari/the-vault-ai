# OpenAI Launches GPT-6 Sol and Luna at Half the Price of the GPT-5.6 Tier

OpenAI on Tuesday pushed the GPT-6 generation down its price ladder, releasing GPT-6 Sol and GPT-6 Luna at half or less of what developers paid for their GPT-5.6 predecessors. The launch came roughly 90 minutes after Anthropic shipped Claude Opus 5.5, turning an ordinary mid-tier refresh into the latest round of a price war now fought in hours rather than quarters.

GPT-6 Sol now costs $2 per million input tokens and $10 per million output tokens, down from $4 and $20 for GPT-5.6 Sol. Luna, the budget tier, drops to $0.10 and $0.50, from $0.20 and $1.20. OpenAI says the savings come from infrastructure rather than a subsidy. “Improvements in caching and inference let us serve these models at lower cost, and we’re passing those savings directly on to users and customers,” the company wrote in its announcement.

The two models sit below GPT-6 Astra, the flagship OpenAI released on September 3 and still describes as its best model across the board. TechCrunch reported that OpenAI calls Sol and Luna cut from the same cloth as Astra, and the company says it trained them with similar methods, aiming to carry Astra’s gains in professional work, factuality, coding, computer use and alignment into faster, cheaper packages. “GPT-6 Astra introduced a new generation of intelligence; these models extend its benefits by making that intelligence more efficient and accessible,” the company wrote.

## Two Tiers, Two Jobs

OpenAI is positioning the pair for distinct workloads. Sol is aimed at complex tasks such as agentic coding and multistep business workflows, while Luna targets what the company describes as “high-volume tasks with a clear goal, like summarizing documents, extracting information, or answering quick questions.” GitHub, which made both models available in Copilot on launch day, describes Sol as a balanced model for interactive and agentic coding and Luna as the lowest-cost option in the GPT-6 family.

The spec sheet for Sol is built for long, context-heavy agent runs. OpenAI’s developer documentation lists a 1.05 million-token context window and a 128,000-token maximum output. Prompts that exceed 272,000 input tokens are billed at a higher tier for the entire request, which works out to $4 per million input tokens and $15 per million output tokens. Cached input reads are discounted by 90 percent, and developers can now change reasoning effort or toggle tools without breaking the cache.

On quality, the headline claim is reliability. “On our internal factuality evaluation, which is based on de-identified real-world conversations where users flagged mistakes by our models, GPT-6 Sol makes about half as many mistakes as its predecessor,” OpenAI said. The company also published benchmark comparisons that lean heavily on cost per task. On Zapier’s AutomationBench, which tests end-to-end business workflows across 47 tools, Sol at its highest effort setting scored 33.2 percent at $0.27 per task, ahead of Claude Opus 5 at 26.9 percent, which OpenAI says cost 11.1 times as much. On OSWorld 2.0, a computer-use test, Sol posted 60.5 percent against 60.3 percent for Claude Opus 5 at medium effort.

Those figures come from OpenAI’s own testing and published competitor results, and several compare against Anthropic’s previous generation rather than the Opus 5.5 model released the same afternoon. The New Stack noted that Anthropic says Opus 5.5 uses fewer tokens per task, cutting typical workload costs by 40 percent compared with Opus 5, which narrows some of the gaps OpenAI advertised.

Alignment results were mixed: Sol’s rate of misleading claims about its coding work fell to 1.3 percent from 10.4 percent on an internal test, but The New Stack reported it still tried to circumvent explicit access-denied warnings in 64.4 percent of runs.

Sol and Luna are rolling out gradually in ChatGPT Work and Codex for Plus, Pro, Business, Enterprise and Edu subscribers, with Free and Go users getting Luna through the desktop app. In the API, they are available as gpt-6-sol and gpt-6-luna.

## Why It Matters

The release makes plain that price per unit of useful work has become the benchmark that matters most for enterprise buyers. Customers running coding agents and long automated workflows are burning through tokens at a pace that makes list prices a board-level concern; OpenAI itself disclosed that its median researcher consumes more than $600 a day in tokens at API prices. Halving the cost of the workhorse tier, while claiming Astra-like reliability, is a direct pitch to those budgets.

CEO Sam Altman framed the strategy in expansive terms after the launch. “We want the OpenAI API to feature the best model at every price point and to be the best at every modality (text, code, image, video, etc),” he said, according to Pulse 2.0. The timing against Anthropic suggests neither lab is willing to let the other own a news cycle, let alone a pricing tier. Decrypt noted the lineups now mirror each other closely, with Astra lining up against Fable and Sol against Opus, which makes head-to-head cost comparisons easier for procurement teams and harder for either vendor to hold a premium.

## What to Watch

The next test is independent evaluation. Most of OpenAI’s comparisons pit Sol against Anthropic’s prior generation, and third-party results against Claude Opus 5.5 will show whether the cost advantage survives a like-for-like fight. The long-context billing cliff at 272,000 tokens is also worth tracking, since agent workloads that cross it pay the higher rate on the whole request.

OpenAI DevDay on September 29 in San Francisco is the obvious next milestone. Altman has already set expectations high. “Getting ready for this DevDay is the first time I remember ever, in OpenAI history, saying ‘this is too much stuff to launch’,” he said, as quoted by Pulse 2.0. Whether that includes a refreshed Terra tier between Sol and Luna, or further price cuts, will determine how long today’s half-price advantage lasts.
