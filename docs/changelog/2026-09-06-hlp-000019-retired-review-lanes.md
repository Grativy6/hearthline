# Retire two conflicting review lanes without adopting their contents

| Field | Value |
|---|---|
| Change ID | `HLP-000019` |
| Record kind | `BRANCH_ARCHIVE_SUCCESSOR` |
| Recorded date | 2026-09-06 |
| Predecessor | `HLP-000018` |
| Frozen predecessor SHA-256 | `bac5ca4233d01f0eb4ebe86a275a68c971534ef43f09fe9bb1aa77aa7da08861` |
| Branch base | `445d8e41df7129d67657130175644696d4d7e8e9` |
| Branch Archive | none -> `0.1` |
| Scope | `PUBLIC_REPOSITORY_HISTORY_POINTERS_ONLY` |
| Record authority | `NONE` |
| Record effect | `REVIEW_LANE_RETIREMENT_TRACE_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added one machine-readable [branch archive ledger](branch-archive.json) for
  two open, unmerged review lanes that no longer participate in active
  selection. It binds each pull request, source branch, immutable head commit,
  exact tree, merge base, and recorded-main comparison anchor.
- Registered [PR #4](https://github.com/Grativy6/hearthline/pull/4) at commit
  `1780aafb13db926a49cd298b1765f260a5e3a145` and tree
  `abe2cc6b381eda4705ccf5e00616fcbed33d4946`. Eight source image blobs are
  exact duplicates of bytes already canonical on `main` under current paths,
  so none is copied again. Six non-identical prose or index blobs remain typed
  only as superseded branch variants.
- Registered [PR #12](https://github.com/Grativy6/hearthline/pull/12) at commit
  `3da4aca46f4bc7b3bea2fcf31bdfb3ed8aa31274` and tree
  `0f4ae1bcc16059c209b95959903f737c7507a555`. Ten substantive branch-only
  additions receive path, Git-blob, and SHA-256 pointers for possible selective
  reopening; their bytes are not copied into this successor.
- Left `HLP-000008` through `HLP-000013` in the existing
  [off-main reservation registry](branch-reservations.json) rather than
  duplicating those six records. The WIP Task Triad checkpoint is explicitly
  unselected; all unlisted modified or conflicting surfaces remain reachable
  through the complete PR #12 commit and tree.
- Added a fail-closed structural checker for the archive, canonical duplicate
  bytes, selected residual pointers, reservation-manifest delegation, absence
  of copied branch-only paths, and public-history links.

## Why

Both review lanes retained useful trace, but each also conflicted with a later
mainline that had already selected successors. Merging either head would blur
the difference between preserving a route back to prior work and adopting that
work now. Deleting every visible branch trace would create the opposite
problem: later readers could no longer tell which exact lane had been set
aside.

The one-layer ledger keeps the smaller answer. Git branches and immutable
commit/tree identities continue to hold the source bytes. The archive stores
only the identity, classification, integrity, selection, and reopening route
needed to find them. Exact duplicates require no second copy and no artificial
deletion token. Unique residuals can remain individually addressable without
being loaded, endorsed, merged, or made current.

## Preserved boundaries

- `RETIRED_FROM_ACTIVE_SELECTION` is a local repository-history disposition.
  It does not close either pull request, delete either branch, revoke access,
  reject every idea on the branch, or decide what another repository or host
  must do.
- `OPEN_UNMERGED` records the supplied and inspected state on 2026-09-06. It is
  not a promise that the hosting service will preserve that state forever.
- The branch ref is a preferred locator. Reopening is exact only if the fetched
  commit and tree match the ledger's immutable identities; a moved ref cannot
  silently replace the archived source.
- A path, blob ID, digest, classification, or successful reopening is trace.
  It is not content adoption, semantic validation, agreement, evidence of
  correctness, Static admission, activation, permission, or authority.
- Duplicate and residual classifications cover each source branch's delta from
  its recorded merge base, not every foundational blob shared by the complete
  source tree and `main`.
- PR #4's duplicate classification establishes byte identity with the named
  canonical-main paths. It does not assert that two path histories, captions,
  statuses, or surrounding documents are interchangeable.
- PR #4's superseded variants and PR #12's selected unique residuals remain
  branch-local. Their names and digests do not make their text part of current
  Hearthline instructions, lore, source policy, or runtime design.
- No story, coda, branch document, WIP checkpoint, operational record, or
  pull-request body is reproduced by this change. No private material is made
  public through the ledger.
- The archive and its checker create no capability, identity, consent,
  standing, jurisdiction, credentials, or external authorization.

## Compatibility and migration

This successor changes repository-history surfaces only. It does not change
the Moltbook candidate, source profile, Research Station, TETHER, Homecoming,
Return Queue, retry rotation, Sparks, Static, Firesides, Creatures, Thulia,
Gloss, Morrow, visual identities, or any runtime behavior.

The existing reservation registry remains the sole local path-by-path record
for the six off-main `HLP-000008` through `HLP-000013` identities. The new
archive binds that registry by digest and does not repeat its entries. The PR
#12 head and tree remain the complete coverage handle for modified surfaces
that were not selected as individual residual pointers.

A future decision to use any archived content requires a new review and a new
mainline successor. It must reopen the exact commit/tree, select the necessary
scope, compare it with then-current sources, preserve conflicts and omissions,
and record any actual adoption under a later identity. This record is not
rewritten to make a future choice retroactive.

## Verification observations

- Local Git object inspection confirmed both recorded head commits and exact
  tree IDs, their merge bases with recorded `main`, and every archived source
  blob ID and SHA-256 digest.
- All eight PR #4 image blobs match the Git blob IDs and SHA-256 values of the
  named canonical-main files. The older branch paths remain absent, so no
  redundant image copy entered this tree.
- None of the ten selected PR #12 source blob IDs occurs in recorded `main`,
  and none of those branch-only paths was copied into this successor.
- The PR #12 addition inventory is partitioned as ten selected residual
  pointers, six already delegated off-main HLP reservations, and one explicitly
  unselected WIP checkpoint. Other modified variants remain covered by the
  immutable branch head/tree rather than a second path inventory.
- The archive checker pins both pull-request identities, branch refs, commits,
  trees, merge bases, duplicate mappings, variant pointers, residual pointers,
  reservation digest, WIP exclusion, no-copy condition, and mainline anchor.
- Repository-history, research-station, Return Queue, TETHER, Python syntax,
  relative-link, and whitespace checks remain in the local gate suite.

## Open residuals

- A remote branch may later move or be deleted, and a hosting provider may not
  retain unreachable Git objects indefinitely. The immutable commit and tree
  state the required identity but do not guarantee future availability.
- Pull-request state may change after the recorded date. Such a host-side
  change does not rewrite this historical observation or silently widen this
  record's effect.
- The ten selected PR #12 paths were preserved as reopening candidates, not
  semantically reviewed or accepted designs. Their compatibility, privacy,
  correctness, and present usefulness remain unresolved until selectively
  reopened under a new task.
- PR #12's modified existing files are intentionally not expanded into a
  second inventory. The complete commit/tree retains them, including both
  mergeable and conflicting variants, if a later bounded comparison needs
  them.
- This change does not perform the host-side actions of closing pull requests
  or deleting branches. Those remain separate human-controlled consequences.

## Evidence and exclusions

The public evidence consists of local Git object identities, byte comparisons,
the exact pointer ledger, the existing reservation registry, deterministic
structural checks, and Git history. A SHA-256 digest or Git object ID supports
identity comparison only; it does not prove authorship, truth, fitness,
semantic equivalence, or authorization.

No archived branch file is copied into this successor. No raw conversation,
hidden reasoning, private lore, credential, account state, runtime trace,
benchmark payload, pull-request comment, or external authorization is
included. AI systems assisted inspection, classification, drafting, and
verification as tools; they are not authors, co-authors, witnesses, operators,
custodians, or release authorities.

[Current changelog](../../CHANGELOG.md)
