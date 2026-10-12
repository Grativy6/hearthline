# CPX v0.6 formal companion — local result

**33 declarations compiled; five modules passed kernel replay.** Completed 11 October 2026 (America/New_York). No selected theorem required a change to its intended mathematical statement.

The formal targets are the four scoped claim cards associated with manuscript SHA-256 `ecc4d45107d20e7d148efeee26491f8310c897785575511fc32bd290ca8ce5dc`. This is not verification of the whole manuscript. The source comparison was performed by Hearthline, the same collaborator who prepared the proofs; it is a self-review.

| Claim family | Declarations | Result and scope |
| --- | ---: | --- |
| Capsule decoding | 4 | Decoder existence on attained values exactly matches fiber constancy; empty-domain and collision controls pass. |
| Protected return | 4 | Projection preservation plus factorization preserves the answer; equality of answers need not preserve histories. |
| Optional information and diagnostics | 15 | Finite rational policy inclusion, zero-mass and cost controls, and the equal-accuracy counterexample pass. Both channels have accuracy 3/4; gross decision values are 3/16 and zero. |
| Question-relative resolution | 10 | Nonempty-account settlement, observational agreement, different intervention probabilities, and any finite passive sequence under shared inputs pass. |

## Evidence

Lean: `4.32.1`, release commit `f054605aea4b840552cca2e725580bffd1e1b704`. Mathlib: `520045ab14e26149ee970e2e617ca04b09bde5d6`. All nine dependency checkout revisions matched the pinned manifest, with no tracked changes observed in that check.

[audit/RESULT.json](audit/RESULT.json) records every theorem's exact axiom list, final proof-source hashes, tool identities, and compiled-object hashes. [audit/statements-and-axioms.txt](audit/statements-and-axioms.txt) is the actual successful report output. The five `audit/kernel-CPX.*.txt` files contain the actual named replay markers; their successful exits are recorded in the result.

Seven declarations have no axiom dependencies. The others use subsets of `propext`, `Classical.choice`, and `Quot.sound`. Universe-decorated raw axiom names are retained alongside the normalized declaration names. There are no admitted proof holes or extra unlisted axioms in the selected declarations.

## What failed before completion

The initial compilation stopped at a missing library instance for an empty finite domain. The first repair round stopped at invalid tuple-annotation syntax. The final round included one diagnostic pass, repairs to policy-enumeration instances and numeric-witness proof steps, then the full compilation.

All final proof modules compiled, but the report command rejected the unsupported display option `pp.width`. That failed receipt remains a failure. The reporting correction used `format.width` and normalized universe suffixes when comparing axiom names. Statement reporting and the first kernel replays then completed against the same unchanged compiled proof objects, within the final round's original 30-minute ceiling. No fourth proof-repair round or fresh proof compilation was used.

The private research shelf retains every command, exit, failed output, source snapshot and the complete source-to-formal review. The repository companion omits the unpublished manuscript and private filesystem paths. Publication does not change the frozen audit: its `LOCAL_ONLY` publication field describes the completed local execution, before this repository copy was shared.

## Limits

The kernel replay uses Lean's own checker and trusted cached imports. It is not an independent proof system or a fresh audit of Mathlib. The rational information theorem does not separately formalize arbitrary real utilities or its conditional-posterior restatement. The causal construction does not formalize an infinite stochastic process or prove the completeness of a supplied world set. The model pilot and broader CPX hypotheses remain outside these formal statements.

The capsule criterion, protected return, feasible-policy argument, and causal construction retain their inherited attribution; the Lean result does not establish novelty.
