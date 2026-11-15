# UNI-DP-08 — Knowledge Subjects and Epistemic Coordinates
## v0.1.0 — UNIVERSALIS public research specification

**Status:** Proposed public domain pack — pending review  
**Date:** 2026-11-15  
**Boundary:** Public tools, open standards and portable contracts only  
**Implementation:** Not performed

## 1. Purpose

This domain pack defines a queryable model for locating a subject or claim by its discipline, epistemic warrant and elemental functional affinity:

\[
K = \langle D, E, S \rangle
\]

D identifies one or more knowledge domains; E records how a claim is warranted and currently assessed; S records which proposed functional roles (Air, Earth, Fire, Water, Spirit) contribute to the knowledge activity.

This is a structured coordinate, not a single score or fixed three-label tag. It sits alongside the Elemental Alchemy functional ontology and the material-property layer. It does not replace either.

## 2. Three distinct dimensions

### 2.1 Domain D

Store an identified domain or discipline using stable identifiers, preferred labels, aliases, broader/narrower relations, taxonomy source/version and context. One subject may belong to several disciplines and application domains.

Biglan's three disciplinary dimensions can be stored as contextual metadata:
- hard–soft: paradigm development or disciplinary consensus;
- pure–applied: orientation toward practical application;
- life–nonlife: focus on living systems.

Biglan's 1973 research derived these dimensions from scholars' similarity judgments across academic subject areas. A 2026 re-evaluation reports within-discipline variation and warns that rigid categorical use may obscure nuance and change. Store the context, population, assessment method, date and uncertainty; do not make a permanent hard/soft, pure/applied, or life/nonlife assignment without evidence.

Biglan is one disciplinary lens, not a universal knowledge-domain ontology.

### 2.2 Epistemic profile E

E must separate what kind of warrant a record has from what an evidence assessment currently concludes.

**Warrant kind**
- DECLARED — an identified party asserted it.
- OBSERVED — a source, measurement or event was recorded with provenance.
- DERIVED — produced by a traceable inference or typed pipeline.
- FORMALLY_VERIFIED — checked proof under declared formal assumptions and a named checker.

**Assessment disposition**
- SUPPORTED
- CONTESTED
- CONTRADICTED
- INSUFFICIENT_EVIDENCE
- UNASSESSED
- SUPERSEDED

Historical status is a temporal/context annotation, not a truth disposition. An observation establishes what was recorded; a derivation establishes what follows from its inputs; a formal proof establishes derivability under its assumptions. None should be inflated into universal empirical truth.

Eigenius publicly documents the declared / observed / derived / verified pattern. It is a useful implementation precedent, not a universal standard.

**Confidence:** optional and method-specific. A numeric score requires a named method, calibration population, sample, uncertainty interval, assessor/model version and interpretation. Do not adopt AFFIRMATIVE > 0.8 as a universal rule. If retaining an AFFIRMATIVE label for compatibility, document its mapping to SUPPORTED and the assessment method.

### 2.3 Elemental affinity S

S is a many-to-many, context-specific annotation of the functional roles involved:
- AIR — information, encoding and communication;
- EARTH — structure, classification and constraints;
- FIRE — transformation, experimentation and computation;
- WATER — flow, adaptation and lifecycle;
- SPIRIT — integration, interpretation and coordination.

A domain can have several affinities. A single discipline may exhibit different role profiles across teaching, theory, experiment, design, governance and application. Affinity is an interpretive architecture overlay, not a physical measurement or a verdict about truth.

## 3. Subject, domain, claim and evidence are different entities

Keep separate identifiers and relationships for:
- Subject or concept being discussed.
- Domain or discipline that studies it.
- Claim asserted about the subject.
- Evidence item (source, observation, data, measurement or proof).
- Warrant describing what the evidence establishes.
- Assessment disposition and review history.
- Elemental-affinity profile for the specified activity/context.

A subject can have multiple domains and claims; a claim can have multiple supporting and contradicting evidence items. Do not flatten disagreement into a single status string.

## 4. The knowledge quality rule

A claim is not “good” merely because it is labelled AFFIRMATIVE or its elemental profile is balanced. Evaluate evidence fit, provenance, method, scope, reproducibility, uncertainty, independent support, contradictory evidence, temporal validity and review status.

Elemental affinity may highlight a missing functional perspective. It cannot substitute for domain-specific evidence standards.

## 5. Owner-proposed epistemic regimes

The secondary and tertiary elemental knowledge regimes are retained as interpretive mappings, not empirical academic classifications.

### Secondary
| Regime | Primaries | Proposed knowledge function |
|---|---|---|
| Lightning | Air + Fire | Rapid cross-domain transfer |
| Ice | Water + Earth | Archived and time-versioned knowledge |
| Dust | Air + Earth | Granular classification |
| Sound | Air + Spirit | Structured expression and communication |
| Steam | Fire + Water | Knowledge transformation through process |
| Metal | Earth + Fire | Formalization and machine-checkable constraints |
| Light | Fire + Spirit | Interpretive illumination and synthesis |
| Nature | Prior definition: Earth + Water + Fire | Adaptive knowledge; conflicts with pairwise tier |
| Life | Water + Spirit | Continuity and knowledge lifecycle |
| Crystal | Earth + Spirit | Structured persistent memory |

Nature's three-primary composition conflicts with listing it as secondary. The public research record preserves this owner decision as unresolved. Do not silently remap it.

### Tertiary
| Regime | Primaries | Proposed knowledge function |
|---|---|---|
| Magma | Air + Earth + Fire | Paradigm transformation |
| Weather | Air + Earth + Water | Discipline-level epistemic dynamics |
| Memory | Air + Earth + Spirit | Structured, provenance-bearing information |
| Storm | Air + Fire + Water | Rapid, contested knowledge flow |
| Radiance | Air + Fire + Spirit | Expressive synthesis |
| Dream | Air + Water + Spirit | Analogical and associative synthesis |
| Blood | Earth + Fire + Water | Circulation of validated knowledge |
| Forge | Earth + Fire + Spirit | Deliberate knowledge-artifact transformation |
| Growth | Earth + Water + Spirit | Organized adaptive expansion |
| Soulfire | Fire + Water + Spirit | Purpose-directed knowledge activity |

These are proposed semantics, not claims of literal elemental substances.

## 6. Open tooling candidates and deployment distinctions

### Eigenius
Public sources:
- https://github.com/eigenius/eigenius
- https://eigenius.io/docs/epistemic-stack/
- https://arxiv.org/abs/2608.04457

Describes a typed knowledge graph with declared, observed, derived and formally verified warrants. Formal verification is proof-relative; empirical premises and model assumptions remain explicit. Independent reproduction is still required.

### Temporal Knowledge Substrate
- https://pypi.org/project/mcp-temporal-knowledge/

PyPI describes a Neo4j-backed MCP server with domain/session histories, NEXT_SESSION, EVOLVED_FROM chains, ten ontological types, five sub-labels, and eleven knowledge relationship types in version 0.7.1. The package also documents a destructive chain-compaction operation. Review exact version, migrations, data retention and operator permissions before use.

### OntoBricks
- https://ontobricks.org/documentation/index.html
- https://ontobricks.org/documentation/mcp.html
- https://github.com/databrickslabs/ontobricks

Documents domain ontology construction, graph access, MCP and SHACL-related validation. The project is source-available under the Databricks License and relies on Databricks deployment and identity services. It must not be represented as a generally local-first or OSI-approved open-source service.

### Library of Congress Linked Data Service
- https://www.loc.gov/apis/additional-apis/linked-data-service/
- https://id.loc.gov/
- https://id.loc.gov/views/pages/swagger-api-docs/

Official authority and bibliographic metadata service with resolvable vocabulary URIs. It can normalize subject identifiers and headings; it does not determine whether a claim is true.

### Unpinned candidates
The exact canonical source/version was not established for:
- the owner-described Knowledge Graph MCP server with search / concept / ontology / epistemic_status / artifact;
- NOUZ domain-core and semantic-bridge engine;
- the specific LC Vocabularies MCP adapter;
- the owner-described arifOS ZEN coordinate implementation.

Keep these as unverified candidates until their canonical source, release, license, interfaces, and evidence are pinned. Do not treat owner descriptions as independent verification.

## 7. Portable contracts

**EpistemicCoordinate:** subject/claim references, domain IDs and taxonomy versions, Biglan context profile, warrant kind, disposition, optional calibrated confidence, elemental-affinity profile, provenance and temporal validity.

**SubjectTaxonomyRecord:** preferred label, aliases, stable URI, broader/narrower/related links, authority source, version, language/context and reviewer disposition.

**ClaimWarrantRecord:** claim, source/evidence, warrant kind, inference method, assumptions, limitations, review, contradiction and correction links.

**ElementalAffinityRecord:** subject/activity, role contributions, optional weighted profile, mapping method, evidence, scope and version.

**BridgeDiscoveryReceipt:** source/target domains and concepts, bridge type, similarity/analogy method, threshold, evidence, human disposition and limitations. Similarity is not causation or identity.

**DriftDetectionRecord:** prior/current domain profiles, observation window, method, uncertainty, affected dependents and review disposition. A drift alert does not automatically reclassify a domain.

**QuintessenceAttestation:** optional evidence for integration across five roles. It must separately assess coverage, consistency, coordination, authorization and claim validity rather than rely on an unvalidated universal coherence score.

## 8. Validation requirements — proposed, not executed

1. Support multiple domain assignments for one subject.
2. Preserve source, context, method and date for Biglan profiles.
3. Allow domain classifications to evolve with history intact.
4. Distinguish subject authority from truth assessment.
5. Preserve provenance for observations.
6. Preserve inputs, assumptions and steps for derivations.
7. Require proof objects, checkers and formal assumptions for FORMALLY_VERIFIED.
8. Permit withdrawal or correction when sources or proof assumptions fail.
9. Reject uncalibrated confidence as a probability.
10. Keep elemental affinity independent from epistemic disposition.
11. Preserve conflicting evidence.
12. Distinguish historical context from truth disposition.
13. Require review before domain reassignment.
14. Prevent semantic similarity from being interpreted as causation.
15. Allow independent reconstruction from portable evidence references.

## 9. Boundary and status

This package describes public tools and portable schemas only. It contains no private credentials, policy configuration, internal services or private operational data. UNIVERSALIS must remain independently operable and must not depend on private C2O infrastructure.

No tools were installed or executed, no knowledge graph was deployed or migrated, no benchmark or formal proof was produced, and no source-code/security/legal audit or owner acceptance was performed. This is a proposed research specification, not an implementation or release commitment.

---

**End of UNI-DP-08 v0.1.0**
