# Symmetry, topology and domain knowledge

Structural knowledge is a cross-cutting design choice, not a separate optimizer family. These source-backed profiles distinguish construction, constrained exploration, population diversity and learned representation. Untagged entries are unassessed in this focused update, not proven to lack these features.

| Knowledge category | Role |
|---|---|
| Symmetric initialization | Generate ordered starting structures; symmetry may change later. |
| Wyckoff / site assignments | Choose compatible orbit multiplicities, species and free coordinates. |
| Symmetry-preserving exploration | Enforce crystallographic constraints during a proposal or search stage. |
| Symmetry hierarchy / diversity | Allocate exploration among symmetry classes or retain multiple classes. |
| Topology / connectivity | Use periodic nets or graph fragments, rather than only coordinates. |
| Molecular units / chemical motifs | Construct and vary reusable molecules, fragments or modules. |
| Prototypes / substitution | Transfer known structural arrangements and chemical substitutions. |
| Cation / occupation ordering | Enumerate symmetry-distinct decorations of a parent lattice. |
| Chemical / geometric plausibility | Use separation, coordination or chemical-compatibility constraints. |

Space-group symmetry differs from connectivity topology, prototype identity and geometric equivariance. A fixed symmetry can reduce search dimension but exclude the target. Template substitution differs from enumerating ordered site decorations. Supplied reference symmetry is additional input in a CSP benchmark.

## Methods, papers and implementations

## USPEX: symmetric initialization and variation

**Knowledge:** Symmetric initialization, Molecular units / chemical motifs, Chemical / geometric plausibility

Initialize symmetric candidates and favor useful local environments in variation.

**Symmetry handling:** Initial symmetry may change through variation and relaxation.

**Limits:** This is not a permanently fixed-space-group search.

**Papers:** [2013 CSP057](https://doi.org/10.1016/j.cpc.2012.12.009)

- [USPEX](software.md#uspex): [Official access portal](https://uspex-team.org/documentation.html/uspex/downloads) — Registration or request required; No source license verified.

**Evidence:** [source 1](https://doi.org/10.1016/j.cpc.2012.12.009); checked 2026-10-17.

## CALYPSO: construction and duplicate control

**Knowledge:** Symmetric initialization, Chemical / geometric plausibility

Combine symmetric generation, swarm search and bond-based duplicate rejection.

**Symmetry handling:** Construction symmetry and subsequent symmetry handling are separate settings.

**Limits:** Same symmetry or energy alone does not establish structural identity.

**Papers:** [2010 CSP043](https://doi.org/10.1103/PhysRevB.82.094116) · [2012 CSP054](https://doi.org/10.1016/j.cpc.2012.05.008)

- [CALYPSO](software.md#calypso): [Official access portal](https://download.calypso.cn/home/) — Registration or request required; No source license verified.

**Evidence:** [source 1](https://doi.org/10.1103/PhysRevB.82.094116) · [source 2](https://doi.org/10.1016/j.cpc.2012.05.008); checked 2026-10-17.

## SPAI / CALYPSO divide-and-conquer

**Knowledge:** Wyckoff / site assignments, Symmetry-preserving exploration, Symmetry hierarchy / diversity

Explore a hierarchy of space groups, Wyckoff combinations and coordinates using bee-colony-inspired roles.

**Symmetry handling:** Preserves symmetry during evolution; reported scheme excludes P1.

**Limits:** Crystallographic subspaces, not independently optimized spatial pieces. Excluding P1 restricts coverage.

**Papers:** [2022 CSP108](https://doi.org/10.1063/5.0074677)

- [SPAI / CALYPSO symmetry divide-and-conquer](software.md#symmetry-divide-conquer): [Official access portal](https://download.calypso.cn/home/) — Registration or request required; No source license verified.
- [CALYPSO](software.md#calypso): [Official access portal](https://download.calypso.cn/home/) — Registration or request required; No source license verified.

**Evidence:** [source 1](https://doi.org/10.1063/5.0074677) · [source 2](https://www.shaoxc.com/assets/pdf/publications/shao2022symmetry.pdf) · [source 3](https://calypso.cn/docs/posts/_input_parameters.html#ialgo); checked 2026-10-17.

## RandSpg

**Knowledge:** Symmetric initialization, Wyckoff / site assignments, Chemical / geometric plausibility

Generate compatible Wyckoff occupations and reject unsuitable distances.

**Symmetry handling:** Specified symmetry at construction.

**Limits:** A constructor, not a complete energy-ranking search.

**Papers:** [2017 CSP072](https://doi.org/10.1016/j.cpc.2016.12.005)

- [RandSpg](software.md#randspg): [Source code / archive](https://github.com/xtalopt/randSpg) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1016/j.cpc.2016.12.005); checked 2026-10-17.

## PyXtal

**Knowledge:** Symmetric initialization, Wyckoff / site assignments, Molecular units / chemical motifs, Chemical / geometric plausibility

Construct atomic or molecular crystals with compatible site symmetry.

**Symmetry handling:** Space, layer, rod and point-group construction; molecular site compatibility.

**Limits:** Atom counts, cell setting and molecular orientations must be compatible.

**Papers:** [2021 CSP107](https://doi.org/10.1016/j.cpc.2020.107810)

- [PyXtal](software.md#pyxtal): [Source code / archive](https://github.com/MaterSim/PyXtal) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1016/j.cpc.2020.107810); checked 2026-10-17.

## Topology-based USPEX generator

**Knowledge:** Topology / connectivity, Symmetric initialization

Decorate idealized periodic nets to create candidates for a target stoichiometry.

**Symmetry handling:** Net embedding and group relations guide candidate construction.

**Limits:** Net-library and decoration coverage limit exploration; topology differs from geometry.

**Papers:** [2019 USPEXTopology2019](https://doi.org/10.1016/j.cpc.2018.09.016)

- [USPEX](software.md#uspex): [Official access portal](https://uspex-team.org/documentation.html/uspex/downloads) — Registration or request required; No source license verified.

**Evidence:** [source 1](https://doi.org/10.1016/j.cpc.2018.09.016); checked 2026-10-17.

## MAGUS: graph fragments and symmetry mining

**Knowledge:** Topology / connectivity, Molecular units / chemical motifs, Symmetry-preserving exploration, Symmetry hierarchy / diversity

Combine graph decomposition with later space-group mining, fragment reorganization and symmetry-preserving mutation.

**Symmetry handling:** Global symmetry and local fragments guide the evolving search.

**Limits:** Source archive is public, but its academic-use terms are not an open-source license.

**Papers:** [2023 MAGUS2023](https://doi.org/10.1093/nsr/nwad128) · [2025 CSP170](https://doi.org/10.1038/s43588-025-00775-z)

- [MAGUS](software.md#magus): [Source code / archive](https://zenodo.org/records/14730874) — Source download; Restricted / non-open-source license.

**Evidence:** [source 1](https://doi.org/10.1093/nsr/nwad128) · [source 2](https://doi.org/10.1038/s43588-025-00775-z); checked 2026-10-17.

## Constrained molecular USPEX

**Knowledge:** Molecular units / chemical motifs, Symmetric initialization

Treat molecular units as whole objects in construction and variation.

**Symmetry handling:** Symmetric packing initialization with unit positions and orientations.

**Limits:** Fixed units can exclude dissociation or changes in bonding.

**Papers:** [2012 MolecularUSPEX2012](https://doi.org/10.1107/S0108768112017466)

- [USPEX](software.md#uspex): [Official access portal](https://uspex-team.org/documentation.html/uspex/downloads) — Registration or request required; No source license verified.

**Evidence:** [source 1](https://doi.org/10.1107/S0108768112017466); checked 2026-10-17.

## MC-EMMA

**Knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility

Assemble chemically informed modules for exploration of complex phase fields.

**Symmetry handling:** Modular construction does not require a single prescribed space group.

**Limits:** The available modules constrain representable chemistry.

**Papers:** [2017 CSP070](https://doi.org/10.1038/nature22374)

- [MC-EMMA](software.md#mc-emma): [Source code / archive](https://github.com/lrcfmd/MC-EMMA-stable) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1038/nature22374); checked 2026-10-17.

## FUSE / FUSE2

**Knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility

Build and rearrange cation–anion modules with stacking and coordination rules.

**Symmetry handling:** Approximate lattice types do not impose full internal symmetry.

**Limits:** Motif restrictions may exclude unusual coordination or reconstructive changes.

**Papers:** [2018 CSP083](https://doi.org/10.1039/c8fd00045j) · [2025 CSP148](https://doi.org/10.1039/d4fd00094c)

- [FUSE / FUSE2](software.md#fuse): [Source code / archive](https://github.com/lrcfmd/FUSE-stable) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1039/c8fd00045j) · [source 2](https://doi.org/10.1039/d4fd00094c); checked 2026-10-17.

## Data-mined ionic substitution

**Knowledge:** Prototypes / substitution, Chemical / geometric plausibility

Learn likely ionic substitutions while transferring a known structure type.

**Symmetry handling:** Inherited template geometry may change during relaxation.

**Limits:** Substitution alone does not specify every ordered site decoration.

**Papers:** [2011 CSP048](https://doi.org/10.1021/ic102031h)

- [Data-mined ionic substitution (pymatgen implementation)](software.md#pymatgen-ionic-substitution): [Source code / archive](https://github.com/materialsproject/pymatgen) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1021/ic102031h); checked 2026-10-17.

## TCSP / TCSP2

**Knowledge:** Prototypes / substitution, Chemical / geometric plausibility

Select and chemically adapt template structures for a specified composition.

**Symmetry handling:** Template occupations and geometry provide the starting arrangement.

**Limits:** Template coverage differs from unconstrained topology discovery.

**Papers:** [2022 CSP123](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879) · [2026 CSP194](https://www.sciencedirect.com/science/article/pii/S0927025625006603)

- [TCSP / TCSP2.0](software.md#tcsp): [Source code / archive](https://github.com/usccolumbia/TCSP) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879) · [source 2](https://www.sciencedirect.com/science/article/pii/S0927025625006603); checked 2026-10-17.

## CSPML

**Knowledge:** Prototypes / substitution

Use learned similarity to retrieve structural templates.

**Symmetry handling:** Symmetry is inherited through candidate templates.

**Limits:** A missing prototype may be difficult to recover by local relaxation.

**Papers:** [2022 CSP115](https://www.sciencedirect.com/science/article/pii/S0927025622002555)

- [CSPML](software.md#cspml): [Source code / archive](https://github.com/Minoru938/CSPML) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://www.sciencedirect.com/science/article/pii/S0927025622002555); checked 2026-10-17.

## Derivative-structure enumeration / enumlib

**Knowledge:** Cation / occupation ordering, Prototypes / substitution

Enumerate distinct parent-lattice occupations while removing symmetry-equivalent arrangements.

**Symmetry handling:** Decorations may lower parent symmetry or require supercells.

**Limits:** Completeness holds only within the chosen parent and cell-size bounds.

**Papers:** [2008 CSP035](https://doi.org/10.1103/PhysRevB.77.224115) · [2012 CSP056](https://doi.org/10.1016/j.commatsci.2012.02.015)

- [enumlib](software.md#enumlib): [Source code / archive](https://github.com/msg-byu/enumlib) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1103/PhysRevB.77.224115) · [source 2](https://doi.org/10.1016/j.commatsci.2012.02.015); checked 2026-10-17.

## AIRSS / buildcell

**Knowledge:** Symmetric initialization, Molecular units / chemical motifs, Chemical / geometric plausibility

Sample plausible starts using volume, separation, symmetry and structural-unit information.

**Symmetry handling:** Construction constraints are selected for the system and workflow.

**Limits:** Chemical constraints are domain-dependent, particularly under pressure.

**Papers:** [2006 CSP028](https://doi.org/10.1103/PhysRevLett.97.045504) · [2011 CSP045](https://doi.org/10.1088/0953-8984/23/5/053201)

- [AIRSS / buildcell](software.md#airss): [Source code / archive](https://www.mtg.msm.cam.ac.uk/Codes/AIRSS) — Source download; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1103/PhysRevLett.97.045504) · [source 2](https://doi.org/10.1088/0953-8984/23/5/053201); checked 2026-10-17.

## CMCrystalHS

**Knowledge:** Wyckoff / site assignments, Symmetry-preserving exploration

Use PyXtal assignments and differential evolution over free Wyckoff coordinates.

**Symmetry handling:** Supplied symmetry and a contact-map objective constrain reconstruction.

**Limits:** Descriptor-assisted reconstruction supplies more information than formula-only prediction.

**Papers:** [2021 CMCrystalHS2021](https://doi.org/10.1088/1361-648x/ac1d6c)

- [CMCrystalHS](software.md#cmcrystalhs): [Source code / archive](https://github.com/usccolumbia/DE-CSP-highsymmetry) — Public source repository; No source license verified.

**Evidence:** [source 1](https://doi.org/10.1088/1361-648x/ac1d6c); checked 2026-10-17.

## CRYSIM

**Knowledge:** Wyckoff / site assignments, Symmetry-preserving exploration

Encode space group, Wyckoff assignments and independent coordinates for optimization.

**Symmetry handling:** Separate discrete crystallographic choices from positional variables.

**Limits:** Results depend on encoding bounds and the energy evaluator.

**Papers:** [2025 CSP176](https://www.nature.com/articles/s42005-025-02380-y)

- [CRYSIM](software.md#crysim): [Source code / archive](https://github.com/tsudalab/CRYSIM) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://www.nature.com/articles/s42005-025-02380-y); checked 2026-10-17.

## DiffCSP++

**Knowledge:** Wyckoff / site assignments, Symmetry-preserving exploration

Constrain lattice and coordinate diffusion using crystallographic symmetry.

**Symmetry handling:** Symmetry-compatible lattice representation and Wyckoff constraints.

**Limits:** Symmetry conditioning is additional information; exact formula requires compatible counts.

**Papers:** [2024 CSP154](https://arxiv.org/abs/2402.03992)

- [DiffCSP++](software.md#diffcsp-plus-plus): [Source code / archive](https://github.com/jiaor17/DiffCSP-PP) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://arxiv.org/abs/2402.03992); checked 2026-10-17.

## CrystalFormer

**Knowledge:** Wyckoff / site assignments, Symmetry-preserving exploration, Prototypes / substitution

Generate symmetry-inequivalent site sequences; support symmetry control and substitution workflows.

**Symmetry handling:** Reconstruct complete crystals from space group and site information.

**Limits:** Original generation and later formula-conditioned CSP interfaces must be distinguished.

**Papers:** [2025 CSP177](https://doi.org/10.1016/j.scib.2025.09.035) · [2025 CrystalFormerCSP2025](https://arxiv.org/abs/2512.18251)

- [CrystalFormer](software.md#crystalformer): [Source code / archive](https://github.com/deepmodeling/CrystalFormer) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://doi.org/10.1016/j.scib.2025.09.035) · [source 2](https://arxiv.org/abs/2512.18251); checked 2026-10-17.

## SymmCD

**Knowledge:** Wyckoff / site assignments, Symmetry-preserving exploration

Learn asymmetric-unit information together with its symmetry transformations.

**Symmetry handling:** Symmetry enters the generative variables rather than only geometric equivariance.

**Limits:** Symmetry-aware generation alone does not establish exact formula conditioning.

**Papers:** [2025 CSP178](https://arxiv.org/abs/2502.03638)

- [SymmCD](software.md#symmcd): [Source code / archive](https://github.com/sibasmarak/SymmCD) — Public source repository; No source license verified.

**Evidence:** [source 1](https://arxiv.org/abs/2502.03638); checked 2026-10-17.

## ParetoCSP2

**Knowledge:** Symmetry hierarchy / diversity

Control space-group diversity within age–fitness evolutionary search.

**Symmetry handling:** Retain multiple symmetry classes across a population.

**Limits:** Different polymorphs can share the same space group.

**Papers:** [2025 CSP175](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792)

- [ParetoCSP2](software.md#paretocsp2): [Source code / archive](https://github.com/usccolumbia/ParetoCSP2) — Public source repository; Open-source license verified.

**Evidence:** [source 1](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792); checked 2026-10-17.
