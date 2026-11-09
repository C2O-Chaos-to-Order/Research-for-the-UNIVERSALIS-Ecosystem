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


def _walk_dicts(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from _walk_dicts(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_dicts(item)


def _git_pinned(entry: dict) -> bool:
    return any(entry.get(field) not in (None, "") for field in ("commit", "blob_sha"))


class OldFormatRegressionTest(unittest.TestCase):
    """Fails if an old-format locator reappears in a valid fixture.

    Old format: a git-pinned source (commit or blob_sha present) without a
    repository field, or a this-repository source still using a package-relative
    path such as sources/vendored/...
    """

    def test_published_register_uses_d09_format(self):
        for src in sources():
            if not _git_pinned(src):
                continue
            with self.subTest(src=src["id"]):
                self.assertTrue(
                    src.get("repository"),
                    "old-format locator: git-pinned source without repository",
                )
                self.assertTrue(src.get("path"), "git-pinned source without path")
                self.assertTrue(src.get("commit"), "git-pinned source without commit")
                self.assertTrue(src.get("blob_sha"), "git-pinned source without blob_sha")
                if src.get("repository") == THIS_REPOSITORY:
                    self.assertTrue(
                        src["path"].startswith("research-packages/UNI-RP-001/"),
                        "this-repository path must be repository-relative, not package-relative",
                    )

    def test_checked_in_json_fixtures_have_no_old_format_locators(self):
        offenders = []
        roots = [PACKAGE, REPO_ROOT / "tests"]
        for root in roots:
            if not root.exists():
                continue
            for path in root.rglob("*.json"):
                if "__pycache__" in path.parts:
                    continue
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                    continue
                for obj in _walk_dicts(data):
                    if _git_pinned(obj) and not obj.get("repository"):
                        rel = path.relative_to(REPO_ROOT)
                        offenders.append(f"{rel} id={obj.get('id')}")
        self.assertEqual(offenders, [])

    def test_e2e_walkthrough_requires_the_d09_repository_field(self):
        text = (PACKAGE / "assurance" / "e2e_walkthrough.py").read_text(encoding="utf-8")
        self.assertIn(
            '("repository", "path", "blob_sha", "commit", "review_scope")',
            text,
        )




if __name__ == "__main__":
    unittest.main()
