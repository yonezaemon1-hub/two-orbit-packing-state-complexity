#!/usr/bin/env python3
"""Finite table audit for Two-Orbit Packing.

Computational evidence only; the proof is in the manuscript.
"""

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent


def cdiv(a: int, b: int) -> int:
    return (a + b - 1) // b


def s_d(D: int, P: int) -> int:
    return cdiv(D, P) + 2


def n_bounds(n: int, P: int) -> tuple[int, int]:
    return 2 + cdiv(n // 2, P), 2 + cdiv(n - 1, P)


def main() -> None:
    out = OUT / "two_orbit_finite_table.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["kind", "size", "P", "lower", "upper", "gap", "three_state"])
        for D in range(1, 61):
            for P in range(1, 61):
                s = s_d(D, P)
                assert (s == 3) == (P >= D)
                assert P * (s - 2) >= D
                if s > 3:
                    assert P * (s - 3) < D
                w.writerow(["known_D", D, P, s, s, 0, int(s == 3)])
        for n in range(4, 61):
            for P in range(1, 61):
                lo, hi = n_bounds(n, P)
                assert lo <= hi
                w.writerow(["known_n", n, P, lo, hi, hi - lo, ""])
    print("PASS_TWO_ORBIT_FINITE_AUDIT")
    print(out.name)


if __name__ == "__main__":
    main()
