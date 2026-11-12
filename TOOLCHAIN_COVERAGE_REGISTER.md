# Toolchain Coverage Register — UNIVERSALIS

**Date:** 2026-11-12  
**Scope:** Public UNIVERSALIS toolchain coverage for the original four toolchain documents plus the subsequently supplied Intelligence Capabilities document.  
**Boundary:** This public register does not link to C2O-private owner repositories or disclose private policies, model weights, benchmark datasets, credentials, or authority tokens.

## 1. Original four source documents

The original four public/open source areas remain inventoried in FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md:
1. Human Knowledge.
2. Powers / Energy Efficiency / Synergy.
3. Human Capabilities.
4. Mapping / Matrix / Organization / Ecosystem Mapping.

That register contains the full UNIVERSALIS candidate lists, functional notes, implementation status, and CI receipts. This document adds the fifth Intelligence Capabilities toolchain.

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
