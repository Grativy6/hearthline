# ARC-AGI-3 handoff

Status: `PREPARED_NOT_RUN`

This repository does not run ARC-AGI-3. The shortest current route is the Hearthline Plays launch candidate:

- Repository: `Grativy6/hearthline-plays`
- Branch: `arc-agi/titles/arc-agi-3-hearthline-launch-20260903`
- Commit: [`97f580504e22bbd59b425274d6b5e0f9a18fe66e`](https://github.com/Grativy6/hearthline-plays/tree/97f580504e22bbd59b425274d6b5e0f9a18fe66e)
- Entry: [`launch/README.md`](https://github.com/Grativy6/hearthline-plays/blob/97f580504e22bbd59b425274d6b5e0f9a18fe66e/launch/README.md)
- Current status: [`launch/status/current.json`](https://github.com/Grativy6/hearthline-plays/blob/97f580504e22bbd59b425274d6b5e0f9a18fe66e/launch/status/current.json)
- Current source lock: [`launch/source-lock.v3.json`](https://github.com/Grativy6/hearthline-plays/blob/97f580504e22bbd59b425274d6b5e0f9a18fe66e/launch/source-lock.v3.json)
- Human gates: [`launch/gates/README.md`](https://github.com/Grativy6/hearthline-plays/blob/97f580504e22bbd59b425274d6b5e0f9a18fe66e/launch/gates/README.md)

## Current blocker

`RUNTIME_CLOSURE_UNFROZEN`

The exact private Kaggle wheel inventory, imported distribution closure, bundled Agents framework files, gateway, and scorer have not been observed and frozen in a reviewed post-stage successor. Gate B is unavailable.

At the pinned commit, phase is `OFFLINE_CANDIDATE_SOURCE_READY_HUMAN_GATES_CLOSED`, readiness is `NOT_KAGGLE_AUTHORIZED`, both human gates are closed, the competition/Kaggle phase is `NOT_AUTHORIZED_NOT_STARTED`, Kaggle contact count is zero, and private holdout access is false.

Three GitHub Actions runs at the exact commit succeeded on Ubuntu with Python 3.12: launchpad `33917834935`, launch kit `33917834892`, and research station `33917834890`. Those receipts establish bounded offline checks only. They do not close the runtime blocker or establish launch readiness.

Historical receipts record five anonymous public-practice contacts under an expired and spent grant. They are not Kaggle contacts, competition submissions, private evaluation, or authority for another contact.

## Human sequence

1. Begin from the exact clean candidate commit.
2. Package and verify it offline for the intended real account slug.
3. A human rechecks live rules and separately opens Gate A.
4. The human performs the private, non-competition stage.
5. Capture exact runtime, distribution, and bundled Agents inventory.
6. Review and freeze a successor source lock with status `FROZEN_POST_STAGE_SUCCESSOR`.
7. Regenerate and restage from that reviewed successor.
8. A human separately opens Gate B.
9. The human alone performs any authorized manual submission.

Gate A does not authorize Gate B. A successful local test or private stage is not a competition result.

## Do not substitute

- Do not run or stage from Hearthline core.
- Do not treat local untracked lookalikes as launch inputs.
- Do not infer readiness from a branch name, package build, passing test, or historical receipt.
- Do not reuse an expired or consumed grant.
- Do not expose credentials, private runtime inventories, raw frames, service identifiers, or holdout material in public Git.
- Do not claim a Kaggle run, private score, submission, or generalization result without its exact later receipt.

Reopen only through the pinned Plays source, then refresh its remote tip, status, source lock, rules, and human-gate state.
