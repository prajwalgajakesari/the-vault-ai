# Anthropic Wants to Monitor Misuse Without Holding the Logs. Banks Keep the Keys.

For a year, Anthropic has been telling its largest customers that frontier models are dangerous enough to require surveillance. On September 1 it conceded the harder half of that argument: the surveillance can happen without Anthropic ever touching the evidence.

Enterprise Frontier Safeguards, or EFS, sends the activity data used for misuse detection into storage the customer already owns -- an Amazon S3 bucket, an Azure Blob container or a Google Cloud Storage account, sitting under the customer's own encryption keys, access policies and audit logging. Anthropic writes and runs the detection logic. The customer holds the logs, holds the keys, and decides who is ever permitted to look.

"Enterprise Frontier Safeguards gives us exactly what we asked for: our logs stay in a Wells-managed environment under Wells-managed keys," said Munish Kumar Sharma, chief information security officer at Wells Fargo. "We keep custody of our data while Anthropic operates the detection. That split is what lets our teams put frontier models to work safely and meet our obligations to customers, employees, and regulators."

That split is the entire product.

## How the Standoff Started

Earlier this year, Anthropic introduced 30-day retention of inputs and outputs for its covered models -- the Fable and Mythos families -- applying it even to customers holding zero-data-retention agreements. The reasoning was technical. Sophisticated misuse spreads across many sessions and accounts, so per-interaction analysis followed by instant deletion cannot catch it. Correlation requires memory.

Anthropic was blunt that this was not a data grab: it has never trained on enterprise data without explicit permission, the company said, and never will. Regulated buyers were unmoved. "The enterprises we worked with generally understood the safety and security value of data retention, but many -- especially in regulated industries -- found it difficult to use models with data retention," Anthropic wrote.

The competitive stakes were plain. Retention is a disadvantage in exactly the segment where Anthropic sells hardest. OpenAI reached a similar conclusion last month, unveiling Private Safety Processing to risk-check interactions without breaking ZDR commitments. Two frontier labs, one architectural idea, weeks apart.

## What EFS Actually Does

Anthropic says it designed EFS with more than 100 customers across financial services, healthcare, manufacturing, telecom, law, retail and the public sector, together with cloud partners at Amazon Web Services, Google Cloud and Microsoft Azure. The consultation spanned roughly a quarter of the Fortune 100 and every US global systemically important bank.

One design partner was the Analysis and Resilience Center for Systemic Risk, whose members include the chief information security officers of Goldman Sachs, Morgan Stanley, Citi, Bank of America and Wells Fargo.

"Eight of our members worked with Anthropic to define what it would take to run the most capable frontier models inside a systemically important bank: who holds the data, who holds the keys, what automated review can and cannot see, and under what conditions a human is ever permitted to look," said Scott DePasquale, ARC's president and chief executive.

Under EFS, automated systems analyze a rolling window of traffic for signals of serious misuse -- attempts to develop offensive cyber or biological capability, and signs of stolen or leaked credentials. Flags route directly to the customer's security team. No Anthropic employee reviews the content. Customer-owned storage, customer-managed encryption keys and fully automated review are each separately **opt-in**, and none of them change model behavior, API pricing or rate limits.

Anthropic charges nothing for EFS; customers pay their cloud provider for storage, reads, writes and egress like any other resource. Support is planned for Claude Code, Claude Enterprise, the Claude Platform, Amazon Bedrock, Google's Agent Platform and Microsoft Foundry. Access is by application, and rollout is phased through this fall, with eligible customers receiving interim zero data retention on Fable 5 and 5.1 until EFS is ready. Mythos remains under the earlier retention policy.

Stripe was among the launch names. Its head of security, Matthew Kemelhar, said EFS will let the company use covered frontier models while conversation logs stay in Stripe's own AWS environment, governed by Stripe's security controls.

## Why This Matters

Safety monitoring and data sovereignty have been treated as a zero-sum trade: either the vendor sees your traffic and can catch a credential-theft campaign unfolding across accounts, or it sees nothing and you are alone. EFS refuses the trade by separating custody from computation. Anthropic keeps the detection intelligence. The bank keeps the corpus.

The architecture is meaningful, and its limits deserve precision. EFS does not mean nobody analyzes your prompts. Anthropic's detection logic still reads them, automatically, inside infrastructure you control. What it means is that Anthropic does not retain them and no Anthropic human reviews them. Under most regulatory regimes that is a real distinction, because custody, key control and access logging are the load-bearing facts. It is not the same as the provider being blind.

It also moves labor across the table. Where Anthropic analysts once triaged flags, the customer's team now confirms real misuse and clears false positives. For a bank with a mature insider-risk function, that is a feature. For a mid-size firm without one, an alerting pipeline into a security team that does not exist is not a safeguard. As The Register noted, customers now carry the burden of verifying that the retention promise actually held.

There is a quieter implication. EFS tests whether Anthropic's case for monitoring survives decentralization. If detection works as well when a hundred security teams own the logs and the triage, centralized vendor custody was always a weaker necessity than stated. If it does not, the industry finds out through incidents nobody caught.

## What to Watch

Three things. Whether the phased fall rollout lands on time and at genuine parity across AWS, Google Cloud and Azure, since cross-cloud equivalence is the claim most likely to slip. Whether Mythos eventually moves under EFS or stays behind the older policy and becomes the model regulated buyers cannot touch. And whether supervisors accept the split at all. No bank examiner has tested this architecture yet, and a design praised by chief information security officers is not the same as a design cleared by their regulators.