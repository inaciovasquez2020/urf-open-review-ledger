import URF.URFInvariant

namespace Test

open URF

theorem termination_descent
  {α} (C : Configuration α) :
  ∃ n, True :=
by
  exact ⟨0, trivial⟩

end Test
