---
headline: "Amazon's Custom Silicon Hits a $20 Billion Annual Run Rate as AI Chip Diversification Turns Real"
slug: amazon-custom-silicon-20-billion
category: business
story_number: "08"
date: 2026-06-30
sources:
  - name: About Amazon
    url: https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-amazon-chips-business-q1-2026-earnings
    domain: aboutamazon.com
  - name: Moneywise
    url: https://moneywise.com/news/top-stories/amazon-ceo-andy-jassy-annual-letter-nvidia-intel-ai-chips
    domain: moneywise.com
  - name: CNBC
    url: https://www.cnbc.com/2025/11/21/nvidia-gpus-google-tpus-aws-trainium-comparing-the-top-ai-chips.html
    domain: cnbc.com
  - name: TechCrunch
    url: https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/
    domain: techcrunch.com
  - name: Anthropic
    url: https://www.anthropic.com/news/anthropic-amazon-compute
    domain: anthropic.com
---

# Amazon's Custom Silicon Hits a $20 Billion Annual Run Rate as AI Chip Diversification Turns Real

For a decade, the received wisdom about the AI boom has been that one company collects the tolls. Every hyperscaler talked about building its own chips; every hyperscaler kept writing checks to Nvidia anyway. Amazon just put a number on the alternative. On its Q1 2026 earnings call, chief executive Andy Jassy disclosed that Amazon's custom silicon business — the Graviton CPUs, Trainium AI accelerators and Nitro security processors that AWS designs in-house — has surged past a $20 billion annual revenue run rate, roughly double the $10 billion figure the company cited only two quarters earlier and growing more than 100 percent year over year.

The eye-catching part was Jassy's counterfactual. "If our chips business was a standalone business and sold chips produced this year to AWS and other third parties as other leading chip companies do," he said, "our annual revenue run rate would be $50 billion." The gap between the two numbers is the whole thesis of vertical integration: Amazon captures the value internally as cheaper compute rather than booking it as merchant-silicon margin, which is why a business that would rank among the largest semiconductor firms on earth barely registers as a line item on AWS's income statement.

## Trainium moves from science project to backbone

The run rate is not a Graviton story dressed up with AI branding. Graviton, Amazon's Arm-based server CPU, has been quietly displacing Intel and AMD in AWS data centers for years — the "movie" Jassy has said he has seen before. But the acceleration this cycle is Trainium, the purpose-built chip for training large language models. Trainium2 supply is largely spoken for, and Trainium3, which began shipping in early 2026 and delivers what Amazon says is 30 to 40 percent better price-performance than its predecessor, is nearly fully subscribed.

What turned Trainium from a hedge into a business is a roster of anchor tenants that reads like the frontier-lab leaderboard. Anthropic has committed more than $100 billion to AWS over the next decade and is standing up nearly a gigawatt of combined Trainium2 and Trainium3 capacity by the end of 2026, much of it inside Project Rainier — a multi-gigawatt buildout that gives Anthropic access to more than a million Trainium accelerators for training Claude. OpenAI, which ended its Azure exclusivity, carved out 2 gigawatts of Trainium capacity within a $50 billion AWS commitment despite its deep roots in Nvidia's CUDA software. Meta and Uber have signed on as well, with Uber beginning to train models on Trainium3 in April. Even Apple confirmed it had moved Siri-tier inference onto Trainium2 — a consumer-grade reliability stamp that matters more than any benchmark slide.

## The economics of not paying full retail

The strategic logic is blunt. Nvidia's data-center GPUs carry gross margins reported in the neighborhood of 70 percent or more, which means every hyperscaler buying them is, in effect, financing a competitor's balance sheet. "Customers want better price-performance," Jassy wrote in his 2026 shareholder letter, framing Trainium as a cheaper path to the same result. "We've seen this movie before" — a pointed reference to AWS displacing Intel in general-purpose cloud computing.

Analysts are watching the trend line rather than any single quarter. Nvidia's share of AI accelerators, pegged near 87 percent in 2024, is expected to slip toward roughly 75 percent in 2026 as custom silicon eats into the general-purpose GPU market. Daniel Newman of the Futurum Group told CNBC he expects custom ASICs to grow "even faster than the GPU market over the next few years." The caution comes from the software moat: Bernstein's Stacy Rasgon has noted that Google spent a decade refining its Tensor Processing Units and remains the furthest along of any hyperscaler, a reminder that Amazon's toolchain still has to prove it can hold labs whose entire codebases assume CUDA.

## What to watch

June 2026 has clarified the shape of the market rather than settled it. Nvidia still owns general-purpose GPU training. Google's TPUs — now split into a training-focused 8t and inference-focused 8i — remain the most established custom alternative. OpenAI's Broadcom-built "Jalapeño" chip is aimed squarely at inference, and Qualcomm's acquisition of Modular signals a race to own the software layer that makes any of this silicon deployable. Amazon's distinct claim is the enterprise training alternative — the chip a serious lab can commit billions to without owning a fab.

Three questions will decide whether the $20 billion becomes $40 billion. First, whether Trainium3 supply can scale fast enough to convert signed commitments into recognized revenue without the power and packaging bottlenecks that constrain the whole industry. Second, whether Amazon's software stack matures enough to keep CUDA-native customers like OpenAI from drifting back to Nvidia for their hardest workloads. And third, whether Jassy acts on his not-so-subtle hint about selling Trainium to outside companies directly — the move that would turn that $50 billion counterfactual into a real income statement, and Amazon from Nvidia's biggest customer into its most credible rival.