"""Trajectory-error model for the Emerald Tablet correspondence contract.

Source clauses
    Technical: C2O Tablets, 01.E05 (single-step agreement does not establish
    trajectory).
    Human: Human Tablets, 01, clause X (Of the limit).

The claim under study is the closed form

    e_{n+1} <= eps + L*e_n        and therefore      e_n <= eps * sum(L^k, k=0..n-1)

which 01.E05 derives under two assumptions: the residual Delta stays uniformly
bounded by eps over the compared domain, and F_Y is L-Lipschitz there. Both
assumptions are about a *domain*. Neither clause states that the domain must be
closed under iteration, and that omission is what these cases test.

Everything here is computed from the case's own declared parameters. No
quantity is copied from the tablet; the known-answer case reads the tablet's
published evidence file independently and recomputes it.

This module is authored by the same party that will read its results. It is not
independent verification of anything.
"""

from fractions import Fraction

# Map families. Each entry is (F_X, F_Y, phi, residual, declared Lipschitz
# constant on the declared domain). All quantities are exact rationals so the
# comparison against a closed form is a test of the mathematics rather than of
# floating-point tolerance.
FAMILIES = {
    # Common translation: e stays at exactly zero for every step.
    "translation": {
        "F_X": lambda a, b: (a + 1, b + 1),
        "F_Y": lambda y: y + 1,
        "phi": lambda a, b: Fraction(a + b, 2),
        "residual": lambda a, b: Fraction(0),
        "L": Fraction(1),
    },
    # Componentwise squaring against a squared mean. This is the tablet's own
    # worked example, whose residual is exactly (a-b)^2/4.
    "squaring": {
        "F_X": lambda a, b: (a * a, b * b),
        "F_Y": lambda y: y * y,
        "phi": lambda a, b: Fraction(a + b, 2),
        "residual": lambda a, b: Fraction((a - b) ** 2, 4),
        "L": None,  # domain dependent; supplied per case
    },
    # A contracting map with a constant nonzero residual. The residual is
    # exactly 1/4 because F_Y is offset from phi-then-F_X by 1/4 everywhere.
    # This is the case where the bound of 01.E05 is attained exactly at every
    # step, so it tests whether the closed form is sharp and not merely valid.
    "offset_contraction": {
        "F_X": lambda a, b: (Fraction(a, 2), Fraction(b, 2)),
        "F_Y": lambda y: Fraction(y, 2) + Fraction(1, 4),
        "phi": lambda a, b: Fraction(a + b, 2),
        "residual": lambda a, b: Fraction(1, 4),
        "L": Fraction(1, 2),
    },
    # An explicitly contracting map. Used to show the bound is useful when
    # L < 1: the error is then uniformly bounded by eps/(1-L).
    "contraction": {
        "F_X": lambda a, b: (Fraction(a, 2) + 1, Fraction(b, 2) + 1),
        "F_Y": lambda y: Fraction(y, 2) + 1,
        "phi": lambda a, b: Fraction(a + b, 2),
        "residual": lambda a, b: Fraction(0),
        "L": Fraction(1, 2),
    },
}


def _closed_form(eps: Fraction, L: Fraction, n: int) -> Fraction:
    """eps * sum(L^k for k in 0..n-1). The claim of 01.E05."""
    return eps * sum((L ** k for k in range(n)), Fraction(0))


def _trajectory(family, a0, b0, steps, eps, L, domain):
    """Iterate both systems and record the true error and the claimed bound."""
    fam = FAMILIES[family]
    FX, FY, phi = fam["F_X"], fam["F_Y"], fam["phi"]
    x, y = (Fraction(a0), Fraction(b0)), None
    y = phi(*x)
    rows = []
    for n in range(steps + 1):
        true_error = abs(phi(*x) - y)
        bound = _closed_form(eps, L, n)
        residual_here = fam["residual"](*x)
        rows.append(
            {
                "n": n,
                "x": [str(x[0]), str(x[1])],
                "y": str(y),
                "phi_x": str(phi(*x)),
                "true_error": str(true_error),
                "claimed_bound": str(bound),
                "residual_here": str(residual_here),
                "inside_domain": all(domain[0] <= v <= domain[1] for v in x)
                and domain[0] <= y <= domain[1],
                "bound_satisfied": true_error <= bound,
                "residual_within_epsilon": residual_here <= eps,
                # The premise of 01.E05 is the residual bound AND a domain on
                # which F_Y is L-Lipschitz. Leaving the domain voids the second
                # half even where the residual still looks small, which is
                # exactly the trap this field exists to expose.
                "hypothesis_intact": (
                    residual_here <= eps
                    and all(domain[0] <= v <= domain[1] for v in x)
                    and domain[0] <= y <= domain[1]
                ),
            }
        )
        x = FX(*x)
        y = FY(y)
    return rows


def _dispatch(case):
    """Compute the full result, including the per-step trajectory.

    Returns only the quantities a case can pre-declare, because the runner
    compares with exact equality and an undeclared key would make every case
    fail for the wrong reason. The per-step trajectory is written to a side
    file by ``_spill`` below and is not part of the returned comparison value.

    Run 1 of this programme failed on exactly that point: the trajectory was in
    the returned dict and no case had declared it. See
    results/run_01_diagnosis.json, defect D-01.
    """
    kind = case["input"]["kind"]

    if kind == "bound_on_declared_domain":
        rows = _trajectory(
            case["input"]["family"],
            case["input"]["start"][0],
            case["input"]["start"][1],
            case["input"]["steps"],
            Fraction(case["input"]["epsilon"]),
            Fraction(case["input"]["L"]),
            tuple(case["input"]["domain"]),
        )
        worst_ratio = max(
            (Fraction(r["true_error"]) / Fraction(r["claimed_bound"])
             if Fraction(r["claimed_bound"]) else Fraction(0))
            for r in rows
        )
        return {
            "steps_within_domain": sum(1 for r in rows if r["inside_domain"]),
            "bound_satisfied_at_every_step": all(r["bound_satisfied"] for r in rows),
            "hypothesis_held_at_every_step": all(r["hypothesis_intact"] for r in rows),
            "max_true_error": str(max(Fraction(r["true_error"]) for r in rows)),
            "max_claimed_bound": str(max(Fraction(r["claimed_bound"]) for r in rows)),
            "worst_error_over_bound": str(worst_ratio),
            "final_true_error": str(Fraction(rows[-1]["true_error"])),
            "trajectory": rows,
        }

    if kind == "domain_escape":
        # Run past the point where the trajectory leaves the declared box.
        rows = _trajectory(
            case["input"]["family"],
            case["input"]["start"][0],
            case["input"]["start"][1],
            case["input"]["steps"],
            Fraction(case["input"]["epsilon"]),
            Fraction(case["input"]["L"]),
            tuple(case["input"]["domain"]),
        )
        first_out = next((r["n"] for r in rows if not r["inside_domain"]), None)
        first_violation = next(
            (r["n"] for r in rows if not r["bound_satisfied"]), None
        )
        first_hypothesis_break = next(
            (r["n"] for r in rows if not r["hypothesis_intact"]), None
        )
        return {
            "first_step_outside_domain": first_out,
            "first_step_bound_violated": first_violation,
            "first_step_hypothesis_broken": first_hypothesis_break,
            # The engineering point: did the bound fail, or did its premise fail
            # first? A bound that is only valid while the premise holds cannot be
            # relied on without a forward-invariance check.
            "hypothesis_broke_before_bound": (
                first_hypothesis_break is not None
                and (first_violation is None or first_hypothesis_break <= first_violation)
            ),
            "max_true_error": str(max(Fraction(r["true_error"]) for r in rows)),
            "trajectory": rows,
        }

    if kind == "uniform_budget":
        # For L < 1 the bound is uniform: eps/(1-L), independent of duration.
        eps = Fraction(case["input"]["epsilon"])
        L = Fraction(case["input"]["L"])
        rows = _trajectory(
            case["input"]["family"],
            case["input"]["start"][0],
            case["input"]["start"][1],
            case["input"]["steps"],
            eps,
            L,
            tuple(case["input"]["domain"]),
        )
        limit = eps / (1 - L) if L < 1 else None
        return {
            "geometric_limit": None if limit is None else str(limit),
            "every_step_below_limit": (
                None if limit is None
                else all(Fraction(r["true_error"]) <= limit for r in rows)
            ),
            "bound_grows_with_duration": (
                Fraction(rows[-1]["claimed_bound"]) > Fraction(rows[0]["claimed_bound"])
                if len(rows) > 1 else False
            ),
            "max_true_error": str(max(Fraction(r["true_error"]) for r in rows)),
            "final_claimed_bound": str(Fraction(rows[-1]["claimed_bound"])),
            "trajectory": rows,
        }

    if kind == "reproduce_published_table":
        # Known-answer control. Recompute the tablet's own published 50 rows
        # from its stated formulas and compare value for value.
        import csv
        from pathlib import Path

        # Resolve against the package root so the case runs from any working
        # directory. A path resolved against the current directory silently
        # makes the reproduction depend on where it was launched.
        package_root = Path(__file__).resolve().parents[1]
        source = Path(case["input"]["published_csv"])
        if not source.is_absolute():
            source = package_root / source
        grid = case["input"]["grid"]
        checked, mismatched, details = 0, 0, []
        with source.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                checked += 1
                a, b = int(row["a"]), int(row["b"])
                model_name = row["fixture_model"].strip().lower()
                if "translation" in model_name:
                    fam = FAMILIES["translation"]
                else:
                    fam = FAMILIES["squaring"]
                ttm = fam["phi"](*fam["F_X"](Fraction(a), Fraction(b)))
                mtt = fam["F_Y"](fam["phi"](Fraction(a), Fraction(b)))
                disc = abs(ttm - mtt)
                expected_value = "true" if disc == 0 else "false"
                problems = []
                if disc != Fraction(row["absolute_discrepancy"]):
                    problems.append(f"discrepancy {disc} != {row['absolute_discrepancy']}")
                if expected_value != row["passes"].strip().lower():
                    problems.append(f"passes {expected_value} != {row['passes']}")
                if problems:
                    mismatched += 1
                    details.append({"row": row["fixture_id"], "problems": problems})
        return {
            "rows_checked": checked,
            "rows_mismatched": mismatched,
            "mismatches": details,
            "expected_row_count": len(grid) * len(grid) * 2,
            "row_count_matches_expectation": checked == len(grid) * len(grid) * 2,
        }

    raise ValueError(f"unknown case kind: {kind!r}")


def run_case(case):
    """Return the declared summary only; spill the trajectory beside the result.

    The wrapper exists so the comparison value and the evidence artefact can
    differ. The comparison must equal exactly what the case declared. The
    evidence must keep everything, including per-step detail, because a summary
    without the steps cannot be re-checked.
    """
    full = _dispatch(case)
    trajectory = full.pop("trajectory", None)
    if trajectory is not None:
        _spill(case["id"], trajectory)
    return full


def _spill(case_id: str, trajectory: list) -> None:
    """Write the per-step trajectory next to the results, never silently dropping it."""
    import json
    from pathlib import Path as _Path

    destination = _Path(__file__).resolve().parents[1] / "results" / "trajectories"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / f"{case_id}_trajectory.json").write_text(
        json.dumps(trajectory, indent=2) + "\n", encoding="utf-8"
    )
