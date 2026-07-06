DeepSeek is back at the front of the open-weight pack, and it got there through code.

The Chinese lab's V4 Pro — and its maximum-reasoning sibling, V4-Pro-Max — has become the top open-weights model on the coding benchmarks developers actually watch. According to launch coverage of the April 24 release, V4 Pro posted roughly 80.6% on SWE-bench Verified, effectively matching the official number for Claude Opus 4.6 within margin and landing in GPT-5.5-class territory on agentic software tasks. On LiveCodeBench, DeepSeek reported V4-Pro-Max at 93.5% Pass@1 — the highest score of any model in the comparison set that circulated at launch.

Those figures cement a return to the frontier for a lab whose reputation was built on doing more with less. And they arrive attached to an unusually aggressive package: an MIT license, downloadable weights on Hugging Face, and pricing that undercuts the American frontier by roughly an order of magnitude.

## What DeepSeek Shipped

V4 Pro is a 1.6-trillion-parameter mixture-of-experts model with about 49 billion active parameters and a one-million-token context window, per launch analyses — making it, by DeepSeek's account, the largest open-weight model available. The architecture leans hard into efficiency: a hybrid attention scheme combining Compressed Sparse Attention and Heavily Compressed Attention that, in the one-million-token setting, DeepSeek says requires only about 27% of the single-token inference FLOPs and 10% of the KV cache of its own V3.2.

DeepSeek framed the release in characteristically modest terms. The company said both models are more efficient and performant than V3.2 thanks to architectural improvements, and have almost "closed the gap" with current leading models — "both open and closed" — on reasoning benchmarks, according to TechCrunch's coverage.

The price is the other headline. Reporting on the launch described a steep V4-Pro price cut that escalated an ongoing AI pricing war; several providers cluster around a blended $2.17 per million tokens, and analysts peg V4 Pro at roughly 7.2x cheaper than Claude Opus 4.7 and 8.6x cheaper than GPT-5.5 on output tokens. One important caveat: many of the headline benchmark numbers are vendor-run figures from the release window, not independent leaderboard entries, and vendor scaffolds routinely score above standardized harnesses.

## How It Stacks Up Against the Open-Weight Field

The open-weight coding race has gotten crowded. Z.ai's GLM-5.2, a 744-billion-parameter MIT-licensed model, has been the reference point in recent showdowns, scoring around 62.1% on the harder SWE-bench Pro and 81.0 on Terminal-Bench 2.1, per CodingFleet's June comparison. MiniMax M3 — pitched as the first open-weight model to fuse frontier coding with native video, image, and desktop operation — trailed at 59.0% on SWE-bench Pro but undercut GLM on price. Qwen3.5, Qwen3.7 Max, and Nvidia's Nemotron 3 Ultra round out a field where the best open models now land roughly 60–72% on SWE-bench Verified.

Against that backdrop, V4 Pro's ~80.6% on SWE-bench Verified is a clear step up on the coding axis specifically. Analysts describe it as "decisively the best open-weight model on coding and competitive programming, competitive on agentic tasks, and roughly 3–6 months behind the closed frontier on world-knowledge reasoning." In other words: not a clean sweep, but a coding crown.

## Why It Matters

The story here is less any single benchmark than what happens when frontier-class coding stops being a closed, metered product. Open weights mean self-hosting, fine-tuning, and no API dependency — a real option for compliance-heavy and data-sensitive deployments that cannot ship code to a US vendor's servers.

"DeepSeek V4-Pro has effectively closed the performance gap on critical tasks like complex math and reasoning, while aggressively leading the market on openness and inference costs," analysts noted. Omdia's Lian Jye Su called the launch a "rather predictable path," adding that "when frontier-adjacent AI becomes predictably cheap and predictably open, the economics of the entire industry shift."

That is the US-China dynamic in miniature. American labs still hold the top of the reasoning leaderboards, but they charge for it. DeepSeek is competing on a different vector — good-enough frontier capability, given away under a permissive license and priced to move. The Council on Foreign Relations flagged V4 as signaling a new phase in the rivalry precisely because openness and cost, not raw capability, are becoming the contested ground.

## What to Watch

Three things. First, independent verification: whether neutral harnesses reproduce the ~80.6% SWE-bench and 93.5% LiveCodeBench numbers, or whether they compress under standardized scaffolding. Second, the pricing war — if DeepSeek's cuts pull GLM, Qwen, and MiniMax down with it, closed labs face margin pressure they cannot easily match. Third, the reasoning gap: DeepSeek's own framing concedes a 3–6 month lag on world-knowledge tasks. If V4's successors close that too, the argument for paying frontier prices narrows to reliability and multimodality — and both are shrinking moats.