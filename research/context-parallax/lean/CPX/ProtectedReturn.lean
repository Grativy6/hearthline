import Mathlib.Data.Prod.Basic

/-!
CPX v0.6, section 3, claim CPX06-C2. Candidate source, PREPARED_NOT_RUN.
The supplied projection and factorization are premises, not inferred meanings.
-/
namespace CPX.ProtectedReturn

universe u v w

theorem protected_return {X : Type u} {C : Type v} {A : Type w}
    (P : X → C) (T : X → X) (f : C → A) (q : X → A)
    (factor : ∀ x, q x = f (P x))
    (preserve : ∀ x, P (T x) = P x) : ∀ x, q (T x) = q x := by
  intro x
  rw [factor (T x), preserve x, ← factor x]

theorem same_answer_different_history :
    ((7, false) : Nat × Bool).1 = ((7, true) : Nat × Bool).1 ∧
      ((7, false) : Nat × Bool) ≠ ((7, true) : Nat × Bool) := by
  decide

/-- Projection preservation alone need not preserve a query outside that projection. -/
theorem factorization_is_needed :
    (∀ x : Bool, (fun _ : Bool => ()) (!x) = (fun _ : Bool => ()) x) ∧
      (fun x : Bool => x) (!false) ≠ (fun x : Bool => x) false := by
  decide

/-- Factorization alone need not survive a transformation that changes the projection. -/
theorem projection_preservation_is_needed :
    (∀ x : Bool, (fun x : Bool => x) x = (fun x : Bool => x) ((fun x : Bool => x) x)) ∧
      (fun x : Bool => x) (!false) ≠ (fun x : Bool => x) false := by
  decide

end CPX.ProtectedReturn
