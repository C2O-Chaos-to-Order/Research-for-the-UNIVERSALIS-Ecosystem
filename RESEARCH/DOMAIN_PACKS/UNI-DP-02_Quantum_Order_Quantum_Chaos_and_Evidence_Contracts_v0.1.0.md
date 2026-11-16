# UNI-DP-02 — Quantum Order and Quantum Chaos: Open Research Tools and Evidence Contracts
## Public research proposal v0.1.0

**Status:** Proposed public research package; independent technical review pending
**Scope:** Quantum Order, Quantum Chaos, controlled chaos engineering, and quantum chaos alchemy
**Implementation/experiment status:** No code, simulator or QPU execution performed by this document

---

## 1. Definitions and domain separation

**Quantum Order:** engineered preservation, recovery, and verification of specified quantum information and computational behaviour within declared physical and operational constraints.

**Quantum Chaos:** research into quantum dynamical regimes and relationships to classical chaos, including integrability, spectral statistics, scrambling, thermalization, and driven systems.

**Quantum Chaos Alchemy:** proposed staged research combining diagnosis, controlled perturbation/fault injection, observation, control/stabilization or optimization, independent evaluation, and explicit disposition.

These are distinct fields. Quantum mechanics is not simply chaos. Entropy, coherence, entanglement, physical error rates, logical error rates, and uncertainty are distinct quantities. A high-fidelity demonstration is not automatically fault-tolerant operation.

## 2. Quantum Order mechanisms

| Mechanism | Goal | Evidence |
|---|---|---|
| Error detection | Identify error syndromes | Code/check definition, syndrome history, detection results |
| Error correction | Recover logical information | Decoder/recovery record, logical error statistics, code distance |
| Error mitigation | Reduce observable bias without full fault-tolerant correction | Assumptions, method, noise model, uncertainty, overhead |
| Dynamical decoupling | Reduce selected environmental couplings using control pulses | Sequence, timing, calibration, measured comparison |
| Optimal/pulse control | Improve gates/state preparation under a declared model | Hamiltonian/noise model, constrained pulses, measured fidelity |
| Topological protection | Encode information robustly against specified local errors | Code and phase assumptions, distance, logical operators |
| Fault-tolerant planning | Estimate resources for protected computation | Physical error rates, code distance, logical workload and cost model |

A parity/syndrome relation such as Hc=s mod 2 is necessary for syndrome consistency under a declared convention, but does not prove logical recovery. A residual error may commute with stabilizers while implementing a nontrivial logical operation. Separate syndrome faithfulness from logical-coset/recovery evidence.

## 3. Public tool candidate register — Quantum Order

| Candidate | Research function | Qualification |
|---|---|---|
| QECTOR-Decoder-v3 | Multi-family QEC decoding and syndrome verification | Verify exact version, license, proof suite scope, parity/logical-coset checks, benchmark and MCP boundary. Some supplied licensing claims distinguish a noncommercial backend from a proprietary plugin; do not label the entire stack unrestricted open source. |
| Stim / stim-mcp-server | Stabilizer circuit simulation, detector error models, logical-error path diagnostics | Distinguish mature simulator from experimental MCP wrapper; inspect auth/local deployment and exact release. |
| tqec | Surface-code/lattice-surgery compiler to Stim circuits | Validate primitive semantics, generated circuits, compiler version and equivalence tests. |
| wai-quantum-cli | QEC CLI/MCP and signed outputs, twirling/DD options | Exact source/release and signing semantics remain to be verified. |
| Orbit | Dynamical decoupling, transpilation and measurement mitigation | Hardware/function-provider dependent; pin experiment, backend, workload, uncertainty and provider terms. |
| QICK | RFSoC pulse control and readout | Open hardware/firmware/software candidate; test actual board, timing, calibration and device integration. |
| SpinQICK | Spin-qubit control | Device-specific; verify measured coherent control and readout evidence. |
| Ctrl-FreeQ | Optimal control with open-system/Lindblad modelling | Validate hard hardware limits; a penalty term is not necessarily an enforced bound. |
| qopt | Experiment-oriented optimal control and noise simulation | Pin version, device support, maintenance, calibration and test coverage. |
| Quantum Expectations | Fault-tolerant resource estimation and hardware scenario comparison | Recompute estimates; assess physical error-rate assumptions, model simplifications, code distance, endpoint auth and uncertainty. |
| FSharp.Azure.Quantum.Topological | Anyon models, braiding and topological gate compilation | A mathematical library is not proof of physical hardware protection. |
| moonlab | Clifford tableau and topological QC simulation candidates | Verify source, model scope, benchmark and exact topological feature support. |

### 3.1 Result qualification

The supplied Orbit note reports a 95.3% logical Bell-state fidelity in one [[4,2,2]] experiment when error detection is combined with decoupling, versus 44% with error detection alone. Keep this as an experiment-specific claim until the exact source, device, circuit, calibration, uncertainty and independent reproduction are pinned. A [[4,2,2]] code is a small distance-2 detection code; the result does not prove arbitrary single-qubit correction or general fault tolerance.

## 4. Quantum Chaos diagnostics

| Diagnostic | Function | Limitations |
|---|---|---|
| Level-spacing statistics | Compare spectra with Poisson and GOE/GUE/GSE ensembles | Resolve symmetries/sectors; finite-size caveats |
| OTOCs | Probe operator spreading/scrambling | Model-, temperature-, and regime-dependent |
| Spectral form factor | Analyze spectral correlations over time | Unfolding, averaging and finite-size choices matter |
| Krylov complexity | Study operator/state growth in a Krylov basis | Definition/basis dependence |
| Loschmidt echo | Probe sensitivity to perturbation/reversal | Sensitivity alone does not prove chaos |
| Floquet quasi-energy analysis | Study periodic driving regimes | Drive, symmetries and sampling matter |
| Entanglement growth | Study information spreading across subsystems | Distinguish chaos, integrability, localization and noise effects |

Diagnostics should allow chaotic, integrable, mixed, and inconclusive results under a declared protocol. Inconclusive is a valid outcome.

## 5. Quantum Chaos Alchemy tool candidates

| Candidate | Function | Qualification |
|---|---|---|
| Quantum Chaos Framework | Symmetry-resolved level statistics, OTOCs, Krylov complexity, SYK/Hubbard/Floquet diagnostics | Reproduce positive and negative results from pinned configs/seeds; no universal accessible-size Lyapunov claim |
| ControlMap.jl | Stochastic quantum control and measurement-feedback Kraus channels | Validate Kraus completeness, Born sampling, numerical stability and convergence |
| quantum-debugger | Chaos diagnostics and error-mitigation tools | Separate chaos measures from PEC/CDR/QNG/ZNE mitigation; compare against reference tools |
| Quantum Chaos Monkey | Simulated noise/gate-fault/decoherence injection | Use deterministic seeds and isolated simulator; do not send fault payloads to production QPU |
| Process Roulette | Quantum pipeline/process fault injection | Isolated staging; preserve idempotency/checkpoint/retry evidence |
| quantum-jitter-labyrinth | Deterministic quantum-inspired decision-graph perturbation via MCP | “Quantum-inspired” is not quantum hardware or physical quantum randomness; measure task benefit and coherence loss |
| q-ring | Entropy-aware secret management | Security tool, not a quantum-physics implementation; review key custody, memory exposure and lifecycle |
| APHF / Arbitrarily Precise Quantum Alchemy | Quantum-chemistry perturbation and energy derivatives | Computational quantum chemistry/alchemical perturbation, not quantum-computer execution |
| Generalized Simulated Bifurcation | Edge-of-chaos optimization | 2,000-variable/10ms and near-100% success statements are supplied claims; reproduce exact instances, baselines, hardware and stopping criteria |

## 6. Quantum Order evidence contracts

- **QECCodeContract:** code family, check matrix/stabilizers, logical operators, distance, logical/physical qubits, circuit, decoder and noise model.
- **SyndromeVerificationReceipt:** observed syndrome, correction, check version, parity result, logical recovery/coset result, decoder version, time quality and reviewer.
- **DecouplingSequenceReceipt:** idle window, sequence, pulse timing/axes, calibration, hardware/noise model, comparison, fidelity and uncertainty.
- **PulseControlAttestation:** target gate/state, pulse envelope, Hamiltonian/noise assumptions, calibrated hardware limits and measured result.
- **FaultTolerantResourceEstimate:** logical workload, physical errors, code distance, layout, surface-code/distillation assumptions, model version, cost/time and uncertainty.
- **QuantumChaosDiagnosticReceipt:** Hamiltonian/circuit, symmetry, diagnostic, system size, seed, numerical method, result class and limitations.
- **ChaosInjectionReceipt:** isolated target/model, fault type/intensity, seed, environment, observed metrics, failure and cleanup record.
- **StabilizationReceipt:** initial state/model, control/feedback, target, stability and convergence evidence, uncertainty.

Every field must state whether it is measured, simulated, estimated, asserted or independently reproduced.

## 7. Safe experimental boundaries

- Simulators and synthetic fixtures precede hardware use.
- Fault injection is restricted to isolated, explicitly approved environments.
- QPU submissions require explicit project, device, shot/time/cost budget and human approval.
- Pulse-level changes must be tied to calibration, hardware limits, rollback/stop conditions, and measured outcome.
- Remote simulators, QPUs, schedulers, telemetry and cloud services are external trust boundaries.
- No live hardware tests, QPU jobs, production fault injection, or destructive experiments are authorized by this proposal.

## 8. Open work

- Pin exact repositories, package versions, licenses and commit hashes.
- Reproduce decoder parity and logical-coset evidence.
- Reproduce Orbit hardware results and uncertainty.
- Validate physical error-rate dependence of resource estimates.
- Determine valid diagnostic thresholds by model class.
- Keep quantum-inspired optimization and quantum chemistry distinct from quantum hardware execution.
- Commission independent technical and security review before tool adoption.

---

**End of UNI-DP-02 v0.1.0**
