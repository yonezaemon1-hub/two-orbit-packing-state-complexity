#!/usr/bin/env python3
"""Finite arithmetic sanity checks for the Two-Orbit Packing paper.

These checks are not a proof. They exercise integer-ceiling identities,
boundary cases, and the arithmetic in the adaptive split constructions.
"""

from math import ceil

def cdiv(a: int, b: int) -> int:
    return (a + b - 1) // b

def run():
    exact_cases = 0
    feasibility_cases = 0
    split_d_cases = 0
    split_n_cases = 0
    known_n_bound_cases = 0

    # Exact formula corollaries and feasibility equivalence.
    for D in range(1, 501):
        for P in range(1, 501):
            S_star = cdiv(D, P) + 2
            assert S_star == ceil(D / P) + 2
            assert (S_star == 3) == (P >= D)
            exact_cases += 1

            # Check enough budgets to straddle the exact threshold.
            for S in range(3, min(D + 5, 40)):
                lhs = S_star <= S
                rhs = P * (S - 2) >= D
                assert lhs == rhs, (D, P, S, S_star)
                feasibility_cases += 1

    # Adaptive split on C_{2D}: if tau0+tau1 <= D-1,
    # L0=2*tau0+1 and L1=2D-L0 must satisfy L1>=2*tau1+1.
    for D in range(2, 301):
        for tau0 in range(D):
            for tau1 in range(D - tau0):
                if tau0 + tau1 <= D - 1:
                    L0 = 2 * tau0 + 1
                    L1 = 2 * D - L0
                    assert L0 >= 2 * tau0 + 1
                    assert L1 >= 2 * tau1 + 1
                    assert L0 + L1 == 2 * D
                    split_d_cases += 1

    # Known-size adaptive split.
    for n in range(4, 301):
        H = n // 2
        for tau0 in range(H + 1):
            for tau1 in range(H + 1):
                if tau0 + tau1 <= H - 1:
                    L0 = 2 * tau0 + 1
                    L1 = n - L0
                    assert L1 >= 2 * tau1 + 1
                    split_n_cases += 1

        for P in range(1, 301):
            lower = 2 + cdiv(n // 2, P)
            upper = 2 + cdiv(n - 1, P)
            assert lower <= upper
            known_n_bound_cases += 1

    print("VERDICT=PASS_ARITHMETIC_SANITY_CHECK_NOT_A_PROOF")
    print(f"EXACT_FORMULA_CASES={exact_cases}")
    print(f"FEASIBILITY_EQUIVALENCE_CASES={feasibility_cases}")
    print(f"KNOWN_D_SPLIT_CASES={split_d_cases}")
    print(f"KNOWN_N_SPLIT_CASES={split_n_cases}")
    print(f"KNOWN_N_BOUND_ORDER_CASES={known_n_bound_cases}")

if __name__ == "__main__":
    run()
