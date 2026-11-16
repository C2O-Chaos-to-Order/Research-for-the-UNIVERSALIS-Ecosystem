# Public Domain Pack Source Qualification Register
## Elemental, Quantum, Identity, and Authorized Security Research v0.1.0

**Status:** Initial bounded source register; review and release disposition pending  
**Date:** 2026-11-15  
**Purpose:** Preserve exact public source locators and distinguish project existence from validation of project claims.

## 1. Status vocabulary

- **Primary source pinned:** official source located; exact release/commit may still need pinning.
- **Research publication located:** paper/preprint/workshop record located; reproduction remains separate.
- **Owner-supplied candidate:** candidate name/description supplied by owner; canonical source/version not yet pinned here.
- **Vendor/project claim:** public claim requiring independent review.
- **Unverified:** exact capability, measurement, license or security property not established.
- **Not assessed:** no relevant review performed.

Open documentation is not automatically open-source licensing. A project page is not independent validation. A paper supports the authors' reported method/results, not necessarily independent replication.

## 2. Public primary sources located

| Area | Candidate/source | Public locator | What it supports | What it does not establish |
|---|---|---|---|---|
| Air / MCP | JetBrains Air | https://www.jetbrains.com/help/air/air-in-ides-extend-agent-capabilities.html | Air IDE documentation and MCP configuration; states SSE is not supported | Does not support claims of all transports in all clients |
| Air / MCP | MCP Streamable HTTP specification | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/transports/streamable-http.mdx | MCP transport revision dated 2026-07-28 | Does not prove a particular client/server implements it correctly |
| Identity | DID Core 1.1 | https://www.w3.org/TR/did-1.1/ | W3C Candidate Recommendation Snapshot dated 2026-03-05 | Not a final Recommendation or endorsement of a DID method |
| Identity | VC Data Model 2.0 | https://www.w3.org/TR/vc-data-model-2.0/ | W3C Recommendation | Does not prove any tool implements it correctly |
| Identity | W3C standards index | https://www.w3.org/TR/ | Current standard/draft publication states | Does not establish interoperability |
| Identity | EdDSA Cryptosuites 1.1 | https://www.w3.org/TR/vc-di-eddsa-1.1/ | W3C Working Draft | Not a final Recommendation |
| Identity | Bitstring Status List 1.1 | https://www.w3.org/TR/vc-bitstring-status-list-1.1/ | W3C Working Draft | Not a final Recommendation |
| Earth | EMMOntoPy / EMMO | https://github.com/emmo-repo/EMMOntoPy | Public ontology tooling project | It is materials-ontology-specific, not a universal elemental ontology |
| Water | Mycelium | https://github.com/harishkotra/mycelium | Multi-agent memory mesh, sync, provenance and contradiction-related code | Does not establish production-grade trust or security |
| Ice | SirixDB | https://github.com/sirixdb/sirix | Project source describes append-only, bitemporal revisions and MCP server | Version, access control and snapshot semantics require exact review |
| Ice | SirixDB MCP design | https://sirix.io/sirix/docs/MCP_SERVER_DESIGN.html | Describes revisions, time-travel reads, diff and snapshot registry; named snapshots are registry labels | Does not establish cryptographic immutability of snapshot labels |
| Metal | NornicDB historical MVCC reads | https://github.com/orneryd/NornicDB/blob/main/docs/user-guides/historical-reads-mvcc-retention.md | Project documentation for MVCC history and historical reads | Does not prove all graph search indexes are historical |
| Light | Lightrun MCP overview | https://docs.lightrun.com/mcp/mcp-overview/ | Live runtime context, expressions, call stacks and MCP integration | Does not remove privacy/security risk of runtime data |
| Light | Lightrun MCP quickstart | https://docs.lightrun.com/mcp/mcp-quickstart/ | Authentication/version availability and access settings | Does not replace independent authorization |
| Nature | SkillPuzzler paper | https://openreview.net/pdf?id=Mc1JTnKQIH | Research publication describing four agents, fifteen tools, materials/chemistry research and reported benchmark | Does not prove general production self-evolution |
| Essence | Attestix API docs | https://docs.attestix.io/api-reference/ | Documents 47 MCP tools across modules | Does not establish security audit or correctness of all claims |
| Essence | Attestix source/contributor guide | https://docs.attestix.io/contributing/ | Public source location and contributor workflow | License/quality must be checked at exact release |
| Quintessence | Daena-Coder | https://github.com/Mas-AI-Official/Daena-Coder | Repository describes council and Quintessence expert-lens synthesis | Does not establish answer truth, model independence or consciousness |
| Quantum | Stim | https://github.com/quantumlib/Stim | Stabilizer circuit simulator source | Does not establish third-party MCP wrapper quality |
| Quantum | tqec | https://github.com/tqec/tqec | Topological QEC compiler source | Does not establish hardware fault tolerance without device evidence |
| Quantum | QICK | https://github.com/openquantumhardware/qick | Open RFSoC-based quantum control/readout source | Does not establish specific device calibration or results |
| Dark / emulation | Sliver | https://github.com/BishopFox/sliver | Adversary-emulation project source | Does not authorize use against any target |
| Dark / emulation | MITRE CALDERA | https://github.com/mitre/caldera | ATT&CK-aligned adversary-emulation source | Does not authorize use against any target |

## 3. Candidates awaiting exact source/version pins

The following candidate names are retained from the research input. This register does not yet pin a canonical repository/release/license for them:

- Elemental: air-mcp-server / Agent Identity Registry; Qualixar OS; Alchemy MCP/code-mode-alchemy-mcp; omni-mcp; metamcp; open-ontologies; Quipu; GreenPick; phase-decoupled power-control implementation; Murakkab; KAIROS; Joule; Graph Merge; MCP-Injector; arifOS; AgentKeeper; Synthesis; LiveAuth MCP Server; Dust.tt; Soundbox; sound-gen-mcp; cks-mcp; Steam Web CLI; crystal-memory-mcp.
- Quantum: QECTOR-Decoder-v3; wai-quantum-cli; Orbit; SpinQICK; Ctrl-FreeQ; qopt; Quantum Expectations; FSharp.Azure.Quantum.Topological; moonlab; Quantum Chaos Framework; ControlMap.jl; quantum-debugger; Quantum Chaos Monkey; Process Roulette; quantum-jitter-labyrinth; q-ring; APHF; GSB.
- Identity/federation: SHIK; Agent Identity Bridge; Delx Ontology; TEQUMSA v60; Quorum; Zen MCP Gemini Transcendent.
- Authorized security research: Behemoth/Spirit Circuit; CAI; offsec-ia/RedAmon; CyberAI; AgentSploit; Mcploit; Raptor; DrogonClaw; dryhack-mcp; kali-mcp; MCP World; AWS AI penetration-testing platform; BEAR-C2; ColdFire II; Peekaboo; IndustrialXPL-Forge.

Not pinned does not mean a project does not exist. It means its exact identity and relevant version have not yet been established in this register.

## 4. Claims requiring independent reproduction

- Tool, server, decoder, module, model, provider and transport counts.
- QEC parity/logical-coset proof claims and benchmark throughput.
- Orbit's reported 95.3% logical Bell-state result and large-qubit dynamic-circuit claims.
- GPU/LLM energy, carbon, cost, and tokens/J improvements.
- MCP-Injector's reported task-completion degradation under a defined fault profile.
- Quipu trust-lattice and post-state gating invariants.
- Dust.tt remote MCP/data-source semantics and data residency.
- Soundbox and sound-gen provider/tool counts.
- Steam Web CLI's proposed generic workflow-transformation role; the located candidate appears to focus on Steam gaming Web APIs.
- Attestix/AIB/SHIK/TEQUMSA cryptographic, identity, delegation and causal verification claims.
- Project license and “open-source” labels at exact version and for transitive dependencies.
- Claims of consciousness, subjective identity, sentience, or universal causal certainty.

## 5. Adoption gates

Before a candidate is adopted:
1. Pin canonical URL, release, commit and package hash.
2. Record direct and transitive licenses/attribution.
3. Review maintenance, provenance, dependencies and supply-chain posture.
4. Inspect data flows, identity, authorization, logging, retention, deletion and external providers.
5. Reproduce quantitative and security claims.
6. Preserve failed/negative results and uncertainty.
7. Obtain independent review and a separate acceptance decision.

---

**End of public source qualification register v0.1.0**
