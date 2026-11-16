# Source Qualification Addendum — Epistemic Coordinates
## v0.1.0 — UNIVERSALIS public source register

**Status:** Bounded desk review — pending review
**Date:** 2026-11-15
**Execution:** No tools installed, invoked, benchmarked or security-tested.

## 1. Biglan dimensions

- Biglan, Anthony (1973), “The Characteristics of Subject Matter in Different Academic Areas,” Journal of Applied Psychology 57(3), 195–203. DOI: https://doi.org/10.1037/h0034701. ERIC record: https://eric.ed.gov/?id=EJ080995.
- Hiller et al. (2026-01-08), “Faculty Perceptions of their Disciplinary Cultures: Re-Evaluating Biglan’s Dimensions,” Research in Higher Education. DOI: https://doi.org/10.1007/s11162-025-09875-1.

The original research supports three dimensions: paradigm development, concern with application, and concern with life systems. The 2026 re-evaluation reports variation within disciplines and cautions against rigid binary classification. Use contextual, revisable profiles, not immutable discipline labels.

## 2. Qualified public tools and standards

### Eigenius
- https://github.com/eigenius/eigenius
- https://eigenius.io/docs/epistemic-stack/
- https://arxiv.org/abs/2608.04457
- Documents declared, observed, derived and verified knowledge categories in a typed knowledge graph.
- Qualification: formally verified means a proof term checks under declared formal assumptions and a named checker. It does not establish the empirical truth of premises. Independent reproduction of project claims remains open.

### Temporal Knowledge Substrate
- https://pypi.org/project/mcp-temporal-knowledge/
- PyPI lists version 0.7.1, uploaded 2026-04-20.
- Describes a Neo4j-backed MCP server, domain/session history, NEXT_SESSION, EVOLVED_FROM, ten ontological types and eleven knowledge relationships.
- Qualification: merge_knowledge is documented as destructive chain compaction. Confirm exact package version and migration behaviour.

### OntoBricks
- https://ontobricks.org/documentation/index.html
- https://ontobricks.org/documentation/mcp.html
- https://github.com/databrickslabs/ontobricks
- Official site reports v0.9.0 in October 2026 and documents MCP and ontology/graph capabilities.
- The project is source-available under the Databricks License and depends on Databricks deployment, authentication and identity controls. Do not label it OSI-approved open source or generally local-first.

### Library of Congress Linked Data Service
- https://www.loc.gov/apis/additional-apis/linked-data-service/
- https://id.loc.gov/
- https://id.loc.gov/views/pages/swagger-api-docs/
- Official authority and bibliographic metadata APIs with resolvable controlled-vocabulary URIs.
- Qualification: subject authority normalization is not epistemic truth validation. An MCP wrapper is a separate implementation and needs its own source/version review.

## 3. Unpinned owner-supplied candidates

| Candidate | Claimed functionality | Current disposition |
|---|---|---|
| Knowledge Graph MCP | search, concept, ontology, epistemic_status, artifact | Exact canonical source/version not pinned |
| NOUZ | domain cores, semantic/tag/analogy bridges, core_drift, SLOI hierarchy | Exact canonical source/version not pinned |
| LC Vocabularies MCP | MCP adapter to Library of Congress linked data | Exact adapter not pinned; underlying LoC service is documented |
| arifOS ZEN | five primitives and domain/layer coordinates | Exact ZEN source/schema/version not pinned |

These candidates remain unverified, not rejected. Their interfaces, schema definitions, licensing, authentication, data flow, maintenance and tests must be checked before adoption.

## 4. Semantic controls

- “AFFIRMATIVE > 0.8” is not adopted as a general epistemic threshold.
- Declared, observed, derived and formally verified are warrant kinds, not identical truth statuses.
- Historical is a temporal qualifier, not a synonym for false.
- Subject headings and taxonomy IDs identify concepts; they do not prove propositions.
- Elemental affinity is an interpretive, multi-valued annotation, not a scientific measurement.
- Similarity and analogy bridges do not establish causation or ontological identity.
- A project README or preprint establishes that the project makes a claim; it is not an independent validation of every implementation claim.

## 5. Adoption prerequisites

Before use, pin canonical repository and release, license, dependencies, tool schemas, transport/authentication, source/version data, provenance, retention/deletion, correction behaviour, known limitations and independent tests. Verify data flows and deployment dependencies before describing any service as local-first or independently operable.

---

**End of Epistemic Coordinate Source Qualification Addendum**
