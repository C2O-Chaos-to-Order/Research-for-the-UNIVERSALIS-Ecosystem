# Report 14 — What to Build

**Programme:** UNIVERSALIS Foundation Research  
**Subject:** UNI-ARCH-001  
**Edition:** 0.1.0  
**Status:** Proposed build/no-build recommendation; owner acceptance and independent review pending.

## 1. Build decision

The evidence supports designing a bounded, source-grounded continuity and research service as the first UNIVERSALIS capability. It does not yet support production deployment or an autonomous action system.

The first implementation target should be a **read-only, local-first, modular service** that can identify what is recorded, where it came from, how it changed, what remains unknown, and whether the current user is permitted to access it.

UNIVERSALIS is the public system and product identity. Existing GIDEON research and prototype names are retained as historical/working identifiers; they must not be used to create a separate privileged agent or to imply that an experimental prototype is production-ready.

## 2. Proposed architecture

### A. Identity and context boundary
Represent authenticated principals, subjects, tenants, purposes, roles, and policy context. Do not accept caller-constructed identity objects as authentication. Keep authorization outside the language model.

### B. Source and evidence registry
Track source identity, version, exact locator, author, recorder, evidence class, integrity reference, permitted audience, purpose, applicability, and status. Keep source authenticity, custody, provenance, and truth as separate claims.

### C. Retrieval gateway
Apply authentication, authorization, tenant and purpose filters before content enters model context. Enforce bounded query budgets, deadlines, cancellation, freshness, and explicit failure states. Return citations that resolve to exact source versions and passages.

### D. Temporal record service
Preserve event time, record time, ingestion time, applicability time, author, recorder, revisions, corrections, conflicts, and retractions. Use an audited relational design first; introduce event sourcing only where replay and audit benefits justify its complexity. Authorized deletion and retention obligations must remain possible.

### E. Epistemic projection
Represent supported, disputed, incomplete, missing, stale, invalidated, inaccessible, pending, and unknown states. Preserve full corpus denominators and dependencies. Support abstention and requests for further evidence instead of fabricated certainty.

### F. Read-only intelligence interface
Synthesize only from permitted evidence, cite supporting material, distinguish inference from source statements, disclose uncertainty, and report retrieval failure honestly. The model may propose an action; it cannot grant itself permission.

### G. Privacy, audit and recovery
Minimize retained personal data, separate sensitive payloads from operational metadata, enforce retention/deletion, protect audit access, and define incident containment, recovery, revocation and rollback. Logs must not become a second uncontrolled data warehouse.

### H. Human interaction and accessibility
Make uncertainty and permissions understandable; support correction, refusal, withdrawal, accessibility needs and user control. Human welfare cannot be inferred from synthetic predicate fixtures.

## 3. Initial build sequence

Build the read-only core first:
1. Typed domain and evidence records.
2. Local source registry with synthetic fixtures.
3. Explicit policy interface and deny-by-default access checks.
4. Temporal records and deterministic projections.
5. Unknown-aware evidence views and exact citations.
6. Read-only assistant adapter with retrieval-failure handling.
7. Audit, privacy lifecycle, recovery and regression tests.

A modular monolith or well-separated library/service boundary is preferred for the first prototype unless measured constraints justify distributed services. Avoid premature microservices and custom cryptography.

## 4. Build only after additional evidence and authorization

- Real identity-provider integration.
- Multi-tenant hosted service.
- External provider/model integration using real user data.
- Vector search and semantic retrieval at scale.
- Monitored external adapters and scheduled jobs.
- Voice, image, specialist or multi-agent roles.
- Supervised consequential actions through exact-action approvals and persistent atomic consumption.
- Public pilot or hosted release.

Each requires provider-specific security, privacy, accessibility, operational and human-impact evaluation.

## 5. Defer or do not build in this objective

- Self-authorizing agents or unrestricted execution.
- Private C2O passthrough, shared private credentials, or automatic source mirroring.
- Automatic memory-to-training pipelines.
- Claims of consciousness, sentience, biological life, mind-reading, universal truth, or future omniscience.
- Clinical diagnosis or physiological intervention.
- Unrestricted surveillance, unrestricted shell, or safety-critical physical actuation.
- A universal digital twin or universal proof engine.

## 6. Acceptance requirements

Each implemented component must have:
- A traceable requirement and source rationale.
- Declared scope, assumptions, threat model and data classification.
- Positive, negative, boundary, adversarial and regression tests as appropriate.
- Evidence for failure handling, privacy, authorization and recovery.
- Whole-system interaction tests.
- Independent review proportional to risk.
- Explicit owner acceptance for the exact version and scope.

A component PASS is not a system PASS. A system PASS is not release authorization.

## 7. Repository placement

- Research methodology and source Tablet collections: `Research-for-the-C2O-Ecosystem`.
- UNIVERSALIS-specific research, reports, evidence, test protocols and traceability: `Research-for-the-UNIVERSALIS-Ecosystem`.
- Public product architecture, code, tests, developer docs and releases: `The-UNIVERSALIS-Ecosystem`.
- Private C2O governance, J.A.R.V.I.S., private infrastructure and coupling controls: `The-C2O-Ecosystem`.

The public UNIVERSALIS product repository's current main branch contains its README, scaffold tooling, prototype code, and tests. Their presence does not establish that the proposed product capability is accepted, production-ready, or release-authorized. Further implementation and release scope must remain tied to accepted requirements and build-stage gates. The private C2O GIDEON prototype is a separate experimental reference and must not be copied wholesale into the public product.

## 8. Disposition

This report recommends what to build and what not to build in the initial scope. It does not establish implementation completion, production readiness, or authorization to deploy.
