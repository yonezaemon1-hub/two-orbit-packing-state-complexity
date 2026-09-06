# Scoped Prior-Art Audit

Status: targeted literature screening through September 5, 2026.  
This note is not a certification of novelty.

## Direct predecessor

Ryutaro Yonezu, *Internal Time as Local Memory: State–Phase Tradeoffs for Explicit Termination in Anonymous Dynamic Binary Consensus*, v2.0.0, 2026. DOI: 10.5281/zenodo.22228873.

That work supplies the periodic external-phase model, the block-counter upper construction, and asymptotic state–phase bounds. The present paper changes the lower-bound accounting by coupling the two opposite homogeneous executions.

## Nearby work checked

- T. Blanc, G. A. Di Luna, and G. Viglietta, *Computing in Anonymous Dynamic Networks with One-Bit Communications*, arXiv:2607.08358 (2026). Same severe one-bit aggregate communication interface; different objective (general computation / round complexity).
- G. Parzych and J. J. Daymude, *Memory Lower Bounds and Impossibility Results for Anonymous Dynamic Broadcast*, Distributed Computing 39(3), Art. 18 (2026), DOI 10.1007/s00446-026-00511-4. Termination-memory lower bounds for anonymous dynamic broadcast; different task and start semantics.
- V. Turau, *Broadcasts in Anonymous, Dynamic Networks: A New Algorithm and Impossibility Results*, SAND 2026, DOI 10.4230/LIPIcs.SAND.2026.6. Randomized broadcast with stabilizing termination and asymptotic memory; different task/randomization/termination objective.
- G. A. Di Luna and G. Viglietta, *Universal Finite-State and Self-Stabilizing Computation in Anonymous Dynamic Networks*, Theoretical Computer Science 1085, Art. 116187 (2026), DOI 10.1016/j.tcs.2026.116187. Finite-state/self-stabilizing computation; different exact state-phase question.
- B. Charron-Bost and L. Penet de Monterno, *Self-Stabilizing Clock Synchronization in Dynamic Networks*, OPODIS 2022, DOI 10.4230/LIPIcs.OPODIS.2022.28.
- B. Charron-Bost and L. Penet de Monterno, *Clock Synchronization Is Almost Impossible with Bounded Memory*, arXiv:2411.10289 (2024).
- R. Bazzi, A. Chaturvedi, A. W. Richa, and P. Vargas, *Brief Announcement: Synchronization in Anonymous Networks Under Arbitrary Dynamics*, DISC 2025, DOI 10.4230/LIPIcs.DISC.2025.49.
- J. Aspnes, *Clocked Population Protocols*, JCSS 121 (2021), DOI 10.1016/j.jcss.2021.05.001.
- J. Mayo and P. Kearns, *Distributed Termination Detection with Roughly Synchronized Clocks*, IPL 52(2) (1994), DOI 10.1016/0020-0190(94)00129-4.

## Narrow claim boundary

The paper does not claim novelty for:

- finite-state pumping;
- disjoint deterministic trajectories as a generic idea;
- static-cycle locality;
- monotone flooding;
- dynamic-diameter definitions;
- periodic clocks;
- generic clock-memory or time-space tradeoffs.

The narrow residual claim is the task-specific two-orbit accounting that yields the exact known-diameter persistent-state formula in the stated anonymous dynamic-consensus model, together with the stated stronger known-size lower bound.
