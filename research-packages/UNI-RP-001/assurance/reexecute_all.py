"""Re-execution gate for UNI-RP-001 (Wave 1 remediation K03; closes the ASR-001 gap).

Structural validation (validate_programme.py) checks that records, links and
locked hashes agree with each other. It cannot detect a recorded result value
that was overwritten and then re-locked in the manifest (ASR-001). This gate
re-runs EVERY simulation from the recorded case configuration and the current
model into a scratch directory outside the package, then compares the fresh
substantive output with the recorded result and trajectory.

Case set: the union of simulations/scenarios.json, ledgers/simulation_ledger.csv
(pass_type executed_simulation) and results/SIM-*.json. A case missing from any
of the three, or a run that cannot complete, is BLOCKED -- never skipped.

Compared: every record field except explicitly nondeterministic metadata
(timestamps, duration, interpreter/platform description, and the output path,
which necessarily differs). The recorded code_sha256 must equal the hash of the
model that is re-run.

Exit codes: 0 REPRODUCED (all cases); 1 MISMATCH; 2 BLOCKED.

Scope: this is a reproduction by the same code in the same environment. It is
not independent reproduction by a party that did not write the model, it does
not establish that the model is correct, and it awards no programme credit.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
RUN_ONE = PACKAGE / "simulations" / "run_one.py"
NONDETERMINISTIC_FIELDS = frozenset({
    "execution_timestamp",
    "started_at",
    "ended_at",
    "duration_seconds",
    "environment",
    "raw_evidence_location",
})


def _case_ids() -> tuple[set[str], set[str], set[str]]:
    scenarios_path = PACKAGE / "simulations" / "scenarios.json"
    scenarios = {c.get("id") for c in json.loads(scenarios_path.read_text(encoding="utf-8"))} if scenarios_path.is_file() else set()
    ledger_path = PACKAGE / "ledgers" / "simulation_ledger.csv"
    ledger: set[str] = set()
    if ledger_path.is_file():
        with ledger_path.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                if row.get("pass_type") == "executed_simulation":
                    ledger.add(row["record_id"])
    results = {p.stem for p in (PACKAGE / "results").glob("SIM-*.json")}
    return scenarios, ledger, results


def _compare(recorded: dict, fresh: dict) -> list[str]:
    keys = (set(recorded) | set(fresh)) - NONDETERMINISTIC_FIELDS
    return sorted(k for k in keys if recorded.get(k) != fresh.get(k))


def run_gate() -> dict:
    scenarios, ledger, results = _case_ids()
    every = sorted(scenarios | ledger | results)
    cases: dict[str, dict] = {}
    rerun = 0
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="uni-rp-001-reexec-") as scratch:
        scratch_dir = Path(scratch)
        for case_id in every:
            missing = [name for name, ids in (("scenarios.json", scenarios), ("simulation_ledger.csv", ledger),
                                             ("results/", results)) if case_id not in ids]
            if missing:
                cases[case_id] = {"status": "BLOCKED", "reason": "case absent from " + ", ".join(missing)}
                continue
            output = scratch_dir / f"{case_id}.json"
            proc = subprocess.run(
                [sys.executable, str(RUN_ONE), "--case", case_id, "--output", str(output)],
                cwd=scratch_dir, capture_output=True, text=True, env=env, timeout=600,
            )
            rerun += 1
            if not output.is_file():
                cases[case_id] = {"status": "BLOCKED", "reason": f"re-run wrote no record (exit {proc.returncode})",
                                  "stderr_tail": proc.stderr[-500:]}
                continue
            recorded = json.loads((PACKAGE / "results" / f"{case_id}.json").read_text(encoding="utf-8"))
            fresh = json.loads(output.read_text(encoding="utf-8"))
            differing = _compare(recorded, fresh)
            canonical_traj = PACKAGE / "results" / "trajectories" / f"{case_id}_trajectory.json"
            fresh_traj = scratch_dir / "trajectories" / f"{case_id}_trajectory.json"
            if canonical_traj.is_file() or fresh_traj.is_file():
                if not (canonical_traj.is_file() and fresh_traj.is_file()
                        and canonical_traj.read_bytes() == fresh_traj.read_bytes()):
                    differing.append("trajectory")
            cases[case_id] = {
                "status": "MISMATCH" if differing else "REPRODUCED",
                "differing_fields": differing,
                "run_exit_code": proc.returncode,
            }
    statuses = {c["status"] for c in cases.values()}
    if not cases or "BLOCKED" in statuses:
        status = "BLOCKED"
    elif "MISMATCH" in statuses:
        status = "MISMATCH"
    else:
        status = "REPRODUCED"
    return {
        "gate": "re-execution (K03 / ASR-001)",
        "status": status,
        "cases_expected": len(every),
        "cases_rerun": rerun,
        "cases": cases,
        "nondeterministic_fields_excluded": sorted(NONDETERMINISTIC_FIELDS),
        "scope": "same-code, same-environment reproduction; not independent reproduction; no programme credit",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="print the full JSON report")
    args = parser.parse_args(argv)
    report = run_gate()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for case_id, info in report["cases"].items():
            detail = info.get("reason") or ", ".join(info.get("differing_fields", [])) or "all substantive fields equal"
            print(f"[{info['status']}] {case_id}: {detail}")
        print(f"RE-EXECUTION GATE: {report['status']} ({report['cases_rerun']}/{report['cases_expected']} re-run)")
    return {"REPRODUCED": 0, "MISMATCH": 1}.get(report["status"], 2)


if __name__ == "__main__":
    sys.exit(main())
