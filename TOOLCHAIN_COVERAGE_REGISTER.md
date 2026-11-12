# Toolchain Coverage Register — UNIVERSALIS

**Date:** 2026-11-12  
**Scope:** Public UNIVERSALIS coverage of thirteen owner-supplied inventories: the original four, Intelligence Capabilities, Intelligence Skills, Intelligence Powers, Human Powers, Ontologies, Encyclopedias, Security and Cybersecurity, Platform / Construction Infrastructure (seven domains), and Websites.
**Boundary:** This public register does not link to C2O-private owner repositories or disclose private policies, model weights, benchmark datasets, credentials, or authority tokens.

## 1. Original four source documents

The original four public/open source areas remain inventoried in FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md:
1. Human Knowledge.
2. Powers / Energy Efficiency / Synergy.
3. Human Capabilities.
4. Mapping / Matrix / Organization / Ecosystem Mapping.

That register contains the full UNIVERSALIS candidate lists, functional notes, implementation status, and CI receipts. This register consolidates the fifth through thirteenth inventories: Intelligence Capabilities, Intelligence Skills, Intelligence Powers, Human Powers, Ontologies, Encyclopedias, Security and Cybersecurity, Platform / Construction Infrastructure, and Websites.

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
