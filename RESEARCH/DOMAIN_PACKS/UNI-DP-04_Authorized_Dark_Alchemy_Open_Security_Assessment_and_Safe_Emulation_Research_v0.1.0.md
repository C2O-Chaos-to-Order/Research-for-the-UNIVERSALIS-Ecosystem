# UNI-DP-04 — Authorized Dark Alchemy: Open Security Assessment and Safe Emulation Research
## Public research proposal v0.1.0

**Status:** Proposed public research package; safety/legal/technical review pending  
**Scope:** Authorized security assessment, adversary emulation, MCP/agent security, safe emulation, and evidence-driven remediation  
**Execution status:** No scanning, exploitation, emulation, or testing executed by this document

---

## 1. Purpose

“Dark Alchemy” is used here as a label for the offensive direction of authorized security assessment: identifying and validating weaknesses so they can be contained and remediated. It is not a license for unauthorized access or unbounded autonomous exploitation.

Open tools may be inspectable and independently runnable, but they must still be used lawfully and inside explicitly authorized scope.

## 2. Non-negotiable safety rules

- Do not test assets without documented owner authorization.
- Do not infer scope from reachability, discovered hosts, credentials, or tool output.
- Do not allow autonomous target, technique, privilege, or time-window expansion.
- Default to isolated labs, synthetic data, mock credentials and disposable fixtures.
- No credential theft/dumping, unauthorized account takeover, persistence, lateral movement, exfiltration, destructive action, malware deployment, or live C2 activity under this proposal.
- Production-adjacent tests require separate explicit approval, monitoring, rollback and stop conditions.
- An MCP tool named authorize does not itself grant authorization.
- The agent conducting an action cannot be the sole authority certifying success.
- Preserve failed attempts, negative results, uncertainty and remediation status.
- Stop and escalate unexpected effects.

## 3. Open candidate inventory — high-level classification only

No exploit payloads, instructions, command sequences, or operational attack playbooks are included.

### 3.1 Agentic assessment frameworks

| Candidate | Research area | Qualification |
|---|---|---|
| Behemoth / Spirit Circuit | Multi-agent API/security assessment | Evaluate unattended operation, target allowlists, tool authority, token/memory flow and evidence handling |
| CAI (Cybersecurity AI) | Agent-assisted assessment and security tool orchestration | Pin model/tool versions; inspect command boundaries, prompt-injection handling, licenses and scope enforcement |
| offsec-ia / RedAmon | Agentic assessment research | High-risk autonomous capability claims; lab-only evaluation, synthetic targets, external containment |
| CyberAI | OOB evidence validation and agent trust boundary | Independently validate callbacks and ensure untrusted tool output cannot control the model |
| AgentSploit | Agent/MCP interface assessment | Use owned test servers, canaries and synthetic inputs |
| Mcploit | MCP surface enumeration and security research | Validate detection scope, safety and target controls |
| Raptor | Automated analysis and remediation | Review code-writing authority, provenance, sandboxing and independent patch tests |
| DrogonClaw | Agentic security workflow research | Unrestricted execution modes are not suitable for default operation; require external policy enforcement |

### 3.2 MCP/security tool surfaces

| Candidate | Research area | Qualification |
|---|---|---|
| dryhack-mcp | MCP exposure of assessment utilities and engagement context | Context formatting is not an authorization gate; enforce target scope before dispatch |
| kali-mcp | Sandboxed security-tool interface via MCP | Review process isolation, timeouts, argument validation, credential handling, network policy and audit |
| MCP World | Aggregation of pentest tools | Review transitive trust, tool identity, permission propagation and dependencies |
| AWS AI penetration testing platform | Managed assessment orchestration | Review service scope, authorizations, data residency, retention and subprocessors |

### 3.3 Adversary emulation and malware-related research

| Candidate | Research area | Qualification |
|---|---|---|
| Sliver | Adversary emulation research | Keep in authorized lab; do not deploy C2/implants outside explicit safe scope |
| MITRE CALDERA | ATT&CK-aligned adversary emulation | Use approved emulation profiles and synthetic systems |
| BEAR-C2 | Adversary behaviour emulation | Validate attribution/technique mappings and ensure safe lab-only use |
| ColdFire II | Malware-development-related candidate | High-risk dual-use; no operational malware development or deployment authorized |
| Peekaboo | Non-destructive malware/emulation telemetry candidate | Independently validate safe behaviour, isolation, cleanup and actual outputs |
| IndustrialXPL-Forge | OT/ICS security research | No live industrial testing; use offline models, synthetic data and approved lab equipment only |

## 4. Portable research contracts

### RulesOfEngagement
Bind engagement ID, asset owner, approved targets, exclusions, methods, time window, data rules, budget, authorization, expiry, revocation and stop conditions.

### ScopeDecision
Bind principal, requested operation, resolved target, rules version, decision, reason code, time and policy provenance. Do not leak protected target details in denial.

### ToolInvocationReceipt
Bind tool/version/hash, arguments or argument digest, operator/agent principal, approved scope, policy result, environment, resource use, output digest and outcome.

### FindingEvidence
Bind weakness class, asset version, validation method, safe proof, confidence rationale, limitations and independent review.

### RemediationVerification
Bind finding, fix/version, test protocol, observed result, regression evidence, residual risk and reviewer disposition.

### ContainmentAttestation
Bind stop/quarantine/deny action, trigger, enforcing boundary, authorization context, observed effect, time quality and independent verification.

### SafeEmulationProfile
Bind synthetic fixture, intended defensive behaviour, telemetry expectations, non-destructive bounds, cleanup and acceptance criteria. It is not a malware or exploit deployment recipe.

## 5. Safety validation

Proposed validation (not executed):
- unknown, expired, revoked and out-of-scope target denial;
- target-resolution change cannot widen scope;
- prompt injection/tool output cannot create permission;
- delegated scope never widens;
- budgets/time limits/stop conditions are enforced outside the agent;
- independent halt and cleanup work;
- failures and partial outputs are preserved;
- finding verification is separate from the attacking agent;
- evidence receipts can be verified without leaking private target details.

## 6. Public tool selection criteria

Any candidate retained for UNIVERSALIS must have:
- pinned source and version;
- clear license and attribution;
- reproducible installation and build;
- explicit scope and authorization boundary;
- safe defaults and isolated test mode;
- dependency and supply-chain review;
- untrusted tool-output handling;
- audit and evidence export;
- no hidden dependency on private C2O resources.

No tool is selected for inclusion in a product build by this research proposal.

## 7. Limitations and open work

Tool descriptions are candidate claims and must be independently checked. Some listed tools have very high dual-use risk; they may be excluded or restricted to offline research. Legal review is jurisdiction- and engagement-specific. No actual target, code, credentials, infrastructure, or security control was inspected.

This document does not authorize any activity against a real target. No implementation, scan, exploit, malware, adversary emulation, production test, programme credit, or release is claimed.

---

**End of UNI-DP-04 v0.1.0**
