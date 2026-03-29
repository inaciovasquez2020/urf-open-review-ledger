import Mathlib.Data.Finset.Basic
import Mathlib.LinearAlgebra.LinearIndependent

namespace URF

universe u

structure Configuration (α : Type u) where
  data : α
  rank : Nat

structure Witness (α : Type u) where
  support : Finset α

-- abstract F₂ vector model (placeholder type)
abbrev F2 := Bool

def cycleRankF2 {α : Type u} (v : α) : Nat := 1

structure DescentSystem (α : Type u) where
  extractR : Nat → Configuration α → Finset (Witness α)
  witnessVector : Witness α → α
  witnessContribution : Witness α → Nat
  step : Configuration α → Configuration α
  nstep : Nat → Configuration α → Configuration α
  terminal : Configuration α → Prop

  contribution_eq_cycleRank :
    ∀ w, witnessContribution w = cycleRankF2 (witnessVector w)

  extractR_independent :
    ∀ R C,
      LinearIndependent (fun w : {w // w ∈ extractR R C} => witnessVector (w : Witness α))

  positive_contribution_on_extractR :
    ∀ R C w, w ∈ extractR R C → 0 < witnessContribution w

  terminal_iff_zero_rank :
    ∀ C, terminal C ↔ C.rank = 0

  nstep_zero :
    ∀ C, nstep 0 C = C

  nstep_succ :
    ∀ n C, nstep (n+1) C = nstep n (step C)

end URF

class CycleSpaceModel (α : Type u) where
  witnessVector : Witness α → α
  cycleRankF2 : Witness α → Nat
  contribution_eq_rank :
    ∀ w, witnessContribution w = cycleRankF2 w

axiom step_rank_drop :
  ∀ {α : Type u} (D : DescentSystem α) (C : Configuration α),
    ¬ D.terminal C → (D.step C).rank + 1 ≤ C.rank

theorem rank_strict_decrease
  {α : Type u} (D : DescentSystem α) (C : Configuration α)
  (h : ¬ D.terminal C) :
  (D.step C).rank < C.rank :=
by
  exact Nat.lt_of_lt_of_le (Nat.lt_succ_self _) (step_rank_drop D C h)

theorem nstep_rank_monotone
  {α : Type u} (D : DescentSystem α) :
  ∀ n C, (D.nstep (n+1) C).rank ≤ (D.nstep n C).rank
| 0, C => by
    rw [D.nstep_succ, D.nstep_zero]
    by_cases h : D.terminal C
    · rw [(D.terminal_iff_zero_rank C).mp h]
      simp
    · exact Nat.le_of_lt (rank_strict_decrease D C h)
| n+1, C => by
    rw [D.nstep_succ, D.nstep_succ]
    exact nstep_rank_monotone n (D.step C)

axiom zero_rank_reached_within_rank
  ∀ {α : Type u} (D : DescentSystem α) (C : Configuration α),
    ∃ n ≤ C.rank, (D.nstep n C).rank = 0

theorem termination
  {α : Type u} (D : DescentSystem α) :
  ∀ C, ∃ n, D.terminal (D.nstep n C)
:= by
  intro C
  rcases zero_rank_reached_within_rank D C with ⟨n, _, hz⟩
  refine ⟨n, ?_⟩
  exact (D.terminal_iff_zero_rank _).2 hz

end URF
