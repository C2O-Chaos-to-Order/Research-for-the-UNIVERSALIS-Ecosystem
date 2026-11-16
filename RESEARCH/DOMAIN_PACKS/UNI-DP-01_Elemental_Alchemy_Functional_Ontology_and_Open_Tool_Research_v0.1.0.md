# UNI-DP-01 — Elemental Alchemy: Functional Ontology, Combinatorial Derivation, and Open Tool Research
## Public research proposal v0.1.0

**Status:** Proposed public research package; independent review and source qualification pending
**Scope:** UNIVERSALIS-compatible ontology concepts, open/public tool research, and portable non-sensitive contracts
**Source basis:** Owner-supplied research notes; AI-assisted organization and bounded public-source qualification
**Implementation status:** Not started
**Research/simulation status:** No implementation or experiment executed by this document
**Release status:** Draft branch only; no merge or product adoption implied

---

## 1. Purpose

This document proposes a functional Elemental Alchemy ontology for systems research and surveys public tools that may help implement or investigate its roles.

The five primaries are functional roles, not literal substances:
- Air — information and communication.
- Earth — structure and constraints.
- Fire — energy and transformation.
- Water — flow and adaptation.
- Spirit — integration, interpretation, observability, and governance.

“Awareness” is used operationally for observation and self-assessment. The ontology makes no claim that software tools possess subjective consciousness.

## 2. Combinatorial foundation

For five distinct primaries, the number of unordered combinations containing k primaries is C(5,k):

| Level | k | Count |
|---|---:|---:|
| Primary | 1 | 5 |
| Secondary | 2 | 10 |
| Tertiary | 3 | 10 |
| Quaternary | 4 | 5 |
| Quintessential | 5 | 1 |
| **Total non-empty combinations** | | **31** |

The identity is exact: 2^5 − 1 = 31. This structure is a graded subset lattice, not a strict tree. The combination counts are mathematical; the assigned names and meanings are ontology proposals.

## 3. Primary roles and evidence

| Primary | Role | Public implementation/evidence examples |
|---|---|---|
| Air | Information, messaging, identity and routing | Protocol schemas, message traces, identity documents, source provenance |
| Earth | Structure, ontology, constraints, state | Ontology/graph version, schema validation, constraint checks |
| Fire | Compute, energy and transformation | Execution receipts, resource and energy measurements, operation versions |
| Water | Flow, routing, adaptation and reconciliation | Flow topology, synchronization events, merge plans, conflict histories |
| Spirit | Integration, interpretation, governance and observability | Governance decision, coordination trace, disagreement and review records |

A system may implement several roles. The roles are not an exclusive product taxonomy.

## 4. Proposed combination register

### 4.1 Secondary — ten pairs

| Pair | Proposed name | Functional hypothesis | Disposition |
|---|---|---|---|
| Air + Earth | Dust | Granular information/matter organized by structural constraints | Proposed |
| Air + Fire | Lightning | Transient directed discharge or high-energy information transfer | Proposed |
| Air + Water | Wave | Information propagating through adaptive flow | Open candidate; no accepted tool assignment |
| Air + Spirit | Sound | Structured information expressed through integrated communication | Proposed |
| Earth + Fire | Metal | Ordered structure transformed or energized while preserving conductive pathways | Proposed |
| Earth + Water | Ice | Flow constrained into a persistent structure | Proposed |
| Earth + Spirit | Crystal | Structured, integrated and persistent knowledge/memory | Proposed |
| Fire + Water | Steam | Energy driving flow and state transformation | Proposed |
| Fire + Spirit | Light | Energy/transformation made observable through integrated interpretation | Current proposal |
| Water + Spirit | Life | Adaptive, persistent and coordinated processes associated with living systems | Proposed |

A prior proposal assigned Light to Air + Fire. The current owner-proposed assignment is Fire + Spirit; preserve the earlier version as a revision-history item. Nature is not a pairwise element because its current proposed combination uses three primaries.

### 4.2 Tertiary — ten triples

| Combination | Proposed name | Functional interpretation |
|---|---|---|
| Air + Earth + Fire | Magma | Geological/material transformation |
| Air + Earth + Water | Weather | Planetary dynamics |
| Air + Earth + Spirit | Memory | Information embedded in structure |
| Air + Fire + Water | Storm | Energetic, flowing atmospheric/system dynamics |
| Air + Fire + Spirit | Radiance | Expression and transmission |
| Air + Water + Spirit | Dream | Symbolic cognition and imagination |
| Earth + Fire + Water | Blood | Living physical circulation |
| Earth + Fire + Spirit | Forge | Intentional transformation of structure or matter |
| Earth + Water + Spirit | Growth | Organized development |
| Fire + Water + Spirit | Soulfire | Drive, animation and sustained transformation |

### 4.3 Quaternary — five four-primary combinations

| Combination | Proposed name | Functional interpretation |
|---|---|---|
| Air + Earth + Fire + Water | Planet | Integrated physical/planetary processes |
| Earth + Fire + Water + Spirit | Creation | Formation and emergence of organized systems |
| Air + Fire + Water + Spirit | Consciousness | Information, energy, adaptation and integrated awareness-as-observation |
| Air + Earth + Fire + Spirit | Civilization | Organized knowledge, structure, energy and purpose |
| Air + Earth + Water + Spirit | World | Connected, structured, adaptive information-bearing system |

A combination that omits a functional role does not mean the corresponding physical phenomenon is literally absent.

### 4.4 Quintessential

\[
Air+Earth+Fire+Water+Spirit\rightarrow Quintessence
\]

Quintessence is the proposed integrated whole within this ontology. Universe, Cosmos, Totality, and Aether remain alternative associated names pending owner disposition. This is not a scientific theory of the physical universe.

### 4.5 Known classification gaps

- Air + Water remains open; Wave is a candidate, not accepted.
- Nature was previously listed as a secondary despite being Earth + Water + Fire. It belongs in the higher-order combination set.
- Nature and Blood both have an Earth + Fire + Water assignment. They can coexist only if their coupling mechanisms and emergent properties are explicitly differentiated.
- Light's current pair is Fire + Spirit, not the earlier Air + Fire proposal; Radiance remains Air + Fire + Spirit.

## 5. Derivation contract

\[
R=\Phi(P,\kappa,B,\tau)
\]

P is the primary set, κ the coupling mechanism, B the boundary conditions, and τ the temporal scale.

A derived element must state:
1. which primaries participate;
2. evidence for each primary;
3. the coupling mechanism;
4. observable emergent properties;
5. boundary and environmental conditions;
6. counterfactual/ablation behaviour;
7. reproduction and limitations.

A name or symbolic association does not establish emergence.

## 6. Public tool research candidates

This is a research inventory, not an adoption list. “Publicly documented” does not mean open source; “open source” does not guarantee production suitability. Pin each repository/package, version, commit, license, dependencies, source date, and claim before evaluation.

### 6.1 Air

| Candidate | Proposed role | Qualification |
|---|---|---|
| JetBrains Air | IDE/agent MCP connection surface | Official documentation states SSE is not supported. Verify the exact transport matrix for the client/version; distinguish stdio and Streamable HTTP from legacy SSE. |
| air-mcp-server / Agent Identity Registry | Agent lookup and W3C DID resolution | Distinct from JetBrains Air; check exact DID methods, data model, trust-score basis, and read/write scope. |
| Qualixar OS | Multi-provider agent runtime and routing | Provider/framework/transport counts are release-specific; verify auth, routing policy, data-egress and licensing. |
| Alchemy MCP / code-mode-alchemy-mcp | Blockchain state and transaction information | Exact server name/tool count varies in supplied descriptions; pin package and inspect RPC dependencies, wallet handling and simulation limits. |
| omni-mcp / metamcp | MCP aggregation | Review permission propagation, server identity, tool-name collisions, prompt/tool poisoning, and transitive dependencies. |

### 6.2 Earth

| Candidate | Proposed role | Qualification |
|---|---|---|
| EMMOntoPy / EMMO | Materials ontology access | EMMO means Elementary Multiperspective Material Ontology; it is materials-science-specific, not a universal elemental ontology. |
| open-ontologies | RDF/OWL, SHACL, SPARQL and reasoning | Tool counts change by release. Validate reasoning semantics, SHACL behaviour, import resolution, tests and license. |
| Quipu | Bitemporal knowledge graph/trust constraints | Current claims are research/project assertions; independently reproduce post-state gating, authority composition, concurrency and security invariants. |

### 6.3 Fire

| Candidate | Proposed role | Qualification |
|---|---|---|
| GreenPick | Design-time GPU/LLM carbon and energy estimates | Estimator outputs depend on workload, hardware, model, location/grid factors and boundaries; distinguish estimates from measurements. |
| Phase-decoupled power-control research | Adaptive GPU power/frequency control | Reported +24.1% tokens/J is experiment-specific; retain baseline, model, hardware and workload details. |
| Murakkab | Declarative workload and profile-guided optimization | Reported GPU/energy/cost reductions require independent reproduction and SLO comparison. |
| KAIROS | Context-aware GPU frequency/concurrency/placement | Validate controller safety, performance, hardware coverage and power measurement. |
| Joule | Per-response energy/carbon/cost telemetry | Validate calibration, measurement boundary, units, model coverage, and uncertainty. |

### 6.4 Water

| Candidate | Proposed role | Qualification |
|---|---|---|
| Graph Merge | Fork/edit/reconcile knowledge graphs with reviewed merge plans | A content digest is not a signature or authorization. Check revision conflicts, no-overwrite and apply semantics. |
| Mycelium | Multi-agent memory and contradiction synchronization | LLM-mediated contradiction resolution is advisory; validate provenance, authority, tenant isolation and correction propagation. |
| MCP-Injector | MCP protocol fault injection | Isolated staging only. Reported task-completion degradation applies to a specific fault profile, not all production systems. |

### 6.5 Spirit

| Candidate | Proposed role | Qualification |
|---|---|---|
| arifOS | Constitutional/governance kernel | Verdicts do not establish legal compliance or owner authority; pin version, rule implementation and license. |
| AgentKeeper | Memory/continuity infrastructure | Persistence is not proof of subjective identity or consciousness; validate migration, access, correction and recovery. |
| Synthesis | Engagement-quality evaluation | Exact repository and independent evaluation require confirmation; do not treat score as proof of empathy or sentience. |

### 6.6 Secondary candidate tooling

| Element | Candidates | Intended use | Qualification |
|---|---|---|---|
| Lightning | LiveAuth MCP Server | Proof-of-work/payment-gated calls and usage receipts | HMAC is a shared-secret MAC, not a public-key digital signature. |
| Dust | Dust.tt | Enterprise workspace search and knowledge resolution | Commercial hosted system; assess tenant boundary, data residency, connectors, subprocessors and export/deletion. |
| Sound | Soundbox; sound-gen-mcp | MCP audio, speech and TTS | Tool count/repository names vary; pin exact project and providers. |
| Ice | SirixDB; cks-mcp | Versioned, revisioned or immutable-by-design records | Validate exact revision/snapshot semantics, retention and restore; “immutable” depends on threat model. |
| Steam | Steam Web CLI | Steam Web API operations | Located candidate is a gaming API CLI, not substantiated as a generic workflow-transformation engine; reclassify or replace. |
| Metal | NornicDB MCP; ArangoDB | Graph traversal, historical reads, indexed retrieval | Validate MVCC and index semantics, query limits, consistency and benchmarks. |
| Light | Lightrun MCP | Live runtime observability | Runtime variables and stack data may contain secrets/PII; enforce scope, redaction, approval and audit. |
| Nature | SkillPuzzler | Research-oriented multi-agent self-evolution | Treat published results as research demonstration, not production qualification. |
| Life | LIFE MCP Server; LifeOS | Agent memory/coordination/continuity | Distinguish a stateless protocol boundary from persistent underlying application state. |
| Crystal | crystal-memory-mcp | Provenance-tracked memory and semantic knowledge | Knowledge-cell counts and honesty claims require pinned release and independent tests. |

## 7. Portable contracts

### ElementalBalance
Binds each primary role to its system responsibility, implementation/version, evidence references, units, measurement method, provenance, uncertainty, and measured/estimated/asserted status.

### CouplingRegime
Binds participating primaries, coupling mechanism, pairwise/higher-order classification, boundary conditions, emergent properties, counterfactual results, and limitations.

### SynthesisAttestation
Binds source balances and coupling records, resulting artifact/claim digest, verifier identity/trust status, result, and uncertainty.

### NegativeSpaceEvidence
Records expected structure, observation scope, confirmed absence, unsearched regions, access limitations, withheld/deleted/unavailable records, and unresolved unknowns.

These contracts are public research proposals. They do not convey access to private systems or establish a central authority.

## 8. Research and implementation boundaries

- Keep ontology proposals distinct from accepted canonical ontology content.
- Place approved domain taxonomies in the designated UNIVERSALIS ontology/domain repository only after review and versioning.
- Ensure tools can run independently and do not depend on external private credentials.
- Record licenses, attribution, and source provenance.
- Treat remote APIs, hosted workspaces, cloud inference, RPC providers, and telemetry as external trust boundaries.
- Avoid turning product labels into ontology facts.
- Measure actual role performance rather than assuming that naming a service Air/Earth/Fire/Water/Spirit proves the role.

## 9. Open work

- Owner disposition of the missing Air + Water pairing.
- Nature/Blood differentiation.
- Light assignment change and revision history.
- Quintessential naming.
- Tool/source qualification and licensing.
- Formal ontology implementation and counterfactual test suite.
- Independent review before promotion into a canonical domain repository.

---

**End of UNI-DP-01 v0.1.0**
