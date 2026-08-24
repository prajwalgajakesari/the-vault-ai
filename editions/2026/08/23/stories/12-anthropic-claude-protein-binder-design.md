On a single assay plate at a contract lab outside Lausanne, a protein that Claude designed latched onto RBX1 with a dissociation constant of 3.9 nanomolar. RBX1, a subunit of the enzyme complex that tags other proteins for destruction, was recently the subject of an open competition in which just 9 of 245 human de novo designs bound at all. Anthropic had that competition's winning entry re-synthesized and measured on the same plate. It came in at 45 nM, roughly ten times weaker.

That comparison anchors "Autonomous de novo protein binder design with Claude," the technical report Anthropic released on August 18. Claude Opus 4.8 and an unreleased model called Mythos Preview designed binders against 16 targets, 30 ranked designs each. Two contract research organizations, Adaptyv Bio and Twist Bioscience, synthesized every design exactly as delivered and measured whether it stuck, blinded to which model produced what. One target, mature GDF-8, aggregated in the assay and gave nothing interpretable. Of the 1,320 designs across the remaining 15 targets, 354 bound: a 27% hit rate, against the 10-15% Anthropic cites as typical. Among designs Claude ranked first for each target, 49% bound.

## The autonomy is real, and it is bounded

Humans chose all 16 targets and handed each to Claude with nothing but a name, a UniProt accession, an organism, and an oligomeric state. Humans wrote the protocol prompt, roughly 30,000 tokens, only about a third of it scientific guidance and a reading list; the rest is scheduling, delegation, verification, and budget discipline. Humans provisioned the GPUs, $50,000 per multi-target campaign and $10,000 per single-target run, placed the orders, and read the binding data.

Everything in between was Claude's. The prompt specified no epitope, scaffold, target construct, or sequence. Claude researched each protein, picked where on its surface to bind, installed and ran the design software itself, and returned a ranked list. Running all targets at once over 48 hours with up to 12,500 H100-hours, Mythos Preview hit 26.7% and Opus 4.8 22.6%. Given one target at a time over 24 hours, Mythos Preview reached 35.1%, but with 2.8 times the compute per target. Focus and budget cannot be pulled apart.

Nor did Claude invent any of the machinery. Backbones came from PXDesign (358 designs), RFdiffusion3 (267), Genie 3 (185), FreeBindCraft, BoltzGen, the original RFdiffusion, and Proteina-Complexa. SolubleMPNN, the soluble variant of ProteinMPNN, wrote 1,133 of the tested sequences. Ranking used an ensemble of ESMFold2, ESMFold2-Fast, and Protenix v2.

That distinction drew the sharpest pushback. "a nice demonstration of Claude Science, but worth clarifying that the design is not 'done by Claude' but by orchestrating tool calls of open-source, task-specific protein design models: PXDesign, RFdiffusion, Genie, BoltzGen, etc," wrote Patrick Hsu, co-founder of the Arc Institute and a bioengineering professor at UC Berkeley, though he called the overall direction a good one.

## Where it broke

The failures are documented as fully as the wins. Against maltose-binding protein, whose smooth surface offers a binder almost nothing to grip, none of 90 designs bound. Against BBF-14, a beta-barrel that does not exist in nature and so has no evolutionary record to learn from, three bound, all weakly. Against 15-PGDH, exactly one binder, at 33.4 nM, still beating the 1.7 micromolar competition best.

The confidence scores Claude used to rank its work gave no warning. Designs against MBP and BBF-14 scored nearly as highly as designs against VEGF-A and TREM2, where 54 of 90 and 72 of 90 bound. "A confident co-fold was therefore a useful requirement for selection but not a guarantee of binding," the report states, "and experimental screening remains the only way to learn which targets a campaign has succeeded on."

TNF-alpha, a hard trimeric target where prior efforts reported zero hits, yielded 12 binders from 150 designs, the tightest at an apparent KD of 0.70 nM. All 12 came from Opus 4.8; Mythos Preview got none, and Anthropic says it does not know why. They trace back to only four distinct backbones.

Anthropic states its limits plainly: no matched human control, no structure solved, every binding pose a prediction, each model-format-target combination run once. "We did not run a matched campaign by human experts," the report says, "and we do not claim that Claude's designs are better than an expert would obtain with the same tools and budget." Four of the six competition results Claude was benchmarked against sat in its reading list. The work is self-reported and unreviewed.

Martin Shkreli, the convicted former pharma executive, called it "not impressive work" on X, arguing "affinities are quite low for peptidics" and that none reach targets inside cells.

## Why It Matters

The claim worth arguing about is not that AI designed a protein. RFdiffusion and BindCraft have done that for years. It is that a generalist model supplied the connective expertise that has gated the field: which tool to reach for, where to aim it, which candidates to order. Every model Claude used is open source, which is why the report argues such campaigns are now "within reach of laboratories that have targets of interest but no expertise in computational protein design."

The human has not left the loop. The human has moved. Problem framing, target selection, protocol writing, and the wet-lab bill remain human work, and much of the domain expertise now lives in the prompt rather than the model. Adaptyv Bio, which ran the validation, called this an "open-loop experiment": Claude designed, the lab measured, and Claude never saw the results.

## What to Watch

Whether anyone closes that loop, with an agent that designs, gets binding data back, and redesigns, is the next real test; Adaptyv already exposes an API and MCP server aimed at exactly that. Watch for independent replication: the prompts, designs and both labs' measurements are on Hugging Face. Watch for solved structures and for function, because binding is not activity and a minibinder is not a drug. And watch access, since protein design stays blocked on Claude Fable 5 as dual-use.