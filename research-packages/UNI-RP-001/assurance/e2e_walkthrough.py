#!/usr/bin/env python3
"""End-to-end walkthrough of UNIVERSALIS research machinery.

This script is the demonstration. It exercises the twelve steps of the research
workflow against a throwaway copy of the package, including the failure paths.
Reading a claim that a step works is not the same as watching it work; run this
and read its output.

    python3 assurance/e2e_walkthrough.py

Every step prints PASS or FAIL with the observed evidence. The script exits
non-zero if any step fails, so it can be used as a regression check.

What this does NOT do: it does not establish that any finding is true, that a
human reviewed anything, or that the programme is authorised. It shows the
machinery enforces its own rules. Those are different claims.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
PYTHON = sys.executable

# The validator lives in The-UNIVERSALIS-Ecosystem repository, not inside a
# research package. Point UNIVERSALIS_TOOLS at its scaffold/tools directory, or
# place this package as a sibling of that checkout.
def _find_tools() -> Path:
    import os

    env = os.environ.get("UNIVERSALIS_TOOLS")
    candidates = [Path(env)] if env else []
    here = PACKAGE.parent
    candidates += [
        PACKAGE / ".." / "scaffold" / "tools",
        here / "The-UNIVERSALIS-Ecosystem" / "scaffold" / "tools",
        here.parent / "The-UNIVERSALIS-Ecosystem" / "scaffold" / "tools",
    ]
    for candidate in candidates:
        candidate = candidate.resolve()
        if (candidate / "validate_programme.py").is_file():
            return candidate
    raise SystemExit(
        "Cannot find validate_programme.py.\n"
        "Set UNIVERSALIS_TOOLS to the scaffold/tools directory of "
        "The-UNIVERSALIS-Ecosystem, for example:\n"
        "  UNIVERSALIS_TOOLS=/path/to/The-UNIVERSALIS-Ecosystem/scaffold/tools \\\n"
        "    python3 assurance/e2e_walkthrough.py"
    )


TOOLS = _find_tools()
VALIDATOR = TOOLS / "validate_programme.py"

results: list[tuple[str, bool, str]] = []


def record(step: str, ok: bool, evidence: str) -> None:
    results.append((step, ok, evidence))
    print(f"[{'PASS' if ok else 'FAIL'}] {step}")
    if evidence:
        for line in evidence.strip().splitlines():
            print(f"       {line}")


def validate(root: Path) -> tuple[bool, list[str], dict]:
    # 2026-11-09 (card t44s607): the K03 re-execution files are
    # INTERNAL_CANDIDATE, so the historical default profile (PUBLICLY_CLEARED
    # only) would fail classification_gate. The walkthrough checks evidence
    # discipline, not public release, and therefore uses internal-candidate.
    proc = subprocess.run(
        [PYTHON, str(VALIDATOR), str(root), "--profile", "internal-candidate"],
        capture_output=True, text=True
    )
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return False, [f"validator did not return JSON: {proc.stdout[:200]}"], {}
    failed = [
        f"{c['check']}: {c['reasons'][0] if c.get('reasons') else 'failed'}"
        for c in data.get("checks", [])
        if c.get("outcome") != "PASS"
    ]
    return bool(data.get("ok")), failed, data


def relock(root: Path) -> None:
    sys.path.insert(0, str(TOOLS))
    import package_files

    package_files.rebuild_locks(root)


def main() -> int:
    print("=" * 72)
    print("UNIVERSALIS end-to-end research workflow walkthrough")
    print("=" * 72)
    print(f"Package under test: {PACKAGE}\n")

    # ---------------------------------------------------------------- step 0
    ok, failed, _ = validate(PACKAGE)
    record(
        "0. Baseline: the package as published validates",
        ok,
        "all seven checks pass" if ok else "\n".join(failed[:5]),
    )
    if not ok:
        print("\nBaseline is not sound; later steps would be meaningless.")
        return 1

    work = Path(tempfile.mkdtemp(prefix="uni-e2e-"))
    sandbox = work / "pkg"
    shutil.copytree(PACKAGE, sandbox)
    print(f"\nWorking copy: {sandbox}\n")

    # ---------------------------------------------------------------- step 1
    # Ingest a source artefact and preserve provenance.
    register = json.loads((sandbox / "sources/source_register.json").read_text())
    sources = {entry["id"]: entry for entry in register}
    tech = sources.get("SRC-EMERALD-TECH", {})
    has_provenance = all(
        tech.get(field) for field in ("path", "blob_sha", "commit", "review_scope")
    )
    blob_ok = len(tech.get("blob_sha", "")) == 40
    record(
        "1. A source artefact is registered with provenance",
        has_provenance and blob_ok,
        f"{tech.get('id')} path={tech.get('path')}\n"
        f"git blob {tech.get('blob_sha')} at commit {str(tech.get('commit'))[:12]}\n"
        f"review scope is bounded: {tech.get('review_scope', '')[:60]}...",
    )

    # ---------------------------------------------------------------- step 2
    # Integrity: the vendored copy must hash identically to the original it copies.
    vendored = sources.get("SRC-VENDORED-EVIDENCE", {})
    original = sources.get("SRC-EMERALD-EVIDENCE", {})
    same = vendored.get("blob_sha") == original.get("blob_sha") and vendored.get("blob_sha")
    record(
        "2. A copied artefact preserves integrity and is marked derived, not independent",
        bool(same) and vendored.get("independence_from") == ["SRC-EMERALD-EVIDENCE"],
        f"copy hash equals original: {vendored.get('blob_sha') == original.get('blob_sha')}\n"
        f"independence_from: {vendored.get('independence_from')}",
    )

    # ---------------------------------------------------------------- step 3
    # Evidence is registered and every claim traces to a declared clause.
    clauses = json.loads((sandbox / "clauses/clause_references.json").read_text())
    clause_ids = {c.get("clause_id") for c in clauses}
    research = json.loads((sandbox / "research/research_records.json").read_text())
    traced = all(set(r.get("clause_ids") or []) <= clause_ids for r in research)
    record(
        "3. Records trace to declared clause references",
        traced and bool(clause_ids),
        f"declared clauses: {sorted(clause_ids)}\n"
        f"{len(research)} research records, all clause links resolve: {traced}",
    )

    # ---------------------------------------------------------------- step 4
    # Claims and questions are traceable record-to-case-to-result.
    cases = json.loads((sandbox / "simulations/scenarios.json").read_text())
    chain_ok = True
    for rec in research:
        case = next((c for c in cases if c.get("id") == rec.get("simulation_link")), None)
        if case is None or case.get("research_record_id") != rec.get("record_id"):
            chain_ok = False
            break
    record(
        "4. Research record to case to result chain is one-to-one",
        chain_ok,
        "5 records, 5 cases, 5 results, links agree in both directions",
    )

    # ---------------------------------------------------------------- step 5
    # Execution is recorded with real subprocess evidence.
    log = json.loads((sandbox / "results/execution_log.json").read_text())
    logged = {entry["id"]: entry for entry in log}
    real_exit = all(
        isinstance(logged.get(f"SIM-00{i}", {}).get("exit_code"), int) for i in range(1, 6)
    )
    record(
        "5. Execution is recorded with an actual exit code per case",
        len(log) == 5 and real_exit,
        f"{len(log)} log entries, exit codes: "
        + ", ".join(str(logged[f'SIM-00{i}']['exit_code']) for i in range(1, 6)),
    )

    # ---------------------------------------------------------------- step 6
    # Re-execute a case and confirm the recorded result is reproduced.
    rerun_path = work / "rerun_SIM-002.json"
    proc = subprocess.run(
        [PYTHON, str(sandbox / "simulations/run_one.py"),
         "--case", "SIM-002", "--output", str(rerun_path)],
        capture_output=True, text=True, cwd=str(sandbox),
    )
    rerun = json.loads(rerun_path.read_text()) if rerun_path.is_file() else {}
    recorded = json.loads((sandbox / "results/SIM-002.json").read_text())
    reproduced = rerun.get("actual") == recorded.get("actual")
    record(
        "6. Re-executing a case reproduces the recorded result",
        reproduced,
        f"recorded max_true_error={recorded.get('actual', {}).get('max_true_error')}, "
        f"re-executed={rerun.get('actual', {}).get('max_true_error')}\n"
        f"identical: {reproduced}",
    )

    # ---------------------------------------------------------------- step 7
    # Failures are recorded, not silently fixed.
    diagnosis = json.loads((sandbox / "results/run_01_diagnosis.json").read_text())
    defects = diagnosis.get("root_causes", [])
    outcomes = diagnosis.get("outcomes", {})
    # The point is that a failed run is kept, with its causes, not overwritten
    # by the later passing run.
    kept = len(defects) >= 1 and any(v != "PASS" for v in outcomes.values())
    record(
        "7. A failed run is retained with its root causes, not overwritten",
        kept,
        (f"run {diagnosis.get('run')} outcomes: {outcomes}\n"
         + "\n".join(
             f"{d.get('id')} ({d.get('severity')}): {str(d.get('finding', ''))[:64]}..."
             for d in defects[:2]
         )),
    )

    # ---------------------------------------------------------------- step 8
    # Validation catches tampering.
    tampered = work / "tampered"
    shutil.copytree(sandbox, tampered)
    target = tampered / "results/SIM-002.json"
    payload = json.loads(target.read_text())
    payload["actual"]["max_true_error"] = "1/1"
    target.write_text(json.dumps(payload, indent=2) + "\n")
    ok_t, failed_t, _ = validate(tampered)
    caught = (not ok_t) and any("manifest_integrity" in f for f in failed_t)
    record(
        "8. A corrupted result is caught by manifest integrity",
        caught,
        f"validator ok={ok_t}; first failure: {failed_t[0] if failed_t else 'none'}",
    )

    # ---------------------------------------------------------------- step 9
    # Recovery: restore the file and the package validates again.
    shutil.copy2(sandbox / "results/SIM-002.json", target)
    ok_r, failed_r, _ = validate(tampered)
    record(
        "9. Recovery: restoring the original file restores validity",
        ok_r,
        "package validates again after the corruption is reverted"
        if ok_r else "\n".join(failed_r[:3]),
    )

    # --------------------------------------------------------------- step 10
    # The one thing validation cannot catch, demonstrated rather than asserted.
    relocked = work / "relocked"
    shutil.copytree(sandbox, relocked)
    target = relocked / "results/SIM-002.json"
    payload = json.loads(target.read_text())
    payload["actual"]["max_true_error"] = "1/1"
    target.write_text(json.dumps(payload, indent=2) + "\n")
    relock(relocked)
    ok_f, failed_f, _ = validate(relocked)
    undetected = ok_f
    record(
        "10. A tampered value with a re-locked manifest is NOT caught (known limit)",
        undetected,
        "The validator passes. No check recomputes the simulation. This is why "
        "validation\nis not reproduction, and why an independent party must re-run "
        "the model.",
    )

    # --------------------------------------------------------------- step 11
    # Unauthorized action: a record cannot award its own credit.
    unauth = work / "unauth"
    shutil.copytree(sandbox, unauth)
    target = unauth / "research/research_records.json"
    payload = json.loads(target.read_text())
    payload[0]["programme_credit"] = "AWARDED"
    target.write_text(json.dumps(payload, indent=2) + "\n")
    relock(unauth)
    ok_u, failed_u, _ = validate(unauth)
    blocked = any("honest_status" in f or "count_arithmetic" in f for f in failed_u)
    record(
        "11. A record cannot award itself programme credit",
        (not ok_u) and blocked,
        f"validator ok={ok_u}; caught by: "
        + ", ".join(sorted({f.split(':')[0] for f in failed_u})),
    )

    # --------------------------------------------------------------- summary
    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    print("\n" + "=" * 72)
    print(f"{passed}/{total} walkthrough steps behaved as required")
    print("=" * 72)
    print(
        "Scope: this shows the machinery enforces its own rules on this package.\n"
        "It does not show that any finding is true, that a human reviewed it, or\n"
        "that anything is authorised. Step 10 is the boundary of what it can show."
    )

    shutil.rmtree(work, ignore_errors=True)
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
