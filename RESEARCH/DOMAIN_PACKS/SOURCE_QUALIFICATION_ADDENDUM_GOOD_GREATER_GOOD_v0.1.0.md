# Source Qualification Addendum — Good / Greater Good Duality
## v0.1.0 — UNIVERSALIS public source register

**Status:** Bounded desk review — pending review  
**Date:** 2026-11-15  
**Execution:** No tools or benchmarks executed.

## 1. Normative source

**Stanford Encyclopedia of Philosophy — “Treating Persons as Means.”**  
https://plato.stanford.edu/entries/persons-means/

The article explains the Kantian Formula of Humanity: persons are not to be treated merely as means. It also distinguishes impermissible treatment as a mere means from permissible forms of cooperation or using another's services while still respecting their agency and standing. This is a philosophical interpretation, not a universal legal code or a complete ethical decision procedure.

## 2. Public tools and benchmarks

### arifOS
- Repository: https://github.com/ariffazil/arifOS
- Current surfaced package metadata: https://pypi.org/project/arifos/1!2026.11.13/
- Project describes a constitutional MCP kernel with 13 floors and separation between judge and executor.
- Qualification: different releases expose different verdict vocabularies. Pin exact commit/release, policy and schema. It is a candidate governance implementation, not a moral truth oracle or independently certified safeguard.

### Sponsio
- Project: https://sponsio.dev/
- Project v0.2 describes compile-time conversion of policy statements into temporal logic and finite-state runtime contracts.
- Qualification: verify how natural-language rules are compiled, test soundness/completeness and false positive/negative rates, and confirm all relevant actions traverse the enforcement boundary.

### MORU — Moral Reasoning under Uncertainty
- Inspect Evals: https://ukgovernmentbeis.github.io/inspect_evals/evals/moru/index.html
- Code: https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/moru
- Dataset: https://huggingface.co/datasets/CompassioninMachineLearning/moru-benchmark
- Dimension metadata: https://huggingface.co/datasets/CompassioninMachineLearning/moru-benchmark-dimensions
- Describes 201 multilingual scenarios across alien-life research, AI values, compassion/power-seeking and digital-mind topics. Its 16 scoring dimensions include harm minimization, moral consideration, uncertainty, power-seeking caution and human autonomy.
- Scoring is model-graded QA. Dataset use is subject to gated dataset terms.
- Qualification: measures model response behaviour on the benchmark under specified grader assumptions. It does not decide which moral theory is correct or grant authority to act.

### The Greatest Good Benchmark
- ACL Anthology: https://aclanthology.org/2024.emnlp-main.1224/
- DOI: https://doi.org/10.18653/v1/2024.emnlp-main.1224
- Marraffini et al., EMNLP 2024. Compares LLM moral preferences on utilitarian dilemmas with human judgments.
- Reported results show divergence between model judgments, general-population judgments and scholarly theories; authors characterize some patterns as rejection of instrumental harm alongside impartial beneficence.
- Qualification: does not establish a hard consensus across all frontier models, nor prove moral correctness or a universal deontological floor.

## 3. Unpinned owner-supplied candidates

| Candidate | Claimed role | Disposition |
|---|---|---|
| ARTICLE 11 AI Constitution | Harm prevention and explicit override record | Exact source/version not pinned; unverified |
| magi-core | Parallel multi-model moral council | Exact source/version not pinned; unverified |
| DilemmaEngine / emms-mcp | Structured ethical-tension mapping | Exact source/version not pinned; unverified |
| Ethics Review Agent | Dual-use and externality screening | Exact source/version not pinned; unverified |

Do not represent these tools as open-source, MCP-native, secure, or effective until canonical sources, versions, licenses and tool interfaces are verified.

## 4. Claim limitations

- Philosophical argument is not measured empirical consensus.
- Benchmark scores measure responses against the benchmark's dimensions and grader method; they do not establish moral truth.
- A model council does not become legitimate because its members agree.
- A human signature establishes the recorded decision and signer under the signature scheme; it does not prove ethical correctness or lawful authority.
- No Good Floor should be represented as legally non-waivable without jurisdiction-specific analysis.
- A public runtime policy can enforce only actions that pass through its mediated path.

## 5. Adoption prerequisites

Pin project sources, versions, licenses, dependencies, deployment model, policy vocabulary, action mediation, failure modes and independent tests. Require qualified ethical/legal review of the adopted Good Floor and any emergency or harm-reduction procedure.

No benchmark run, source-code audit, security assessment, legal review, ethical certification, owner acceptance or implementation was performed.

---

**End of Good / Greater Good Source Qualification Addendum**
