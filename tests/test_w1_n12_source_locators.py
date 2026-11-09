"""Wave 1 remediation N12: every declared source locator must resolve.

Audit finding N12: SRC-VENDORED-EVIDENCE declared commit 9211d9b... together with
the package path sources/vendored/...; that commit belongs to the C2O source
repository, while the vendored path exists only in this repository, so the
commit:path pair resolved nowhere (git exit 128).

D09 recommendation applied: the public package keeps the private lineage as
declared (not rewritten) and gives the vendored public copy its own real public
provenance in this repository. No vendor commit is invented.

Run from the repository root:  python3 -m unittest discover -s tests -p "test_w1_n12*.py"
Set C2O_SOURCE_REPO to a checkout of Research-for-the-C2O-Ecosystem to also
resolve the four C2O-origin locators.
"""

import hashlib
import json
import os
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE = REPO_ROOT / "research-packages" / "UNI-RP-001"
THIS_REPOSITORY = "Research-for-the-UNIVERSALIS-Ecosystem"


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def resolve(repo: Path, commit: str, path: str) -> str | None:
    proc = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", f"{commit}:{path}"],
                          capture_output=True, text=True)
    return proc.stdout.strip() if proc.returncode == 0 else None


def sources() -> list[dict]:
    return json.loads((PACKAGE / "sources" / "source_register.json").read_text(encoding="utf-8"))


class SourceLocatorTest(unittest.TestCase):
    def setUp(self):
        if not (REPO_ROOT / ".git").exists():
            self.skipTest("not a git checkout")

    def test_every_git_pinned_source_declares_its_repository(self):
        for src in sources():
            if src.get("commit"):
                with self.subTest(src=src["id"]):
                    self.assertIn(src.get("repository"), {THIS_REPOSITORY, "Research-for-the-C2O-Ecosystem"})

    def test_sources_in_this_repository_resolve_to_the_declared_blob(self):
        local = [s for s in sources() if s.get("repository") == THIS_REPOSITORY]
        self.assertTrue(local, "the vendored copy must be pinned in this repository")
        for src in local:
            with self.subTest(src=src["id"]):
                self.assertEqual(resolve(REPO_ROOT, src["commit"], src["path"]), src["blob_sha"])
                self.assertTrue(src["path"].startswith("research-packages/UNI-RP-001/"))
                package_rel = src["path"].removeprefix("research-packages/UNI-RP-001/")
                self.assertEqual(git_blob(PACKAGE / package_rel), src["blob_sha"])

    def test_vendored_copy_is_byte_identical_to_its_declared_original(self):
        by_id = {s["id"]: s for s in sources()}
        vendored, original = by_id["SRC-VENDORED-EVIDENCE"], by_id["SRC-EMERALD-EVIDENCE"]
        self.assertEqual(vendored["blob_sha"], original["blob_sha"])
        self.assertNotEqual(vendored["commit"], "9211d9b546174064255e628e4fdaafb7a3fd422c")

    def test_c2o_origin_sources_resolve_when_that_checkout_is_available(self):
        c2o = os.environ.get("C2O_SOURCE_REPO")
        if not c2o:
            self.skipTest("C2O_SOURCE_REPO not set; C2O-origin locators not resolved in this run")
        for src in sources():
            if src.get("repository") == "Research-for-the-C2O-Ecosystem":
                with self.subTest(src=src["id"]):
                    self.assertEqual(resolve(Path(c2o), src["commit"], src["path"]), src["blob_sha"])

    def test_resolver_rejects_wrong_commit_path_or_blob(self):
        vendored = next(s for s in sources() if s["id"] == "SRC-VENDORED-EVIDENCE")
        if vendored.get("repository") != THIS_REPOSITORY:
            self.fail("vendored copy is not pinned in this repository")
        self.assertIsNone(resolve(REPO_ROOT, "9211d9b546174064255e628e4fdaafb7a3fd422c", vendored["path"]))
        self.assertIsNone(resolve(REPO_ROOT, vendored["commit"], vendored["path"] + ".missing"))
        self.assertNotEqual(resolve(REPO_ROOT, vendored["commit"], "research-packages/UNI-RP-001/README.md"),
                            vendored["blob_sha"])


if __name__ == "__main__":
    unittest.main()
