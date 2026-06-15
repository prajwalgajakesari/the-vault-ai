Microsoft has built a Surface laptop that can run a 120-billion-parameter language model without ever touching the cloud. The Surface Laptop Ultra, unveiled at the end of May and detailed further through the company's Build conference in early June, is the first Windows PC engineered around Nvidia's new RTX Spark superchip — a single piece of silicon that packs a Blackwell GPU, a 20-core Arm CPU and up to 128GB of unified memory into a chassis Microsoft says is as thin as a conventional ultrabook.

It is, by any reasonable measure, the most aggressive bet yet that serious AI work belongs on the device in your bag rather than in a distant data center.

## What's actually inside

The headline number is one petaflop of AI compute, measured in the FP4 precision format that modern AI models increasingly rely on. That figure comes from the RTX Spark superchip, which Nvidia formally unveiled at GTC Taipei on May 31. The chip pairs an Nvidia Blackwell RTX GPU — 6,144 CUDA cores and fifth-generation Tensor Cores with FP4 precision — to a 20-core Nvidia Grace CPU over the company's NVLink-C2C chip-to-chip interconnect. MediaTek, the Arm specialist, co-designed the custom CPU. The result, per Nvidia, runs the full CUDA and RTX software stack natively on Windows.

The piece that matters most for AI work is the 128GB of unified memory. Rather than splitting a fixed allocation between CPU and GPU, the pool is assigned dynamically to wherever a workload needs it. That is what lets the machine, in Microsoft's words, run "up to 120B parameter models locally" with as much as a 1-million-token context window — model sizes that until recently demanded a workstation GPU or a cloud API call.

Microsoft's Surface team frames the Ultra as a creator-and-developer machine first. The 15-inch mini-LED PixelSense Ultra touchscreen hits up to 2,000 nits of peak HDR brightness at 262 pixels per inch, which Microsoft calls the brightest display it has ever shipped. The laptop comes in Platinum and Nightfall finishes, keeps a full port array — HDMI, USB-C, USB-A, SD card and headphone — and promises all-day battery life from what Microsoft describes as an "ultra-efficient CPU architecture." Nvidia's broader RTX Spark spec sheet describes laptops as slim as 14 millimeters and as light as three pounds across the partner ecosystem, though Microsoft has not published the Ultra's exact dimensions or weight.

## A reinvented PC, or a marketing reinvention

Nvidia and Microsoft are pitching this as nothing less than a new category of computer. "The PC is being reinvented," Nvidia founder and CEO Jensen Huang said in announcing RTX Spark. "For forty years, you launched apps. Click. Type. With RTX Spark and Microsoft Windows, you ask — and the PC does the work."

Microsoft's Satya Nadella tied the chip directly to the company's long-running ambition. "Our goal is to deliver unmetered intelligence to every home and every desk with Windows," Nadella said. "RTX Spark marks a real breakthrough towards that vision."

The strategic logic is the word "unmetered." Cloud AI is, by definition, metered — every token costs money, every query travels off-device, and every workflow depends on a network connection and a provider's uptime. The pitch behind RTX Spark is that a sufficiently powerful local chip flips that equation: a 120B-parameter model running on-device incurs no per-token cost, leaks no data to a third party and works on an airplane. Nvidia's accompanying OpenShell runtime, paired with new Windows security primitives, is explicitly designed to let AI agents run "securely and privately on users' primary PCs" — and even to route sensitive queries to local models while disguising personal information in anything sent to the cloud.

That privacy-and-cost story is the real product here. The Surface Laptop Ultra is the showcase, but the platform spans laptops and compact desktops from ASUS, Dell, HP, Lenovo and MSI, all shipping this fall, with Acer and Gigabyte to follow. It also slots neatly into Microsoft's Copilot+ PC campaign, which has spent two years trying to make "AI PC" mean something concrete. Until now that mostly meant modest NPUs running small models. A device that runs a frontier-class open model locally is a different order of capability.

## The caveats worth keeping in view

A few things deserve skepticism. The petaflop figure is, per Microsoft's own footnote, a theoretical FP4 number that relies on the chip's sparsity feature — a best-case benchmark, not a guarantee of real-world throughput. Battery-life claims rest on internal testing of pre-release units. And the most conspicuous gap is price: neither Microsoft nor Nvidia has announced what the Surface Laptop Ultra will cost, and the device is officially a "pre-release product." A 128GB unified-memory machine with a Blackwell GPU is not going to be an entry-level purchase, and the absence of a number is telling.

There is also a quieter strategic story underneath the hardware. Nvidia's entry into the Windows-on-Arm market arrives as Qualcomm's exclusivity over Arm-based Windows chips has lapsed — a window Nvidia, with MediaTek's CPU expertise, is moving fast to fill. The Microsoft partnership gives it a flagship vehicle.

Independent developers, notably, are already on board. "RTX Spark laptops change the game by multiplying the amount of context processing and putting it directly into a beautiful, portable chassis," said Georgi Gerganov, founder of llama.cpp, the open-source inference engine that powers much of the local-LLM community. "Highly optimized models running locally through llama.cpp with RTX Spark's AI performance will unleash the next wave of personal, private agents."

## What to watch next

Three questions will decide whether this is a genuine inflection point or an expensive curiosity. First, price: the fall launch window means a number should land within months, and it will determine whether local 120B inference reaches developers or stays a halo product. Second, real-world performance — independent benchmarks of token-generation speed and sustained thermals on the thin Surface chassis, not theoretical FP4 peaks. Third, the software: Microsoft's Windows agent primitives and Nvidia's OpenShell only matter if developers like the OpenClaw Foundation and Nous Research actually ship the secure, on-device agents both companies keep promising. The hardware looks real. Whether the "personal AI computer" becomes a category — or a tagline — depends on what runs on it.
