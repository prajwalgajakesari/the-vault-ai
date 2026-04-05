Google has unveiled TurboQuant, a compression algorithm that solves one of the most pressing bottlenecks in LLM deployment: the explosive memory consumption of key-value caches during inference. The technique compresses KV caches to just 3 bits per value without sacrificing accuracy.

The algorithm achieves up to 8x performance increase over 32-bit unquantized keys on H100 GPU accelerators. Its two-stage approach uses PolarQuant (transforming vectors into polar coordinates) and a 1-bit error correction layer using Quantized Johnson-Lindenstrauss projections.

TurboQuant is a post-training quantization method requiring no retraining, fine-tuning, or calibration data. It works on any transformer architecture with zero model-specific tuning. Evaluation across LongBench, Needle In A Haystack, ZeroSCROLLS, RULER, and L-Eval showed 100% recall in needle-in-a-haystack tests up to 104,000 tokens.

A 6x reduction in KV cache memory means enterprises could serve six times more concurrent users per GPU. Google's reference implementation is expected in Q2 2026, coinciding with the algorithm's presentation at ICLR 2026 in Rio de Janeiro.

The release signals that the frontier of AI optimization is shifting from model architecture toward memory efficiency, where smarter algorithms deliver outsized wins.