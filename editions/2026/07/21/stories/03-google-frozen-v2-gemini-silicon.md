# Google's 'Frozen v2' Chip Would Hardwire Gemini Straight Into Silicon

For fifteen years the guiding logic of AI hardware has been flexibility: build a general-purpose accelerator, then let software decide what runs on it. Google is now reportedly exploring the opposite bet. According to a report published Monday by *The Information*, the company is developing a server chip informally dubbed "Frozen v2" that would etch part of Gemini's architecture directly into the silicon itself — trading away flexibility in exchange for an efficiency leap engineers on the project estimate at six to ten times the tokens-per-watt of Google's newest Tensor Processing Units.

Google has not confirmed the project, and the numbers have not been independently benchmarked. But if the projection holds, it would rank among the largest single-generation efficiency gains the inference market has seen — and it would signal that at least one hyperscaler now believes its flagship model is stable enough to freeze into hardware.

## What "frozen" actually means

Modern AI chips make a cascade of runtime decisions as a query passes through a model: how to route tokens, how to schedule operations, how to move data between memory and compute. Those decisions are flexible precisely because the hardware doesn't know in advance which model it will run.

Frozen v2 would take some of those decisions for Gemini and fix them in the transistors themselves, cutting the number of steps the chip performs and the volume of data it shuttles around per query, according to the report. The scheduling and routing that a general TPU computes on the fly would instead be physically built into the circuitry. Less computation and less data movement is where the projected 6-to-10x tokens-per-watt improvement is said to come from.

Crucially, the chip freezes Gemini's *architecture*, not its *weights*. An earlier, more radical version of the concept — reportedly overseen by Google DeepMind chief scientist Jeff Dean — would have baked the model's weights directly into the silicon. Google set that proposal aside because a chip tied to a single frozen model version would have too short a useful life, per the report. Frozen v2's compromise leaves the weights updatable while hardwiring the underlying design, so the chip can serve future Gemini releases as long as their skeleton stays the same.

## The reporting is unconfirmed

Every figure here traces back to *The Information*'s two sources; Google itself has stayed noncommittal. A company spokesperson told the outlet that not every project moves into production and that "this rigorous exploration is central to our full stack approach" — an acknowledgment of the research culture without confirmation of a shipping product.

Deployment, if it happens, is targeted for as early as 2028. Google reportedly does not plan to manufacture Frozen v2 at anything like TPU volumes, viewing it partly as a trial run for more specialized silicon as model designs settle. The chip would sit alongside — not replace — Google's TPU line, which split into distinct training and inference variants with the eighth generation unveiled at Cloud Next in April. The project is also described as partly a response to an AI compute shortage severe enough that Google Cloud has turned down deals with outside customers.

## Why it matters

The economics of AI have quietly shifted from training to inference. Training a frontier model is a one-time capital event; serving it to hundreds of millions of users is a recurring cost measured in electricity. At that scale, tokens-per-watt is the metric that decides margins, and a 6-to-10x improvement — even a fraction of it in practice — would reset the unit economics of running Gemini. It would also ease the compute crunch that has Google turning away cloud customers.

It lands in the middle of a custom-silicon arms race. Nvidia still dominates, but every major buyer is building an escape hatch: Google has its TPUs, Amazon its Trainium and Inferentia, Meta its MTIA, and Broadcom has become the quiet enabler behind much hyperscaler ASIC design. Frozen v2 pushes that logic to its extreme — not a general accelerator that happens to run your model, but a chip that *is* your model. Model-hardwired inference silicon is no longer purely theoretical: Taalas, a Toronto startup that has raised more than $200 million from investors including Quiet Capital and Fidelity, launched its model-baked HC1 chip in February.

The trade-off is the whole story. A frozen chip is only as durable as the architecture it enshrines. If Google preserves Gemini's core design across versions, Frozen v2 keeps paying dividends for years. If a future Gemini adopts a fundamentally different structure — a new attention mechanism, a different routing scheme — the specialized silicon risks obsolescence the day the model changes. That is a bet on architectural stability, and the AI field's track record on staying still is short.

## What to watch

Watch whether Google confirms the project at all, or whether it surfaces only through further leaks. Watch for any independent benchmark of the tokens-per-watt claim, which remains a projection, not a measurement. Watch how committed Google stays to Gemini's current architecture in its next model generations — the single variable that determines whether a frozen chip is a masterstroke or a stranded asset. And watch the rivals: if Amazon, Meta, or a startup like Taalas signals a similar move toward model-specific silicon, "frozen" stops being an experiment and starts becoming a strategy.
