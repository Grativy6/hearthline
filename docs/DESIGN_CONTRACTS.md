# Design contracts

These names describe bounded functions. They do not require a character, a
particular model or Chris's personal context. The documents retain their
declared versions and implementation limits. The [capability matrix](CAPABILITY_MATRIX.md)
separately identifies the operations supplied by the current package.

| Name | Function |
| --- | --- |
| [Sparks](HEARTHLINE_SPARKS.md) | Purpose-bounded workers with distinct read and mutation grants. |
| [Creatures](HEARTHLINE_CREATURES.md) | Manifest-bound formations with separate members, ledgers and budgets. |
| [Firesides](HEARTHLINE_FIRESIDES.md) | Scoped consultation over committed events and explicit carry. |
| [Static](HEARTHLINE_STATIC.md) | Exact source-bound decoding and separately governed representation changes. |
| [Thulia / Owl Scribe](HEARTHLINE_THULIA.md) | Partitioned custody and direction-bound translation without joining ledgers. |
| [Homecoming](HEARTHLINE_HOMECOMING.md) | Paired dispatch, bounded heartbeat and separate return/reconciliation/closure. |
| [Morrow / Return Queue](HEARTHLINE_RETURN_QUEUE.md) | Stateless order proposals; the controller retains admission and queue state. |
| [Ordered Lineage](HEARTHLINE_ORDERED_LINEAGE.md) | Typed identities, append-only versions, allocation and recovery. |
| [TETHER](HEARTHLINE_TETHER.md) | Exact reopening routes that preserve scope without renewing authority. |

The [history guide](HISTORY.md) preserves the complete mixed predecessors.
Editorial separation changes their presentation; it does not provide new
implementation evidence or broaden any formal result.
