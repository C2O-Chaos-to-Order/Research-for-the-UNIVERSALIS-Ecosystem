# Four-Document Toolchain Coverage Register

**Date:** 2026-11-12  
**Scope:** Four owner-supplied toolchain documents: Human Knowledge; Powers / Energy Efficiency / Synergy; Human Capabilities; Mapping / Matrix / Organization / Ecosystem Mapping.  
**Purpose:** Preserve every named tool and architectural pattern, identify its owning repository, and distinguish a documented candidate from an implemented contract or an integrated product.

## 1. Reading the status labels

- **Documented:** Tool or pattern is explicitly recorded in its owning architecture and/or this full inventory.
- **Basic contract implemented:** A local, versioned schema/fixture/semantic check exists for the relevant data boundary.
- **CI passed:** The current semantic checks and repository baseline passed for the referenced branch commit.
- **Integrated:** A product adapter or deployable service has actually been connected and exercised against its real implementation.
- **Not integrated:** The named tool remains a candidate/reference pattern. Mention in a document is not installation, adoption, source verification, or demonstrated behavior.

At this review, the four documents are fully inventoried below. The foundational contracts exist for all four domains. **No third-party candidate is being represented as installed merely because it is listed.**

## 2. Canonical owning repositories and implementation records

| Source document | C2O owner | UNIVERSALIS owner | Basic executable foundation |
|---|---|---|---|
| Human Knowledge | [The-C2O-Human-Knowledge](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/tree/implementation/repository-foundation-2026-11-12) | [The-UNIVERSALIS-Human-Knowledge](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/tree/implementation/repository-foundation-2026-11-12) | Provenance/bi-temporal record contract, six versioned MCP request/response tool definitions, validator, synthetic fixture, CI |
| Powers / Energy | [The-C2O-Powers](https://github.com/C2O-Chaos-to-Order/The-C2O-Powers/tree/implementation/repository-foundation-2026-11-12) | [The-UNIVERSALIS-Intelligence-Powers](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/tree/implementation/repository-foundation-2026-11-12) | Measurement, task receipt, attenuable energy-budget grant, synergy evaluation, validator, synthetic fixtures, CI |
| Human Capabilities | [The-C2O-Human-Capabilities](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Capabilities/tree/implementation/repository-foundation-2026-11-12) | [The-UNIVERSALIS-Human-Capabilities](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Capabilities/tree/implementation/repository-foundation-2026-11-12) | Portable capability evidence record, consent/proctor/attestation gates, validator, synthetic fixture, CI |
| Mapping / Matrix / Organization | [The-C2O-Ecosystem](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/tree/implementation/repository-foundation-2026-11-12) | [The-UNIVERSALIS-Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/tree/implementation/repository-foundation-2026-11-12) | Typed architecture graph, provenance-bearing nodes/edges, matrix entries, reviewed proposals, validator, synthetic fixture, CI |

### Canonical source documents

- Human Knowledge: C2O and UNIVERSALIS each have HUMAN_KNOWLEDGE_ARCHITECTURE.md, MCP_INTERFACE_CONTRACTS.md, and HUMAN_KNOWLEDGE_VALIDATION.md.
- Powers: each owner has POWERS_ENERGY_ARCHITECTURE.md and POWERS_ENERGY_VALIDATION.md. C2O Intelligence Powers also has INTELLIGENCE_ENERGY_OPTIMIZATION.md.
- Human Capabilities: each owner has HUMAN_CAPABILITIES_ARCHITECTURE.md and HUMAN_CAPABILITIES_VALIDATION.md.
- Mapping: each ecosystem repository has ARCHITECTURE_MAPPING_AND_ORGANIZATION.md and ARCHITECTURE_MAPPING_VALIDATION.md.

## 3. Document 1 — Human Knowledge

### UNIVERSALIS candidates

| Layer | Every named candidate from the source |
|---|---|
| Graph / memory substrate | chip-memory; THOUGHT; Exocortex |
| Ontology validation | fabio-rovai/open-ontologies; Quipu |
| Provenance / audit / tacit knowledge | strata-agent-memory; Metis; memledger |
| Citation integrity / broad verification | retractionwatch-mcp; vivory-mcp-verification |

### C2O candidates

| Layer | Every named candidate from the source |
|---|---|
| Private knowledge workspace | CueCrux; Cressio Second Brain; C2 Companion |
| Claim / memory fabric | Pythia; C2Cognitive |
| Enterprise reference patterns | Cloudflare OS; CoWork OS; Kerdos OS |

### Shared Human Knowledge interface contracts

The six versioned MCP tool contracts implemented in both Human Knowledge repositories are: **memory_search; memory_remember; memory_think; correct; verify; audit**.

### Basic implementation present

- Human-knowledge record envelope with bi-temporal intervals, source lineage, consent, verification state, confidence lineage, contradiction/supersession, authority class, and erasure/tombstone representation.
- C2O and UNIVERSALIS enforcement profiles; public UNIVERSALIS rejects C2O Controlled authority.
- Shared six-tool MCP v1 registry and request/response definitions.
- Synthetic examples, positive/negative semantic tests, and repository CI.

### Still not integrated

No production graph database, temporal query engine, source connector, ontology reasoner, SHACL/OWL validation service, production MCP server, signed receipt store, external citation verifier, or tacit-knowledge workspace has been deployed. All candidate tools above remain pending source/license/maintainer/security/compatibility review.

## 4. Document 2 — Powers / Energy Efficiency / Synergy

### UNIVERSALIS candidates

| Function | Every named candidate from the source |
|---|---|
| Measurement / attribution | CodeCarbon; Zeus; Joular Core; Perfetto's Wattson |
| Carbon-aware scheduling | ebb-ai; Green SARC; GreenAccounter; Arboric |
| Inference-level reduction | Joule; ModeSwitch-LLM; SDSIE; llm-zipper; sleeping_gpu_inference |
| Workflow / multi-agent optimization | Murakkab; KAIROS; EcoxPU; SAGE |

### C2O candidates

- JADE Decision Governance.
- C2Cognitive.
- Paperclip.
- CueCrux.
- Pythia.
- Velorum.

### Shared measurement / attestation / synergy building blocks

- PDU physical-layer measurement.
- Intel RAPL CPU-package and memory-controller counters.
- Kepler pod/container attribution.
- NVIDIA Management Library (NVML) GPU sampling.
- InfluxDB as the time-series store in the supplied reference pattern (not a mandated central shared database).
- One-second / 1 Hz sampling target where the hardware and collector genuinely support it.
- Forecast-before-action record, carbon/energy receipt, Joule-compatible response-header mapping, and PACT Passport as a proposed attenuable capability-token substrate.
- S-v1 synergy factor computed locally from portable receipts; no central synergy oracle.

### Basic implementation present

- Shared v1 definitions for energy measurement, task receipt, attenuable energy-budget grant, and synergy evaluation.
- Measurement scope, meter method, uncertainty, sampling frequency, source/calibration references, and overlapping meter IDs.
- Forecast method, confidence, calibration reference, upper bounds, actual energy/carbon/cost, actual carbon-intensity source, SLO/outcome evidence, and signing fields.
- Parent/child budget non-widening rules and separate issuer/holder receipt references.
- S-v1 calculation and no-double-count requirement for PDU/RAPL/Kepler/GPU views.
- Ten negative cases in the semantic validator.

### Still not integrated

No live PDU/RAPL/Kepler/NVML collector, calibration pipeline, grid-carbon feed, production time-series service, carbon-aware scheduler, inference router, accelerator optimizer, cryptographic signing/verification service, private permit engine, or independently measured C2O–UNIVERSALIS synergy benchmark has been deployed. Candidate savings figures supplied for Green SARC, ModeSwitch-LLM, Murakkab, KAIROS, EcoxPU, and ebb-ai remain unverified research claims.

## 5. Document 3 — Human Capabilities

### UNIVERSALIS candidates

| Sub-layer | Every named candidate from the source |
|---|---|
| Sensory / accessibility | human-mcp; a11y-toolkit |
| Skill / capability attestation | Kredo; Gaia; ToolGym; SkillSeal |
| Human-in-the-loop / teaming | Everstaff; SecTrust; Magentic-UI; Enju; MOSAIC |
| Ethics / capability maturity | WIA-AUG-012; HCQM (Hierarchical Capability Map) |

The source states that human-mcp's Ears suite is planned; it is not recorded here as already complete. Product tool counts, coverage rates, and other numerical claims remain supplied claims, not independently verified facts.

### C2O candidates

| Sub-layer | Every named candidate or pattern from the source |
|---|---|
| Private audited knowledge / capability | CueCrux; Pythia; C2Cognitive; C2 Companion; JADE Decision Governance |
| Enterprise reference patterns | Cloudflare OS; CoWork OS; Kerdos OS |

### Shared portable trust substrates

PACT Passport (Protocol for Agent Capability and Trust); Open Agent Passport (OAP); Cognitive Skill Passport (CSP-0.1); Agent Passport System (APS); Cupel; MortarCAPS Human Capability Record; Enju; MOSAIC.

### Basic implementation present

- Portable subject/capability/proficiency record.
- Assessment, evidence artifact references and hashes, provenance, consent, independent reviewer/proctor, attestation metadata, and governance class.
- Human-subject consent gate; submitter/assessor cannot independently proctor their own mastery; mastery requires independent authorized review; public UNIVERSALIS rejects Controlled authority.
- Synthetic fixture, semantic validator, negative tests, and CI in both Human Capabilities repositories.

### Still not integrated

No sensory MCP server, WCAG automation, public capability registry, independent peer-attestation service, isolated skill-sealing service, human-supervision runtime, teaming laboratory, credential issuer/verifier, consent registry, or live qualification/proctoring workflow has been deployed. PACT Passport, OAP, CSP-0.1, APS, Cupel, and MortarCAPS are recorded as shared protocol candidates; they are not implemented by the current record schema.

## 6. Document 4 — Mapping / Matrix / Organization / Repository Structure / Ecosystem Mapping

### Architectural mapping and visualization candidates

- UNIVERSALIS: Kula; reponova; AnaxiGraph / AnaxiMCP; GRASP; wikifier; FlowForge; MokuGraph.
- C2O: Velorum; @datasynx/agentic-ai-cartography; WorkBraid.

### Matrix and dependency candidates

- UNIVERSALIS: FlowForge; wikifier; reponova; Kula.
- C2O: Velorum; GRASP; agentic-flow.

### Organization / hierarchy candidates

- UNIVERSALIS: Agentopology; QuinnAI; agents_Inc; Paperclip; AGI-Super-Team.
- C2O patterns: Paperclip (private instance); QuinnAI (private hierarchy); agents_Inc (authority-and-review pattern).

### Repository structure / agent taxonomy candidates

- ai-native-repo-template (ANR v0.2).
- gitagent.
- omni-agents-cli.

C2O's supplied adaptation adds authority classes and audit classes to the ANR context budget and maps gitagent knowledge/tools into private knowledge and authority-gated surfaces.

### Ecosystem mapping candidates

- ai-ecosystem-map.
- VisualAgents.
- Agent Fabric / Agent Visualizer.
- Reco Graph.
- AgentFolio.

### Shared structural contracts / artifacts

- MokuGraph JSON schema.
- Draw.io XML and the supplied @drawio/mcp pattern.
- WorkBraid proposal format.
- Agentopology .at topology language.
- Paperclip portable company template.
- Dependency-graph interchange schema (nodes, edges, weights, provenance).
- ai-ecosystem-map discovery schema.
- VisualAgents event format.
- Reco Graph identity/permission/action schema.

### Basic implementation present

- Portable architecture graph v1 with typed nodes, typed provenance-bearing edges, snapshot/scope/visibility, matrix entries, and proposals separate from accepted architecture.
- Referential integrity for edges and matrix entries; public graph restrictions against confidential/secret nodes and C2O Controlled authority; accepted proposal requires an independent reviewer and decision evidence; credential-bearing field names are rejected.
- Synthetic fixture, semantic validator, and CI in both ecosystem repositories.

### Still not integrated

No live repository/code graph discovery, system landscape scanner, dependency crawler, impact/blast-radius calculator, critical-path scheduler, matrix computation engine, organization/topology compiler, agent ecosystem sync service, VisualAgents runtime observer, MokuGraph renderer integration, Draw.io MCP editing integration, or WorkBraid proposal client has been deployed. The present graph contract is a portable baseline, not a complete mapping platform.

## 7. Cross-document dependencies and build order

1. **Foundation records and provenance:** Human Knowledge record/evidence contracts underpin source references, correction, reviewer identity, and audit evidence used by the other layers.
2. **Capability evidence:** Human Capabilities records demonstrate competence and assessment history; they do not grant authorization.
3. **Power measurement and budgets:** Powers records measure resource consumption and enforce budget/permit constraints; they do not establish human or agent competence.
4. **Architecture maps:** Mapping graphs show where systems, tools, dependencies, authority boundaries, measurement sources, and execution flows live; maps must distinguish documented, implemented, tested, and verified edges.
5. **Integration:** Add external adapters only after candidate verification and after each adapter has fixtures, conformance tests, least-privilege permissions, provenance, revocation, and independent review.

## 8. Whole-ecosystem status

| Area | Inventory in repositories | Basic contract | CI evidence | External tools actually installed/integrated |
|---|---|---|---|---|
| Human Knowledge | Complete source inventory recorded | Implemented | Passed in both repositories | None verified as installed |
| Powers | Complete source inventory recorded | Implemented | Passed in both repositories | None verified as installed |
| Human Capabilities | Complete source inventory recorded | Implemented | Passed in both repositories | None verified as installed |
| Mapping / Matrix / Organization | Complete source inventory recorded | Implemented | Passed in both repositories | None verified as installed |

The phrase “complete source inventory” means the named tools and patterns supplied in the four documents are listed here. It does not mean every candidate has passed due diligence or been integrated.

## 9. Boundary invariants

- UNIVERSALIS stays public, local-first, inspectable, and independently operable.
- C2O stays private, audit-gated, and authority-bounded.
- Shared schemas describe interoperability; they do not carry C2O credentials, private policies, authority tokens, private source material, operational receipts, or private budgets.
- Human capability claims do not imply consent or authorization.
- Measurement data is not permission to consume resources.
- A graph edge is not proof unless its evidence state and source are explicit.
- No tool receives adoption status solely because it was named in a source document.
