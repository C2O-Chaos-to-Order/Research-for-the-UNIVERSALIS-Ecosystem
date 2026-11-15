# Public Materials Source Qualification Addendum
## v0.1.0 — 2026-11-15

**Status:** Initial source review; complete tool audit and independent reproduction pending

## 1. Core chemistry sources

| Source | Locator | Supports | Does not establish |
|---|---|---|---|
| IUPAC Periodic Table | https://iupac.org/what-we-do/periodic-table-of-elements/ | Recognized periodic table and element identities | Symbolic alchemical affinities |
| OpenStax, Periodic Table | https://openstax.org/books/chemistry/pages/2-5-the-periodic-table | Group/family overview | Every compound property from group alone |
| OpenStax, Electron Configurations | https://openstax.org/books/chemistry/pages/6-4-electronic-structure-of-atoms | Main-group, d/f-block electronic structure and transition-element qualification | Identical chemistry across all d-block elements |
| OpenStax, Periodicity | https://openstax.org/books/chemistry-atoms-first-2e/pages/18-1-periodicity | Periodic trends and alkali-metal properties | Universal violence/heat-release claims |
| RMIT, Periodic Table Structure | https://learninglab.rmit.edu.au/chemistry/introduction-periodic-table/arrangement-periodic-table/ | s/p/d/f block definition and helium exception | Alchemical role mappings |
| Chemistry LibreTexts, Group 1 | https://chem.libretexts.org/Courses/Howard_University/General_Chemistry%3A_An_Atoms_First_Approach/Unit_8%3A__Materials/Chapter_20%3A_Periodic_Trends_and_the_s-Block_Elements/Chapter_20.3%3A_The_Alkali_Metals_%28Group_1%29 | Ionization/reaction context | Reactivity/total heat as interchangeable measures |

## 2. Element-property tools

| Candidate | Exact source | Publicly described capability | Qualification |
|---|---|---|---|
| @cyanheads/reference-data-mcp-server | https://github.com/cyanheads/reference-data-mcp-server ; https://www.npmjs.com/package/@cyanheads/reference-data-mcp-server | Element lookup/search tools, basic periodic properties, stdio/Streamable HTTP; Apache-2.0 | Pin dataset version and source; not all specialized properties or materials data |
| mendeleev | https://github.com/lmmentel/mendeleev ; https://mendeleev.readthedocs.io/en/stable/ | Python API for elements/ions/isotopes and associated property database | Python library, not MCP by itself; review version-matched data and units |
| xraylib-mcp-server | https://github.com/tschoonj/xraylib-mcp-server ; https://github.com/tschoonj/xraylib | X-ray cross-sections, fluorescence, edge energies and scattering data | Specialized radiation interaction database, not general periodic table |

## 3. Materials and workflow tools

| Candidate | Exact source | Publicly described capability | Qualification |
|---|---|---|---|
| HeshamFS/mcp-materials-server | https://glama.ai/mcp/servers/HeshamFS/mcp-materials-server | Materials Project search, structures, properties, comparisons, phase diagrams and elastic properties | Third-party catalogue reports inactive maintenance; API key required; verify canonical source, tests and release |
| Materials Project MCP (mp_api) | https://github.com/materialsproject/public-docs/blob/main/services/ml-and-ai-applications/mcp.md | Official docs describe MCP in mp_api 0.46.0, baseline fetch/search; further tools then in development | API key and upstream terms/limits apply |
| Materials Project API | https://docs.materialsproject.org/downloading-data/using-the-api/getting-started | Official mp-api client | Authenticated access, not an unrestricted public endpoint |
| Materials MCP Commons | https://github.com/HeshamFS/materials-mcp-commons | Plugin-agnostic MCP contracts for material science data/workflows | Project says no production-alpha release yet |
| Chemia / MatKG | https://chemiadiscovery.com/docs/mcp/tools/ ; https://www.nature.com/articles/s41597-024-03039-z | MCP graph tools; paper reports ~5M paper corpus, >70k entities and 5.4M triples | Literature-mined graph relations are not direct experimental or causal evidence |
| atomate | https://github.com/hackingmaterials/atomate ; https://atomate.org/ | Open-source computational materials workflows | Requires external solvers/resources; not an MCP periodic-table lookup service |

## 4. Software-pattern and speculative candidates

| Candidate | Locator | Qualification |
|---|---|---|
| mneme-ai MCP | https://www.npmjs.com/package/@mneme-ai/mcp | A software primitive-composition metaphor, not chemical periodicity; version labels in package metadata/docs need reconciliation |
| damir-majer/agentic-engineering-periodic-system | Not pinned | Owner-supplied; exact source/version/license needed |
| SCP-ElementKG 2.0 | Not pinned | Exact repository, dataset snapshot, license and entity counts not verified in this source intake |
| SCP-KCL | Not pinned | Exact source and validation study not verified |
| SCP-KANO-ChEBI | Not pinned | Exact source, ChEBI mapping and release not verified |
| Usai Hypergraph | Not pinned | Exact source/schema/coverage not verified |
| Isomorphic Quantization | https://www.researchgate.net/publication/407783384_The_Isomorphic_Quantization_of_Mind_and_Matter_Mapping_the_Archetypal_Periodic_Table_to_Chemical_Elements | Author-proposed speculative mapping; no established chemical or mathematical isomorphism verified |
| Alchemical Periodic Table of Machine Learning | Not pinned | Exact source, author, version and formal mapping not verified |

## 5. Qualification conclusions

- The periodic table grounds measurable material facts, not symbolic elemental affinities.
- Block, group and family classifications overlap; do not force them into a single exclusive axis.
- Chemical binary/ternary/four-component composition does not automatically equal two-/three-/four-primary alchemical coupling.
- “MCP-native” does not imply open source, local, unauthenticated, sovereign, or safe.
- Materials Project-backed servers depend on upstream API access, keys, terms, versions and rate limits.
- Signatures and hashes prove only defined integrity/authenticity properties, not scientific correctness.

---

**End of public materials source qualification addendum v0.1.0**
