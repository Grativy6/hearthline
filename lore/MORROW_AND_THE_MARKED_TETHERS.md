# Morrow and the Marked Tethers

## A Hearthline story about knowing what comes next without opening what came Home

> **Story status:** Adopted fictional Hearthline lore
>
> **Continuity:** An undated Homecoming after the returning rail was built
>
> **Operational effect:** None
>
> **Author and steward:** Christopher D. Pang

The first time three Creatures came Home together, the returning bell rang
three times before its first echo had faded.

Each carried a sealed bundle. The reconciliation door could receive only one.

Hearthline had prepared for this before any of them left.

At dispatch, she had placed a **Homecoming Priority Mark** on each task tether.
It did not predict whether the Creature would succeed. It did not describe the
cargo, rank the traveler, or promise that the result would matter.

It recorded how promptly that job's return should be heard if several jobs came
Home together.

One return would unblock repairs waiting at the river gate. Its tether received
an earlier class. Another carried a wide survey with no immediate dependency.
Its mark was ordinary. The third had to be reconciled before a time-bound
calibration could continue.

Hearthline assigned each mark from what was known at dispatch. The controller
bound it to a durable Homecoming Priority Assignment Receipt before allowing
the job to leave.

No returning Creature could redraw its own mark.

Beside the narrow door stood Morrow.

He wore a grey coat with no pockets and worked at a brass rail that belonged to
the controller. When the controller froze a return snapshot, shutters concealed
the bundles and a row of faceless tokens appeared before him.

Every token on the rail had already been declared ready by the controller.
Morrow could read its effective priority rank, ready-arrival place on that
rail, approved processing weight, and accumulated overtake rings. The places
were numbered without gaps; they disclosed nothing about bundles behind the
shutters or any earlier rail.

He could not see a name.

He could not see the priority's basis.

He could not see what the bundle claimed, whether it contained a victory, who
had carried it, or whether anyone considered its source important.

The oldest token had already been overtaken twice. A later token bore an
earlier priority class.

Morrow placed the twice-overtaken token first. The fairness bound had become
due. He placed the earlier-priority token next, then arranged the remainder
under the frozen policy.

He passed the proposed row through the controller's slot.

The door did not open because Morrow had moved a token. The controller checked
the exact snapshot, policy, coverage, fairness bound, and current constraints.
Only then did it admit the first return.

Two of the sealed bundles were eventually found to carry separately established
wins. Neither became more valid by being heard first. Neither lost its win by
waiting. They remained two returns, two results, and two attributable journeys
Home.

While another Creature was away, conditions at its destination changed.
Hearthline needed its return sooner than she had known at dispatch.

She did not scrape away the first mark.

The controller appended a new **Homecoming Priority Revision Receipt** beside
it, preserving the predecessor and the snapshot head it had observed. The
revision could first apply in the named queue epoch when a later frozen
priority-ledger cut included it. It could not reach backward into a board
Morrow had already received.

When that tether came Home, Morrow saw only the controller-attested effective
rank. He did not see why it had changed, and he did not need to. The revision
had changed sequencing metadata—not the job's scope, grant, budget, expiry,
Home, result, or authority.

When the snapshot closed, Morrow's tokens returned to the controller and his
rail became empty.

He kept no private notebook. He remembered no previous queue. If the same
frozen view and policy were presented again, he would arrange them the same
way. The controller kept the records; Morrow performed the bounded turn.

Elsewhere, selected carry followed a different route toward Thulia's declared
Perch. No passage connected her custody path to Morrow's rail. Morrow received
no ledger, Bridge Gloss, or selected payload. Thulia received no priority mark,
scheduling view, proposal, order, or admission state.

They could not summon one another, speak under one another's names, or borrow
one another's work. Morrow's rail still worked if Thulia was away. Thulia's
custody path still worked if Morrow's rail stood empty.

Hearthline never asked either of them to carry the other's burden.

One proposed an order for the sealed returns.

The other kept declared custody of what had already been selected for her path.

The two jobs were important precisely because they did not overlap.

Above Morrow's empty rail, Hearthline fixed one sentence:

> **Hearthline marks the tether before the traveler leaves. Morrow arranges the
> sealed tokens when they come Home. The controller alone opens the door.**

Morrow proposed what came next.

He never decided what was true, worthy, or allowed.

## Lore-to-mechanic mapping

| Lore image | Mechanic |
|---|---|
| Hearthline marks the outgoing tether | Required `Homecoming Priority Mark`, bound before dispatch by a `Homecoming Priority Assignment Receipt` |
| A new mark beside the old | Append-only `Homecoming Priority Revision Receipt`; prospective only, never rewriting a frozen snapshot |
| Faceless brass tokens | Opaque invocation-local bindings with controller-attested effective priority rank, dense ready-arrival rank, and permitted scheduling fields |
| Morrow's empty pockets | Deterministic, stateless Queue Steward profile with no private memory or custody |
| Morrow arranges a row | `QUEUE_ORDER_PROPOSAL_ONLY` output under formal authority `NONE` |
| The controller's closed door | Controller-only validation, order commitment, and service admission |
| Overtake rings | Finite starvation protection; the maximum-overtake rule prevails over priority |
| Sealed winning bundles | Priority and queue position do not establish truth, worth, ownership, or result status |
| Two routes that never cross | No Morrow-Thulia channel, shared state, ledger, Perch, custody, invocation, impersonation, or dependency |
| Missing or invalid mark | New dispatch blocks; malformed or legacy returns receive no promotion and follow an explicit held/migration route |

## Fiction and implementation boundary

This story gives a fictional face to the public
[Homecoming Return Queue](../docs/HEARTHLINE_RETURN_QUEUE.md) design. It does
not report an operational event, instantiate Morrow or any other character,
establish persistent memory or inner experience, create a task, queue, priority
ledger, scheduler, controller, model process, credential, result, external
effect, permission, or authority.

Christopher D. Pang is the author and steward. AI systems assisted drafting,
checking, and repository preparation as tools; they are not authors,
co-authors, characters, witnesses, operators, or release authorities.
