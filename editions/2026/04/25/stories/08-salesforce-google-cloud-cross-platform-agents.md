# Salesforce and Google Cloud Enable AI Agents to Act Across Both Platforms

Enterprise software customers have long wrestled with a frustrating paradox: their most powerful tools live in separate ecosystems, and getting them to talk to each other usually means copying data, building custom middleware, or accepting that critical context will be lost in translation. On April 22, Salesforce and Google Cloud announced a sweeping expansion of their partnership that aims to dissolve those boundaries entirely -- enabling AI agents to execute end-to-end workflows across both platforms without moving data or forcing users to toggle between applications.

The announcement, made at Google Cloud Next '26 in Las Vegas, introduces a suite of integrations that thread Salesforce's Agentforce platform and Google's Gemini Enterprise together at the infrastructure level. The result is a system in which autonomous AI agents can pull context from CRM records, Google Docs, Slack threads, and Google Meet transcripts simultaneously, then take action across any of those surfaces.

## Bridging Two Ecosystems

The centerpiece of the partnership is bidirectional interoperability between Agentforce and Gemini Enterprise. Salesforce's Agentforce Sales agents can now operate directly inside Gemini Enterprise, engaging leads, creating meeting briefs, surfacing deal risks, and managing pipeline updates in real time -- all without requiring a user to leave Google's environment. The capability is already available in open beta on the Gemini Enterprise Marketplace.

Moving in the other direction, Gemini Enterprise is being embedded into Slack, Salesforce's collaboration hub. From within Slack, Gemini can act as a cross-platform assistant: summarizing a Google Meet transcript alongside a Slack conversation thread, pulling in data from Google Sheets, or drafting a Google Slides presentation based on inputs scattered across both ecosystems. That integration is currently in private preview on the Slack Marketplace.

Srini Tallapragada, Salesforce's President and Chief Engineering Officer, framed the partnership as a necessary step for enterprises adopting agentic AI at scale. "Businesses are ready to go all in on agentic AI, and that requires infrastructure and models that can operate across the entire enterprise," Tallapragada said. "Our deepened partnership with Google Cloud gives joint customers exactly that, so they can deploy Agentforce across every part of their business and accelerate their Agentic Enterprise transformation."

Thomas Kurian, CEO of Google Cloud, echoed that customer demand was the driving force. "Our mutual customers have asked us to be able to work more seamlessly across Salesforce and Google Cloud, and this expanded partnership will help them accelerate their AI transformations with agentic AI, state-of-the-art AI models, data analytics and more," Kurian said.

## Under the Hood: Zero Copy and Multimodal Reasoning

Two technical pillars underpin the integration. First, Agentforce will gain native access to data stored in Google's Lakehouse -- BigQuery and associated storage layers -- through what the companies call Zero Copy technology. Rather than replicating data between platforms, agents can read and act on information in place, reducing latency, cost, and the security risks inherent in data duplication. The IDMC Google BigQuery Connectors and Apache Iceberg GCP Support are available now, with Zero Copy for Google Lakehouse slated for late 2026.

Second, Agentforce is adding native support for Gemini models through its Atlas Reasoning Engine. This gives Salesforce's agents multimodal capabilities -- the ability to process text, images, and video -- powered by Google's foundation models. A customer service agent, for example, could analyze a photo of a damaged product submitted via email, cross-reference the customer's purchase history in Salesforce, and initiate a return workflow, all without human intervention. Gemini-powered reasoning for Agentforce is expected to be available in May 2026.

## The Broader Trend: Agentic Interoperability

The Salesforce-Google deal is the latest and most concrete example of a pattern taking shape across enterprise technology: the race to make AI agents platform-agnostic. As companies deploy autonomous agents to handle sales pipelines, customer support, procurement, and internal operations, the agents are only as useful as the data and applications they can reach. An agent confined to a single platform hits a ceiling quickly.

Google has been building toward this vision from multiple angles. At Cloud Next '26, the company also promoted its Agent-to-Agent (A2A) protocol, an open standard designed to let AI agents from different vendors communicate and collaborate. The Salesforce integration, while a bilateral partnership rather than an open protocol, advances a similar goal: agents that work across organizational and platform boundaries.

For Salesforce, the partnership extends a strategic pivot that accelerated in late 2025 when the two companies first announced deeper Agentforce-Gemini integration. That earlier agreement included a multibillion-dollar infrastructure deal that moved portions of Salesforce's workloads onto Google Cloud. The April 2026 announcement builds on that foundation with product-level integrations that customers can actually deploy.

## What It Means for Enterprises

The practical implications are significant. Sales teams using both Salesforce and Google Workspace will be able to interact with Agentforce agents without leaving Gmail, Google Docs, or Google Meet. A new Slackbot capability, expected at mid-2026, will let users turn any Slack request into polished Google Workspace content -- pulling from Slack threads, Google Slides, Docs, Sheets, or PDFs, structuring the information, and delivering a ready-to-share file.

The partnership also reduces a common friction point for IT departments: managing data governance across platforms. By keeping data in place through zero-copy access rather than replicating it, enterprises can maintain existing security and compliance controls without building new pipelines for every integration.

## What to Watch

The rollout is staggered. Agentforce Sales in Gemini Enterprise and Gemini Enterprise in Slack are available now in beta and preview, respectively. Gemini-powered multimodal reasoning arrives in May. The zero-copy data layer and Slackbot content generation follow in the second half of 2026. The cadence will test whether enterprises adopt these capabilities incrementally or wait for the full stack to mature.

More broadly, the deal raises competitive questions. Microsoft and OpenAI have their own vision of cross-platform agents through Copilot and the Azure ecosystem. Amazon Web Services is pushing agentic capabilities through Bedrock. The enterprise AI agent market is rapidly becoming a battle not just over model quality but over how many applications and data sources an agent can natively reach -- and how seamlessly it can act across them.
