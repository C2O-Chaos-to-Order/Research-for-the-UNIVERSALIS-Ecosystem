# UNIVERSALIS Research Tool Landscape — 2026-11-12

**Status:** Owner-supplied research intake; candidate inventory, not an adoption decision.  
**Thread:** UNIVERSALIS OS / MotherThread.  
**Purpose:** Record file-system-native, composable research substrates and shared research-fabric candidates for evaluation before implementation.

## Placement rule

Research records, comparative analysis, rubrics, evidence, and adoption decisions belong in this research repository. Actual public UNIVERSALIS tools and reusable implementations must be built in `C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem`. Private C2O governance and authority tools belong in `C2O-Chaos-to-Order/The-C2O-Ecosystem`. Shared capabilities must be exposed through explicit, versioned, portable interfaces; public UNIVERSALIS components must not contain C2O private credentials, private policy, or authority state.

## MotherThread research-substrate candidates

| Candidate | Intended contribution | Initial assessment / validation required |
|---|---|---|
| FS-Researcher | Dual-agent research with a persistent hierarchical filesystem knowledge base; Context Builder archives sources and Report Writer synthesizes from notes. | Direct fit with disk-backed research. Validate artifact schema, resume semantics, source provenance, concurrent writes, and deletion/versioning. |
| DeerFlow | Open super-agent harness combining sub-agents, memory, sandboxes, and extensible skills. | Potential orchestration substrate. Verify current release, license, architecture, sandbox boundary, security posture, and claimed community/trending status. |
| PARNESS | Thin declarative DAG kernel, four-field agent contract, PDF corpus with typed figures/tables, knowledge graph, scenario-typed retrieval. | Strong composability candidate. Verify implementation, schema stability, parser quality, graph provenance, and extension compatibility. |
| chitta-research | Rust research OS with typed belief graph, hypothesis/experiment loop, confidence, and correction propagation. | Strong epistemic substrate concept. Validate graph semantics, confidence calibration, reconsolidation behavior, concurrency, and test coverage. |
| Research Vault | Delegated specialist crew with artifact-mediated coordination, citation traceability, and reviewer separation. | Candidate workflow pattern. Verify actual reviewer read-only enforcement, anti-self-review controls, source artifacts, and reproducibility. |
| AutoSearch | MCP-native multi-channel research retrieval decoupled from model and agent host. | Candidate sensory/retrieval adapter. Verify actual channel count and availability, API terms, rate limits, freshness, and per-source provenance. |
| Gigaxity Deep Research | MCP tools for search, discovery, synthesis, and reasoning with parallel retrieval, fusion, citations, and contradiction detection. | Candidate synthesis adapter. Verify six-tool contract, provider dependencies, fusion implementation, latency claims, and citation binding. |
| Harness Research | Asynchronous MCP deep research across multiple sources with credibility assessment and report generation. | Candidate long-running job pattern. Verify task persistence, timeout/retry semantics, CRAAP scoring validity, cost claims, and artifact retrieval. |
| Research OS (research-panel) | Project-local `.research/` substrate with canonical text files, SQLite index, CLI/TUI, extension, Python API, and MCP interfaces. | Very strong architectural fit. Validate canonical file schema, index rebuildability, provider independence, remote/HPC portability, and migration path. |
| Research MCP Server (Apify) | MCP research surface exposing web, academic, repository, news, and other live data tools. | Broad connector candidate. Verify exact 23-tool surface, actor dependencies, credential scope, source terms, and data handling. |
| NAVA | Deterministic personal-agent OS with secure workspace execution, deep research synthesis, and mutation gateway. | Application-layer candidate, not the base research substrate. Verify 12-step mutation controls, isolation, audit records, and portability. |

## Shared research-fabric candidates

These candidates can serve both ecosystems through explicit contracts. Their output is evidence input, not authority.

| Candidate | Intended contribution | Initial assessment / validation required |
|---|---|---|
| Caesar | Graph-based RAG, web exploration, adversarial verification, and multi-draft synthesis. | Verify published comparisons, source traceability, reproducibility, and package security. |
| Argus | Evidence assembly graph with Searchers and a Navigator that detects missing evidence and dispatches targeted retrieval. | Verify benchmark claims, scaling economics, graph completeness semantics, and failure handling. |
| CortexRAG | Research, processing, indexing, and synthesis with graph orchestration and knowledge-base construction. | Verify component replaceability, provenance, index reproducibility, privacy, and deletion behavior. |
| NVIDIA AI-Q Blueprint | Configurable shallow/deep research routing, parallel workers, job-scoped state, isolated tool execution, and evaluation. | Verify sandbox guarantees, data locality, provider dependence, operational cost, and evaluation portability. |
| DOVA | Multi-source academic and web retrieval, intent-weighted fan-out, DOI/citation verification. | Verify source coverage, identifier matching, API terms, citation precision, and credential isolation. |
| Pydantic Researchers | Lightweight, pluggable research loop using Pydantic AI agents. | Verify extension contract, dependency footprint, and upstream parity. |
| Panda Research Tools | Scholarly search, retraction/citation integrity, expert discovery, PDF table extraction, archival and trend tools. | Verify retraction freshness, source coverage, false-positive rates, and provenance. |

## Application-ecosystem candidates

| Candidate | Intended contribution | Destination / validation |
|---|---|---|
| Claw AI Lab | Configurable autonomous research teams as an interactive laboratory product. | Application layer; evaluate user control, provenance, reproducibility, and data isolation. |
| AMAR | Seven-agent academic research workflow from discovery through experiments and drafting. | Academic vertical; validate experiment isolation, source coverage, and authorship records. |
| Arbor Agent | Generalist CLI research using hypothesis-tree refinement, literature search, and novelty checks. | Installable application capability; validate novelty method, skill permissions, and evidence quality. |
| Paper2Agent | Converts papers into interactive agents. | Research-to-product pathway; require paper-to-code traceability, permissions, and sandboxing. |
| TrustResearcher | Knowledge-grounded multi-agent ideation. | Ideation application; validate grounding, novelty claims, and reviewer independence. |
| AI Research Toolkit | Local-first, skill-based workflows for coding-agent hosts. | Distribution layer; validate registry trust, provenance, and least-privilege execution. |

## UNIVERSALIS acceptance rubric — proposed, not yet adopted

A candidate should be assessed for:
1. **Filesystem-native persistence:** canonical inspectable files; restart/resume without hidden context.
2. **Composability:** modular agents, tools, storage, and model providers with documented contracts.
3. **Portability:** cross-device and cross-platform operation, including local, remote, and batch/HPC environments where applicable.
4. **Evidence provenance:** source artifacts, transformations, claims, and synthesis remain linked.
5. **Epistemic correction:** contradictions, retractions, and changed beliefs propagate to dependent claims.
6. **Interoperability:** open protocols and replaceable adapters; MCP is an interface option, not a mandatory runtime dependency.
7. **Security and privacy:** least privilege, sandboxed execution, credential isolation, and explicit data boundaries.
8. **Reproducibility:** versioned specs, parameters, environments, outputs, and verifiable manifests.

No weighted score or pass threshold is assigned in this intake. Define and approve the rubric before using it for selection or promotion.

## Evidence and decision status

- The descriptions and reported performance figures in this intake were supplied by the project owner on 2026-11-12.
- No primary repository, paper, license, security review, benchmark artifact, or reproducible run was attached to this intake.
- Therefore all candidates are **PROPOSED / UNVERIFIED**. Reported benchmark numbers and release claims are not accepted results.
- No candidate is approved, adopted, installed, or authorized for production by this document.
- Next research action: collect canonical source URLs and primary artifacts per candidate; verify existence, maintainers, licenses, release status, dependency/security posture, reproducibility, and fit against the rubric.
- Next implementation action occurs only after a documented selection: implement public UNIVERSALIS capabilities in the UNIVERSALIS ecosystem repository and record commit, tests, and verification evidence here.

## Cross-repository coordination

- UNIVERSALIS implementation destination: [The UNIVERSALIS Ecosystem](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem)
- C2O research counterpart: [Research for the C2O Ecosystem](https://github.com/C2O-Chaos-to-Order/Research-for-the-C2O-Ecosystem)
- C2O implementation destination: [The C2O Ecosystem](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem)


## Follow-up primary-source discovery — 2026-11-12

A first source-discovery pass found the following project-maintained repositories or primary papers. This confirms identifiable source material, not production readiness or independent validation of every reported result.

| Candidate | Source | What is supported at this stage |
|---|---|---|
| FS-Researcher | https://arxiv.org/abs/2602.01566 ; https://aclanthology.org/2026.acl-long.288/ ; https://github.com/Ignoramus0817/FS-Researcher | ACL Anthology paper and source repository describe a dual-agent filesystem workspace with persistent notes and archived raw sources. Benchmark superiority remains paper-reported pending reproduction. |
| DeerFlow 2.0 | https://github.com/bytedance/deer-flow | Official repository describes an open-source long-horizon agent harness with subagents, memory, sandboxes, tools and skills; v2 is a ground-up rewrite relative to v1. |
| PARNESS | https://arxiv.org/abs/2605.05258 ; https://github.com/gtrhythm/PARNESS | Paper and repository describe declarative DAG workflows, full-text PDF indexing, typed objects, and cross-run knowledge. Verify current implementation and license before adoption. |
| chitta-research | https://github.com/genomewalker/chitta-research ; https://research.vaklab.dev/ | Project repository and maintained overview describe a Rust research system with typed belief graph, agent loop and artifact provenance. Important qualification: README says reconsolidation is exposed as a library function and is not automatically called in the current agent loop; do not overstate automatic correction propagation. |
| Research OS (research-panel) | https://pypi.org/project/research-panel/ | Package description documents a project-local `.research/` substrate, canonical text records, SQLite index, CLI/TUI/API/MCP interfaces and remote/HPC support. Validate source repository, license, release integrity, and schema/migration constraints before adoption. |

Not located in this first pass: a sufficiently clear primary source for the specific FS-Researcher-adjacent claims beyond the cited paper, Research Vault, AutoSearch, Gigaxity, Harness Research, Apify Research MCP Server, and NAVA. Keep these entries unverified; absence from this limited search is not proof of nonexistence.

## Source discovery references
- FS-Researcher paper: https://arxiv.org/abs/2602.01566
- FS-Researcher ACL Anthology record: https://aclanthology.org/2026.acl-long.288/
- FS-Researcher repository: https://github.com/Ignoramus0817/FS-Researcher
- DeerFlow official repository: https://github.com/bytedance/deer-flow
- PARNESS paper: https://arxiv.org/abs/2605.05258
- PARNESS repository: https://github.com/gtrhythm/PARNESS
- chitta-research repository: https://github.com/genomewalker/chitta-research
- Research OS package: https://pypi.org/project/research-panel/
