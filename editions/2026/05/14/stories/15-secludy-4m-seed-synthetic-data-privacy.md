---
headline: "Secludy Raises $4 Million to Let Financial Firms Train AI Without Exposing Customer Data"
slug: secludy-4m-seed-synthetic-data-privacy
category: policy
story_number: "15"
date: 2026-05-14
author: The Vault AI
tags: [secludy, synthetic-data, differential-privacy, financial-services, seed-funding, data-privacy, genai]
---
# Secludy Raises $4 Million to Let Financial Firms Train AI Without Exposing Customer Data

Banks want to train AI on their most sensitive data. Secludy just raised $4 million to make sure they never have to.

The San Francisco-based privacy-tech startup announced its seed round on May 13, positioning itself at the intersection of two forces reshaping financial services: the rush to deploy generative AI and the regulatory reality that the most valuable training data -- transaction histories, fraud patterns, loan files, customer support logs -- is also the most tightly controlled.

Impression Ventures, a fintech-focused firm based in Toronto, led the round. LAUNCH and The Syndicate, the venture firm and angel investing group led by Jason Calacanis, also participated, alongside Wedbush Ventures, Precursor Ventures, Hustle Fund, Script Capital, Mana Ventures, and Chispa VC.

## The Problem With Proprietary Data

Every major bank and payments company is under pressure to ship AI-powered products, from fraud detection models to customer service chatbots. But the datasets that would make those models most effective sit behind walls of compliance obligations, privacy regulations, and institutional risk aversion. In practice, that means enterprise AI deals stall during vendor evaluation and pilot phases because firms cannot share real customer data with outside partners or even move it freely within their own organizations.

"Every CEO is telling their teams to ship AI," said Ben Cerchio, founder and CEO of Secludy. "None of them want to be the one explaining a customer data leak on the next earnings call."

Cerchio would know the tension firsthand. Before founding Secludy, he spent his career in privacy and information security, most recently leading product privacy at TikTok and earlier working in information security compliance at PayPal. His co-founder and CTO, Mingze He, holds a PhD in computational biology with a machine learning specialization, conducted postdoctoral research at the Stanford Research Institute, and built enterprise AI systems at Williams-Sonoma.

## How Secludy Works

The company's platform generates synthetic data that statistically mirrors an organization's real datasets while guaranteeing that no individual customer record can be reverse-engineered from the output. The technical foundation is differential privacy, a mathematical framework that provides formal, provable limits on how much information about any single person can leak from a dataset. Unlike anonymization or masking techniques, which have repeatedly been shown to be vulnerable to re-identification attacks, differential privacy offers a quantifiable privacy guarantee.

Secludy deploys entirely within the customer's own cloud environment, meaning raw data never leaves the institution's infrastructure. The synthetic output can then be used freely for model training, fine-tuning, benchmarking, and vendor evaluation -- all without triggering the regulatory tripwires that stall most enterprise AI projects.

The approach is compliant by design with GDPR, CCPA, and HIPAA, a detail that matters enormously for firms operating across multiple jurisdictions with overlapping and sometimes contradictory data protection requirements.

## A Market in Rapid Expansion

Secludy enters a synthetic data market that analysts expect to grow aggressively. Multiple research firms estimate the global synthetic data generation market at roughly $635 million to $790 million in 2026, with projections reaching between $4.2 billion and $6.9 billion by the early 2030s, reflecting compound annual growth rates above 30 percent. Model training represents the largest application segment, accounting for an estimated 46 percent of market demand.

Financial services is a particularly acute pressure point. Banks and insurers sit on decades of proprietary data but face some of the strictest regulatory environments for sharing or repurposing it. That dynamic creates a large addressable market for any company that can credibly bridge the gap between data utility and data protection.

"We keep hearing the same thing from banks and insurers: they're sitting on decades of proprietary data and know they need to train models on it, but can't do it safely," said Christian Lassonde, Managing Partner at Impression Ventures. "That's the gap Secludy closes."

## Where the Money Goes

Secludy plans to use the $4 million to accelerate hiring, scale its go-to-market operation targeting banks, payments firms, and fintech companies, and expand the platform across additional enterprise AI workflows beyond its initial financial services focus.

The round is modest by 2026 standards -- the same week saw Anduril raise $5 billion and Cerebras debut at a $95 billion market cap -- but the thesis is narrowly targeted. Secludy is not building a general-purpose AI platform. It is selling a compliance-first data layer to institutions that have the data, the budget, and the regulatory mandate to care deeply about how that data gets used.

## The Bigger Picture

The rise of synthetic data startups reflects a broader reckoning in enterprise AI. The industry spent the past three years demonstrating that large language models can be transformative. The next phase is proving they can be deployed within the constraints that regulated industries actually operate under. Privacy is not a feature request -- it is a prerequisite.

For financial services firms, the calculus is straightforward: the cost of a data breach or regulatory penalty dwarfs the cost of generating synthetic alternatives. If Secludy's differential privacy guarantees hold up under production workloads, the company could become essential infrastructure for an industry that controls trillions of dollars in data-rich transactions but has barely begun to tap generative AI.

The seed round is a starting point, not a destination. But in a market where every bank is racing to deploy AI and none of them can afford to get privacy wrong, Secludy is betting that the safe path is the fast path.
