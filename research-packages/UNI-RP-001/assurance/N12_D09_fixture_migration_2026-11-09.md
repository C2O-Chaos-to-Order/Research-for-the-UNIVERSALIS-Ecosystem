# N12 / D09 source-locator fixture migration — 2026-11-09

Owner decision: Kyle Steen, card t45s615, 2026-11-09 14:43 CT (America/Chicago).
Verification level: internal recheck only; not independent verification.

This record is additive. The 2026-11-08 N12 locator correction in
`sources/source_register.json` and the 2026-11-09 K03 relabel remain in place.

## What D09 format means

A git-pinned source declares four fields together:

- `repository` — the repository that `commit` belongs to
- `path` — a repository-relative path in that repository (no leading `/`, no `..`)
- `commit` — 40-character commit SHA
- `blob_sha` — 40-character git blob SHA

Old format: `commit` and/or `blob_sha` present without `repository`, or a
this-repository copy still using a package-relative path such as
`sources/vendored/...` paired with a commit from another repository.

Sources that are not git objects omit those fields. That is not the old format.

## Inventory before this follow-up

### Research-for-the-UNIVERSALIS-Ecosystem

Git-pinned JSON locators (5), all already in the new format after N12
(`8b0b3a5` / `source_register.json`):

| id | repository | path form | old-format? |
| --- | --- | --- | --- |
| SRC-EMERALD-TECH | Research-for-the-C2O-Ecosystem | repo-relative C2O path | no |
| SRC-EMERALD-HUMAN | Research-for-the-C2O-Ecosystem | repo-relative C2O path | no |
| SRC-EMERALD-COMPENDIUM | Research-for-the-C2O-Ecosystem | repo-relative C2O path | no |
| SRC-EMERALD-EVIDENCE | Research-for-the-C2O-Ecosystem | repo-relative C2O path | no |
| SRC-VENDORED-EVIDENCE | Research-for-the-UNIVERSALIS-Ecosystem | full repo path `research-packages/UNI-RP-001/sources/vendored/...` | no |

Occurrences that still described or checked the old field set (no `repository`):

| file | count / notes |
| --- | --- |
| `assurance/e2e_walkthrough.py` | 1 provenance check used `(path, blob_sha, commit, review_scope)` |
| `README.md` | 1 provenance paragraph mentioned commit and blob only |
| `assurance/e2e_run_log.txt` | historical 2026 walkthrough capture; step 1 printed path/commit/blob without repository. Kept as a prior record; not rewritten. |

Package-relative `sources/vendored/` strings in `README.md`, results, scenarios,
the manifest, and classifications name a file inside the package. They are not
source-locator objects and were not rewritten.

### The-UNIVERSALIS-Ecosystem (public, corpus-agnostic)

Git-pinned JSON locators in fixtures or examples: **0**.

`scaffold/templates/programme/sources/source_register.json` is `[]`.
`scaffold/tests/support.py` builders (`build_empty`, `build_executed`,
`build_duplicate_id`) and `test_source_provenance.py` `_source()` emit unpinned
sources (no commit/blob). Those are not old-format locators.

Occurrences of the old documented form (commit + blob_sha, no repository):

| file | count / notes |
| --- | --- |
| `scaffold/schemas/source_register_entry.schema.json` | `repository` property absent; path/commit/blob documented without it |
| `scaffold/SPECIFICATION.md` | 1 sentence: "When commit or blob_sha is present, each is a 40-character hexadecimal SHA." |
| `scaffold/README.md` | 1 workflow step: register with commit and blob_sha when the source is a git object |
| `scaffold/tools/validate_programme.py` | SHA-format check only; no repository/path pairing rule |

No public synthetic example in this repository cited a private C2O path.

## Inventory after this follow-up

Research-UNI published register: 5/5 still new-format (unchanged bytes).
Research-UNI walkthrough and README: migrated to the four-field D09 form (2 files).
Research-UNI historical `e2e_run_log.txt`: unchanged (prior record).

The-UNIVERSALIS-Ecosystem: schema, specification, README, SOURCE_PROVENANCE, and
validator now require or document the four-field form. New synthetic tests use
`example-public-repository` / `examples/synthetic_source.txt` and clearly fake
SHAs; they invent no real citations.

Negative fixtures:

- Existing unpinned negatives (`build_duplicate_id`, independence/siglum tests)
  stay invalid for their original reason. They were not git-pinned, so D09 does
  not change their failure mode.
- New D09 negatives fail on the rule they target (missing repository, missing
  path, missing blob_sha, non-relative path).
- The invalid-commit fixture uses the full D09 shape so it fails on the SHA
  rule rather than on a missing repository.

## D09 eligibility — documented, not weakened

The four C2O-origin entries above are `PUBLICLY_CLEARED` and name a private
source repository. D09 says: record the real repository/commit/path/blob for
private evidence; keep private lineage as declared, not rewritten; give public
or vendored material its own real public provenance; do not invent a vendor
commit.

A stronger eligibility rule of the form "a public package may not cite a
private repository at all" would now reject those four entries. That rule is
not added. N12 (2026-11-08) kept those locators as declared private lineage,
and card t45s615 asked only to migrate fixtures and examples to the locator
*format*. Replacing private-origin inputs with a synthetic public fixture
(the separate follow-up noted on PR #7) is still not done; it would change
the evidence itself and was not chosen on this card.

No public UNIVERSALIS synthetic fixture was found that D09 eligibility would
reject, and none citing private C2O content was added.

## Regression

`tests/test_w1_n12_source_locators.py` now fails if a git-pinned JSON object
without `repository` reappears under the package or tests, if a this-repository
source reverts to a package-relative path, or if the walkthrough drops
`repository` from its provenance check.
