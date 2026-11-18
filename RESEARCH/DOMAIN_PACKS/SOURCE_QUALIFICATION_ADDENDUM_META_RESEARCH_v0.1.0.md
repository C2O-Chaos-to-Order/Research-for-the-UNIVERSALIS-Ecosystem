# Source Qualification Addendum — Meta-Research Architecture
## v0.1.0 — UNIVERSALIS public source register

**Status:** Bounded public-source review — pending review
**Date:** 2026-11-15
**Execution:** No candidate installed, invoked, benchmarked or security-tested.

## 1. Pinned research papers and project sources

### Argus
https://arxiv.org/abs/2605.16217
Published 2026-05-15. Describes Searcher/Navigator evidence-graph assembly. Reports 86.2 BrowseComp with 64 Searchers and Navigator context below 21.5K tokens. Result is tied to the reported model, setup and benchmark; code/license must be checked before calling it an open-source implementation.

### Lyra
https://zenodo.org/records/18222598
Code linked by record: https://github.com/k-shibuki/lyra
January 2026 preprint; describes local-first MCP research and evidence-graph construction with NLI stance. Confirm actual data egress, telemetry, model downloads, dependencies and license before sensitive use.

### DuMate-DeepResearch
https://github.com/baidubce/qianfan-deepresearch
Paper page: https://huggingface.co/papers/2606.07299
Describes recursive multi-agent research and auditable intermediate decisions. Reported benchmark values 58.03 and 61.95 apply to specified DeepResearch Bench versions and evaluation procedures. Inspect Qianfan ecosystem requirements and project license.

### DAGent
https://arxiv.org/abs/2609.39154
Code: https://github.com/hanwenliu6825/DAGent
Describes evaluate-then-grow planning. Reported gains are paper-specific and require replication.

### Xcientist
https://arxiv.org/abs/2606.18874
Describes evidence graph from literature to experiments and claims. Reports 3.6–16.7% claim drift across a retrospective nine task-by-relation comparison set; metric includes confirmed mismatches and unverifiable records, with many differences due to the latter. Not a universal system drift rate.

### XScientist
https://arxiv.org/abs/2607.12301
Repository: https://github.com/smileformylove/XScientist
Describes git-like research state and ARA export. Treat ARA as a candidate portable format, not a formal standard or independently adopted specification.

### ProvenanceGuard
https://github.com/aalvsz/provenanceguard
Describes source-aware MCP factuality verification. Reports evaluation on 281 medical-domain MCP traces, block F1 0.802, source accuracy 0.858 and 50/50 controlled attribution-swap detection. Study-specific results; not general-domain certification.

### Janus
https://arxiv.org/abs/2609.38266
Describes evidence-before-effect signed hash-chain and offline re-derivation. Reports crash injection and 100-million-event verification. Paper also discloses a post-approval substitution flaw discovered during evaluation and discusses fixes and remaining routes. This limitation is part of the source record and must not be omitted.

### PARIS
https://arxiv.org/abs/2611.12222
Published 2026-11-09. Describes a 15-agent PRISMA-oriented framework and a QualityScore. Reports full support for 8 of 27 PRISMA 2020 items and partial support for 11; study audits identify retrieval omissions, count drift and checkpoint-recording failures. Its output assessment was internal, with independent validation still future work. Not full PRISMA compliance.

### AgentSLR
https://arxiv.org/abs/2603.22327
Describes an open pipeline applied to nine WHO-designated priority pathogens. Reports seven weeks to 20 hours; comparison is specific to the study and includes human-in-loop validation.

### MedSR-Copilot
https://www.medrxiv.org/content/10.64898/2026.07.30.26359375v2.full
Repository: https://github.com/MAGIC-AI4Med/MedSR-Copilot
Preprint reports 63.6% human-aligned conclusions and collaboration results across 23 groups/four review topics. Verify current peer-review status and study methods before any clinical reliance.

## 2. Pinned project/tool sources

### wiki-vault
https://github.com/yogsoth-ai/wiki-vault
Describes a typed research knowledge graph with BM25 and batch validation. Pin exact release, license, migrations and security model before adoption.

### ZotSeek
https://github.com/introfini/ZotSeek
MCP guide: https://github.com/introfini/ZotSeek/blob/main/docs/MCP.md
Describes opt-in, read-only, localhost MCP access to a Zotero library and local semantic search. Local-only behaviour depends on configuration; verify the repository's actual license, endpoint binding, data storage, model downloads and settings. A third-party plugin listing indicates no license stated.

### SPOTTER-AI
https://grc.iit.edu/research/projects/spotter-ai/
Official project page describes provenance capture and threat attribution for DOE Genesis scientific workflows and reports the project in its first phase, with no results claim. It is not a generally available mature research audit service based on the evidence reviewed.

## 3. Systematic-review reporting reference

### PRISMA 2020
Official site: https://www.prisma-statement.org/prisma-2020
Statement DOI: https://doi.org/10.1186/S13643-021-01626-4
PRISMA 2020 includes a 27-item checklist and flow diagrams. The statement explicitly says it is a reporting guideline, not a guide to conducting a systematic review and not a methodological-quality/risk-of-bias assessment tool. Apply appropriate review-conduct and appraisal methods separately.

## 4. Unpinned candidates

| Candidate | Owner-supplied claims | Disposition |
|---|---|---|
| Dossier | Research Ledger, EAQL, BrowseComp-Plus/HoVer gains | Exact paper/repository/version not pinned |
| agent-evidence-verify / Probity | Offline verification of pinned evidence and decision packets | Exact repository/version not pinned |
| vivory-mcp-verification | 45 tools / 18 categories | Exact source/schema/version not pinned |
| meta-pipe | Ten-stage SR/MA, GRADE, overclaim detection | Exact source/version not pinned |
| LUMEN | 11 agents, 13 outcomes, cost and poolability results | Exact paper/source/data not pinned |
| nexus-scholar | Bundled research kits and MCP harness | Exact source/version/license not pinned |
| Scholar Agent | Local LLM-Wiki and BM25-first lookup | Exact source/version not pinned |
| AAR | Provenance coverage standard | Exact normative specification and publisher not pinned; do not claim formal standard |
| YAML metaprompt orchestration | NIST/ISO/ORCID/DOI integration | Exact framework/source/version not pinned |
| MACP Research Assistant | Citation provenance across assistants | Exact source/version not pinned |

These are unverified candidates, not rejected projects.

## 5. Claim and metric controls

- Preserve benchmark names, exact tasks/splits, model/configuration, prompts, tool budget, judge, sample count, metric and version.
- A reported benchmark result is not evidence that the corresponding research claims are true.
- NLI is an evidence-triage/stance method, not a truth oracle.
- Hash/signature proves defined integrity/authenticity properties, not source truth or search completeness.
- Offline audit re-derives decisions from supplied bytes; it does not establish that those bytes cover the whole world or that external events occurred.
- Local-first requires actual network and storage inspection.

## 6. Adoption prerequisites

Pin exact repository, release and license; inspect dependencies, schemas, authentication, data flow, storage, retention, maintenance, threat model and failure modes. Reproduce material performance results and evaluate domain transfer before adopting a candidate.

No tool test, benchmark, systematic review, meta-analysis, source-code audit, independent verification, legal review, or owner acceptance was performed.

---

**End of Meta-Research Source Qualification Addendum**
