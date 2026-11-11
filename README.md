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

## Status

`main` is an initialization plus the Golden-Compass working papers. It is not yet the home of the research packages described below.

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

## Core deliverables

- Research charter and subject definition.
- Report 13 — Research Requirements and Gap Analysis.
- Report 14 — What to Build.
- Report 15 — How to Build What to Build.
- Traceability matrices linking tablet clauses, requirements, evidence, tests, and acceptance.
- Research and simulation ledgers with execution evidence and limitations.

**Research informs design. Evidence supports claims. Separate authorization governs implementation and release.**

## Public traceability (2026-11-10)

This map uses only public locators. It does not copy private C2O tablet or corpus text.

| Step | Public locator | Gap |
|---|---|---|
| Requirement | [The UNIVERSALIS Ecosystem `prototype/REQUIREMENT_TRACE.md`](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/main/prototype/REQUIREMENT_TRACE.md) | Collection-level `UNI-001`…`UNI-015` is stated there as not implemented. Private ULC inventories stay in the private C2O research repository and are not copied here. |
| Research | This `main`: `Golden-Compass/`. Packages: drafts #1–#8, especially #2 (UNI-RP-001) and #8 (UNI-RP-001-S) | Packages are not on `main`. Acceptance of any draft execution is **GAP**. |
| Simulation | Claimed on the #2/#5/#6/#7 stack | **GAP** on this `main`. Not treated as accepted evidence here. |
| Spec | Draft #1 (charter and reports 13–15); draft #3 (reciprocal stewardship charter) | **GAP** on this `main`. |
| Implementation | [The UNIVERSALIS Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem) `main` holds a LIMITED `prototype/` and `scaffold/` | This research repository has no product implementation tree. Implementation acceptance remains **GAP**. |

Evidence is behind the planned README deliverables (charter, reports 13–15, matrices, ledgers) until those drafts are reviewed and, if the owner later authorizes it, merged.
