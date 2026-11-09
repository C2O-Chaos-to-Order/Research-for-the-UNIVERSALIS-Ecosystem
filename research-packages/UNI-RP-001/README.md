# UNI-RP-001 — Emerald 01.E05 research package

Edition 0.1.0. Programme unit `UNI-RP-001`, checkpoint `CP-04`.

This package contains an executed research unit on one clause of tablet 01, not an empty
template. Every number below is counted from the files in this package.

## What is in here

| Item | Count | Where |
|---|---|---|
| Research records | 5 | `research/research_records.json`, `research/RES-00N.md` |
| Simulation cases | 5 | `simulations/scenarios.json` |
| Executed results | 5 | `results/SIM-00N.json` |
| Candidate requirements | 1 | `requirements/requirements.json` |
| Reports | 1 | `reports/` |
| Sources registered | 5 | `sources/source_register.json` |

## What was actually executed

All five cases ran in separate subprocesses with exact rational arithmetic (`fractions.Fraction`,
so no floating-point tolerance is involved). Exit codes and result hashes are recorded in
`results/execution_log.json`.

- **SIM-001** — zero residual: the error stays at zero, so the bound holds trivially. This is a
  harness control, not a test of the clause.
- **SIM-002** — contracting map with a constant residual: the true error equals the claimed bound
  at every step (0, 1/4, 3/8, 7/16, 15/32, 31/64). The closed form in 01.E05 is **sharp**, not
  merely valid.
- **SIM-003** — non-contracting map: at step 1 the error equals the bound and the point is inside
  the domain, but the residual has already exceeded the premise. The bound first reports trouble
  at step 2. **A bound can be vacuous before it is violated.**
- **SIM-004** — for L &lt; 1 the geometric limit eps/(1-L) = 1/2 bounds the error at every step
  while the summed form keeps growing.
- **SIM-005** — the tablet's own 50-row published computation reproduced row for row, from the
  vendored copy in `sources/vendored/`.

A first run (`results/run_01_original/`) failed four of five cases. It is preserved unmodified,
with its root causes in `results/run_01_diagnosis.json`. Both defects were mine, not the model's,
and both are still on record.

## What remains incomplete

- **CP-04 requires 9 research and 9 simulation passes.** This package has 5 and
  5. The checkpoint is `IN_PROGRESS`, not met. See
  `ledgers/checkpoint_schedule.csv`.
- One clause of one tablet is examined. 27 other Tablets and the vast majority of clauses are
  untouched.
- Nothing here advances beyond the **BASE** stage of the progression.

## What has not been independently verified

No reviewer has examined the model, the expectations, or the report. Independent reviews: 0.
Independent reproductions: 0. Programme credit is `NONE` and owner acceptance is `PENDING`.
Everything in this package was produced by one party, so nothing in it is independently verified.

`assurance/e2e_walkthrough.py` re-runs the twelve-step workflow demonstration (including the
failure and recovery paths) and `assurance/ASR-001_validator_coverage.json` records what the
validator catches and the one defect class it cannot.

## The limit that matters most

`assurance/ASR-001_validator_coverage.json` records this, and step 10 of the walkthrough
demonstrates it: the programme validator **does not re-execute simulations**. A recorded value
altered and then covered by a re-locked manifest passes every check. Validation shows the package
is internally consistent and honestly labelled. It does not show any number is true. Only
re-running the model from its recorded configuration, by a party that did not write it, can show
that.

## Reproducing this work

```
python3 simulations/run_all.py --output-dir /tmp/uni-rp-001-reproduction
python3 assurance/e2e_walkthrough.py
```

Runs never overwrite existing evidence (Wave 1 remediation N05). Each record and its
trajectory are written only under the chosen output location, and a location that already
holds a record, trajectory or execution log is refused with exit 2 unless
`--replace-existing` is passed explicitly. The checked-in `reproduction_results/` directory is
therefore not reused by default; choose a new directory. `simulations/model.py` itself is
unchanged, so the recorded `code_sha256` values still apply; calling `model.run_case()` directly
(outside the runner) still writes to `results/trajectories/`.

The cases resolve their inputs against the package root, so they behave the same from any working
directory.

## Provenance

Tablet clause 01.E05 and its paired Human clause X are registered in
`sources/source_register.json` with git blob hashes and the commit they were read at. The tablet's
published computation is vendored at `sources/vendored/` and hashes identically to the original.
The tablet is treated as a **proposed specification to be tested**, never as established
mathematics.
