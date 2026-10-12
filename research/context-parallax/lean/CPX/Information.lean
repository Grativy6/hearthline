import Mathlib.Data.Finset.Max
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Pi
import Mathlib.Algebra.Order.Field.Rat

/-!
CPX v0.6, section 9, claim CPX06-C3. Candidate source, PREPARED_NOT_RUN.
Finite rational expected utility, fixed actions and all contingent policies.
The feasible-set argument needs neither posterior division nor independence.
-/
namespace CPX.Information

open scoped BigOperators

noncomputable def maximum {D : Type*} [Fintype D] [Nonempty D] (v : D → ℚ) : ℚ := by
  classical
  exact (Finset.univ.image v).max' (Finset.univ_nonempty.image v)

theorem le_maximum {D : Type*} [Fintype D] [Nonempty D] (v : D → ℚ) (d : D) :
    v d ≤ maximum v := by
  classical
  unfold maximum
  apply Finset.le_max'
  exact Finset.mem_image.mpr ⟨d, Finset.mem_univ d, rfl⟩

theorem maximum_le {D : Type*} [Fintype D] [Nonempty D] (v : D → ℚ) (b : ℚ)
    (h : ∀ d, v d ≤ b) : maximum v ≤ b := by
  classical
  unfold maximum
  apply Finset.max'_le
  intro z hz
  obtain ⟨d, _, rfl⟩ := Finset.mem_image.mp hz
  exact h d

def expected {W S A : Type*} [Fintype W] [Fintype S]
    (mu : W → S → ℚ) (utility : W → A → ℚ) (policy : S → A) : ℚ :=
  ∑ w, ∑ s, mu w s * utility w (policy s)

noncomputable def blind {W S A : Type*} [Fintype W] [Fintype S]
    [Fintype A] [Nonempty A] (mu : W → S → ℚ) (utility : W → A → ℚ) : ℚ :=
  maximum (fun a => expected mu utility (fun _ => a))

noncomputable def informed {W S A : Type*} [Fintype W] [Fintype S]
    [Fintype A] [Nonempty A] (mu : W → S → ℚ) (utility : W → A → ℚ) : ℚ :=
  maximum (expected mu utility)

/-- The stronger algebraic inclusion lemma does not require probabilistic masses. -/
theorem constant_policy_inclusion {W S A : Type*} [Fintype W] [Fintype S]
    [Fintype A] [Nonempty A] (mu : W → S → ℚ) (utility : W → A → ℚ) :
    blind mu utility ≤ informed mu utility := by
  apply maximum_le
  intro a
  exact le_maximum (expected mu utility) (fun _ => a)

/-- The source-facing probabilistic specialization keeps its declared premises. -/
theorem free_optional_information {W S A : Type*}
    [Fintype W] [Nonempty W] [Fintype S] [Nonempty S] [Fintype A] [Nonempty A]
    (mu : W → S → ℚ) (utility : W → A → ℚ)
    (_nonnegative : ∀ w s, 0 ≤ mu w s)
    (_normalized : (∑ w, ∑ s, mu w s) = 1) :
    blind mu utility ≤ informed mu utility :=
  constant_policy_inclusion mu utility

theorem zero_mass_signal_contributes_zero {W S A : Type*} [Fintype W]
    (mu : W → S → ℚ) (utility : W → A → ℚ) (policy : S → A) (s : S)
    (zeroMass : ∀ w, mu w s = 0) :
    (∑ w, mu w s * utility w (policy s)) = 0 := by
  simp [zeroMass]

theorem single_action_no_gross_gain {W S A : Type*} [Fintype W] [Fintype S]
    [Fintype A] [Nonempty A] [Subsingleton A]
    (mu : W → S → ℚ) (utility : W → A → ℚ) :
    informed mu utility = blind mu utility := by
  classical
  apply le_antisymm
  · apply maximum_le
    intro policy
    let a : A := Classical.choice (inferInstance : Nonempty A)
    have hp : policy = (fun _ => a) := funext (fun _ => Subsingleton.elim _ _)
    rw [hp]
    exact le_maximum (fun b => expected mu utility (fun _ => b)) a
  · exact constant_policy_inclusion mu utility

theorem compulsory_cost_can_hurt {W S A : Type*} [Fintype W] [Fintype S]
    [Fintype A] [Nonempty A] [Subsingleton A]
    (mu : W → S → ℚ) (utility : W → A → ℚ) (cost : ℚ) (positive : 0 < cost) :
    informed mu utility - cost < blind mu utility := by
  rw [single_action_no_gross_gain mu utility]
  exact sub_lt_self _ positive

end CPX.Information
