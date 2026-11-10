"""Owner decision t46s633: C2O-origin sources are INTERNAL_CANDIDATE.

The original PUBLICLY_CLEARED labels were an authoring default at 8c3b789 and
never an owner decision. This test fails if those labels silently return.
"""

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE = REPO_ROOT / "research-packages" / "UNI-RP-001"
SOURCE_IDS = (
    "SRC-EMERALD-TECH",
    "SRC-EMERALD-HUMAN",
    "SRC-EMERALD-COMPENDIUM",
    "SRC-EMERALD-EVIDENCE",
    "SRC-VENDORED-EVIDENCE",
)
CSV = "sources/vendored/01_EMERALD_TABLET_COMPUTATION.csv"
RECORD = "assurance/source_classification_relabel_2026-11-09.md"


class SourceClassificationRelabelTests(unittest.TestCase):
    def test_named_sources_are_internal_candidate(self):
        sources = json.loads((PACKAGE / "sources" / "source_register.json").read_text())
        by_id = {item["id"]: item for item in sources}
        for source_id in SOURCE_IDS:
            with self.subTest(source_id=source_id):
                self.assertIn(source_id, by_id)
                self.assertEqual(by_id[source_id]["release_classification"], "INTERNAL_CANDIDATE")

    def test_vendored_csv_file_is_internal_candidate(self):
        classes = json.loads((PACKAGE / "metadata" / "classifications.json").read_text())
        self.assertEqual(classes[CSV], "INTERNAL_CANDIDATE")

    def test_dated_record_preserves_the_authoring_default_and_owner_card(self):
        text = (PACKAGE / RECORD).read_text(encoding="utf-8")
        self.assertIn("t46s633", text)
        self.assertIn("8c3b789", text)
        self.assertIn("authoring default", text)
        self.assertIn("never an owner decision", text)
        self.assertIn("Kyle Steen", text)
        for source_id in SOURCE_IDS:
            self.assertIn(source_id, text)
        self.assertIn(CSV, text)
        self.assertIn("sources/source_register.json", text)

    def test_package_declares_its_own_repository(self):
        status = json.loads((PACKAGE / "metadata" / "programme_status.json").read_text())
        self.assertEqual(status.get("repository"), "Research-for-the-UNIVERSALIS-Ecosystem")

    def test_source_register_file_is_internal_candidate(self):
        classes = json.loads((PACKAGE / "metadata" / "classifications.json").read_text())
        self.assertEqual(classes["sources/source_register.json"], "INTERNAL_CANDIDATE")

    def test_dated_record_includes_source_register_file_addendum(self):
        text = (PACKAGE / RECORD).read_text(encoding="utf-8")
        self.assertIn("sources/source_register.json", text)
        self.assertIn("Addendum 2026-11-09", text)
        self.assertIn("private-repository citations", text)

    def test_programme_status_release_classification_is_internal_candidate(self):
        status = json.loads((PACKAGE / "metadata" / "programme_status.json").read_text())
        self.assertEqual(status["release_classification"], "INTERNAL_CANDIDATE")

    def test_dated_record_includes_programme_status_relabel_addendum(self):
        text = (PACKAGE / RECORD).read_text(encoding="utf-8")
        self.assertIn("t46s642", text)
        self.assertIn("Kyle Steen", text)
        self.assertIn("`metadata/programme_status.json` `release_classification`", text)
        self.assertIn("INTERNAL_CANDIDATE", text)

    def test_programme_status_file_is_internal_candidate(self):
        classes = json.loads((PACKAGE / "metadata" / "classifications.json").read_text())
        self.assertEqual(classes["metadata/programme_status.json"], "INTERNAL_CANDIDATE")

    def test_this_relabel_record_file_is_internal_candidate(self):
        classes = json.loads((PACKAGE / "metadata" / "classifications.json").read_text())
        self.assertEqual(classes[RECORD], "INTERNAL_CANDIDATE")

    def test_dated_record_includes_t49s657_file_class_addendum(self):
        text = (PACKAGE / RECORD).read_text(encoding="utf-8")
        self.assertIn("t49s657", text)
        self.assertIn("Kyle Steen", text)
        self.assertIn("file `metadata/programme_status.json`", text)
        self.assertIn("file `assurance/source_classification_relabel_2026-11-09.md`", text)
        self.assertIn("Addendum 2026-11-09 20:13 CT", text)


if __name__ == "__main__":
    unittest.main()
