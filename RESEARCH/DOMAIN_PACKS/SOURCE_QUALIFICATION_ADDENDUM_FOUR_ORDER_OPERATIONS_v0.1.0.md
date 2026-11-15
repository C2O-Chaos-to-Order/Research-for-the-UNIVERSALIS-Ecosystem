# Public Source Qualification Addendum — Four-Operation Order Tools
## v0.1.0 — 2026-11-15

**Status:** Bounded public source intake; review and independent reproduction pending  
**Purpose:** Qualify the public tool candidates in UNI-DP-05. Project/vendor claims are not treated as independent assurance.

## 1. Prevent Chaos

| Candidate | Public source | Source-supported description | Qualification |
|---|---|---|---|
| Ballast / ballast-agents | https://pypi.org/project/ballast-agents/ | PyPI lists 0.1.1 Alpha, MIT, Python >=3.11; package description lists circuit breakers, backpressure, fallbacks, chaos injection and audit | Early-stage alpha; distinguish from unrelated SSH load-balancer software named Ballast. |
| Sponsio | https://github.com/SponsioLabs/Sponsio ; https://sponsio.dev/ | Runtime agent-contract enforcement for tool calls/action sequences; repository lists Apache-2.0 and v0.2 alpha line | Alpha software. Repository notes security findings and subsequent fixes; pin exact version and independently review. |
| NVIDIA OpenShell | https://www.nvidia.com/en-us/ai/openshell/ ; https://docs.nvidia.com/openshell/dev/security/best-practices ; https://docs.nvidia.com/openshell/about/architecture | Open runtime with sandbox, supervisor, network mediation, filesystem/process controls, policy decisions and audit | Landlock best_effort can continue without Landlock when unavailable; strict deployments must use hard_requirement and test host compatibility. Enforcement depends on backend and configuration. |
| agentic-chaos | https://github.com/RicoKomenda/agentic-chaos | Project describes controlled security/reliability fault injection and invariant probes across LLM, tool, memory, control, agent and MCP paths | A validation harness, not a preventive control. Use isolated systems and synthetic fixtures. |

## 2. Find Order

| Candidate | Source | Source-supported description | Qualification |
|---|---|---|---|
| CP-WBFT | https://ojs.aaai.org/index.php/AAAI/article/view/40806 ; DOI 10.1609/aaai.v40i41.40806 | AAAI 2026 paper reports confidence-probe weighted consensus experiments, including an 85.7% Byzantine fault-rate setting | Study-specific result; not a general BFT guarantee. Preserve the paper's model, topology, tasks and attack assumptions. |
| Quipu | https://arxiv.org/abs/2608.16813 | August 2026 arXiv paper describes a bitemporal governed graph, post-state gates and non-widening authority composition; reports deterministic evaluation | Preprint/project evidence; independent reproduction and implementation/security review remain open. |
| LLM Precedence Order | No formal source pinned | Owner-supplied provenance heuristic placing system-of-record, live-observation, user-assertion and model-prior sources in a proposed order | Policy proposal only. Define authority per field, freshness, integrity and conflict handling. |
| Quantum Chaos Framework | Exact repository/release not pinned | Owner-supplied level-spacing, OTOC, Krylov and Floquet diagnostic candidate | Not yet a qualified tool. Quantum diagnostics are model-specific, not generic software-order measures. |

## 3. Presume Order

| Candidate | Source | Source-supported description | Qualification |
|---|---|---|---|
| Progressive Trust | https://datatracker.ietf.org/doc/draft-sato-soos-pt/ | Internet-Draft describing multidimensional behavioural measurements and time decay toward a configured baseline | Not an adopted IETF standard. Scores are contextual risk evidence, not authorization. |
| ATTP | https://datatracker.ietf.org/doc/draft-sharif-attp/ | Internet-Draft describing agent trust scoring, identity and action-limit enforcement | Not an adopted IETF standard. Intended status does not establish standards adoption; check current revision and IPR disclosures. |
| NBTP | https://datatracker.ietf.org/doc/draft-nirvanai-nbtp/ | September 2026 draft-01 describes local volatile trust, decay, signed attestations and PROBATIONARY / TRUSTED / SUSPECT / QUARANTINED states; intended status Experimental | Not an IETF standard. The Datatracker says Internet-Drafts have no formal standing in the standards process; the draft says its score is a risk indicator, not an authorization verdict. |
| Fidelity Probe | Exact source/release not pinned | Owner-supplied externally measured model/substrate drift gate | Source, measurement protocol, thresholds and independent reproduction not established. |

## 4. Resume Order

| Candidate | Source | Current qualification |
|---|---|---|
| Saga Engine | Exact repository/release not pinned | Owner-supplied saga orchestration and recovery candidate; compensation is not universal rollback. |
| Resilience Lab | Exact repository/release not pinned | Owner-supplied flight recorder and chaos-replay candidate; claims not yet verified. |
| Hermes Agentic Architecture | Exact project/release not pinned | Owner-supplied durable session/checkpoint candidate; exact Hermes project must be identified. |
| OUROBOROS | Exact repository/release not pinned | Owner-supplied in-run recovery planner; exact source/version and semantics unverified. |

## 5. Hardware and governance qualification context

- NVIDIA Sentry / BlueField-4: https://www.nvidia.com/en-us/networking/products/software/sentry/ and https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime . NVIDIA describes an isolated hardware trust domain, out-of-band monitoring and in-silicon policy enforcement. These are vendor claims; enforcement only applies to traffic/actions routed through the deployed control path.
- NVIDIA OpenShell technical controls: https://docs.nvidia.com/openshell/dev/security/best-practices . Landlock best_effort may warn and continue if unavailable; strict deployments must explicitly require it and test host compatibility.
- arifOS source/version and license context: https://github.com/ariffazil/arifOS . The public repository is AGPL-3.0 and describes 13 constitutional floors; the archived constitutional document records floor-name drift and points to a live canonical policy. It is referenced here as an ecosystem context source, not as an automatic dependency or adopted UNIVERSALIS policy.

## 6. Safety cautions

1. Trust state is not identity, authority or proof of truth.
2. Missing attestation can reflect network or measurement failure; do not automatically equate silence with misconduct.
3. Consensus scores require common-mode failure analysis, dissent, abstention and explicit Byzantine assumptions.
4. A successful chaos experiment does not prove all possible resilience.
5. OpenShell controls depend on platform and configuration; Landlock best_effort may continue without Landlock.
6. NVIDIA Sentry's in-silicon enforcement applies only to the actual mediated traffic/action path.
7. Saga compensation cannot erase every irreversible side effect. Unknown external commit status requires reconciliation before retry.
8. Presume Order cannot create authority; actions remain inside pre-existing, independently authorized scope.

---

**End of public source qualification addendum v0.1.0**
