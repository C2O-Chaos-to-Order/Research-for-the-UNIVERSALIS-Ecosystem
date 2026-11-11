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
| `The-UNIVERSALIS-Ecosystem` | Public; README initialized, no product implementation yet. Product architecture, source code, tests, developer documentation, build workflows, packages and releases will live here. |
| `The-C2O-Ecosystem` | Private C2O governance, J.A.R.V.I.S. operations, private infrastructure, internal systems and coupling controls. |

## Domain repositories

Existing UNIVERSALIS domain repositories for ontology, human/intelligence powers, skills, capabilities and knowledge should remain taxonomy/content repositories. The product repository should consume approved, versioned domain data through documented interfaces rather than duplicating those corpora.

Existing public domain repositories discovered in the organization are:

- `The-UNIVERSALIS-Ontology`
- `The-UNIVERSALIS-Human-Powers`, `The-UNIVERSALIS-Human-Skills`, `The-UNIVERSALIS-Human-Capabilities`, `The-UNIVERSALIS-Human-Knowledge`
- `The-UNIVERSALIS-Intelligence-Powers`, `The-UNIVERSALIS-Intelligence-Skills`, `The-UNIVERSALIS-Intelligence-Capabilities`, `The-UNIVERSALIS-Intelligence-Knowledge`
- `The-UNIVERSALIS-Encyclopedias`

Treat these as domain/content repositories pending a content and ownership audit. Their descriptions currently retain GAIA wording, so canonical naming and scope must be reconciled before integration. Do not infer that the plural Encyclopedias repository is an official GAIA Encyclopedia or an approved universal source of truth.

Several current repository descriptions retain GAIA wording. Conduct a separate naming, ownership and scope audit before treating them as authoritative UNIVERSALIS registries. Do not mass-rename or modify them as part of this initial research work.

## Private-source exclusion

No private C2O prototype code, branch names, credentials, configuration, data, operational records, or infrastructure details are included in this public proposal or used as evidence for its claims. Any future proposal to derive public implementation from private C2O material requires source classification, licensing/IP, dependency, secret and security review, and explicit owner release approval. Public UNIVERSALIS repositories must not acquire ambient access to C2O private resources.

## C2O–UNIVERSALIS interface

Any future coupling must define system identity, authenticated principals, data ownership and classification, purpose and permitted flows, authorization scope and revocation, API versioning, audit and incident handling, privacy and licensing/IP, isolation, recovery, and termination.

No automatic mirroring or shared credentials. Public UNIVERSALIS must not read C2O private resources by default. C2O governance does not make public users agents of C2O.

## Change control

This map does not create, rename, change visibility, merge, or repurpose repositories. It records proposed responsibilities for owner review. Verify repository visibility and content before each transfer or release.
