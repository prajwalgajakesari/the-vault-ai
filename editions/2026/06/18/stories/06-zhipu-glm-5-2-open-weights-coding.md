# Zhipu's Open-Weights GLM-5.2 Tops the Intelligence Index and Undercuts GPT-5.5 on Coding

A Chinese lab just shipped a model anyone can download for free that beats OpenAI's flagship on long-horizon coding tasks while costing roughly one-sixth as much to run. On June 16, Z.ai—the company formerly known as Zhipu—released the full open weights of GLM-5.2 under an unrestricted MIT license, three days after handing it to its coding-plan subscribers. By the next morning, the independent benchmarking firm Artificial Analysis had crowned it the new leader of the open-weights pack, and the framing of the AI race shifted again: the most capable model you can self-host is now Chinese, and it is cheap.

## What the numbers say

GLM-5.2 scored 51 on the Artificial Analysis Intelligence Index v4.1, the firm's composite measure of reasoning, coding, and agentic ability. That figure put it ahead of every other open-weights model on the board—MiniMax-M3 and DeepSeek V4 Pro (max) tied at 44, and Moonshot's Kimi K2.6 at 43. Notably, the model is the same size as its predecessor, GLM-5.1 (744 billion total parameters, 40 billion active in a mixture-of-experts design), yet it jumped 11 points on the index, a gain Artificial Analysis attributed largely to scientific reasoning.

The under-the-hood improvements are specific. According to Artificial Analysis, GLM-5.2 lifted its Humanity's Last Exam score by 12 points to 40%, raised SciCode by 7 points to 50%, gained 16 points on the CritPt physics benchmark to 21%, and pushed TerminalBench v2.1 up 16 points to 78%. On GDPval-AA v2, the firm's marquee real-world agentic-work metric, GLM-5.2 hit 1524—ahead of MiniMax-M3 (1418) and DeepSeek V4 Pro (1328), and effectively level with GPT-5.5 at its highest reasoning setting (1514).

Where the story gets pointed is coding. On FrontierSWE, GLM-5.2 reached 74.4%, edging GPT-5.5 (72.6%) and landing in a near-tie with Anthropic's Claude Opus 4.8 (75.1%). On MCP-Atlas, a tool-use benchmark, it scored 77.0 against GPT-5.5's 75.3, again just shy of Opus 4.8. It also led GPT-5.5 on Humanity's Last Exam when both models were equipped with external tools. The picture isn't a clean sweep—GPT-5.5 still won DeepSWE handily (70.0% to GLM-5.2's 46.2%)—but on the long-running, agentic engineering tasks Z.ai built the model for, GLM-5.2 either matches or beats the closed flagship.

## The price gap is the headline

GLM-5.2 lists at $1.40 per million input tokens and $4.40 per million output tokens on Z.ai's first-party API (with a $0.26 cache-hit rate), pricing held flat from GLM-5.1. GPT-5.5, by comparison, runs about $5.00 input and $30.00 output per million tokens. Add it up and a comparable workload costs roughly $5.80 per million tokens on GLM-5.2 versus about $35 on GPT-5.5—the "one-sixth the cost" figure that has anchored nearly every headline this week. Because the weights are MIT-licensed and downloadable from Hugging Face, enterprises can also skip the API entirely and run the model on their own hardware for the price of compute and electricity, with no regional restrictions.

The model ships with a 1-million-token context window, up fivefold from the 200,000 tokens on GLM-5.1—a change Z.ai pitched as essential for sustaining the "long, messy coding-agent trajectories" that break shorter-context models partway through a task.

## Reporting

Z.ai announced the release on X with a deliberately loaded tagline: "Introducing GLM-5.2: Frontier Intelligence, Open Weights." The company emphasized "significant improvements in coding and agentic tasks" and "strong long-horizon capabilities with a 1M context window," offering two reasoning tiers—a "max" mode that pushes peak performance and a "high" mode tuned for efficiency. Z.ai, led by CEO Zhang Peng, completed a Hong Kong Stock Exchange listing in January that raised roughly HKD 4.35 billion, giving it unusual capital depth for an open-weights lab.

The timing was hard to miss. GLM-5.2's June 13 debut landed one day after Washington moved to block Anthropic's top-tier "Fable 5" model from global export—a sequence multiple outlets read as a direct Chinese answer to tightening US controls. Independent developer and analyst Simon Willison, reviewing the open weights, called GLM-5.2 "probably the most powerful text-only open-weights LLM" currently available. One Beijing-based analyst, quoted in coverage of the launch, framed the moment more sharply, calling the model "proof that open knowledge can look the most expensive secrets of Silicon Valley in the eye."

Not everyone is sanguine. Reporting from TechTimes flagged that while the open weights are clean, using Z.ai's hosted API routes data through Chinese infrastructure—a compliance and data-residency concern that may push security-sensitive enterprises toward self-hosting or third-party providers like Fireworks, Baseten, and Nebius, all of which are already serving the model.

## Analysis

The strategic logic here is the same one DeepSeek demonstrated in early 2025, now executed with more polish and better benchmarks. A succession of Chinese labs—DeepSeek, MiniMax, Moonshot, and now Z.ai—has converged on open weights not as charity but as a wedge: if the frontier can be matched and given away, the pricing power of closed American models erodes, and the gravitational center of the developer ecosystem drifts toward whoever ships the most capable downloadable model. GLM-5.2 sits on the Pareto frontier of intelligence versus cost per task, meaning no model at its capability level is cheaper to run. That is precisely the position that disciplines a market.

US export controls were designed to slow Chinese AI by restricting access to advanced chips and, increasingly, to frontier models themselves. GLM-5.2 is an awkward data point for that strategy: a model trained and released under sanction pressure that nonetheless tops the open-weights index and trades blows with GPT-5.5 on coding. Controls can gate compute, but they cannot easily contain a 744-billion-parameter file once it is on Hugging Face under an MIT license. The one caveat is token efficiency—GLM-5.2 burns 43,000 output tokens per index task, well above its peers, which narrows the real-world cost advantage for verbose workloads.

## What to watch

Three things over the coming weeks. First, adoption: whether the migration of cost-sensitive developers from closed APIs to GLM-5.2—via self-hosting or cheap third-party endpoints—shows up in OpenRouter and provider traffic. Second, the enterprise data question: how security-conscious buyers split between Z.ai's hosted API and self-managed deployments, and whether Western providers compete the inference price down further. Third, the closed-model response: whether OpenAI, Anthropic, or Google adjust pricing or reasoning-tier strategy now that a free, downloadable model can credibly claim parity on the coding tasks enterprises actually pay for.
