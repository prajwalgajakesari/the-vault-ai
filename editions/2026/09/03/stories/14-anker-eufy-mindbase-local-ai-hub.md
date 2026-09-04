# Anker Put 26 TOPS and 48 Terabytes in a Box So Your Camera Footage Never Leaves the House

The most interesting thing Anker showed at IFA Berlin on September 3 was not a camera. It was a card you can pull out with your fingers.

Under a lid on top of the new Anker MindBase, sitting beside the hard drive bays, is what the company calls its AI Core compute card: a 26 TOPS accelerator running a large language model Anker developed in-house. Everything else -- the router-shaped tower, the Matter 1.5 controller, the 48 terabytes of expandable storage -- follows from the bet that card represents: that analysis of your home security footage belongs in your living room, not somebody's data center.

"We believe the autonomous home needs three things: connection, local intelligence and memory that stays in the home under the family's control," Steven Yang, CEO of Anker Innovations, said in the announcement. "MindBase brings those together in one system and gives the home a true brain of its own that can understand what is happening across the home, make decisions locally, and coordinate the devices inside it."

## What Is Actually In The Box

The MindBase ships with 64GB of internal flash and takes up to 48TB of user-supplied storage -- 2.5-inch or 3.5-inch drives, spinning or solid state. Anker markets that layer as EverSafe Memory, and it is a real NAS, not a camera buffer: Brett White, a senior PR manager at Anker's IFA booth, told Gizmodo it is meant to store general files and even run apps, searchable in natural language. Owners of the older eufy HomeBase S380 can migrate their existing recordings over.

Connectivity comes through a software layer called EasyOmni Link, which Anker says reaches close to 100 of its own devices and hundreds of Matter products. As a Matter 1.5 controller the MindBase can run a smart home by itself, or attach to Apple Home, Google Home, Alexa or Home Assistant and present its devices onward. It handles 16 wireless cameras, plus four more over Ethernet if you add a PoE switch.

The agent architecture is deliberately modular. A NAS Agent and a Security Agent launch first, with an Energy Agent and a Clean Agent promised later. The security agent, Anker says, "evaluates events in real-time to assess risk and respond through observation, lighting, verbal warnings or active deterrence." The MindBase Security Kit pairs the hub with a new eufy TrackLight Cam S1 -- 4K, 180-degree dual-radar, with a light that tracks what it sees -- the Video Doorbell S4, entry and motion sensors, and a yard-edge Smart Security Shield that Anker says spots strangers at 15 meters and recognizes enrolled household members at 30.

## The Prices That Exist, And The One That Does Not

Here the announcement gets thinner than the marketing suggests. **Anker did not price the MindBase and did not say when it ships.** The hub, the TrackLight Cam S1, the Smart Security Shield and the Security Kit are all filed under details to be announced at a later stage.

What does have prices are the conventional products announced alongside it: the eufy NVR Security System E50, available now in the US, Canada and Australia at $999 for a four-camera kit or $1,199 with a 2TB drive, and $1,599 or $1,899 for the eight-camera versions; the Video Doorbell S4 at $299.99 with chime, arriving late September; and the Window Camera E10 at $69.99 later this year. A non-wearable millimeter-wave fall detection sensor for seniors was also shown, unpriced.

One more disclosure reframes the branding: the Eufy and Soundcore sub-brands are being retired, and everything becomes Anker. This is not the Eufy MindBase. It is the Anker MindBase, and its AnkaAI voice assistant is an expansion of software that until now lived only on Soundcore speakers.

## Why This Matters

Twenty-six TOPS is modest in isolation; Microsoft requires at least 40 for a Copilot+ PC. But TOPS budgets only mean something against a workload, and classifying events from a few camera feeds is not the job of a chat assistant. What 26 TOPS plausibly buys is the elimination of a round trip: no upload, no queue, no inference bill, no subscription. Anker is explicit that there is no monthly fee, and that is the commercially interesting part. Ring, Nest and Arlo all monetize the cloud leg. A vendor that moves inference onto hardware the customer already paid for is attacking that business model, not just a latency figure.

The claim that deserves scrutiny is the privacy one, because Anker has been caught on exactly this ground before. In November 2022, security consultant Paul Moore found that eufy cameras were uploading images to the cloud with cloud storage switched off, and that live streams could be opened in VLC. Anker spent two months giving The Verge answers the outlet characterized as misleading before admitting, on January 31, 2023, that its cameras had never offered the end-to-end encryption its marketing promised. The company said its web portal "now prohibits users from entering debug mode, and the code has been hardened and obfuscated," then added that only 0.1 percent of daily users touched that portal anyway. A class action followed.

Local processing is architecturally more private than cloud processing, but only to the extent it is actually local. A claim of no personal data sent to the cloud covers telemetry, model updates, remote access and companion-app behavior, not merely where a neural net executes. That is precisely the distinction eufy got wrong last time.

## What To Watch

Three things. Whether the MindBase gets a price and a ship date before CES in January, or quietly slips. Whether Anker subjects the box to the third-party audit and bug bounty it promised in 2023, and publishes the results. And whether that swappable AI Core card is a genuine upgrade path or a slot that never sees a second product. If it is real, Anker has something the incumbents cannot easily copy: a home hub whose intelligence can be replaced without replacing the cameras.