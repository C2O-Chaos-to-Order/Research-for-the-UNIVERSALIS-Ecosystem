"""Wave 1 remediation K03 / ASR-001: re-execution gate.

ASR-001 recorded one defect the programme validator cannot catch: a result value
overwritten in results/SIM-002.json and the manifest re-locked over the edit.
Every hash then agrees, so structural validation passes. The re-execution gate
(assurance/reexecute_all.py) re-runs EVERY simulation from the recorded case and
code into a scratch directory and compares substantive outputs with the
recorded results, so that tamper must now fail.

Run from the repository root:  python3 -m unittest discover -s tests -p "test_w1_k03*.py"
Optional: set UNIVERSALIS_TOOLS to The-UNIVERSALIS-Ecosystem/scaffold/tools to
also show that the structural validator still passes on the tampered copy.
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1] / "research-packages" / "UNI-RP-001"
GATE = Path("assurance") / "reexecute_all.py"
CASES = ["SIM-001", "SIM-002", "SIM-003", "SIM-004", "SIM-005"]


def relock(pkg: Path, rel: str) -> None:
    manifest_path = pkg / "metadata" / "sha256_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest[rel] = hashlib.sha256((pkg / rel).read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def tamper_sim002_value(pkg: Path) -> None:
    """ASR-001 defect: overwrite a recorded result value."""
    path = pkg / "results" / "SIM-002.json"
    record = json.loads(path.read_text(encoding="utf-8"))
    assert record["actual"]["max_true_error"] == "31/64"
    record["actual"]["max_true_error"] = "1/64"
    record["outcome_summary"] = record["outcome_summary"].replace('"max_true_error": "31/64"', '"max_true_error": "1/64"')
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    # Keep the ledger consistent too, as a careful tamperer would.
    ledger = pkg / "ledgers" / "simulation_ledger.csv"
    lines = ledger.read_text(encoding="utf-8").split("\n")
    for i, line in enumerate(lines):
        if line.startswith("SIM-002,"):
            lines[i] = line.replace('""max_true_error"": ""31/64""', '""max_true_error"": ""1/64""')
    ledger.write_text("\n".join(lines), encoding="utf-8")


class ReexecutionGateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="k03-"))
        self.pkg = self.tmp / "UNI-RP-001"
        shutil.copytree(PACKAGE, self.pkg, ignore=shutil.ignore_patterns("__pycache__"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def gate(self, *extra):
        proc = subprocess.run(
            [sys.executable, str(GATE), "--json", *extra],
            cwd=self.pkg, capture_output=True, text=True, timeout=300,
        )
        try:
            report = json.loads(proc.stdout)
        except json.JSONDecodeError:
            report = {"raw_stdout": proc.stdout, "stderr": proc.stderr}
        return proc.returncode, report

    def test_gate_exists_and_reproduces_every_simulation_on_untouched_package(self):
        self.assertTrue((self.pkg / GATE).is_file(), "re-execution gate missing")
        code, report = self.gate()
        self.assertEqual(code, 0, report)
        self.assertEqual(report["status"], "REPRODUCED")
        self.assertEqual(sorted(report["cases"]), CASES)
        self.assertTrue(all(c["status"] == "REPRODUCED" for c in report["cases"].values()))
        self.assertEqual(report["cases_rerun"], len(CASES))

    def test_asr_001_tamper_plus_relock_now_fails(self):
        tamper_sim002_value(self.pkg)
        relock(self.pkg, "results/SIM-002.json")
        relock(self.pkg, "ledgers/simulation_ledger.csv")
        # The hashes agree again: the manifest is internally consistent.
        manifest = json.loads((self.pkg / "metadata/sha256_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["results/SIM-002.json"],
                         hashlib.sha256((self.pkg / "results/SIM-002.json").read_bytes()).hexdigest())
        tools = os.environ.get("UNIVERSALIS_TOOLS")
        if tools:
            structural = subprocess.run(
                [sys.executable, str(Path(tools) / "validate_programme.py"), str(self.pkg)],
                capture_output=True, text=True, timeout=300)
            self.assertEqual(structural.returncode, 0,
                             "precondition: structural validation still passes on tamper+relock\n" + structural.stdout[-2000:])
        code, report = self.gate()
        self.assertNotEqual(code, 0, "tamper + re-lock must fail the re-execution gate")
        self.assertEqual(report["status"], "MISMATCH")
        self.assertEqual(report["cases"]["SIM-002"]["status"], "MISMATCH")
        self.assertIn("actual", report["cases"]["SIM-002"]["differing_fields"])
        for other in set(CASES) - {"SIM-002"}:
            self.assertEqual(report["cases"][other]["status"], "REPRODUCED")

    def test_tamper_of_the_last_case_is_also_caught(self):
        # every simulation is re-run, not a sample
        path = self.pkg / "results" / "SIM-005.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        record["expectation_matched"] = not record["expectation_matched"]
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        relock(self.pkg, "results/SIM-005.json")
        code, report = self.gate()
        self.assertNotEqual(code, 0)
        self.assertEqual(report["cases"]["SIM-005"]["status"], "MISMATCH")

    def test_tampered_trajectory_is_caught(self):
        path = self.pkg / "results" / "trajectories" / "SIM-003_trajectory.json"
        path.write_bytes(path.read_bytes().replace(b"1", b"7", 1))
        relock(self.pkg, "results/trajectories/SIM-003_trajectory.json")
        code, report = self.gate()
        self.assertNotEqual(code, 0)
        self.assertEqual(report["cases"]["SIM-003"]["status"], "MISMATCH")
        self.assertIn("trajectory", report["cases"]["SIM-003"]["differing_fields"])

    def test_missing_recorded_result_is_blocked_not_skipped(self):
        (self.pkg / "results" / "SIM-004.json").unlink()
        code, report = self.gate()
        self.assertNotEqual(code, 0)
        self.assertEqual(report["status"], "BLOCKED")
        self.assertEqual(report["cases"]["SIM-004"]["status"], "BLOCKED")

    def test_ledger_case_without_scenario_is_blocked(self):
        ledger = self.pkg / "ledgers" / "simulation_ledger.csv"
        lines = ledger.read_text(encoding="utf-8").splitlines()
        lines.append(lines[-1].replace("SIM-005", "SIM-006", 1))
        ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
        code, report = self.gate()
        self.assertNotEqual(code, 0)
        self.assertEqual(report["cases"]["SIM-006"]["status"], "BLOCKED")

    def test_model_code_changed_since_record_is_mismatch(self):
        model = self.pkg / "simulations" / "model.py"
        model.write_text(model.read_text(encoding="utf-8") + "\n# edited\n", encoding="utf-8")
        code, report = self.gate()
        self.assertNotEqual(code, 0)
        self.assertIn("code_sha256", report["cases"]["SIM-001"]["differing_fields"])

    def test_gate_never_writes_into_the_package(self):
        before = {p.relative_to(self.pkg): p.read_bytes() for p in self.pkg.rglob("*")
                  if p.is_file() and "__pycache__" not in p.parts}
        self.gate()
        after = {p.relative_to(self.pkg): p.read_bytes() for p in self.pkg.rglob("*")
                 if p.is_file() and "__pycache__" not in p.parts}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
