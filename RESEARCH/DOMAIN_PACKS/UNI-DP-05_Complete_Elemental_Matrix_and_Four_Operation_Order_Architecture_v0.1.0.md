# UNI-DP-05 — Complete Elemental Matrix and Four-Operation Order Architecture
## Public research proposal v0.1.0

**Status:** Owner-supplied model recorded as a public research proposal; owner/reviewer disposition pending  
**Scope:** Elemental matrix, Essence/Quintessence distinction, open order-operation tools and portable contracts  
**Implementation status:** Not started  
**Test / simulation status:** Not executed  
**Release status:** Draft PR only; no merge or product adoption implied

---

## 1. Purpose

This document records the revised elemental hierarchy and its relationship to four distinct system operations:

1. Prevent Chaos — prevent disorder before action.
2. Find Order — diagnose order already present.
3. Presume Order — operate provisionally when evidence is incomplete.
4. Resume Order — restore safe operation after disruption.

The elemental hierarchy and four operations are complementary models. The four operations are lifecycle functions, not additional elemental tiers.

## 2. Complete owner-supplied hierarchy

| Tier | Count | Elements | Composition rule |
|---|---:|---|---|
| Primary | 5 | Air, Earth, Fire, Water, Spirit | Functional roles |
| Secondary | 10 | Lightning, Ice, Dust, Sound, Steam, Metal, Light, Nature, Life, Crystal | Two primaries coupled |
| Tertiary | 10 | Magma, Weather, Memory, Storm, Radiance, Dream, Blood, Forge, Growth, Soulfire | Three primaries coupled |
| Quaternary | 5 | Aether, Chaos, Void, Logos, Eros | Four primaries; one omitted |
| Quintessence | 1 | Unity | All five primaries integrated |
| Essence | ∞ | Every individual thing | Entity-level core nature/identity, not a combination tier |

For five distinct primaries:

\[
\sum_{k=1}^{5}\binom{5}{k}=2^5-1=31
\]

The 5 + 10 + 10 + 5 + 1 = 31 finite combination count is a mathematical identity. Names and semantic interpretations are ontology proposals, not scientific conclusions.

Essence is not an additional combination tier. The infinity symbol expresses an open-ended entity-level domain, not a proven cardinality of actual entities.

## 3. Matrix representation

Use the fixed primary vector order:

\[
[A,E,F,W,S]=[Air,Earth,Fire,Water,Spirit]
\]

Each combination is represented by a five-position indicator vector. A value of 1 means a primary participates; 0 means it is omitted.

The 31 combination rows are the non-empty subsets of the five primary columns. The exact composition vector and the name of the derived regime must be stored separately. Unity maps to [1,1,1,1,1]. Essence identifies the defining nature of an individual entity and is not another subset row.

## 4. Current proposed composition register

### 4.1 Primary roles

| Primary | Functional role |
|---|---|
| Air | Information and communication |
| Earth | Structure and constraint |
| Fire | Energy and transformation |
| Water | Flow and adaptation |
| Spirit | Integration, interpretation, observability and governance |

“Awareness” is used operationally for observation and integration. It does not imply subjective experience or consciousness.

### 4.2 Secondary names and prior pair assignments

| Secondary | Previously proposed pair | Status |
|---|---|---|
| Lightning | Air + Fire | Proposed |
| Ice | Water + Earth | Proposed |
| Dust | Air + Earth | Proposed |
| Sound | Air + Spirit | Proposed |
| Steam | Fire + Water | Proposed |
| Metal | Earth + Fire | Proposed |
| Light | Fire + Spirit in the latest owner-supplied assignment | Current proposal; prior Air + Fire assignment remains a historical alternative |
| Nature | Earlier definition: Earth + Water + Fire | Composition conflict; this is a three-primary set |
| Life | Water + Spirit | Proposed |
| Crystal | Earth + Spirit | Proposed |

An earlier derivation named Wave as a candidate for Air + Water. The latest ten-name list includes Nature but does not give it a valid two-primary composition or supply an accepted name for the remaining pair. Wave remains a candidate, not an accepted assignment.

The conflict is preserved for review:
- Nature's former definition uses three primaries but the latest list places it among secondary elements.
- Light's assignment changed from Air + Fire to Fire + Spirit.
- The pairwise name/identity register is not yet a complete one-to-one mapping of all ten pairs.

### 4.3 Tertiary names and compositions

| Tertiary | Composition |
|---|---|
| Magma | Air + Earth + Fire |
| Weather | Air + Earth + Water |
| Memory | Air + Earth + Spirit |
| Storm | Air + Fire + Water |
| Radiance | Air + Fire + Spirit |
| Dream | Air + Water + Spirit |
| Blood | Earth + Fire + Water |
| Forge | Earth + Fire + Spirit |
| Growth | Earth + Water + Spirit |
| Soulfire | Fire + Water + Spirit |

Nature was also previously assigned Earth + Water + Fire, the same set as Blood. Distinct coupling mechanisms and observable properties are required before both can remain canonical names for the same combination. This proposal does not resolve that question.

### 4.4 Quaternary names and compositions

The latest owner-supplied names are Aether, Chaos, Void, Logos and Eros. The five names are provided without a name-to-composition mapping. The five mathematically possible four-primary vectors are:

| Four-primary set | Vector [A,E,F,W,S] | Omitted primary |
|---|---|---|
| Earth + Fire + Water + Spirit | [0,1,1,1,1] | Air |
| Air + Fire + Water + Spirit | [1,0,1,1,1] | Earth |
| Air + Earth + Water + Spirit | [1,1,0,1,1] | Fire |
| Air + Earth + Fire + Spirit | [1,1,1,0,1] | Water |
| Air + Earth + Fire + Water | [1,1,1,1,0] | Spirit |

The owner must assign the five names to these vectors. Earlier names (Planet, Creation, Consciousness, Civilization, World) are retained as historical proposals, not the current set.

### 4.5 Quintessence and Essence

The current owner-supplied Quintessence element name is **Unity**:

\[
Air+Earth+Fire+Water+Spirit\rightarrow Unity
\]

Unity means coherent integration of the five functional roles. It does not erase their distinctions or the separate identity and authority of participating agents.

**Essence** is the defining nature or pattern of one entity at any tier. An Essence record should specify subject, entity type, defining characteristics, provenance, version, invariants, uncertainty and observed changes. It does not prove personhood, sentience or metaphysical identity.

## 5. Four operations that preserve and restore order

| Operation | Core question | Function | Default posture |
|---|---|---|---|
| Prevent Chaos | How do we stop disorder before it begins? | Pre-action boundaries and invariant enforcement | Deny by default; enforce before action |
| Find Order | What order already exists? | Diagnostics, provenance and historical reconstruction | Measure; preserve uncertainty |
| Presume Order | How do we operate while order is assumed but unverified? | Bounded, revocable provisional operation | Confidence is not authority |
| Resume Order | How do we restore safe operation after disruption? | Checkpointing, reconciliation, compensation and verification | Reconcile before retry |

### 5.1 Prevent Chaos — open tool candidates

- **Ballast (ballast-agents):** circuit breakers, backpressure, fallback chains, cost/resource routing, chaos injection and audit. PyPI identifies version 0.1.1 as Alpha, MIT-licensed and requiring Python 3.11 or later. Do not confuse it with an unrelated SSH load-balancer project named Ballast.
- **Sponsio:** runtime agent-contract enforcement for tool calls and action sequences. The public project describes its v0.2 line as alpha. It is a candidate, not a certified enforcement authority.
- **NVIDIA OpenShell:** open runtime for agent sandboxing and policy enforcement outside the agent process, including gateway/supervisor, network mediation, filesystem access controls, process restrictions and auditable decisions. Exact controls depend on platform and policy.
- **agentic-chaos-security / agentic-chaos:** controlled fault injection and security-invariant probes across agent, memory, control, tool and MCP paths. Fault injection tests a system; it does not itself prevent disorder.

**Portable contracts**
- **agentic-chaos/v1:** experiment scope, fault, hypothesis, probes, results and cleanup.
- **EnforcementReceipt:** principal, requested action, target, policy/version, decision, enforcement point, evidence and verification.

### 5.2 Find Order — open tool candidates

- **Quantum Chaos Framework:** candidate spectral diagnostics using symmetry-resolved level statistics, GOE/GUE/GSE comparisons, OTOCs, Krylov complexity and Floquet quasi-energies. Exact source/version remains to be pinned. These metrics apply to declared quantum models, not arbitrary software order.
- **CP-WBFT:** confidence-probe weighted consensus research for LLM multi-agent systems. A 2026 paper reports results under experimental Byzantine conditions including an 85.7% fault-rate setting. The value is specific to the paper's model, topology, tasks and assumptions; it is not a general BFT fault-tolerance guarantee.
- **LLM Precedence Order:** provenance heuristic proposing system-of-record evidence before live observation, user assertion and model prior. It is a field-specific policy template, not universal truth. Source authority, freshness and susceptibility to spoofing must be explicit.
- **Quipu:** proposed bitemporal, governed knowledge-graph store with pending-post-state gates and non-widening authority composition. The identified source is an August 2026 arXiv paper with reported deterministic evaluation; independent reproduction remains open.

**Portable contracts**
- **PrimaMateriaDiagnostic:** model/Hamiltonian, symmetry sector, method, configuration, seed, metrics, uncertainty and classification (integrable / chaotic / mixed / inconclusive).
- **ConsensusEvidenceCertificate:** participants, protocol/version, messages, confidence inputs, quorum rule, failure assumptions, dissent and result.
- **ProvenancePrecedenceRecord:** value, source, as-of time, source authority, version, uncertainty, conflicts and adjudication.
- **HistoricalOrderReconstruction:** event-log checkpoint, evidence/policy versions and replay gaps.

### 5.3 Presume Order — open tool candidates

- **Progressive Trust (PT):** Internet-Draft candidate proposing multidimensional behavioural scores, time decay and trust/mandate recommendations. Scores are contextual and must not themselves grant authority.
- **ATTP (Agent Trust Transport Protocol):** Internet-Draft candidate separating identity from action-level trust decisions and defining trust dimensions and levels. It is not an adopted IETF standard.
- **NBTP (NirvanAI Behavioral Trust Protocol):** September 2026 Internet-Draft with intended experimental status. It describes local volatile trust state, time decay, signed attestations and PROBATIONARY / TRUSTED / SUSPECT / QUARANTINED states. It is not an IETF standard; the draft says outputs are risk indicators, not authorization verdicts.
- **Fidelity Probe:** proposed externally measured substrate/model migration and drift gate. Exact source/version and measurement specification remain unverified.

**Presumption safety invariant**

\[
Authority_{effective}\subseteq Authority_{already\ granted}
\]

A provisional state may narrow or condition existing permission. It must not create new targets, tools, data rights, spending authority, external action or delegation. Missing, stale or conflicting evidence should cause HOLD/deny. Where an existing policy allows provisional activity, it should be low-risk, bounded, reversible, logged and time-limited. Consequential actions require their ordinary authorization and human approval.

**Portable contracts**
- **TrustState:** dimensions, measurement window, score vector, uncertainty, decay, freshness, missing data, attestations and local verifier.
- **FidelityAttestation:** subject/substrate versions, task distribution, measured axes, baseline, confidence interval, external measurer, expiry and limitations.
- **ProvisionalAuthorizationReceipt:** pre-existing authority reference, requested action, confidence ceiling, allowed/prohibited action classes, expiry, degradation, revocation and required approval.

### 5.4 Resume Order — open tool candidates

- **Saga Engine:** candidate saga orchestration and crash recovery; exact repository/release still needs pinning.
- **Resilience Lab:** proposed agent flight recorder, chaos replay and recovery-evidence tooling; exact source/version remains unverified.
- **Hermes Agentic Architecture:** proposed durable session/checkpoint resumption; pin the exact project and checkpoint implementation.
- **OUROBOROS:** proposed in-run recovery planning with observable recovery events; exact source/version remains unverified.

Saga compensation is not necessarily rollback: a compensating action cannot erase every irreversible external side effect. Do not infer exactly-once execution from durable checkpointing.

**Resume safety invariant:** Never automatically repeat an operation whose external commit status is unknown unless it is proven idempotent or reconciled against an authoritative external record. If status is ambiguous, HOLD and reconcile before retry.

**Portable contracts**
- **SagaCheckpoint:** saga/workflow version, completed/pending/compensated steps, idempotency keys, external operation IDs, state digest, log checkpoint and ambiguous effects.
- **RecoveryReceipt:** disruption event, last verified state, replay range, reconciliation, compensations, resumed state, authorization, verification and residual uncertainty.

## 6. Four-operation public tool matrix

| Operation | Public candidate tools | Portable contract family |
|---|---|---|
| Prevent Chaos | Ballast, Sponsio, OpenShell, agentic-chaos-security | Chaos experiment; enforcement receipt |
| Find Order | Quantum Chaos Framework, CP-WBFT research, LLM Precedence Order, Quipu | Quantum diagnostic; consensus evidence; provenance precedence; historical reconstruction |
| Presume Order | Progressive Trust, ATTP, NBTP, Fidelity Probe | Trust state; fidelity attestation; provisional authorization |
| Resume Order | Saga Engine, Resilience Lab, Hermes, OUROBOROS | Saga checkpoint; recovery receipt |

These contracts are public research proposals. They do not create a central authority or grant access to private systems.

## 7. Cross-operation lifecycle

The four operations are related but not a rigid one-way pipeline:
- Prevent Chaos operates continuously.
- Find Order can inspect an initial, evolving or recovering system.
- Presume Order is a bounded decision state under incomplete verification.
- Resume Order starts after recorded disruption or loss of required invariants and ends only after evidence verifies recovery.

A lifecycle model must also permit HOLD, DENIED, INCONCLUSIVE, QUARANTINED, FAILED and UNRECOVERABLE. It must never force a positive “ordered” result.

## 8. Evidence and status separation

Keep separate:
1. Operational outcome.
2. Evidence status (asserted / observed / measured / reproduced / independently verified).
3. Review status.
4. Owner acceptance.
5. Implementation status.
6. Programme credit.
7. Action and release/publication authorization.

A policy receipt does not prove a policy is correct. A successful chaos test does not prove all possible resilience. A diagnostic classification is not authorization. A trust score is not permission. A checkpoint does not prove an external side effect was undone.

## 9. Open decisions

- Resolve Nature's tier/composition and fill the Air + Water secondary slot.
- Confirm Light's current composition.
- Assign Aether, Chaos, Void, Logos and Eros to the five quaternary vectors.
- Confirm Unity as the Quintessence element name and Essence as an entity-level concept.
- Define evidence measures for each elemental role and coupling.
- Decide whether the four operations are separate tool layers, shared-substrate lifecycle functions, or both.
- Preserve the rule that trust does not grant authority.
- Pin exact repositories, releases, licenses and performance claims for every candidate.
- Define recovery semantics for irreversible side effects and reconciliation.

## 10. Source qualification and limitations

The public source qualification register is updated for this revision. Current public source findings include:
- Ballast's ballast-agents 0.1.1 Alpha/PyPI record.
- Sponsio public repository and alpha release information.
- NVIDIA OpenShell official product and technical documentation.
- agentic-chaos public repository.
- CP-WBFT 2026 research publication.
- Quipu August 2026 arXiv paper.
- Progressive Trust, ATTP and NBTP Internet-Drafts.
- arifOS and NVIDIA Sentry public project/vendor records are referenced only as qualification context, not as dependencies in this public tool matrix.

Several proposed tools (Saga Engine, Resilience Lab, Hermes Agentic Architecture, OUROBOROS, Fidelity Probe, and Quantum Chaos Framework) still need exact source/version pins. OpenShell's enforcement and Sentry's BlueField isolation depend on deployment path and configuration; neither proves universal hardware mediation. The CP-WBFT 85.7% result is study-specific. Internet-Drafts are not standards.

No code, tool, policy, quantum system, real-world service or security control was tested. No simulation, penetration test, production test, deployment, legal review, security certification, independent audit, owner acceptance or product release is claimed.

---

**End of UNI-DP-05 v0.1.0**
