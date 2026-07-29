It began, as major mathematical news increasingly does, with a social-media post rather than a journal submission. Late on July 19, 2026, the Harvard number theorist Levent Alpöge published a short message on X that ended with the almost absurdly casual line, "hello there the jacobian conjecture is false thanx." Attached were three polynomials in three variables and a claim: this map, found with the help of an AI model, breaks a problem that had stood since 1939.

Within hours, mathematicians were checking the algebra by hand and by computer. By the weekend, the consensus was striking in its speed: the general form of the Jacobian Conjecture, one of the field's most stubborn open questions, is false — and the counterexample was short enough to fit in a single post.

## What the conjecture claimed

The Jacobian Conjecture is easy to state and famously hard to settle. Take a polynomial map from n-dimensional space to itself — a function whose outputs are polynomials in the inputs. The Jacobian determinant measures how the map stretches or folds space at each point. The inverse function theorem guarantees that wherever that determinant is nonzero, the map is locally reversible: zoom in far enough and it looks like a clean change of coordinates.

The conjecture asked whether local good behavior forces global good behavior. If the Jacobian determinant is a nonzero constant everywhere, must the map be globally invertible, with a polynomial inverse? Applied mathematician John D. Cook summed up the surprise in the counterexample's title: "Locally everywhere does not imply everywhere."

The question is usually credited to Ott-Heinrich Keller in 1939, which is where the "87-year-old" framing comes from, though a 2026 historical study traces the precise statement back to Ludwig Kraus in 1884. Stephen Smale thought it important enough to include as Problem 16 on his 1998 list of challenges for the 21st century. Decades of attempted proofs and reduction frameworks piled up. What no one had produced was a single explicit function that broke it.

## The counterexample

Alpöge supplied exactly that: a polynomial map from three-dimensional space to itself whose Jacobian determinant is the constant −2 everywhere — satisfying the conjecture's hypothesis — but which sends different inputs to the same output, violating its conclusion. Cook noted that the points (0, 0, −1/4) and (1, −3/2, 13/2) both map to (−1/4, 0, 0); other checkers found a third collision at (−1, 3/2, 13/2). A function that maps three distinct points to one output cannot have an inverse of any kind, polynomial or otherwise.

The counterexample disproves the conjecture for n = 3, and trivially for every dimension above 3 by leaving the extra coordinates untouched. Crucially, it leaves the two-variable case — the version closest to the historical starting point — untouched. "It's an amazing achievement," commenter Adam Ginensky wrote on Cook's blog, "but n=2 was the original connector and may be harder."

What makes the result so quickly accepted is that it is trivial to verify even though it was hard to find. A long proof can hide a subtle gap; a counterexample only has to survive the definition. Mathematicians reproduced the determinant identity in SymPy and Sage; Stanford's Jared Duker Lichtman publicly walked through the collision, and MathOverflow contributor Qiaochu Yuan called it symbolically easy to check. On the Secret Blogging Seminar, Berkeley-trained mathematicians David Speyer and Will Sawin were already dissecting the map's geometry within a day, with Sawin sketching "an almost elegant geometric construction" of it.

## What "AI-assisted" actually means here

The role of the AI model — Claude Fable, which Alpöge said he and a friend spent a morning querying — is where caution is warranted. As the AI-news outlet Kingy.ai stressed after reproducing the checks, "The public map checks out," but "the AI provenance is not yet auditable." Alpöge credited "Fable"; secondary coverage filled in "Fable 5," Anthropic's current model, though the original post did not specify a version. There is no formal paper, no released prompt transcript, and no official Anthropic announcement. How much the model searched, how much a human steered it, and how many failed candidates preceded the answer all remain unknown.

That gap matters for the history of AI, not for the mathematics. And it clarifies what this breakthrough is and isn't. The model did not "solve" the conjecture in any autonomous sense. As Cook put it bluntly: "Of course Claude doesn't know that it solved the conjecture. It didn't even solve the conjecture. It was an inanimate tool in the hand of a mathematician, just like a piece of chalk or a dry erase marker." Asked cold whether a counterexample existed, Claude reportedly denied one had been found.

The narrower, defensible claim is the interesting one: frontier models can be genuinely useful search partners in problems where success has an exact, checkable verifier. Here the artifact was a handful of integer-coefficient polynomials any mathematician could test — no need to trust the model, the company, or a benchmark.

## What to watch

Three things. First, whether Alpöge or Anthropic releases a transcript detailing how much the model contributed versus human insight — the single biggest open question. Second, the two-variable case, still standing and possibly the harder problem. Third, whether "verifiable-search" AI assists start toppling other long-open problems, which would mark a real methodological shift in how mathematics gets done.
