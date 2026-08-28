Amazon's Ring built a product launch around a sentence you almost never hear from a company in the home-surveillance business: after 24 hours, it says, it can no longer decrypt your video either.

Ring announced TAKE — Throw Away the Key Encryption — on August 26, with a phased rollout beginning in September and default-on encryption for every Ring customer worldwide once complete. True end-to-end encryption, an opt-in since 2021, remains available for anyone willing to trade away cloud features. Default-on encryption at Ring's scale is a real improvement over the status quo. It is also a claim whose weight rests entirely on machinery the customer cannot inspect.

Under TAKE, footage is encrypted with content keys that rotate every five minutes — generated on-device on newer cameras, or on arrival in the cloud on older ones. Ring keeps a copy of those keys, but only inside an AWS Nitro Enclave, and only to run the cloud features a customer has switched on: Smart Alerts, Video Search, Video Descriptions. After 24 hours Ring's copies are destroyed, while the keys on the owner's enrolled phones, tablets and computers survive. If the user later asks Ring to process older footage, the app temporarily hands the key back, and Ring deletes it again when the job finishes. The scheme is built on Messaging Layer Security, the IETF's open group-encryption standard, which supplies forward secrecy through cryptographic ratcheting.

"People are always going to have questions about, like, how do you store it? How do you protect it?" Ring founder Jamie Siminoff told CNN. "As a company we've done, I believe, a really good job with that, but this is the physical way of now giving them confidence. This is the show, not just tell."

## What a Nitro Enclave is, and what it is not

Nitro Enclaves are isolated VMs carved out of an EC2 host. Amazon's TAKE white paper describes them as providing "no persistent storage, no interactive operator access, and no general network connectivity." Code inside an enclave can produce a cryptographic attestation — a signed measurement of exactly which image is running — and Ring's key service releases material only to an image that satisfies it. The paper is blunt about the intended guarantee: "a Ring operator, or a tampered image, cannot satisfy that attestation." Key records are signed such that quietly postponing the 24-hour ratchet forward invalidates them.

That is a meaningfully stronger posture than "trust our access controls." It is also a different threat model from end-to-end encryption, and the difference is not rhetorical. Under E2EE the provider never holds a usable key; the guarantee is arithmetic. Under TAKE the provider does hold the key — briefly, under conditions it authored, enforced by an enclave whose image it builds and measures, on hardware its parent company owns. Ring's promise reduces to two propositions no user can check: that the attested image does only what the paper says, and that deletion is deletion. Amazon has not published enclave image measurements outsiders could reproduce, and no independent cryptographer had published a review of the design in the first day after launch.

## Twenty-four hours is still a window

A key that exists for 24 hours is a key that exists for 24 hours. Federal preservation requests under 18 U.S.C. 2703(f) can compel a provider to hold records without a warrant, but a provider can only preserve what it currently has. TAKE converts Ring from a searchable retrospective archive into a rolling window: a demand that lands on Tuesday cannot reach back to Sunday. A demand that lands while the key is live is a different question, and Ring has not said publicly how it would handle one.

For customers on TAKE or E2EE, Ring says it can supply only "non-video information, such as basic subscriber information" in response to warrants, subpoenas and court orders. A spokesperson told Gizmodo the company would also produce encrypted video files. Absent keys, those files are noise. None of this constrains the customer: Ring's Community Requests program, run with Axon, still lets police ask users to hand footage over voluntarily.

## The record this is arguing against

In 2019, reports described broad employee access to customer recordings. In 2023, Amazon paid $5.8 million to settle FTC allegations involving a former employee who viewed thousands of videos of female customers and hackers who reached roughly 55,000 US accounts. Ring shut down warrantless footage requests through Neighbors in 2024, then restored police requests via the Axon partnership after Siminoff returned in 2025. In February, EFF senior investigative researcher Beryl Lipton wrote that Ring's AI features were "the latest entry in the company's history of profiting off of public safety worries and disregard for individual privacy." Ring cancelled a planned Flock Safety integration days later. A June class action over the Familiar Faces facial recognition feature is still pending.

TAKE touches almost none of that. It controls Ring's access to the account holder's video. It does not control what the account holder shares, and it offers nothing at all to the delivery driver, the neighbor, or the kid who walks into frame — the people with the least say and the most exposure. The AI still runs. It just runs inside an enclave for a day, rather than against a warm archive indefinitely.

## What to watch

Three things separate engineering from positioning here. Whether Amazon publishes enclave image measurements, commissions a third-party audit, or opens a bug bounty scoped to the enclave. Whether Ring's transparency reporting shows video productions to law enforcement actually falling once the rollout completes — the number that would prove the architecture rather than describe it. And whether the September rollout is genuinely worldwide, including jurisdictions whose data-access rules a 24-hour key lifetime would frustrate.

Ring chose a middle path, and middle paths are often where the honest engineering lives. It also chose to keep the keys just long enough to run the AI, then named the product after the part where it lets go.
