# UNI-DP-11 — Governed Execution, Worker Lifecycle and Thermodynamic Accounting
## Public research specification v0.1.0

**Status:** Proposed public research specification; review and owner disposition pending  
**Date:** 2026-11-18  
**Boundary:** Public, portable, independently operable design contract  
**Implementation status:** Specification only; no production worker service or live resource adapter is implemented by this document  
**Research relationship:** This package defines a public UNIVERSALIS design surface. It does not copy private implementation, governance records, credentials, policies, incidents, tenant information or unpublished operational procedures.

## 1. Purpose and governing role

This package specifies the research and architecture requirements for a **Governed Execution and Worker Lifecycle Service**. The service controls when bounded computational work may begin, how it is queued and observed, how authorization and resource limits are maintained, how work is paused or stopped, how termination is evidenced, and how generated candidates remain distinct from accepted results.

Its governing rule is:

> Let work begin only through explicit gates, let activity claims answer to current observation, and let no expenditure or generated candidate stand in place of verified work.

The service must not treat intention as execution, a queue as a worker, a visual activity indicator as telemetry, missing observation as idle, a stop request as confirmed termination, resource expenditure as value, generated output as acceptance, or technical capability as permission.

This package is an architecture and research specification. It does not establish that a service has been implemented, that any worker has run, or that any result has been accepted.

## 2. Scope and non-goals

### In scope

- Request identity, declared scope and operation-specific constraints.
- Independent readiness, authorization and budget gates.
- Additional worker, runtime, safety, input and output-handling checks.
- Fresh gate decisions and reauthorization at consequential boundaries.
- Request, queue, start, execution, pause, stop, termination and result states.
- Worker identity, trusted observation and telemetry-loss handling.
- Resource reservation, consumption, hard ceilings and expiry.
- Cancellation, cleanup, retries, idempotency and residual side effects.
- Candidate generation, persistence, independent evaluation and release separation.
- Classical thermodynamic accounting with explicit physical boundaries and sign conventions.
- Multi-worker scheduling, workflow orchestration and cross-environment portability.
- Accessibility, operational transparency, security and audit evidence.

### Out of scope

This specification does not itself implement operating-system process supervision, kernel isolation, a resource broker, a live authorization provider, a distributed scheduler, a durable artifact store, a physical energy meter, a quantum processor adapter, an acceptance authority or a publication service. Each requires a separately designed and tested implementation.

The service is not a consciousness detector, motivation detector, autonomous source of authority, truth evaluator, ethical adjudicator, acceptance authority or unrestricted self-restarting agent.

## 3. Core distinctions and invariants

| Distinction | Required interpretation |
|---|---|
| Operational Forge State vs imagined will | A declared operating mode or lifecycle condition; no consciousness or independent will is inferred. |
| Physical thermodynamics vs computational activation | Joules, heat, work and entropy belong to a declared physical model. A software decision to activate work is a separate control decision. |
| Closed vs isolated system | A closed system excludes matter exchange but may exchange energy; an isolated system excludes both under the declared model. |
| Heat/work transfers vs internal-energy state | Boundary transfers and changes in stored internal energy are different terms in the balance. |
| Dissipation vs destruction | Dissipation changes energy's distribution or availability; it is not annihilation of energy. |
| Local vs total entropy | The second-law condition applies to the complete declared isolated total, not automatically to every subsystem. |
| Expenditure vs usefulness | Energy, time, tokens, compute units and cost do not establish truth, quality, utility, safety or permission. |
| Readiness vs authorization vs budget | Three independent decisions. None may substitute for another. |
| Request vs queue vs execution | A request can be queued without a worker starting; queue admission is not execution evidence. |
| Indicator vs observation | An activity statement requires fresh observation of the identified worker from a declared source. |
| Missing telemetry vs idle | Missing, stale or contradictory telemetry is UNKNOWN, not idle. |
| Stop request vs termination | STOPPING remains distinct until a fresh, identified observation establishes the worker is no longer alive. |
| Candidate vs acceptance | Generation or persistence does not make an artifact accepted, publishable or correct. |
| Understanding vs permission | Comprehension is not consent; consent is not system authorization; capability is not permission. |

These distinctions are normative design invariants. They are not claims that a particular implementation already enforces them.

## 4. Base — bounded admission and execution contracts

### 4.1 Request contract

A request record should contain, at minimum:

- Stable run ID and request ID.
- Requester and tenant or isolation-domain identity.
- Requested operation and declared scope.
- Component, version and execution-environment identity.
- Candidate-output class and output-handling policy.
- Readiness, authorization and budget decision references.
- Worker identity or worker-pool requirement.
- Resource reservation identity, unit, amount and hard ceiling.
- Maximum runtime and operation-specific resource limits.
- Telemetry source and observation-freshness policy.
- Cancellation, cleanup, persistence, retry and idempotency policies.
- Acceptance interface and sharing restrictions.

Unknown, missing or malformed mandatory fields must fail closed. A request is not an instruction to bypass admission.

### 4.2 Independent activation gates

The core necessary-condition rule is:

**Generate ⇒ Ready = PASS AND Authorized = PASS AND BudgetAvailable = PASS.**

This is a necessary condition, not a complete sufficiency theorem. A real admission decision also checks the worker, runtime, input, safety holds, telemetry, reservation integrity and output handling.

A proposed operation-specific extension set includes:

1. worker availability;
2. runtime compatibility;
3. safety holds;
4. input and scope validity;
5. output-handling validity.

Each gate must have an identifiable decision owner, source, decision ID, observation timestamp, expiry or freshness bound, evidence reference where applicable, and explicit status.

Supported gate statuses:

- PASS
- FAIL
- UNKNOWN
- ERROR
- REVOKED
- EXPIRED
- STALE
- NOT_APPLICABLE, only when the gate is explicitly optional and its contract permits that disposition

Only explicit, current PASS is accepted for a required gate. Truthy strings or numbers, missing values, stale records, inferred consent and a passing result from another gate are not substitutes. NOT_APPLICABLE is not allowed for the three core gates.

### 4.3 Reauthorization points

Relevant controls must be re-evaluated before:

- Queue admission and worker start.
- Every consequential execution step.
- Access to a new tool, capability or external service.
- Crossing a data, tenant, trust or network boundary.
- Increasing a resource reservation or consuming beyond the current increment.
- Persisting, transferring, publishing or releasing output.
- Resuming paused work or work whose observation or authorization became unknown.

Revocation closes the no-new-work boundary. A worker that remains alive after revocation is not treated as authorized merely because it has not yet stopped.

### 4.4 Lifecycle vocabulary

The service should distinguish at least:

idle, requested, queued, starting, running, pausing, paused, stopping, stopped, cancelled, failed, timed_out, budget_exhausted, authorization_revoked, telemetry_unknown, finished_unverified, candidate_persisted and candidate_withheld.

A transition record must identify the prior state, next state, event, actor or control authority, timestamp, reason and evidence. An illegal or unproven transition must not be silently normalized into success.

### 4.5 Worker observation

An observation must identify the worker, observation source, observation time, status and evidence or provenance reference. Freshness is policy-bounded. A stale observation cannot establish current liveness or current termination. An observation for a different worker cannot establish the target worker's state.

No activity indicator may imply execution solely from a queued request, a UI animation, a heartbeat from a different process or an old status record.

### 4.6 Resource reservation

A reservation must declare resource class and unit, owner or tenant, reservation ID, reserved quantity, hard ceiling, consumed quantity, expiry, enforcement point and provider evidence. Reserved does not mean consumed. A local bookkeeping counter does not prove an external quota was enforced.

Synthetic work units, tokens, runtime, CPU time, memory, accelerator allocation, monetary cost and physical joules are different units. Conversion requires a declared measurement and accounting method; it must never be assumed.

## 5. Meta — authority, lifecycle semantics and independent judgment

The execution service must not be the sole requester, authorizer, executor, observer, resource accountant, output evaluator and auditor of the same operation.

Define separately:
- who may submit a request;
- who issues readiness decisions;
- who issues and revokes authorization;
- who owns reservations and hard ceilings;
- who observes workers and validates telemetry;
- who may request pause, cancellation or escalation;
- who validates cleanup and residual side effects;
- who evaluates generated candidates;
- who authorizes publication, transfer or release.

The worker cannot grant its own authority. A status emitted by a worker is not automatically independent evidence of the worker's actual operating-system state. A candidate evaluator must be independent of the generator to the extent required by the risk and acceptance contract.

State-machine review must cover illegal transitions, duplicate events, delayed or reordered events, restart, replay, idempotency, orphan detection, retries, partial outputs, clock uncertainty, expiry, cleanup and recovery. A terminal state must not be revived by stale authorization or by a retry that reuses an earlier identity without explicit idempotency semantics.

## 6. Super — multi-worker and distributed execution

A workflow may pass through:

Request → policy evaluation → readiness → reservation → queue → worker assignment → execution → tool calls → candidate persistence → independent evaluation → release decision.

Every stage has distinct identity, status, evidence and authority. A local worker finishing does not prove that a distributed workflow, external effect, dependent job, persistence operation or release decision is complete.

Research and design must cover:
- scheduling, worker pools, queue fairness, quotas and reservation accounting;
- backpressure, capacity planning, admission control and autoscaling;
- workflow dependencies, fan-out/fan-in, batching and interactive jobs;
- tenant isolation, tool capability boundaries and least privilege;
- idempotency, duplicate delivery, retry budgets and side-effect reconciliation;
- distributed cancellation, compensating actions, cleanup and orphan recovery;
- service-level objectives and observability without turning a metric into an authorization signal.

The system must distinguish queued from running, reserved from consumed, running from productive, finished from accepted, accepted from releasable, and stopped from fully rolled back. Cancellation cannot claim that external effects have been reversed unless that reversal has separate evidence.

## 7. Hyper — emergent and correlated failure

Locally valid jobs can combine into globally unsafe work. Threat and failure analysis must include:
- queue amplification, retry storms, thundering herds and autoscaling oscillation;
- deadlock, livelock, starvation and priority inversion;
- recursive tool or agent calls, runaway task creation and circular workflows;
- shared-resource contention and hidden single points of failure;
- correlated telemetry loss, stale observations and common-mode policy failure;
- cascading cancellation that affects unrelated work;
- cross-workflow data leakage and transitive capability escalation;
- partial failure across providers, workers, storage and downstream services;
- local budget compliance that coexists with portfolio-level overspend;
- restart storms and cleanup that damages another workflow.

Model and fault campaigns must use isolated synthetic environments until the relevant safety and authorization boundaries are independently demonstrated. Recovery logic must not become an unbounded source of new work.

## 8. Ultra — portability, succession and migration

Portable workflow definitions should identify required capabilities, inputs, environment constraints, resource units, authorization references, state transitions, evidence and output contracts without binding the specification to one cloud, operating system, vendor, model or processor.

Migration and succession requirements include:
- reproducible environment descriptions and versioned worker manifests;
- provider-independent queue and workflow state;
- portable evidence and audit records;
- cryptographic agility and verifiable artifact identity;
- offline and low-resource execution modes where feasible;
- replay boundaries and explicit handling of non-repeatable external effects;
- decommissioning, stranded-work recovery and obsolete-worker retirement.

A successor controller or worker must revalidate environment compatibility, current policy, identity, authorization, capabilities, budget and cancellation semantics. Earlier admission is not perpetual permission. Migration must not revive expired credentials or prior approvals.

## 9. Quantum — operational control remains distinct from quantum state

For genuine quantum or hybrid workloads, this service may coordinate job submission, backend reservation, calibration readiness, shot limits, queue status, classical orchestration, cancellation requests and measurement-completion records.

It does not determine quantum-state validity. Quantum state preparation, measurement, probability, evolution and quantum-specific evidence must be validated by the relevant domain components and methods. Operational lifecycle state is not a superposition, and missing telemetry is not quantum uncertainty.

Quantum thermodynamics is a separate research subject. Classical macroscopic fixtures do not establish quantum thermodynamic results. Any future module must declare its physical model, system/environment boundary, observables, assumptions and measurement method.

## 10. Magic — truthful and accessible operational presentation

A management interface should make visible:
- what was requested and by whom;
- the declared scope and operation;
- which gates passed, failed, expired or remain unknown;
- which worker and environment are involved;
- what resources are reserved, consumed and remaining;
- whether the task is queued, starting, executing, paused or observation-unknown;
- whether cancellation is requested, stopping, or termination-confirmed;
- what output candidates were generated and whether they were persisted;
- whether independent evaluation or release authorization remains pending.

Use literal state labels such as “queued”, “executing”, “observation unknown”, “termination pending”, “stopped”, “candidate awaiting review” and “accepted by independent evaluator”. Do not animate queued work as running, show idle when telemetry is missing, display stopped immediately after a stop request, hide budget depletion, or imply that color, glow or motion proves energy, life, will or consciousness.

All essential information and controls must remain available through nonvisual, keyboard-accessible and assistive-technology-compatible interfaces. Color must not be the only carrier of meaning.

## 11. Transformative — evidence of actual behavioral change

A future implementation should be evaluated against measurable outcomes, including:
- unauthorized or unknown-gate starts prevented;
- starts blocked for unavailable or expired reservations;
- queued/executing mislabels prevented;
- new work blocked after revocation;
- resource overruns prevented;
- cancellation-to-confirmed-termination latency;
- orphan workers detected and recovered;
- telemetry-loss cases handled without false idle;
- duplicate external effects prevented;
- generated candidates correctly marked unverified;
- independent acceptance decisions recorded;
- cleanup and rollback outcomes recorded;
- recursion, retry amplification and cross-workflow interference contained;
- physical-energy and entropy claims kept within their evidence boundaries.

A metric is meaningful only with a defined denominator, observation window, measurement source, uncertainty and failure reporting. A high activity rate or high expenditure is not itself success. Reduce waste, not necessary capability; cost and energy optimization must not degrade safety, evidence quality, accessibility, privacy, resilience or human welfare.

## 12. Classical thermodynamic accounting boundary

For a closed system using heat positive into the system and work positive on the system:

**ΔU = Q + W_on**

If a source instead defines work positive by the system, translate explicitly:

**W_on = −W_by**

The equation is meaningful only with a declared system boundary, consistent energy units and compatible initial/final state definitions. A sign convention change must not silently change the physical law.

For an open control volume, mass-flow energy terms and any relevant kinetic/potential energy terms must be declared. A representative balance is:

**ΔE = Q + W_on + E_mass,in − E_mass,out**

For a declared isolated combined system:

**ΔS_total ≥ 0**

A subsystem may decrease in entropy while the complete isolated total, including surroundings and all relevant exchanges, satisfies the second law. Refrigerator and heat-pump analysis must include supplied work and every relevant reservoir. Dissipation is not destruction of energy.

Thermodynamic records should declare:
- system boundary and closed/open/isolated classification;
- matter exchange, heat channels and work channels;
- sign conventions and units;
- absolute temperatures and reservoir definitions;
- initial and final states;
- kinetic and potential energy treatment;
- entropy-generation model;
- measurement or simulation status;
- uncertainty, approximation and omitted effects.

Thermodynamic expenditure describes a physical process. It cannot establish that a computational result is correct, useful, ethical, accepted or authorized. A synthetic compute unit cannot be relabelled as a joule.

## 13. Elemental and Six-Alchemy research lenses

The following are interpretive design lenses, not empirical properties of a gemstone, physical law, worker, or person.

### Elemental profile

| Primary lens | Execution interpretation |
|---|---|
| Earth | Worker, runtime, queue, configuration, reservation, execution record |
| Water | Lifecycle transition, transfer, workflow, cancellation and recovery |
| Air | Request, telemetry, state labels, manifests and declared conventions |
| Fire | Authorized activation, computation, work and candidate generation |
| Spirit | Purpose, permission, stewardship, safety and independent acceptance boundaries |

The combinations may be used to examine growth, form, forge, integrity, exchange, metabolism, regeneration, insight, meaning, agency, cultivation, production, stewardship, engineering, constitution, manifestation, learning, communion, renewal and illumination. Missing-lens analyses should test for missing execution substrate, lifecycle control, observation, bounded action or authority. These labels are analytic vocabulary, not measurable system properties.

### Six Alchemies

| Lens | Carnelian assessment focus |
|---|---|
| Body | Hardware, heat, power, cooling, worker processes, accessibility, fatigue and physical safety |
| Heart | Enthusiasm, urgency and conflict must not substitute for consent, readiness, boundaries or capacity |
| Mind | Planning, generation, status interpretation, state transitions, telemetry, cancellation and independent evaluation |
| Soul | A generated artifact does not define its creator; human identity must not be reduced to activity or output |
| Spirit | Purpose, permission, stewardship, resource responsibility and limits on action |
| Consciousness | People should be able to distinguish queued, executing, unknown, stopping, terminated, unverified and accepted states |

The six lenses may be examined individually, in all 15 unordered pairs, and as integrated combinations. They are design-review questions, not covert measurements of a person's motivation, identity or mental state.

## 14. Interoperability contracts

The service should consume distinct, versioned interfaces for:
- environment and deployment readiness;
- identity and authorization decisions;
- reservation and durable resource accounting;
- worker supervision and telemetry;
- event lineage and audit persistence;
- physical energy and performance measurement;
- semantic, mathematical or domain-specific verification;
- independent candidate acceptance;
- publication, transfer and release authorization.

Each interface must identify its own owner, version, trust boundary, evidence semantics, freshness, failure behavior and revocation behavior. No service should claim another service's authority. A durable candidate is not accepted; an accepted candidate is not automatically publishable; a released candidate is not universally correct.

Public installations must be independently operable without access to any private system. Any future interoperability between public and non-public environments requires a separately reviewed, scoped, revocable and auditable interface. No shared credentials, ambient access, automatic mirroring or private operational evidence is implied.

## 15. Proposed research and acceptance work

The following test families are proposed for an independently reviewed reference implementation:

| ID | Subject | Minimum negative or boundary case |
|---|---|---|
| UNI-EX-01 | Gate admission | UNKNOWN or missing readiness, authorization or budget blocks admission |
| UNI-EX-02 | Gate freshness | Expired, stale or future-dated evidence is not accepted as current PASS |
| UNI-EX-03 | Scope and runtime | Missing scope, incompatible worker or uncleared safety hold blocks start |
| UNI-EX-04 | Queue/start separation | Queued and starting states are not displayed as executing |
| UNI-EX-05 | Observation loss | Missing, stale, mismatched or contradictory telemetry remains UNKNOWN |
| UNI-EX-06 | Revocation | Revocation blocks consequential new work and triggers controlled stop behavior |
| UNI-EX-07 | Budget | Reservation expiry, ceiling exhaustion and attempted overspend block further work |
| UNI-EX-08 | Cancellation | Stop request remains STOPPING until fresh worker-specific termination evidence |
| UNI-EX-09 | Duplicate effects | Retry and replay do not silently duplicate external effects |
| UNI-EX-10 | Candidate separation | Generated and persisted candidates remain unaccepted until an independent decision |
| UNI-EX-11 | Thermodynamics | Sign convention, boundary declaration and complete isolated entropy total are checked |
| UNI-EX-12 | Distributed failure | Retry storms, recursion, shared-resource exhaustion and cancellation cascades are contained |
| UNI-EX-13 | Migration | Old authorization, capability or worker identity is not revived during succession |
| UNI-EX-14 | Accessibility | State and controls are usable without color, pointer or animation |
| UNI-EX-15 | Public boundary | No private credential, tenant record, private policy or unpublished operational detail is required or exposed |

These are test definitions, not executed results. A future implementation must pin its source revision, interpreter/runtime, dependencies, fixtures, test runner and output digests. Independent review must challenge the model with counterexamples and realistic fault cases.

## 16. Evidence and status discipline

Keep these dispositions separate:

- specification authored;
- implementation present;
- tests authored;
- tests executed;
- independently reproduced;
- technically reviewed;
- security/privacy reviewed;
- owner accepted;
- research-programme credit awarded;
- publication authorized;
- runtime/deployment authorized.

A checked box, successful unit test, syntactically valid schema, model-checking result or green build supports only the property and scope actually tested. It does not automatically prove production readiness, safe operation, scientific validity, acceptance or release permission.

## 17. Open research questions

1. Which external supervisor can provide trustworthy worker-specific liveness and termination evidence across processes, containers, VMs and remote workers?
2. What freshness and trusted-time assumptions are needed for each gate and observation source?
3. How should cancellation and compensating actions be represented when external effects cannot be reversed?
4. How can resource reservations be enforced consistently across heterogeneous schedulers and accelerators?
5. Which fairness, priority and admission policies avoid starvation without granting unbounded privilege?
6. How should recursive tool calls and transitive capabilities be bounded and audited?
7. How can correlated telemetry and policy failures be detected independently?
8. What minimum evidence is sufficient for a candidate to progress from generated to persisted, evaluated, accepted and releasable?
9. Which measurement and uncertainty models support credible whole-workflow energy accounting?
10. Which workflow state can be migrated or replayed safely across providers without reviving old authority?

## 18. Disposition

UNI-DP-11 is a proposed public research specification. It is not a deployed worker service, a completed security review, a validated thermodynamics package, a certification, a release decision or an authorization to execute workloads. Product implementation belongs in the public product repository after requirements, schemas, threat analysis, isolation, tests and explicit approval are established.

**Research informs design. Evidence supports claims. Separate authorization governs consequential change.**
