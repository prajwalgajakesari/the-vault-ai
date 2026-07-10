When the machine learning field's flagship conference handed out its highest honors this week, both of its Outstanding Paper Awards landed on the same subject: diffusion models, the mathematical engine behind nearly every modern image, video, and increasingly text generator. One of the two winners is not a splashy new model or a benchmark-topping system. It is a theory paper. And its central claim is that the accuracy-versus-speed tradeoff that has quietly constrained diffusion sampling for years can, in principle, be collapsed.

The paper, "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions," was written by Fan Chen, Sinho Chewi, Constantinos Daskalakis, and Alexander Rakhlin. Chen, Daskalakis, and Rakhlin are at MIT; Chewi is at Yale. It was recognized at ICML 2026 in Seoul, running July 6 through 11, alongside "The Flexibility Trap," a separate Outstanding Paper on diffusion language models. That two theory-and-analysis papers on diffusion swept the top prize is itself a signal of where the field's attention has moved.

## The barrier the paper breaks

To understand why this result matters, it helps to know what has been slowing diffusion models down. When one of these models generates an image, it starts from pure noise and gradually denoises it, step by step, following a learned "score" function — essentially the gradient of the log-probability of the data. Each step requires a call to a large neural network. The more steps, the more accurate the sample, but also the slower and more expensive the generation.

The problem is mathematical, not just engineering. Standard samplers work by discretizing a continuous differential equation, and that discretization introduces bias. To cut the error in half, you generally need far more than twice the steps. In the language of the field, reaching an error of epsilon required a number of steps that scaled polynomially in 1/epsilon — roughly 1/epsilon-squared for the most common methods. Accuracy came at a punishing price.

The award citation, written by the ICML program chairs, frames the achievement bluntly. The paper "settles a long-standing question in the theory of score-based sampling: whether epsilon-error can be achieved in polylog(1/epsilon) steps using only score (gradient) evaluations, rather than the poly(1/epsilon) steps that discretization-based samplers require." That shift — from polynomial to polylogarithmic — is an exponential improvement in how error scales with effort.

## First-order rejection sampling

The mechanism the authors introduce is called first-order rejection sampling, or FORS. Classical statistics has long had a tool for fixing discretization bias: Metropolis-Hastings correction, the accept-reject step at the heart of Markov Chain Monte Carlo. But that correction requires evaluating probability densities directly, and diffusion models do not give you densities. They give you scores — gradients — and nothing else.

FORS is a meta-algorithm that "simulates rejection sampling from first-order queries alone, bypassing density evaluations that previous high-accuracy methods relied on," the citation explains. The authors reframe the accept-reject decision as a "Bernoulli factory" problem, using unbiased estimators built from score differences evaluated along continuous paths. The upshot: high-accuracy correction becomes possible using exactly the score estimates that diffusion models already produce, with no architectural changes and no density queries.

The theoretical payoff is a sampler whose complexity scales as roughly the data's intrinsic dimension times polylog(1/epsilon) — and, as a byproduct, the first polylog(1/epsilon) gradient-only sampler for general log-concave distributions, a foundational class of problems in statistics and optimization far beyond generative AI.

## Why theory here reaches practice

It is tempting to file a result like this under pure math. But the through-line to deployed systems is unusually direct. As the citation notes, for diffusion models specifically the number of denoising steps needed "can in principle drop from polynomial to polylogarithmic in 1/epsilon, suggesting that highly accurate diffusion sampling can be obtained with a smaller number of function evaluations." Function evaluations are the currency of inference cost — every step is a forward pass through a large network. Fewer steps at the same fidelity means cheaper, faster image and video generation, and cleaner sampling for the diffusion language models that are emerging as rivals to autoregressive LLMs.

The independent analysis from the technical newsletter ArXivIQ called the work "a major theoretical milestone" that "bridges the gap between classic Markov Chain Monte Carlo error correction and modern diffusion models," while noting its implications reach into "molecular dynamics, structural biology, and high-precision physical simulations" where exact samples are critical.

There are caveats, and the authors are candid about them. Rejection sampling can suffer high rejection rates in high dimensions; the analysis assumes accurate score estimates across the whole data support, which real neural networks do not always provide in low-density regions. FORS is, for now, a proof that a better tradeoff exists rather than a drop-in production recipe.

Still, that is often how the theory-to-practice pipeline in generative AI works. Someone proves a thing is possible, sharpening the target; engineers then chase it. The barrier that has quietly capped diffusion sampling for years now has a crack in it, and an ICML award marking the spot.
