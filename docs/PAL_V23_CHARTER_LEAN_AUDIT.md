# PAL v2.3 and CHARTER local Lean audit summary

## Scope

Christopher D. Pang's PAL v2.3 and CHARTER v1.0 remain the controlling source
texts for their declared roles. This page is a plain-language pointer to three
local Lean 4 audit runs. It does not reproduce their proofs or receipts.

The exact proof sources, commands, execution logs, receipts, and generated
report remain in the PAL Lean Audit repository:

- [Draft audit pull request #11](https://github.com/Grativy6/PAL-Lean-Audit/pull/11)
- [Immutable local-check report](https://github.com/Grativy6/PAL-Lean-Audit/blob/e00ffc6c506e9801c745856c0090688336e61850/docs/generated/pal-v23-charter-local-checks.md)
- [Immutable reproduction note](https://github.com/Grativy6/PAL-Lean-Audit/blob/e00ffc6c506e9801c745856c0090688336e61850/Audit/pal-v23-charter/PUBLICATION.md)

PR #11 is open. This summary preserves the report's stated local-check status;
CI was queued when this link was added, and no CI result is claimed here.

## What the local checks found

The three runs checked 27 bounded theorem targets: 18 were proved from the
declared rules, 4 were assumption-bound, and 5 were countermodels to
overclaims. Those five targets do not represent five independent confirmations;
some use shared constructions.

A countermodel here means that a stronger inference fails in a stated bounded
model. It does not mean a claim is stronger than Lean 4, and it is not a
contradiction of PAL or CHARTER.

For PAL, the checked realizations keep the limits visible: readable decoding
requires agreement within trace fibers; restoring a work projection need not
restore every state field; and repeating a heartbeat need not establish
progress. For CHARTER, the bounded arithmetic uses
`n_m = 3m^2 + 3m + 1`: 7, 19, and 37 are example values, while
`n_5 = 91 = 7 * 13`; the derived family
`n_(7k+5) = 7(21k^2 + 33k + 13)` gives a checked composite pattern.

## Boundaries and open work

These are partial source-coverage results from local checks, prepared as
proposals for Christopher's review. They do not prove or contain PAL, amend
either source, establish an adoption decision, or activate a runtime. O04 and
O25 remain `OPEN`.

## Reopening handle

Use the draft pull request and immutable commit-bound report above to reopen
the exact audit material. This page preserves only the bounded summary and its
limits.
