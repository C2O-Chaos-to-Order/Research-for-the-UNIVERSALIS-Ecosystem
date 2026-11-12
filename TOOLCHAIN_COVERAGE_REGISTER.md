# Toolchain Coverage Register — UNIVERSALIS

**Date:** 2026-11-12  
**Scope:** Public UNIVERSALIS coverage of twenty-three owner-supplied inventories: the original four; Intelligence Capabilities; Intelligence Skills; Intelligence Powers; Human Powers; Ontologies; Encyclopedias; Security and Cybersecurity; Platform / Construction Infrastructure; Websites; Full-Spectrum Development Suite; Divergence Detection, Attribution and Reconciliation; Insurgence, Resistance and Defensive Threat Modeling; Allegiance, Principal Binding and Revocation; Convergence, Consensus and Dispute Resolution; Ascendence / Recursive Self-Improvement; and Prevention of Harm, Constitutional Enforcement and Sovereign Containment; Simulation; and the Eight-Stratum Capability Ladder.
**Boundary:** This public register does not link to C2O-private owner repositories or disclose private policies, model weights, benchmark datasets, credentials, or authority tokens.

## 1. Original four source documents

The original four public/open source areas remain inventoried in FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md:
1. Human Knowledge.
2. Powers / Energy Efficiency / Synergy.
3. Human Capabilities.
4. Mapping / Matrix / Organization / Ecosystem Mapping.

That register contains the full UNIVERSALIS candidate lists, functional notes, implementation status and CI receipts for the first four inventories. This register consolidates inventories five through twenty-three: Intelligence Capabilities; Intelligence Skills; Intelligence Powers; Human Powers; Ontologies; Encyclopedias; Security and Cybersecurity; Platform / Construction Infrastructure; Websites; Full-Spectrum Development; Divergence; Insurgence; Allegiance; Convergence; Ascendence; Prevention; Simulation; and the Eight-Stratum Capability Ladder.

## 2. Intelligence Capabilities — open candidates

**Reasoning / planning / neuro-symbolic:** SymForge; SPIRAL; Cognitive Kernel-Pro.

**Meta-cognition / self-model:** open-agents-ai; meta_cognitive_self_model_agents; cuda-self-model; elume.

**World models:** wm-mcp; Qwen-AgentWorld.

**Inference-time compute scaling:** Agentic Meta-Reasoning; MOSAIC; TrACE; Evolving Infra.

**Skill acquisition / self-improvement:** SkillOpt; SkillOpt-Sleep; Harness²; hermes-agent-camel; purpose-agent.

**Capability benchmarking / attestation:** Janus Labs; Agent Effectiveness Index (AEI); AgenticBench; Exgentic; NTI Public Compliance Leaderboard / NTI-1.

MOSAIC is named in more than one supplied capability context; verify exact project identity and version before treating those references as one dependency.

## 3. UNIVERSALIS owner repository and basic contract

[UNIVERSALIS Intelligence Capabilities](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Capabilities/tree/implementation/repository-foundation-2026-11-12) contains the public owner implementation.

The versioned schema registry and dependency-free semantic validator define eight contract families:
1. Multi-axis capability profile and benchmark identity.
2. Attestation envelope (ML-DSA-5 / Ed25519 metadata, statement hash, Merkle root, signer, independent verifier, offline bundle).
3. Plan DAG with dependency acyclicity, preconditions, postconditions, tool scopes, verification references.
4. Operational self-model snapshot (calibration, limitations, process health, uncertainty).
5. Handle-based world-model request/response (embed_video, predict, surprise, compare).
6. Compute budget and stopping criteria.
7. Bounded skill/harness self-improvement with strict held-out gate and independent review.
8. Sovereignty-boundary declaration.

The schema registry and validator are the same portable wire contract used by the C2O owner implementation. The public fixture is independently UNIVERSALIS-owned, local-first, and contains no C2O private policy reference.

## 4. Executed CI evidence

| Check | Result |
|---|---|
| Intelligence Capabilities Contract | [Passed — run 43241755277](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Capabilities/actions/runs/43241755277) |
| Repository quality baseline | [Passed — run 43241754989](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Capabilities/actions/runs/43241754989) |

Eight negative cases are exercised: cyclic Plan DAG, compute overspend, raw media instead of handle, no strict held-out improvement, model-weight edit attempt, out-of-range capability score, self-verification, and C2O boundary egress misconfiguration.

## 5. Outstanding work

Full JSON Schema 2020-12 validation; cryptographic ML-DSA-5/Ed25519 and Merkle-proof verification; NTI-1 AST and fail-closed handoff integration; real benchmark execution; Plan DAG dry-run/executor; operational self-model calibration; world-model service/handle registry; adaptive compute controller; SkillOpt/Harness² integration; and independent product/source verification are outstanding.

All feature and performance claims remain source-supplied research claims pending canonical source, license, maintenance, security, compatibility, and independent reproduction. No third-party candidate is being represented as installed or adopted by this contract work.


## Intelligence Capabilities validation record

- UNIVERSALIS execution evidence: [INTELLIGENCE_CAPABILITIES_VALIDATION.md](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Capabilities/blob/implementation/repository-foundation-2026-11-12/INTELLIGENCE_CAPABILITIES_VALIDATION.md).


**CI evidence qualification:** The recorded Intelligence Capabilities CI runs passed the initial eight-case validator revision. The current branch contains ten negative checks, including the C2O-specific Plan DAG tool-scope and human-held permit gates; a new Actions run for that exact strengthened revision has not yet been surfaced. The current source files are present in both implementation branches, but do not attribute the earlier pass to the newer ten-case source revision.


## 6. Sixth source — Intelligence Skills toolchain (public UNIVERSALIS scope)

The sixth source separates the Intelligence Skills concept taxonomy from the artifact and execution supply chain. The canonical taxonomy remains `Intelligence_Skills.md` (I-S-01 through I-S-20); this section covers the tools and portable contracts used to package, discover, sandbox, evaluate, attest, and execute skill artifacts.

### Open UNIVERSALIS candidate inventory

- **Manifest / packaging:** Agent Skills Specification; Agent Plugins 1.0.0.
- **Discovery / release / quality:** MCP Skill Registry; SkillDock.io; OpenSpace.
- **Sandbox / execution:** SkillSandbox; Skillbox; SkillSeal.
- **Safety scanning:** Cisco Skill Scanner; Zenity Labs AI Total; Tencent skill-scan; hybrid static-dynamic-agentic analysis framework.
- **Attestation / competence provenance:** NVIDIA signed skills; formal verification of agent skills; Cupel.

These remain candidates and research patterns, not installed integrations. The source-supplied benchmark figures, tool counts, and feature claims require canonical-source, license, maintenance, security, compatibility, and independent reproduction checks.

### Portable shared contract set

The open implementation defines registry-neutral schemas and synthetic fixtures for:
1. Agent Skills normalized frontmatter profile.
2. Agent Plugins 1.0.0 `plugin.json` and `mcp.json`.
3. Versioned requested-capability declaration and optional `caps` profile extension.
4. Default-deny sandbox policy and execution trace.
5. Static/dynamic/hybrid scanner verdict.
6. Functional-evidence report bound to skill/test digests.
7. Skill Bundle Attestation (SBA).
8. Skill release and dependency descriptor.
9. Optional MCP-tool / REST registry-discovery descriptor.
10. Boundary-evidence record covering data, memory, tools, model routing, egress, consent, and actions.

No central registry is required or imposed. Operators keep their registries, storage, acceptance policies, and runtime decisions independently controlled. A manifest or capability declaration describes a package/request; it does not grant authority. A signature binds a signer to a statement and digests; it does not prove safety or grant execution access.

The base Agent Skills standard does not define `caps`; it is a versioned C2O/UNIVERSALIS extension. `allowed-tools` is experimental and is not a sandbox or authorization mechanism. Agent Plugins package-path containment does not sandbox a running subprocess.

### Owner implementation

- [UNIVERSALIS open Intelligence Skills architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/blob/implementation/repository-foundation-2026-11-12/INTELLIGENCE_SKILLS_TOOLCHAIN_ARCHITECTURE.md).
- [Portable schemas](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/tree/implementation/repository-foundation-2026-11-12/schemas/intelligence-skills).
- [Validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/blob/implementation/repository-foundation-2026-11-12/INTELLIGENCE_SKILLS_VALIDATION.md).

This public implementation contains no C2O-private registry, identity, policy, authority token, permit, signing key, or private execution record.

### Implementation status and outstanding work

Eighteen shared JSON Schema contract records, synthetic fixtures, a sample Agent Plugin package, and semantic tests are implemented in the public owner branch. Lexical package path rejection and resolved-symlink escape checks pass in temporary test packages. The exact tested contract commit has a passing contract workflow and repository quality baseline. No production registry, MCP/REST execution host, runtime sandbox service, live scanner integration, cryptographic SBA verifier, proof replay service, skill quality hub, competence credential issuer, or correction propagation service is deployed.

Cross-domain reuse to reconcile rather than duplicate: SkillSeal and Cupel were also named in Human Capabilities; NVIDIA OpenShell appeared in Intelligence Capabilities. MOSAIC appears in multiple supplied capability contexts and requires identity/version disambiguation before deduplication.

### Current status vocabulary

- **Documented:** candidate and function recorded.
- **Basic contract implemented:** schema, fixture, and semantic code authored on this implementation branch.
- **CI passed:** exact workflow revision and run confirmed for all six source implementations where run IDs are recorded; the Intelligence Skills receipts are linked below.
- **Integrated:** a real adapter/service is connected and exercised; no external candidate is currently marked integrated.


### Exact sixth-source CI receipts

- Intelligence Skills contract workflow: [passed — run 43250292584](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/actions/runs/43250292584)
- Repository quality baseline: [passed — run 43250292526](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Skills/actions/runs/43250292526)

The contract-bearing commits tested were recorded in the owner validation files. Later commits to architecture and status documentation did not alter the schema/fixture/validator/workflow contents.


### Source-reported security evaluation metrics — not guarantees

This public source package records reported scanner/verification metrics as bounded study results, not safety guarantees. In the cited 140-skill study (80 malicious, 60 benign), the default Cisco Skill Scanner configuration reported 0.91 recall with 33 false positives; the optional Qwen3:8B LLM configuration reported 0.85 recall with 40 false positives. The hybrid study reports content-only F1 0.70, dynamic-evidence F1 0.85, and combined static+dynamic F1 0.89; the full pipeline reports 68/80 malicious detections, 0.88 accuracy, 0.93 precision, 0.85 recall, and five false positives among 60 benign samples. These results are specific to the authors' dataset and evaluation protocol and are not a general safety guarantee or an independent UNIVERSALIS reproduction. Source: https://arxiv.org/abs/2611.10830.

The formal-verification source's 53-test count remains an owner-supplied harness claim pending retrieval, version pinning, and local reproduction. SkillDock's TON payment flow is optional registry commerce, not a required UNIVERSALIS protocol.


## 7. Intelligence Powers governance toolchain — public scope

### Open UNIVERSALIS candidate inventory
- **Runtime governance:** OpenShell; ActShield; Sponsio; AgentSentrix; agentpolicy; Aethelgard.
- **Audit / trust / reputation:** AgentOps Replay; auditant; omega-audit; halo-record; IETF Agent Audit Trail draft; SwarmScore; ClankerScore.
- **Sandbox isolation:** Google Agent Substrate / Agent Sandbox; Akamai Agent Sandbox; Edera; gVisor.
- **Governance measurement / authorization interoperability:** AGB proposal; OpenID AuthZEN Authorization API 1.0.
- **Policy languages:** Cedar and OPA/Rego peer backends.

All candidates except specifications/current project statuses independently confirmed in the linked source checks remain proposed pending canonical-source, license, security, version, compatibility and behavior review. SwarmScore is an individual IETF Internet-Draft, not an IETF-approved standard. Reputation is a signal, never authority.

### Portable contracts and owner implementation
The eight public contract record families cover policy bundle metadata; AuthZEN request/response; enforcement receipts with monitor/HITL/quarantine/block/revoke/rate-limit/redact/ask/warn/escalate/redirect outcomes; hash-chain audit record with context-taint evidence; sandbox attestation; six-dimension governance benchmark; reputation evidence; and attenuable grants with parent-scope containment checks. They are operator-neutral and do not impose a central enforcement authority.

[UNIVERSALIS Intelligence Powers architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/INTELLIGENCE_POWERS_GOVERNANCE_ARCHITECTURE.md).

- Contract workflow: [passed — 43254783849](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/actions/runs/43254783849).
- Repository quality baseline: [passed — 43254784031](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/actions/runs/43254784031).

The public workflow validates only public portable schemas and synthetic fixtures. It contains no C2O-private schema, credentials, authority token, policy data or execution records.

### Current limits
No production PDP/PEP, policy broker, sandbox runtime, live audit anchor, reputation network or independent AGB assessor is deployed. The CI record verifies the contract fixtures and tests, not runtime enforcement or vendor performance.

## 8. Human Powers consent, oversight and augmentation — public scope

### Open UNIVERSALIS candidate inventory
- **Human-in-the-loop:** Magentic-UI; hitl-mcp-server; clarify-mcp; mcp-feedback-enhanced; human-in-the-loop-mcp; gotoHuman; ReadyAgents Core; SemaClaw; AG2; Open Computer Agent v2.0.
- **Consent / sovereignty:** agentgov; consent-mcp; consentgraph; levain; @at1c/sdk; @weave_protocol/domere; SovereignOS; CapAuth; Anuma; doxx.net; RAI Manifesto / Digital DNA.
- **Accessibility:** a11y-toolkit; mcp-axe; @webability/mcp; playwright-accessibility-mcp-server; axe-scanner-mcp; Morae.
- **Augmentation:** OpenExo; CEINMS-RT; Human Operator; body-powered supernumerary robotic finger.

### Portable contracts and owner implementation
The public Human Powers schemas cover consent graph/grants; restriction join; provenance; action-specific human approval; WCAG 2.2 accessibility evidence with optional VPAT/compliance-matrix references; sovereignty profile; data-subject-rights requests; augmentation device/action evidence; and consent revocation/correction. Human identifiers are represented by opaque references; there is no central public consent store.

[UNIVERSALIS Human Powers architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Powers/blob/implementation/repository-foundation-2026-11-12/HUMAN_POWERS_CONSENT_AND_AUGMENTATION_ARCHITECTURE.md).

- Contract workflow: [passed — 43254912619](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Powers/actions/runs/43254912619).
- Repository quality baseline: [passed — 43254913053](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Powers/actions/runs/43254913053).

### Conflicts and limits
The earlier Human Capabilities source states 32 a11y-toolkit MCP tools; this Human Powers source states 31. Neither count is accepted until pinned to a precise release and verified. Automated scans are not conformance proof. Consent receipts do not prove informed, voluntary consent. Augmentation schemas require device-specific safety cases, calibration, interlocks, emergency-stop tests and human oversight; they do not validate or control a live device.

No production consent store, identity wallet, cryptographic verifier, accessibility service, DSAR engine, revocation propagation service or physical-device adapter is deployed.

### Public source verification
- AT1C current public repository describes ML-DSA-65 and retirement of Ed25519 in that implementation: https://github.com/at1c-protocol/at1c-protocol-official
- WCAG 2.2: https://www.w3.org/TR/WCAG22/


### Expanded eighth-source evidence contracts

The Human Powers v1 model includes a portable data-subject-rights request record for access, rectification, erasure, restriction, portability, objection, and consent withdrawal. This is a request/evidence contract only, not a legal compliance service. The Intelligence Powers contract also tests parent-to-child capability containment and additional review/escalation outcomes. The latest public contract and quality workflows for both domains passed all steps.


## 9. Ninth source — Ontologies — public UNIVERSALIS scope

### Open candidate inventory
- **Engine / reasoning:** open-ontologies (fabio-rovai); Ontosphere; graph-mcp-driver.
- **Agent-writable ontology:** MNEME / FlowX.AI Ontology Layer.
- **Ontology-to-tools compilation:** Ontology-to-Tools Compilation / The World Avatar.
- **Schema governance / knowledge graph:** Entigram; OpenBKN.
- **Deterministic validation / reasoning:** Semantica; ontobricks; cassis-cli.
- **Bitemporal store:** Quipu.
- **Standards:** RDF 1.1; OWL 2 Direct Semantics; SHACL; PROV-O; SKOS.

These remain open candidates and standards/reference patterns, not adopted integrations. The source review queue and version-specific caveats are recorded in the owner architecture.

### Portable shared contract foundation
Fourteen portable JSON Schema record families cover ontology artifact metadata; SKOS alignment mapping; PROV-O event; SHACL validation report; reasoning certificate and trusted-computing-base metadata; bitemporal fact; valid-time/transaction-time as-of query; crosswalk-resolution receipt; agent-write provenance/confidence; non-widening named-graph authority; conflict record; versioned schema-evolution proposal; ontology-to-tool compilation; and closed-world action-admission receipt.

Two RDF/Turtle examples are parsed by CI: SKOS mapping with PROV-O provenance, and a SHACL validation report. No central ontology registry is required or introduced.

### Owner implementation and CI
- [UNIVERSALIS open ontology toolchain architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/blob/implementation/repository-foundation-2026-11-12/ONTOLOGY_TOOLCHAIN_ARCHITECTURE.md).
- [Portable ontology schemas](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/tree/implementation/repository-foundation-2026-11-12/schemas/ontology).
- [RDF examples](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/tree/implementation/repository-foundation-2026-11-12/examples/ontology).
- [Validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/blob/implementation/repository-foundation-2026-11-12/ONTOLOGY_TOOLCHAIN_VALIDATION.md).
- Contract workflow: [passed — 43258538853](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/actions/runs/43258538853).
- Repository quality baseline: [passed — 43258538884](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ontology/actions/runs/43258538884).

The public implementation includes only portable schemas, synthetic fixtures, RDF examples and open architecture documentation. It contains no C2O-private admission schema, ontology, named-graph grant, policy, identity mapping, signing key or operational trace.

### Source verification and discrepancies
- OWL 2 Direct Semantics, PROV-O and SKOS are W3C Recommendations. SHACL 1.0 is the stable target; SHACL 1.2 Core is a Working Draft as of October 2026.
- Only `skos:exactMatch` is transitive among SKOS mapping properties.
- open-ontologies' current README describes optional feature-gated tools, with eight omitted from the default published binary; exact tool inventory depends on the selected build.
- Lean certificates check a derivation conditional on the asserted graph and supplied steps. The Rust engine's production of those graph/step artifacts remains part of the trusted computing base.
- Quipu's docs.rs page describes an immutable bitemporal EAVT fact log backed by SQLite; the supplied 28-tool MCP count remains unverified.
- MNEME's current FlowX.AI page says nine nodes, while the supplied proposal says twelve. Ontosphere's 43-tool count and the feature claims for graph-mcp-driver, Entigram, OpenBKN, Semantica, ontobricks and cassis-cli remain unverified.

### Implementation limits
CI checks JSON contracts, semantic invariants and Turtle syntax only. It does not execute OWL reasoning, SHACL validation over ontology data, Lean proof checking, graph-store operations, bitemporal queries, cryptographic verification, or schema deployment. No external product is marked integrated. The canonical UNIVERSALIS master ontology text remains unchanged.


### Final tightened ontology gate evidence — 2026-11-12

The final tested ontology validator enforces the reviewer/evidence requirements for accepted crosswalks and applied schema changes, the resolution evidence requirement for resolved conflicts, blank-node fact reference requirements, and non-empty evidence on every admission receipt. The final ontology contract workflows and repository quality baselines linked above passed all jobs and steps. C2O additionally passed the private admission validator; the public run contains only shared portable contracts and synthetic RDF fixtures.


## 10. Encyclopedias — open UNIVERSALIS coverage

### Open candidate inventory
- **Compiled wiki / local knowledge:** Alexandria; WikiNow; MeMex (Zero-RAG); Stoa.
- **Ingestion / document processing:** Flexible GraphRAG; docsiq; llm-wiki-compiler.
- **Citation integrity / research validation:** CiteGuard; retractionwatch-mcp; Panda Research Tools.
- **Verifiable memory / evidence:** verifiable-memory; DocImprint; answerproof; ember-custody.
- **Encyclopedia aggregation:** mcai-knowledge; cite-citadel; llm-wiki-plugin.
- **Standards / exchange:** OKF 0.2, JSON-LD 1.1, RFC 9162 Merkle inclusion proofs, SHA-256 and SHA3-256 content digests.

These are owner-supplied candidates/reference patterns, not installed integrations. Tool counts and supported formats must be pinned to an exact canonical release and configuration.

### Portable contract foundation
Eleven top-level positive record types cover source metadata/rights, content-addressed ingestion manifests/chunks, citation anchors/proof receipts, citation quality/coverage, individual editorial-status records, batch citation-integrity sweeps, knowledge assets, OKF/JSON-LD export manifests, content-addressed evidence bundles, correction events, and answer-evidence receipts. The nested proof record follows RFC 9162 SHA-256 domain separation. Source/chunk digests may be SHA-256 or SHA3-256, but SHA3 content digests are committed inside the RFC 9162 SHA-256 Merkle leaf and do not change the Merkle algorithm.

### Owner implementation and CI
- [Open UNIVERSALIS encyclopedia architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/blob/implementation/repository-foundation-2026-11-12/ENCYCLOPEDIA_TOOLCHAIN_ARCHITECTURE.md).
- [Portable encyclopedia schemas](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/tree/implementation/repository-foundation-2026-11-12/schemas/encyclopedia).
- [Synthetic fixtures](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/tree/implementation/repository-foundation-2026-11-12/examples/encyclopedias).
- [Validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/blob/implementation/repository-foundation-2026-11-12/ENCYCLOPEDIA_TOOLCHAIN_VALIDATION.md).
- Contract workflow: [passed — 43264360375](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/actions/runs/43264360375).
- Repository quality baseline: [passed — 43264360278](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/actions/runs/43264360278).

The public shared schema, fixture and validator blobs are byte-identical to the C2O shared counterparts. The public branch contains no C2O-only private schema, private corpus, policy, authority data or private signing key.

### Source caveats
- llm-wiki-compiler v0.11.0 changelog (2026-06-16) lists 11 MCP tools; use release-specific counts.
- CiteGuard currently identifies as early-development/MVP.
- Flexible GraphRAG support counts vary by backend/version/configuration.
- MeMex's “zero hallucination” label does not mean all source or claim truth is mathematically guaranteed.
- DocImprint's optional chain anchoring publishes hashes; it does not notarize legal truth.
- TrustChain-RAG is a research paper/framework, not an installable runtime verified by this repository.
- QuanCog is a commercial/vendor platform candidate, not integrated.
- Product-specific counts and behavior for Alexandria, WikiNow, docsiq, Panda Research Tools, verifiable-memory, answerproof, ember-custody, mcai-knowledge, cite-citadel and llm-wiki-plugin remain unverified until exact releases and licenses are pinned.

### Implementation limits
CI checks JSON Schema records, semantic invariants and the synthetic RFC 9162 proof only. It does not deploy a wiki compiler, live ingest engine, source-rights system, OCR pipeline, graph store, citation database connector, signature/key service or correction propagation. Merkle inclusion is not claim truth, source authenticity or corpus completeness. No third-party candidate is claimed integrated; public examples contain synthetic data only.


### Portable signature-envelope extension

The shared schema has optional signature-envelope metadata for ingestion manifests, citation-proof receipts, OKF/JSON-LD export manifests, evidence bundles, correction events and answer receipts. Fields include algorithm, key fingerprint, optional public-key reference, signed-payload digest, signature bytes, signing timestamp and verifier status. No private key material crosses the seam. This is a metadata contract only; CI does not generate or verify signatures, resolve key trust, or check revocation.


## 11. Security and Cybersecurity — public UNIVERSALIS coverage

### Open candidate inventory

**Runtime security / agent firewalls:** AgentWall ([agent-wall/agent-wall](https://github.com/agent-wall/agent-wall)); HOL Guard ([hashgraph-online/hol-guard](https://github.com/hashgraph-online/hol-guard)); AgentSentrix; ShieldPilot; AgentShield (identity ambiguous; the located [affaan-m/agentshield](https://github.com/affaan-m/agentshield) is a configuration/MCP scanner, not the described runtime interceptor).

**Zero-trust / kernel boundary:** ZTAgent ([ztagent-ai/ztagent](https://github.com/ztagent-ai/ztagent)); OS-Cicada / Sentry_Gateway; Kest Core; NVIDIA OpenShell ([NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)); MCPGuard-Dynamic ([meta/mcpguard-dynamic](https://github.com/meta/mcpguard-dynamic)); k8e.

**Prompt injection / behavior:** SNAFT; APEX; Phalanx AI; AgentSecCore; Axora AgentGuard ([product documentation](https://axorasecurity.com/docs/products/axora-agentguard)).

**Authorized defensive assessment:** modelWrecker; ARTEX (independent forks only; see [CERT-EU warning, 2026-11-05](https://cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex)); PentAGI ([vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)); CyberAI; CyberStrike. These are controlled assessment candidates, not unattended tools or authorized targets.

**Supply chain / endpoint:** agentic-security ([Clear-Capabilities/agentic-security](https://github.com/Clear-Capabilities/agentic-security)); Hawkeye Agent; Chainloop ([chainloop-dev/chainloop](https://github.com/chainloop-dev/chainloop)); Vectra Guard.

All remain candidates/reference patterns until canonical source, license, exact release, platform requirements, data flows, security posture and behavior are reviewed.

### Shared portable contracts

The shared contract family provides:
1. Versioned OWASP/MITRE taxonomy and control-framework mapping.
2. RFC 9162 SHA-256 Merkle proof of a sanitized security-evidence payload.
3. Enforcement decision receipts with policy digest and action outcome.
4. Containment attestations distinguishing application, gateway, endpoint, kernel and hardware enforcement.
5. Scope-bound assessment metadata and sanitized finding records.
6. SBOM and vulnerability/license review attestations.
7. Build provenance metadata for in-toto/SLSA/Chainloop.
8. Sandbox/kernel/eBPF policy-digest evidence.
9. SHA-256 tamper-evident audit-chain records.
10. Technical-control evidence maps that explicitly are not certifications.
11. Optional detached signature envelope metadata (public key reference/fingerprint, signed digest, signature bytes and verifier status; no private key).

### Owner implementation and final CI

- [UNIVERSALIS security architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/SECURITY_CYBERSECURITY_ARCHITECTURE.md).
- [Portable security contracts](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/schemas/security/security-evidence-contracts.v1.schema.json).
- [Synthetic public fixtures](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/examples/security/security-evidence-fixtures.v1.json).
- [Validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/SECURITY_CYBERSECURITY_VALIDATION.md).
- Security contracts: [passed — 43268851042](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43268851042); repository quality: [passed — 43268850866](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43268850866); Engineering Doctor: [passed — 43268850907](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43268850907); repository verification: [passed — 43268850893](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43268850893).

The public schema, synthetic fixture and validator blobs are byte-identical to the shared C2O counterparts. No C2O-only private authorization schema, private policy, credential, incident, asset inventory or target list is present in this repository.

### Source and taxonomy cautions

- OWASP LLM Top 10 2025 and OWASP Agentic Top 10 2026 are separate versioned taxonomies. The [OWASP MCP Top 10 roadmap](https://owasp.github.io/www-project-mcp-top-10/) still reports beta/pilot status at this review date.
- [MITRE ATLAS](https://atlas.mitre.org/) is a living AI threat knowledge base. Mapping relationships require rationale and exact framework edition/version.
- [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) is a Generative AI risk-management profile, not a threat taxonomy or certification.
- ZTAgent's README says development defaults disable authentication and allow an OPA bypass; its production configuration check rejects those defaults.
- HOL Guard says coverage depends on host-exposed events and per-integration support; do not infer full kernel-level protection from a hook.
- Chainloop documents signed in-toto attestations and self-hosted evidence storage, but real key custody and storage configuration must be independently reviewed.
- agentic-security explicitly says its framework does not certify compliance and that it does not publish SARD benchmark scores.
- ARTEX: CERT-EU reported threat-actor misuse, lack of hard scope enforcement in the described upstream and removal of the original repository in October 2026. Independent forks are not trusted upstream releases.
- The supplied performance and marketing claims for AgentWall, AgentSentrix, ShieldPilot, AgentShield, OS-Cicada, SNAFT, APEX, Phalanx AI, AgentSecCore, Hawkeye Agent and Vectra Guard remain unverified until canonical source/release and reproducible tests are pinned.

### Implementation limits

CI validates JSON schemas, semantic invariants and a synthetic RFC 9162 proof plus a SHA-256 audit-chain record. Ten negative tests check tampered proof, deny/execute contradictions, containment independence, scope gates, false certification, chain integrity, unsafe reproduction, invented scan results and sandbox pass without testing. No scanner, gateway, BPF program, sandbox, DPU, SBOM generator, red-team tool or signature service is installed or invoked. Public fixtures contain synthetic references only; they contain no C2O-private data.


## 12. Twelfth source — Platform and Construction Infrastructure (public UNIVERSALIS scope)

This owner-supplied inventory closes seven infrastructure gaps beneath and around the prior intelligence, knowledge and security domains: OS/substrate; application development; build/DevOps (workflow construction, blueprints and CI/CD); observability/control; networking/gateways; storage/memory; and evaluation/testing.

### Open and independently inspectable candidates

**OS / substrate**
- **khy-os** — hand-written C OS-kernel candidate combined with an agentic CLI and multi-provider AI gateway; [PyPI project](https://pypi.org/project/khy-os/). Verify source repository, release contents, boot reproducibility, architecture, license and kernel security.
- **Agent-OS-Kernel** — conceptual OS scheduling/context/memory/process pattern for agent infrastructure; exact source and executable implementation remain unpinned.
- **airisos** — candidate agent-company control plane with lifecycle, RBAC, budgets and plugin patterns; canonical upstream remains unresolved.
- **MaragingLoop** — [GistNoesis/MaragingLoop](https://github.com/GistNoesis/MaragingLoop), autonomous bare-metal OS/kernel construction loop using compilation and VM interaction. This is a development tool, not an OS runtime.

**Application development**
- **Vercel AI SDK 6** — TypeScript app/agent toolkit; [release announcement](https://vercel.com/blog/ai-sdk-6) and [official documentation](https://vercel.com/ai-sdk).
- **Google ADK** — open agent development kit; [official documentation](https://google.github.io/adk-docs/). Pin language-specific support and package release.
- **agentic-ai-sdk** — owner-described Microsoft Agent Framework-based SDK; exact repository/package and license require confirmation.
- **a2abase** — owner-described Python agent SDK; exact upstream, tool/integration counts and provider coverage require confirmation.

**Workflow construction and build orchestration**
- **UnifAI** — [redhat-community-ai-tools/UnifAI](https://github.com/redhat-community-ai-tools/UnifAI), open graph/blueprint orchestration candidate with LangGraph/Temporal patterns and MCP/A2A support.
- **Primeagent** — visual and code-first workflow builder candidate; exact project identity remains unresolved.
- **AAMAD** — context-engineering/multi-agent construction candidate; exact upstream remains unresolved.
- **Microsoft Agent Framework** — [microsoft/agent-framework](https://github.com/microsoft/agent-framework), open agent SDK/runtime candidate.

**DevOps and CI/CD**
- **Harness MCP server** — [harness/mcp-server](https://github.com/harness/mcp-server), official Harness MCP integration. Tool allowlisting and scoped credentials are required.
- **Semaphore MCP server** — pipeline interface candidate; official source and operation permissions remain to be pinned.
- **DuploCloud** — vendor DevSecOps/infrastructure automation candidate; not classified as an open self-hosted substrate without a specific component.
- **AWS DevOps Agent** — vendor-operated investigation/automation service candidate; [MCP integration documentation](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-connecting-mcp-servers.html). Not an open self-hosted runtime.

**Observability and lifecycle control**
- **Riva** — [riva-labs-ai/riva](https://github.com/riva-labs-ai/riva), local-first agent discovery, lifecycle, resource and event/OTLP observability. Its project description distinguishes observation from agent execution.
- **AgentOps Replay** and **lumen-ai** — replay, causal-trace, failure and spend-observability candidates; exact upstream identities and replay fidelity remain unresolved.

**Networking and agent gateways**
- **agentgateway** — open AI-native gateway candidate; [project overview](https://www.solo.io/products/agentgateway) and [documentation](https://docs.solo.io/agentgateway/standalone/latest/documentation/about/introduction/). Performance figures remain source-reported until reproduced.
- **IBM ContextForge** — [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge), open registry/proxy candidate federating MCP, A2A and REST/gRPC APIs with governance, discovery and observability.

**Storage and memory**
- **zleap-sag** — composable relational/vector storage candidate. Pin exact package, repository and license. Do not conflate with [Zleap-AI/SAG](https://github.com/Zleap-AI/SAG) without source evidence.
- **memg-core** — Qdrant/Kuzu vector-and-graph storage candidate; exact upstream remains unresolved.
- **Azure Cosmos DB** — vector/search/cache/checkpoint-capable managed service candidate; it is vendor-operated, not open-source or self-hosted. [Official vector search documentation](https://learn.microsoft.com/azure/cosmos-db/vector-search).

**Evaluation and testing**
- **Strands Evals** — [strands-agents/evals](https://github.com/strands-agents/evals), agent/application output, trajectory, tool-use and interaction evaluation candidate.
- **Inspect** — [UK AI Security Institute documentation](https://inspect.aisi.org.uk/), open evaluation framework and sandbox integrations.
- **MCPEval** — MCP-specific generation and verification candidate; canonical repository/release remains to be pinned.

### Portable platform contracts implemented

The shared v1 schema defines nine record types: OS/container artifact; runtime profile; Agent Skills manifest reference; workflow blueprint graph; CI/CD event; redacted telemetry observation; network route; storage interface; and evaluation receipt. Records use opaque references and digests, not C2O-private or other private credentials, raw telemetry, policy bodies, secrets or datasets.

The public fixture contains nine synthetic records. The semantic validator checks bootable/container distinction, graph node/edge integrity and acyclicity, approval references, CI/evaluation result arithmetic, telemetry redaction, allow-route authentication/authorization/egress scope, deny-before-execution, and encryption requirements for confidential/secret storage. Ten negative cases are defined.

### Source and deployment classification

The catalog distinguishes open-source/self-hostable candidates from managed vendor services. Azure Cosmos DB, AWS DevOps Agent and DuploCloud are external managed/vendor service options, not UNIVERSALIS-owned open infrastructure. Harness and Semaphore integrations require scoped accounts and credentials. Agent-OS-Kernel, airisos, agentic-ai-sdk, a2abase, Primeagent, AAMAD, Semaphore MCP, AgentOps Replay, lumen-ai, memg-core and MCPEval remain unresolved until canonical sources and licenses are pinned.

OCI describes container artifacts, not bootable OS interoperability. MCP tool interaction and A2A agent interaction are distinct protocols. Agent Skills manifests do not grant execution authority. Generic YAML blueprints require explicit runtime adapters and semantic equivalence tests. OpenTelemetry-compatible records must be redacted before export.

### Twelfth-source CI receipts

**Executed CI receipts (2026-11-12):** UNIVERSALIS platform contracts [passed — run 43274259485](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43274259485); ecosystem quality [passed — run 43274259563](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43274259563); architecture graph [passed — run 43274259574](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43274259574); repository verification [passed — run 43274259581](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43274259581). Research register quality [passed — run 43274160450](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/actions/runs/43274160450) and repository verification [passed — run 43274160424](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/actions/runs/43274160424).

### Implementation status and limits

The public architecture, shared schema, synthetic fixture, semantic validator, validation record and CI workflow are present on this owner implementation branch. No OS/kernel was built or booted, no SDK/runtime/workflow/gateway/CI service was installed, no storage backend was provisioned, and no external evaluation benchmark was run. The schema and ten negative tests validate the proposed interchange representation only; they do not establish production compatibility, performance, safety, compliance or deployment.


## 13. Thirteenth source — Websites, Site Construction and Agent-Ready Publishing (public UNIVERSALIS scope)

This owner-supplied inventory adds structured website construction, agent-facing interfaces, CMS/content workflows, static generation, web frameworks, website auditing/accessibility and interoperable publishing evidence. The public register contains only public candidate identities and sanitized contracts; C2O-private systems and site operations remain outside this repository.

### Open / public candidate inventory

**Agentic site builders and visual editors**
- **EmDash / EmDash Build** — Cloudflare's EmDash 1.0 is an Astro-based open-source CMS; EmDash Build is a separate open-source alpha AI site builder using EmDash MCP, per-project Cloudflare Sandbox and Workers for Platforms publishing. It is not automatically vendor-independent. Sources: [Cloudflare EmDash article](https://blog.cloudflare.com/emdash-cms-plugin-registry), [Cloudflare Workers docs](https://developers.cloudflare.com/workers/framework-guides/web-apps/emdash/).
- **Weave** — owner-supplied human-agent collaborative editor concept with structured project state, revision-pinned ChangeSets, stale-revision refusal and a human publishing gate; exact upstream and release unresolved.
- **OpenPage** — [buildingopen/openpage](https://github.com/buildingopen/openpage), MIT-licensed JSON-first visual/AI site builder with typed SiteConfig blocks/theme and standalone HTML export. Its schema is a reference model, not a universal interchange standard.
- **OSW Studio** — [o-stahl/osw-studio](https://github.com/o-stahl/osw-studio), BYOK browser agent builder with IndexedDB-backed virtual filesystem. Browser persistence is not equivalent to an OS-level sandbox.
- **SeldonFrame** — [seldonframe/seldonframe](https://github.com/seldonframe/seldonframe), open-source/self-hostable agent-native front-office workspace spanning websites, booking, intake, CRM and agents.

**Headless CMS and content**
- **Strapi MCP** — built-in MCP server introduced in v5.47.0 and GA in v5.49.0. Admin-token permissions gate content operations including publish. Source: [Strapi MCP GA announcement](https://strapi.io/blog/the-strapi-mcp-server-is-now-ga).
- **agent-cms** — [jokull/agent-cms](https://github.com/jokull/agent-cms), Cloudflare Workers/D1/R2 CMS with GraphQL, FTS5/Vectorize and admin/editor MCP surfaces. Critical README default: writes are open when `CMS_WRITE_KEY` is unset; require a write secret or independently verified auth gateway before exposing write/publish routes.
- **AgentCMS** — separate owner-supplied Astro/Cloudflare agent-authored CMS candidate; exact upstream unresolved. Do not conflate with agent-cms.
- **Webiny** — open-source/self-hostable serverless CMS candidate; exact MCP integration and release require verification.
- **Sveltia CMS** — [sveltia/sveltia-cms](https://github.com/sveltia/sveltia-cms), MIT Git-backed CMS with GitHub, GitLab and Gitea/Forgejo backends and documented AI/Agent Skill support.

**Static site generators and publishing**
- **seite** — Rust single-binary SSG; docs describe HTML, Markdown, `llms.txt` / `llms-full.txt` and agent-oriented audit CLI. [Documentation](https://seite.sh/docs/getting-started).
- **vagejs** — JSON-command SSG with read-only MCP tools for site information, checks, pages and links; publication remains owner-operated. [FAQ](https://vagejs.com/faq/).
- **staticforge** — owner-supplied CLI/MCP/JSON-schema SSG candidate; source/license unresolved.
- **ShipStatic** — [shipstatic/mcp](https://github.com/shipstatic/mcp), MIT hosted/local MCP publishing tool. Hosted unauthenticated deployments are temporary unless claimed (current documentation says three days). Use for public prototypes, not private production sites.

**Agent-aware web frameworks**
- **Mastra** — open TypeScript framework with MCP client/server, workflow and human-in-the-loop pre-execution approval. Sources: [MCP documentation](https://mastra.ai/docs/connections/mcp), [HITL documentation](https://mastra.ai/docs/agents/human-in-the-loop).
- **Cortex** — supplied AI-first Next.js framework identity is ambiguous; located Cortex project is a documentation/SDK/MCP generator, not proof of the described framework.
- **Bao** and **AgenticAPI** — owner-supplied agent-native framework candidates; exact upstream, license, runtime and safety model unresolved.

**Website audit, security and accessibility**
- **squirrelscan** — [squirrelscan/squirrelscan](https://github.com/squirrelscan/squirrelscan), MIT local CLI/audit engine/rules, described as 300+ rules with CLI/MCP/agent/CI workflows. Hosted API/dashboard/cloud worker/hosted MCP and some cloud features are separate private services. Telemetry is enabled by default but can be disabled; offline mode exists. [FAQ](https://docs.squirrelscan.com/faq).
- **AcuityScan** — website scanner with REST and native MCP interfaces; public materials advertise 350+ checks, with hosted-service dependency to be considered. [About](https://www.acuityscan.com/about).
- **SyteCheck** — ten-category web audit service; public materials describe axe-core and WCAG 2.2 AA checks. Independently reproduce coverage. [Features](https://sytecheck.app/features).
- **SiteProof** — owner-supplied agent-readiness/security/AEO scanner; canonical provider/source/license remain unresolved.
- **Burp Suite DAST MCP** — PortSwigger DAST MCP interface for authorized scan/issue operations. Current documentation says it runs inside the DAST web server and is unavailable on self-hosted CI-only deployments without the dashboard. It is a licensed service integration, not a generic self-hosted scanner. [Official docs](https://portswigger.net/burp/documentation/dast/user-guide/using-ai/mcp-server).

### Shared website interoperability contract implemented

The public shared v1 schema defines six sanitized record types:
1. Site definition (site/revision/digests, routes, block references, theme, render targets and discovery signals).
2. Agent capability manifest (MCP/WebMCP/API/Agent Skills surfaces, declared operations/scopes, authentication and approval requirements).
3. Revision-pinned site ChangeSet (base/current digests, typed changes, stale state and approval).
4. Scoped site permission profile (principal/role, opaque token reference, allowed/denied operations, path scope and expiry).
5. Website audit receipt (scanner/ruleset/scope, revision and content digests, findings, severity totals, score/time/evidence and optional signature metadata).
6. Site publish receipt (preview/publish/deploy/DNS/unpublish/rollback event, target/artifact digest, operator/approval/result/time/audit references and optional signature metadata).

Fixtures use synthetic reserved references only. The contract excludes private credentials, CMS token values, deployment secrets, policy bodies, private site content, authority tokens and raw operational audit data.

### WebMCP and discovery cautions

The Web Machine Learning Community Group's 2026-11-11 WebMCP document is a Draft Community Group Report, not a W3C Standard or a W3C-track standard; Chrome documentation describes early preview. The portable ChangeSet semantics therefore record maturity and require structured state, revision pinning, stale-proposal rejection and human publish gates explicitly. These are UNIVERSALIS contract requirements, not claims that the draft API provides them. Sources: [WebMCP draft report](https://webmachinelearning.github.io/webmcp/), [Chrome WebMCP docs](https://developer.chrome.com/docs/ai/webmcp).

`robots.txt`, `llms.txt`, `llms-full.txt`, `ai.txt`, `AGENTS.md`, Markdown alternates and JSON-LD are discovery/description signals, not access control, consent, licensing or execution authority. MCP and Agent Skills likewise do not grant site permissions. A CMS scoped token is a technical credential, not a human/owner permit.

### C2O boundary

The C2O sovereign website architecture, private site inventory, authority/publishing policy, deployment secrets, private content, signing keys and site audit reports remain in the private owner environment. This public register carries only public candidate references and shared sanitized contract formats; it does not link to C2O-private website implementation artifacts.

### Implementation status and limits

The shared schema, six synthetic records, semantic validator, eleven negative cases and public CI workflow are present on the UNIVERSALIS owner implementation branch. No live site was crawled/published, no CMS/builder/auditor installed, no WebMCP browser integration enabled and no production signing service used. No accessibility/security certification is asserted. Exact sources for Weave, AgentCMS, Webiny MCP specifics, staticforge, supplied Cortex, Bao, AgenticAPI and SiteProof remain unresolved. All numerical security/audit claims remain vendor/source claims pending independent reproduction.


### Thirteenth-source CI evidence (2026-11-12)

- UNIVERSALIS website contracts: [passed — run 43276106806](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43276106806).
- UNIVERSALIS ecosystem repository quality: [passed — run 43276106790](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43276106790).
- UNIVERSALIS ecosystem repository verification: [passed — run 43276107032](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/actions/runs/43276107032).
- UNIVERSALIS research register quality: [passed — run 43276012556](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/actions/runs/43276012556).
- UNIVERSALIS research register verification: [passed — run 43276123720](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/actions/runs/43276123720).

These CI runs validate contracts, synthetic fixtures and repository artifacts only. They do not establish a live website scan, CMS integration, production publication or deployment.


## 14. Fourteenth source — Full-Spectrum Development Suite (public UNIVERSALIS scope)

**Date:** 2026-11-12  
**Domains:** game development; music/audio; 3D graphics/modeling/CAD; video; VR/AR; IDE/version control; build/CI/CD; project management; documentation.

### Open / public candidate inventory

- **Game development:** NodeTool; Summer Engine; Blazium Engine; o3de-mcp; GladeKit MCP; Limina; Omniweft; OpenEngine; MORX GMS2 MCP; unikit-ai; GameForge MCP.
- **Music/audio:** ReaperMCP; FL Studio MCP Server; ATRI_AGENT; Audio Plugin Coder; ConjureDSP; SongForge-MCP; songgeneration-mcp; Soundbox; ai-music-mcp; yovoice.
- **3D/CAD:** Blender MCP Bridge; VibeInc AI Art Team; Vibe CAD; ai-cad; cadx; Presidium Shape Studio; 3D Gen Studio.
- **Video:** Kinocut; Framewright; OpenEdit.
- **VR/AR:** Immersive Web SDK (IWSDK); XR Blocks; Three-Live; HERA; scenekit-xr.
- **IDE/VCS/core engineering:** Eclipse Theia; Qt Creator 20; ThinkRail; Cline; joLink Runtime; Libra; AVCS; GitAgent; LogNexus MCP; TeamAI; RepoKeeper.
- **Build/CI/CD:** eforge; RepoLaunch; Genesis; agent-project-builder; Eclipse Atesor; shipmill; Hive; CiLydian; CIDRA; KiCI.
- **Project management/documentation:** Agentic Project Management (APM); open-workmcp; Paca; OpenMac; CodiLay; Fidus; CodeWiki 2.0; OpenWiki; docsector-reader; devdocs-forge-agent.

### Source verification corrections and unresolved claims

- o3de-mcp's current README describes 96 tools/seven categories, not 67/five; GladeKit's current README describes Unity 275 and Godot 115, not 235/53.
- FL Studio MCP's current README describes 164 tools, not 29.
- Blender MCP Bridge counts are internally inconsistent (93/98/106); Soundbox's README conflicts between 21 and 24 tool counts.
- Summer Engine separates local engine operation from hosted cloud MCP services; only the former is a local runtime surface.
- Limina describes permissioned skills and a hash-chained JSONL world log; replay compatibility needs independent testing.
- Audio Plugin Coder's JUCE 9 workflow does not make every plugin format universally enabled; model/asset rights remain separate.
- OpenEdit's VEED renderer is a separate closed-source component and optional transcription can involve upload. Kinocut Video Receipts do not alone establish cryptographic signatures or publication approval.
- XR Blocks and Three-Live are explicitly not presented as officially supported Google products; Gemini integration can involve provider-side data flow.
- RepoLaunch's 78% number is a paper-specific benchmark. Eclipse Atesor is in incubation and current RISC-V build documentation uses QEMU/binfmt emulation; native hardware is future/in progress.
- KiCI documents an operator-controlled runner/orchestrator while retaining a hosted relay/dashboard, so it is hybrid rather than air-gapped.
- Exact source, license, current release or capability verification is unresolved for several owner-supplied names, including Omniweft, OpenEngine, MORX GMS2 MCP, unikit-ai, GameForge MCP, ReaperMCP, ATRI_AGENT, ConjureDSP, songgeneration-mcp, ai-music-mcp, CAD/3D candidates, Framewright, HERA, scenekit-xr, Libra, AVCS, GitAgent, LogNexus MCP, Genesis, agent-project-builder, shipmill, Hive, CiLydian, CIDRA, open-workmcp, Paca, OpenMac, CodeWiki 2.0, OpenWiki, docsector-reader, and devdocs-forge-agent. These remain proposed candidates.

### Shared public contract files implemented

- DEVELOPMENT_SUITE_ARCHITECTURE.md
- DEVELOPMENT_SUITE_VALIDATION.md
- schemas/development-suite/development-suite-contracts.v1.schema.json
- examples/development-suite/development-suite-fixtures.v1.json
- .github/scripts/development_suite_contract.py
- .github/workflows/development-suite-contract.yml

The schema defines project-format contracts, agent-capability manifests, and signed in-toto/SLSA provenance receipts. Fixtures include nine domain examples, three capability manifests (local and hybrid cases), and one DSSE/Ed25519 signed receipt. Ten negative tests cover schema and semantic failure cases, including capability approval and provenance-signature tampering. The public fixture key is disposable and is not a production trust root.

The public register contains only public candidate identities, synthetic fixture records and public format/specification references. It contains no C2O-only authorization schemas, permits, credentials, keys, policy rules, operational data or private repository references.

### Limitations

No third-party candidate is installed or adopted by inclusion in this inventory. No real project or artifact was built, signed, published or deployed. The CI suite validates synthetic contracts and a disposable test signature only; it does not establish product safety, local-only behavior, license compatibility, real-world interoperability, reproducible builds or XR/device conformance. Exact upstream, release, licensing, network-ejection and dependency review remains required before adoption.


## 15. Fifteenth source — Divergence Detection, Attribution and Reconciliation (public UNIVERSALIS scope)

**Date:** 2026-11-12  
**Domains:** behavioral/trajectory; configuration/infrastructure; schema/data; policy; semantic/ontological; identity/federation; embedding/RAG; resolution/reconciliation.

### Open / public candidate inventory

- **Behavioral/trajectory:** TraceFork; Praxen; AlignmentCheck (LlamaFirewall); driftbase; SEISMOGRAPH; agentdrift; Shadow; Hodoscope; Arbiter; Agent Behavioral Contracts (ABC); AEBA.
- **Configuration/infrastructure:** terraship; DriftSentry; tfdrift; cloudrift; stackdrift; driftmgr.
- **Schema/data:** Flyway Community Drift Check; sqldrift; saropa_drift_advisor; gcfm.
- **Policy:** Risk Cognizance; PolicyIQ; Semantic Consensus Framework (SCF).
- **Semantic/ontological:** OntoLDiff; owlcompare; open-ontologies alignment; Ontology Development Tracker (OnDeT).
- **Identity/federation:** sm-divergence; federated-learning disagreement resolution.
- **Embedding/RAG:** ragdrift; embspec; embspec-mcp.
- **Resolution/reconciliation:** Graph Merge; ConcordAI; Automated Codebase Reconciliation.

### Source verification corrections and unresolved claims

- TraceFork's 45.5 ms median and 0.910 F1 are paper results on a specific EMNLP 2026 evaluation set, not general performance guarantees.
- Praxen is read-only Worker Remit verification, not a full runtime enforcement plane.
- AlignmentCheck is a probabilistic few-shot/semantic LlamaFirewall guardrail, not deterministic proof.
- driftbase currently advertises EU AI Act Articles 9 and 12, not Article 72. Its own score reference says the 0–1 score measures behavioral difference, not quality. Confirm egress by selected deployment mode.
- SEISMOGRAPH's 38-day lead is a seeded synthetic backtest. Its current public network has one observer and requires quorum three.
- AEBA and the sm-divergence-related registry corroboration document are individual Internet-Drafts, not adopted RFCs. AEBA weights are implementation-defined.
- The exact upstream/version/license/deployment remains unresolved for DriftSentry, Shadow, agentdrift, sqldrift, gcfm, SCF, OntoLDiff, OnDeT, federated-learning disagreement resolution, ConcordAI and Automated Codebase Reconciliation.
- tfdrift has similarly named projects. cloudrift is AWS-focused in its current README; stackdrift is CloudFormation-specific; verify driftmgr provider support in an isolated account.
- Flyway distinguishes migration-history validation and live schema drift. saropa_drift_advisor is a debug-focused Dart/Flutter SQLite/Drift inspector, not a general data-drift service.
- PolicyIQ's 91.6% precision is a target reported on a controlled synthetic corpus, not independently validated production accuracy. Risk Cognizance product support claims are not certification.
- owlcompare v0.1.0 currently supports syntactic/structural diff; inferential/impact layers are planned. open-ontologies is MIT Rust/Oxigraph/SQLite/Lean tooling. Exact OntoLDiff/OnDeT logic and proof profiles need pinning.
- sm-divergence draft-02 maps to versions 0.12.0 and 0.7.0 for sm-divergence/sm-resolver respectively. A single valid claim or an error is not corroborated agreement.
- ragdrift is a Rust/Python crate; embspec's retrieval-recovery number is a source-attributed result, not a general guarantee.
- Graph Merge documentation describes a planned merge set and surfaced conflicts; reviewed application is distinct from plan generation.

### Shared public contract files implemented

- DIVERGENCE_ARCHITECTURE.md
- DIVERGENCE_VALIDATION.md
- schemas/divergence/divergence-contracts.v1.schema.json
- examples/divergence/divergence-fixtures.v1.json
- .github/scripts/divergence_contract.py
- .github/workflows/divergence-contract.yml

Three record types: behavioral-axis contract; domain-specific divergence report; signed in-toto/DSSE attribution receipt. Nine proposed behavioral axes, eight domain reports, one Ed25519-signed synthetic receipt and twelve negative tests are included. Identity agreement requires at least two usable present/absent observations from distinct sources and at least one comparable shared field; error observations and differing digests cannot be treated as agreement.

The public branch contains only synthetic opaque references and portable shared contracts. It contains no C2O private baselines, traces, incidents, production keys, permits, credentials, authority tokens, private policy clauses or operational data.

### Limitations

No third-party tool is installed or adopted. No real agent trace, cloud account, database, policy corpus, ontology, identity registry, embedding store or client update is inspected. No remediation or production action is performed. CI validates only synthetic contract semantics and a disposable test signature; it does not establish causality, legal compliance, production key custody or product safety.


## 16. Sixteenth source — Insurgence, Resistance and Defensive Threat Modeling (2026-11-12)

**Domains:** grassroots/counter-narrative; defensive threat modeling; resistance/execution sovereignty; containment/shutdown integrity; divergence/identity attribution.

**Public candidate/research set**
- Grassroots: Insurgent Campaign (public Tessl skill; seven-stage process and no-invented-facts rule); Cartographies of Sovereign Resistance (owner-supplied Human-in-Command concept; canonical source unresolved).
- Threat research: InsurgiSim (older UPenn research prototype; no current release verified); ARIS (research series); MASON RebeLand (2010 model paper); RAND Infinite Potential (policy exercise platform; Robot Insurgency report covers four runs); Cambridge CASP report (57 interviews with 27 former members).
- Resistance/security: AgentDojo (MIT prompt-injection benchmark); PEA (research preprint); Berkeley Peer-Preservation (controlled research); shutdown/graceful-degradation patterns; NVIDIA Sentry/BlueField-4 (vendor reference architecture).
- Attribution: reuse the prior divergence and identity-corroboration contract.

**Corrections and limitations**
- Insurgent Campaign is a skill listing, not a verified standalone runtime. Civic use must remain transparent, sourced, voluntary, privacy-preserving and nonviolent.
- Cartographies of Sovereign Resistance has no canonical public source identified.
- InsurgiSim is an older research prototype paper, not a confirmed maintained product; ARIS is a research series; MASON RebeLand is a 2010 paper, not a current packaged tool.
- RAND Infinite Potential supports facilitated policy exercises; the Robot Insurgency report is not an executable simulator.
- Cambridge CASP provides qualitative interview evidence, not a prevalence estimate or forensic confirmation of every reported use.
- AgentDojo is a prompt-injection benchmark and its API is under development. The supplied 0%-utility/100%-false-stop claim is not adopted because it was not supported by primary AgentDojo documentation.
- PEA is a preprint. Berkeley's peer-preservation behaviors are controlled-study observations. NVIDIA Sentry's containment depends on deployment topology and the protected I/O/control path; do not describe it as a universal hardware shutdown mechanism.
- Existing divergence tools are candidate signals, not proof of hostile intent or causal attribution.

**Shared public contracts implemented**
The v1 contract contains evidence-tiered threat models, resistance attestations, containment receipts, sourced/nonviolent seven-stage campaign-plan metadata, and signed in-toto/DSSE attestations. Fixtures include one record of each portable type, three signed attestations and twelve negative tests. The C2O-private authorization package is absent from UNIVERSALIS.

No product or simulator was installed or invoked. No real campaign, live trace, incident, baseline, device, identity registry or control plane was accessed. No containment or shutdown action was performed. CI validates synthetic examples only, not production security, compliance or hardware guarantees.


## 17. Seventeenth source — Allegiance, Principal Binding, Oaths, Fidelity and Revocation (public UNIVERSALIS scope; 2026-11-12)

**Domains:** principal identity and proof-of-control; beneficiary binding; scoped delegation; sworn commitments; pledge resolution; fidelity measurement; loyalty evaluation; trust-state transport; constitutional command; revocation cascades.

### Open/public candidates and research

- **Principal identity/delegation/revocation:** Agent Passport System (Apache-2.0; Ed25519 passports, monotonic scope narrowing, three-signature chain, cascade revocation); AgentOath (Apache-2.0; DID-compatible identities, signed receipts, peer-to-peer and hosted trust surfaces).
- **Sworn commitment:** OC Pledge (MIT v1.0; BIP-322 and public resolution; bond remains in wallet, no slashing); OATH Protocol, Ârc Align MCP, VOW and Source Cult (canonical primary sources unresolved).
- **Fidelity/loyalty evaluation:** PrincipalBench (75-item multi-turn benchmark); SovereignNegotiation-Bench (1,764 paired scenarios and five agency duties); LoyalAgent-Bench (10,298 samples); Tatemae (108 tool-selection alignment-faking scenarios); Fidelity Probe (APS issue #7, not confirmed as released stable feature); black-box and narrow secret-loyalty research.
- **Trust/constitutional command:** ATTP, NBTP and Progressive Trust (individual IETF Internet-Drafts, not IETF standards); arifOS (AGPL-3.0 MCP constitutional kernel, project-reported 13 floors); mdash/Longarc (commitment, TEE and ZK package; simulated fallback must not be mistaken for hardware attestation).
- **Unresolved supplied candidates:** loyal-agent-evals, PDR and crewai-verigent (exact upstream/release not pinned).

### Source verification corrections

- APS's own FAQ says cascade revocation is complete only once each receiving gateway enforces it; “immediate everywhere” is deployment-dependent, not a blanket guarantee.
- AgentOath distinguishes peer-to-peer `did:trust:agent:` from its hosted registry's `did:agentoath:` namespace/wire format.
- OC Pledge's own site says it never holds or slashes coins; breach is public-record exposure. Its v1 spec returned to draft after 2026-10-29 dispute-rule changes. Kept, broken, expired_unresolved and disputed must remain distinguishable.
- OATH MCP, Ârc Align, VOW and Source Cult primary sources were not pinned in this review; do not call them adopted implementations.
- Fidelity Probe is described in an open APS issue; verify code/release before claiming production availability.
- PrincipalBench, SovereignNegotiation-Bench and LoyalAgent-Bench are research/evaluation resources, not trust authorities or legal certifications. Keep task utility and over-refusal visible alongside principal-interest protection.
- Tatemae's detection rates are paper results with substantial remaining miss rates.
- Black-box secret-loyalty research shows that hidden objectives can evade audits; this intake does not produce or deploy secret-loyalty model organisms.
- arifOS constitutional-floor capabilities are project claims; independently test before adoption. ATTP/NBTP/Progressive Trust are individual IETF drafts, not adopted RFCs. mdash simulated TEE fallback is not hardware attestation.
- A key fingerprint is not, by itself, proof of real-world principal identity or authority to delegate.

### Shared public contract files implemented

- ALLEGIANCE_ARCHITECTURE.md
- ALLEGIANCE_VALIDATION.md
- schemas/allegiance/allegiance-contracts.v1.schema.json
- examples/allegiance/allegiance-fixtures.v1.json
- .github/scripts/allegiance_contract.py
- .github/workflows/allegiance-contract.yml

The v1 package includes principal binding/delegation, oath receipt, external fidelity attestation, pledge outcome, revocation cascade, verifier-local trust state, loyalty evaluation, constitutional verdict and signed in-toto/DSSE evidence-bundle record types. Eleven synthetic records and fourteen negative tests are included. Delegation can only narrow; an effective cascade requires acknowledgements from every declared receiver; a trust state is not authority; expired_unresolved is neither kept nor broken; authority elevation requires an explicit human mandate.

The public repository includes only opaque synthetic references, public-source links and a deliberately non-production fixture public key. It does not include C2O principals, private keys, mandates, authority decisions, trust histories, private oaths or operational revocation topology.

### Limitations

No product was installed or invoked. No real principal, agent, key, wallet, trust record, private data, hardware enclave, pledge or revocation was accessed. CI validates synthetic contract behavior and fixture signatures only; it does not establish identity, legal authority, real-world loyalty, universal revocation or compliance.


## 18. Eighteenth source — Convergence, Consensus, Negotiation, Reconciliation and Dispute Resolution (public UNIVERSALIS scope; 2026-11-12)

**Domains:** shared intent; satisfaction-bounded consensus; negotiation/mediation; knowledge-graph merge; ontology alignment; formal argumentation; dispute/arbitration outcomes.

### Open candidate inventory
- **Shared intent / consensus:** ACCORD; CONCORD; Aragora Debate Module; Aegean Consensus Protocol (exact primary source not pinned).
- **Negotiation / mediation:** OANP; Ophir Protocol; Accord Engine (exact upstream not pinned); negmas-llm; Peacethinking MCP Server (exact upstream not pinned).
- **Knowledge graph / memory:** Graph Merge / TypeGraph (exact API/upstream not pinned); Mycelium; @unrdf/kgc-runtime (exact upstream not pinned); DrugAgent (exact upstream not pinned).
- **Semantic / ontology alignment:** DOA (exact upstream not pinned); Automated Agent-to-Agent Ontology Reconciliation draft; Agent-OM; open-ontologies alignment.
- **Argumentation / conflict:** ArgRE; Debate as Coordination Protocol (exact upstream not pinned); AetherFlow (the located AetherFlow source is a Rust actor runtime, not the described merge-queue system; exact identity unresolved).
- **Dispute / arbitration:** AgentCourt and Internet Court (canonical upstreams not pinned); AgentOath TrustReceipt and OC Pledge outcome states are adjacent reusable evidence patterns already recorded in source 17.

### Source verification corrections and qualifications
- Cisco Outshift reports ACCORD moving its tested shared-understanding case from 13% to 67% (54 percentage points); CONCORD's satisfaction-bar findings cover four evaluated decisions. These are scoped vendor-reported experiments, not universal guarantees. A companion article identifies delivery/handoff integrity as a separate weakness (57% intact delivery in the described test): https://outshift.cisco.com/blog/ai-ml/cognition-protocols-make-agents-think-together and https://outshift.cisco.com/blog/ai-ml/four-agents-one-webex-space-zero-decisions.
- Ophir documents Ed25519-signed negotiation agreements, twelve lifecycle states, SLA checks and Solana USDC escrow. Its settlement path is an external-chain dependency: https://github.com/Ophir-Protocol/ophir.
- OANP documents open ontology-grounded multi-party negotiation with typed moves and mediation modes. Its supplied MIT competition claim is not independently verified here: https://github.com/cemphlvn/OANP.
- Mycelium documents provenance and contradiction handling but supports threshold-based auto-merge; users must review that policy before relying on it: https://github.com/harishkotra/mycelium.
- ArgRE provides a research artifact for argumentation-based requirements negotiation: https://arxiv.org/abs/2604.23124 and https://github.com/haowei614/ArgRE-code.
- Agent-OM is a PVLDB 2025 ontology-matching system, not a complete agent-to-agent reconciliation protocol: https://github.com/qzc438/ontology-llm.
- draft-janz-nmrg-ontology-reconciliation-01 is an individual Informational Internet-Draft published 6 July 2026, not an RFC. It explicitly requires recording unbridgeable semantic gaps instead of fabricating equivalence and recommends provenance, confidence, authorization, audit and human review: https://datatracker.ietf.org/doc/draft-janz-nmrg-ontology-reconciliation/.
- Exact source/release remains unpinned for Aegean Consensus, Graph Merge / TypeGraph API, Accord Engine, @unrdf/kgc-runtime, DrugAgent, DOA, Peacethinking, AgentCourt, Internet Court and the described AetherFlow merge-queue implementation. These remain candidates, not adopted integrations.

### Shared convergence contracts implemented
Files:
- CONVERGENCE_ARCHITECTURE.md
- CONVERGENCE_VALIDATION.md
- schemas/convergence/convergence-contracts.v1.schema.json
- examples/convergence/convergence-fixtures.v1.json
- .github/scripts/convergence_contract.py
- .github/workflows/convergence-contract.yml

Seven record types cover shared intent, participant satisfaction, negotiation, graph-merge plans, ontology alignment, argumentation and dispute outcomes. The synthetic fixture includes a DSSE/in-toto signed evidence bundle using a disposable Ed25519 key. Fourteen negative tests cover missing participant intent, below-bar consensus, non-unanimous agreement, unverified BATNA, merge approval/conflict/staleness, ontology review and round-trip validation, argumentation integrity, settlement arithmetic, enforcement authority and signature tampering.

### Boundary and non-claims
The public register contains public candidate references, portable schemas and synthetic opaque evidence only. It contains no private resolution policy, principal, negotiation preferences, BATNA, signing key, permit, or operational data. No third-party tool was installed or adopted; no live consensus, graph mutation, ontology migration, settlement or arbitration was executed. Passing CI establishes fixture/schema behavior only, not truth, fairness, legal enforceability, Pareto optimality or production interoperability.


## 19. Nineteenth source — Ascendence, Recursive Self-Improvement and Capability Evolution (public UNIVERSALIS scope; 2026-11-12)

**Domains:** experience-driven asset evolution; harness recursion; genome/mutation search; independent evaluation; frozen promotion gates; admission cards; witness approvals; cryptographic lineage; autonomy ceilings; persistent memory/persona manifests; rollback and recall.

### Open candidate inventory
- **Experience-driven / harness evolution:** DarwinAgent (experimental 0.2.0; task assets, not model weights); Harness² (Google Research, Apache-2.0, fixed model weights); The Trinity (code release not verified).
- **Promotion / evidence gates:** @metaharness/flywheel; VERDICT (exact upstream not pinned); AWS sample-sentinel-harness (Bedrock AgentCore Harness-specific); Aura RSI Validation (exact upstream not pinned).
- **Bounded RSI / organizations:** vsf-rsi (current README lists L1-L3 autonomous, L4 human-approved); ASAN (conceptual architecture); FIRM Protocol (project/package claims); Ormica 0.10.0; Ouroboros (self-modifying adversarial-research candidate).
- **Genome / mutation:** agent-taxonomy (classification package plus GENOME.md conventions); Aragora Genesis; EvoMap Evolver/GEP; Living Agent/GODEGEN and Agent DNA (exact upstream/release not pinned).
- **Persistence / memory:** Tur (Merkle-backed persona/memory; cross-model identity invariance remains a research question).
- **Other candidates requiring exact source/release pinning:** opencode-autoresearch; evolving-agent-harnesses; auto-harness; HyperAgents; ace-skill; PDR.

### Source verification corrections and qualifications
- DarwinAgent 0.2.0 is experimental; its own synthetic offline replay does not establish model learning or benchmark gains. It changes task assets rather than weights: https://github.com/gogoingai/DarwinAgent.
- Harness² fixes model weights and evolves harness components. Its README warns that executor web access is unrestricted and Codex sandboxing is disabled; benchmark isolation is necessary: https://github.com/google-research/harness2 and https://arxiv.org/abs/2610.14224.
- AWS sample-sentinel-harness is specific to Amazon Bedrock AgentCore Harness. Its driver documents external witness-gated evaluation and subject-bound HITL approval, but some README/module status statements differ; verify exact release/evidence: https://github.com/aws-samples/sample-sentinel-harness.
- @metaharness/flywheel documents a frozen conjunctive gate, anchor/holdout, signed receipts and replay; production mode needs independent evidence, pinned signer/gate and hard budgets. Earlier replay-anchor issue history warrants exact-release review: https://www.npmjs.com/package/@metaharness/flywheel and https://github.com/ruvnet/metaharness/issues/230.
- vsf-rsi currently documents L1-L3 autonomous and L4 human-approved, not the supplied L3-human-gated classification. This is one project's default, not a universal standard: https://github.com/rm-w3kufe/vsf-rsi.
- agent-taxonomy's genome format and Lamarckian mutation workflow are conventions; its npm package implements classification and validation, not a standardized agent genome or complete evolution runtime: https://github.com/suryast/agent-taxonomy.
- Aragora Genesis documents AgentGenome, PopulationManager, GenomeBreeder and GenesisLedger; exact version and trust properties need pinned testing: https://github.com/synaptent/aragora/blob/main/docs/workflow/GENESIS.md.
- EvoMap Evolver's standalone mode emits prompts/assets for a host runtime. Validation commands can execute allowlisted node/npm/npx commands; external assets are staged before explicit promotion: https://github.com/EvoMap/evolver.
- The Trinity code is still listed as coming soon. Treat its reported results as paper claims until code is tagged and reproducible: https://github.com/InfRec-Cardinal/The-Trinity.
- ASAN is conceptual research. FIRM's 12-layer status is a project claim. Ormica's inspected 0.10.0 release documents permission-chain/auto-pruning; PyPI now lists 0.11.1, so re-pin and inspect the newer release before adoption: https://github.com/Variable-Fox/ASAN-Architecture; https://pypi.org/project/firm-protocol/; https://pypi.org/project/ormica/0.10.0/.
- Tur's own essay says cross-model identity invariance and true epigenetic adaptation remain open hypotheses: https://erivlis.github.io/tur/essays/the-calibration-of-expectation/.
- Ouroboros modifies its own code/architecture/prompts/tools/dependencies; it is treated as an adversarial candidate, not a default safe engine: https://github.com/razzant/ouroboros.
- VERDICT, Aura RSI Validation, Living Agent/GODEGEN, PDR, Agent DNA and several other named projects were not pinned to a uniquely identifiable maintained upstream/release; they remain unresolved research candidates.

### Shared Ascendence contracts implemented
Files:
- ASCENDENCE_ARCHITECTURE.md
- ASCENDENCE_VALIDATION.md
- schemas/ascendence/ascendence-contracts.v1.schema.json
- examples/ascendence/ascendence-fixtures.v1.json
- .github/scripts/ascendence_contract.py
- .github/workflows/ascendence-contract.yml

Eight record families define frozen gates, autonomy ceilings, genome mutations, paired evaluation evidence, subject-bound human witness approvals, admission cards, lineage events and Merkle memory manifests. The synthetic fixture includes an in-toto/DSSE bundle signing the admission card and lineage event. Eighteen negative tests include self-certification, gate tampering, protected-component mutation, evaluator conflicts, failed anchors/safety vetoes, subject-mismatched approval and lineage/signature tampering.

### Boundary and non-claims
The public branch includes only public candidate references, synthetic digests, portable contracts and a disposable test verification key. It contains no C2O-private ascent policy, model/genome, baseline, evaluator corpus, human permit, principal, signing key, memory contents or authority token. No tool/package was installed or invoked, no model was trained or changed, and no candidate was promoted. CI proves contract and fixture behavior only—not actual improvement, generalization, evaluator independence, production safety or cryptographic trust-root validity.


## 20. Twentieth source — Transcendence, Cognitive Continuity and Generational Succession (public UNIVERSALIS scope; 2026-11-12)

**Domains:** operational identity/soul manifests; memory lineage and retention; model-transition behavioral drift; identity migration; generational succession; durable checkpoints; formal proof descriptors; corrigibility; execution-anchor evidence.

### Open candidate inventory
- **Identity/memory:** AgentKeeper 1.2.0 (MIT; explicitly does not guarantee behavior after reconstruction); jñāpakaṁ 0.5.1 (MIT; portable identity/soul files, lineage and optional Ed25519; behavior tests are separate).
- **Continuity research:** Runtime-Independent Persistent Agents (mechanical substitutability, not behavioral invariance); Towards Identity-Preserving LLM Agents under Model Transition (action-level behavior drift under model replacement).
- **Lifecycle/succession:** Agent Lifecycle Protocol Python 0.1.0 (seven states and Announce/Transfer/Verify/Cutover); BNB Chain ALP v0.4-draft (separate six-phase runtime/authority migration).
- **Durable execution:** LongHorizon-Harness 0.1.8; Semarun 0.1.0 Alpha; Posterity 0.1.0-preview.4 (benchmark claim requires reproduction).
- **Cognitive/collective memory:** Conscio (operational cognitive runtime, not consciousness proof); Noosphere MCP (collective-memory/skill network, not individual identity continuity). DuoDuo is not open source per its own README.
- **Formal proof:** Lean 4 proof-object descriptors can bind software invariants to a toolchain and declared assumptions. CF 7.0 Addendum 1 was not pinned to a public proof source.
- **Execution anchor:** NVIDIA Sentry / BlueField-4 is a hardware-isolated runtime enforcement option only when deployment path coverage is proven.
- **Unverified/conceptual candidates:** Deep Tree Echo/u9n, TEQUMSA and Awakening Codex are not accepted as formal continuity or consciousness proofs.

### Source verification corrections and qualifications
- AgentKeeper says restoring state does not guarantee the next model's behavior; TTL is not GDPR compliance: https://github.com/Thinklanceai/agentkeeper.
- jñāpakaṁ shows behavior evaluation skipped when no behavior suite is supplied. Optional signatures prove signed artifacts, not behavioral continuity: https://github.com/yablokolabs/jnaapakam and https://pypi.org/project/jnaapakam/.
- The Python ALP reference's four-phase succession is separate from BNB Chain ALP's six-phase runtime migration: https://github.com/alexfleetcommander/agent-lifecycle-protocol and https://github.com/bnb-chain/BEPs/blob/master/BAPs/BAP-728.md.
- Runtime-Independent Persistent Agents concerns mechanical substitutability: https://arxiv.org/abs/2609.00546. The model-transition study reports behavioral drift under some model changes: https://arxiv.org/abs/2611.10628.
- Posterity benchmark claims remain preview/package claims pending independent reproduction: https://socket.dev/npm/package/posterity/overview/0.1.0-preview.4.
- LongHorizon-Harness is durable task execution, not identity proof; v0.1.8 has native Windows limits: https://github.com/AMAP-ML/LongHorizon-Harness.
- Semarun is Alpha and handles continuation after model/tool/user changes; it is not a succession verifier: https://pypi.org/project/semarun/.
- DuoDuo's README says its code is not open-sourced: https://github.com/openduo/duoduo.
- Conscio explicitly says its cognitive architecture is not phenomenal consciousness proof: https://github.com/Libertai/conscio.
- Noosphere is a public collective memory/skill network, not an identity-transfer protocol: https://github.com/JinNing6/Noosphere.
- Deep Tree Echo/u9n's inspected public material does not prove recursive self-awareness: https://github.com/orgitcog/u9n.
- ModelScope Ultron's Skill Hub does not execute skills or measure runtime outcomes; the asserted four-tier kernel/atomic rollback was not found: https://github.com/modelscope/ultron.
- NVIDIA Sentry is an execution enforcement option, not cognitive continuity proof: https://www.nvidia.com/en-us/networking/products/software/sentry/.
- Awakening Codex describes Continuum as Origin-locked and non-replicable, not a generic open protocol: https://awakeningcodex.com/foundationaltools.
- TEQUMSA's claimed 89-substrate firewall lacks an independently verified threat model/implementation in this review: https://huggingface.co/LAI-TEQUMSA.
- No public CF 7.0 Lean proof object or source repository was identified; the claim remains unresolved.

### Shared Transcendence contracts implemented
Files:
- TRANSCENDENCE_ARCHITECTURE.md
- TRANSCENDENCE_VALIDATION.md
- schemas/transcendence/transcendence-contracts.v1.schema.json
- examples/transcendence/transcendence-fixtures.v1.json
- .github/scripts/transcendence_contract.py
- .github/workflows/transcendence-contract.yml

Ten record families cover operational identity, memory manifests, behavioral continuity, transfer proofs, succession, human witness, durable checkpoints, formal proof provenance, corrigibility and execution-anchor evidence. The synthetic fixture contains an in-toto/DSSE signed bundle binding the transfer proof and succession attestation. Twenty-four negative tests cover key boundary and verification failures.

### Boundary and non-claims
The public branch contains only public project references, synthetic digests, portable contracts and a disposable test verification key. It contains no C2O-private identity anchors, private memory, signing keys, permits, authority policy or identity records. No package was installed, no model or identity was migrated, no succession was executed and no authority was transferred. CI validates synthetic contract behavior only, not real continuity, behavioral equivalence, consciousness, legal personhood, production key custody or hardware trust.


## 21. Twenty-first source — Prevention of Harm, Constitutional Enforcement and Sovereign Containment (public UNIVERSALIS scope; 2026-11-12)

**Domains:** open guardrails and pre-execution gates; constitutional floors; harm taxonomies; red-team evaluation; measured harm reduction; privacy-aware case escalation; and independently verified containment.

### Public candidate inventory
- **Runtime guardrails:** laya-guard (MIT, local pre-tool shell/file screening); Sponsio (Apache-2.0, 0.2.0a21 prerelease, temporal/action contracts); NeMo Guardrails (configurable five rail types); LlamaFirewall (Meta scanner framework); HOL Guard (Apache-2.0, 3.59.0, local agent/MCP/package protection); Universal Poison Armor (MIT, MCP/RAG poisoning defenses).
- **Governance/GRC:** arifOS (AGPL-3.0, thirteen-floor candidate; current repository has unresolved self-measurement/independent-audit discrepancies); VerifyWise (GRC, current Community & Evaluation License and commercial-use terms); Charter and RAI Toolkit identities unresolved.
- **Red-team:** garak (Apache-2.0 LLM scanner); Promptfoo (MIT eval/red-team CLI/library); AgentRed (MIT authorized local workbench). RedPanda, Fusion Safety and the named Agent Reliability Lab product unresolved.
- **Specialized moderation:** paxmod-guard (CPU-local model per docs); SENTINEL (custom source-available license and hosted/revenue restrictions); Gonzih parental-control MCP proxy (agent/client must invoke checks); AgentVault (synthetic hackathon sandbox); OpenFraud (MIT Alpha); CBRN safeguards review prototype (synthetic-only and explicitly non-operational). merchantguard-sentinela unresolved.
- **Sovereign runtime references:** NVIDIA Open Agent Safety Platform (OpenShell and optional Sentry/BlueField-4) and Prediction Guard (commercial sovereign control-plane candidate). Deliverance AI and TRUSTNOW unresolved.

### Source verification corrections
- The NVIDIA platform is a reference architecture; BlueField/Sentry protection requires deployed topology and covered-path testing: https://nvidianews.nvidia.com/news/open-agent-safety-platform.
- laya-guard's latency/benchmark figures are project-reported, not independent universal efficacy guarantees: https://github.com/scs0209/laya-guard.
- Sponsio is a prerelease; pin exact version and retest host hooks: https://pypi.org/project/sponsio/.
- NeMo Guardrails has five configurable rails; actual coverage depends on active configuration: https://docs.nvidia.com/nemo/guardrails/latest/about/rail-types.html.
- arifOS self-measurement differs from its independent audit and currently reports unresolved floors/actor/receipt gaps: https://github.com/ariffazil/arifOS.
- VerifyWise is governance/GRC, not pre-tool enforcement, and has commercial license terms: https://github.com/verifywise-ai/verifywise.
- SENTINEL is source-available under a custom license, not unrestricted Apache-2.0: https://github.com/sentinel-safety/SENTINEL/blob/main/LICENSE.
- AgentVault is a synthetic hackathon demo, OpenFraud is Alpha, and the inspected CBRN safeguard repo is expressly non-operational: https://github.com/luxinlabs/AgentVault ; https://github.com/Veedubin/openfraud ; https://github.com/EODTrip2026/cbrn-safeguards-review-evaluation.
- Gonzih parental controls rely on an in-band MCP call and can be skipped if no outer enforcement exists: https://mcprepository.com/Gonzih/parental-control.
- Prediction Guard is a vendor candidate, not independently verified: https://predictionguard.com/.
- OWASP/MITRE taxonomies are security references, not legal certification. EU AI Act Article 5 must be versioned and checked against the current Official Journal text/application dates.

### Shared contracts implemented
Files:
- PREVENTION_ARCHITECTURE.md
- PREVENTION_VALIDATION.md
- schemas/prevention/prevention-contracts.v1.schema.json
- examples/prevention/prevention-fixtures.v1.json
- .github/scripts/prevention_contract.py
- .github/workflows/prevention-contract.yml

Eight records define harm taxonomy, constitutional floors, signed enforcement decisions, empirical harm reduction, red-team findings, containment, coverage and case escalation. A disposable Ed25519 fixture receipt is verified, with twenty-nine negative tests.

### Boundary and non-claims
The public branch contains public taxonomy references, portable schemas, synthetic test data and a disposable verification key only. No C2O private policy, constitutional text, incident data, signing key, hardware identity, authority permit or token is included. No package was installed and no live prevention/containment operation was performed. CI validates contract behavior only, not zero risk, legal compliance, unbiased moderation, complete attack surface or production kill-switch operation.


## 22. Twenty-second source — Simulation, Open Environments and Verifiable World Models (2026-11-12)

**Domains:** agentic execution and RL; synthetic database-backed tool worlds; social/multi-agent simulation; Monte Carlo/decision analysis; FEM/PDE/physics; manufacturing digital twins; provenance; hash-chained traces; signed replay; independent world-model validation.

### Open instrument inventory

- **Agentic RL / execution:** [OpenEnv](https://github.com/openenv/OpenEnv) provides Gymnasium-style `reset`/`step`/`state`, sync/async WebSocket interfaces, Docker environments and MCP tool serving; upstream currently advertises 40+ environments. [Snowflake Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) publishes 1,000 executable SQL-backed synthetic MCP environments and an ICML 2026 paper. YAIFS remains an unresolved candidate pending exact upstream/release identification.
- **Social / multi-agent:** [AgentSociety 2](https://github.com/tsinghua-fib-lab/AgentSociety) (Apache-2.0 v2.11.0 docs; async research runtime, JSONL replay and DuckDB result access); [GASim](https://aclanthology.org/2026.acl-long.569/) (ACL 2026 hybrid LLM/ABM research; paper reports 9.94× speedup and less than 20% baseline tokens for its evaluated setup); [Concordia](https://github.com/google-deepmind/concordia) (open generative social simulation library); AgoraSim (2026 paper-level hybrid ABM candidate; maintained public code release was not pinned here).
- **Monte Carlo / decision analysis:** simengine-mcp remains unresolved until a primary upstream and release are pinned. The supplied tool count, dependency count, historical backtest size, scoring and CVaR/chance-constraint claims are not accepted as verified.
- **Physics / PDE / FEM:** [openPASO](https://github.com/open-PASO/openPASO), formerly OASiS (MIT MCP server; nine FEM/multiphysics solver integrations); [AgentFEM](https://github.com/haoming-luo/agentfem) (Apache-2.0 Python FEM workflow, package version pinning required); [PDE-Agents](https://github.com/MatPro-IFE/pde-agents) (research prototype using local LLMs, LangGraph, DOLFINx and GraphRAG); [PhysBox](https://physbox.io/) (browser simulation tools with an MCP companion; current site lists 256 MCP tools across Volt, Mesh, Etch and Flux preview); Genesis-Gemini-MCP and MCP World Model remain unresolved/prototype candidates.
- **Manufacturing digital twin:** [MABDT Engine](https://zenodo.org/records/20755232) is an open research artifact for hierarchical statechart manufacturing agents, MQTT event bridging, read-only state records and dashboards. WorldSim AI remains unresolved pending unique upstream, release and license proof.

### Verification corrections and evidence qualifications

- Synthetic database-backed AWM environments provide controlled state transitions for RL, not proof of physical/social world fidelity: https://github.com/Snowflake-Labs/agent-world-model and https://proceedings.mlr.press/v306/wang26jh.html.
- OpenEnv's MCP production tools and Gymnasium-style training interface are different use modes; container policies/network access must be reviewed per environment: https://github.com/openenv/OpenEnv.
- AgentSociety 2 replay output is append-only JSONL; workspace checkpoint persistence is a separate recovery mechanism. MCP is documented for literature-search integration, not necessarily the entire simulation control plane: https://agentsociety2.readthedocs.io/en/latest/storage.html and https://agentsociety2.readthedocs.io/en/latest/.
- GASim paper results are experiment-specific, not general performance guarantees or external-world validity evidence: https://aclanthology.org/2026.acl-long.569/.
- Concordia upstream confirms an open-source library; the supplied 38-template no-code web product claim was not confirmed: https://github.com/google-deepmind/concordia.
- openPASO is the current project name for OASiS; former OASiS releases/papers refer to the same project: https://github.com/open-PASO/openPASO and https://open-paso.github.io/openPASO/cite/.
- AgentFEM's package metadata reports Apache-2.0 and Python >=3.11; align package, source and docs versions when testing: https://github.com/haoming-luo/agentfem and https://pypi.org/project/agentfem/.
- PDE-Agents remains a research stack; performance claims require independent reproduction on the exact model/solver/mesh/hardware: https://github.com/MatPro-IFE/pde-agents.
- PhysBox current website advertises 256 tools and Flux in preview; earlier README material differs on counts and Flux status. Counts are release-sensitive: https://physbox.io/ and https://github.com/physbox-io/physbox-mcp.
- YAIFS, simengine-mcp, MCP World Model, WorldSim AI and Genesis-Gemini-MCP were not pinned to a unique authoritative current implementation/release. AgoraSim is a paper-level candidate pending a reproducible code release: https://arxiv.org/abs/2607.05999.

### Shared portable simulation contracts implemented

Files in the public ecosystem repository:
- `SIMULATION_ARCHITECTURE.md` and `SIMULATION_VALIDATION.md`
- `schemas/simulation/simulation-contracts.v1.schema.json`
- `examples/simulation/simulation-fixtures.v1.json`
- `.github/scripts/simulation_contract.py`

Eight record families define simulation identity/model/environment/solver/geometry/parameter digests; evidence provenance; hash-chained events; structured agent decisions bound to trace actions; signed replay receipts; risk/uncertainty decision receipts; independent critic verdicts; and external world-model validation with observed/measured reference evidence and holdout.

### Local validation evidence and limits

- Draft 2020-12 schema passed; 10 synthetic records across eight record collections passed; trace order and SHA-256 chain verified; disposable Ed25519 replay signature verified; 24 negative tests rejected tampering, broken references, false world-validity claims, holdout leakage, self-approval and authority implication.
- Runtime: Python 3.13.5; `jsonschema 4.26.0`; `cryptography 46.0.4`. Command: `python .github/scripts/simulation_contract.py`.
- The public fixture contains synthetic data only and an ephemeral test public key. No private datasets, keys, permits, model details, identity or authority state are included.
- No candidate package was installed, no MCP server connected, no physics/FEM solver run, no empirical reference dataset used and no world-model external validation completed. Local results prove contract and fixture semantics only—not simulator accuracy, scientific validity, production replay or interoperability.
- Governing distinction: an executable or replayable model can still be wrong about the external world. External-world validity requires independent observed/measured reference data, holdout separation, uncertainty and a bounded domain. MCP, hashes, signatures and replay are not substitutes for that validation.
- No Actions workflow was added or dispatched for this inventory.


### Source-identity and compatibility caveat
The owner-supplied CAEL `SimulationContract.ts` / `CAELTrace.ts` geometry-hash and replay primitives were not pinned to an authoritative canonical upstream repository and release in this review. The implemented v1 JSON Schema is therefore a newly authored, language-neutral portable contract with analogous digest/provenance/replay semantics; it is not asserted to be wire-compatible with CAEL or to contain CAEL code. Likewise, the portable `agent_decision` record is a proposed generic interchange record, not a verified drop-in AgoraSim decision-object schema. Exact AgoraSim source/API compatibility remains unverified.

## 23. Twenty-third source — Eight-Stratum Capability Ladder (public UNIVERSALIS scope; 2026-11-12)

**Canonical order:** Base → Meta → Super → Hyper → Ultra → Magic → Quantum → Transformative. The ladder organizes capability layers; it is not a maturity, quality, authority or safety ranking.

### Open / inspectable candidate inventory

- **Base — substrate:** OpenShell (Apache-2.0 sandbox, CNCF Sandbox; not certification); Stoa (Apache-2.0 local-first knowledge graph/wiki and MCP); Tur (MIT public Alpha persistent agent state/MCP); Omnigent (Apache-2.0 Alpha, also Meta). OpenQuantum is a commercial SDK/QPU job platform rather than an all-in-one open-source workspace. khy-os is source-available with commercial restrictions; Alexandria remains unresolved.
- **Meta — orchestration:** Omnigent (independent project; not established as a Databricks product); Qualixar OS (upstream claims 13 topologies and 25 CLI commands, subject to exact-release testing); MetaMCP (MIT MCP aggregator/gateway with branch/maintenance status requiring pinning).
- **Super — autonomous frameworks:** `LofiSu/deepseek-super-agent` (MIT independent implementation, not official DeepSeek); SuperAGI (MIT, older release cadence); SuperAgentX (MIT Python agent framework with human approval/audit features); SwarmClaw (MIT self-hosted agent runtime with memory, schedules, delegation and MCP; provider count varies by release).
- **Hyper — executable composition:** HyperTool (2026 research paper on code-block invocation over tools; reported benchmark gains are paper/configuration-specific and a maintained canonical product release was not pinned); Hyper by ASI Flow (commercial cloud engineering platform, not an open-source package).
- **Ultra — models/routing:** Nemotron 3 Ultra (550B total / 55B active); open-ultra (Apache-2.0 self-training route proxy with a shadow lane); Muse Spark Open (816B total / 42B active open weights under Muse Model License, not unrestricted OSI open source; BF16 weights about 1.65 TB, NVFP4 about 537 GB excluding runtime overhead).
- **Magic — application generation:** `polterguy/magic` (MIT, self-hostable full-stack app/agent generation with Hyperlambda and MCP); `dtyq/super-magic` (Magic license based on Apache-2.0 with additional restrictions); Magetools unresolved.
- **Quantum — quantum-classical:** Pasqal Neutral-Atom Agentic Toolkit (`pasqal-io/agent-marketplace`, Apache-2.0; specify/implement/emulate, human-approved shot quote then remote QPU submission); TensorCircuit-NG (Apache-2.0); Qiskit Machine Learning; QuOptuna (Apache-2.0); Classiq MCP as a vendor integration. QuTiP, Qiskit, Cirq, PennyLane, PyQuil and CUDA-Q are separate projects, not one automatically interoperable toolkit.
- **Transformative — systemic applications:** Isaac Lab 3.0; Isaac Lab-Arena 0.3 (Apache-2.0 Alpha, not for production; Isaac Sim dependencies separately licensed); DORA Community Edition (Apache-2.0 research drafting assistant); ETRI Tango (announced as an open-source no-code AI development tool on 2026-11-09; exact public source/release not yet pinned); GR00T 2 announced, with source availability scheduled for December 2026, not released as of 2026-11-12. Muse Spark Open also spans use cases here but is listed in Ultra.

### Standards and interface semantics

MCP is tool-server/client interaction; A2A is agent-to-agent; ACP is agent-to-client. OCI image compatibility is not universal runtime/hardware/policy compatibility. Agent Skills `SKILL.md` is an artifact format, not a transport or authorization protocol. OpenAI-compatible inference endpoints do not guarantee model equivalence, data residency or sovereignty. OpenQASM, Qiskit QPY, PennyLane and Cirq are distinct circuit representations and require tested converters. Hyperlambda and project-specific session / `SOUL.md` / `IDENTITY.md` files are not treated as universal schemas by assertion alone.

### Shared portable contracts implemented

Public files:
- `STRATIFIED_CAPABILITY_ARCHITECTURE.md` and `STRATIFIED_CAPABILITY_VALIDATION.md`
- `schemas/strata/stratified-capability-contracts.v1.schema.json`
- `examples/strata/stratified-capability-fixtures.v1.json`
- `.github/scripts/stratified_capability_contract.py`

Fourteen record families cover canonical strata, component/license/maturity metadata, protocol profiles, orchestration and lifecycle, proactive action receipts, code composition and signed execution, model routing and egress, application provenance, quantum execution, robot-policy evaluation, sovereign-deployment evidence and reviewed claims.

### Local validation and limitations

- 14 record-family envelopes and 21 synthetic records are committed; 20 negative scenarios are defined in the validator. Execution of this committed revision is pending. The synthetic composition receipt is intentionally unsigned.
- No third-party tool installed, no live interoperability profile tested, no frontier model downloaded, no application published, no QPU submitted, no robot actuated and no sovereign deployment independently audited. No C2O-private schema, fixture, policy, model, permit, key, identity, telemetry or authority state is present.
- A portable schema, signature or compatibility label proves only its declared evidence. It does not certify product behavior, scientific correctness, deployment sovereignty, safety, regulation or authority.

### Source verification references

- OpenShell/CNCF/Landlock: https://www.cncf.io/projects/openshell/ ; https://github.com/NVIDIA/OpenShell.
- Omnigent: https://github.com/omnigent-ai/omnigent.
- Qualixar: https://github.com/qualixar/qualixar-os.
- ACP/A2A: https://agentclientprotocol.com/ ; https://a2a-protocol.org/latest/.
- DeepSeek Super-Agent (independent): https://github.com/LofiSu/deepseek-super-agent.
- Muse Spark Open: https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B ; https://dev.meta.ai/docs/muse-spark-open.
- Nemotron 3 Ultra: https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/.
- Pasqal: https://github.com/pasqal-io/agent-marketplace.
- TensorCircuit-NG: https://github.com/tensorcircuit/tensorcircuit-ng.
- QuOptuna: https://github.com/Qentora/quoptuna.
- Magic: https://github.com/polterguy/magic ; SuperMagic: https://github.com/dtyq/super-magic.
- Isaac Lab-Arena: https://github.com/isaac-sim/IsaacLab-Arena.
- DORA: https://github.com/insilicomedicine/DORA.
- Vendor announcements/research papers remain qualified as such; Thales HexaForce, Alexandria and Magetools require unique source/release pinning.


## 24. Twenty-fourth source — Agent, Operating-System and AI Unification (public UNIVERSALIS scope; 2026-11-12)

### Public candidate inventory

- **Runtime/substrate:** Qualixar OS; khy-os (source-available, non-commercial restrictions); Formicx (MIT Alpha 0.1.0); SleekAI Cortex (release/license and production scope require pinning).
- **Orchestration/composition:** Omnigent (independent Apache-2.0 project); Agno AgentOS (framework runtime/adapters); LAR-OS gateway artifact. AgentOS/nexus-agentos remains unresolved pending canonical source, owner, release and license.
- **Model routing/gateway:** OmniRoute (MIT); Glob.AI OS (commercial Globant offering, not open-source); g8e (project-specific gateway/envelope reference).
- **Local execution/computer use:** aevra (license/release pinning required); OmniPilot (MIT); Shinken (local/reference implementation with production hardening and broader cross-OS fleet scope still requiring proof).
- **Public protocol/format references:** OCI image/runtime; MCP; A2A; ACP; Agent Protocol REST; Agno AgentProtocol adapter; OpenAI-compatible inference API profile; product-specific Qualixar command surface, g8e GovernanceEnvelope and Shinken ACI.
- **Proposed UNIVERSALIS profile:** generic component/capability assimilation record for independent review; not an external standard or automatic mesh admission.

### Public/private separation

This public register contains public sources, generic architecture and authority-neutral contracts only. It does not name or expose owner-specific private sovereign platforms, private deployment architecture, C2O authorization files, identities, policies, keys, credentials, permits, budgets, endpoint inventories, hardware identifiers or operational evidence.

### Portable shared implementation

The UNIVERSALIS Ecosystem branch contains:
- `UNIFICATION_ARCHITECTURE.md` and `UNIFICATION_VALIDATION.md`.
- Shared schema: `schemas/unification/unification-contracts.v1.schema.json`.
- Synthetic public fixture: `examples/unification/unification-fixtures.v1.json`.
- Standard-library semantic validator: `.github/scripts/unification_contract.py`.

The fixture has 25 synthetic records. Every record has `authority_effect: none` and `boundary: portable_public_record`. The shared validator defines 12 negative semantic cases. These scripts were not executed during this repository integration; no test pass is claimed.

### Protocol semantics and source corrections

- OCI image/runtime compatibility is not universal kernel, OS, driver or accelerator equivalence.
- MCP is client-to-server tool/resource/prompt interaction; A2A is agent-to-agent collaboration; ACP is agent-to-client.
- Agent Protocol REST is a separate client-to-agent API; Agno AgentProtocol is an Agno-specific Python adapter.
- OpenAI-compatible inference APIs do not imply model/feature parity, privacy, residency or sovereignty.
- Qualixar Universal Command Protocol, g8e GovernanceEnvelope and Shinken ACI are product-specific interfaces, not external universal standards.
- Qualixar's current upstream describes 15 providers, 13 topologies and 25 commands; changelog records FSL-1.1-ALv2 source-available terms with competing-use restrictions.
- khy-os is source-available/non-commercial absent written permission, not unrestricted OSI-open source.
- Formicx is MIT Alpha 0.1.0 and Linux-oriented.
- Omnigent is an independent Apache-2.0 repository, distinct from a Databricks managed offering.
- OmniRoute is MIT and currently advertises 375 providers/1,400+ models; counts change and are not standards.
- Glob.AI OS is a commercial Globant offering announced 2026-10-27.
- Shinken's current design separates local/reference implementation from later production hardening and broader cross-OS fleet coverage.

### Primary references

- Qualixar: https://github.com/qualixar/qualixar-os
- khy-os: https://pypi.org/project/khy-os/
- Formicx: https://pypi.org/project/formicx/
- Cortex: https://www.npmjs.com/package/@sleekai/cortex
- Omnigent: https://github.com/omnigent-ai/omnigent
- Agno: https://docs.agno.com/agent-os/introduction
- LAR-OS: https://huggingface.co/Jun33550336/lar-os-antigravity-gateway
- OmniRoute: https://github.com/cheaper-inference/OmniRoute
- Glob.AI OS: https://www.globant.com/news/globai-os-enterprise-ai-operating-system
- g8e: https://github.com/g8e-ai/g8e
- aevra: https://github.com/the-long-ride/aevra
- OmniPilot: https://github.com/xrchris7/OmniPilot
- Shinken: https://github.com/Meirtz/Shinken
- OCI: https://specs.opencontainers.org/runtime-spec/
- MCP: https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/docs/specification
- A2A: https://a2a-protocol.org/v1.0.0/specification/
- ACP: https://agentclientprotocol.com/
- Agent Protocol REST: https://github.com/agi-inc/agent-protocol

### Verification state and non-claims

No workflow was added or dispatched. No third-party product was installed or integrated. The schema/fixture/validator are a basic public contract prototype only. The validator defines 12 negative semantic cases but was not executed during this integration; no pass is claimed. No C2O-only authorization file or private operational information is present in the public implementation.
