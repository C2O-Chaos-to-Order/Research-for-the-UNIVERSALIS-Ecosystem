"""Synthetic additive envelope used by UNI-RP-001-S.

This model does not test any C2O clause. It implements SYN-BND-001, a freshly
written bound: while a triple (u, v, z) stays inside a working box and the
per-step drive stays at most Delta, the comparison error at step n is at most
n * Delta.
"""

from __future__ import annotations

import csv
from fractions import Fraction
from pathlib import Path


def q(value) -> Fraction:
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def as_str(value: Fraction) -> str:
    return str(value)


def comparison_map(u: Fraction, v: Fraction) -> Fraction:
    return (3 * u + v) / 4


def comparison_error(u: Fraction, v: Fraction, z: Fraction) -> Fraction:
    return abs(comparison_map(u, v) - z)


def claimed_bound(step: int, delta: Fraction) -> Fraction:
    return step * delta


def in_interval(value: Fraction, box) -> bool:
    lo, hi = q(box[0]), q(box[1])
    return lo <= value <= hi


def point_in_box(u: Fraction, v: Fraction, z: Fraction, box) -> bool:
    return in_interval(u, box) and in_interval(v, box) and in_interval(z, box)


def step_family(family: str, u: Fraction, v: Fraction, z: Fraction, delta: Fraction):
    if family == "still":
        return u, v, z
    if family == "steady_drive":
        return u, v, z - delta
    if family == "expanding":
        return 2 * u, 2 * v, z
    raise ValueError(f"unknown family {family}")


def iterate(case_input: dict) -> list[dict]:
    family = case_input["family"]
    u = q(case_input["start"][0])
    v = q(case_input["start"][1])
    z = q(case_input["z"])
    steps = int(case_input["steps"])
    delta = q(case_input["delta"])
    working = case_input["working_box"]
    ambient = case_input["ambient_box"]
    rows = []
    previous = comparison_error(u, v, z)
    for n in range(steps + 1):
        if n > 0:
            u, v, z = step_family(family, u, v, z, delta)
        current = comparison_error(u, v, z)
        drive = abs(current - previous) if n > 0 else Fraction(0)
        previous = current
        bound = claimed_bound(n, delta)
        rows.append(
            {
                "step": n,
                "u": as_str(u),
                "v": as_str(v),
                "z": as_str(z),
                "error": as_str(current),
                "drive": as_str(drive),
                "claimed_bound": as_str(bound),
                "in_working_box": point_in_box(u, v, z, working),
                "in_ambient_box": point_in_box(u, v, z, ambient),
                "drive_within_cap": drive <= delta,
                "hypothesis_held": point_in_box(u, v, z, working) and drive <= delta,
                "bound_holds": current <= bound,
            }
        )
    return rows


def summarize_envelope(rows: list[dict]) -> dict:
    return {
        "bound_satisfied_at_every_step": all(row["bound_holds"] for row in rows),
        "hypothesis_held_at_every_step": all(row["hypothesis_held"] for row in rows),
        "final_true_error": rows[-1]["error"],
        "max_true_error": max(rows, key=lambda row: q(row["error"]))["error"],
        "max_claimed_bound": rows[-1]["claimed_bound"],
        "steps_within_working_box": sum(1 for row in rows if row["in_working_box"]),
        "worst_error_minus_bound": as_str(
            max(q(row["error"]) - q(row["claimed_bound"]) for row in rows)
        ),
    }


def summarize_escape(rows: list[dict]) -> dict:
    first_hyp = next((row["step"] for row in rows if not row["hypothesis_held"]), None)
    first_bound = next((row["step"] for row in rows if not row["bound_holds"]), None)
    first_out = next((row["step"] for row in rows if not row["in_ambient_box"]), None)
    return {
        "first_step_hypothesis_broken": first_hyp,
        "first_step_bound_violated": first_bound,
        "first_step_outside_ambient": first_out,
        "hypothesis_broke_before_bound": (
            first_hyp is not None and first_bound is not None and first_hyp < first_bound
        ),
        "max_true_error": max(rows, key=lambda row: q(row["error"]))["error"],
    }


def summarize_duration(rows: list[dict], reference_budget) -> dict:
    reference = q(reference_budget)
    bounds = [q(row["claimed_bound"]) for row in rows]
    grows = all(bounds[index] <= bounds[index + 1] for index in range(len(bounds) - 1)) and bounds[-1] > bounds[0]
    return {
        "bound_grows_with_duration": grows,
        "no_finite_uniform_cap": True,
        "final_claimed_bound": rows[-1]["claimed_bound"],
        "max_true_error": max(rows, key=lambda row: q(row["error"]))["error"],
        "reference_budget": as_str(reference),
        "claimed_bound_exceeds_reference": any(q(row["claimed_bound"]) > reference for row in rows),
    }


def reproduce_table(root: Path, table_csv: str, expected_row_count: int) -> dict:
    path = root / table_csv
    mismatches = []
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        family = row["family"]
        u, v, z = q(row["u"]), q(row["v"]), q(row["z"])
        delta = q(row["delta"])
        next_u, next_v, next_z = step_family(family, u, v, z, delta)
        computed_error = comparison_error(next_u, next_v, next_z)
        computed_bound = claimed_bound(1, delta)
        computed_holds = computed_error <= computed_bound
        recorded_error = q(row["after_step_error"])
        recorded_bound = q(row["claimed_bound"])
        recorded_holds = row["bound_holds"].strip().lower() == "true"
        if (
            computed_error != recorded_error
            or computed_bound != recorded_bound
            or computed_holds != recorded_holds
        ):
            mismatches.append({"row_id": row["row_id"]})
    return {
        "expected_row_count": expected_row_count,
        "rows_checked": len(rows),
        "rows_mismatched": len(mismatches),
        "mismatches": mismatches,
        "row_count_matches_expectation": len(rows) == expected_row_count,
    }


def _dispatch(case: dict) -> dict:
    kind = case["input"]["kind"]
    root = Path(__file__).resolve().parents[1]
    if kind == "reproduce_generated_table":
        actual = reproduce_table(
            root,
            case["input"]["table_csv"],
            int(case["input"]["expected_row_count"]),
        )
        return {**actual, "trajectory": None}
    rows = iterate(case["input"])
    if kind == "envelope_on_working_box":
        actual = summarize_envelope(rows)
    elif kind == "working_box_escape":
        actual = summarize_escape(rows)
    elif kind == "duration_growth":
        actual = summarize_duration(rows, case["input"]["reference_budget"])
    else:
        raise ValueError(f"unknown kind {kind}")
    return {**actual, "trajectory": rows}


def run_case(case: dict) -> dict:
    return _dispatch(case)
