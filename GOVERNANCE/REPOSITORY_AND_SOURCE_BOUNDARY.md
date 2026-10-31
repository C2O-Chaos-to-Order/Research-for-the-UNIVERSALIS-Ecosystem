# UNIVERSALIS Repository and Source Boundary

**Document ID:** UNI-GOV-REPO-001  
**Version:** 0.1.0  
**Status:** Proposed repository ownership map; owner review pending.

## Governing distinction

**C2O is Private Source. UNIVERSALIS is Open Source.** Public product development and private company operations remain distinct. Any interoperability must use an explicitly governed interface.

## Repository responsibilities

| Repository | Intended responsibility |
|---|---|
| `Research-for-the-C2O-Ecosystem` | Governing C2O Research Plan and paired technical/Human Tablet source collections. |
| `Research-for-the-UNIVERSALIS-Ecosystem` | Public UNIVERSALIS research, evidence, reports, requirements, test protocols and review records. |
| `The-UNIVERSALIS-Ecosystem` | Public product architecture, source code, tests, developer documentation, build workflows, packages and releases. |
| `The-C2O-Ecosystem` | Private C2O governance, J.A.R.V.I.S. operations, private infrastructure, internal systems and coupling controls. |

## Domain repositories

Existing UNIVERSALIS domain repositories for ontology, human/intelligence powers, skills, capabilities and knowledge should remain taxonomy/content repositories. The product repository should consume approved, versioned domain data through documented interfaces rather than duplicating those corpora.

Several current repository descriptions retain GAIA wording. Conduct a separate naming, ownership and scope audit before treating them as authoritative UNIVERSALIS registries. Do not mass-rename or modify them as part of this initial research work.

## GIDEON prototype handling

The GIDEON Continuity Core v0.1.0 was merged into the private C2O repository's `integration/human-technical-tablets-gideon-jarvis-v1-0-0` branch, not into that repository's `main` branch. It is an experimental local reference implementation with explicit security, privacy, persistence, concurrency and deployment limitations.

It is evidence and a design reference, not an approved public product release. Do not copy it wholesale into the public UNIVERSALIS repository. Derive public implementation from approved requirements and independently reviewed design. Any specific code transfer requires source classification, licensing/IP, dependency, secret and security review and explicit owner approval.

## C2O–UNIVERSALIS interface

Any future coupling must define system identity, authenticated principals, data ownership and classification, purpose and permitted flows, authorization scope and revocation, API versioning, audit and incident handling, privacy and licensing/IP, isolation, recovery, and termination.

No automatic mirroring or shared credentials. Public UNIVERSALIS must not read C2O private resources by default. C2O governance does not make public users agents of C2O.

## Change control

This map does not create, rename, change visibility, merge, or repurpose repositories. It records proposed responsibilities for owner review. Verify repository visibility and content before each transfer or release.
