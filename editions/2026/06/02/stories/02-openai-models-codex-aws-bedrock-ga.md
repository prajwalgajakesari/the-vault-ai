---
headline: "OpenAI Frontier Models and Codex Go Generally Available on Amazon Bedrock"
slug: openai-models-codex-aws-bedrock-ga
category: business
story_number: "02"
date: 2026-06-02
authors:
  - name: The Vault AI Staff
sources:
  - name: AWS News Blog
    url: https://aws.amazon.com/blogs/aws/get-started-with-openai-gpt-5-5-gpt-5-4-models-and-codex-on-amazon-bedrock/
  - name: OpenAI Blog
    url: https://openai.com/index/openai-on-aws/
  - name: Help Net Security
    url: https://www.helpnetsecurity.com/2026/06/02/openai-models-and-codex-on-aws/
  - name: About Amazon
    url: https://www.aboutamazon.com/news/aws/bedrock-openai-models
  - name: ChannelLife Australia
    url: https://channellife.com.au/story/amazon-adds-openai-models-to-bedrock-for-aws-users
  - name: AI Weekly
    url: https://aiweekly.co/alerts/openai-gpt-55-and-codex-hit-ga-on-amazon-bedrock
---

# OpenAI Frontier Models and Codex Go Generally Available on Amazon Bedrock

**AWS becomes the first non-Microsoft cloud to offer OpenAI's most powerful models in production, as the two companies deepen a partnership that is reshaping the enterprise AI landscape.**

The walls between the world's largest AI lab and the world's largest cloud provider came down another notch on Monday. OpenAI's GPT-5.5, GPT-5.4, and Codex coding agent are now generally available on Amazon Bedrock, graduating from a limited preview that began on April 28 and marking the first time AWS customers can run OpenAI's frontier models in production workloads without leaving their existing cloud environment.

The move is significant not just for what it enables technically, but for what it signals strategically: OpenAI's once-exclusive relationship with Microsoft Azure is now firmly in the rearview mirror, and a multi-cloud future for frontier AI is the new default.

## What Shipped

GPT-5.5, which OpenAI positions as its most capable model for demanding reasoning and coding tasks, is available in the US East (Ohio) region. GPT-5.4, optimized for best price-performance on complex multi-step work, launched in both US East (Ohio) and US West (Oregon). Both models are accessible through the Responses API on Bedrock's next-generation inference engine, with pricing that matches OpenAI's direct first-party per-token rates and no additional fees from AWS.

Codex, the AI-powered coding agent that OpenAI says more than 5 million people use each week, is available through the Codex App, Codex CLI, and IDE integrations with Visual Studio Code, JetBrains, and Xcode. All inference routes through Amazon Bedrock infrastructure, with processing staying within the customer's selected AWS region for data residency compliance. Codex carries no seat licenses or per-developer commitments; charges are purely pay-per-token.

Critically, usage of all three offerings counts toward existing AWS cloud commitments, removing a procurement obstacle that has historically slowed enterprise adoption of third-party AI services.

## Enterprise Controls Front and Center

The GA launch inherits Bedrock's full enterprise governance stack: IAM-based access management, AWS PrivateLink connectivity, guardrails, encryption at rest and in transit, CloudTrail audit logging, and integration with existing compliance frameworks. Prompts and responses are not used to train models and are not shared with model providers, a guarantee that matters in regulated industries.

OpenAI emphasized the operational value of this approach. "As customers begin using these capabilities, the AWS path helps reduce friction around procurement, security review, and production readiness. By making OpenAI capabilities available within familiar AWS environments, organizations can spend less time navigating operational barriers and more time building," the company said in its announcement.

## Customers Already Moving

Several major enterprises signaled immediate interest. Sean Bruich, Senior Vice President and Chief Technology Officer at Amgen, pointed to the significance for scientific workloads: "OpenAI's GPT-5.5 and frontier models offer compelling advances in capability, quality and consistency that matter in a field where the questions are complex and the standards for scientific accuracy and decision quality are exceptionally high. Making these models available on AWS gives us an important new path to explore and scale those capabilities within the responsible AI framework, including security, governance and operational frameworks across the enterprise."

Autodesk is also evaluating the offering for its design and manufacturing workflows. Ritesh Bansal, Vice President of Analytics Data, Agentic AI and AI/ML Platform at Autodesk, said his teams are assessing "how frontier AI capabilities and AI-powered development tools on scalable, secure AWS infrastructure can help accelerate development workflows and support more informed decision-making for our customers."

## Why This Matters

Three dynamics make this launch worth watching closely.

First, it confirms that the era of exclusive cloud-AI partnerships is over. OpenAI ending its Microsoft-only arrangement and shipping production-ready models on AWS, with pricing parity, creates genuine multi-cloud optionality for enterprises that have been locked into one provider's AI stack. Organizations running on AWS no longer face a build-vs-migrate dilemma when they want access to OpenAI's models.

Second, the Codex integration transforms Amazon Bedrock from a model-hosting service into something closer to a full developer platform. With 5 million weekly active Codex users now able to route inference through Bedrock, AWS gains a potent hook into software engineering workflows that competitors will struggle to replicate without similar partnerships.

Third, the simultaneous launch of Amazon Bedrock Managed Agents, powered by OpenAI, signals that the two companies are not just sharing models but co-building production infrastructure for agentic AI. Box CTO Ben Kus noted this would enable "agents that continuously learn what works over time, tailor responses to each user's specific environment, and operate with the governance and auditability enterprises require."

## What to Watch Next

The companies have confirmed that the collaboration will deepen, with future OpenAI advances arriving on Bedrock as they become available. Perhaps most intriguing is the planned integration of Daybreak, OpenAI's cybersecurity initiative, through AWS, which would bring AI-assisted vulnerability validation into enterprise security stacks.

The broader question is how Microsoft responds. Azure still hosts OpenAI's training infrastructure and remains the default cloud for ChatGPT, but the competitive moat is narrowing with every model that ships on a rival platform. For enterprise buyers, the message is clear: the best AI models are becoming infrastructure-agnostic, and the real differentiation is shifting to governance, pricing flexibility, and operational integration. The AI model marketplace just got considerably more competitive.
