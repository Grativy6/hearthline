# Add a bounded PAL v2.3 and CHARTER Lean audit summary

| Field | Value |
|---|---|
| Change ID | `HLP-000021` |
| Record kind | `PAL_CHARTER_AUDIT_SUMMARY` |
| Recorded date | 2026-09-07 |
| Predecessor | `HLP-000020` |
| Scope | `PUBLIC_DOCUMENTATION_POINTER_ONLY` |
| Record authority | `NONE` |
| Record effect | `LOCAL_AUDIT_SUMMARY_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added a short public pointer to three local Lean 4 checks of bounded PAL
  v2.3 and CHARTER v1.0 realizations.
- Recorded the aggregate target classifications and the limits of the checked
  PAL and CHARTER examples in plain language.
- Kept exact proofs, receipts, commands, and source reports in
  [PAL Lean Audit draft PR #11](https://github.com/Grativy6/PAL-Lean-Audit/pull/11),
  with its [immutable report](https://github.com/Grativy6/PAL-Lean-Audit/blob/e00ffc6c506e9801c745856c0090688336e61850/docs/generated/pal-v23-charter-local-checks.md)
  and [reproduction note](https://github.com/Grativy6/PAL-Lean-Audit/blob/e00ffc6c506e9801c745856c0090688336e61850/Audit/pal-v23-charter/PUBLICATION.md).

## Why

The audit results are useful as a small, reviewable summary for readers of
Hearthline, but detailed Lean evidence belongs with the audit that produced it.
This pointer lets readers distinguish a bounded model check from a claim about
the full frameworks.

## Preserved boundaries

- PAL v2.3 and CHARTER v1.0 retain their separately declared source roles.
- A checked countermodel only rejects a stronger inference in its stated
  bounded model; it does not contradict PAL, CHARTER, or Lean 4.
- The summary does not prove or contain PAL, amend either source, grant
  authority, activate a runtime, or create an adoption decision.
- O04 and O25 remain `OPEN`, and the results have partial source coverage.

## Compatibility and migration

This documentation-only successor adds no implementation, configuration,
runtime dependency, migration, or compatibility requirement. It links no
private receipt or workspace path and introduces no external service effect.

## Verification observations

- The summary reports 27 bounded theorem targets across three local runs:
  18 proved from declared rules, 4 assumption-bound, and 5 countermodels to
  overclaims.
- PAL examples retain fiber, projection, heartbeat, and checkpoint limits.
- CHARTER examples retain `n_m = 3m^2 + 3m + 1`, including
  `n_5 = 91 = 7 * 13` and the checked composite family
  `n_(7k+5) = 7(21k^2 + 33k + 13)`.
- Repository-local Markdown links and the public change-history structure are
  checked locally.

## Open residuals

- The linked audit PR #11 is open. Its CI was queued when this record was
  updated; this record preserves the report's local-check status and claims no
  CI result.
- The five countermodel targets share some constructions and are not five
  independent confirmations.
- Local Lean results remain limited to their declared realizations and do not
  close PAL obligations.

## Evidence and exclusions

The public evidence is a concise report of the local audit counts and bounded
examples. Exact Lean proof sources, execution logs, receipts, and generated
reports remain in PAL Lean Audit with the audit that produced them.

Credentials, private conversation, hidden reasoning, and local workspace paths
are excluded from this public summary. They are not represented as PAL Lean
Audit artifacts.

No remote service was activated, no runtime was changed, and no external effect
was authorized by this documentation-only record.
