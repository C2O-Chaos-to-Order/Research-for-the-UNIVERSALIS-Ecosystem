# Report 13 — Research Requirements and Gap Analysis

**Programme:** UNIVERSALIS Foundation Research  
**Subject:** UNI-ARCH-001  
**Edition:** 0.1.0  
**Status:** Proposed research disposition; independent review and owner acceptance pending.

## 1. Decision

Further research is required before claiming a secure, useful, real-world UNIVERSALIS continuity and knowledge service.

The existing GIDEON research package is useful candidate evidence. Its 107 research assessments and 107 recorded finite-model executions have internally consistent ledger, scenario, and execution-log mappings. This does not make the records independent studies, independent reproductions, empirical validation, or owner-accepted programme credits. The 107 scenarios span 11 model families.

The first build decision should remain a bounded, read-only, locally testable prototype. No public pilot or consequential action capability is justified by the current evidence alone.

## 2. Evidence already available

The current evidence base includes:
- A proposed 28-pair technical/Human Tablet collection (IDs 00–27).
- A governing C2O Research Plan with Do No Harm, risk elimination/reduction, universal subject research, verification, and source-boundary requirements.
- A GIDEON/UNIVERSALIS research package with 15 reports, 107 research records, 107 scenario configurations, and 107 execution-log records.
- Finite synthetic models for retrieval, approvals, temporal history, forecasting, replay, state projection, and integration.
- A bounded GIDEON continuity-core reference implementation in the private C2O ecosystem integration branch. It is experimental and must not be copied wholesale into the public product repository.
- Existing architecture documents describing C2O and UNIVERSALIS as distinct parent environments with a governed coupling boundary.

The package's original execution records are candidate evidence. They require independent reproduction, oracle review, and owner disposition before formal programme credit is awarded.

## 3. Newly identified technical assurance gaps

### G13-A — Forecast input-domain validation

The forecast definition requires probabilities in [0,1] and binary outcomes in {0,1}. The inspected implementation checks nonempty, equal-length arrays but does not enforce those mathematical domains. Invalid inputs can therefore produce a numeric score instead of a validation error.

**Closure:** enforce probability and outcome domains, numeric types, finite values, and nonempty/equal-length constraints; test endpoints, out-of-range values, booleans, strings, nulls, NaN, infinity, and malformed arrays. Independently reproduce the tests.

### G13-B — Approval-consumption test validity

The repeated-reservation scenario uses an explicit repeat flag. The model's local copied grant state does not establish durable consumption across independent requests. A second request can be evaluated against the original approved input without a persistent consumed-state authority.

**Closure:** use a genuinely stateful harness and test sequential reuse, concurrent reservations, revocation races, crashes during consumption, restart recovery, exact-action binding, and audit/policy failure. Do not claim atomicity from a single-process fixture.

### G13-C — Tablet lineage and clause-level audit

The current collection has 28 technical and 28 Human files, but a collection-level filename match is not a clause-level audit. Some later Human Tablet documents (notably IDs 22–27) retain legacy source-lineage filenames or explicitly unresolved transfer/registry metadata.

**Closure:** reconcile source lineage against actual technical files, indexes, commit history, and documented renames; preserve unresolved conflicts; audit all clauses and pair differences; do not silently normalize source history.

## 4. Material research gaps and closure criteria

| ID | Gap | Required evidence for closure |
|---|---|---|
| G01 | Retrieval utility | Consented/licensed representative corpus, query/relevance ground truth, citation-support evaluation, held-out results and predefined acceptance criteria. |
| G02 | Injection and exfiltration | Provider/version-specific adaptive tests across documents, tool outputs, citations, caches, and tenant boundaries; independent threat review. |
| G03 | Identity and approvals | Real authenticated principal, protected approval channel, exact-action binding, persistent atomic reservation/consumption, revocation ordering, crash/race tests. |
| G04 | Temporal correctness | Partial-period corrections, branching provenance, event/record/applicability time, conflicts, schema evolution, replay, retention and deletion propagation. |
| G05 | Privacy lifecycle | Provider/data-flow inventory, purpose, geography, training/retention settings, derived-data/cache deletion, backup handling, support access and legal review. |
| G06 | Human experience | Accessible interface review and ethically scoped evaluation of comprehension, trust calibration, refusal, withdrawal, correction and cognitive load. |
| G07 | Reliability | Real clocks, load, retries, cancellation, outages, durable queues/storage, recovery tests and declared RTO/RPO/service objectives. |
| G08 | Forecasting | Domain-specific temporal outcome data, baselines, held-out scoring, calibration and uncertainty analysis. |
| G09 | Source integrity | Exact source versions, authorship, edition, quotation, provenance, and historical/lapidary attribution review. |
| G10 | Programme assurance | Independent review of source interpretations, code, simulation oracles, pass classification, and owner acceptance. |
| G11 | Whole-system interactions | Cross-component threat and failure tests across retrieval, memory, uncertainty, authorization, privacy, recovery and human interface. |
| G12 | Repository and release boundary | Accepted repository ownership map, public/private classification, dependency/secret review, release process and coupling contract. |
| G13 | Tablet-derived requirements | Full 28-pair clause audit, traceable technical/Human requirements, applicability decisions and conflict disposition. |

A gap is not closed by writing a plan, adding a requirement, or recording an expected output. Closure requires the stated evidence and an appropriate review.

## 5. Whole-system research lenses

Use the 28-pair Tablet crosswalk as a source-informed research map, not a universal implementation checklist. For the first UNIVERSALIS scope, the most direct lenses are:
- T16/H16 — bounded transport and retrieval.
- T18/H18 — memory, provenance and temporal records.
- T21/H21 — legibility and explicit unknowns.
- T26/H26 — care, consent and non-coercion.

The integrated system must also account for T00 integration/scope, T07 initialization, T08 environment readiness, T09 persistence/resources, T10 measurement/performance, T13 access/disclosure, T17 information/uncertainty, T19 observation, T20 inference, T22 abstention, T23 governed transitions, T24 failure/recovery, T25 acceptance, and T27 stewardship. Other physical-science tablets apply only where the subject actually requires their domain models.

## 6. Research exclusions and safeguards

Do not include medical diagnosis, physiological control, mind-reading, consciousness proof, time travel, unrestricted surveillance, autonomous self-authorization, or aircraft/robotic actuation in this initial objective.

Apply Do No Harm and the risk-elimination hierarchy. Prefer hazard elimination and safer substitution before containment or administrative controls. Keep unknown risk distinct from zero risk. Pause if material harm cannot be responsibly assessed or controlled.

## 7. Disposition

**Research status:** substantial preliminary documentary and finite-model work exists; full research assurance remains open.

**Recommended next step:** complete the tablet clause/lineage audit, independently reproduce and correct the forecast and approval-model gaps, and close the read-only prototype's retrieval, security, privacy, temporal, human-experience, and reliability research obligations before considering a public pilot.

No production deployment, external action, public pilot, or owner acceptance is authorized by this report.
