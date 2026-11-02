# UNIVERSALIS Public Research and Assurance Charter

**Document ID:** UNI-RES-ASSURE-001  
**Version:** 1.0.0  
**Status:** Proposed public research charter; owner review required  
**Date:** 2026-11-01

## 1. Purpose and authority

This charter organizes public research, requirements, evidence, simulation, testing, review and release recommendations for UNIVERSALIS. It applies the governing Unified C2O Research Plan without replacing or amending it.

The public research repository contains only material approved for public release. Private C2O governance, credentials, infrastructure, internal source, confidential data and unapproved research remain outside this repository.

## 2. Research questions

Public research should establish:
1. What user problems and public-interest needs should UNIVERSALIS address?
2. Which capabilities are feasible, necessary, proportionate and measurable?
3. What are the relevant privacy, security, accessibility, reliability and misuse risks?
4. Which local-first and optional remote architectures meet the requirements?
5. What evidence would falsify the proposed design or benefit claim?
6. Which components can be independently reproduced and reviewed?
7. What should be built, deferred, narrowed or rejected?

## 3. Evidence classes

Every claim must be labelled by evidence type:
- Primary source or normative requirement.
- Secondary research or expert analysis.
- Owner-provided project input.
- Formal specification.
- Synthetic fixture or illustrative example.
- Executed software test.
- Executed scenario-model simulation.
- Empirical/operational observation.
- Independent reproduction.
- Independent review or validation.

Do not promote a synthetic test into a scenario simulation, a scenario model into empirical evidence, or a proposal into an implemented capability.

## 4. Traceability chain

For each public capability or outcome claim, preserve:

**Source → research question → hypothesis → requirement → design → protocol → executed evidence → verification/review → disposition.**

Every material artifact should carry:
- Stable identifier and version.
- Owner/maintainer.
- Status and date.
- Source references and provenance.
- Assumptions, parameters and dependencies.
- Risk and data classification.
- Acceptance and falsification criteria.
- Test/review evidence.
- Known limitations and unresolved issues.

## 5. Research and simulation execution records

Each research execution must identify its scope, sources, search/retrieval method, inclusion/exclusion criteria, analysis method, assumptions, findings, contradictions, limitations and reviewer.

Each scenario-model simulation must separately identify protocol, model/code version, scenario boundary, inputs, parameters, constraints, initial conditions, seed/deterministic method, execution environment, outputs, failures, sensitivity, uncertainty, limitations and falsification outcome.

Each software test run must identify the code revision, dependencies, environment, command, fixtures, assertions, pass/fail results and logs.

A planned, described or hypothetical execution is NOT RUN. If a mandatory input is missing, record BLOCKED or INDETERMINATE.

## 6. Public release review

Before publishing any artifact:
1. Confirm public ownership and licensing.
2. Check for secrets, personal data, confidential material and private infrastructure details.
3. Review third-party dependencies, licences and attribution.
4. Review security implications and misuse pathways.
5. Check factual claims and citations.
6. Confirm the artifact contains no private C2O source or unapproved derivative.
7. Record the release decision and exact artifact version.

No private-to-public mirroring or synchronization is permitted.

## 7. Minimum assurance programme

- Functional correctness and schema validation.
- Negative, boundary and malformed-input tests.
- Prompt-injection and tool-misuse tests where model/tool integrations exist.
- Privacy and data-lifecycle tests.
- Authorization and cross-user isolation tests.
- Dependency and build integrity review.
- Failure, cancellation, recovery and rollback tests.
- Accessibility and usability review.
- Resource, cost and environmental impact measurement.
- Independent reproduction of selected material results.

## 8. Outcome evaluation

For each proposed transformative outcome, define a baseline, intended beneficiaries, affected stakeholders, metric definitions, measurement method, costs, harms, externalities, uncertainty, time horizon, counterfactual or comparison, falsification criteria and accountable reviewer.

Technical capability is not proof of social or ecological benefit. Report distributional impacts and unintended consequences; do not conceal them in an aggregate score.

## 9. Initial public work queue

| ID | Task | Required evidence | Status |
|---|---|---|---|
| UNI-R01 | Approve public research questions and scope | Owner decision and charter review | OPEN |
| UNI-R02 | Map public requirements to tests | Requirements traceability matrix | OPEN |
| UNI-R03 | Define public threat model | Threat model and mitigations | OPEN |
| UNI-R04 | Define evidence/run record schema | Schema and validator tests | OPEN |
| UNI-R05 | Define local-first reference environment | Reproducible environment and inventory | OPEN |
| UNI-R06 | Establish synthetic fixtures | Fixture provenance and validation | OPEN |
| UNI-R07 | Define outcome scorecard | Baseline and stakeholder methodology | OPEN |
| UNI-R08 | Establish independent review | Reviewer scope, findings and disposition | OPEN |

No item is marked complete by this charter's creation.

## 10. Status metadata

- **Change type:** Proposed public research and assurance charter.
- **Risk level:** Low to moderate at charter stage; research and implementation risks depend on data, integration and use.
- **Evidence:** Current public research repository README and public UNIVERSALIS repository README.
- **Assumptions:** This repository remains public; only public-approved research is committed.
- **Repositories affected:** Research-for-the-UNIVERSALIS-Ecosystem.
- **Status:** Proposed; owner review and research readiness decision pending.
