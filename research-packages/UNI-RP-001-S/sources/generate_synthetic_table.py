#!/usr/bin/env python3
"""Write the 50-row synthetic envelope table used by UNI-RP-001-S SIM-005.

This script does not test any C2O clause. It emits a freshly designed table
for the synthetic additive envelope SYN-BND-001.
"""

from __future__ import annotations

import csv
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "simulations") not in sys.path:
    sys.path.insert(0, str(ROOT / "simulations"))
from model import (  # noqa: E402
    as_str,
    claimed_bound,
    comparison_error,
    comparison_map,
    q,
    step_family,
)


def main() -> int:
    destination = ROOT / "sources" / "generated" / "synthetic_envelope_table.csv"
    destination.parent.mkdir(parents=True, exist_ok=True)
    grid = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]
    families = (("still", Fraction(0)), ("steady_drive", Fraction(1, 5)))
    rows = []
    index = 1
    for family, delta in families:
        for u in grid:
            for v in grid:
                z = comparison_map(u, v)
                next_u, next_v, next_z = step_family(family, u, v, z, delta)
                after = comparison_error(next_u, next_v, next_z)
                bound = claimed_bound(1, delta)
                rows.append(
                    {
                        "row_id": f"R{index:03d}",
                        "family": family,
                        "u": as_str(u),
                        "v": as_str(v),
                        "z": as_str(z),
                        "delta": as_str(delta),
                        "after_step_error": as_str(after),
                        "claimed_bound": as_str(bound),
                        "bound_holds": "true" if after <= bound else "false",
                    }
                )
                index += 1
    if len(rows) != 50:
        raise SystemExit(f"expected 50 rows, wrote {len(rows)}")
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "row_id",
                "family",
                "u",
                "v",
                "z",
                "delta",
                "after_step_error",
                "claimed_bound",
                "bound_holds",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
