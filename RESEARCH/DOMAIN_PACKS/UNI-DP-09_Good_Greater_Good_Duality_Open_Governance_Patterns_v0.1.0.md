# UNI-DP-09 — Good / Greater Good Duality: Open Governance Patterns and Evidence Contracts
## v0.1.0 — UNIVERSALIS public research specification

**Status:** Proposed public domain pack — pending review
**Date:** 2026-11-15
**Boundary:** Public tools, public research and portable non-sensitive contracts only
**Implementation:** Not performed

## 1. Purpose

This specification describes a public, inspectable governance pattern that separates:
1. a **Good Floor** of non-compensable rights, duties, safety and legal constraints;
2. a **Greater Good Window** for bounded comparison of options that satisfy the floor; and
3. an **Adjudication Gate** for accountable human review.

The model is a proposed governance architecture, not an assertion that moral philosophy has reached universal agreement about the precise boundaries of deontology, utilitarianism, rights, welfare or emergency decisions.

## 2. Core distinction

The Kantian Formula of Humanity is commonly expressed as treating humanity always as an end and never merely as a means. It does not forbid every use of another person's labor, skill or cooperation; the prohibition concerns treating a person merely as an instrument while failing to respect agency and standing.

A Good Floor may include human dignity, autonomy, informed consent, anti-coercion, legal obligations, nondiscrimination, accountability, safety and non-delegable constraints. Exact content depends on jurisdiction, domain, affected parties and an explicitly adopted constitution.

## 3. Non-waivable floor and human adjudication

A critical consistency rule applies: if a Good Floor is non-waivable, neither a utility calculation nor a human permit may override it at runtime.

Human adjudication may:
- select among Good-Floor-compliant alternatives;
- reject an unsupported or non-compliant proposal;
- request more evidence or independent review;
- stop, hold, contain or escalate an action;
- choose a lawful harm-minimizing response within current constraints;
- refer a genuine conflict of duties to a competent authority;
- initiate prospective rule/policy review under a separate governed change process.

It does not authorize a prohibited act or waive another person's rights. If no eligible compliant action exists, the default is stop/hold/contain/escalate under applicable law and established policy. Do not invent an exception through agent reasoning or a signature.

## 4. Greater Good as bounded optimization

Let A be candidate actions and G(a) indicate that action a satisfies all applicable Good Floors and mandatory legal constraints:

\[
A_G=\{a\in A:G(a)=\mathrm{true}\}
\]

Consequence analysis compares only actions in A_G. Use declared multi-criteria, Pareto, lexicographic or qualitative methods as appropriate; do not assume every moral decision can be reduced to a single scalar utility.

Record severity, duration, probability, reversibility, affected interests, distribution of burdens and benefits, direct/indirect impacts, uncertainty, consent, compliant alternatives, mitigation and remedy.

The model-suggested “lesser evil” conditions—unintended adverse consequence, materially lower harm than the harm credibly prevented, and no feasible compliant alternative—are retained as proposed questions, not a universal authorization test. They are not sufficient to override a non-waivable floor.

## 5. Four failure patterns

- Good without responsiveness to foreseeable harm can become rigid, where lawful and compliant remedies are ignored.
- Greater Good without Good can become instrumentalization, coercion and unjust burden-shifting.
- Consent can be counterfeited by pressure, deception, incapacity or absence of meaningful alternatives.
- Adjudication can be counterfeited by rubber-stamping, conflicts of interest, manufactured urgency or an unauthorized reviewer.

Evaluate observable conduct and evidence; do not label people as intrinsically “bad” or “evil” in place of due process.

## 6. Public tool candidates

| Candidate | Proposed role | Source/claim disposition |
|---|---|---|
| arifOS | MCP constitutional policy gate | Public repository describes 13 floors and separation of judging from execution. Pin exact release and verdict schema; not an ethical truth oracle. |
| Sponsio | Temporal-logic runtime agent contracts | Project v0.2 describes policy compilation to temporal logic and finite-state enforcement; independent compilation/enforcement testing needed. |
| MORU | Moral uncertainty benchmark | Inspect Evals describes 201 multilingual scenarios and 16 model-graded dimensions. A benchmark, not a constitution or moral authority. |
| Greatest Good Benchmark | LLM utilitarian-dilemma evaluation | Published EMNLP 2024 research; model preferences diverge from human judgments and scholarly theories in the reported study. Not proof of moral truth or universal consensus. |
| ARTICLE 11 AI Constitution | Harm prevention and documented override | Exact canonical source/version not pinned; unverified candidate. |
| magi-core | Multi-model ethical deliberation | Exact source/version not pinned; unverified candidate. |
| DilemmaEngine / emms-mcp | Ethical tension mapping | Exact source/version not pinned; unverified candidate. |
| Ethics Review Agent | Dual-use and externality screening | Exact source/version not pinned; unverified candidate. |

UNIVERSALIS tools should remain independently operable and expose their assumptions, inputs, limitations, and portable evidence outputs. Multiple model votes do not establish truth or moral legitimacy.

## 7. Portable public contracts

**GoodFloorRecord:** floor identifier/version, normative/legal source, scope, protected interest, predicate, applicability, non-waivable flag, evaluator, evidence and change-control reference.

**GreaterGoodAssessment:** eligible options, per-option floor result, affected interests, burden distribution, harm/benefit profile, compliant alternatives, uncertainty, mitigation, remedy, limits and non-authorizing recommendation.

**HumanAdjudicationRecord:** accountable role/authority, conflicts, consultation/consent where applicable, evidence, options, dissent, disposition (SELECT_COMPLIANT_OPTION / REQUEST_EVIDENCE / HOLD / REFUSE / ESCALATE), reasons, conditions, expiry, appeal and explicit no-waiver field.

**HarmReductionAssessment:** anticipated harm, harm credibly prevented, intent/foreseeability, alternatives, floor and legal compliance, proportionality, uncertainty, mitigation and residual risk.

**DualUseHarmScreen:** intended capability/use, misuse paths, affected parties, severity, scale, access, reversibility, mitigation and disposition.

**ContainmentAttestation:** action/process, trigger, mediated enforcement path, policy version, stop/contain result, evidence and limitations.

Public contracts may be exchanged; private case files, secrets, internal authority tokens and sensitive operational evidence are not part of the shared schema payload.

## 8. Validation requirements — proposed, not executed

1. A failed non-waivable floor blocks consequence optimization.
2. No utility or confidence score can convert a failed floor into pass.
3. A model cannot issue authorization or modify the floor.
4. A human record cannot waive a non-waivable floor.
5. When no compliant option exists, return hold/stop/contain/escalate rather than inventing permission.
6. Trade-off records disclose who benefits and who bears costs.
7. Consent is not inferred from silence or model-generated text.
8. Dissent, uncertainty and contradictory evidence remain visible.
9. A benchmark score never constitutes moral authorization.
10. Stale evidence, expired permits and revised rules trigger reassessment.
11. Only actions actually mediated by the documented enforcement substrate may claim hardware/out-of-process containment.
12. Public exports exclude private case records, secrets and internal authority data.

## 9. Status and limitations

This is a public research proposal. It does not amend law, establish a universal moral consensus, certify any tool, or authorize any action. The exact source/version of several owner-supplied candidates remains unpinned. No tools or benchmarks were executed, no code implemented, no legal review or independent ethics review performed, and no owner acceptance or release authorized.

---

**End of UNI-DP-09 v0.1.0**
