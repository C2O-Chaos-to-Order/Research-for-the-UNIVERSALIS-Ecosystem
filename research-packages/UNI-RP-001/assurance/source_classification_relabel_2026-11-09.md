# Source classification relabel — 2026-11-09

**Decision:** Kyle Steen (owner), card t46s633, answered 2026-11-09 15:22 CT
(America/Chicago): relabel the C2O-origin source-register entries in UNI-RP-001
and the vendored CSV file classification from PUBLICLY_CLEARED to
INTERNAL_CANDIDATE.

**Verification level:** internal recheck only; **not independent verification**.

This record is additive. The 2026-11-08 N12 locator correction and the
2026-11-09 K03 and N12/D09 records remain in place. Locators are not rewritten
here; only release classifications change.

## Origin of the previous labels

The original `PUBLICLY_CLEARED` labels on these five source-register entries,
and on `sources/vendored/01_EMERALD_TABLET_COMPUTATION.csv`, were an authoring
default applied at `8c3b789` (package creation, 2026-10-31,
"Add UNI-RP-001: executed research on Emerald tablet clause 01.E05"). That
labelling was never an owner decision. No owner release record authorized it.

This dated record states the change so the previous labels are not silently
rewritten away.

## New labels

| Item | Prior classification | Classification as of 2026-11-09 |
|---|---|---|
| source `SRC-EMERALD-TECH` | PUBLICLY_CLEARED (authoring default at `8c3b789`) | INTERNAL_CANDIDATE |
| source `SRC-EMERALD-HUMAN` | PUBLICLY_CLEARED (authoring default at `8c3b789`) | INTERNAL_CANDIDATE |
| source `SRC-EMERALD-COMPENDIUM` | PUBLICLY_CLEARED (authoring default at `8c3b789`) | INTERNAL_CANDIDATE |
| source `SRC-EMERALD-EVIDENCE` | PUBLICLY_CLEARED (authoring default at `8c3b789`) | INTERNAL_CANDIDATE |
| source `SRC-VENDORED-EVIDENCE` | PUBLICLY_CLEARED (authoring default at `8c3b789`) | INTERNAL_CANDIDATE |
| file `sources/vendored/01_EMERALD_TABLET_COMPUTATION.csv` | PUBLICLY_CLEARED (authoring default at `8c3b789`) | INTERNAL_CANDIDATE |
| `assurance/source_classification_relabel_2026-11-09.md` (this record) | (new) | PUBLICLY_CLEARED |

`metadata/programme_status.json` now also declares
`repository: Research-for-the-UNIVERSALIS-Ecosystem` so a public-release
validator can compare git-pinned source repositories against this package's
own public repository. That field is a package identity declaration, not a
clearance or a release authorization.

## Profile consequences

- `--profile internal-candidate` admits INTERNAL_CANDIDATE and should pass
  (never release-ready).
- `--profile public-release` rejects INTERNAL_CANDIDATE (`CLASSIFICATION_GATE`
  on the five source records and the vendored CSV, and on the earlier K03
  files) and, separately, reports `RELEASE_NOT_AUTHORIZED` because the
  package has no owner release-authorization record. Labels alone do not
  authorize release.
- With the companion The-UNIVERSALIS-Ecosystem public-release source-repository
  guard, `public-release` also refuses the four git-pinned sources whose
  `repository` is not this package's repository (`SRC-EMERALD-TECH`,
  `SRC-EMERALD-HUMAN`, `SRC-EMERALD-COMPENDIUM`, `SRC-EMERALD-EVIDENCE`).
  `SRC-VENDORED-EVIDENCE` is pinned to this package's repository and does not
  fail that check. No owner exception record names those four sources.
- With no `--profile` (historical PUBLICLY_CLEARED-only gate) the INTERNAL_CANDIDATE
  labels produce `CLASSIFICATION_GATE`.

This record does not authorize public release.

## Addendum 2026-11-09 (same card t46s633; gap closed after the first relabel)

The file `sources/source_register.json` was still classified PUBLICLY_CLEARED
after the source-record and vendored-CSV relabel, even though that file holds
the private-repository citations. That file classification is now
INTERNAL_CANDIDATE. Prior rows in the table above are unchanged.

| Item | Prior classification | Classification as of this addendum |
|---|---|---|
| file `sources/source_register.json` | PUBLICLY_CLEARED (authoring default at `8c3b789`; left unchanged in the first relabel) | INTERNAL_CANDIDATE |

`metadata/programme_status.json` `release_classification` remains PUBLICLY_CLEARED
(not changed; recorded here only). Labels alone do not authorize public release.

## Addendum 2026-11-09 15:49 CT (card t46s642)

**Decision:** Kyle Steen (owner), card t46s642, answered 2026-11-09 15:49 CT
(America/Chicago): change UNI-RP-001 `metadata/programme_status.json`
`release_classification` from PUBLICLY_CLEARED to INTERNAL_CANDIDATE.

This addendum is additive. Prior rows and the source-register file addendum
above are unchanged. Locators are not rewritten here.

| Item | Prior classification | Classification as of this addendum |
|---|---|---|
| `metadata/programme_status.json` `release_classification` | PUBLICLY_CLEARED (authoring default at `8c3b789`; left unchanged in the t46s633 source-record, vendored-CSV, and source-register file relabels) | INTERNAL_CANDIDATE |

The file classification of `metadata/programme_status.json` in
`metadata/classifications.json` remains PUBLICLY_CLEARED (not changed;
recorded here only). `release_authorized` remains false. Labels alone do
not authorize public release.

## Addendum 2026-11-09 20:13 CT (card t49s657)

**Decision:** Kyle Steen (owner), card t49s657, answered 2026-11-09 20:13 CT
(America/Chicago): relabel the file classification of
`metadata/programme_status.json` and of
`assurance/source_classification_relabel_2026-11-09.md` from PUBLICLY_CLEARED
to INTERNAL_CANDIDATE.

This addendum is additive. Prior rows and earlier addenda are unchanged and
remain the historical record, including the t46s642 note that the
`programme_status.json` file classification was still PUBLICLY_CLEARED at that
time. Locators are not rewritten here.

| Item | Prior classification | Classification as of this addendum |
|---|---|---|
| file `metadata/programme_status.json` | PUBLICLY_CLEARED (authoring default at `8c3b789`; left unchanged through the t46s633 and t46s642 relabels, which changed only `release_classification`) | INTERNAL_CANDIDATE |
| file `assurance/source_classification_relabel_2026-11-09.md` (this record) | PUBLICLY_CLEARED (label at creation, first table above) | INTERNAL_CANDIDATE |

The file now names private-repository citations and records an INTERNAL_CANDIDATE
package-level field, so keeping its own file classification PUBLICLY_CLEARED
was inconsistent with its content. `release_authorized` remains false. Labels
alone do not authorize public release.
