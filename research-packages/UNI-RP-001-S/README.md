# UNI-RP-001-S — synthetic additive envelope

This package does not test any C2O clause.

UNI-RP-001-S is a corpus-agnostic demonstration package. It executes five
authored cases (SIM-001 through SIM-005) against a freshly written synthetic
bound, SYN-BND-001. The bound, the inputs, the generated table, and the
generation script were written for this package. They are not drawn from a
private corpus and they do not evaluate any C2O clause.

Release classification: INTERNAL_CANDIDATE. No owner record authorizes public
release. Labels alone do not authorize release.

## Bound in brief

While (u, v, z) stays inside a working box and the per-step drive stays at
most Delta, the comparison error at step n is at most n * Delta. The
comparison map is psi(u, v) = (3u + v) / 4.

## Cases

- SIM-001 (`still`): a smoke case whose error stays zero.
- SIM-002 (`steady_drive`): the envelope is attained, so the bound is sharp.
- SIM-003 (`expanding`): the working-box premise fails before the bound fails.
- SIM-004 (`steady_drive`, duration growth): the additive envelope has no
  finite uniform cap as the run gets longer.
- SIM-005: reproduces a 50-row table written by
  `sources/generate_synthetic_table.py`.

## Re-run

From this directory:

```
python3 simulations/run_all.py --output-dir /tmp/uni-rp-001-s-repro
python3 assurance/reexecute_all.py
```

The re-execution gate compares a fresh run with the committed `results/`
records. It is a same-code reproduction, not an independent review, and it
awards no programme credit.

Exact rational arithmetic is used throughout. There is no network use and no
random sampling.
