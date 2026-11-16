# UNI-DP-03 — Agent Essence and Quintessence: Open Identity and Federation Research
## Public research proposal v0.1.0

**Status:** Proposed research package; standards, security, and interoperability review pending
**Scope:** Portable agent identity, continuity, credentials, delegation, multi-agent federation, and coherent integration
**Implementation status:** Not started
**Test status:** No credential or federation tests executed

---

## 1. Definitions

**Essence** is the persistent, attributable, governed identity of an individual agent, independent of its current cognition model or execution substrate.

**Quintessence** is the emergent, verifiable coherence of a governed system integrating multiple agents and functional roles while preserving each constituent's identity, permissions and accountability.

Essence describes an individual principal. Quintessence describes coordination. Quintessence is not a super-identity and must not erase or fuse the identities of its members.

Operational terms such as awareness, consciousness and self do not establish subjective experience.

## 2. Essence identity model

A conceptual identity tuple is:

\[
I=\langle id,K,P,M,H\rangle
\]

where id is a stable identifier, K represents cryptographic identity references, P the constitutional profile/policies, M memory, and H interaction history.

Implementation should keep separate:
- stable logical principal;
- model/runtime/hardware substrate;
- versioned purpose, values and limits;
- memory/history references with provenance;
- credentials and public verification methods;
- accountable owner or organization.

Private signing keys never belong in portable identity attestations. Credentials should contain key identifiers/public verification methods, issuer, subject, audience, validity, status, delegation and proof suite.

Copying memory does not prove sameness of identity. State explicitly whether a migration is same principal, successor, fork, delegate, restored backup, or independent agent.

## 3. Open Essence candidates

| Candidate | Proposed function | Qualification |
|---|---|---|
| SHIK — Self-Hosted Identity Kernel | Persistent identity state separated from active cognition engine; MCP interface | Research/architecture candidate until storage, access control, migration, key management, backup/recovery, and independent tests are reviewed |
| Agent Identity Bridge (AIB) | Cross-protocol identity/credential bridge across MCP/A2A/ANP/AG-UI | Check exact draft status and whether the implementation is W3C-endorsed (do not assume so); verify DID method, credential proof, status, delegation and protocol mapping |
| Attestix | Identity, DIDs, delegation, credentials, reputation and provenance | Pin release, license, audit state, key custody, privacy, and provenance claims |
| Delx Ontology | Declarative functional identity: mission, style, role, limits, purpose, failure patterns and continuity | Conceptual schema; not proof of personal identity or subjective continuity |

## 4. Standards snapshot

As of 2026-11-15:
- DID Core 1.1 was a W3C Candidate Recommendation Snapshot (05 March 2026).
- Verifiable Credentials Data Model 2.0 is a Recommendation; 2.1 remains draft work in 2026.
- Data Integrity EdDSA Cryptosuites 1.0 is a Recommendation; 1.1 is draft work.
- Bitstring Status List 1.0 is a Recommendation; 1.1 remains draft work in November 2026.

Pin exact versions and update status during implementation. Candidate Recommendation and Working Draft do not mean final Recommendation. Older Ed25519Signature2020 is not the default for new designs without compatibility justification. Credential fields claiming AI Act compliance do not prove compliance.

References:
- https://www.w3.org/TR/did-1.1/
- https://www.w3.org/TR/vc-data-model-2.0/
- https://www.w3.org/TR/vc-di-eddsa-1.1/
- https://www.w3.org/TR/vc-bitstring-status-list-1.1/
- https://www.w3.org/TR/

## 5. Quintessence: multi-agent integration

A proposed model:

\[
Q=\Phi(Air,Earth,Fire,Water,Spirit,\Gamma,\Pi)
\]

The five roles are functions, not a requirement for five agents. One agent may fulfill multiple roles; multiple agents may jointly fulfill one role.

The evidence model should bind:
- Air: message traces, schemas, identity and provenance.
- Earth: structural constraints, ontology/schema versions and validation.
- Fire: execution receipts, resource/energy records and outputs.
- Water: workflow topology, synchronization, retries and conflicts.
- Spirit: governance decisions, integration, disagreement and review.

Do not reduce these distinct measures to one unvalidated coherence score.

## 6. Open Quintessence candidates

| Candidate | Proposed function | Qualification |
|---|---|---|
| TEQUMSA v60 | Multi-instance federation and causal ledger | Claims about Merkle causal ledger, Pearl L3/RDoD gate, phi-recursive federation, consciousness and MCP calls require exact source, version, mathematical definitions and independent reproduction; presently unverified |
| Daena-Coder QUINTESSENCE | Multi-model council and expert-lens synthesis | Diversifies perspectives; not proof of correctness or consciousness |
| Quorum | Evidence-scored agent deliberation, dissent and abstention | Review evidence rubric, model independence, consensus assumptions, and MCP security |
| Zen MCP Gemini Transcendent | Multi-stage cross-model collaboration | Exact repository/version and performance claims require pinning and independent review |

Model voting is not truth. Shared data, training, prompts, infrastructure, provider dependencies, and model families can create correlated errors. Preserve dissent, abstention, evidence gaps and unresolved contradictions.

## 7. Causal, cryptographic, and coherence claims

Pearl's L1/L2/L3 ladder describes association, intervention, and counterfactual reasoning. L3 is not a universal numerical confidence threshold. Causal claims require an appropriate model and identification assumptions.

Merkle structures can make record changes detectable if checkpoints and roots are correctly maintained. They do not prove claim truth or causal validity.

Keep distinct:
1. ledger integrity;
2. causal validity;
3. federation coherence;
4. authorization legitimacy.

Do not accept a quoted 0.999999 threshold without a clear statistical definition, dataset, calibration, error analysis and independent reproduction.

## 8. Portable contracts

### EssenceAttestation
Stable principal, issuer, owner, identity version, continuity relation, public key reference, constitutional profile version, declared capabilities, scope, delegation chain, protected memory/history references, credential status, validity, audience and verifier limitations.

### QuintessenceAttestation
Federation identity, member Essence references, functional-role coverage, integration contract, message/proposal/evidence references, dissent/abstention, coherence metrics with uncertainty, authorization record, execution result, independent reviewer and limitations.

### DelegationChain
Parent principal, child principal, scope, purpose, audience, expiry, constraints, revocation and explicit monotonic narrowing.

### EssenceToQuintessenceBridge
Membership consent, role assignment, requested collective authority, aggregate policy evaluation, approval, member-level limits, and exit/revocation behaviour.

## 9. Federation safety requirements

- Verify member identity, issuer, proof, credential status, expiry and audience.
- Record accountable owner and participation authorization.
- Do not infer approval from silence or an offline member.
- Preserve member-level permissions; collective authority cannot exceed explicit system authorization.
- Record dissent, abstention, conflict and unresolved evidence.
- Revoke capabilities when member identity or credentials are revoked.
- Keep cognition separate from authorization.
- Provide member exit, suspension, migration, fork and successor semantics.
- Maintain an independent stop and audit path.
- Do not treat model consensus, a Merkle root or a signed output as proof of truth.

## 10. Proposed validation

Tests remain PROPOSED — NOT EXECUTED:
- model/runtime migration and continuity classification;
- key rotation/revocation/recovery;
- credential signature, issuer, audience, status and expiry;
- delegation scope narrowing;
- memory provenance, conflict and correction;
- member impersonation, duplicate identity, offline/revoked member;
- correlated model failure and manufactured consensus;
- dissent/abstention retention;
- authorization independence from model output;
- exit, revocation, and federation state recovery.

## 11. Status and limitations

These are public research candidates, not selected or production-ready dependencies. No identity kernel, credential bridge, federation, key system, or verifier was implemented or tested. No subjective consciousness or universal causal proof is claimed. Owner review, standards review, security assessment, licensing, privacy, and interoperability validation remain open.

---

**End of UNI-DP-03 v0.1.0**
