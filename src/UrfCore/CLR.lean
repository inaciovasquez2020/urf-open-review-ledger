import UrfCore.Prelude

namespace UrfCore
namespace CLR

open Classical

structure Graph (V : Type) where
  adj : V → V → Prop
  degree_bound : ℕ

variable {V : Type} [Fintype V] [DecidableEq V]

noncomputable def neighbors (G : Graph V) (v : V) : Finset V :=
  Finset.univ.filter (fun w => G.adj v w)

noncomputable def radiusBall (G : Graph V) (_R : ℕ) (v : V) : Finset V :=
  insert v (neighbors G v)

end CLR
end UrfCore

