# Research for the UNIVERSALIS Ecosystem

**Purpose:** Public, evidence-led research for UNIVERSALIS as an open-source architecture and product family.

**Guiding principle:** *With Power, Comes Responsibility.*

## Authority and relationship

The [Unified C2O Research Plan](https://github.com/C2O-Chaos-to-Order/Research-for-the-C2O-Ecosystem/blob/main/The%20C2O%20Research%20Plan/README.md) is the governing research methodology. This repository applies that methodology to UNIVERSALIS; it does not replace or silently amend the governing Plan.

The paired technical and Human Tablet collections are maintained in the C2O research repository. They are proposed contemporary research artifacts and interpretive inputs, not independent scientific authority, implementation proof, or permission to act.

## Repository responsibility

This repository holds UNIVERSALIS-specific research charters, evidence registers, gap analyses, requirements, reports, test protocols, executed research/simulation records, review outcomes, and build/no-build recommendations.

The actual open-source UNIVERSALIS product source, architecture implementation, tests, developer documentation, and releases belong in [The UNIVERSALIS Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem).

C2O's private company, governance, infrastructure, credentials, internal data, and private source remain in the private C2O environment. No private C2O material is copied here without explicit classification and release approval.

## Historical status snapshot (2026-11-10)

`main` was an initialization plus the Golden-Compass working papers. It is not yet the home of the research packages described below.

`main` is at `0be97ca73b3eb758803d47355e6071b69d6126b0` (2026-11-02 2:19:25 PM CT, America/Chicago). A `git ls-tree -r --name-only` of that HEAD listed **9** files: this `README.md` and eight paths under `Golden-Compass/`.

Research packages live in eight open draft pull requests, not on `main`:

| PR | Title (as of 2026-11-10) | Base |
|---|---|---|
| #1 | Establish UNIVERSALIS research charter and build reports 13–15 | `main` |
| #2 | UNI-RP-001: executed research on Emerald tablet clause 01.E05 | `main` |
| #3 | Propose reciprocal stewardship governance charter | `main` |
| #4 | Add research-package, provenance, and reproduction CI checks | `main` |
| #5 | Wave 1 / N05: research runs write only to their own output and never overwrite evidence (stacked on #2) | #2 head |
| #6 | feat(K03): re-execution gate re-runs every simulation; closes ASR-001 tamper+relock [Wave 1, draft] | #5 head |
| #7 | fix(N12): pin vendored source to a resolvable locator [Wave 1, draft] | #6 head |
| #8 | UNI-RP-001-S: synthetic additive envelope package [Wave 1, draft] | `main` |

The stack #2 ← #5 ← #6 ← #7 is four deep. None of those drafts is merged by this note. This `main` has no `.github/` workflow tree; in-tree CI is proposed on pull request #4.

Initialization, and the presence of Golden-Compass papers, do not mean the research programme, requirements, architecture, implementation, validation, or release is complete or authorized.

## Current status (2026-11-11)

`main` is at `65d1ccf31b50ececb9c8ba3008093346ddaf60bc`. The following changes are now merged:

- PR #1 — UNIVERSALIS research charter, repository/source boundary, requirements register, and Reports 13–15. These remain proposed research/governance artifacts; owner acceptance and independent review are still pending.
- PR #3 — Reciprocal Stewardship Charter. It remains a proposal and does not establish legal independence, accepted governing policy, or implementation authorization.
- PR #4 — research-package, provenance, and reproduction CI checks.

**Open:** PR #8 — UNI-RP-001-S. Its mathematical claim and implementation have been corrected to include the initial-error term; its dedicated tests, SHA-256 manifest check, and same-code re-execution passed on the PR branch. It remains `INTERNAL_CANDIDATE`, is not release-authorized, and has not been merged into this public repository's `main`.

**Closed without merge:** PRs #2, #5, #6, and #7. Their work is not counted as merged or accepted. The Emerald research package and the stacked output-isolation, re-execution, and source-locator changes require content-level reconciliation against current `main` and surviving branches before any replacement or pass credit is claimed.

PR #9 is the status/traceability update represented by this branch. A closed-without-merge PR is not a completed deliverable, and a merged proposal is not an accepted policy or authorized release.

## Core deliverables

- Research charter and subject definition.
- Report 13 — Research Requirements and Gap Analysis.
- Report 14 — What to Build.
- Report 15 — How to Build What to Build.
- Traceability matrices linking tablet clauses, requirements, evidence, tests, and acceptance.
- Research and simulation ledgers with execution evidence and limitations.

**Research informs design. Evidence supports claims. Separate authorization governs implementation and release.**

## Public traceability (updated 2026-11-11)

This map uses only public locators. It does not copy private C2O tablet or corpus text.

| Step | Public locator | Gap |
|---|---|---|
| Requirement | [The UNIVERSALIS Ecosystem `prototype/REQUIREMENT_TRACE.md`](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/main/prototype/REQUIREMENT_TRACE.md) | Collection-level `UNI-001`…`UNI-015` is stated there as not implemented. Private ULC inventories stay in the private C2O research repository and are not copied here. |
| Research | `main`: `RESEARCH/` charter and Reports 13–15; `Golden-Compass/` working papers. UNI-RP-001-S remains in draft #8. | Research-package acceptance remains **GAP**. PR #2's Emerald package was closed without merge and requires recovery/reconciliation. |
| Simulation | Historical #2/#5/#6/#7 stack was closed without merge; #8 contains a separate synthetic package candidate. | No programme pass credit is awarded by these PR states. Historical package and execution evidence require recovery, provenance checks, and owner/reviewer disposition. |
| Spec | PR #1 and PR #3 are merged as proposed artifacts. | Owner acceptance, independent review, and reconciliation with governing C2O authority remain **GAP**. |
| Implementation | [The UNIVERSALIS Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem) `main` holds a LIMITED `prototype/` and `scaffold/` | This research repository has no product implementation tree. Implementation acceptance remains **GAP**. |

The charter, Reports 13–15, requirements register, and reciprocal stewardship proposal are now present on `main`. Research-package execution, historical PR recovery, independent review, owner acceptance, and release authorization remain open.
