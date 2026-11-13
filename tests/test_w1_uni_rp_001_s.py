"""Checks for the UNI-RP-001-S synthetic package."""

import csv
import json
import unittest
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1] / "research-packages" / "UNI-RP-001-S"


class UniRp001STests(unittest.TestCase):
    def test_package_states_it_does_not_test_any_c2o_clause(self):
        readme = (PACKAGE / "README.md").read_text(encoding="utf-8")
        note = (PACKAGE / "assurance" / "DOES_NOT_TEST_C2O_CLAUSES.md").read_text(encoding="utf-8")
        bound = (PACKAGE / "sources" / "SYN-BND-001.md").read_text(encoding="utf-8")
        for text in (readme, note, bound):
            self.assertIn("does not test any C2O clause", text)

    def test_records_are_internal_candidate(self):
        sources = json.loads((PACKAGE / "sources" / "source_register.json").read_text())
        for source in sources:
            self.assertEqual(source["release_classification"], "INTERNAL_CANDIDATE")
            self.assertEqual(source.get("repository"), "Research-for-the-UNIVERSALIS-Ecosystem")
            self.assertNotIn("C2O", source.get("repository", ""))
        status = json.loads((PACKAGE / "metadata" / "programme_status.json").read_text())
        self.assertEqual(status["release_classification"], "INTERNAL_CANDIDATE")
        self.assertEqual(status["repository"], "Research-for-the-UNIVERSALIS-Ecosystem")
        self.assertFalse(status["release_authorized"])

    def test_generated_table_has_fifty_rows_and_a_script(self):
        self.assertTrue((PACKAGE / "sources" / "generate_synthetic_table.py").is_file())
        path = PACKAGE / "sources" / "generated" / "synthetic_envelope_table.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 50)
        self.assertEqual(
            list(rows[0]),
            [
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

    def test_five_executed_cases_exist(self):
        cases = json.loads((PACKAGE / "simulations" / "scenarios.json").read_text())
        self.assertEqual([item["id"] for item in cases], ["SIM-001", "SIM-002", "SIM-003", "SIM-004", "SIM-005"])
        for item in cases:
            self.assertTrue((PACKAGE / "results" / f"{item['id']}.json").is_file())


if __name__ == "__main__":
    unittest.main()
