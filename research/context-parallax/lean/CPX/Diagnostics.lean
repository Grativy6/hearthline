import CPX.Information
import Mathlib.Tactic.NormNum

/-!
CPX06-C3 boundary fixture, section 9. Candidate source, PREPARED_NOT_RUN.
Exact reconstruction of the review counterexample, not a claim about model behavior.
False/true world = external cause/fault. False/true action = keep/revise.
-/
namespace CPX.Diagnostics

open CPX.Information

def symmetricMass : Bool → Bool → ℚ
  | false, false => 9 / 16
  | false, true => 3 / 16
  | true, false => 1 / 16
  | true, true => 3 / 16

def constantMass : Bool → Bool → ℚ
  | false, false => 3 / 4
  | true, false => 1 / 4
  | _, true => 0

def utility (fault revise : Bool) : ℚ :=
  19 / 10 - (if revise then 1 else 0) - (if fault && revise then 0 else 3)

def accuracy (mu : Bool → Bool → ℚ) : ℚ := mu false false + mu true true

theorem distributions_valid :
    (∀ w s, 0 ≤ symmetricMass w s) ∧ (∀ w s, 0 ≤ constantMass w s) ∧
      (symmetricMass false false + symmetricMass false true +
        symmetricMass true false + symmetricMass true true = 1) ∧
      (constantMass false false + constantMass false true +
        constantMass true false + constantMass true true = 1) := by
  constructor
  · intro w s; cases w <;> cases s <;> norm_num [symmetricMass]
  constructor
  · intro w s; cases w <;> cases s <;> norm_num [constantMass]
  norm_num [symmetricMass, constantMass]

theorem equal_accuracy : accuracy symmetricMass = 3 / 4 ∧ accuracy constantMass = 3 / 4 := by
  norm_num [accuracy, symmetricMass, constantMass]

theorem symmetric_upper_bound (policy : Bool → Bool) :
    expected symmetricMass utility policy ≤ -73 / 80 := by
  cases h0 : policy false <;> cases h1 : policy true <;>
    norm_num [expected, Fintype.sum_bool, symmetricMass, utility, h0, h1]

theorem constant_upper_bound (policy : Bool → Bool) :
    expected constantMass utility policy ≤ -11 / 10 := by
  cases h0 : policy false <;> cases h1 : policy true <;>
    norm_num [expected, Fintype.sum_bool, constantMass, utility, h0, h1]

theorem symmetric_best_value : informed symmetricMass utility = -73 / 80 := by
  apply le_antisymm
  · exact maximum_le _ _ symmetric_upper_bound
  · have h := le_maximum (expected symmetricMass utility) (fun s : Bool => s)
    norm_num [expected, Fintype.sum_bool, symmetricMass, utility] at h
    exact h

theorem constant_best_value : informed constantMass utility = -11 / 10 := by
  apply le_antisymm
  · exact maximum_le _ _ constant_upper_bound
  · have h := le_maximum (expected constantMass utility) (fun _ : Bool => false)
    norm_num [expected, Fintype.sum_bool, constantMass, utility] at h
    exact h

theorem blind_values :
    blind symmetricMass utility = -11 / 10 ∧ blind constantMass utility = -11 / 10 := by
  constructor
  · apply le_antisymm
    · apply maximum_le
      intro a
      cases a <;> norm_num [expected, Fintype.sum_bool, symmetricMass, utility]
    · have h := le_maximum (fun a => expected symmetricMass utility (fun _ => a)) false
      norm_num [expected, Fintype.sum_bool, symmetricMass, utility] at h
      exact h
  · apply le_antisymm
    · apply maximum_le
      intro a
      cases a <;> norm_num [expected, Fintype.sum_bool, constantMass, utility]
    · have h := le_maximum (fun a => expected constantMass utility (fun _ => a)) false
      norm_num [expected, Fintype.sum_bool, constantMass, utility] at h
      exact h

theorem unequal_gross_values :
    informed symmetricMass utility - blind symmetricMass utility = 3 / 16 ∧
      informed constantMass utility - blind constantMass utility = 0 := by
  rw [symmetric_best_value, constant_best_value, blind_values.1, blind_values.2]
  norm_num

end CPX.Diagnostics
