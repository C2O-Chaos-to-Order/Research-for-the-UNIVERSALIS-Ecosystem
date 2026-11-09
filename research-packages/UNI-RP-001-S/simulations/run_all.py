"""Run every authored case in its own subprocess and keep the captured output.

Does not rewrite scenarios.json and does not award programme credit.

Wave 1 remediation N05: each case's record and trajectory go under
``--output-dir`` only. A directory that already holds a record, a trajectory
or an execution log is refused (exit 2) unless ``--replace-existing`` is given,
so a reproduction cannot silently overwrite earlier evidence.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run all simulation cases in separate processes.")
    parser.add_argument("--output-dir", default="reproduction_results")
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Explicitly allow overwriting existing records in --output-dir.",
    )
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    dest = Path(args.output_dir)
    if not dest.is_absolute():
        dest = Path.cwd() / dest
    cases = json.loads((root / "simulations" / "scenarios.json").read_text(encoding="utf-8"))
    if not args.replace_existing:
        existing = [dest / "execution_log.json"]
        for case in cases:
            existing += [dest / f"{case['id']}.json", dest / "trajectories" / f"{case['id']}_trajectory.json"]
        present = [str(p) for p in existing if p.exists()]
        if present:
            print(
                "OUTPUT_EXISTS: refusing to overwrite existing evidence in "
                f"{dest} ({len(present)} file(s)); choose a new --output-dir or pass "
                "--replace-existing explicitly",
                file=sys.stderr,
            )
            return 2
    dest.mkdir(parents=True, exist_ok=True)
    runner = root / "simulations" / "run_one.py"
    statuses = []
    for case in cases:
        output = dest / f"{case['id']}.json"
        command = [sys.executable, str(runner), "--case", case["id"], "--output", str(output)]
        if args.replace_existing:
            command.append("--replace-existing")
        proc = subprocess.run(command, capture_output=True, text=True)
        statuses.append(
            {
                "id": case["id"],
                "command": command,
                "exit_code": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            }
        )
    (dest / "execution_log.json").write_text(json.dumps(statuses, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "runs": len(statuses),
                "successful": sum(item["exit_code"] == 0 for item in statuses),
                "output_dir": str(dest),
            }
        )
    )
    return 0 if all(item["exit_code"] == 0 for item in statuses) else 1


if __name__ == "__main__":
    sys.exit(main())
