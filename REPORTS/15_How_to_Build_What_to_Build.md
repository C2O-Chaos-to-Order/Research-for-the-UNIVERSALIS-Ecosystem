# Report 15 — How to Build What to Build

**Programme:** UNIVERSALIS Foundation Research  
**Subject:** UNI-ARCH-001  
**Edition:** 0.1.0  
**Status:** Proposed implementation roadmap; owner acceptance, independent review and authorization pending.

## 1. Governing implementation rule

The governing C2O Research Plan and Do No Harm rule apply. Build only against accepted requirements, in the public UNIVERSALIS product repository, using public-approved source material. Do not expose or import private C2O source, credentials, data, infrastructure, or authority.

Report 13's open research gaps govern what must be learned. Report 14's build/no-build scope governs what may be designed. This roadmap is not permission to implement, deploy, or publish.

## 2. Repository map and ownership

| Repository | Visibility / current state | Responsibility |
|---|---|---|
| `Research-for-the-C2O-Ecosystem` | Public; populated | Governing research Plan and paired Tablet source collections. |
| `Research-for-the-UNIVERSALIS-Ecosystem` | Public; initialized for research | UNIVERSALIS charter, research reports, requirements, source/evidence registers, test records, independent reviews and release evidence. |
| `The-UNIVERSALIS-Ecosystem` | Public; currently empty | Open-source product architecture, source code, tests, developer documentation, build workflows, packages and releases. |
| `The-C2O-Ecosystem` | Private; populated | C2O company/governance model, J.A.R.V.I.S. operational architecture, private infrastructure, internal systems, and controlled C2O–UNIVERSALIS coupling. |

Existing UNIVERSALIS domain repositories for ontology, human/intelligence powers, skills, capabilities and knowledge remain taxonomy/content repositories. They are not substitutes for the core product repository. Their current descriptions and metadata include legacy GAIA wording; perform a separate naming, ownership and scope audit before treating them as authoritative UNIVERSALIS registries.

No additional repository is required for this initial programme. Do not create duplicates or split the product into multiple repositories before dependency and ownership evidence justifies it.

## 3. Staged implementation roadmap

### Stage 0 — Research and boundary closure
- Complete the 28-pair clause-level Tablet audit and provenance reconciliation.
- Finalize the requirements traceability matrix and risk register.
- Reproduce the existing finite-model cases independently.
- Correct or disposition forecast input validation and approval-consumption test design.
- Decide local-only prototype stack, owner, data, and acceptance criteria.
- No production credentials, external integrations, user-data ingestion, or deployment.

**Exit:** approved bounded prototype charter, requirement set, threat model, and test plan.

### Stage 1 — Local, read-only domain core
- Implement typed records for sources, claims, evidence, identity context, permissions, temporal events and status.
- Use synthetic fixtures and a local test database.
- Validate input types, ranges, schema versions and identifiers.
- Define stable error and failure taxonomy.
- Keep source content and sensitive payloads separate from metadata.

**Exit:** deterministic unit and integration tests, reproducible fixtures, reviewed schema and documented limitations.

### Stage 2 — Authorization and trust boundaries
- Define authenticated principal and tenant context.
- Implement deny-by-default policy enforcement outside the model.
- Enforce access checks before content, titles, citations, counts or derived metadata enter context.
- Test cross-tenant access, forged identity, revocation, policy failure and race conditions.
- Keep public product credentials and stores unable to access private C2O systems.

**Exit:** reviewed threat model and evidence for the exact local authorization boundary. A production identity provider remains a separate gate.

### Stage 3 — Source registry and retrieval
- Implement exact source version and passage locators.
- Enforce purpose, scope, tenant, freshness, and permission filters before retrieval.
- Bound request size, latency, retries, cancellation and resource use.
- Return explicit states for no result, inaccessible source, stale source, invalid source, timeout and provider failure.
- Test injection, poisoning, citation manipulation, cache leakage and retrieval utility on held-out fixtures.

**Exit:** source-fidelity and adversarial test results meeting predeclared criteria.

### Stage 4 — Temporal memory and provenance
- Implement append-only correction history or another audited temporal model.
- Keep event time, record time, ingestion time and applicability time distinct.
- Preserve prior assertions and correction/retraction events.
- Implement governed retention and deletion; append-only history must not become a reason to retain personal data unlawfully or without authority.
- Test branching corrections, conflicts, retractions, partial intervals, schema migration, replay, crash recovery and deletion propagation.

**Exit:** independently reproduced temporal semantics and reviewed privacy/retention design.

### Stage 5 — Epistemic projection and human interface
- Implement explicit evidence states, uncertainty, abstention, conflict presentation and full-denominator coverage.
- Distinguish source statement, inference, hypothesis, and recommendation.
- Provide accessible explanations, correction and refusal paths.
- Evaluate trust calibration and comprehension with appropriately approved human research.

**Exit:** accessibility review and human evaluation; synthetic tests alone are insufficient.

### Stage 6 — Reliability, privacy and recovery
- Add durable persistence, backup/restore, monitoring and incident workflows.
- Test timeouts, retries, overload, cancellation, process restart, storage failure and recovery.
- Establish RTO/RPO and service objectives from measured requirements.
- Test retention, deletion, export and access review across derived data, caches and backups.

**Exit:** reliability and privacy lifecycle evidence, incident owner, and tested recovery procedure.

### Stage 7 — Optional supervised action capability
Do not begin until a separate authorization decision permits it.
- Select one low-impact, non-production action.
- Bind approval to the exact principal, target, parameters, purpose, environment, policy version and expiry.
- Use protected approval channels and persistent atomic reservation/consumption.
- Define revocation ordering, idempotency, uncertain provider outcomes and reconciliation.
- Keep the action disabled by default and preserve a human-controlled stop mechanism.

**Exit:** independent security review, tested failure/revocation cases, explicit owner acceptance and separate authorization for the exact action.

### Stage 8 — Release evaluation
- Review the exact source revision, dependencies, threat model, data flows, tests, accessibility and incident procedures.
- Verify license and source provenance.
- Scan for secrets and private C2O material.
- Reproduce critical results independently.
- Record release scope, known limitations, support/maintenance owner, rollback and revocation process.
- Publish only the exact approved artifact/version.

**Exit:** explicit release authorization. A completed roadmap or successful CI run is not release approval.

## 4. Engineering rules

- Prefer a modular monolith or library-first architecture until measured scale or isolation requirements justify service separation.
- Use maintained libraries and established identity/key-management systems; do not invent cryptography.
- Start with an audited relational persistence model. Adopt event sourcing selectively, not by default.
- Treat embeddings, indexes, caches, logs and telemetry as potentially sensitive derived data.
- Keep authorization, validation, tenant isolation, rate limits and action gates outside the language model.
- Use deterministic tests for invariants and probabilistic/empirical evaluations for model behaviour.
- Measure latency, cost, storage, compute, energy/resource use and human workload where relevant; never trade away safety, accessibility or evidence quality for a performance score.
- Maintain a software bill of materials, dependency review, vulnerability handling and reproducible build records.
- Every pull request must map changed files to requirements, tests, evidence, risk review and reviewer disposition.

## 5. Risk and incident controls

Apply the risk hierarchy: eliminate hazard, substitute safer alternative, isolate/contain, engineer safeguards, administrative controls, then warnings/protective measures. Warnings are not substitutes for stronger controls.

Every material risk record must identify hazard, pathway, affected parties, consequences, likelihood basis, uncertainty, controls, residual/transferred risk, owner, stop conditions, monitoring, incident response, recovery and review/expiry.

On suspected compromise or injection, contain and quarantine affected sources, revoke compromised access, invalidate dependent projections, preserve necessary evidence, and reassess before restoration. Do not let an agent authorize its own recovery.

## 6. Decision and evidence gates

Keep these distinct:
1. Research complete for a declared question.
2. Design accepted for a declared scope.
3. Implementation completed for an exact revision.
4. Tests executed and verified.
5. Independent review completed.
6. Real-world validation completed where required.
7. Owner acceptance recorded.
8. Release or deployment separately authorized.

A later defect or changed condition may revoke present eligibility without erasing the historical record of earlier acceptance.

## 7. Current disposition

This is a staged, evidence-led roadmap for review. No UNIVERSALIS product code, hosted infrastructure, external provider integration, real-user data processing, or deployment is authorized by this report.
