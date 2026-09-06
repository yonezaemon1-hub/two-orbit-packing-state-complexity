# Two-Orbit Packing for Exact State Complexity

Source and audit package for:

**Two-Orbit Packing for Exact State Complexity of Explicit Binary Consensus in Anonymous Dynamic Networks with Periodic Time**

Ryutaro Yonezu — Independent Researcher  
Version v1.0.0  
Manuscript date: September 5, 2026  
Public release: September 6, 2026  
Status: preprint / not peer reviewed

## Main result

For deterministic binary consensus with explicit termination in the stated anonymous synchronous dynamic-network model, with known dynamic-diameter bound `D`, unknown network size, one-bit broadcast-counting communication, and a free globally aligned phase `phi_t = t mod P`,

```text
S_D(D,P) = ceil(D/P) + 2.
```

Equivalently, an algorithm with at most `S >= 3` persistent states exists exactly when

```text
P(S - 2) >= D.
```

Hence the exact three-state threshold is

```text
S_D(D,P) = 3  iff  P >= D.
```

The paper also strengthens the known-size lower bound to

```text
S_n(n,P) >= 2 + ceil(floor(n/2)/P),
```

while the existing upper bound remains `2 + ceil((n-1)/P)`.

## Proof idea

The lower bound packs the two opposite homogeneous executions simultaneously in phase-augmented state space. If `tau_0` and `tau_1` are their first-final times on the static cycle `C_{2D}`, an adaptive split gives

```text
tau_0 + tau_1 >= D.
```

The two pre-final augmented trajectories are disjoint, while the two immutable final states each occupy a full cylinder of `P` phase values. Therefore

```text
P|Q| >= tau_0 + tau_1 + 2P >= D + 2P.
```

This matches the existing block-counter upper construction.

## Scope

The claims are deliberately narrow. The model assumes:

- deterministic anonymous nodes executing identical code;
- synchronous propagation rounds;
- simple undirected connected communication graph in every round;
- one-bit local broadcast, with a node observing only received zero/one counts;
- free globally aligned phase `t mod P`, but no full round number;
- explicit termination, agreement, and unanimity validity;
- finality and output encoded in persistent state;
- final nodes remain communication-present.

No novelty is claimed for generic finite-state pumping, periodic clocks, static-cycle locality, deterministic trajectory packing in general, or generic time-space tradeoffs.

## Files

- `paper.tex` — LaTeX source corresponding to the v1.0.0 manuscript content.
- `Yonezu_2026_Two_Orbit_Packing_Exact_State_Complexity.pdf` — authoritative final manuscript PDF.
- `audit/audit_formula.py` — finite arithmetic/off-by-one sanity checks for the theorem corollaries and split inequalities.
- `audit/audit_output.txt` — output of the included audit script.
- `PRIOR_ART_AUDIT.md` — scoped related-work/claim-boundary note.
- `CITATION.cff` — citation metadata with the published paper DOI.
- `.zenodo.json` — metadata for the software/source-package Zenodo release.
- `paper.publish.json` — paper-deposit metadata with published identifiers.
- `LICENSE` — MIT license for scripts/source-package utilities.
- `LICENSE_PAPER.txt` — CC BY 4.0 notice for the manuscript text/PDF.
- `SHA256SUMS.txt` — integrity manifest for the v1.0.0 release package.

## Reproduction

A standard LaTeX installation with `pdflatex` can compile `paper.tex`.

```bash
pdflatex paper.tex
pdflatex paper.tex
```

The included Python audit uses only the standard library:

```bash
python audit/audit_formula.py
```

The finite audit is not a proof. The mathematical proof is in the manuscript.

## Direct predecessor

Ryutaro Yonezu,  
*Internal Time as Local Memory: State–Phase Tradeoffs for Explicit Termination in Anonymous Dynamic Binary Consensus*, v2.0.0, 2026.  
Paper DOI: `10.5281/zenodo.22228873`

## DOI

Paper DOI: `10.5281/zenodo.22538052`  
All-versions paper DOI: `10.5281/zenodo.22538051`  
Software/source-package DOI: `10.5281/zenodo.22538011`
