# Europe Just Spent €387.8 Million on an AI Supercomputer, and Skipped Nvidia

The European High Performance Computing Joint Undertaking signed a €387.8 million procurement contract on Aug. 31 for a machine called LUMI-AI, to be assembled in a former paper-mill town in eastern Finland. It will run on AMD Instinct MI430X GPUs paired with sixth-generation AMD EPYC processors carrying 256 cores apiece. There is not an Nvidia part in it.

That is the line that will get repeated. The more revealing detail is that nobody involved treated it as a decision worth defending.

## The Contract

EuroHPC awarded the deal to Bull, the French supercomputer maker, following a tender launched in May 2025. Finland had been picked as the host site back in December 2024. The system lands at CSC — IT Center for Science's new data center in the Renforsin Ranta business park in Kajaani, the same site that already houses LUMI, one of Europe's most powerful machines. Deployment is scheduled for the second half of 2027.

The performance target is aggressive: roughly ten times the AI capacity of the existing LUMI system, and nearly double its conventional high-performance computing throughput. LUMI-AI will not replace LUMI. It will sit beside it.

The €387.8 million covers acquisition, delivery, installation and maintenance, and it is split down the middle. EuroHPC funds half, drawn from the EU's Digital Europe Programme. The other half comes from the LUMI AI Factory consortium — Finland, Czechia, Denmark, Estonia, Norway and Poland.

This is EuroHPC's sixth AI Factory procurement contract, and the Joint Undertaking is not being subtle about the ambition.

> With LUMI-AI, EuroHPC JU has now signed its sixth AI Factory procurement contract for a next-generation AI-optimised supercomputer. Together, these systems will form a powerful European AI infrastructure ecosystem, enabling SMEs and startups to access world-class supercomputing resources, unlock the full potential of AI, and drive innovation, growth, and technological leadership across Europe.
>
> — Anders Jensen, Executive Director, EuroHPC JU

## What They Are Building

The machine is a BullSequana XH3500, Bull's newest liquid-cooled architecture. The GPUs are AMD's next-generation Instinct MI430X, not yet shipping in volume. The CPUs are 6th Gen EPYC parts at 256 cores each. Interconnect is BXI, Bull's own fabric and, per the company, the only European-designed high-bandwidth low-latency interconnect built for HPC and AI. Storage comes from IBM Storage Scale. Nokia is supplying data center networking.

Beyond the AMD silicon, almost every layer is European or, in IBM's case, a legacy partner rather than a hyperscaler.

Cooling is warm-water direct liquid, a Bull patent. Waste heat gets pushed into Kajaani's district heating network. The system runs entirely on renewable electricity. Alongside it, IQM is delivering LUMI-IQ, a quantum computer housed in the same building and integrated with LUMI-AI to form a hybrid HPC-AI-quantum platform.

CSC's managing director framed the pairing as the point of the exercise.

> LUMI-AI's modern capabilities combined with the LUMI-IQ quantum computer will help European researchers and industry tackle unforeseen research and innovation challenges in key fields such as health, climate and disruptive technologies.
>
> — Kimmo Koski, Managing Director, CSC — IT Center for Science

## Why This Matters

Start with the correction most coverage will need: Bull is not an Atos subsidiary. The French State completed its purchase of Atos's Advanced Computing business on March 31, 2026, for an enterprise value of up to €404 million including earn-outs. The company that just won Europe's newest AI supercomputer contract is, functionally, owned by a European government. That is not incidental to a procurement whose stated purpose is technological autonomy — it is the thesis.

Now the Nvidia question. The honest framing is that LUMI-AI is continuity, not defection. LUMI has run AMD Instinct accelerators since it came online in 2022, and its software stack, its tuned codes and its user community are all built on ROCm rather than CUDA. Switching to Nvidia would have been the disruptive choice, not the safe one. Kajaani is arguably the single largest installed base of AMD HPC expertise in Europe.

What is genuinely notable is that the bet compounded. A 2021 procurement decision, made when AMD's data center GPU business was a rounding error against Nvidia's, has now produced a second-generation follow-on at four times the price tag. That is what vendor lock-in looks like when it runs in the underdog's favor — and it is the strongest argument AMD has for why sovereign buyers should pick it a third time.

AMD, for its part, is selling the openness angle hard.

> Europe's next wave of AI innovation will depend on infrastructure that is open, efficient and trusted.
>
> — Thomas Zacharia, SVP, Global Public Sector and Strategic Partnerships, AMD

There is a self-interested edge to that. AMD's ROCm is open source; CUDA is not. For a European institution whose entire remit is reducing dependence on foreign proprietary stacks, that distinction does real political work — arguably more than any benchmark. Bull CEO Emmanuel Le Roux made the same pitch in blunter terms, describing the company's mission as strengthening Europe's technological autonomy.

The strategic context is that EuroHPC is now running 19 AI Factories with 13 additional Antennas, and it opened tenders for full AI Gigafactories at the end of July. LUMI-AI is a mid-sized piece of a much larger buildout — and it establishes AMD as the incumbent going into those far bigger awards.

## What to Watch

Three things. First, whether the MI430X ships on schedule; the part is unannounced in volume, and a 2027 install date leaves little slack. Second, the Gigafactory tenders, where the money is an order of magnitude larger and Nvidia will compete aggressively for what LUMI-AI just conceded by default. Third, whether the 10x AI capacity claim survives contact with reality. EuroHPC has quoted a capacity multiple, not a FLOPS figure or a precision. Until Kajaani publishes numbers, the most concrete thing in this contract remains the price.
