# Toolchain Coverage Register — UNIVERSALIS

**Date:** 2026-11-12  
**Scope:** Public UNIVERSALIS coverage of eight owner-supplied toolchain inventories: original four, Intelligence Capabilities, Intelligence Skills, Intelligence Powers, and Human Powers.
**Boundary:** This public register does not link to C2O-private owner repositories or disclose private policies, model weights, benchmark datasets, credentials, or authority tokens.

## 1. Original four source documents

The original four public/open source areas remain inventoried in FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md:
1. Human Knowledge.
2. Powers / Energy Efficiency / Synergy.
3. Human Capabilities.
4. Mapping / Matrix / Organization / Ecosystem Mapping.

That register contains the full UNIVERSALIS candidate lists, functional notes, implementation status, and CI receipts. This register consolidates the fifth through eighth inventories: Intelligence Capabilities, Intelligence Skills, Intelligence Powers, and Human Powers.

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
