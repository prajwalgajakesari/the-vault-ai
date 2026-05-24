# OpenAI Model Autonomously Disproves 80-Year Erdős Geometry Conjecture

*A general-purpose reasoning model cracked a problem that had stumped mathematicians since 1946 — and this time, the experts who exposed OpenAI's last embarrassing claim are vouching for the result.*

---

On May 20, 2026, OpenAI announced that an internal general-purpose reasoning model had autonomously disproved a famous conjecture in discrete geometry — a problem first posed by the prolific Hungarian mathematician Paul Erdős in 1946 and left unsolved for nearly eight decades. The proof, which has been independently verified by a panel of external mathematicians including some who previously and publicly embarrassed OpenAI over a botched math announcement, marks what the company calls "the first time AI has autonomously solved a prominent open problem central to a field of mathematics."

## The Problem That Stumped a Generation

The question at the heart of the breakthrough is deceptively simple: given *n* points arranged on a flat plane, what is the maximum number of pairs of those points that can sit exactly one unit apart? This is the planar unit distance problem, and Erdős himself described it as one of the best-known and easiest-to-explain problems in combinatorial geometry. Easy to explain, nearly impossible to resolve.

For 80 years, the accepted wisdom was that arrangements based on square grids — think the intersections of graph paper — represented the theoretical best case. The mathematical consensus held that the number of unit-distance pairs could grow only slightly faster than linearly as more points were added: technically, no faster than n raised to a power of (1 + o(1)), where that small correction term drifts toward zero as n grows. Erdős posed the problem in 1946, and his own lower-bound construction using that square grid approach had not been meaningfully improved since.

OpenAI's model changed that. It discovered an infinite family of point configurations that beats the grid, producing at least n^(1+δ) unit-distance pairs for infinitely many values of n — where δ is a fixed positive constant that does not vanish as n scales up. Princeton mathematician Will Sawin subsequently refined the result, showing that δ can be set as high as 0.014. The lower bound on the unit distance problem, frozen since 1946, has finally moved.

## The Cross-Field Leap That Stunned Experts

What made the proof surprising was not just that it worked — it was *how* it worked. Rather than grinding through geometry with brute computational force, the AI model made a conceptual leap into an entirely different mathematical universe: algebraic number theory, a deep branch of mathematics concerned with the structure of generalized number systems called algebraic number fields.

Erdős's original lower bound construction can be understood through Gaussian integers — complex numbers of the form a + bi — which encode a special symmetry useful for counting unit distances. OpenAI's model extended that idea into richer algebraic number fields, drawing on concepts such as infinite class field towers and Golod-Shafarevich theory, tools ordinarily associated with pure number theory, not planar geometry.

"Mathematics is a clear testbed for measuring AI's reasoning ability because mathematical problems require precise formulation, verifiable proofs, and logically coherent arguments from beginning to end," OpenAI wrote in its announcement. The company described the achievement as an example of AI "not merely providing an answer, but connecting ideas from disparate fields to generate mathematical discoveries."

OpenAI researcher Noam Brown was blunter about what the pace of progress implies. "Less than 1 year ago frontier AI models were at IMO gold-level performance," he posted on X. "I expect this pace of progress to continue."

## Credibility This Time: The Skeptics Are Onside

The announcement carries added weight because of who is validating it. Seven months earlier, in October 2025, OpenAI made a similar-sounding claim when its then-VP Kevin Weil declared on X that GPT-5 had solved 10 previously unsolved Erdős problems. That claim collapsed within days after mathematician Thomas Bloom — who maintains the authoritative Erdős Problems website — publicly called it "a dramatic misrepresentation," pointing out that the model had simply surfaced existing solutions from published literature rather than producing original proofs. Yann LeCun and Google DeepMind CEO Demis Hassabis both weighed in with pointed criticism. Weil deleted the post and left OpenAI entirely in April 2026.

This time, Bloom is one of the mathematicians who signed off on the result. So is Princeton combinatorialist Noga Alon, who described the unit distance problem as "one of Erdős's favorite problems" and called the solution "an outstanding achievement that settles a long-standing unsolved problem." Fields Medal laureate Tim Gowers contributed companion remarks, hailing the proof as "a milestone in AI mathematics." OpenAI published the companion document — signed by Alon, Bloom, Melanie Wood, and others — alongside its announcement.

Number theorist Arul Shankar perhaps put it most directly: current AI models, he said, demonstrate that they are "capable of going beyond being mere assistants to human mathematicians and generating and executing original ideas."

## Why This Matters Beyond Mathematics

The broader implication OpenAI is pressing is that the capability demonstrated here is not domain-specific. This proof did not come from a system fine-tuned for mathematics or a specialized theorem-proving engine. It came from a general-purpose reasoning model that was handed a written statement of the problem and told to work. That distinction matters: if the same class of model that handles business documents and code reviews can autonomously advance the mathematical frontier, the question of what else it can do — in biology, materials science, drug discovery, physics — becomes very live very quickly.

The upper bound on the unit distance problem, meanwhile, remains where it has stood since Spencer, Szemerédi, and Trotter placed it in 1984: O(n^(4/3)). Closing the gap between that ceiling and the newly raised floor is now the next open question — and the mathematics community will be watching to see whether AI plays a role there too.

Thomas Bloom, the mathematician whose public rebuke of OpenAI's 2025 claim became a cautionary tale for the whole industry, offered a characteristically measured but evocative take: "AI is helping us to more fully explore the cathedral of mathematics we have built over the centuries. What other unseen wonders are waiting in the wings?"

## What to Watch Next

The immediate question is peer review. The proof has been verified by a hand-selected external panel, but it has not yet been through formal journal review, and the full paper will need to survive scrutiny from the broader mathematical community before the result is fully settled. The upper bound on the unit distance problem — O(n^(4/3)) since 1984 — remains untouched, leaving a large gap that researchers will now be motivated to narrow. And OpenAI has not publicly named or released the model responsible for the proof, raising questions about reproducibility. For a company with a self-inflicted credibility deficit on math claims, the best thing it can do now is let the mathematics speak — and let the peer review process run its course.

---

*Sources: OpenAI (openai.com), TechCrunch, GIGAZINE, Interesting Engineering, AutoGPT*
