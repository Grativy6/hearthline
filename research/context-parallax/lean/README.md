# Context Parallax Lean companion

**CHECKED LOCALLY — 11 October 2026.** All 33 named declarations compiled, their statements and axiom dependencies were recorded, and all five modules passed replay by Lean's own kernel. The source-to-formal comparison was a self-review. See [RESULTS.md](RESULTS.md) for the outcome, repairs and limits, and [audit/RESULT.json](audit/RESULT.json) for the machine-evidence summary.

Preparation labels inside the frozen proof headers and `THEOREMS.json` describe their original status; this dated result supersedes those labels. The proof-source bytes remain exactly those used for the final compilation.

The four source claims and their limits are:

| Claim | Target | Boundary controls |
| --- | --- | --- |
| CPX06-C1, section 3 | A decoder on attained capsules exists exactly when the protected answer is constant on each capsule fiber. | Colliding distinct answers; empty domain; no invented answer for an unattained capsule. |
| CPX06-C2, section 3 | A transformation preserving a supplied projection preserves a query that factors through it. | Equal answers with different histories; omission of either premise. |
| CPX06-C3, section 9 | Free optional information cannot lower optimal expected utility when all signal-dependent policies are available. | Single action, positive compulsory cost, zero-mass signals, equal diagnostic accuracy with unequal gross value. |
| CPX06-C4, sections 3 and 9 | One question can be settled while another remains open on the same nonempty account. | Empty accounts, matching observational tables with different interventions, arbitrarily long finite passive sequences. |

The decoder criterion and protected-return observation are inherited. The information result is a finite rational specialization; its algebraic helper needs fewer assumptions than its source-facing probability statement. The causal pair is an elementary non-identification example, with Pearl as the established antecedent. None is presented as a new mathematical discovery.

## Layout

`CPX/` holds five candidate modules. `CPX.lean` imports them. `THEOREMS.json` maps every named theorem to a claim and role. `Inspect.lean` prints every target's statement and axiom dependencies. `run_checks.py` defaults to preparation inspection. Execution requires its explicit `--run` flag after the work key is turned.

Lean is pinned to **4.32.1** and Mathlib to **520045ab14e26149ee970e2e617ca04b09bde5d6**. The manifest also pins transitive package revisions. The runner can reuse an existing matching dependency cache without changing that project or downloading dependencies.

## Preparation and later execution

With Python 3.11 or later, run `python run_checks.py --help` for the arguments. Supply the dependency project, installed toolchain directory and private source lock. Omitting `--run` performs static preparation checks only and invokes no Lean executable. A later authorized run also needs a fresh output directory; existing evidence directories are never overwritten.

The runner compiles each candidate, collects all statement and axiom output, and replays each module through the pinned Lean kernel checker. It records source bytes, dependency/tool identities, outputs and exit codes. An interrupted or failed run stays incomplete. The completed local run retains its failed attempts, final compilation receipt, and separate report-completion receipt; their relationship is explained in `RESULTS.md`. Repairs must retain the earlier attempt and keep the source-facing statements fixed, or explicitly report a translation change.

Kernel replay uses Lean's own checker and cached imported dependencies. It is not an independent kernel implementation, a full audit of Mathlib, or proof that the natural-language translation is faithful. That comparison is a separate recorded self-review.

## What these checks cannot establish

The model pilot, framing benefit, broader language-sustainability hypothesis, benevolence, private experience, and adequacy of a real-world model are outside these statements. Lean also cannot establish that a program's chosen utility accounts for everyone affected by it.

The manuscript, private source bindings, work key and local execution history remain on the research shelf outside this repository folder. Publication of this companion leaves the original local evidence intact: `LOCAL_ONLY` in the audit JSON describes the execution-time publication status, not a restriction on this repository copy. The reserved manuscript DOI is **10.5281/zenodo.23306102**; reservation does not imply publication.
