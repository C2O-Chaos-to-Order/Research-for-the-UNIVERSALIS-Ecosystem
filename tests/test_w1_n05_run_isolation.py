"""Wave 1 remediation N05: a research run never overwrites canonical evidence.

Audit finding N05 (2026-11-07, High): running
``simulations/run_one.py --case SIM-003 --output <custom path>`` rewrote the
canonical ``results/trajectories/SIM-003_trajectory.json`` (model spill used a
hard-coded package path) and recorded ``raw_evidence_location`` as
``results/SIM-003.json`` regardless of where the record was written.

Every test here runs against a scratch copy of the package, never the
checked-in tree. Run from the repository root:

    python3 -m unittest discover -s tests -v
"""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1] / "research-packages" / "UNI-RP-001"


def _tree_hashes(root: Path) -> dict:
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


class W1N05RunIsolationTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="w1-n05-"))
        self.pkg = self.tmp / "UNI-RP-001"
        shutil.copytree(PACKAGE, self.pkg)
        self.canonical_before = _tree_hashes(self.pkg / "results")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run_one(self, case, output, *extra):
        return subprocess.run(
            [sys.executable, str(self.pkg / "simulations" / "run_one.py"),
             "--case", case, "--output", str(output), *extra],
            capture_output=True, text=True, cwd=str(self.tmp),
        )

    def test_custom_output_run_leaves_canonical_results_byte_identical(self):
        out = self.tmp / "scratch-run" / "SIM-003.json"
        self._run_one("SIM-003", out)
        self.assertTrue(out.is_file(), "the run must still write its own record")
        self.assertEqual(_tree_hashes(self.pkg / "results"), self.canonical_before)

    def test_failed_custom_run_with_different_trajectory_leaves_canonical_intact(self):
        # The audit reproduction: change SIM-003 in the scratch copy so the run
        # fails and produces a different trajectory, then write to a custom path.
        scenarios = self.pkg / "simulations" / "scenarios.json"
        cases = json.loads(scenarios.read_text())
        next(c for c in cases if c["id"] == "SIM-003")["input"]["steps"] = 1
        scenarios.write_text(json.dumps(cases))
        out = self.tmp / "failed-run" / "SIM-003.json"
        proc = self._run_one("SIM-003", out)
        self.assertEqual(proc.returncode, 1, "the altered case must fail its expectation")
        self.assertTrue(out.is_file(), "a failed run is still documented")
        self.assertEqual(_tree_hashes(self.pkg / "results"), self.canonical_before)

    def test_custom_output_trajectory_is_written_beside_the_record(self):
        out = self.tmp / "scratch-run" / "SIM-003.json"
        self._run_one("SIM-003", out)
        trajectory = out.parent / "trajectories" / "SIM-003_trajectory.json"
        self.assertTrue(trajectory.is_file())
        self.assertIsInstance(json.loads(trajectory.read_text()), list)

    def test_raw_evidence_location_names_where_this_run_wrote(self):
        out = self.tmp / "scratch-run" / "SIM-003.json"
        self._run_one("SIM-003", out)
        record = json.loads(out.read_text())
        self.assertNotEqual(record["raw_evidence_location"], "results/SIM-003.json")
        self.assertEqual(Path(record["raw_evidence_location"]).resolve(), out.resolve())
        inside = self.pkg / "reruns" / "SIM-002.json"
        self._run_one("SIM-002", inside)
        self.assertEqual(json.loads(inside.read_text())["raw_evidence_location"], "reruns/SIM-002.json")

    def test_existing_canonical_record_is_not_overwritten_by_default(self):
        canonical = self.pkg / "results" / "SIM-003.json"
        proc = self._run_one("SIM-003", canonical)
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertIn("OUTPUT_EXISTS", proc.stderr)
        self.assertEqual(_tree_hashes(self.pkg / "results"), self.canonical_before)

    def test_existing_trajectory_alone_blocks_the_run(self):
        out_dir = self.tmp / "scratch-run"
        (out_dir / "trajectories").mkdir(parents=True)
        sentinel = out_dir / "trajectories" / "SIM-003_trajectory.json"
        sentinel.write_text("prior evidence\n")
        proc = self._run_one("SIM-003", out_dir / "SIM-003.json")
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertEqual(sentinel.read_text(), "prior evidence\n")
        self.assertFalse((out_dir / "SIM-003.json").exists())

    def test_explicit_replace_existing_regenerates_in_place(self):
        canonical = self.pkg / "results" / "SIM-002.json"
        proc = self._run_one("SIM-002", canonical, "--replace-existing")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(canonical.read_text())["raw_evidence_location"], "results/SIM-002.json")

    def test_run_all_into_fresh_directory_does_not_touch_canonical(self):
        dest = self.tmp / "fresh-repro"
        subprocess.run(
            [sys.executable, str(self.pkg / "simulations" / "run_all.py"), "--output-dir", str(dest)],
            capture_output=True, text=True, cwd=str(self.tmp),
        )
        self.assertEqual(len(list(dest.glob("SIM-00*.json"))), 5)
        self.assertTrue((dest / "trajectories" / "SIM-003_trajectory.json").is_file())
        self.assertEqual(_tree_hashes(self.pkg / "results"), self.canonical_before)

    def test_run_all_refuses_a_populated_directory_without_replace(self):
        dest = self.pkg / "reproduction_results"
        before = _tree_hashes(dest)
        proc = subprocess.run(
            [sys.executable, str(self.pkg / "simulations" / "run_all.py"), "--output-dir", str(dest)],
            capture_output=True, text=True, cwd=str(self.tmp),
        )
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertEqual(_tree_hashes(dest), before)
        self.assertEqual(_tree_hashes(self.pkg / "results"), self.canonical_before)


if __name__ == "__main__":
    unittest.main()
