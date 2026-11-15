# UNI-DP-10 — Meta-Research Architecture: Evidence Graphs, Claim Verification and Reproducible Synthesis
## v0.1.0 — UNIVERSALIS public research specification

**Status:** Proposed public domain pack — pending review  
**Date:** 2026-11-15  
**Boundary:** Public tools, public research and portable non-sensitive schemas only  
**Implementation:** Not performed

## 1. Purpose

This pack defines the cross-domain research layer for UNIVERSALIS. It is not a new subject-specific tool. It describes interoperable capabilities for source discovery, evidence assembly, claim verification, systematic synthesis, persistent research state and offline audit.

The five lifecycle operations are:
1. DISCOVER — find sources and capture what they claim;
2. ASSEMBLE — connect claims, source fragments, methods, results and gaps;
3. VERIFY — assess atomic claims against exact pinned evidence and source attribution;
4. SYNTHESIZE — conduct protocol-driven reviews and combine evidence only where justified;
5. AUDIT — independently replay research and decision records.

PERSIST is a cross-cutting substrate supporting every operation, not a separate sequential phase.

These are recurring architectural primitives in the candidate projects surveyed, not a claim of formal field-wide consensus or of one system implementing every primitive.

## 2. Architecture primitives

### Evidence graph
A typed, versioned graph connects questions, source records, captured bytes, fragments, claims, evidence relationships, methods, datasets, runs, decisions, reviews, reports and corrections.

Recommended edge types: CITES, CAPTURED_AS, CONTAINS_FRAGMENT, ASSERTS, SUPPORTS, REFUTES, QUALIFIES, DERIVED_FROM, TESTED_BY, PRODUCED, REVIEWED_BY, SUPERSEDES, CORRECTS, DEPENDS_ON and DISPUTES.

Each evidence relationship binds the exact source capture and fragment, claim version, relation stance, method and limitations. NLI/embedding scores assist navigation and triage; they are not truth or causal proofs.

### Research Ledger
Persists the question, scope, protocol, searches, inclusion/exclusion decisions, claims, sources, supported/unresolved states, contradictions, gaps, methods, runs, results, reviews, decisions, corrections and next actions.

Suggested claim workflow dispositions: DISCOVERED, EXTRACTED, ASSESSED, SUPPORTED, CONTRADICTED, NOT_ESTABLISHED, UNRESOLVED, SUPERSEDED and WITHDRAWN. These are workflow states, not universal truth categories.

### Claim-level verifier
Decomposes outputs into scoped propositions, routes each claim to its exact attributed source, verifies support independently from attribution, and emits a per-claim packet.

Verdicts:
- SUPPORTED — evidence supports the claim under declared scope;
- CONTRADICTED — evidence conflicts with the claim under declared scope;
- NOT_ESTABLISHED — supplied evidence does not establish it.

Separate attribution verdict:
- CORRECT_SOURCE;
- WRONG_SOURCE;
- SOURCE_UNRESOLVED;
- NOT_APPLICABLE.

A claim can be factually supported somewhere yet incorrectly attributed. Source identity must remain attached through decomposition and synthesis.

### Systematic-review pipeline
A research protocol, search, deduplication, screening, extraction, risk-of-bias appraisal, synthesis and transparent reporting pipeline with human checkpoints and reproducibility artifacts.

### Offline audit
A portable Research Artifact Bundle contains manifest, source captures, graph, ledger, methods, run data, verification packets, review decisions, signatures and offline verifier. Independent auditors re-derive defined decisions from pinned inputs rather than trusting a rendered report.

### Persistent substrate
Versioned records, content-addressed artifacts, queryable knowledge graphs, correction history, export/import and local/offline options. Local-first does not automatically establish security.

## 3. Research lifecycle

| Operation | Output | Required control |
|---|---|---|
| Discover | Source records, captures, exact fragments, search logs | Declared scope and reproducible search |
| Assemble | Evidence graph, research ledger, contradiction/gap register | Typed relationships and source-specific provenance |
| Verify | Claim packets and attribution decisions | Exact evidence capture and scoped verdict |
| Synthesize | Protocol-led narrative or justified quantitative synthesis | Eligibility, appraisal, human checkpoints, uncertainty |
| Audit | Offline audit packet, replay result and discrepancies | Hash/signature verification and re-derived decisions |

The lifecycle is iterative. A correction, retraction or newly discovered contradiction can reopen any earlier stage. The report is a generated view, not the authoritative research-state store.

## 4. Core portable schemas

**SourceCapture:** source URI/version, final URI, exact bytes or lawful immutable representation, digest, retrieval timestamp/method, fragment locators, license/access constraints and limitations.

**EvidenceGraphRecord:** typed nodes/edges, stable identifiers, source capture and fragment references, claim version, relation method, scope, limitations and graph version.

**ResearchLedgerRecord:** question/protocol, searches, inclusion/exclusion, claim state, contradictions/gaps, evidence links, run/decision history, correction links and next actions.

**ClaimVerificationPacket:** atomic claim/version, exact cited source and pinned evidence, claim-support verdict, separate attribution verdict, method/verifier version, assumptions, uncertainty, limitations, reviewer and correction references.

**SystematicReviewRecord:** protocol, eligibility criteria, search strategy, screening decisions, extraction data, appraisal, synthesis model, deviations, human checkpoints, reporting coverage and reproducibility inputs.

**ResearchArtifactBundle (ARA-compatible):** manifest, graph, ledger, source captures/references, run inputs/outputs, verification packets, reviews, signatures, dependencies and replay instructions. XScientist's ARA is a candidate external format, not adopted as a formal standard by this pack.

**OfflineAuditPacket:** manifest and artifact digests, signer/public key references, verification algorithms, event order, verifier version, recomputation output, missing inputs and final audit disposition.

## 5. Systematic review and meta-analysis

Recommended stages:
1. define question and scope;
2. establish and version a protocol;
3. define eligibility criteria, outcomes and planned analysis;
4. search and document sources, dates and queries;
5. deduplicate and screen, retaining reasons;
6. extract structured study data;
7. assess risk of bias using domain-appropriate methods;
8. synthesize narratively or quantitatively as justified;
9. assess certainty/limitations where an appropriate framework exists;
10. report results and provide reproducibility artifacts.

PRISMA 2020 is a reporting guideline with a 27-item checklist and flow diagrams. It is not a complete systematic-review conduct methodology and is not a risk-of-bias or methodological-quality instrument. Use suitable methods for conduct, appraisal and certainty assessment in addition to PRISMA.

A composite corpus QualityScore may be exploratory diagnostics only. Disclose components, weights, normalization, missingness, calibration and validation. It cannot replace eligibility adjudication, risk-of-bias assessment, certainty grading or human expertise.

Quantitative pooling is conditional on compatible designs, populations, interventions/exposures, outcomes and estimands. Preserve extraction tables, effect-size definitions, variance, statistical model, heterogeneity, sensitivity analysis, uncertainty and protocol deviations. Do not pool incompatible evidence because a pipeline supports it.

## 6. Public candidate-tool map

### Discover
- Argus — shared evidence-graph navigation and evidence-gap-directed search.
- Dossier — owner-supplied research-ledger approach; exact source remains unpinned.
- Lyra — local MCP research with evidence graph and NLI stance.
- DuMate-DeepResearch — recursive, graph-planned research and traceable tool calls.
- DAGent — incremental evaluate-then-grow research graph.

### Assemble
- Lyra, Argus and Dossier — evidence graph and ledger patterns.
- Xcientist — evidence graph spanning literature, methods, experiments and claims.
- XScientist — git-like exploration graph and Agent-Native Research Artifact.

### Verify
- ProvenanceGuard — source-aware claim verification and cross-source attribution checks.
- agent-evidence-verify / Probity — unpinned offline decision-packet candidate.
- vivory-mcp-verification — unpinned broad source-registry MCP candidate.
- Janus — signed, hash-chained, offline-verifiable action provenance research.

### Synthesize
- PARIS — PRISMA-oriented multi-agent review prototype.
- meta-pipe — unpinned end-to-end SR/MA candidate.
- LUMEN — unpinned cost/quality SR/MA candidate.
- AgentSLR — research pipeline evaluated across nine WHO priority pathogens.
- MedSR-Copilot — medical systematic-review copilot preprint and code.
- nexus-scholar — unpinned research harness/toolkit candidate.

### Persist
- wiki-vault — typed research-artifact graph and BM25 search.
- Scholar Agent — unpinned local research-card/LLM-Wiki candidate.
- ZotSeek — local Zotero semantic search with opt-in read-only MCP interface.
- XScientist ARA — candidate portable research-state package.

### Audit
- Janus — offline-verifiable event/decision chain research.
- ProvenanceGuard — source-specific attribution verdicts.
- XScientist/ARA — portable graph and artifact provenance.
- SPOTTER-AI — early-phase scientific workflow provenance/threat-tracing project.
- AAR standard, YAML metaprompt framework and MACP — unpinned owner-supplied candidates, not adopted standards.

## 7. Performance claims and evaluation discipline

Published papers report strong task-specific results for Argus, DuMate, DAGent, Xcientist, ProvenanceGuard, Janus, AgentSLR, MedSR-Copilot and PARIS. These results are not comparable by a common scale and do not transfer automatically to other domains or workloads.

Every reported result must preserve:
- exact paper/version and date;
- benchmark and split;
- tested system/model and configuration;
- task count and sample size;
- prompt/tooling and search budget;
- grader/ground truth and human involvement;
- metric definition and uncertainty;
- baseline and replication status.

Preprint and project claims must be labelled. An internal reviewer agent is not independent human validation. A high benchmark score is not evidence that an individual research claim is supported.

## 8. Public sources and qualification

- Argus: https://arxiv.org/abs/2605.16217
- Lyra preprint/software record: https://zenodo.org/records/18222598 ; code link on record: https://github.com/k-shibuki/lyra
- DuMate/Qianfan: https://github.com/baidubce/qianfan-deepresearch ; paper page: https://huggingface.co/papers/2606.07299
- DAGent: https://arxiv.org/abs/2609.39154
- Xcientist: https://arxiv.org/abs/2606.18874
- XScientist: https://arxiv.org/abs/2607.12301 ; https://github.com/smileformylove/XScientist
- ProvenanceGuard: https://github.com/aalvsz/provenanceguard
- Janus: https://arxiv.org/abs/2609.38266
- AgentSLR: https://arxiv.org/abs/2603.22327
- MedSR-Copilot: https://www.medrxiv.org/content/10.64898/2026.07.30.26359375v2.full ; https://github.com/MAGIC-AI4Med/MedSR-Copilot
- PRISMA 2020: https://www.prisma-statement.org/prisma-2020 ; https://doi.org/10.1186/S13643-021-01626-4
- wiki-vault: https://github.com/yogsoth-ai/wiki-vault
- ZotSeek: https://github.com/introfini/ZotSeek ; MCP guide: https://github.com/introfini/ZotSeek/blob/main/docs/MCP.md
- SPOTTER-AI project phase: https://grc.iit.edu/research/projects/spotter-ai/

Dossier, agent-evidence-verify, vivory, meta-pipe, LUMEN, nexus-scholar, Scholar Agent, AAR, YAML metaprompt framework and MACP require canonical source/version pinning before adoption.

## 9. Boundary

UNIVERSALIS uses public tools and open interfaces that can run independently. Portable schemas are public and do not require C2O credentials, private policy engines, keys or internal authority services.

This pack contains no private C2O operational data, case records, credentials, target scopes, policy configuration or private control details.

## 10. Validation requirements — proposed, not executed

1. Bind each report claim to atomic claim version(s).
2. Resolve every support/refute edge to an exact source capture and fragment.
3. Check attribution separately from support.
4. Preserve contradictions, qualifications and gaps.
5. Test cross-source conflation.
6. Propagate retractions and source corrections to dependent results.
7. Replay ledger from ordered events under fixed rules.
8. Export/import a portable research bundle without the originating session.
9. Distinguish PRISMA reporting coverage from review conduct quality and risk of bias.
10. Require attributable human decisions at inclusion/corpus/synthesis checkpoints.
11. Recompute quantitative synthesis from pinned extraction and analysis artifacts.
12. Reject offline audit PASS where required bytes, keys or verifier versions are absent.
13. Report nondeterminism and unsupported assumptions.
14. Test local tool data flows, permissions, secrets, dependencies and egress.
15. Preserve negative results and failed research branches.
16. Keep execution/evidence/review/owner acceptance/release statuses distinct.

No tests or experiments have been executed.

## 11. Status and limitations

This is a proposed public research architecture, not a deployed meta-research platform or a declaration that any candidate meets all requirements. Project metrics are source-reported and may be preprint or maintainer claims. Tool licenses, dependencies, data flow, security and maintenance require further review. No implementation, benchmark, systematic review, meta-analysis, offline audit, legal review, or independent security assessment was performed.

---

**End of UNI-DP-10 v0.1.0**
