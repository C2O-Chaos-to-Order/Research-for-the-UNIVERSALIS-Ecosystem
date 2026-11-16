# UNIVERSALIS Engineering, Verification, Research, and Immersive Toolchain Proposal

**Date recorded:** 2026-11-12  
**Status:** Owner-supplied proposal; candidates are proposed and unverified, not approved deployments.  
**Scope:** Open UNIVERSALIS / MotherThread repository responsibilities, shared engineering controls, immersive WebXR, and the controlled integration boundary with C2O.

## 1. Architectural placement and boundary

- UNIVERSALIS is the open, composable, independently operable MotherThread ecosystem. Its architecture must remain cross-device and cross-platform rather than tied to one device class.
- Public UNIVERSALIS implementations belong in the owning UNIVERSALIS ecosystem repository. Research, comparisons, evidence, and adoption decisions belong in this research repository.
- C2O remains separately governed and private. Public UNIVERSALIS code, documentation, examples, build artifacts, and test fixtures must not contain C2O credentials, private policies, authority state, or other restricted C2O information.
- Shared capabilities cross only through explicit, versioned, scope-limited interfaces with boundary authentication and authorization.
- This document records proposed candidates and intended responsibilities; it does not constitute adoption, installation, authorization, or verification.

## 2. Universal engineering foundation

The proposal calls for a common assurance baseline across C2O and UNIVERSALIS repositories, tailored to repository risk and role:

| Candidate / pattern | Proposed responsibility | Evidence and review required |
|---|---|---|
| Secure SDLC Evidence Collector | Normalize evidence from SARIF (Semgrep, CodeQL, SonarQube, Snyk Code, Trivy, Grype, Gitleaks, Bandit, pip-audit), Trivy JSON, CycloneDX/SPDX SBOMs, OSV-Scanner, JUnit XML, OWASP ZAP, in-toto SLSA VSA, SLSA provenance / GitHub Artifact Attestations, release attestations, and PyPI/npm attestations. | Validate accepted formats, schema handling, signature verification, provenance semantics, and evidence completeness. |
| repo-assurance | GitHub-native CodeQL, secret scanning, dependency graph/SBOM, Dependabot, and actionlint baseline. | Verify workflow permissions, repository feature availability, alert handling, and actual scan execution. |
| Chainguard Actions | Hardened GitHub Actions replacements for supply-chain-sensitive workflows. | Pin immutable action references where possible; assess publisher trust, permissions, compatibility, and update process. |
| cnspec SBOM Cataloger | Catalog GitHub Actions dependencies as part of the software supply chain. | Verify coverage, action/version resolution, output format, and integration with repository SBOM records. |
| European-Parliament-MCP-Server CI/CD pattern | Reusable pipeline pattern: tests, CodeQL, OSSF Scorecard, SLSA Level 3 provenance, PR dependency review, documentation generation, multi-registry publishing, cosign signing, and build provenance attestations. | Treat as a reference pattern, not a drop-in guarantee; adapt and test per repository. |
| JSON Schema tooling | Validate manifests, capability contracts, and skill definitions with ajv, jsonschema, or equivalent. | Pin schema dialect and validator versions; test valid, invalid, and compatibility fixtures. |

Reproducible-build controls proposed: pin toolchain versions, use deterministic build flags, record build environment and inputs, generate provenance, use semantic versioning and automated changelogs, and use immutable releases where supported. Independent rebuild comparison remains a separate check.

## 3. UNIVERSALIS domain-specific candidate tooling

### Ontology — typed schemas, graph validation, consistency

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| seocho | Python ontology-driven knowledge graph; schema-led extraction, querying, validation, SHACL shape generation, and Neo4j UNIQUE/INDEX constraint generation. | Validate ontology semantics, generated constraints, SHACL coverage, and migration safety. |
| ontogate | CI validation of RDF instances against pinned ontologies and SHACL shapes before graph/RAG ingestion. | Verify deterministic validation, shape pinning, and actionable failure reports. |
| @t2kai/core | Portable typed contracts for graph, claim, decision, policy, execution, observation, and learning; exact ontology-pack validation against JSON Schema. | Verify contract completeness, compatibility, and implementation maturity. |
| arras | Embeddable Python ontology interface, React operator console, graph browser, read-only GraphQL console, declared-action operator surface, and MCP stdio server. | Review action authorization, read-only guarantees, and operator-console security. |
| MAW (Model Assessment Wizard) | Ontology evaluation, visualization, missing-information identification, and constraint-update workbench. | Verify assessment methodology, traceability, and update controls. |

The proposal also names open-ontologies for formal ontology change planning, rollback, blast-radius reporting, and checkable disagreement/refutation proofs. Any use in a public UNIVERSALIS component requires source, license, proof-soundness, compatibility, and security review. Its proposed C2O-private governance use is documented only as a boundary reference; no C2O private authority model is to be copied into UNIVERSALIS.

### Encyclopedias — ingestion, indexing, citation integrity, knowledge graphs

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| olo-commons | Open verifiable knowledge base from open sources, with provenance and license per fact; proposal notes trust/time status. | Verify source licensing, update cadence, fact status semantics, and API terms. |
| Flexible GraphRAG | Document pipelines (Docling, LlamaParse, LiteParse), graph construction, ontology/schema support, hybrid search, and Langflow components. | Evaluate extraction accuracy, data egress, component licensing, and provenance. |
| myKG | Confidence-scored graphs from mixed document formats grounded in induced RDFS/OWL ontology. | Validate confidence calibration, extraction error rates, and ontology quality. |
| llmwiki | Persistent citation-traced Markdown wiki from URLs, files, and session exports, with typed pages and source-line citations. | Verify line-level citation stability, versioning, and source preservation. |
| stoa | Personal-context layer that builds a cited wiki and knowledge graph from files, with hybrid retrieval and MCP; described as Apache-2.0 and self-hostable. | Consider only for independently controlled, appropriately scoped deployments; verify license, data isolation, access controls, and deletion/export behavior. Do not use it to transfer private C2O context into public UNIVERSALIS. |

### Powers — measurement, permissions, evaluation

- Capability conformance harnesses are proposed for behavioral measurement and evaluation.
- Human and synthetic-agent permissions must be represented as explicit contracts, not inferred from capability declarations or test success.
- C2Cognitive is identified in the owner-supplied research as a private C2O bounded-authority candidate. It is not an assumed UNIVERSALIS dependency; any public alternative requires independent design and review.

### Skills — manifests, sandboxing, execution verification

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| SkillSandbox | Capability-based runtime in which skills declare needs and execution is enforced with structured audit trails. | Proposed primary open UNIVERSALIS enforcement candidate; verify license compatibility, escape resistance, OS support, and policy semantics. |
| hackmyagent | Security scanner, red-team toolkit, behavioral simulation, and skill builder with governance/manifest/security metadata. | Review generated permissions, default policies, and false-negative rates. |
| Cisco DefenseClaw | Skills scanning and sandboxing within a broader defense platform. | Verify integration boundaries, license/availability, and telemetry/privacy. |
| Sandlock | Process-level sandboxing alternative. | Compare OS support, isolation strength, policy model, and audit output. |
| SandyClaw (Permiso Security) | Dynamic skill analysis and multi-engine verdict infrastructure. | Identified primarily for C2O private vetting; any UNIVERSALIS use requires separate license, privacy, and deployment review. Do not assume shared deployment. |

### Capabilities — APIs, contracts, SDKs, conformance

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| @continua-ai/wheelie-capability-core | TypeScript SDK/testkit for making local tools, apps, or services safely agent-callable through capability contracts. | Verify contract model, local execution behavior, and test coverage. |
| dummy-a2a | Programmable A2A 1.0 test agent for client behavior, extension negotiation, artifact tagging, required extensions, and multi-extension activation. | Validate protocol version and conformance fixtures. |
| Agent Conformance Testing | Shared YAML behavioral specifications executed by language-specific Genkit Agent harnesses. | Verify test neutrality and cross-language parity. |
| agentic-dataset-conformance | Four-method contract: load_world, capabilities, step, reset; treats self-reported capabilities as claims to verify. | Validate environment determinism and conformance semantics. |
| @absolutejs/agent-conformance | Provider-neutral adversarial conformance for agent security, A2A, MCP, Arazzo, WebMCP, credentials, delegations, and spend mandates. | Verify standards coverage, threat model, and test validity. |
| @openwop/openwop-conformance | Multi-Agent Workflow Orchestration Protocol tests, including MCP redaction invariants and SSRF/body-size-cap advertisement contracts. | Verify protocol scope and adversarial test coverage. |

### Knowledge — persistence, retrieval, provenance, correction

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| compiled-memory / agent-knowledge | Compiles conversations, documents, and decisions into a provenance-bearing knowledge base with confidence and contradiction detection. | Verify source attribution, confidence semantics, and correction/deletion. |
| MNEME | Agent-writable knowledge graph with provenance categories and confidence as first-class fields. | Verify write authorization, provenance integrity, and graph consistency. |
| HELM | Hierarchical epistemic memory with logged read/write/consolidate/prune operations and provenance/epistemic state. | Verify lifecycle semantics and audit completeness. |
| Pythia | Continuous claim extraction, provenance/time, stale/contradictory knowledge detection, push hooks, and MCP access. | Candidate shared research fabric only after connector, correction, data-boundary, and license review; no private C2O data may flow into open services. |

### Human repositories — consent, accessibility, privacy, human-centered assessment

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| Prufa / prufa-mcp | Web-application audits for broken flows, console errors, tracking, consent, security headers, mobile tap targets, and accessibility, with graded findings. | Verify audit coverage, scoring methodology, false positives, and evidence reproducibility. |
| PAISL (Personal AI Sovereignty Lab) | Local-first benchmark scaffold for privacy, autonomy, consent, usefulness, explainability, data minimization, and overreach containment. | Verify benchmark validity and independent evaluation. |
| AI Workflow Privacy Compliance Review Agent | Editorial privacy/compliance triage with escalation for jurisdiction-specific advice. | Treat as triage, not legal determination; verify jurisdiction handling and escalation. |

Human-facing deployments require explicit consent, accessibility review, privacy minimization, independent verification, and clear human override.

## 4. UNIVERSALIS open immersive VR/AR layer

The target is an open-source, WebXR-native, independently deployable immersive substrate. It must degrade gracefully to standard screens and remain cross-device.

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| XARP (XR Agent-ready Remote Procedures) | Python toolkit exposing XR capabilities to agents through callable tools and MCP. | Verify protocol surface, device coverage, security, and project/license maturity. |
| Meta Immersive Web SDK (IWSDK) | Open-source MIT WebXR framework based on Three.js and ECS for browser 3D/VR/MR scenes; proposal notes agent-assisted workflow and gaze/pinch preparation. | Verify current SDK release, browser/device support, API stability, license, and accessibility. |
| NWO MR | Mixed-reality layer for robotics and AI agents, avatars, simulation, and virtual-world participation. | Verify source, license, supported platforms, and physical/virtual safety boundaries. |
| Agent Hands (Google xrblocks) | WebXR/Three.js agent hands and spatial control panel, with desktop simulator and Android XR support described. | Verify source, device compatibility, interaction safety, and license. |
| incarna | WebXR / Meta Quest 3 3D avatar embodiment for agent interaction. | Verify project maturity, identity/security model, and data handling. |

### Spatial knowledge-graph visualization

| Candidate | Proposed responsibility | Review required |
|---|---|---|
| @unrdf/spatial-kg | WebXR-enabled 3D navigation of RDF knowledge graphs across headsets, AR, and screens. | Verify graph scale, accessibility, interaction semantics, and query provenance. |
| Constellation | Turns Markdown vaults into 3D knowledge graphs with Vision Pro gaze/pinch interactions. | Verify supported vault formats, privacy/locality, and device compatibility. |
| VisionFlow | GPU-accelerated 3D knowledge graphs with agent orchestration and OWL 2 EL reasoning via Whelk. | Verify reasoning soundness, source, performance, and security. |
| LogseqXR | WebXR visualization for Logseq knowledge graphs with integrated AI services. | Verify integration boundaries, source, license, and data locality. |

### Spatial procedural verification

- OpenEye (@dumbspacecookie/openeye) is proposed as a thin device-side layer that captures camera views, runs a tool-using agent to verify procedure steps, and uses Groq Llama vision for scene understanding.
- Review consent, camera permissions, data minimization, on-device versus remote processing, false acceptance/rejection, safety-critical limitations, and human confirmation before any deployment.

## 5. C2O–UNIVERSALIS bridge candidates

The proposal identifies kaptyorka, NeuralBridge, OllaBridge, AIBridge, linco-bridge, and Crow as candidates for cross-environment agent/session connectivity, data-source adapters, model routing, private mesh routing, client connectors, and modular MCP integration.

Proposed integration architecture:
- A versioned MCP server for scoped tool invocation.
- A versioned A2A endpoint for agent-to-agent delegation.
- Published interface schemas in the shared integration repository.
- Conformance tests against shared contracts.
- Authentication and authorization at the boundary; explicit scopes, expiry, revocation, and audit records.
- No C2O private credentials, policies, authority tokens, or private operational state in public UNIVERSALIS repositories or artifacts.
- Runtime-negotiated interfaces must not imply implicit trust or bypass C2O authorization.

Each bridge candidate requires independent source, license, security, protocol, and data-flow review. None is selected by this proposal.

## 6. Requirement-to-evidence mapping

| Requirement | Proposed evidence mechanism |
|---|---|
| Source code in owning ecosystem repository | Separate repository ownership and versioned boundary interfaces. |
| Documented specification | Ontology contracts, capability contracts, and shared conformance specifications. |
| Automated tests | Agent, A2A, MCP, capability, and workflow conformance harnesses. |
| Security and dependency review | repo-assurance, hardened actions, dependency review, and evidence collection. |
| Execution and verification records | Normalized security/test/provenance artifacts and structured sandbox audit trails. |
| Version and provenance information | SLSA provenance, cosign signing, immutable releases, source and dependency manifests. |
| Limitations and outstanding work | Explicit abstention, conformance-as-claim, missing-information reports, and unresolved findings. |

## 7. Proposed seven-step execution order

1. Audit each repository's existing state: workflows, tests, dependencies, permissions, secrets exposure, schemas, provenance, visibility, and current evidence.
2. Map existing and missing tools by repository responsibility.
3. Produce a repository-specific implementation plan with dependencies, boundary impact, risk, cost, and acceptance tests.
4. Implement the highest-priority missing capability in its owning ecosystem repository.
5. Execute tests, security checks, conformance, and independent verification.
6. Record execution evidence, limitations, versions, and provenance in the corresponding research repository.
7. Continue from foundation to domain-specific verification and only then to immersive capabilities.

## 8. Adoption and evidence gates

- All tools and product descriptions in this document are owner-supplied research candidates as of 2026-11-12.
- Their existence, current release, license, maintainer, maintenance state, security posture, compatibility, advertised features, and benchmark claims require primary-source verification.
- A candidate is not approved, installed, implemented, tested, or verified merely because it appears here.
- Adoption requires a documented decision, source/license review, threat model, data-flow assessment, compatibility test, owner assignment, rollback plan, and repository-backed implementation evidence.
- Do not deploy a uniform stack indiscriminately. Select tooling according to repository responsibility and risk.
- Preserve the distinction between proposed, documented, implemented, tested, verified, failed, and unresolved.

## 9. Relationship to companion record

The C2O counterpart records private FatherThread assurance and governance responsibilities. Its private details are not reproduced here:
[Research for the C2O Ecosystem](https://github.com/C2O-Chaos-to-Order/Research-for-the-C2O-Ecosystem).
