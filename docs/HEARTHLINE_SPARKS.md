# Hearthline Sparks

> **One family. Three roles. As many names as the work requires.**

| Field | Value |
|---|---|
| Version | `0.2` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Sparks** is the family name for Hearthline's purpose-bounded bots. One such bot is a **Spark**.

The name gives related work a shared home without pretending that every helper is the same process, carries the same access, or possesses one continuous identity.

## The 1–3–∞ naming ladder

1. **One family:** Hearthline Sparks.
2. **Three roles:** Seeker, Explorer, or Handler.
3. **An open-ended naming space:** the job currently being carried, and—when Christopher chooses—the unique name of an important or long-lived Spark.

Ordinary Sparks are named by job and role: **Repo Seeker**, **Spine Explorer**, **Package Handler**. A lasting Spark may later earn a unique name, but its role, job, source, and grant must remain visible in the trace.

The infinity is poetic shorthand for open-ended names and work. It does not mean infinite running instances, self-replication, automatic promotion, unlimited concurrency, or authority.

## The three roles

| Role | Aperture | Ceiling |
|---|---|---|
| **Seeker** | Receives a brokered metadata view: names, paths, types, sizes, timestamps, modes, and already-computed digests when supplied | Does not open, search, preview, parse, render, or execute content; changes nothing |
| **Explorer** | May open and investigate content as well as metadata; may compare, report, and propose | Read-only; a proposed patch is not an applied patch |
| **Handler** | May receive the reads and persistent-mutation capabilities named in a separate current grant | May build, edit, move, or otherwise change only the expressly granted targets and structures |

A true Seeker may be shown a recorded hash, but it cannot compute a new content hash itself: calculation requires reading the underlying bytes and therefore crosses into an Explorer aperture.

These are consequence ceilings, not ranks that silently inherit one another. A Handler is not automatically allowed every Explorer read. Its grant must separately identify what it may inspect and what it may change.

A Spark carries one declared role at a time. Changing roles, widening scope, or moving from proposal to mutation requires a new explicit grant. A name describes a Spark; it never authorizes one.

## Hearthline Static

[Hearthline Static](HEARTHLINE_STATIC.md) is local, versioned shorthand that Hearthline may develop with one Spark through repeated work. Each Spark has its own Static ledger. Hearthline does not pool or silently carry its vocabulary into another Spark: a handoff must expand the meaning and bind it to source records before a receiving Spark can form new local shorthand.

Static changes none of the role ceilings. A Seeker may receive only brokered Static metadata within its existing aperture; an Explorer may inspect authorized records read-only; and a Handler may persist a Static record only under an explicit current grant naming that ledger and mutation. Static does not create shared memory, authority, or permission.

## Strongwiz and the meta layer

[Strongwiz](https://github.com/Grativy6/strongwiz) is a model-neutral, general-purpose operating layer: a laboratory body around whichever AI model is assigned to reason through difficult work.

The layers answer different questions:

| Layer | What it carries |
|---|---|
| **Reasoning model** | The inference and proposals produced for the current task |
| **Hearthline Spark** | The bounded family, role, and job identity under which work is carried |
| **Strongwiz** | Memory, experiments, receipts, authority boundaries, and reusable learned structure around the work |

Codex can supply reasoning without becoming Strongwiz. Strongwiz can preserve the laboratory and its receipts while the reasoning model changes. A future implementation could use Strongwiz to carry a Spark's work, but neither name presently implies that integration or grants the other authority.

That separation is why the meta arrangement matters: the model is not confused with the operational body, and the operational body is not confused with the permission to act.

## Grant and execution boundary

A Handler's role means persistent mutation is possible in principle, not preauthorized. Any real Handler grant should bind at least:

- the exact target and scope;
- permitted reads and mutations;
- destination or affected system;
- time, action, or budget limits;
- the applicable reviewer or executor boundary; and
- revocation and reopening conditions.

Anything omitted remains outside the grant. Handler status does not itself provide credentials, network access, publication, deployment, deletion, broad filesystem access, or external-action authority. Successful output cannot enlarge its own scope.

Reading content must not silently execute it. Opening a file does not authorize macros, imports, hooks, renderers, installers, links, or embedded instructions.

## Lore and implementation boundary

This document adopts Hearthline's naming language. It does not instantiate a Spark, implement access controls, activate a runtime, or authorize delegated work.

If Sparks become operational, the implementation must separately declare and test its role enforcement, task grants, custody, receipts, failure behavior, and revocation path. Until then, the names carry lore and design intent—not capability.

Sparks and Strongwiz are AI tools, not persons, co-authors, or independent authorities. Their names do not establish consciousness, consent, ownership, standing, or permission.
