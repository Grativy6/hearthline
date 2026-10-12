import Mathlib.Data.Set.Function
import Mathlib.Data.Finite.Defs
import Mathlib.Data.Fintype.Basic

/-!
CPX v0.6, section 3, claim CPX06-C1. Candidate source, PREPARED_NOT_RUN.
This inherited fiber-factorization criterion is not a new CPX theorem.
The decoder is defined only on attained capsules; no default answer is assumed.
-/
namespace CPX.Capsule

universe u v w

def Attained {X : Type u} {C : Type v} (c : X → C) :=
  {z : C // z ∈ Set.range c}

def lift {X : Type u} {C : Type v} (c : X → C) (x : X) : Attained c :=
  ⟨c x, ⟨x, rfl⟩⟩

/-- The paper's finite specialization, including an empty supplied domain.
Finiteness is retained for source fidelity; the proof itself does not use it. -/
theorem decoder_iff {X : Type u} {C : Type v} {A : Type w} [Finite X]
    (c : X → C) (a : X → A) :
    (∃ d : Attained c → A, ∀ x, d (lift c x) = a x) ↔
      (∀ x y, c x = c y → a x = a y) := by
  classical
  constructor
  · rintro ⟨d, hd⟩ x y hxy
    rw [← hd x, ← hd y]
    exact congrArg d (Subtype.ext hxy)
  · intro h
    refine ⟨fun z => a (Classical.choose z.property), ?_⟩
    intro x
    exact h _ x (Classical.choose_spec (lift c x).property)

/-- A constant capsule cannot decode two distinct Boolean answers. -/
theorem collision_blocks_decoder :
    ¬ ∃ d : Attained (fun _ : Bool => ()) → Bool,
      ∀ x, d (lift (fun _ : Bool => ()) x) = x := by
  intro hd
  have h := (decoder_iff (fun _ : Bool => ()) (fun x : Bool => x)).mp hd
  have impossible : false = true := h false true rfl
  cases impossible

def emptyCapsule : Empty → Unit := fun x => nomatch x
def emptyAnswer : Empty → Empty := fun x => nomatch x

/-- Empty attained values require no fabricated answer. -/
theorem empty_attained_decoder_exists :
    ∃ d : Attained emptyCapsule → Empty,
      ∀ x, d (lift emptyCapsule x) = emptyAnswer x := by
  apply (decoder_iff emptyCapsule emptyAnswer).mpr
  intro x
  cases x

/-- Extending that empty decoder to an inhabited ambient capsule type is impossible. -/
theorem no_total_empty_answer_decoder : ¬ Nonempty (Unit → Empty) := by
  rintro ⟨d⟩
  exact Empty.elim (d ())

end CPX.Capsule
