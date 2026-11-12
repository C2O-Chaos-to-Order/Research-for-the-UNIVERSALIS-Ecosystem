# Engineering Toolchain and Initial Build Plan

**Repository:** `C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem`  
**Responsibility:** UNIVERSALIS Research / MotherThread research substrate  
**Status:** Initial executable foundation in this branch; specialized candidates remain proposed pending verification.  
**Boundary:** Open UNIVERSALIS / independently operable. Never include C2O-private credentials, policies, authority state, private research records, or operational data.

## Universal engineering foundation

- Least-privilege GitHub Actions CI, automated tests, and JSON contract/config validation.
- CodeQL/static analysis, secret scanning, dependency review, Dependabot, actionlint, and SBOM generation after settings and alert ownership are confirmed.
- CycloneDX/SPDX, OSV-Scanner, Trivy/Grype, Gitleaks, SLSA provenance, in-toto attestations, cosign signing, immutable releases, and reproducible-build comparison as staged controls.
- Pin toolchain versions and action references; retain specifications, fixtures, execution logs, provenance, and explicit limitations.

**Foundation candidates:** Secure SDLC Evidence Collector; repo-assurance; Chainguard Actions; cnspec SBOM Cataloger; CodeQL; actionlint; OSV-Scanner; Trivy/Grype; Gitleaks; SLSA/in-toto; cosign. Not yet verified as installed.

## Domain-specific candidate tools

ResearchPilot for evidence-grounded academic research and persistent workspaces; research-kb-core for deterministic local-first research records, stable IDs, provenance, and transactions; research-os for structured resumable workspaces; Lyra and Certus as evidence-graph/abstention references; T21 Research Assistant for section-aware corpus-grounded retrieval. Keep research resumable across sessions/devices, source-fragment anchored, and explicit about uncertainty, failed retrieval, and abstention.

Verify canonical source, license, maintainer, release activity, security, compatibility, data flow, and evidence claims before adoption. XR camera, microphone, gaze, hand-tracking, and spatial data require explicit consent and minimization. Agent-to-agent delegation requires explicit boundary authorization.

## Initial executable implementation

- `.github/workflows/repository-quality.yml` runs on pushes and pull requests with read-only repository permissions.
- `.github/scripts/repository_quality_baseline.py` provides a dependency-free self-test and validates JSON in schema/manifest/contract/capability/skill directories plus `package.json` and `tsconfig.json`.
- This first gate does not yet implement XR scenes, spatial interaction, persistent research, bridge authorization, or device conformance.

## Next increments

1. Audit current runtime, API, device, data-flow, and repository boundaries.
2. Add portable manifests/contracts and device-independent fixtures.
3. Add browser/screen-reader and supported-device tests; provide non-immersive fallbacks.
4. Implement versioned MCP/A2A public interface contracts with authentication, scopes, expiry, revocation, and audit events at the boundary.
5. Record conformance, accessibility, privacy, performance, and safety limitations.

## Evidence status

| Item | Status |
|---|---|
| Tool candidates recorded | Documented |
| Baseline validator and CI authored | Implemented in this branch |
| GitHub Actions execution | Pending |
| Domain candidate verification | Pending |
| Specialized integration | Not yet implemented |
