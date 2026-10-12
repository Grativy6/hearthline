import Mathlib.Data.Set.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-!
CPX v0.6, sections 3 and 9, claim CPX06-C4. Candidate source, PREPARED_NOT_RUN.
An explicitly nonempty account can settle one query without settling another.
Worlds are supplied; Lean does not certify that they exhaust real possibilities.
-/
namespace CPX.Resolution

def Settled {W A : Type*} (worlds : Set W) (query : W → A) : Prop :=
  worlds.Nonempty ∧ ∃ a, ∀ w ∈ worlds, query w = a

theorem empty_not_settled {W A : Type*} (query : W → A) :
    ¬ Settled (∅ : Set W) query := by
  simp [Settled]

theorem empty_agreement_is_vacuous :
    ∀ w ∈ (∅ : Set Bool), w = false := by
  simp

theorem one_query_settled_another_open :
    Settled (Set.univ : Set Bool) (fun _ => ()) ∧
      ¬ Settled (Set.univ : Set Bool) (fun w => w) := by
  constructor
  · exact ⟨⟨false, Set.mem_univ _⟩, (), fun _ _ => rfl⟩
  · rintro ⟨_, a, ha⟩
    have h : false = true := (ha false (Set.mem_univ _)).trans (ha true (Set.mem_univ _)).symm
    cases h

/-- True world uses Y=C; false world uses Y=U. This equation is kept during intervention. -/
def yEquation (world c u : Bool) : Bool := if world then c else u

def observe (world u : Bool) : Bool × Bool := (u, yEquation world u u)
def doZero (world u : Bool) : Bool × Bool := (false, yEquation world false u)

def fairJoint (f : Bool → Bool × Bool) (c y : Bool) : ℚ :=
  (if f false = (c, y) then 1 / 2 else 0) +
    (if f true = (c, y) then 1 / 2 else 0)

def interventionProbability (world : Bool) : ℚ :=
  (if (doZero world false).2 then 1 / 2 else 0) +
    (if (doZero world true).2 then 1 / 2 else 0)

def agreementProbability (world : Bool) : ℚ :=
  (if (observe world false).1 = (observe world false).2 then 1 / 2 else 0) +
    (if (observe world true).1 = (observe world true).2 then 1 / 2 else 0)

theorem same_observation (u : Bool) : observe true u = observe false u := by
  cases u <;> rfl

theorem observational_tables_agree (c y : Bool) :
    fairJoint (observe true) c y = fairJoint (observe false) c y := by
  rw [show observe true = observe false from funext same_observation]

theorem fair_observation_table (world c y : Bool) :
    fairJoint (observe world) c y = if c = y then 1 / 2 else 0 := by
  cases world <;> cases c <;> cases y <;>
    norm_num [fairJoint, observe, yEquation]

/-- Any finite passive sequence agrees pointwise under the same exogenous sequence. -/
theorem passive_sequences_agree (us : List Bool) :
    us.map (observe true) = us.map (observe false) := by
  rw [show observe true = observe false from funext same_observation]

theorem different_interventions :
    interventionProbability true = 0 ∧ interventionProbability false = 1 / 2 := by
  norm_num [interventionProbability, doZero, yEquation]

theorem observation_query_settled :
    Settled (Set.univ : Set Bool) agreementProbability := by
  refine ⟨⟨false, Set.mem_univ _⟩, 1, ?_⟩
  intro w _
  cases w <;> norm_num [agreementProbability, observe, yEquation]

theorem intervention_query_not_settled :
    ¬ Settled (Set.univ : Set Bool) interventionProbability := by
  rintro ⟨_, a, ha⟩
  have h := (ha true (Set.mem_univ _)).trans (ha false (Set.mem_univ _)).symm
  rw [different_interventions.1, different_interventions.2] at h
  norm_num at h

end CPX.Resolution
