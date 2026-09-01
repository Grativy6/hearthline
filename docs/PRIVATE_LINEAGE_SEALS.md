# Private lineage seals

## Status and purpose

This document records the public format and limits of the Hearthline Workshop v1 private-lineage contract. This repository contains no real seal, secret key, hidden marker, signing key, verification claim, or sealed release.

The contract has one narrow function: compare an exact committed Git tree and an exact shared-key HMAC record. A matching HMAC is supplemental shared-key evidence, not a public-key signature. It does not authenticate a person, establish authorship or chronology, or grant authority.

For releases requiring public authenticity at publication time, a signed annotated Git tag with an independently pinned signing key is the recommended separate channel. The Workshop v1 lineage commands neither create nor verify signed tags.

## Committed-tree boundary

Creation and verification take an explicit full commit object ID and inspect the commit, its root tree, and all tracked leaf objects from the local Git object database. They recompute each selected commit, traversed tree, and blob object ID from its exact type, length, and bytes rather than trusting its storage name. They do not hash the worktree or index. Dirty, staged, generated, and untracked state is outside the record and remains `NOT_EVALUATED`; it neither enters the manifest nor invalidates an otherwise readable selected commit.

The tools disable replacement objects and lazy fetching and do not prompt or contact a network endpoint. A missing, malformed, unsupported, unreadable, or object-ID-mismatched local object fails closed. Only `sha1` and `sha256` Git object formats are accepted. Limits are 64 MiB for the selected commit object, 64 MiB of cumulative unique tree-object bytes, 100,000 tree occurrences, 100,000 leaf entries, and 256 MiB of total committed blob bytes. The verifier also limits a manifest to 64 MiB and a seal to 64 KiB.

Symbolic links bind the committed link-target blob bytes without traversal. Gitlinks bind only their recorded external commit object ID, not the contents of the external repository.

## Canonical JSON

Manifest and seal files use exactly the Workshop v1 canonical encoder:

```python
json.dumps(
    value,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=False,
    allow_nan=False,
).encode("utf-8")
```

This is the implementation's own strict JSON profile. Objects are encoded as UTF-8 with recursively sorted keys, no insignificant whitespace, no ASCII escaping requirement for non-ASCII text, no non-JSON numeric constants, and **no trailing line feed**. Verification rejects duplicate keys and rejects any input whose bytes differ from re-encoding the parsed value through this exact function.

## Manifest schema

A conforming manifest is one canonical JSON object with exactly these top-level members:

| Member | Type | Exact value or rule |
|---|---|---|
| `schema_version` | integer | `1` |
| `manifest_kind` | string | `HEARTHLINE_GIT_LINEAGE_MANIFEST` |
| `repository_id` | string | Caller-supplied stable identifier matching `[A-Za-z0-9][A-Za-z0-9._:/-]{0,199}` |
| `release_id` | string | Caller-supplied release identifier matching the same grammar |
| `release_sequence` | integer | `1` through `2^63 - 1` |
| `previous_seal_sha256` | string or null | Null for sequence 1; otherwise one 64-character lowercase hexadecimal digest |
| `coverage` | string | `EXACT_COMMITTED_GIT_TREE` |
| `git_object_format` | string | `sha1` or `sha256` |
| `commit_oid` | string | Full lowercase object ID of the selected commit |
| `tree_oid` | string | Full lowercase root tree object ID resolved from that commit |
| `path_encoding` | string | `GIT_RAW_PATH_BASE64` |
| `entry_order` | string | `RAW_PATH_BYTES_ASCENDING` |
| `entries` | array | Complete tracked leaf inventory, sorted and unique by decoded raw path bytes |
| `entry_count` | integer | Exact length of `entries` |
| `blob_bytes` | integer | Sum of the sizes of all blob entries |
| `key_commitment` | string | 64-character lowercase hexadecimal value defined below |

`repository_id`, `release_id`, `release_sequence`, and `previous_seal_sha256` are HMAC-bound but self-asserted context. Sequence 1 refuses a predecessor; every higher sequence requires one. The tool does not retrieve or verify the predecessor, prove chronology, enforce a unique history, or authenticate either identifier. Forks and omitted records therefore remain possible.

Each entry is one object with exactly:

| Member | Type | Exact value or rule |
|---|---|---|
| `path_b64` | string | Canonical padded RFC 4648 base64 of raw repository-relative Git path bytes |
| `mode` | string | `100644`, `100755`, or `120000` for a blob; `160000` for a gitlink |
| `type` | string | `blob` for file and symbolic-link blobs; `commit` for a gitlink |
| `object_oid` | string | Full lowercase Git object ID for `git_object_format` |
| `size` | integer or null | Exact nonnegative blob length; null for a gitlink |
| `sha256` | string or null | SHA-256 of exact blob bytes; null for a gitlink |

Decoded paths must be nonempty and relative, contain no NUL or backslash byte, and contain no empty, `.`, or `..` component. Paths are ordered and compared as raw decoded bytes, without filesystem case folding, Unicode normalization, locale ordering, or symlink traversal.

## Seal schema

A conforming seal is a second canonical JSON object with exactly:

| Member | Type | Exact value or rule |
|---|---|---|
| `schema_version` | integer | `1` |
| `seal_kind` | string | `HEARTHLINE_PRIVATE_LINEAGE_SEAL` |
| `manifest_sha256` | string | SHA-256 of the exact canonical manifest file bytes |
| `key_commitment` | string | Exact match to the manifest's commitment |
| `authentication` | object | Exact object defined below |

`authentication` has exactly:

| Member | Type | Exact value or rule |
|---|---|---|
| `algorithm` | string | `HMAC-SHA256` |
| `tag` | string | Full 64-character lowercase hexadecimal HMAC tag |

The exact seal file digest, called `seal_sha256` by Workshop results, is SHA-256 over the canonical seal file bytes. A later manifest may place that digest in `previous_seal_sha256`, but the pointer remains self-asserted unless the preceding record is separately supplied and evaluated.

## Key commitment and HMAC framing

The key is exactly 32 raw bytes. With `||` denoting byte concatenation, the implementation uses these exact domain byte strings, each including its final NUL byte:

```text
KEY_COMMITMENT_DOMAIN = UTF8("HEARTHLINE_LINEAGE_KEY_COMMITMENT_V1") || 0x00
HMAC_DOMAIN           = UTF8("HEARTHLINE_PRIVATE_LINEAGE_SEAL_V1")  || 0x00
```

The commitment is:

```text
key_commitment = lowercase_hex(
  SHA-256(KEY_COMMITMENT_DOMAIN || key)
)
```

For exact canonical manifest bytes `M`, the authenticated message is:

```text
message = HMAC_DOMAIN || uint64_be(len(M)) || M
tag = lowercase_hex(HMAC-SHA256(key, message))
```

`uint64_be(len(M))` is the manifest byte length encoded as exactly eight unsigned big-endian bytes. The HMAC covers the full canonical manifest, including its key commitment and self-asserted release context. It does not authenticate the seal file's other fields independently; verification separately requires the seal's `manifest_sha256` and `key_commitment` to match the supplied manifest.

## Detached files and key custody

During creation, the new manifest and seal outputs must be different, unused paths outside every Git worktree, Git directory, and linked-worktree common directory detectable from their destination. This prevents accidental versioning during construction and avoids a self-referential digest. They may later be deliberately published as release assets or committed in a later Git tree. That later commit creates a new Git context; it does not add them retroactively to the already sealed commit. Verification may read deliberately published manifest and seal files from a Git context; the key must still remain external.

The raw key must remain outside **every** Git worktree, Git directory, and linked-worktree common directory, not merely outside the repository being sealed. Key generation refuses an existing target and creates a new 32-byte file from the operating system's cryptographic random source at an explicit outside path. Use a fresh key for each release; the tool cannot prove uniqueness or safe custody. The key must not be committed, copied into a release, embedded in a seal or manifest, printed in logs, or treated as a watermark.

As a defense against straightforward accidental disclosure, creation rejects an exact raw key or its contiguous hexadecimal or standard/URL-safe base64 encoding in a selected-tree blob. That check is not a general secret scanner. It does not establish absence from Git paths, commit metadata or history, gitlink targets, unreachable objects, or split, transformed, compressed, or encrypted material.

The manifest and seal contain no secret key bytes. Their deliberate later publication exposes the complete HMAC tag and key commitment, but not the key.

## Signed-tag public channel

A separate signed annotated Git tag can bind the selected `commit_oid` together with the exact `manifest_sha256` and `seal_sha256`. Its signer must be verified against a public-key fingerprint pinned through a channel independent of the mutable repository. A hosting badge, account display, author field, unsigned tag, or public key introduced only inside the same repository is not an independent pin.

That signature provides public-key authentication of the signed tag data. It does not establish personal identity without the external pin, human authorship, originality, semantic correctness, adoption, activation, or authority. A signed tag and HMAC created by the same person or release process are two mechanisms in one lineage, not independent corroboration.

## Later key disclosure

If later public HMAC recomputation is desired, first retire the key from all new sealing and preserve or publish the exact manifest, full seal, and signed or independently archived pre-disclosure anchor. A separate disclosure record should identify the exact `key_commitment`, `manifest_sha256`, and `seal_sha256` it addresses. Original artifacts remain unchanged.

Disclosure can show that the revealed 32 bytes reproduce the commitment and HMAC of a **pre-existing anchored record**. It adds no authenticity or chronology beyond that earlier anchor. After disclosure, anyone can create fresh manifests and valid HMACs under the key, so a record first surfaced after disclosure has no private-lineage force from that key alone.

Disclosure does not prove who held the key, when a computation occurred, whether custody was exclusive, or whether the key was uncompromised.

## Claim limits

A successful Workshop v1 verification reports scope `EXACT_COMMITTED_GIT_TREE_OBJECTS_AND_SHARED_KEY_TAG_ONLY`. It can establish only that:

- the expected repository contains the declared commit and resolved root tree;
- the canonical manifest exactly matches the complete supported committed entry inventory;
- the manifest and seal digest fields match the supplied exact bytes;
- the supplied key reproduces the declared key commitment and HMAC tag; and
- caller-supplied repository ID, release ID, sequence, and commit match their HMAC-bound manifest fields.

It does **not** establish:

- worktree cleanliness, current branch state, remote freshness, or publication time;
- repository ownership, distributor identity, signer identity, human authorship, originality, copyright ownership, or trademark rights;
- key exclusivity, custody quality, non-compromise, forward secrecy, or non-repudiation;
- chronology, unique ancestry, historical continuity, independence, or completeness beyond the exact supported committed tree;
- source truth, semantic correctness, safety, conformance, peer review, or fitness for use;
- adoption, activation, deployment, consent, standing, jurisdiction, permission, or authorization; or
- official or canonical status for a fork, adaptation, account, service, or runtime.

Absence of a seal or HMAC does not establish absence from the lineage: an explicit token can be omitted, stripped, or lost. A matching subset does not establish that a later work copied the whole tree. Exact equality between two declared committed trees establishes byte equality under the comparison, not causal copying direction, exclusive origin, or preservation of anything outside those trees. These questions remain unresolved without separate evidence.

A mismatch establishes only that the supplied repository objects, manifest, seal, key, expected context, or canonical encoding do not form the declared comparison. It does not identify which input is wrong and must not be silently repaired.

Successful verification has `authority: NONE` and `effect: NONE`. Successful creation reports only the explicit local effect of creating detached manifest and seal files. Neither result is an adoption record, activation receipt, or authority source.

## Reopening

Any change to the committed tree, canonical manifest, repository or release identifier, release sequence, previous-seal pointer, key, schema, or authentication framing requires a new manifest and seal. Earlier records remain preserved. A new record never rewrites an earlier result or transfers its chronology, identity, canonical status, or authority.
