# UNI-DP-07 — Periodic Table and Materials Property Layer
## Public research proposal v0.1.0

**Status:** Owner-supplied material-layer model recorded; scientific/tool review pending
**Scope:** Open element-property data, materials structures, computational workflows, knowledge graphs, and portable evidence contracts
**Implementation status:** Not started
**Experiment / simulation status:** Not executed
**Release status:** Draft research branch only; no merge or product adoption implied

---

## 1. Purpose

The periodic table and materials-science data provide an empirical material-property layer beneath the proposed functional Elemental Alchemy hierarchy.

- **Elemental Alchemy** describes functional roles, couplings and system regimes.
- **The material-property layer** describes chemical elements, compounds, structures, phases and measured or computed properties under declared conditions and methods.

The periodic table does not replace the alchemical hierarchy. The alchemical hierarchy does not replace chemistry, quantum chemistry, solid-state physics, materials thermodynamics or experimental evidence.

**The symbolic affinities are interpretive proposals, not standard chemical classifications.** The material data can ground claims about substances and their properties; it cannot by itself validate the Air/Earth/Fire/Water/Spirit mapping.

## 2. Periodic-table scientific baseline

The conventional periodic table contains 118 named elements and organizes them by increasing atomic number and recurring chemical/physical patterns.

- Atomic number Z is the proton count and identifies the chemical element.
- Periods are rows related to electron-shell/subshell occupation; period position is informative but does not alone determine all material properties.
- Groups are columns. For many main-group elements, similar valence configurations explain recurring chemistry; the relationship is more complex for transition and f-block elements.
- Blocks classify elements according to the subshell being filled (s, p, d, f). Block and group are not interchangeable.
- Chemical properties depend on electron configuration, oxidation state, bonding, environment, temperature, pressure, phase and structure.
- Atomic mass is not determined by atomic number alone; isotopic composition changes mass and nuclear properties without changing element identity.

### 2.1 Blocks and families

| Classification | Conventional meaning | Qualification |
|---|---|---|
| s-block | Subshell being filled is s; commonly groups 1–2, with helium as an electron-configuration exception | Hydrogen is in group 1 but is a nonmetal and is not an alkali metal |
| p-block | Subshell being filled is p; commonly groups 13–18 | Includes metals, metalloids and nonmetals; halogens/noble gases are families inside this block |
| d-block | Subshell being filled is d; commonly groups 3–12 | The d-block is not identical under every definition to IUPAC-defined transition elements |
| f-block | Subshell being filled is f; lanthanoid and actinoid series | Series boundary conventions must be declared in the dataset |

Special families: Group 1 alkali metals (excluding H), Group 2 alkaline-earth metals, Group 17 halogens, and Group 18 noble gases. Helium sits in group 18 while its electron configuration is 1s².

### 2.2 Chemical-property cautions

- Alkali metals generally have low first ionization energies and readily form +1 cations. Their reactions with water are exothermic and become more vigorous down the group, but rate, total heat release, mechanism and observed violence are not interchangeable. Group 2 is not simply identical to group 1.
- Transition metals commonly show variable oxidation states, metallic conductivity, coordination chemistry and catalytic activity, but these properties are element- and context-dependent. The IUPAC definition concerns atoms with incomplete d subshells or cations with incomplete d subshells; broad usage sometimes includes the entire d-block.
- The p-block is not “the nonmetal block.” It includes post-transition metals, metalloids and nonmetals. Semiconductivity belongs to selected elemental metalloids and many compounds/materials, not all p-block nonmetals.
- Halogens are generally electronegative and readily form anions in many reactions, but reactivity varies with element and environment.
- Noble gases have closed valence shells and generally low chemical reactivity; “inert” is not absolute, and noble-gas compounds are known.
- Lanthanoids often have predominant +3 oxidation states and characteristic magnetic/optical properties; actinoids exhibit more variable oxidation chemistry and include radioactive elements/isotopes. Neither series has one universal “high-energy, long-lived” behaviour.

Primary chemistry references:
- OpenStax, Periodic Table: https://openstax.org/books/chemistry/pages/2-5-the-periodic-table
- OpenStax, Electronic Structure: https://openstax.org/books/chemistry/pages/6-4-electronic-structure-of-atoms
- OpenStax, Periodicity: https://openstax.org/books/chemistry-atoms-first-2e/pages/18-1-periodicity
- RMIT, Periodic Table Structure: https://learninglab.rmit.edu.au/chemistry/introduction-periodic-table/arrangement-periodic-table/
- IUPAC Periodic Table: https://iupac.org/what-we-do/periodic-table-of-elements/

## 3. Proposed periodic-family affinities — interpretive overlay

The following owner-supplied associations are retained as hypotheses. They are not measurable chemical properties, do not replace group/block/family classifications, and may overlap.

| Periodic family/feature | Proposed alchemical affinity | Material basis motivating the analogy | Limitation |
|---|---|---|---|
| Alkali metals (Group 1, excluding H) | Fire | Electropositive character, low first ionization energy, ready oxidation and vigorous reactions with some reagents | Not every reaction is violent; behavior depends on reagent and conditions |
| Alkaline-earth metals (Group 2) | Fire, weaker/differentiated candidate | Electropositive metals, commonly form +2 ions | Not equivalent to Group 1; members differ |
| Transition metals / d-block | Earth + Water | Metallic lattices/conductivity, variable oxidation and coordination, catalytic pathways | Not all d-block elements meet the strict IUPAC transition-element definition; properties are context-dependent |
| Selected p-block nonmetals | Air | Covalent bonding and molecular diversity | p-block also contains metals and metalloids |
| Metalloids / selected semiconductors | Air + Earth candidate | Band structure, controlled conductivity, dopability and information-processing uses | Specific material/structure required; not universal to all metalloids |
| Halogens (Group 17) | Fire + Water | Oxidizing/electron-accepting chemistry and reactive combinations | Subset of p-block; context-dependent |
| Noble gases (Group 18) | Spirit | Closed valence shells and generally low reactivity | Low reactivity is not awareness or integration; compounds exist |
| Lanthanoids | Spirit + Fire candidate | f-electron-related magnetic, optical and coordination properties | Series properties vary; distinguish from actinoids |
| Actinoids | Spirit + Fire candidate, distinct from lanthanoids | f-electron chemistry, variable oxidation and nuclear/radioactive properties | Isotope and handling constraints are element-specific |

Affinities are many-to-many: halogens and noble gases are both p-block families. A data model must allow multiple typed relationships rather than force one block into one primary.

## 4. Relationship to the Elemental Alchemy hierarchy

| Alchemical tier | Proposed material-science analogue | What can be measured | Qualification |
|---|---|---|---|
| Primary | Element families, electron configurations, blocks and properties | Z, configuration, group, period, electronegativity, ionization energy, radii, density, phase | Family properties can motivate analogies, not validate symbolic primaries |
| Secondary | Binary compounds and two-role coupling examples | Composition, structure, bonding, formation energy, phase and properties | Two chemical species do not automatically mean two alchemical primaries |
| Tertiary | Ternary compounds, alloys and multi-component materials | Composition, structure, phase stability, property tensors and synthesis data | Chemical component count is not an alchemical functional coupling |
| Quaternary | Four-component chemical systems and multi-component phase behaviour | Composition, stable phases, phase diagrams and thermodynamic data | Group behaviour and lanthanide contraction are not four-primary combinations |
| Quintessence / Unity | Periodic table and materials-property knowledge as a whole | Dataset coverage, schema, provenance and predictive model performance | Periodic table is a classification, not a single material or proof of Unity |
| Essence | Entity-specific identity; element identity includes atomic number Z | Z, isotopic composition, state and provenance | Z identifies the element; isotopes/states affect mass and properties, so Z does not determine everything else |

### 4.1 Chemical composition is not alchemical coupling

NaCl and H₂O are binary compounds in chemistry. Their formulae do not, by themselves, establish pairings such as Fire + Earth or Air + Water. A valid alchemical coupling needs a separate mapping from chemical species/material roles to the functional ontology, an explicit mechanism and observable emergent properties.

Steel is an iron-based alloy, commonly containing carbon and potentially other alloying elements. It should not be treated generically as a fixed ternary compound. Specify composition, phase, microstructure and processing before using a steel example.

The lanthanide contraction is a periodic trend across the lanthanoid series, not a four-primary coupling.

## 5. Material data model

Every value must retain conditions, units, provenance and method.

### ElementRecord
- atomic number, symbol, name;
- group, period, block, family classifications and table convention;
- electron configuration with charge/state context;
- standard atomic weight or conventional interval as appropriate;
- isotope records and abundances;
- oxidation states and source;
- property values, units, uncertainty, conditions and method;
- data release, retrieval time and reviewer disposition.

### PropertyObservation
- subject element/isotope/ion/compound/material;
- property identifier and value;
- machine-readable unit, uncertainty and coverage;
- state/phase, temperature, pressure, composition and conditions;
- experimentally measured / computed / estimated / compiled / inferred status;
- method/model/software version and parameters;
- source publication/database and revision;
- measurement/calculation time and retrieval time;
- missingness and quality flags.

A null means no usable value is supplied; never silently replace it with zero or an invented estimate. Estimated or computed values remain labelled.

### MaterialRecord
- material identifier, formula and component stoichiometry;
- crystal structure, space group, structure source/version;
- phase/polymorph, synthesis/processing conditions;
- properties, tensor/anisotropy and units;
- thermodynamic stability and calculation/experiment method;
- database revision, parameters and uncertainty.

### PhaseDiagramRecord
- chemical system, temperature and pressure domain;
- thermodynamic model/database revision;
- stable/metastable phases, formation energies and reference states;
- approximation/DFT functional or experimental method;
- uncertainty and coverage;
- diagram software/version, inputs, digest and provenance.

A phase diagram is conditional on its data, method and thermodynamic assumptions. Matching the source version does not by itself prove chemical accuracy.

## 6. Open tool candidates

This is a candidate inventory, not an adoption list. Counts, data coverage, license, maturity and performance must be pinned to exact releases.

### 6.1 Element-property lookup

**@cyanheads/reference-data-mcp-server**
- Repository: https://github.com/cyanheads/reference-data-mcp-server
- Package: https://www.npmjs.com/package/@cyanheads/reference-data-mcp-server
- Documents ref_element_lookup and ref_element_search. Fields include atomic number, symbol, mass, electron configuration, group, period, block, category, electronegativity, density, melting/boiling points, phase, radioactivity/natural occurrence and discovery information.
- Offers local stdio and Streamable HTTP; repository lists Apache-2.0.
- Qualification: pin the dataset/source revision. It does not replace specialist sources for every ionization energy, radius, isotope uncertainty or materials thermodynamics field.

**mendeleev**
- Repository: https://github.com/lmmentel/mendeleev
- Docs: https://mendeleev.readthedocs.io/en/stable/
- PyPI: https://pypi.org/project/mendeleev/
- Python API for elements, ions and isotopes; data models include electron configuration, ionization energies, ionic radii, isotopes, oxidation states, phase transitions and property metadata. Unit support is documented in the 1.3 series.
- Qualification: a Python library, not MCP by itself; match the mendeleev-data release and review property citations, licenses, units and missingness.

**xraylib-mcp-server**
- Repository: https://github.com/tschoonj/xraylib-mcp-server
- Underlying library: https://github.com/tschoonj/xraylib
- Exposes X-ray interaction data including cross sections, fluorescence lines, edge energies and scattering factors; maintainer announcement reports 101 tools.
- Qualification: specialized radiation-interaction data, not a complete periodic-table/materials database. Validate units, energy range, matrix/formula handling and exact version.

### 6.2 Materials and structure databases

**HeshamFS/mcp-materials-server**
- Listing/source mirror: https://glama.ai/mcp/servers/HeshamFS/mcp-materials-server
- Documented listing describes ten tools, two resources and three prompts for Materials Project search, structure retrieval (CIF/POSCAR/JSON), properties, comparisons, filters, similar structures, phase diagrams and elastic properties; requires a Materials Project API key.
- Qualification: third-party catalogue reports inactive maintenance. Verify canonical repository, current code/version, dependencies, license, API compatibility and tests before adoption. Ten tool names do not establish completeness or production readiness.

**Materials Project MCP in mp_api**
- Official docs: https://github.com/materialsproject/public-docs/blob/main/services/ml-and-ai-applications/mcp.md
- Materials Project docs state MCP functionality is included with mp_api 0.46.0. The documented baseline includes fetch and search; fetch_all, fetch_many and a phase-diagram tool are described as in development in that guide.
- API setup: https://docs.materialsproject.org/downloading-data/using-the-api/getting-started
- Qualification: authenticated Materials Project data requires an account/API key. Respect terms, access limits, attribution, data version and external service boundaries. Distinguish official mp_api from third-party adapters.

**Materials MCP Commons**
- Repository: https://github.com/HeshamFS/materials-mcp-commons
- Describes plugin-agnostic contracts/infrastructure for materials data, simulations and workflows with evidence-backed trust levels.
- Qualification: project states no production-alpha release has been published yet; developing interoperability foundation only.

**Chemia / MatKG**
- MCP docs: https://chemiadiscovery.com/docs/mcp/tools/
- MatKG paper: https://www.nature.com/articles/s41597-024-03039-z
- Chemia documents graph-neighbour, shortest-path, top-connected, application and substitute tools.
- The 2024 MatKG paper reports a graph extracted from about five million materials-science papers with over 70,000 entities and 5.4 million unique triples.
- Qualification: corpus size is not entity count. Literature-mined relations are not direct experimental or causal proof. Pin data revision, access and tool inventory.

**MCP4MP / mcp-materials-project**
- Names retained from owner-supplied research.
- Exact repositories/packages have not been pinned here. Do not count them as separate implementations until confirmed. Compare the official mp_api MCP and third-party adapters rather than duplicating labels.

### 6.3 Computational materials workflows

**atomate**
- Repository: https://github.com/hackingmaterials/atomate
- Docs: https://atomate.org/
- Open-source computational materials workflow framework built around pymatgen, custodian and FireWorks; documented workflows cover structure optimization, band structures, elastic/dielectric properties, equations of state, nudged elastic band and spectroscopy.
- Qualification: workflow orchestration, not a periodic table lookup tool or necessarily an MCP server. It executes external computational codes; solver availability, licenses, HPC resources, input settings, convergence and provenance must be managed. Atomate2 is a distinct successor and should be reviewed separately.

### 6.4 Knowledge-graph candidates

| Candidate | Owner-supplied proposed role | Source qualification |
|---|---|---|
| SCP-ElementKG 2.0 | Element → functional group → molecule → reaction → experiment graph | Exact repository, dataset snapshot, PubChem/ORD ingestion, license and entity count not pinned |
| SCP-KCL | Association graph using electronegativity, covalent radius, bonding and periodic proximity | Exact source/version and validation study not pinned |
| SCP-KANO-ChEBI | Element properties and functional-group hierarchy integration with ChEBI | Exact source/version and mapping provenance not pinned |
| Usai Hypergraph | NDJSON-LD representation of all 118 elements/property morphisms | Exact source, schema, release and coverage definition not pinned |

These candidates are retained, not rejected. “Complete knowledge graph” requires a declared coverage universe, date, exclusions and validation metrics.

### 6.5 Periodic-table software architecture pattern

**mneme-ai**
- Package: https://www.npmjs.com/package/@mneme-ai/mcp
- Describes an MCP server with tool categories including a lab/periodic-table/primitive-operation composition model.
- Qualification: current npm package version and internal documentation version strings differ in the surfaced description; pin release and generated tool catalogue. Its “periodic table” is a software-composition metaphor, not chemical periodicity or a chemical data service.

**damir-majer/agentic-engineering-periodic-system**
- Owner-supplied candidate for a periodic taxonomy of agentic-engineering practices and an MCP interface.
- Exact canonical source/version and license remain unpinned.

### 6.6 Archetypal and machine-learning periodic tables

**Isomorphic Quantization**
- Owner-supplied candidate refers to a 2026 paper proposing a 1:1 mapping between the physical periodic table and an archetypal table, including a symbolic variable mapped to atomic number.
- Source surfaced: https://www.researchgate.net/publication/407783384_The_Isomorphic_Quantization_of_Mind_and_Matter_Mapping_the_Archetypal_Periodic_Table_to_Chemical_Elements
- Qualification: author-proposed speculative framework, not established chemistry or a demonstrated mathematical isomorphism. Requires formal definitions, proof obligations and falsifiable predictions.

**Alchemical Periodic Table of Machine Learning**
- Owner-supplied symbolic atlas of ML architectures.
- Exact source, author, version, license and formal mapping not pinned; speculative/design reference only.

## 7. Portable evidence contracts

- **ElementPropertyReceipt:** atomic identity, property value/unit/uncertainty, isotope/ion/state, source/release/citation, method, conditions, retrieval time and output digest.
- **MaterialsComparisonReceipt:** material IDs/formulae, properties/units, conditions, database version, structure/phase, method, comparison rule, missingness/uncertainty and result digest.
- **PhaseDiagramReceipt:** chemical system, temperature/pressure, phases, thermodynamic data/method, database/model version, assumptions, uncertainty, diagram software and result digest.
- **PropertyMorphism:** typed mapping between properties/ontologies, mapping rule, units, equivalence/approximation class, schema versions, provenance and validation. Graph similarity alone does not prove scientific equivalence.
- **PeriodicPrimitiveComposition:** typed software operations, parameters, composition graph, execution order, pre/postconditions, side effects, permissions, resource estimate and evidence. It must not be conflated with a chemical ElementPropertyReceipt.

## 8. Validation requirements

All requirements are proposed and unexecuted:
1. Cross-check Z, symbol, name and dataset release; preserve discrepancies.
2. Require units, citations, uncertainty, conditions, oxidation state and method for property values.
3. Do not infer isotope/ion values from neutral-element records without a defined method.
4. Keep block, group and special-family labels distinct and potentially overlapping.
5. Validate formula parsing, material IDs, structures, and upstream API schemas.
6. Verify CIF/POSCAR/JSON outputs preserve lattice, symmetry, occupancy and composition.
7. Reproduce phase diagrams from frozen inputs/database/model versions.
8. Report solver, functional, pseudopotential/basis, k-points, cutoffs, software and convergence.
9. Quantify knowledge-graph extraction accuracy, entity resolution and provenance.
10. Propagate source corrections to affected downstream claims.
11. Test MCP authentication, least privilege, input validation, prompt/tool injection resistance, rate limits, secrets and egress.
12. Verify data flows, retention and external dependencies before describing a deployment as local/sovereign.

## 9. Public/private and evidentiary boundary

UNIVERSALIS tools should remain independently operable. This package contains public tool candidates and portable contracts only; it does not depend on private credentials, services, policies or approval infrastructure.

A hash/signature establishes only the integrity/authenticity property defined by its cryptographic scheme. It does not prove scientific correctness, material safety or fitness for synthesis.

## 10. Open decisions and status

Open decisions:
- Owner acceptance of the periodic/material layer and its relationship to UDRR.
- Which family-affinity mappings are retained and how they are typed.
- Periodic-table conventions for helium, La/Lu, Ac/Lr and group-3 variants.
- Coverage of isotopes, ions, transuranic elements and naturally occurring materials.
- Canonical dataset/source precedence, missingness and uncertainty policy.
- Exact tool source/version/license pins, especially SCP graphs, Usai Hypergraph and archetypal/ML tables.
- Whether mneme-ai is merely an architecture pattern or a runtime dependency.

The chemistry classification and property facts are established scientific material; mappings to Air/Earth/Fire/Water/Spirit are owner-proposed analogies. No chemical experiment, materials synthesis, simulation, DFT calculation, phase-diagram computation, measurement, product implementation, security test, legal review or owner acceptance is claimed.

---

**End of UNI-DP-07 v0.1.0**
