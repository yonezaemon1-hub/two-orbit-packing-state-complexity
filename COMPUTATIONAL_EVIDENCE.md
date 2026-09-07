# Computational evidence backfill

Status: candidate for a future manuscript version; the current Zenodo PDF remains unchanged.

The paper is an exact theorem paper. The computational evidence therefore targets finite arithmetic, threshold behavior, and the remaining known-size gap rather than Monte Carlo simulation.

## Reproduction

Existing theorem sanity check:

```bash
python audit/audit_formula.py
```

Additional finite table:

```bash
python audit/computational_evidence.py
```

The new script emits representative values of

`S_D(D,P) = ceil(D/P) + 2`

and the known-size interval

`2 + ceil(floor(n/2)/P) <= S_n(n,P) <= 2 + ceil((n-1)/P)`.

It also checks the exact three-state threshold `P >= D` over a finite grid and reports the size of the remaining known-size interval.

## Role of the computation

The finite audit is independent bookkeeping evidence for boundary cases and off-by-one behavior. It is not used to prove the exact known-diameter theorem.
