# Report 001 — The Emerald trajectory-error bound: validity, sharpness, and a premise that fails silently

**Programme:** UNI-RP-001, edition 0.1.0
**Research record:** RES-001
**Source clauses:** Technical `01.E05`; Human clause X ("Of the limit")
**Status:** Evidence-backed first pass. **Not independently reviewed. Not independently reproduced. No programme credit awarded.**
**Author:** the same party that wrote the model and the expectations. See §8.

---

## 1. Question

Emerald technical clause 01.E05 argues that a single step agreeing does not establish the behaviour of a whole trajectory, and derives

```
e_{n+1} <= eps + L*e_n        hence        e_n <= eps * sum_{k=0..n-1} L^k
```

under two premises: the residual `Delta` is uniformly bounded by `eps` over a domain, and the coarse map `F_Y` is `L`-Lipschitz on that domain.

The paired Human clause X makes three demands in its own terms: a tolerance must be fixed before agreement is commended, the domain and the duration must be stated, and one step agreeing says nothing about the journey.

The question asked here: **does the bound hold, is it sharp, and does its premise survive iteration?**

## 2. Method

Five cases, exact rational arithmetic (no floating-point tolerance). `X` is the real plane, `Y` the real line, `phi` the arithmetic mean, `d_Y` the absolute difference — the tablet's own worked setting from its section 5. Expectations were derived by hand in `/workspace/work/derivation/derive.py` **before** the model was executed, and those derivations are quoted in the research record.

The declared domain is treated as a closed box. `hypothesis_intact` requires the residual bound **and** that the current point and its image both lie inside the box, because an `L` constant is only established on the domain it was established for.

## 3. Results

### 3.1 The bound is valid and can be sharp

| Case | Family | eps | L | True error at n=5 | Claimed bound at n=5 | Ratio |
|---|---|---:|---:|---:|---:|---:|
| SIM-001 | translation | 0 | 1 | 0 | 0 | — |
| SIM-002 | offset contraction | 1/4 | 1/2 | 31/64 | 31/64 | **1** |

In SIM-002 the bound is **attained exactly at every step**: 0, 1/4, 3/8, 7/16, 15/32, 31/64. It is not merely an upper bound there; it is the exact error. So 01.E05's closed form is correct and sharp, and no weaker bound would do for this family.

This confirms the algebra: the closed form was checked against the recurrence at every step for four `(eps, L)` pairs, including `L = 1` and `L > 1`.

### 3.2 The premise can fail before the bound does

SIM-003 (`F_X(a,b) = (a^2, b^2)`, `F_Y(y) = y^2`, start `(2,0)`, `eps = 1`, `L = 4`, domain `[-10,10]`):

| n | x₀ | true error | bound | inside domain | bound satisfied | residual ≤ eps |
|---:|---:|---:|---:|---|---|---|
| 0 | 2 | 0 | 0 | yes | yes | **yes** |
| 1 | 4 | 1 | 1 | **yes** | **yes** | **NO** |
| 2 | 16 | 7 | 5 | no | no | no |
| 3 | 256 | 127 | 21 | no | no | no |
| 6 | 2^64 | 2^63−1 | 1365 | no | no | no |

**At step 1 every visible quantity is still fine.** The error equals the bound exactly (1 = 1) and the point is still inside the declared domain. But the residual has already exceeded `eps`, so the premise that justifies the bound has already failed.

The bound first reports trouble at step 2. The premise failed at step 1. **A practitioner reading only `e_n <= bound` would see a satisfied bound at the exact moment the guarantee became vacuous.**

This is the substantive finding of this report, and it is not stated in 01.E05. The clause derives the bound correctly but does not require the domain to be closed under iteration, which is the condition that would make the premise durable.

### 3.3 Correction propagation

With the declared domain widened from `[-10,10]` to `[-1000,1000]` and everything else fixed:

| Quantity | Domain [-10,10] | Domain [-1000,1000] |
|---|---:|---:|
| first step outside domain | 2 | **4** |
| first step bound violated | 2 | **2** |
| first step premise broken | 1 | 1 |

Widening the domain delays the domain exit by two steps but leaves the premise failure at step 1 and the bound violation at step 2 untouched. So the two failures are **independent**, and the domain exit is not what causes the bound violation. A correction to one does not move the other, which is exactly the kind of dependency a research record must be able to show.

### 3.4 Known-answer control

SIM-005 recomputes the tablet's own published 50-row table from the formulas the tablet states. All 50 rows reproduced: discrepancies and pass/fail flags match value for value. Corrupting a single value in that table (NEG-004 and correction C2) was detected immediately, naming row TR-01.

This establishes that the tablet's published arithmetic is internally correct. It is **not** independent verification of the tablet, and it tests no scientific claim.

## 4. Adversarial controls

Four controls were authored to fail, and all four did:

| Control | Purpose | Required | Observed |
|---|---|---|---|
| NEG-001 | wrong declared value | FAIL | FAIL |
| NEG-002 | input changed, expectation stale | FAIL | FAIL |
| NEG-003 | unknown case kind | ERROR | ERROR |
| NEG-004 | one corrupted value in the published table | FAIL | FAIL |

Without these, five passes would only show that the harness runs.

## 5. What failed, and what was wrong

Run 1 recorded **four of five cases as FAIL**. Those failures are preserved unmodified in `results/run_01_original/` and diagnosed in `results/run_01_diagnosis.json`.

- **D-01 (Medium).** All four failed because the model returned a per-step `trajectory` that no case had pre-declared, and the runner compares with exact equality. Three cases were correct on every declared value. The runner was right; my case contract was wrong. Fixed by returning only declared quantities and writing trajectories to a side file.
- **D-02 (High).** My pre-declared expectation for SIM-003 was arithmetically wrong in four values (`4, 4, 4` and max error `36`; actual `2, 2, 1` and `2^63−1`). The model was right. The expectation was corrected after hand derivation, with the wrong values kept on record.

Both are recorded rather than quietly repaired, because an expectation that cannot fail proves nothing.

## 6. Limitations

1. Three map families were studied, chosen because their residuals are exactly computable. They do not characterise the space of maps a deployed system would meet.
2. Exact rational arithmetic eliminates floating-point error but says nothing about numerical behaviour of a real implementation.
3. The premise-failure finding is demonstrated on one family. Whether it generalises is untested here.
4. `L` was supplied as an input per case rather than estimated from a map. A real system must establish `L`, and that step is not modelled.
5. Nothing here says UNIVERSALIS should adopt this bound, and nothing here authorises implementing it.

## 7. Bearing on UNIVERSALIS

The result argues for a specific requirement, stated as a candidate only:

> A correspondence or approximation guarantee must declare a domain that is **closed under iteration**, and must be checked for forward invariance at each step. A bound that holds only where its premises hold, and whose premises are not re-checked as the state evolves, is not a guarantee over a trajectory.

This is a candidate requirement, not an accepted one. It is filed as a gap against 01.E05 rather than as an amendment to the clause, because the clause is a source document and this programme does not amend sources.

It is registered as **ULC-01-05** in `requirements/requirements.json`, traced to RES-003 and SIM-003, with `implementation: None` and `programme_credit: CANDIDATE_PENDING_OWNER_REVIEW`. The identifier follows the existing `ULC-<tablet>-<clause>` convention, so it is tablet 01, clause E05. Nothing in UNIVERSALIS implements it, and this report does not claim otherwise.

## 8. Independence

Every result in this report was produced, derived, read and written by the same party. The hand derivation and the model are two implementations written from one statement, which is a cross-check and **not** independent verification. No reviewer, human or automated, has examined the model, the expectations, or this report. Programme credit is `NONE` and authorisation is `NOT_AUTHORIZED`.

## 9. Reproduction

From the package root:

```
python simulations/run_all.py --output-dir reproduction_results
```

Each case runs in its own subprocess. Record fields include the model hash, the case-file hash and the exact environment. The five passing records are in `reproduction_results/`; run 1 is preserved in `results/run_01_original/`.
