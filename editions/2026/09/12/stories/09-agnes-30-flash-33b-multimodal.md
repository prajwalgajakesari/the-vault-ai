Agnes AI put a 33-billion-parameter multimodal model on Hugging Face under Apache 2.0 with a 262,144-token context window and a checkpoint that fits on a single H100. The architecture is the part worth reading: 72 decoder layers, of which only 18 run standard global attention. The other 54 run a gated delta rule — recurrent layers whose state size does not grow with the sequence. Three delta layers, one attention layer, repeat. The practical consequence is that a quarter of the stack carries a KV cache that scales with context, and the rest does not.

That ratio is no longer exotic. Qwen3-Next shipped the same 3:1 Gated DeltaNet-to-attention pattern a year ago, Qwen3.5 folded it into the mainline, and MiniMax has been mixing linear and softmax attention since M1. What is new is seeing it in a dense 33B open-weight release with a permissive license and a vision tower attached — the size class that actually lands on one rented GPU.

"Today we are introducing Agnes-3.0-Flash Preview, an open-weights multimodal preview model built for people who want flagship-class reasoning without flagship-class hardware," the model card reads. The highlights it claims: a 262,144-token window, adjustable reasoning effort, tool calling, and text, image and video understanding.

## Three different context windows, one model name

Before the benchmarks, the naming. There are two Agnes 3.0 Flash checkpoints in circulation and they are not the same model.

The Hugging Face repository now carries an explicit correction: it holds "an earlier open-weight Preview checkpoint," 33B parameters, 262,144 tokens, distinct from a newer production/API checkpoint. The repo was originally published as `Agnes-3.0-Flash` without the `Preview` suffix, and the card was amended after the fact to draw the line.

Which matters, because the widely circulated Artificial Analysis intelligence score of 36 is attached to the *other* one. The Artificial Analysis page for Agnes 3.0 Flash lists it as a proprietary model with a 1M-token context window, released September 11, credited to Sapiens AI, priced at $0.05 in and $0.15 out — and notes the weights are not publicly available. That page's own footnote marks the 36 as an estimate, with independent evaluation forthcoming. Agnes AI's developer documentation, meanwhile, states a 512K context window and a 65,536-token output cap.

So: 262K on the weights you can download, 512K in the vendor docs, 1M on the third-party leaderboard, and a headline intelligence score that belongs to none of the open files. The model card is unusually direct about this, warning that the published figures "are not results for the production/API Agnes 3.0 Flash model listed on Artificial Analysis." Anyone quoting "36" alongside "Apache 2.0" is splicing two models together.

## What the open weights actually score

On the card's own table, the Preview checkpoint posts 85.05 on GPQA Diamond, 74.20 on IFBench, 68.33 on AA-LCR, 38.08 on SciCode and 23.00 on AA-Omniscience accuracy. Against the comparison column for Qwen3.8-27B — a smaller model — that is 85.05 versus 90.5 on GPQA, 74.20 versus 79.5 on IFBench, and 68.33 versus 82.0 on long-context reasoning. Agnes trails on every row. Against Qwen3.6-35B-A3B it wins narrowly on four of five.

Agnes flags the caveat itself: the figures "were compiled from different sources, harnesses, and model snapshots and do not constitute a controlled head-to-head comparison." Competitive, not leading — and the card says so.

The lineage is also public. A community teardown of the weights reports that the Preview checkpoint carries the Qwen3.8-27B blueprint: same tokenizer, same chat template, a byte-identical vision tower, same embeddings and norms, with eight extra delta layers, a new parallel 2048-wide SwiGLU branch in every layer, renamed tensors and retrained projections. Both licenses are Apache 2.0, so this is entirely permitted. It does reframe what "new architecture" means here.

## The single-H100 claim, tested

The card recommends one H200 141GB or one H100 80GB at bf16, with roughly 66GB of weights on disk. That is tight. An independent benchmarker publishing as deluxetiky ran the checkpoint on a 96GB RTX PRO 6000 Blackwell and logged 66.2GB of weights, 10.12GB of SSM state and 335,517 fp8 KV tokens at full 262K context — a budget that does not obviously survive the drop to 80GB.

"Every number below is measured, not estimated — reproduce or falsify it on your own hardware," that card states. The numbers are unflattering on speed: 41.4 tokens/second single-stream warm median for Agnes at bf16, against 110.0 for an NVFP4-quantized Qwen3.8-27B on the same card; 145.9 versus 437.3 at four concurrent; a plateau near 125 tok/s at eight concurrent where the quantized Qwen reached 766. Both scored 4/4 on the quality battery. Agnes emitted 31% fewer tokens on hard reasoning, cutting a 2.6x per-token deficit to 1.56x in wall clock, and it kept 6/6 at `reasoning_effort=low` where the Qwen model dropped to 3/6 with thinking off. Prefill was cheap — roughly 45K tokens/second, 125K tokens in under three seconds cold.

Getting there is not turnkey. The checkpoint requires `trust_remote_code=True`, transformers 5.12 or later, and ships its own `serve.sh` plus a three-file patch that overlays SGLang's `qwen3_5.py` to register the `agnes` model type. After patching, the engine logs the model as `Qwen3_5ForConditionalGeneration`.

## What to watch

Eight community quantizations already exist — FP8, NVFP4, GGUF, MLX 4-bit. The bf16-only constraint is the binding one on this release, and the benchmarker's estimate is that FP8 or NVFP4 would roughly double or quadruple throughput. Whether Agnes ships its own quantized weights, whether the delta-rule path lands in upstream vLLM and SGLang without a patch, and whether the production 1M-context checkpoint ever opens are the three questions that decide if this is a durable self-hosting option or a well-documented curiosity. As of this writing the repo shows 34 downloads.
