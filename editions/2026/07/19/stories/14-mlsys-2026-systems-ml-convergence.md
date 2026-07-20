# The Next Big Gains Aren't Coming From Bigger Models. MLSys 2026 Says They're Coming From the Systems.

The most quietly radical sentence in AI research this year is not about a new architecture. It closes a keynote abstract from Stanford and NVIDIA architect Christos Kozyrakis at MLSys 2026 in Bellevue: “Large gains in inference efficiency will come not from isolated improvements, but from treating hardware, systems, and models as an integrated stack.”

That is a thesis statement for the whole conference. The Ninth Annual Conference on Machine Learning and Systems ran May 17 to 22, and its accepted-paper list reads less like a machine learning program than a plumbing manifesto: fused kernels, KV-cache layouts, streaming multiprocessor budgets, prefill-decode disaggregation, vector index compression. Almost none of it involves adding parameters. Almost all of it finds multiple-x improvements in the machinery between the model and the silicon.

## The kernel layer is where the free money is

Start with attention, still the bottleneck layer of the Transformer. **FlashAttention-4**, from Ted Zadouri, Jay Shah, Vijay Thakkar and Tri Dao, exists because Blackwell GPUs broke the assumptions of its predecessor. The authors describe the problem as “asymmetric hardware scaling: tensor core throughput doubles while other functional units (shared memory bandwidth, exponential units) scale more slowly or remain unchanged.” The fix is not a better attention mechanism — it is redesigned pipelines, software-emulated exponentials, and 2-CTA MMA mode. Result: up to 1.3x over cuDNN 9.13 and 2.7x over Triton on B200 GPUs in BF16, hitting 1,613 TFLOPs/s at 71 percent utilization. Written entirely in CuTe-DSL embedded in Python, it also compiles 20 to 30 times faster than C++ template approaches.

The same Stanford lineage produced two more entries. **HipKittens**, from William Hu, Simran Arora, Christopher Ré and colleagues, asks whether tile-based kernel abstractions are NVIDIA-specific or general — and finds they port to AMD CDNA3 and CDNA4, competing with AMD's hand-tuned assembly and beating all available baselines by 1.2x to 2.4x in some settings. **ParallelKittens**, from Stuart Sul, Arora, Benjamin Spector and Ré, reports up to 2.33x on data- and tensor-parallel workloads and 4.08x on sequence-parallel — from “fewer than 50 lines of device code.”

Microsoft's **TokenWeave** (Raja Gond, Nipun Kwatra, Ramachandran Ramjee) targets a cost nobody advertises: tensor-parallel inference burns roughly 20 percent in communication overhead even across NVLink. By fusing AllReduce with RMSNorm — an operation the authors call “previously overlooked” — TokenWeave does the job using only 2 to 8 streaming multiprocessors on an 8xH100 DGX, delivering up to 1.28x latency speedup and 1.19x throughput. In several configurations it beats an equivalent model with all communication removed entirely.

## Memory hierarchy is the second front

If kernels are the first front, memory is the second. **Kitty**, a 15-author collaboration led by Haojun Xia, tackles 2-bit KV cache quantization, which normally wrecks long-context reasoning accuracy. Its Dynamic Channel-wise Precision Boost keeps a small fraction of sensitive Key channels at higher precision, paired with a page-centric layout. Across seven tasks on Qwen3 and LLaMA3, Kitty cuts KV memory nearly 8x with negligible accuracy loss, enabling 8x larger batches and 2.1x to 4.1x higher throughput at the same memory budget.

**LEANN**, from a Berkeley team including Ion Stoica, Matei Zaharia and Joseph Gonzalez, recomputes embeddings on the fly rather than storing them, shrinking vector index size by up to 50x while holding state-of-the-art accuracy — enough to make RAG viable on a personal device. And University of Chicago PhD candidate Yuhan Liu presented LMCache, an open-source KV caching layer already in production at more than 30 companies including Google Cloud, AWS and NVIDIA, reporting up to 15x throughput improvement combined with vLLM.

Not everything was triumphalist. NVIDIA's **Beyond the Buzz: A Pragmatic Take on Inference Disaggregation**, led by Tiyasa Mitra, evaluated hundreds of thousands of design points and found prefill-decode disaggregation — the year's most hyped serving pattern — is “most effective for prefill-heavy traffic patterns and larger models,” not universally.

## What the merger means for who wins

The scaling era rewarded whoever could buy the most compute. The systems era rewards whoever extracts the most from compute they already have — a more distributable kind of advantage. A 2.1x throughput gain from KV quantization is indistinguishable, on a cloud bill, from doubling your GPU fleet, and it is available to anyone who reads the paper and runs the repo. Kitty, TokenWeave and LEANN all shipped code.

That is why Microsoft principal researcher Esha Choukse framed her talk as a case for “rethinking the boundary between machine learning and computer systems, and for treating accuracy and quality as dynamic system-level quantities that can be traded against latency, cost, and energy.” Quality stops being a fixed property of a checkpoint and becomes a dial on a serving stack.

It also reframes the efficiency results circulating in July's research coverage. Secondary write-ups of ICML 2026 have highlighted a “selective activation sparsity” training method said to let models match ones three times their size on reasoning benchmarks — a claim we covered separately, and one worth treating cautiously until the primary paper is public. MLSys makes the same directional point with harder evidence: parameter count is no longer the variable doing the most work.

## What to watch

Three threads. First, cross-vendor portability — HipKittens suggests a single tile-based software layer across GPU vendors is achievable, the most credible threat to CUDA lock-in in years. Second, AI writing its own systems code: GPU MODE co-founder Mark Saroufim warned in his keynote that “very few AI-generated kernels are reliable enough to be used in production without significant human supervision,” even as papers like AccelOpt and FlashInfer-Bench build the feedback loops to change that. Third, Microsoft Research Asia's Lidong Zhou pushed the frame further: “MLSys showed how systems can accelerate AI. The next shift is broader: AI is beginning to reshape the practice of systems itself.”

The 2027 program will tell us whether that inversion holds. For now, the cheapest performance gain in AI is a well-written kernel.
