# N05 run_case spill fix — 2026-11-09

**Decision:** Kyle Steen (owner), card t49s657, answered 2026-11-09 20:13 CT
(America/Chicago): fix UNI-RP-001 `simulations/model.py` `run_case()` so
trajectories no longer spill beside results into the canonical tree; they go
to the isolated run output, consistent with N05.

**Verification level:** internal recheck only; **not independent verification**.

**Placement:** this change is on Research-UNI PR #7 (`fix/w1-n12-source-locator`),
the living tip of the N05 → K03 → N12 stack. N05 originated on PR #5. The
standing constraint forbids merging into base branches, so the spill fix was
not pushed onto #5 or #6. It will cascade when the stack merges in order
(#2 → #5 → #6 → #7).

This record is additive. The 2026-11-08 N05 runner isolation and the 2026-11-08
K03 re-execution gate remain in place.

## Prior behaviour

Until this change, `run_case()` called `_spill()`, which wrote
`results/trajectories/<case>_trajectory.json` using a hard-coded path resolved
from `model.py`'s location (the package tree). A direct call to `run_case`
therefore mutated the canonical tree even when the runner wrote its record
somewhere else.

The N05 runners (`run_one.py`, `run_all.py`, `reexecute_all.py`) already
avoided that path: `run_one.py` called `_dispatch()` directly and wrote the
trajectory beside `--output`, because changing `model.py` would change the
recorded `code_sha256` of every stored result. The public `run_case()` API
itself still spilled. That prior behaviour is preserved in this record and in
the `run_case` docstring; it is not silently rewritten away.

## Current behaviour

`run_case(case, trajectory_dir=None)` writes the trajectory only when the
caller supplies `trajectory_dir` (typically `<output-dir>/trajectories`). If
`trajectory_dir` is omitted, no trajectory file is written. The function
never writes into `results/trajectories`. `run_one.py` now calls
`run_case(..., trajectory_dir=...)`.

The comparison value still excludes the trajectory (see
`results/run_01_diagnosis.json`, defect D-01). That part of the design is
unchanged.

## Code hash change

`simulations/model.py` SHA-256:

| When | SHA-256 |
|---|---|
| Before this change (at merge tip after t49s657 relabel, `fba4c71`) | `d21c2613b01655726d0c7b6e6cd3efaba3b652a9bfd1ec1c9f90dd5f383ac453` |
| After this change | `72c94c8f3be6c86d24b7a1c7626437b68d532742663176cf8dee805a3561b220` |

## Simulation re-run

Every authored case (SIM-001 through SIM-005) was re-run into an isolated
directory via `simulations/run_all.py --output-dir` (not into the canonical
tree). Comparison against the recorded results, excluding nondeterministic
metadata (`execution_timestamp`, `started_at`, `ended_at`, `duration_seconds`,
`environment`, `raw_evidence_location`):

- `actual` values: identical for all five cases
- trajectories: byte-identical for SIM-001 through SIM-004 (SIM-005 has no trajectory)
- `code_sha256`: differs on all five records (old model hash → new model hash)

No other substantive recorded field changed.

## Recorded result and ledger hashes

The `code_sha256` field was then updated in the five canonical result files
and in the matching `code_sha256` column of `ledgers/simulation_ledger.csv`,
so the re-execution gate compares like-for-like against the model that is now
on disk. No `actual`, `expected`, trajectory, or other substantive field was
changed. These file-hash changes are recorded here rather than silently
relocked:

| File | SHA-256 before updating `code_sha256` | SHA-256 after |
|---|---|---|
| `results/SIM-001.json` | `f5ffd372b30436121f4c3b32d2dde472a5f776ae9c00af9eb7371613ff34ff30` | `9ef4219997ffe9de34ff46591ad723508fabae1382681957fd562d4f9480dc8b` |
| `results/SIM-002.json` | `2ff48296f2db4183b4226ee2488dd798366cced88f2e9b1fa7538b2ca79d9b35` | `085e460fda97c1186451c11a99d30b3523afa39c83e6aa71f0a1434c48f12079` |
| `results/SIM-003.json` | `0ad25914759ff26add9f3872f8a40ba9895755c8adb118f1c660d39e6655e6a1` | `1c6225fd0759fdde90a92e93b3a743955526096a8b3fe04af6e265f600c0c5b2` |
| `results/SIM-004.json` | `9057e2fef690e975ce529e6d6563220e926c1b11a21b4da0c234e28bd54f08de` | `4069cafa9de865238d839d1dbacd42442a341d61910d83245b94420832c3372b` |
| `results/SIM-005.json` | `fbd6eb55e8feefd2286a734b1d298932900844844b33cc3a24c4fba2d03368f3` | `42f018e96ca6270fbfe1bc706aaffb5cee706ce0cb28f599add22e9646ba59a6` |
| `ledgers/simulation_ledger.csv` | `448f13f4ea5839da3d350169ccd38f84823db8ddd0ca0faf63db9c291211718e` | `2e729c84c66877b7d3e8ea9b9ce2f6066317b07f18b5bf4dacab3cde11627d2d` |

Trajectory file hashes are unchanged:

| File | SHA-256 (unchanged) |
|---|---|
| `results/trajectories/SIM-001_trajectory.json` | `b296a423759e52fc0176734411c634b8871ab61049771cfcf510b522a8dad528` |
| `results/trajectories/SIM-002_trajectory.json` | `598b80658ea03107303a379d1da181d022ef2cb29e091afb9a702e15e1a9fb99` |
| `results/trajectories/SIM-003_trajectory.json` | `e5edb33859522f9b8c86c03f04c4c1e6f0b41c023ebe7c9a805753ca37aa3ab8` |
| `results/trajectories/SIM-004_trajectory.json` | `598b80658ea03107303a379d1da181d022ef2cb29e091afb9a702e15e1a9fb99` |

This record is classified INTERNAL_CANDIDATE. It does not authorize public release.
