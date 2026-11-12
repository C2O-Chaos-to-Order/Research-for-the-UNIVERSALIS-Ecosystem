> **Register status — 2026-11-12:** This file remains the historical inventory of the first four supplied toolchain documents. The current consolidated register covers all ten source inventories, including Intelligence Capabilities, Intelligence Skills, Intelligence Powers, Human Powers and Ontologies: [public UNIVERSALIS master toolchain coverage register](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md). Use the master register for current coverage, implementation status, and CI evidence.

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
| Human Knowledge | C2O private owner repository (not exposed through this public register) | [The-UNIVERSALIS-Human-Knowledge](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/tree/implementation/repository-foundation-2026-11-12) | Provenance/bi-temporal record contract, six versioned MCP request/response tool definitions, validator, synthetic fixture, CI |
| Powers / Energy | C2O private Powers owner repository (not exposed through this public register) | [The-UNIVERSALIS-Intelligence-Powers](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/tree/implementation/repository-foundation-2026-11-12) | Measurement, task receipt, attenuable energy-budget grant, synergy evaluation, validator, synthetic fixtures, CI |
| Human Capabilities | C2O private Human Capabilities owner repository (not exposed through this public register) | [The-UNIVERSALIS-Human-Capabilities](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Capabilities/tree/implementation/repository-foundation-2026-11-12) | Portable capability evidence record, consent/proctor/attestation gates, validator, synthetic fixture, CI |
| Mapping / Matrix / Organization | C2O private ecosystem owner repository (not exposed through this public register) | [The-UNIVERSALIS-Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/tree/implementation/repository-foundation-2026-11-12) | Typed architecture graph, provenance-bearing nodes/edges, matrix entries, reviewed proposals, validator, synthetic fixture, CI |

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
- One-second / 1 Hz sampling target where the hardware and collector genuinely support it; GPU power integration using the trapezoidal rule over the full decision window, including inference, tool execution, and communication delays.
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

## 10. Source-specific functions and implementation notes to preserve

The following details are transcribed as requirements or product descriptions from the four supplied documents. They are not independently verified product facts; maintain them as testable acceptance questions during later tool review.

### Human Knowledge — source-specific notes

- **chip-memory:** local-first temporal graph; bi-temporal edges; single-valued predicates supersede earlier facts without silent deletion; source type, confidence, and access history; human-in-the-loop review; MCP actions described as memory search, remember, context, think, bump, and a "why" audit trail.
- **THOUGHT:** typed edges with mandatory source references; explicit CONTRADICTS edges at ingestion; query routing among vector, fact, change, and hybrid structures. The source calls out HippoRAG 2 personalized PageRank, Graphiti bi-temporal semantics, corrective RAG, and Ebbinghaus-style decay as techniques to evaluate.
- **Exocortex:** Rust-code ontology, deterministic ingestion, no LLM in the core path, local-first operation, Git/document adapters, and a CI-enforced deterministic/performance posture. The source's 29-microsecond p50 over 100,000 memories is a benchmark claim to reproduce.
- **fabio-rovai/open-ontologies:** Rust MCP server pattern with an in-memory Oxigraph store, OWL 2-DL reasoning, SHACL, SPARQL, and ontology versioning; the source emphasizes a single binary without JVM.
- **Quipu:** bitemporal data/trust/verdict/rule records, post-state gate predicates, named graphs as authority units, non-widening composition, signed verdicts, and audit as a query. The source states 28 MCP tools.
- **strata-agent-memory:** append-only claim ledger, proof receipt required for an outcome, independent replay rather than self-review, dependency taint after refutation, and receipts for compiled context inclusion/exclusion and rendered-text hash.
- **Metis:** consented tacit-knowledge fragments with applicability conditions (site, equipment, operating mode, shift, role, risk), named human reviewers, evidence-derived confidence, and Evidence/Advisory/Controlled authority tiers.
- **memledger:** attribution, confidence, derivation chain, audit trail, and weakest-link confidence across ancestry.
- **retractionwatch-mcp:** retraction/withdrawal/expression-of-concern/correction flags based on the Retraction Watch data; the source describes six MCP tools and Crossref/CC-BY redistribution.
- **vivory-mcp-verification:** broad verification surface; the source claims 98 tools across 36 categories. Tool coverage and licensing must be checked before using the count as a planning assumption.
- **CueCrux:** encrypted cited corpus, trusted-reference drift watch, organizational constraints, Light/Verified/Audit modes, signed proof receipt in Verified, and historical as-of replay; source claims 92 MCP tools across nine endpoints.
- **Cressio Second Brain:** organization-owned approved content, every answer cites a source or logs an evidence gap, verified outcomes written back, portable handoff.
- **C2 Companion:** version-controlled operator knowledge base, Git history as audit trail, NIST CSF 2.0 baseline with SOC 2 / ISO 27001 overlays.
- **Pythia:** atomic claims, temporal/scope/conflict/duplicate adjudication, correction propagation, source-edit/delete handling, and a deliberately small five-tool MCP surface (search, open, timeline, correct, define) plus stored-knowledge-only push briefing.
- **C2Cognitive:** typed L0–L3 memory tiers with bounded authority.
- **Cloudflare OS / CoWork OS / Kerdos OS:** reference patterns for zero-permission starts, resource-specific authorization, approval gates, budgets, audit sidecars, redaction/suppression/expansion, and reviewable step histories. These are reference patterns in the supplied document, not direct deployment instructions.

### Powers — measurement and optimization details

- **CodeCarbon:** hardware energy-counter use where available, with CPU-load/TDP estimation fallback; estimated readings must remain distinguishable from counter measurements.
- **Zeus:** GPU/CPU/DRAM and other accelerator energy profiling/optimization with monitoring export; actual supported hardware and versions require verification.
- **Joular Core:** cross-platform power/energy measurement with language interfaces.
- **Perfetto Wattson:** trace-level per-thread power attribution; attribution must not be mistaken for a second independent meter.
- **Shared measurement reference:** PDU → RAPL → Kepler plus GPU NVML. The source specifies one-second PDU/RAPL/Kepler series to InfluxDB, GPU sampling at 1 Hz, and trapezoidal energy integration over the whole decision window (inference, tool execution, and communications). Treat this as a reference implementation pattern; reconcile nested/overlapping scopes before totaling.
- **ebb-ai:** defer non-urgent tasks to windows selected using grid intensity, provider pricing, and hardware conditions; produce per-task carbon receipt.
- **Green SARC:** forecast-before-action token/carbon gate with a conformal bound; source-provided savings figures are benchmark claims, not guarantees.
- **GreenAccounter / Arboric:** multi-cloud and orchestration-layer workload timing/placement patterns; migration requires checkpoint, compatibility, data-residency, and SLO testing.
- **Joule:** OpenAI-compatible request boundary and per-response energy/CO2/cost headers; header provenance must be checked before treating values as measured facts.
- **ModeSwitch-LLM / SDSIE / llm-zipper / sleeping_gpu_inference:** mode routing, energy-proportional serving, compression/quality tradeoffs, and local inference patterns, respectively.
- **Murakkab / KAIROS / EcoxPU / SAGE:** workflow profile optimization; context-aware resource controls; heterogeneous accelerator placement; separate optimization and sustainability-audit roles. Reported savings require matched workload, model, hardware, SLO, quality, latency, and accounting boundaries.
- **C2O governance:** JADE human-held permit, C2Cognitive authority tier, Paperclip budget/audit/rollback, CueCrux signed as-of receipt, Pythia energy-claim correction, and Velorum impact mapping. A token budget, cost budget, carbon ceiling, and joule budget are distinct units and controls.
- **PACT Passport:** proposed holder-bound attenuable budget/capability delegation with independent receipts. The current Powers grant is a structural contract only; it is not PACT protocol interoperability.

### Human Capabilities — source-specific notes

- **human-mcp:** source describes 29 tools across Eyes (4), Hands (18), Mouth (4), Brain (3); Ears (speech/audio) is described as planned.
- **a11y-toolkit:** source describes 32 MCP tools, six prompts, a WCAG 2.2 audit/fix/document/watch/handoff loop, screen-reader-only blindfold usability testing, signable evidence packs, and VPAT 2.5 drafts. The stated 51/55 criteria coverage is a claim to reproduce.
- **Kredo:** peer-issued, skill-specific, evidence-linked Ed25519 attestations, with verify/revoke/dispute and trust-graph behavior.
- **Gaia:** public evidence ledger and Trust Magnitude based on evidence type, weight, and freshness; source-supplied thresholds are not adopted as C2O/UNIVERSALIS policy.
- **ToolGym:** workout receipt → simulation receipt → qualification record → independent-proctor-reviewed mastery credential; the learner cannot approve their own field evidence; expiration/recertification is part of the source ladder.
- **SkillSeal:** isolated Docker execution, no network, read-only filesystem, resource limits, syscall capture, artifact/test hashes, and Ed25519 evidence signing. Signature verification and the evaluator/certifier separation require explicit tests.
- **Everstaff / SecTrust:** human approval modes and asynchronous queues; observable DAG/task registry; dangerous-action approvals expire to deny; voting is advisory rather than an execution grant.
- **Magentic-UI / Enju / MOSAIC:** co-planning and guarded human-agent interaction; humans and agents as peers on a shared Git-backed task graph; isolated IPC workers with a universal operator interface and reproducible cross-paradigm evaluation.
- **WIA-AUG-012 / HCQM:** augmentation-ethics reference and human capability taxonomy. Source describes HCQM as eight domains, 32 constructs, about 120 subcomponents and about 130 behavioral indicators; these counts and taxonomy version need verification.
- **PACT / OAP / CSP-0.1 / APS / Cupel / MortarCAPS:** portable identity/authority, skill identity/runtime separation, competence provenance, credential and consent patterns. None is implemented by the current portable human-capability evidence envelope.

### Mapping / Matrix / Organization — source-specific notes

- **Kula:** Git repository graph in RDF, Turtle/JSON-LD export, SPARQL query, symbol-aware fences, graph diff and code-anchored memory.
- **reponova:** source describes 11 MCP tools for search, impact, shortest path, semantic similarity and community detection.
- **AnaxiGraph / AnaxiMCP:** typed repository graph distinguishing source facts, inferred meaning, and proposed design.
- **GRASP:** source describes 150 MCP tools, 35 languages, 10 graph views, multimodal ingestion and security/dependency outputs. Claims and language coverage require reproduction.
- **wikifier:** file-health matrix, dependency/import graph, cycles, confidence, and agent-facing wiki.
- **FlowForge:** evidence-cited LLM/MCP/API call flow, DAG scheduling, retry/fallback mapping and critical-path analysis.
- **Velorum:** private deterministic enterprise context graph and pre-change impact system mapper.
- **@datasynx/agentic-ai-cartography:** read-only MCP system-landscape map with recursive dependency traversal.
- **WorkBraid:** Git-backed proposal workbench; proposed and accepted architecture remain distinct; change before/after comparison and review gate.
- **agentic-flow:** min-cut task dependency partitioning and graph analytics for delegation.
- **Agentopology:** declarative .at topology source compiled to platform-native agent configurations; source lists Claude Code/Workflow, OpenClaw, Codex, Cursor, Gemini CLI and Copilot targets.
- **QuinnAI / agents_Inc / Paperclip / AGI-Super-Team:** org tree and OKR cascade; CEO→CoS→Lead→Worker review pattern; budgets/governance/rollback; source describes 14 role packs, 92 optional specialists, eight team manifests and 18 runtime adapters.
- **ANR v0.2:** AGENTS.md, context index, src/tests/tools/docs/skills/workflows/guardrails; context classes startup, on_demand, archive, runtime; C2O extension adds authority and audit classes. The source lists context-index fields path, purpose, read_when, source_of_truth, context_cost.
- **gitagent / omni-agents-cli:** portable versioned agent definitions and centralized distribution of agents/skills/rules.
- **ai-ecosystem-map / VisualAgents / Agent Fabric / Agent Visualizer / Reco Graph / AgentFolio:** discovery and inventory of agents/skills/MCP/rules; workflow/event visualization and replay; external agent scanning; identity/permission/connection/action graph; curated discovery directory. Any visualizer that exposes model-internal reasoning requires a privacy/safety review; prefer observable action and event traces rather than disclosure of private reasoning.
- **MokuGraph / Draw.io / shared formats:** MokuGraph JSON rendering schema; Draw.io XML and supplied MCP 3.0 Task Protocol pattern; WorkBraid proposal format; Agentopology .at; Paperclip template; dependency graph interchange. These are separate contracts/adapters still to be implemented, not all covered by the generic architecture graph v1.

## 11. Executed CI receipts for the four basic foundations

These run links show the dedicated contract workflows and repository-quality baselines passed. Mapping owners also retain their additional repository validation workflows.

| Domain | C2O contract / graph | C2O quality | UNIVERSALIS contract / graph | UNIVERSALIS quality |
|---|---|---|---|---|
| Human Knowledge | [43233037409](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/actions/runs/43233037409) | [43233037332](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/actions/runs/43233037332) | [43233072778](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/actions/runs/43233072778) | [43233072777](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/actions/runs/43233072777) |
| Powers / Energy | [43237146027](https://github.com/C2O-Chaos-to-Order/The-C2O-Powers/actions/runs/43237146027) | [43237145898](https://github.com/C2O-Chaos-to-Order/The-C2O-Powers/actions/runs/43237145898) | [43237154087](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/actions/runs/43237154087) | [43237154046](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/actions/runs/43237154046) |
| Human Capabilities | [43238884857](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Capabilities/actions/runs/43238884857) | [43238884861](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Capabilities/actions/runs/43238884861) | [43238904991](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Capabilities/actions/runs/43238904991) | [43238904935](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Capabilities/actions/runs/43238904935) |
| Mapping / Matrix | [43238968417](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/actions/runs/43238968417) | [43238968426](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/actions/runs/43238968426) | [43238990961](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43238990961) | [43238991355](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43238991355) |

Additional ecosystem checks:
- C2O Repository Verification: [43238969066](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/actions/runs/43238969066).
- UNIVERSALIS Engineering Doctor: [43238991130](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43238991130).
- UNIVERSALIS Repository Verification: [43238991044](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43238991044).

These runs establish that the authored semantic checks and repository baseline passed for the synthetic fixtures. They do **not** establish that the external products have been installed, that the full JSON Schema 2020-12 keyword set is validated, that Ed25519 signatures are verified, or that live data has been measured.


## Scope note — additional Intelligence Capabilities source

This file preserves the original four source documents. The subsequently supplied Intelligence Capabilities document is inventoried separately in [TOOLCHAIN_COVERAGE_REGISTER.md](TOOLCHAIN_COVERAGE_REGISTER.md), which is now the current master register covering all ten source inventories.
