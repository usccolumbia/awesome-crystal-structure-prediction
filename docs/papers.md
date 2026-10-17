# Paper catalogue

208 records, grouped by primary category. All source records are in [papers.json](../data/papers.json); citations are in [references.bib](../references.bib).

## Construction, templates and discrete search

<a id="csp001"></a>
### 1996 — Computer Prediction of Organic Crystal Structures Using Partial X-ray Diffraction Data

**CSP001 · Journal article · Molecular / organic**

Angelo Gavezzotti; Giuseppe Filippini. *Journal of the American Chemical Society*. [Paper](https://doi.org/10.1021/ja9540637)

**Method:** Experiment-constrained packing construction. Known unit-cell dimensions and space group constrain construction of complete molecular packing.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Gavezzotti–Filippini collaboration](https://pubs.acs.org/doi/abs/10.1021/ja9540637)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/ja9540637) · [source 2](https://pubs.acs.org/doi/abs/10.1021/ja9540637)

**Scope:** Requires experimental cell and symmetry information; distinguish structure solution from molecule-only prediction.

<a id="csp004"></a>
### 1997 — Enumeration of periodic tetrahedral frameworks

**CSP004 · Published journal article · Atomic / inorganic**

M. M. J. Treacy; K. H. Randall; S. Rao; J. A. Perry; D. J. Chadi. *Zeitschrift für Kristallographie - Crystalline Materials*. [Paper](https://doi.org/10.1524/zkri.1997.212.11.768)

**Method:** Enumerate symmetry-constrained four-connected graphs and refine their geometric embeddings.. Enumerate symmetry-constrained four-connected graphs and refine their geometric embeddings.

**Inputs:** Space group; number of independent tetrahedral vertices; connectivity bounds

**Software:** [Periodic tetrahedral-framework enumeration (Treacy et al.)](software.md#tetrahedral-framework-enumeration)

**Groups:** [Treacy–Randall framework-enumeration team](https://people.csail.mit.edu/randall/)

**Evidence:** Author publication list and published abstract indexed by scholarly search. [source 1](https://doi.org/10.1524/zkri.1997.212.11.768) · [source 2](https://people.csail.mit.edu/randall/)

**Scope:** Topology enumeration is finite only under declared nodality, neighbour and symmetry bounds.

<a id="csp006"></a>
### 1999 — Systematic enumeration of crystalline networks

**CSP006 · Published journal article · Atomic / inorganic**

Olaf Delgado Friedrichs; Andreas W. M. Dress; Daniel H. Huson; Jacek Klinowski; Alan L. Mackay. *Nature*. [Paper](https://doi.org/10.1038/23210)

**Method:** Use tiling theory to enumerate bounded classes of periodic four-connected crystal networks.. Use tiling theory to enumerate bounded classes of periodic four-connected crystal networks.

**Inputs:** Chosen coordination, nodality and tiling class

**Software:** [Systematic crystalline-network enumeration (Delgado Friedrichs et al.)](software.md#systematic-network-enumeration)

**Groups:** [Delgado Friedrichs–Klinowski–Mackay network-enumeration collaboration](https://www.nature.com/articles/23210)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1038/23210) · [source 2](https://www.nature.com/articles/23210)

**Scope:** Enumerates specified network classes, not every possible three-dimensional crystal net.

<a id="csp011"></a>
### 2001 — Systematic prediction of crystal structures

**CSP011 · Published journal article · Atomic / inorganic**

Björn Winkler; Chris J. Pickard; Victor Milman; Georg Thimm. *Chemical Physics Letters*. [Paper](https://doi.org/10.1016/S0009-2614(01)00126-9)

**Method:** Enumerate periodic graphs, embed candidate nets and assess structures with first-principles calculations.. Enumerate periodic graphs, embed candidate nets and assess structures with first-principles calculations.

**Inputs:** Coordination/network constraints and cell-size bound

**Software:** [Systematic periodic-network search (Winkler–Pickard–Thimm)](software.md#quotient-graph-search)

**Groups:** [Winkler–Pickard–Thimm systematic-net team](https://www.sciencedirect.com/science/article/abs/pii/S0009261401001269)

**Evidence:** Primary abstract and selected method/result sections. [source 1](https://doi.org/10.1016/S0009-2614(01)00126-9) · [source 2](https://www.sciencedirect.com/science/article/abs/pii/S0009261401001269)

**Scope:** Demonstration covers bounded small-cell sp2-carbon topologies rather than unrestricted chemistry.

<a id="csp017"></a>
### 2003 — Predicting Crystal Structures with Data Mining of Quantum Calculations

**CSP017 · Published journal article · Atomic / inorganic**

Stefano Curtarolo; Dane Morgan; Kristin Persson; John Rodgers; Gerbrand Ceder. *Physical Review Letters*. [Paper](https://doi.org/10.1103/PhysRevLett.91.135503)

**Method:** Extract correlations from computed structure libraries to prioritize candidate prototypes.. Extract correlations from computed structure libraries to prioritize candidate prototypes.

**Inputs:** Composition and library of computed prototypes

**Software:** [Data-mined prototype search (Curtarolo / Fischer / Ceder)](software.md#data-mined-prototype-search)

**Groups:** [Gerbrand Ceder / data-driven crystal modeling](https://arxiv.org/abs/cond-mat/0307262)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevLett.91.135503) · [source 2](https://arxiv.org/abs/cond-mat/0307262)

**Scope:** Prediction is restricted by the prototype library and its chemical coverage.

<a id="csp019"></a>
### 2004 — Enumeration of periodic tetrahedral frameworks. II. Polynodal graphs

**CSP019 · Published journal article · Atomic / inorganic**

M.M.J. Treacy; I. Rivin; E. Balkovsky; K.H. Randall; M.D. Foster. *Microporous and Mesoporous Materials*. [Paper](https://doi.org/10.1016/j.micromeso.2004.06.013)

**Method:** Extend symmetry-constrained intersite bonding search to polynodal periodic framework graphs.. Extend symmetry-constrained intersite bonding search to polynodal periodic framework graphs.

**Inputs:** Space group and number of unique tetrahedral vertices

**Software:** [Periodic tetrahedral-framework enumeration (Treacy et al.)](software.md#tetrahedral-framework-enumeration)

**Groups:** [Treacy–Randall framework-enumeration team](https://www.sciencedirect.com/science/article/abs/pii/S1387181104002331)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.micromeso.2004.06.013) · [source 2](https://www.sciencedirect.com/science/article/abs/pii/S1387181104002331)

**Scope:** Constrained framework enumeration does not guarantee an experimentally realizable crystal.

<a id="csp021"></a>
### 2004 — Systematic prediction of crystal structures: An application tosp3-hybridized carbon polymorphs

**CSP021 · Published journal article · Atomic / inorganic**

Rachel T. Strong; Chris J. Pickard; Victor Milman; Georg Thimm; Björn Winkler. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.70.045101)

**Method:** Apply systematic periodic-network construction and first-principles evaluation to tetrahedral carbon structures.. Apply systematic periodic-network construction and first-principles evaluation to tetrahedral carbon structures.

**Inputs:** Tetrahedral carbon bonding model and finite cell bounds

**Software:** [Systematic periodic-network search (Winkler–Pickard–Thimm)](software.md#quotient-graph-search)

**Groups:** [Winkler–Pickard–Thimm systematic-net team](https://journals.aps.org/prb/issues/70/4)

**Evidence:** Primary issue metadata and article-title method identification. [source 1](https://doi.org/10.1103/PhysRevB.70.045101) · [source 2](https://journals.aps.org/prb/issues/70/4)

**Scope:** Chemistry- and coordination-constrained enumeration; not an unrestricted CSP algorithm.

<a id="csp024"></a>
### 2005 — Inorganic structure prediction withGRINSP

**CSP024 · Published journal article · Atomic / inorganic**

Armel Le Bail. *Journal of Applied Crystallography*. [Paper](https://doi.org/10.1107/S0021889805002384)

**Method:** Use Monte Carlo construction and ideal-distance fitting to generate corner-sharing inorganic polyhedral networks.. Use Monte Carlo construction and ideal-distance fitting to generate corner-sharing inorganic polyhedral networks.

**Inputs:** Allowed polyhedra, coordination, ideal distances and cell bounds

**Software:** [GRINSP / GRINS](software.md#grinsp)

**Groups:** [Le Bail / GRINSP team](https://journals.iucr.org/j/issues/2005/02/00/cg5019/index.html)

**Evidence:** Primary abstract and selected full-text sections. [source 1](https://doi.org/10.1107/S0021889805002384) · [source 2](https://journals.iucr.org/j/issues/2005/02/00/cg5019/index.html)

**Scope:** Geometric plausibility does not establish thermodynamic stability; restricted connectivity families.

<a id="csp029"></a>
### 2006 — Predicting crystal structure by merging data mining with quantum mechanics

**CSP029 · Published journal article · Atomic / inorganic**

Christopher C. Fischer; Kevin J. Tibbetts; Dane Morgan; Gerbrand Ceder. *Nature Materials*. [Paper](https://doi.org/10.1038/nmat1691)

**Method:** Learn co-occurrence correlations among prototypes to guide quantum-mechanical structure evaluation.. Learn co-occurrence correlations among prototypes to guide quantum-mechanical structure evaluation.

**Inputs:** Chemical system and existing structural observations

**Software:** [Data-mined prototype search (Curtarolo / Fischer / Ceder)](software.md#data-mined-prototype-search)

**Groups:** [Gerbrand Ceder / data-driven crystal modeling](https://www.nature.com/articles/nmat1691)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1038/nmat1691) · [source 2](https://www.nature.com/articles/nmat1691)

**Scope:** Data-driven prototype selection cannot represent arbitrary unseen structure types.

<a id="csp035"></a>
### 2008 — Algorithm for generating derivative structures

**CSP035 · Published journal article · Atomic / inorganic**

Gus L. W. Hart; Rodney W. Forcade. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.77.224115)

**Method:** Enumerate symmetry-distinct superlattices and atomic decorations of a supplied parent structure.. Enumerate symmetry-distinct superlattices and atomic decorations of a supplied parent structure.

**Inputs:** Parent lattice; species; supercell-size bounds

**Structural knowledge:** Cation / occupation ordering, Prototypes / substitution — [Mechanisms and limits](structural-priors.md)

**Software:** [enumlib](software.md#enumlib)

**Groups:** [Hart–Forcade enumeration team](https://doi.org/10.1103/PhysRevB.77.224115)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevB.77.224115)

**Scope:** Complete only within the specified parent lattice and finite supercell bound; not all crystal topologies.

<a id="csp048"></a>
### 2011 — Data Mined Ionic Substitutions for the Discovery of New Compounds

**CSP048 · Published journal article · Atomic / inorganic**

Geoffroy Hautier; Chris Fischer; Virginie Ehrlacher; Anubhav Jain; Gerbrand Ceder. *Inorganic Chemistry*. [Paper](https://doi.org/10.1021/ic102031h)

**Method:** Use learned ionic-substitution probabilities to propose composition–structure candidates from known templates.. Use learned ionic-substitution probabilities to propose composition–structure candidates from known templates.

**Inputs:** Known ionic crystal templates and substitution species

**Structural knowledge:** Chemical / geometric plausibility, Prototypes / substitution — [Mechanisms and limits](structural-priors.md)

**Software:** [Data-mined ionic substitution (pymatgen implementation)](software.md#pymatgen-ionic-substitution)

**Groups:** [Gerbrand Ceder / data-driven crystal modeling](https://pubs.acs.org/doi/abs/10.1021/ic102031h)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1021/ic102031h) · [source 2](https://pubs.acs.org/doi/abs/10.1021/ic102031h)

**Scope:** Template-based crystal discovery rather than an unrestricted fixed-formula global search.

<a id="csp056"></a>
### 2012 — Generating derivative structures at a fixed concentration

**CSP056 · Published journal article · Atomic / inorganic**

Gus L.W. Hart; Lance J. Nelson; Rodney W. Forcade. *Computational Materials Science*. [Paper](https://doi.org/10.1016/j.commatsci.2012.02.015)

**Method:** Enumerate distinct atomic decorations efficiently while fixing composition.. Enumerate distinct atomic decorations efficiently while fixing composition.

**Inputs:** Parent lattice; fixed concentrations; cell bounds

**Structural knowledge:** Cation / occupation ordering, Prototypes / substitution — [Mechanisms and limits](structural-priors.md)

**Software:** [enumlib](software.md#enumlib)

**Groups:** [Hart–Forcade enumeration team](https://www.sciencedirect.com/science/article/abs/pii/S092702561200081X)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.commatsci.2012.02.015) · [source 2](https://www.sciencedirect.com/science/article/abs/pii/S092702561200081X)

**Scope:** Search completeness is limited to the chosen parent lattice and cell bounds.

<a id="csp067"></a>
### 2016 — Generation of crystal structures using known crystal structures as analogues

**CSP067 · Journal article · Molecular / organic**

Jason C. Cole; Colin R. Groom; Murray G. Read; Ilenia Giangreco; Patrick McCabe; Anthony M. Reilly; Gregory P. Shields. *Acta Crystallographica Section B Structural Science, Crystal Engineering and Materials*. [Paper](https://doi.org/10.1107/S2052520616006533)

**Method:** Shape-matched database templates. Retrieve molecular-shape analogues from the CSD and adapt their lattices to initialize crystal minimization.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Cole / CCDC shape-analogue collaboration](https://journals.iucr.org/b/issues/2016/04/00/gp5082/index.html)

**Evidence:** Primary selected methods/results. [source 1](https://doi.org/10.1107/S2052520616006533) · [source 2](https://journals.iucr.org/b/issues/2016/04/00/gp5082/index.html)

**Scope:** Requires suitable database analogues; conformational flexibility, special sites and multicomponent cases need further development.

<a id="uspextopology2019"></a>
### 2019 — Topology-based crystal structure generator

**USPEXTopology2019 · Published journal article · Atomic / inorganic**

Pavel V. Bushlanov; Vladislav A. Blatov; Artem R. Oganov. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2018.09.016)

**Method:** Topological net construction for evolutionary CSP. Select suitable idealized periodic nets, decorate for the target stoichiometry, and use candidates directly or within evolutionary search.

**Inputs:** Composition, permitted cell sizes and a periodic-net library

**Structural knowledge:** Symmetric initialization, Topology / connectivity — [Mechanisms and limits](structural-priors.md)

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://doi.org/10.1016/j.cpc.2018.09.016)

**Evidence:** Primary paper and developer descriptions; Crossref title/authors verified. [source 1](https://doi.org/10.1016/j.cpc.2018.09.016)

**Scope:** Finite net-library and decoration coverage; topology is not a fixed space-group label.

<a id="csp108"></a>
### 2022 — A symmetry-orientated divide-and-conquer method for crystal structure prediction

**CSP108 · Published journal paper · Atomic / inorganic**

Xuecheng Shao; Jian Lv; Peng Liu; Sen Shao; Pengyue Gao; Hanyu Liu; Yanchao Wang; Yanming Ma. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/5.0074677)

**Method:** A symmetry tree partitions the search space and a learned strategy selects subspaces.. Composition → symmetry-dependent subspaces → adaptive selection → symmetry-preserving search

**Inputs:** Composition and symmetry representations

**Structural knowledge:** Symmetry hierarchy / diversity, Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [SPAI / CALYPSO symmetry divide-and-conquer](software.md#symmetry-divide-conquer) · [CALYPSO](software.md#calypso)

**Groups:** [Yanming Ma–Yanchao Wang / CALYPSO collaboration](https://doi.org/10.1063/5.0074677)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1063/5.0074677)

**Scope:** Partitioning and symmetry preservation reduce search complexity but may emphasize preferred symmetry subspaces.

<a id="csp115"></a>
### 2022 — Crystal structure prediction with machine learning-based element substitution

**CSP115 · Published journal article · Atomic / inorganic**

Minoru Kusaba; Chang Liu; Ryo Yoshida. *Computational Materials Science*. [Paper](https://www.sciencedirect.com/science/article/pii/S0927025622002555)

**Method:** CSPML metric-learning template selection. Formula → classify template isomorphism → select database templates → element substitution → relaxation

**Inputs:** Query composition and structure database

**Structural knowledge:** Prototypes / substitution — [Mechanisms and limits](structural-priors.md)

**Software:** [CSPML](software.md#cspml)

**Groups:** [Ryo Yoshida / Kusaba–Liu collaboration](https://www.sciencedirect.com/science/article/pii/S0927025622002555)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://www.sciencedirect.com/science/article/pii/S0927025622002555) · [source 2](https://github.com/Minoru938/CSPML)

**Scope:** Cannot recover a genuinely absent structural prototype through substitution alone; classification accuracy is not full-structure recovery.

<a id="csp123"></a>
### 2022 — TCSP: a Template-Based Crystal Structure Prediction Algorithm for Materials Discovery

**CSP123 · Published journal article · Atomic / inorganic**

Lai Wei; Nihang Fu; Edirisuriya M. D. Siriwardane; Wenhui Yang; Sadman Sadeed Omee; Rongzhi Dong; Rui Xin; Jianjun Hu. *Inorganic Chemistry*. [Paper](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879)

**Method:** TCSP chemistry-informed template matching / substitution. Formula → chemistry / oxidation-state template ranking → substitute elements → candidate structures

**Inputs:** Query composition and known templates

**Structural knowledge:** Chemical / geometric plausibility, Prototypes / substitution — [Mechanisms and limits](structural-priors.md)

**Software:** [TCSP / TCSP2.0](software.md#tcsp)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879)

**Evidence:** Author paper PDF abstract and PubMed author metadata. [source 1](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879) · [source 2](https://pubmed.ncbi.nlm.nih.gov/35420427/) · [source 3](https://par.nsf.gov/servlets/purl/10359253)

**Scope:** Template availability constrains attainable prototypes; leave-one-out formula evaluation is not a held-out prototype test.

<a id="csp133"></a>
### 2023 — Optimality guarantees for crystal structure prediction

**CSP133 · Published journal paper · Atomic / inorganic**

Vladimir V. Gusev; Duncan Adamson; Argyrios Deligkas; Dmytro Antypov; Christopher M. Collins; Piotr Krysta; Igor Potapov; George R. Darling; Matthew S. Dyer; Paul Spirakis; Matthew J. Rosseinsky. *Nature*. [Paper](https://doi.org/10.1038/s41586-023-06071-y)

**Method:** Integer programming solves periodic lattice allocation, followed by continuous local relaxation.. Composition + discrete grid + pair energy → exact allocation optimization → local minimization

**Inputs:** Composition, cell/grid and specified interaction model

**Software:** [IPCSP (integer-programming CSP)](software.md#ipcsp)

**Groups:** [Spirakis–Gusev–Rosseinsky / exact CSP collaboration](https://doi.org/10.1038/s41586-023-06071-y)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1038/s41586-023-06071-y)

**Scope:** Optimality is conditional on the modeled/discretized problem and the paper’s assumptions; this is not an unrestricted guarantee for arbitrary DFT crystals.

<a id="csp176"></a>
### 2025 — Predicting symmetric structures of large crystals with GPU-based Ising machines

**CSP176 · Published journal paper · Atomic / inorganic**

Chen Liang; Diptesh Das; Jiang Guo; Ryo Tamura; Zetian Mao; Koji Tsuda. *Communications Physics*. [Paper](https://www.nature.com/articles/s42005-025-02380-y)

**Method:** CRYSIM encodes symmetry and site variables for optimization with a GPU-based Ising machine.. Composition → space group / Wyckoff / coordinate encoding → Ising optimization → geometric relaxation

**Inputs:** Composition, symmetry encoding and objective evaluator

**Structural knowledge:** Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [CRYSIM](software.md#crysim)

**Groups:** [Yamashita–Tsuda / adaptive CSP collaboration](https://www.nature.com/articles/s42005-025-02380-y)

**Evidence:** Primary abstract, author list and selected introduction; no independent reproduction. [source 1](https://www.nature.com/articles/s42005-025-02380-y)

**Scope:** GPU-based Ising optimization in the reported implementation; proposed quantum compatibility is not demonstrated quantum advantage.

<a id="csp194"></a>
### 2026 — TCSP 2.0: Template based crystal structure prediction with improved oxidation state prediction and chemistry heuristics

**CSP194 · Published journal article · Atomic / inorganic**

Lai Wei; Rongzhi Dong; Nihang Fu; Sadman Sadeed Omee; Jianjun Hu. *Computational Materials Science*. [Paper](https://www.sciencedirect.com/science/article/pii/S0927025625006603)

**Method:** TCSP2.0: learned oxidation states, element embeddings and symmetry voting. Formula → BERTOS oxidation states → embedding-ranked templates → symmetry voting → substitution

**Inputs:** Composition and crystal-template database

**Structural knowledge:** Chemical / geometric plausibility, Prototypes / substitution — [Mechanisms and limits](structural-priors.md)

**Software:** [TCSP / TCSP2.0](software.md#tcsp)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://www.sciencedirect.com/science/article/pii/S0927025625006603)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://www.sciencedirect.com/science/article/pii/S0927025625006603) · [source 2](https://arxiv.org/abs/2503.23183)

**Scope:** January2026 volume, DOI and preprint2025. Template dependence still limits novel-prototype recovery.

## Random structure search

<a id="csp008"></a>
### 1999 — Upack program package for crystal structure prediction: Force fields and crystal structure generation for small carbohydrate molecules

**CSP008 · Journal article · Molecular / organic**

Bouke P. van Eijck; Jan Kroon. *Journal of Computational Chemistry*. [Paper](https://doi.org/10.1002/(SICI)1096-987X(199906)20:8<799::AID-JCC6>3.0.CO;2-Z)

**Method:** Molecular packing generation and force-field minimization. Generate molecular crystal packings, locally minimize and rank with molecular force fields.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [UPACK](software.md#upack)

**Groups:** [van Eijck–Kroon / UPACK](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1096-987X(199906)20:8%3C799::AID-JCC6%3E3.0.CO;2-Z)

**Evidence:** Publisher DOI citation plus indexed author/title metadata; cited by primary subsequent papers. [source 1](https://doi.org/10.1002/(SICI)1096-987X(199906)20:8<799::AID-JCC6>3.0.CO;2-Z) · [source 2](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1096-987X(199906)20:8%3C799::AID-JCC6%3E3.0.CO;2-Z) · [source 3](https://cir.nii.ac.jp/crid/1360574094354920192)

**Scope:** Search coverage and ranking depend on molecular flexibility and force-field quality.

<a id="csp023"></a>
### 2005 — Ab initio crystal structure prediction—I. Rigid molecules

**CSP023 · Journal article · Molecular / organic**

Panagiotis G. Karamertzanis; Constantinos C. Pantelides. *Journal of Computational Chemistry*. [Paper](https://doi.org/10.1002/jcc.20165)

**Method:** CrystalPredictor global lattice-enthalpy minimization. Extensive packing proposals followed by local enthalpy minimization using QM-derived distributed charges.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CrystalPredictor / CrystalPredictor II](software.md#crystalpredictor)

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://pubmed.ncbi.nlm.nih.gov/15622548/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1002/jcc.20165) · [source 2](https://pubmed.ncbi.nlm.nih.gov/15622548/)

**Scope:** Rigid molecular identities; known experimental structures need not be global minima of the approximate model.

<a id="csp028"></a>
### 2006 — High-Pressure Phases of Silane

**CSP028 · Published journal article · Atomic / inorganic**

Chris J. Pickard; R. J. Needs. *Physical Review Letters*. [Paper](https://doi.org/10.1103/PhysRevLett.97.045504)

**Method:** Introduce random initialization followed by first-principles enthalpy relaxation for crystal prediction.. Introduce random initialization followed by first-principles enthalpy relaxation for crystal prediction.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility, Symmetric initialization — [Mechanisms and limits](structural-priors.md)

**Software:** [AIRSS / buildcell](software.md#airss)

**Groups:** [Pickard–Needs / AIRSS collaboration](https://arxiv.org/abs/cond-mat/0604454)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevLett.97.045504) · [source 2](https://arxiv.org/abs/cond-mat/0604454)

**Scope:** Foundational small-cell demonstration; random-search difficulty grows with cell complexity.

<a id="csp031"></a>
### 2007 — Ab initiocrystal structure prediction. II. Flexible molecules

**CSP031 · Journal article · Molecular / organic**

P. G. Karamertzanis†; C. C. Pantelides. *Molecular Physics*. [Paper](https://doi.org/10.1080/00268970601143317)

**Method:** Flexible-fragment CrystalPredictor. Treat connected rigid fragments with torsional flexibility and QM-derived intramolecular energy surfaces.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CrystalPredictor / CrystalPredictor II](software.md#crystalpredictor)

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://www.tandfonline.com/doi/abs/10.1080/00268970601143317)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1080/00268970601143317) · [source 2](https://www.tandfonline.com/doi/abs/10.1080/00268970601143317)

**Scope:** Intramolecular interpolation accuracy and conformational coverage constrain performance.

<a id="csp039"></a>
### 2009 — Can the Formation of Pharmaceutical Cocrystals Be Computationally Predicted? 2. Crystal Structure Prediction

**CSP039 · Journal article · Molecular / organic**

Panagiotis G. Karamertzanis; Andrei V. Kazantsev; Nizar Issa; Gareth W.A. Welch; Claire S. Adjiman; Constantinos C. Pantelides; Sarah L. Price. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/ct8004326)

**Method:** Multistage cocrystal lattice-energy search. Generate flexible multicomponent packings with approximate charge and intramolecular models; refine promising minima.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://pubmed.ncbi.nlm.nih.gov/26609729/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/ct8004326) · [source 2](https://pubmed.ncbi.nlm.nih.gov/26609729/)

**Scope:** Requires selected molecular species/stoichiometry; cocrystal formation competes with pure phases.

<a id="csp063"></a>
### 2015 — Efficient Handling of Molecular Flexibility in Ab Initio Generation of Crystal Structures

**CSP063 · Journal article · Molecular / organic**

Matthew Habgood; Isaac J. Sugden; Andrei V. Kazantsev; Claire S. Adjiman; Constantinos C. Pantelides. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/ct500621v)

**Method:** CrystalPredictor II and local approximate intramolecular models. Quasi-random packing and conformational exploration using improved local representations of intramolecular energy.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CrystalPredictor / CrystalPredictor II](software.md#crystalpredictor)

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://pubs.acs.org/doi/abs/10.1021/ct500621v)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/ct500621v) · [source 2](https://pubs.acs.org/doi/abs/10.1021/ct500621v)

**Scope:** Global coverage still depends on conformer/space-group choices and computational budget.

<a id="csp066"></a>
### 2016 — Convergence Properties of Crystal Structure Prediction by Quasi-Random Sampling

**CSP066 · Journal article · Molecular / organic**

David H. Case; Josh E. Campbell; Peter J. Bygrave; Graeme M. Day. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/acs.jctc.5b01112)

**Method:** Low-discrepancy quasi-random packing (GLEE). Build valid rigid-molecule packings from quasi-random sequences, locally minimize, cluster repeated structures and monitor convergence.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GLEE (Global Lattice Energy Explorer)](software.md#glee) · [mol-CSPy: quasi-random sampling, QRBH and threshold MC](software.md#mol-cspy)

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://pubmed.ncbi.nlm.nih.gov/26716361/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/acs.jctc.5b01112) · [source 2](https://pubmed.ncbi.nlm.nih.gov/26716361/)

**Scope:** Low-energy minima are often found early, but higher-energy coverage can require much longer sampling; finite convergence evidence is not exhaustive proof.

<a id="csp071"></a>
### 2017 — Functional materials discovery using energy–structure–function maps

**CSP071 · Journal article · Molecular / organic**

Angeles Pulido; Linjiang Chen; Tomasz Kaczorowski; Daniel Holden; Marc A. Little; Samantha Y. Chong; Benjamin J. Slater; David P. McMahon; Baltasar Bonillo; Chloe J. Stackhouse; Andrew Stephenson; Christopher M. Kane; Rob Clowes; Tom Hasell; Andrew I. Cooper; Graeme M. Day. *Nature*. [Paper](https://doi.org/10.1038/nature21419)

**Method:** Energy–structure–function maps. Molecular CSP generates packings; property calculations map prospective functions onto each energy landscape to guide experiment.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GLEE (Global Lattice Energy Explorer)](software.md#glee)

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://www.nature.com/articles/nature21419)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1038/nature21419) · [source 2](https://www.nature.com/articles/nature21419)

**Scope:** Molecular design and property selection are downstream from fixed-molecule CSP; low-energy landscapes do not alone establish accessibility.

<a id="csp072"></a>
### 2017 — RandSpg: An open-source program for generating atomistic crystal structures with specific spacegroups

**CSP072 · Published journal article · Atomic / inorganic**

Patrick Avery; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2016.12.005)

**Method:** Enumerate compatible Wyckoff combinations and randomly populate them under distance constraints.. Enumerate compatible Wyckoff combinations and randomly populate them under distance constraints.

**Inputs:** Composition; chosen space groups; cell/distance bounds

**Structural knowledge:** Chemical / geometric plausibility, Symmetric initialization, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [RandSpg](software.md#randspg)

**Groups:** [Zurek / XtalOpt team](https://researchconnect.buffalo.edu/en/publications/randspg-an-open-source-program-for-generating-atomistic-crystal-s/)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2016.12.005) · [source 2](https://researchconnect.buffalo.edu/en/publications/randspg-an-open-source-program-for-generating-atomistic-crystal-s/)

**Scope:** Symmetry-compatible proposals require downstream relaxation and ranking; generation alone is not CSP completion.

<a id="csp079"></a>
### 2018 — Genarris: Random generation of molecular crystal structures and fast screening with a Harris approximation

**CSP079 · Journal article · Molecular / organic**

Xiayue Li; Farren S. Curtis; Timothy Rose; Christoph Schober; Alvaro Vazquez-Mayagoitia; Karsten Reuter; Harald Oberhofer; Noa Marom. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/1.5014038)

**Method:** Random physical packing plus diversity clustering. Generate physically constrained rigid-molecule packings, cluster by packing similarity and screen with Harris-approximation DFT.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Genarris (1.0–3.x; Rigid Press)](software.md#genarris)

**Groups:** [Marom / Genarris–GAtor collaboration](https://arxiv.org/abs/1803.02145)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1063/1.5014038) · [source 2](https://arxiv.org/abs/1803.02145)

**Scope:** Rigid-molecule search; screening approximations require final relaxation and ranking.

<a id="csp082"></a>
### 2018 — Prediction of novel high-pressure H2O -NaCl and carbon oxide compounds with a symmetry-driven structure search algorithm

**CSP082 · Published journal article · Atomic / inorganic**

Rustin Domingos; Kareemullah M. Shaik; Burkhard Militzer. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.98.174107)

**Method:** Randomly sample space groups and Wyckoff positions before DFT relaxation.. Randomly sample space groups and Wyckoff positions before DFT relaxation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [Symmetry-driven structure search (Domingos–Shaik–Militzer)](software.md#symmetry-driven-random-search)

**Groups:** [Militzer / SYDSS team](https://arxiv.org/abs/1811.01462)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevB.98.174107) · [source 2](https://arxiv.org/abs/1811.01462)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp096"></a>
### 2020 — Genarris 2.0: A random structure generator for molecular crystals

**CSP096 · Journal article · Molecular / organic**

Rithwik Tom; Timothy Rose; Imanuel Bier; Harriet O’Brien; Álvaro Vázquez-Mayagoitia; Noa Marom. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2020.107170)

**Method:** Space-group/Wyckoff-aware random generation. Use learned volume estimates, special Wyckoff positions, hierarchical contact checks and parallel user-defined workflows.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Genarris (1.0–3.x; Rigid Press)](software.md#genarris)

**Groups:** [Marom / Genarris–GAtor collaboration](https://www.sciencedirect.com/science/article/pii/S0010465520300242)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1016/j.cpc.2020.107170) · [source 2](https://www.sciencedirect.com/science/article/pii/S0010465520300242)

**Scope:** Semi-rigid molecules without bond-rotational degrees of freedom in this version.

<a id="csp107"></a>
### 2021 — PyXtal: A Python library for crystal structure generation and symmetry analysis

**CSP107 · Published journal article · Cross-domain**

Scott Fredericks; Kevin Parrish; Dean Sayre; Qiang Zhu. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2020.107810)

**Method:** Generate atomic or molecular structures consistent with specified symmetry and Wyckoff-site compatibility.. Generate atomic or molecular structures consistent with specified symmetry and Wyckoff-site compatibility.

**Inputs:** Composition; symmetry group; optional molecular geometry

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility, Symmetric initialization, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [PyXtal](software.md#pyxtal)

**Groups:** [Qiang Zhu / crystal search and generation](https://www.sciencedirect.com/science/article/pii/S0010465520304057)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2020.107810) · [source 2](https://www.sciencedirect.com/science/article/pii/S0010465520304057)

**Scope:** Candidate generator; energetic search and validation require an external workflow.

<a id="csp165"></a>
### 2025 — Beyond theory-driven discovery: introducing hot random search and datum-derived structures

**CSP165 · Published journal article · Atomic / inorganic**

Chris J. Pickard. *Faraday Discussions*. [Paper](https://doi.org/10.1039/D4FD00134F)

**Method:** Add MLIP-accelerated annealing to random search and generate structures by matching reference environment descriptors.. Add MLIP-accelerated annealing to random search and generate structures by matching reference environment descriptors.

**Inputs:** Composition and conditions; reference structure for datum-derived branch

**Software:** [AIRSS / buildcell](software.md#airss)

**Groups:** [Pickard–Needs / AIRSS collaboration](https://pubs.rsc.org/en/content/articlehtml/2025/fd/d4fd00134f)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1039/D4FD00134F) · [source 2](https://pubs.rsc.org/en/content/articlehtml/2025/fd/d4fd00134f)

**Scope:** MLIP reliability and reference descriptor restrict extrapolation; datum-derived generation is a separate branch from unbiased random sampling.

<a id="csp171"></a>
### 2025 — Genarris 3.0: Generating Close-Packed Molecular Crystal Structures with Rigid Press

**CSP171 · Journal article · Molecular / organic**

Yi Yang; Rithwik Tom; Jose A. G. L. Wui; Jonathan E. Moussa; Noa Marom. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/acs.jctc.5c01080)

**Method:** Rigid Press random generation with hierarchical MLIP screening. Compress generated cells using a symmetry-preserving regularized hard-sphere potential; relax and down-select using learned potentials and DFT.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Genarris (1.0–3.x; Rigid Press)](software.md#genarris)

**Groups:** [Marom / Genarris–GAtor collaboration](https://pubs.acs.org/doi/10.1021/acs.jctc.5c01080)

**Evidence:** Primary selected abstract/conclusions. [source 1](https://doi.org/10.1021/acs.jctc.5c01080) · [source 2](https://pubs.acs.org/doi/10.1021/acs.jctc.5c01080)

**Scope:** Rigid-molecule generator can start from conformer ensembles; multiple independent molecules in asymmetric unit remain future development.

## Evolutionary and genetic search

<a id="csp007"></a>
### 1999 — The prediction of inorganic crystal structures using a genetic algorithm and energy minimisation

**CSP007 · Published journal article · Atomic / inorganic**

Scott M. Woodley; Peter D. Battle; Julian D. Gale; C Richard A. Catlow. *Physical Chemistry Chemical Physics*. [Paper](https://doi.org/10.1039/A901227C)

**Method:** Evolve ionic arrangements using bond-valence fitness and relax promising structures with lattice potentials.. Evolve ionic arrangements using bond-valence fitness and relax promising structures with lattice potentials.

**Inputs:** Unit-cell dimensions and constituent elements

**Software:** [Ionic-crystal genetic algorithm (Woodley et al.)](software.md#woodley-ga)

**Groups:** [Woodley–Catlow–Gale–Battle team](https://pubs.rsc.org/en/content/articlelanding/1999/cp/a901227c)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1039/A901227C) · [source 2](https://pubs.rsc.org/en/content/articlelanding/1999/cp/a901227c)

**Scope:** Requires cell dimensions and transferable ionic potentials; not an unconstrained cell search.

<a id="csp013"></a>
### 2002 — Combined Electronic Structure and Evolutionary Search Approach to Materials Design

**CSP013 · Published journal article · Atomic / inorganic**

G. H. Jóhannesson; T. Bligaard; A. V. Ruban; H. L. Skriver; K. W. Jacobsen; J. K. Nørskov. *Physical Review Letters*. [Paper](https://doi.org/10.1103/PhysRevLett.88.255506)

**Method:** Combine DFT with evolutionary selection among compositionally decorated fcc and bcc alloy prototypes.. Combine DFT with evolutionary selection among compositionally decorated fcc and bcc alloy prototypes.

**Inputs:** Selected metal elements and fcc/bcc prototype set

**Software:** [Evolutionary alloy-prototype search (Jóhannesson et al.)](software.md#norskov-alloy-search)

**Groups:** [Nørskov–Jacobsen alloy-search collaboration](https://link.aps.org/pdf/10.1103/PhysRevLett.88.255506)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevLett.88.255506) · [source 2](https://link.aps.org/pdf/10.1103/PhysRevLett.88.255506)

**Scope:** Fixed-parent alloy search; does not search arbitrary crystal topologies.

<a id="csp015"></a>
### 2002 — Modified genetic algorithm to model crystal structures. I. Benzene, naphthalene and anthracene

**CSP015 · Journal article · Molecular / organic**

Victor E. Bazterra; Marta B. Ferraro; Julio C. Facelli. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/1.1458547)

**Method:** Real-valued molecular crystal genetic algorithm. Encode molecular positions and orientations; genetic selection and variation search packing minima.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Modified genetic algorithm for molecular crystals (Bazterra–Ferraro–Facelli)](software.md#bazterra-modified-ga)

**Groups:** [Bazterra–Ferraro–Facelli / MGAC](https://journals.iucr.org/b/issues/2005/05/00/de5014/de5014sup2.pdf)

**Evidence:** Primary blind-test methods supplement and review reference; publisher citation metadata. [source 1](https://doi.org/10.1063/1.1458547) · [source 2](https://journals.iucr.org/b/issues/2005/05/00/de5014/de5014sup2.pdf) · [source 3](https://www.tandfonline.com/doi/pdf/10.1080/0889311X.2010.517526)

**Scope:** Rigid-molecule examples and empirical potential; exact physical polymorph ordering is evaluator dependent.

<a id="csp016"></a>
### 2003 — Modified genetic algorithm to model crystal structures: III. Determination of crystal structures allowing simultaneous molecular geometry relaxation

**CSP016 · Journal article · Molecular / organic**

Victor E. Bazterra; Marta B. Ferraro; Julio C. Facelli. *International Journal of Quantum Chemistry*. [Paper](https://doi.org/10.1002/qua.10726)

**Method:** Flexible-molecule genetic search. Extend MGAC to optimize molecular internal geometry together with crystal packing.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Modified genetic algorithm for molecular crystals (Bazterra–Ferraro–Facelli)](software.md#bazterra-modified-ga)

**Groups:** [Bazterra–Ferraro–Facelli / MGAC](https://ri.conicet.gov.ar/bitstream/handle/11336/74197/CONICET_Digital_Nro.378b8372-ae0d-4603-aa73-2ae81eaacc63_A.pdf?sequence=2)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1002/qua.10726) · [source 2](https://ri.conicet.gov.ar/bitstream/handle/11336/74197/CONICET_Digital_Nro.378b8372-ae0d-4603-aa73-2ae81eaacc63_A.pdf?sequence=2)

**Scope:** Tests on L- and DL-alanine; simultaneous flexibility expands search complexity.

<a id="csp026"></a>
### 2006 — A periodic genetic algorithm with real-space representation for crystal structure and polymorph prediction

**CSP026 · Published journal article · Atomic / inorganic**

N. L. Abraham; M. I. J. Probert. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.73.224104)

**Method:** Apply real-space periodic crossover to jointly search cell shape and atomic arrangement.. Apply real-space periodic crossover to jointly search cell shape and atomic arrangement.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [Periodic real-space genetic algorithm (Abraham–Probert)](software.md#periodic-ga-abraham-probert)

**Groups:** [Probert–Abraham periodic-GA team](https://arxiv.org/abs/cond-mat/0605066)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevB.73.224104) · [source 2](https://arxiv.org/abs/cond-mat/0605066)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp027"></a>
### 2006 — Crystal structure prediction using ab initio evolutionary techniques: Principles and applications

**CSP027 · Published journal article · Atomic / inorganic**

Artem R. Oganov; Colin W. Glass. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/1.2210932)

**Method:** Combine specialized real-space evolutionary variation with first-principles local relaxation.. Combine specialized real-space evolutionary variation with first-principles local relaxation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://arxiv.org/abs/0911.3186)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1063/1.2210932) · [source 2](https://arxiv.org/abs/0911.3186)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp030"></a>
### 2006 — USPEX—Evolutionary crystal structure prediction

**CSP030 · Published journal article · Atomic / inorganic**

Colin W. Glass; Artem R. Oganov; Nikolaus Hansen. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2006.07.020)

**Method:** Implement composition-constrained evolutionary crystal search using heredity, mutation, selection and relaxation.. Implement composition-constrained evolutionary crystal search using heredity, mutation, selection and relaxation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://uspex-team.org/static/file/CPC-USPEX-2006.pdf)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2006.07.020) · [source 2](https://uspex-team.org/static/file/CPC-USPEX-2006.pdf)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp033"></a>
### 2007 — Global space-group optimization problem: Finding the stablest crystal structure without constraints

**CSP033 · Published journal article · Atomic / inorganic**

Giancarlo Trimarchi; Alex Zunger. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.75.104113)

**Method:** Evolve lattice vectors and atomic decorations after transforming dissimilar parent cells to a common basis.. Evolve lattice vectors and atomic decorations after transforming dissimilar parent cells to a common basis.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [GSGO (global space-group optimization)](software.md#gsgo)

**Groups:** [Zunger–Trimarchi / GSGO team](https://www.colorado.edu/faculty/zunger-matter-by-design/sites/default/files/attached-files/540.pdf)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevB.75.104113) · [source 2](https://www.colorado.edu/faculty/zunger-matter-by-design/sites/default/files/attached-files/540.pdf)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp037"></a>
### 2008 — Improved real-space genetic algorithm for crystal structure and polymorph prediction

**CSP037 · Published journal article · Atomic / inorganic**

N. L. Abraham; M. I. J. Probert. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.77.134117)

**Method:** Improve periodic real-space genetic search for low-enthalpy crystal structures.. Improve periodic real-space genetic search for low-enthalpy crystal structures.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [Periodic real-space genetic algorithm (Abraham–Probert)](software.md#periodic-ga-abraham-probert)

**Groups:** [Probert–Abraham periodic-GA team](https://doi.org/10.1103/PhysRevB.77.134117)

**Evidence:** Primary bibliographic metadata; cited-method summary. [source 1](https://doi.org/10.1103/PhysRevB.77.134117)

**Scope:** A published 2016 erratum exists: DOI10.1103/PhysRevB.94.059904; finite-search and evaluator limitations remain.

<a id="csp044"></a>
### 2010 — How to predict very large and complex crystal structures

**CSP044 · Published journal article · Atomic / inorganic**

Andriy O. Lyakhov; Artem R. Oganov; Mario Valle. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2010.06.007)

**Method:** Improve evolutionary diversity through fingerprints, local order and cell splitting.. Improve evolutionary diversity through fingerprints, local order and cell splitting.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://uspex-team.org/static/file/USPEX-LargeComplexSystems-2010.pdf)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2010.06.007) · [source 2](https://uspex-team.org/static/file/USPEX-LargeComplexSystems-2010.pdf)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp052"></a>
### 2011 — XtalOpt version r7: An open-source evolutionary algorithm for crystal structure prediction

**CSP052 · Published journal article · Atomic / inorganic**

David C. Lonie; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2011.06.003)

**Method:** Software version announcement updating the XtalOpt evolutionary search implementation.. Software version announcement updating the XtalOpt evolutionary search implementation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained publication list and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2011.06.003) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Version announcement, not a separate global-search paradigm.

<a id="csp053"></a>
### 2011 — XtalOpt: An open-source evolutionary algorithm for crystal structure prediction

**CSP053 · Published journal article · Atomic / inorganic**

David C. Lonie; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2010.07.048)

**Method:** Implement asynchronous evolutionary CSP with ripple mutations, hybrid operators and duplicate control.. Implement asynchronous evolutionary CSP with ripple mutations, hybrid operators and duplicate control.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://www.sciencedirect.com/science/article/abs/pii/S0010465510003140)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2010.07.048) · [source 2](https://www.sciencedirect.com/science/article/abs/pii/S0010465510003140)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="molecularuspex2012"></a>
### 2012 — Constrained evolutionary algorithm for structure prediction of molecular crystals: methodology and applications

**MolecularUSPEX2012 · Published journal article · Molecular / organic**

Qiang Zhu; Artem R. Oganov; Colin W. Glass; Harold T. Stokes. *Acta Crystallographica Section B Structural Science*. [Paper](https://doi.org/10.1107/S0108768112017466)

**Method:** Constrained molecular evolutionary CSP. Construct and vary packings of molecular units; sample symmetry and relax candidate crystals.

**Inputs:** Molecular units, composition and search bounds

**Structural knowledge:** Molecular units / chemical motifs, Symmetric initialization — [Mechanisms and limits](structural-priors.md)

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://doi.org/10.1107/S0108768112017466)

**Evidence:** Primary paper and developer descriptions; Crossref title/authors verified. [source 1](https://doi.org/10.1107/S0108768112017466)

**Scope:** Constraining units can exclude alternative bonding or dissociation.

<a id="csp057"></a>
### 2013 — New developments in evolutionary structure prediction algorithm USPEX

**CSP057 · Published journal article · Atomic / inorganic**

Andriy O. Lyakhov; Artem R. Oganov; Harold T. Stokes; Qiang Zhu. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2012.12.009)

**Method:** Combine random symmetric initialization, environment-aware variation and antiseeds to reduce search trapping.. Combine random symmetric initialization, environment-aware variation and antiseeds to reduce search trapping.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility, Symmetric initialization — [Mechanisms and limits](structural-priors.md)

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://uspex-team.org/static/file/Lyakhov-CPC-2013.pdf)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2012.12.009) · [source 2](https://uspex-team.org/static/file/Lyakhov-CPC-2013.pdf)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp060"></a>
### 2014 — Muse: Multi-algorithm collaborative crystal structure prediction

**CSP060 · Published journal article · Atomic / inorganic**

Zhong-Li Liu. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2014.03.017)

**Method:** Coordinate evolutionary search, simulated annealing and basin hopping with self-adaptive operator competition.. Coordinate evolutionary search, simulated annealing and basin hopping with self-adaptive operator competition.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [MUSE](software.md#muse)

**Groups:** [Zhong-Li Liu / MUSE team](https://arxiv.org/abs/1303.2802)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2014.03.017) · [source 2](https://arxiv.org/abs/1303.2802)

**Scope:** Collaborative EA/SA/BH method; must not be mislabeled as differential evolution.

<a id="csp069"></a>
### 2016 — XtalOpt version r9: An open-source evolutionary algorithm for crystal structure prediction

**CSP069 · Published journal article · Atomic / inorganic**

Zackary Falls; David C. Lonie; Patrick Avery; Andrew Shamp; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2015.09.018)

**Method:** Software version announcement updating the XtalOpt evolutionary search implementation.. Software version announcement updating the XtalOpt evolutionary search implementation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained publication list and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2015.09.018) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Version announcement, not a separate global-search paradigm.

<a id="csp074"></a>
### 2017 — XtalOpt Version r10: An open–source evolutionary algorithm for crystal structure prediction

**CSP074 · Published journal article · Atomic / inorganic**

Patrick Avery; Zackary Falls; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2017.04.001)

**Method:** Software version announcement updating the XtalOpt evolutionary search implementation.. Software version announcement updating the XtalOpt evolutionary search implementation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained publication list and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2017.04.001) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Version announcement, not a separate global-search paradigm.

<a id="csp076"></a>
### 2018 — Evolutionary niching in the GAtor genetic algorithm for molecular crystal structure prediction

**CSP076 · Journal article · Molecular / organic**

Farren Curtis; Timothy Rose; Noa Marom. *Faraday Discussions*. [Paper](https://doi.org/10.1039/C8FD00067K)

**Method:** Clustering-driven evolutionary niches. Dynamically cluster the GA population and use niche-aware selection to reduce genetic drift and improve landscape exploration.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GAtor](software.md#gator-molecular)

**Groups:** [Marom / Genarris–GAtor collaboration](https://pubs.rsc.org/en/content/articlepdf/2018/fd/c8fd00067k)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1039/C8FD00067K) · [source 2](https://pubs.rsc.org/en/content/articlepdf/2018/fd/c8fd00067k)

**Scope:** Method improvement within molecular GA; niching does not resolve quantum energy-ranking errors.

<a id="csp078"></a>
### 2018 — GAtor: A First-Principles Genetic Algorithm for Molecular Crystal Structure Prediction

**CSP078 · Journal article · Molecular / organic**

Farren Curtis; Xiayue Li; Timothy Rose; Álvaro Vázquez-Mayagoitia; Saswata Bhattacharya; Luca M. Ghiringhelli; Noa Marom. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/acs.jctc.7b01152)

**Method:** Molecular GA with dynamic evolutionary niching. Create and evolve molecular packings using specialized crossover/mutation and DFT optimization; cluster-based fitness preserves diversity.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GAtor](software.md#gator-molecular)

**Groups:** [Marom / Genarris–GAtor collaboration](https://pubmed.ncbi.nlm.nih.gov/29481740/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/acs.jctc.7b01152) · [source 2](https://pubmed.ncbi.nlm.nih.gov/29481740/)

**Scope:** Evaluated on selected past blind-test targets; energy landscape exploration remains budget and evaluator dependent.

<a id="csp084"></a>
### 2018 — XtalOpt version r11: An open-source evolutionary algorithm for crystal structure prediction

**CSP084 · Published journal article · Atomic / inorganic**

Patrick Avery; Zackary Falls; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2017.09.011)

**Method:** Software version announcement updating the XtalOpt evolutionary search implementation.. Software version announcement updating the XtalOpt evolutionary search implementation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained publication list and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2017.09.011) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Version announcement, not a separate global-search paradigm.

<a id="csp085"></a>
### 2019 — Accelerating crystal structure prediction by machine-learning interatomic potentials with active learning

**CSP085 · Published journal article · Atomic / inorganic**

Evgeny V. Podryabinkin; Evgeny V. Tikhonov; Alexander V. Shapeev; Artem R. Oganov. *Physical Review B*. [Paper](https://uspex-team.org/static/file/Podryabinkin-2019.pdf)

**Method:** USPEX plus on-the-fly active-learning MTP. Evolutionary proposals → MTP relaxation → extrapolation test / DFT labels → retrain → final DFT verification

**Inputs:** Formula, pressure and evolutionary search bounds

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / Shapeev collaboration](https://uspex-team.org/static/file/Podryabinkin-2019.pdf)

**Evidence:** Author-hosted paper first-page abstract and workflow excerpt. [source 1](https://uspex-team.org/static/file/Podryabinkin-2019.pdf) · [source 2](https://arxiv.org/abs/1802.07605)

**Scope:** Surrogate acceleration needs extrapolation checks and final DFT ranking; not a separate guarantee of exhaustive landscape coverage.

<a id="csp091"></a>
### 2019 — XtalOpt Version r12: An open-source evolutionary algorithm for crystal structure prediction

**CSP091 · Published journal article · Atomic / inorganic**

Patrick Avery; Cormac Toher; Stefano Curtarolo; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2018.11.016)

**Method:** Software version announcement updating the XtalOpt evolutionary search implementation.. Software version announcement updating the XtalOpt evolutionary search implementation.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained publication list and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2018.11.016) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Version announcement, not a separate global-search paradigm.

<a id="csp080"></a>
### 2019 — henniggroup/GASP-python: GASP-python V1.0

**CSP080 · Software archive · Atomic / inorganic**

Benjamin Revard; Kiran Mathew. *Zenodo / GitHub software record*. [Paper](https://doi.org/10.5281/zenodo.2554076)

**Method:** GASP software release. Provide fixed-composition and phase-diagram evolutionary searches through interfaces to atomistic evaluators.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [GASP-Python](software.md#gasp-python)

**Groups:** [Richard Hennig / GASP and learned CSP](https://github.com/henniggroup/GASP-python)

**Evidence:** Official repository README and citation instructions. [source 1](https://doi.org/10.5281/zenodo.2554076) · [source 2](https://github.com/henniggroup/GASP-python)

**Scope:** Software citation rather than a distinct journal method paper; history includes earlier development in the Ceder group.

<a id="dmcrystal2020"></a>
### 2020 — Distance Matrix-Based Crystal Structure Prediction Using Evolutionary Algorithms

**DMCrystal2020 · Journal article · Atomic / inorganic**

Hu, Jianjun; Yang, Wenhui; Dilanga Siriwardane, Edirisuriya M.. *The Journal of Physical Chemistry A*. [Paper](https://doi.org/10.1021/acs.jpca.0c08775)

**Method:** DMCrystal. Genetic reconstruction from pairwise distances, lattice, and space-group information.

**Inputs:** Pairwise atomic distances; lattice and space group

**Software:** [DMCrystal](software.md#dmcrystal)

**Groups:** [Jianjun Hu–Wenhui Yang collaboration](https://doi.org/10.1021/acs.jpca.0c08775)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1021/acs.jpca.0c08775)

**Scope:** Reconstruction requires supplied structural constraints.

<a id="cmcrystal2021"></a>
### 2021 — Contact map based crystal structure prediction using global optimization

**CMCrystal2021 · Journal article · Atomic / inorganic**

Hu, Jianjun; Yang, Wenhui; Dong, Rongzhi; Li, Yuxin; Li, Xiang; Li, Shaobo; Siriwardane, Edirisuriya M. D.. *CrystEngComm*. [Paper](https://doi.org/10.1039/d0ce01714k)

**Method:** CMCrystal. Contact-map reconstruction comparing global optimization algorithms.

**Inputs:** Contact map and crystallographic information

**Software:** [CMCrystal](software.md#cmcrystal)

**Groups:** [Jianjun Hu–Wenhui Yang collaboration](https://doi.org/10.1039/d0ce01714k)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1039/d0ce01714k)

**Scope:** Reconstruction requires supplied structural constraints.

<a id="csp110"></a>
### 2022 — Accelerated identification of equilibrium structures of multicomponent inorganic crystals using machine learning potentials

**CSP110 · Published journal article · Atomic / inorganic**

Sungwoo Kang; Wonseok Jeong; Changho Hong; Seungwoo Hwang; Youngchae Yoon; Seungwu Han. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-022-00792-w)

**Method:** SPINNER: NNP evolutionary and random searches. Melt-quench training → NNP-refined evolutionary/random search → DFT refinement / energy ranking

**Inputs:** Composition and formula-unit / cell-size bounds

**Software:** [SPINNER](software.md#spinner)

**Groups:** [Seungwu Han / SPINNER collaboration](https://www.nature.com/articles/s41524-022-00792-w)

**Evidence:** Publisher abstract, workflow and benchmark / limitations excerpts. [source 1](https://www.nature.com/articles/s41524-022-00792-w)

**Scope:** Finite-budget results; benchmark uses known cell formula-unit counts and excludes several magnetic chemistries. DFT functional choice can change polymorph ordering.

<a id="cmcrystalmoo2022"></a>
### 2022 — Crystal Structure Prediction Using an Age-Fitness Multiobjective Genetic Algorithm and Coordination Number Constraints

**CMCrystalMOO2022 · Journal article · Atomic / inorganic**

Yang, Wenhui; Dilanga Siriwardane, Edirisuriya M.; Hu, Jianjun. *The Journal of Physical Chemistry A*. [Paper](https://doi.org/10.1021/acs.jpca.1c07170)

**Method:** CMCrystalMOO / MOOCSP. Multiobjective reconstruction using contact agreement, coordination agreement and individual age.

**Inputs:** Contact map, coordination constraints and crystallographic settings

**Software:** [CMCrystalMOO / MOOCSP](software.md#cmcrystalmoo)

**Groups:** [Jianjun Hu–Wenhui Yang collaboration](https://doi.org/10.1021/acs.jpca.1c07170)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1021/acs.jpca.1c07170)

**Scope:** Reconstruction requires supplied structural constraints.

<a id="csp125"></a>
### 2023 — Accelerated Organic Crystal Structure Prediction with Genetic Algorithms and Machine Learning

**CSP125 · Journal article · Molecular / organic**

Amit Kadan; Kevin Ryczko; Andrew Wildman; Rodrigo Wang; Adrian Roitberg; Takeshi Yamazaki. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/acs.jctc.3c00853)

**Method:** Random screening followed by ML-potential GA. Generate random molecular packing pool then optimize with a GA using learned potentials.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Kadan–Yamazaki / Good Chemistry–Roitberg collaboration](https://pubmed.ncbi.nlm.nih.gov/38059458/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/acs.jctc.3c00853) · [source 2](https://pubmed.ncbi.nlm.nih.gov/38059458/)

**Scope:** Success depends on molecular/element coverage and potential quality; reported target recovery is not completeness.

<a id="magus2023"></a>
### 2023 — MAGUS: machine learning and graph theory assisted universal structure searcher

**MAGUS2023 · Published journal article · Atomic / inorganic**

Junjie Wang; Hao Gao; Yu Han; Chi Ding; Shuning Pan; Yong Wang; Qiuhan Jia; Hui-Tian Wang; Dingyu Xing; Jian Sun. *National Science Review*. [Paper](https://doi.org/10.1093/nsr/nwad128)

**Method:** Graph-decomposition and ML-assisted evolutionary search. Extract and rearrange graph-based fragments; accelerate structure evaluation using on-the-fly learned potentials.

**Inputs:** Composition, cell bounds and a reference energy evaluator

**Structural knowledge:** Molecular units / chemical motifs, Symmetry hierarchy / diversity, Symmetry-preserving exploration, Topology / connectivity — [Mechanisms and limits](structural-priors.md)

**Software:** [MAGUS](software.md#magus)

**Groups:** [Jian Sun–Wang–Han / MAGUS team](https://doi.org/10.1093/nsr/nwad128)

**Evidence:** Primary paper and developer descriptions; Crossref title/authors verified. [source 1](https://doi.org/10.1093/nsr/nwad128)

**Scope:** Training generated during search is system-dependent; fragment restrictions and potential accuracy affect coverage.

<a id="csp141"></a>
### 2024 — Crystal structure prediction using neural network potential and age-fitness Pareto genetic algorithm

**CSP141 · Published journal article · Atomic / inorganic**

Sadman Sadeed Omee; Lai Wei; Ming Hu; Jianjun Hu. *Journal of materials Informatics*. [Paper](https://www.oaepublish.com/articles/jmi.2023.33)

**Method:** ParetoCSP: age–fitness Pareto genetic algorithm with M3GNet. Genetic structural proposals → neural potential relaxation / energy fitness → age-aware NSGA selection

**Inputs:** Composition and search constraints

**Software:** [ParetoCSP](software.md#paretocsp)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://www.oaepublish.com/articles/jmi.2023.33)

**Evidence:** Publisher abstract, author contribution and journal PDF citation metadata. [source 1](https://www.oaepublish.com/articles/jmi.2023.33) · [source 2](https://f.oaes.cc/xmlpdf/ff332f6a-77ca-412b-8d5e-cc87872f6253/jmi4033.pdf)

**Scope:** Performance is evaluator-, budget- and benchmark-dependent; comparison with GN-OA combines search and energy-model differences. Journal version adds Ming Hu relative to early preprint.

<a id="csp158"></a>
### 2024 — XtalOpt version 13: Multi-objective evolutionary search for novel functional materials

**CSP158 · Published journal article · Atomic / inorganic**

Samad Hajinazar; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2024.109306)

**Method:** Optimize energy and user-selected functional objectives in evolutionary structure search.. Optimize energy and user-selected functional objectives in evolutionary structure search.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained method and publication summary. [source 1](https://doi.org/10.1016/j.cpc.2024.109306) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Multi-objective functionality search; Pareto rank does not establish phase stability.

<a id="csp164"></a>
### 2025 — Automated high-throughput organic crystal structure prediction via population-based sampling

**CSP164 · Journal article · Molecular / organic**

Qiang Zhu; Shinnosuke Hattori. *Digital Discovery*. [Paper](https://doi.org/10.1039/D4DD00264D)

**Method:** HTOCSP symmetry-preserving population sampling. Automate conformer analysis, force-field generation and crystal packing search, with population mutations of cell and Wyckoff variables.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [HTOCSP (population / width-first sampling)](software.md#htocsp)

**Groups:** [Qiang Zhu / crystal search and generation](https://pubs.rsc.org/en/content/articlelanding/2025/dd/d4dd00264d)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1039/D4DD00264D) · [source 2](https://pubs.rsc.org/en/content/articlelanding/2025/dd/d4dd00264d)

**Scope:** User-defined constraints and force fields limit coverage; journal issue 2025, first online November 2024.

<a id="csp167"></a>
### 2025 — CrySPAI: A new Crystal Structure Prediction Software Based on Artificial Intelligence

**CSP167 · Preprint · Atomic / inorganic**

Zongguo Wang; Ziyi Chen; Yang Yuan; Yangang Wang. *arXiv*. [Paper](https://arxiv.org/abs/2501.15838)

**Method:** CrySPAI: distributed evolutionary optimization plus learned energies. Evolutionary structure proposals → DFT energies → neural energy model → distributed automated search

**Inputs:** Composition, search bounds and first-principles evaluator

**Software:** [CrySPAI](software.md#cryspai)

**Groups:** [CrySPAI · Zongguo Wang / Yangang Wang collaboration](https://arxiv.org/abs/2501.15838)

**Evidence:** Primary arXiv abstract and author list. [source 1](https://arxiv.org/abs/2501.15838)

**Scope:** Preprint abstract describes software architecture; broad unknown-domain reliability and exhaustive coverage are not independently established.

<a id="csp170"></a>
### 2025 — Efficient crystal structure prediction based on the symmetry principle

**CSP170 · Published journal paper · Atomic / inorganic**

Yu Han; Chi Ding; Junjie Wang; Hao Gao; Jiuyang Shi; Shaobo Yu; Qiuhan Jia; Shuning Pan; Jian Sun. *Nature Computational Science*. [Paper](https://doi.org/10.1038/s43588-025-00775-z)

**Method:** MAGUS uses mined symmetry and graph fragments to improve evolutionary proposals.. Explore structures → mine space groups / reorganize fragments → symmetry-kept mutation → relaxation

**Inputs:** Composition and search/energy settings

**Structural knowledge:** Molecular units / chemical motifs, Symmetry hierarchy / diversity, Symmetry-preserving exploration, Topology / connectivity — [Mechanisms and limits](structural-priors.md)

**Software:** [MAGUS](software.md#magus)

**Groups:** [Jian Sun–Wang–Han / MAGUS team](https://doi.org/10.1038/s43588-025-00775-z)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1038/s43588-025-00775-z)

**Scope:** A symmetry-informed evolutionary generator; it is not a trained diffusion generator, despite the shared word generation.

<a id="csp175"></a>
### 2025 — Polymorphism Crystal Structure Prediction with Adaptive Space Group Diversity Control

**CSP175 · Published journal article · Atomic / inorganic**

Sadman Sadeed Omee; Lai Wei; Sourin Dey; Jianjun Hu. *Advanced Science*. [Paper](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792)

**Method:** ParetoCSP2: symmetry-diverse Pareto evolutionary CSP. Symmetry-aware generation → neural-potential relaxation → age/fitness and adaptive space-group diversity selection

**Inputs:** Composition and population / symmetry bounds

**Structural knowledge:** Symmetry hierarchy / diversity — [Mechanisms and limits](structural-priors.md)

**Software:** [ParetoCSP2](software.md#paretocsp2)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792)

**Evidence:** Publisher abstract, method / limitations excerpts and author list. [source 1](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792)

**Scope:** Predicting multiple polymorphs is finite-budget; source reports misses and symmetry-dependent recovery. Neural-potential accuracy is distinct from search coverage.

<a id="csp196"></a>
### 2026 — XtalOpt version 14: Variable-composition crystal structure search for functional materials through Pareto optimization

**CSP196 · Published journal article · Atomic / inorganic**

Samad Hajinazar; Eva Zurek. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2025.109910)

**Method:** Extend Pareto evolutionary crystal search to variable composition.. Extend Pareto evolutionary crystal search to variable composition.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [XtalOpt (including r7–14)](software.md#xtalopt)

**Groups:** [Zurek / XtalOpt team](https://xtalopt.github.io/pub.html)

**Evidence:** Author-maintained method and publication summary. [source 1](https://doi.org/10.1016/j.cpc.2025.109910) · [source 2](https://xtalopt.github.io/pub.html)

**Scope:** Variable-composition Pareto search requires phase-competition evaluation and finite chemical-system bounds.

## Swarm and differential evolution

<a id="csp043"></a>
### 2010 — Crystal structure prediction via particle-swarm optimization

**CSP043 · Published journal article · Atomic / inorganic**

Yanchao Wang; Jian Lv; Li Zhu; Yanming Ma. *Physical Review B*. [Paper](https://doi.org/10.1103/PhysRevB.82.094116)

**Method:** Move candidate structures using particle-swarm history and population information, then locally relax.. Move candidate structures using particle-swarm history and population information, then locally relax.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Structural knowledge:** Chemical / geometric plausibility, Symmetric initialization — [Mechanisms and limits](structural-priors.md)

**Software:** [CALYPSO](software.md#calypso)

**Groups:** [Yanming Ma–Yanchao Wang / CALYPSO collaboration](https://arxiv.org/abs/1008.3601)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevB.82.094116) · [source 2](https://arxiv.org/abs/1008.3601)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp054"></a>
### 2012 — CALYPSO: A method for crystal structure prediction

**CSP054 · Published journal article · Atomic / inorganic**

Yanchao Wang; Jian Lv; Li Zhu; Yanming Ma. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2012.05.008)

**Method:** Combine PSO with symmetry-constrained initialization, structure duplicate checks and random injection.. Combine PSO with symmetry-constrained initialization, structure duplicate checks and random injection.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Structural knowledge:** Chemical / geometric plausibility, Symmetric initialization — [Mechanisms and limits](structural-priors.md)

**Software:** [CALYPSO](software.md#calypso)

**Groups:** [Yanming Ma–Yanchao Wang / CALYPSO collaboration](https://arxiv.org/abs/1205.2264)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2012.05.008) · [source 2](https://arxiv.org/abs/1205.2264)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp064"></a>
### 2015 — Inverse design of materials by multi-objective differential evolution

**CSP064 · Published journal article · Atomic / inorganic**

Yue-Yu Zhang; Weiguo Gao; Shiyou Chen; Hongjun Xiang; Xin-Gao Gong. *Computational Materials Science*. [Paper](https://doi.org/10.1016/j.commatsci.2014.10.054)

**Method:** Jointly optimize energy and desired properties using multi-objective differential evolution.. Jointly optimize energy and desired properties using multi-objective differential evolution.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [IM²ODE](software.md#im2ode)

**Groups:** [Gong–Xiang–Chen / IM2ODE team](https://physics.ecust.edu.cn/_upload/article/files/59/56/bb36e249416cb10e1e3a83d6a0fb/ee775485-26ff-4956-84b0-49f22d50fee8.pdf)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.commatsci.2014.10.054) · [source 2](https://physics.ecust.edu.cn/_upload/article/files/59/56/bb36e249416cb10e1e3a83d6a0fb/ee775485-26ff-4956-84b0-49f22d50fee8.pdf)

**Scope:** Adjacent inverse-property objective; minimizing a property objective is not identical to finding the thermodynamic ground state.

<a id="csp073"></a>
### 2017 — SGO: A fast engine for ab initio atomic structure global optimization by differential evolution

**CSP073 · Published journal article · Atomic / inorganic**

Zhanghui Chen; Weile Jia; Xiangwei Jiang; Shu-Shen Li; Lin-Wang Wang. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2017.05.005)

**Method:** Combine parallel differential evolution, accelerated local relaxation and GPU plane-wave DFT.. Combine parallel differential evolution, accelerated local relaxation and GPU plane-wave DFT.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [SGO](software.md#sgo)

**Groups:** [Lin-Wang Wang / SGO collaboration](https://www.sciencedirect.com/science/article/am/pii/S0010465517301352)

**Evidence:** Primary abstract and selected methods/results sections. [source 1](https://doi.org/10.1016/j.cpc.2017.05.005) · [source 2](https://www.sciencedirect.com/science/article/am/pii/S0010465517301352)

**Scope:** Reported performance depends on tested cell sizes and GPU/evaluator configuration.

<a id="cmcrystalhs2021"></a>
### 2021 — Crystal structure prediction of materials with high symmetry using differential evolution

**CMCrystalHS2021 · Journal article · Atomic / inorganic**

Yang, Wenhui; Dilanga Siriwardane, Edirisuriya M; Dong, Rongzhi; Li, Yuxin; Hu, Jianjun. *Journal of Physics: Condensed Matter*. [Paper](https://doi.org/10.1088/1361-648x/ac1d6c)

**Method:** CMCrystalHS. PyXtal-compatible Wyckoff assignments followed by differential evolution of free coordinates.

**Inputs:** Formula, contact map and space group

**Structural knowledge:** Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [CMCrystalHS](software.md#cmcrystalhs)

**Groups:** [Jianjun Hu–Wenhui Yang collaboration](https://doi.org/10.1088/1361-648x/ac1d6c)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1088/1361-648x/ac1d6c)

**Scope:** Reconstruction requires supplied structural constraints.

## Energy-landscape exploration

<a id="csp005"></a>
### 1998 — Diffusion Equation and Distance Scaling Methods of Global Optimization: Applications to Crystal Structure Prediction

**CSP005 · Journal article · Molecular / organic**

Ryszard J. Wawak; Jaroslaw Pillardy; Adam Liwo; Kenneth D. Gibson; Harold A. Scheraga. *The Journal of Physical Chemistry A*. [Paper](https://doi.org/10.1021/jp972424u)

**Method:** Potential-energy-surface smoothing. Smooth away minor minima; trace surviving minima back to the original landscape while removing smoothing.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Diffusion-equation / distance-scaling global optimization](software.md#deds-crystal)

**Groups:** [Scheraga / Pillardy collaboration](https://pubs.acs.org/doi/10.1021/jp972424u)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/jp972424u) · [source 2](https://pubs.acs.org/doi/10.1021/jp972424u)

**Scope:** Demonstrations on hexasulfur and benzene; classical diffusion-equation smoothing is distinct from modern learned diffusion generation.

<a id="csp010"></a>
### 2001 — Conformation-family Monte Carlo: A new method for crystal structure prediction

**CSP010 · Journal article · Molecular / organic**

Jaroslaw Pillardy; Yelena A. Arnautova; Cezary Czaplewski; Kenneth D. Gibson; Harold A. Scheraga. *Proceedings of the National Academy of Sciences*. [Paper](https://doi.org/10.1073/pnas.231479298)

**Method:** Conformation-family Monte Carlo. Maintain a database of structurally clustered families and sample new crystal minima from these families.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Conformation-family Monte Carlo (CFMC)](software.md#cfmc-crystal)

**Groups:** [Scheraga / Pillardy collaboration](https://pmc.ncbi.nlm.nih.gov/articles/PMC60057/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1073/pnas.231479298) · [source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC60057/)

**Scope:** Classical potential and finite search do not guarantee experimental polymorph ordering.

<a id="csp018"></a>
### 2003 — Predicting Crystal Structures: The Parrinello-Rahman Method Revisited

**CSP018 · Published journal article · Atomic / inorganic**

R. Martoňák; A. Laio; M. Parrinello. *Physical Review Letters*. [Paper](https://doi.org/10.1103/PhysRevLett.90.075503)

**Method:** Use history-dependent bias on the simulation cell to escape known crystalline free-energy basins.. Use history-dependent bias on the simulation cell to escape known crystalline free-energy basins.

**Inputs:** Initial crystal; thermodynamic conditions; cell collective variables

**Software:** [Simulation-cell metadynamics (Martonak–Laio–Parrinello)](software.md#cell-metadynamics)

**Groups:** [Martoňák–Laio–Parrinello metadynamics team](https://arxiv.org/abs/cond-mat/0211551)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1103/PhysRevLett.90.075503) · [source 2](https://arxiv.org/abs/cond-mat/0211551)

**Scope:** Choice of initial phase and collective variables can restrict reachable structures.

<a id="csp020"></a>
### 2004 — Minima hopping: An efficient search method for the global minimum of the potential energy surface of complex molecular systems

**CSP020 · Published journal article · Surfaces / clusters (adjacent)**

Stefan Goedecker. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/1.1724816)

**Method:** Alternate short molecular-dynamics escape trajectories with local minimization and adaptive escape parameters.. Alternate short molecular-dynamics escape trajectories with local minimization and adaptive escape parameters.

**Inputs:** Atomic system; potential-energy evaluator

**Software:** [Minima Hopping (Goedecker-group Python implementation)](software.md#minima-hopping)

**Groups:** [Goedecker–Amsler / minima-hopping collaboration](https://edoc.unibas.ch/95451/1/20230811123429_64d60eb59705f.pdf)

**Evidence:** Primary published paper first page and abstract, deposited by University of Basel. [source 1](https://doi.org/10.1063/1.1724816) · [source 2](https://edoc.unibas.ch/95451/1/20230811123429_64d60eb59705f.pdf) · [source 3](https://arxiv.org/abs/cond-mat/0402136)

**Scope:** Foundational minima-hopping method; the variable-cell crystal extension is a separate 2010 paper.

<a id="csp025"></a>
### 2005 — Simulation of structural phase transitions by metadynamics

**CSP025 · Published journal article · Atomic / inorganic**

Roman Martoňák; Alessandro Laio; Marco Bernasconi; Chiara Ceriani; Paolo Raiteri; Federico Zipoli; Michele Parrinello. *Zeitschrift für Kristallographie - Crystalline Materials*. [Paper](https://doi.org/10.1524/zkri.220.5.489.65078)

**Method:** Develop simulation-cell metadynamics for structural transitions and crystal exploration.. Develop simulation-cell metadynamics for structural transitions and crystal exploration.

**Inputs:** Initial crystal and thermodynamic conditions

**Software:** [Simulation-cell metadynamics (Martonak–Laio–Parrinello)](software.md#cell-metadynamics)

**Groups:** [Martoňák–Laio–Parrinello metadynamics team](https://www.research-collection.ethz.ch/bitstreams/192fd910-ee0a-494a-b0a5-2849738f24a2/download)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1524/zkri.220.5.489.65078) · [source 2](https://www.research-collection.ethz.ch/bitstreams/192fd910-ee0a-494a-b0a5-2849738f24a2/download)

**Scope:** Phase-transition exploration is conditioned on initial state and collective variables.

<a id="csp032"></a>
### 2007 — Global exploration of the energy landscape of solids on the ab initio level

**CSP032 · Published journal article · Atomic / inorganic**

K. Doll; J. C. Schön; M. Jansen. *Physical Chemistry Chemical Physics*. [Paper](https://doi.org/10.1039/B709943F)

**Method:** Perform global solid-state search with ab initio energies rather than filtering first with empirical potentials.. Perform global solid-state search with ab initio energies rather than filtering first with empirical potentials.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [Ab initio landscape exploration (Schön et al.)](software.md#abinitio-landscape-sch-n)

**Groups:** [Schön–Jansen landscape team](https://arxiv.org/abs/0711.2708)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1039/B709943F) · [source 2](https://arxiv.org/abs/0711.2708)

**Scope:** LiF demonstration; computational costs constrain larger and chemically complex landscapes.

<a id="csp034"></a>
### 2008 — A Major Advance in Crystal Structure Prediction

**CSP034 · Journal article · Molecular / organic**

Marcus A. Neumann; Frank J. J. Leusen; John Kendrick. *Angewandte Chemie International Edition*. [Paper](https://doi.org/10.1002/anie.200704247)

**Method:** Tailor-made-force-field search and DFT-D reranking. Molecular packing search with a compound-specific force field; final periodic dispersion-corrected DFT ranking.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GRACE (Generation Ranking and Characterization Engine)](software.md#grace-csp)

**Groups:** [Neumann / GRACE collaboration](https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.200704247)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1002/anie.200704247) · [source 2](https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.200704247)

**Scope:** Four fourth-blind-test targets do not establish universal accuracy for flexible, disordered or multicomponent crystals.

<a id="csp042"></a>
### 2010 — Crystal structure prediction using the minima hopping method

**CSP042 · Published journal article · Atomic / inorganic**

Maximilian Amsler; Stefan Goedecker. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/1.3512900)

**Method:** Generalize minima hopping to variable-cell enthalpy surfaces with soft-mode-informed escape velocities.. Generalize minima hopping to variable-cell enthalpy surfaces with soft-mode-informed escape velocities.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [Minima Hopping (Goedecker-group Python implementation)](software.md#minima-hopping)

**Groups:** [Goedecker–Amsler / minima-hopping collaboration](https://arxiv.org/abs/1007.2003)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1063/1.3512900) · [source 2](https://arxiv.org/abs/1007.2003)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp055"></a>
### 2012 — Evolutionary metadynamics: a novel method to predict crystal structures

**CSP055 · Published journal article · Atomic / inorganic**

Qiang Zhu; Artem R. Oganov; Andriy O. Lyakhov. *CrystEngComm*. [Paper](https://doi.org/10.1039/C2CE06642D)

**Method:** Use cell-shape metadynamics with evolutionary equilibration to explore ground and reachable metastable states.. Use cell-shape metadynamics with evolutionary equilibration to explore ground and reachable metastable states.

**Inputs:** Reasonable initial crystal structure; composition; conditions

**Software:** [USPEX](software.md#uspex)

**Groups:** [Oganov / USPEX collaboration](https://pubs.rsc.org/en/content/articlelanding/2012/ce/c2ce06642d)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1039/C2CE06642D) · [source 2](https://pubs.rsc.org/en/content/articlelanding/2012/ce/c2ce06642d)

**Scope:** Initial-structure and collective-variable choices shape accessible states; not unbiased sampling of every basin.

<a id="csp058"></a>
### 2013 — Stochastic Surface Walking Method for Structure Prediction and Pathway Searching

**CSP058 · Published journal article · Surfaces / clusters (adjacent)**

Cheng Shang; Zhi-Pan Liu. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/ct301010b)

**Method:** Use repeated bias-driven small displacements and Monte Carlo acceptance to explore minima and transition paths.. Use repeated bias-driven small displacements and Monte Carlo acceptance to explore minima and transition paths.

**Inputs:** Atomic system; energy/force evaluator

**Software:** [SSW / LASP](software.md#ssw-lasp)

**Groups:** [Zhi-Pan Liu–Cheng Shang / SSW team](https://pubs.acs.org/doi/10.1021/ct301010b)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1021/ct301010b) · [source 2](https://pubs.acs.org/doi/10.1021/ct301010b)

**Scope:** Founding paper demonstrates clusters and molecular pathways; periodic-crystal extension is separate in 2014.

<a id="csp062"></a>
### 2014 — Stochastic surface walking method for crystal structure and phase transition pathway prediction

**CSP062 · Published journal article · Atomic / inorganic**

Cheng Shang; Xiao-Jie Zhang; Zhi-Pan Liu. *Phys. Chem. Chem. Phys.*. [Paper](https://doi.org/10.1039/C4CP01485E)

**Method:** Extend stochastic surface walking to coupled lattice and atom degrees of freedom for crystalline minima and transition paths.. Extend stochastic surface walking to coupled lattice and atom degrees of freedom for crystalline minima and transition paths.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [SSW / LASP](software.md#ssw-lasp)

**Groups:** [Zhi-Pan Liu–Cheng Shang / SSW team](https://pubs.rsc.org/en/content/getauthorversionpdf/C4CP01485E)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1039/C4CP01485E) · [source 2](https://pubs.rsc.org/en/content/getauthorversionpdf/C4CP01485E)

**Scope:** Finding low-enthalpy endpoints and transition pathways does not by itself establish finite-temperature phase populations.

<a id="csp070"></a>
### 2017 — Accelerated discovery of two crystal structure types in a complex inorganic phase field

**CSP070 · Published journal paper · Atomic / inorganic**

C. Collins; M. S. Dyer; M. J. Pitcher; G. F. S. Whitehead; M. Zanella; P. Mandal; J. B. Claridge; G. R. Darling; M. J. Rosseinsky. *Nature*. [Paper](https://doi.org/10.1038/nature22374)

**Method:** MC-EMMA assembles chemical modules and uses probe-structure energies to guide synthesis.. Modules + phase field → Monte Carlo structure exploration → energy ranking → targeted experiments

**Inputs:** Specified chemical phase field and modular crystal-chemistry knowledge

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility — [Mechanisms and limits](structural-priors.md)

**Software:** [MC-EMMA](software.md#mc-emma)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1038/nature22374)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1038/nature22374)

**Scope:** A workflow/method demonstration: promising probe structures guide experimental search; synthesis need not reproduce the lowest probe exactly.

<a id="csp083"></a>
### 2018 — The Flexible Unit Structure Engine (FUSE) for probe structure-based composition prediction

**CSP083 · Published journal paper · Atomic / inorganic**

C. Collins; G. R. Darling; M. J. Rosseinsky. *Faraday Discussions*. [Paper](https://doi.org/10.1039/c8fd00045j)

**Method:** Small chemical building blocks are assembled and explored by modified basin hopping.. Chemical submodules → probe structures → basin hopping / relaxation → composition-region ranking

**Inputs:** Phase field or composition and chemical construction rules

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility — [Mechanisms and limits](structural-priors.md)

**Software:** [FUSE / FUSE2](software.md#fuse)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1039/c8fd00045j)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1039/c8fd00045j)

**Scope:** Probe structures can rank promising composition regions without being the exact experimentally observed structure.

<a id="csp089"></a>
### 2019 — Reliable and practical computational description of molecular crystal polymorphs

**CSP089 · Journal article · Molecular / organic**

Johannes Hoja; Hsin-Yu Ko; Marcus A. Neumann; Roberto Car; Robert A. DiStasio; Alexandre Tkatchenko. *Science Advances*. [Paper](https://doi.org/10.1126/sciadv.aau3338)

**Method:** Parallel-tempering sampling and high-accuracy free-energy ranking. Combine GRACE tailor-made-force-field Monte Carlo parallel tempering with hybrid DFT, many-body dispersion and vibrational free energies.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GRACE (Generation Ranking and Characterization Engine)](software.md#grace-csp)

**Groups:** [Tkatchenko–Neumann / Hoja–DiStasio collaboration](https://pubmed.ncbi.nlm.nih.gov/30746448/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1126/sciadv.aau3338) · [source 2](https://pubmed.ncbi.nlm.nih.gov/30746448/)

**Scope:** Successful retrospective blind-test targets do not imply universal polymorph coverage; expensive final free-energy corrections remain.

<a id="csp093"></a>
### 2020 — Chemically directed structure evolution for crystal structure prediction

**CSP093 · Published journal paper · Atomic / inorganic**

Paul M. Sharp; Matthew S. Dyer; George R. Darling; John B. Claridge; Matthew J. Rosseinsky. *Physical Chemistry Chemical Physics*. [Paper](https://doi.org/10.1039/d0cp02206c)

**Method:** ChemDASH prioritizes atom swaps using local chemical-environment scores.. Initial structure / grid → rank environments → directed atom swaps → relax → basin-hopping acceptance

**Inputs:** Composition and initial site arrangement

**Software:** [ChemDASH](software.md#chemdash)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1039/d0cp02206c)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1039/d0cp02206c)

**Scope:** Swap-based exploration depends on starting construction and chemical-environment heuristics.

<a id="csp104"></a>
### 2021 — Exploration and Optimization in Crystal Structure Prediction: Combining Basin Hopping with Quasi-Random Sampling

**CSP104 · Journal article · Molecular / organic**

Shiyue Yang; Graeme M. Day. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/acs.jctc.0c01101)

**Method:** Quasi-random basin hopping (QR-BH). Combine broad low-discrepancy initial packings with local Monte Carlo basin-hopping exploration.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [mol-CSPy: quasi-random sampling, QRBH and threshold MC](software.md#mol-cspy)

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.0c01101)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/acs.jctc.0c01101) · [source 2](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.0c01101)

**Scope:** Exploration versus low-energy exploitation must be balanced to retain higher-energy polymorphs.

<a id="csp116"></a>
### 2022 — Global analysis of the energy landscapes of molecular crystal structures by applying the threshold algorithm

**CSP116 · Journal article · Molecular / organic**

Shiyue Yang; Graeme M. Day. *Communications Chemistry*. [Paper](https://doi.org/10.1038/s42004-022-00705-4)

**Method:** Monte Carlo threshold landscape exploration. Perturb structures under an energy lid and quench sampled configurations to characterize basins and inter-polymorph barriers.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [mol-CSPy: quasi-random sampling, QRBH and threshold MC](software.md#mol-cspy)

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://www.nature.com/articles/s42004-022-00705-4)

**Evidence:** Primary full-text selected methods/conclusions. [source 1](https://doi.org/10.1038/s42004-022-00705-4) · [source 2](https://www.nature.com/articles/s42004-022-00705-4)

**Scope:** Starts from supplied known/predicted minima; rigid molecules in this implementation; barriers depend on symmetry constraints.

<a id="csp119"></a>
### 2022 — Predicting spinel solid solutions using a random atom substitution method

**CSP119 · Published journal paper · Atomic / inorganic**

Robert C. Dickson; Troy D. Manning; Edwin S. Raj; Jonathan C. S. Booth; Matthew J. Rosseinsky; Matthew S. Dyer. *Physical Chemistry Chemical Physics*. [Paper](https://doi.org/10.1039/d2cp02180c)

**Method:** Variable-composition ChemDASH extends basin hopping to substitutions in a spinel phase field.. Spinel configuration → substitutions / atom swaps → energy minimization → composition–configuration search

**Inputs:** Known spinel structure family and bounded chemical phase field

**Software:** [ChemDASH](software.md#chemdash)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1039/d2cp02180c)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1039/d2cp02180c)

**Scope:** Demonstrated in a specified structure family; it does not search every possible topology for every composition.

<a id="csp136"></a>
### 2023 — Reducing overprediction of molecular crystal structures via threshold clustering

**CSP136 · Journal article · Molecular / organic**

Patrick W. V. Butler; Graeme M. Day. *Proceedings of the National Academy of Sciences*. [Paper](https://doi.org/10.1073/pnas.2300516120)

**Method:** Threshold clustering of landscape minima. Group low-barrier connected energy minima into basins to reduce overcounting candidate polymorphs.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [mol-CSPy: quasi-random sampling, QRBH and threshold MC](software.md#mol-cspy)

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://www.pnas.org/doi/10.1073/pnas.2300516120)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1073/pnas.2300516120) · [source 2](https://www.pnas.org/doi/10.1073/pnas.2300516120)

**Scope:** Post-processing of generated landscapes; kinetic stability estimates depend on model/threshold and do not fully model nucleation.

<a id="csp161"></a>
### 2025 — A robust crystal structure prediction method to support small molecule drug development with large scale validation and blind study

**CSP161 · Journal article · Molecular / organic**

Dong Zhou; Imanuel Bier; Biswajit Santra; Leif D. Jacobson; Chuanjie Wu; Adiran Garaizar Suarez; Barbara Ramirez Almaguer; Haoyu Yu; Robert Abel; Richard A. Friesner; Lingle Wang. *Nature Communications*. [Paper](https://doi.org/10.1038/s41467-025-57479-1)

**Method:** Conformer search, symmetry-constrained MD and hierarchical refinement. Separate molecular conformer generation from lattice packing exploration; use force-field dynamics/minimization and quantum refinement.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [Schrödinger Crystal Structure Prediction](software.md#schrodinger-csp)

**Groups:** [Lingle Wang–Friesner / Schrödinger collaboration](https://www.nature.com/articles/s41467-025-57479-1)

**Evidence:** Primary abstract and selected discussion/benchmark. [source 1](https://doi.org/10.1038/s41467-025-57479-1) · [source 2](https://www.nature.com/articles/s41467-025-57479-1)

**Scope:** Validation emphasized neat crystals with Z-prime 1 or 0.5; large flexible/multicomponent/disordered problems remain distinct.

## Adaptive and ML-guided search

<a id="csp059"></a>
### 2014 — An adaptive genetic algorithm for crystal structure prediction

**CSP059 · Published journal article · Atomic / inorganic**

S Q Wu; M Ji; C Z Wang; M C Nguyen; X Zhao; K Umemoto; R M Wentzcovitch; K M Ho. *Journal of Physics: Condensed Matter*. [Paper](https://doi.org/10.1088/0953-8984/26/3/035402)

**Method:** Iteratively fit classical potentials to DFT data and use them for fast evolutionary structure exploration.. Iteratively fit classical potentials to DFT data and use them for fast evolutionary structure exploration.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [Adaptive Genetic Algorithm (AGA; Wang–Ho collaboration)](software.md#aga)

**Groups:** [Ho–Wang–Wu / adaptive-GA team](https://arxiv.org/abs/1309.4742)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1088/0953-8984/26/3/035402) · [source 2](https://arxiv.org/abs/1309.4742)

**Scope:** Adaptive potentials must be checked against DFT outside the structures sampled for fitting.

<a id="csp065"></a>
### 2016 — Accurate and efficient representation of intramolecular energy inab initiogeneration of crystal structures. I. Adaptive local approximate models

**CSP065 · Journal article · Molecular / organic**

Isaac Sugden; Claire S. Adjiman; Constantinos C. Pantelides. *Acta Crystallographica Section B Structural Science, Crystal Engineering and Materials*. [Paper](https://doi.org/10.1107/S2052520616015122)

**Method:** Adaptive local approximate models. Adaptively place local QM-based intramolecular models during CrystalPredictor exploration to improve computational allocation.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CrystalPredictor / CrystalPredictor II](software.md#crystalpredictor)

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://pmc.ncbi.nlm.nih.gov/articles/PMC5134761/)

**Evidence:** Primary full-text selected introduction/methods. [source 1](https://doi.org/10.1107/S2052520616015122) · [source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC5134761/)

**Scope:** Local-model accuracy and finite sampling remain important; adaptive surrogates do not establish a ground-state certificate.

<a id="csp075"></a>
### 2018 — Crystal structure prediction accelerated by Bayesian optimization

**CSP075 · Published journal article · Atomic / inorganic**

Tomoki Yamashita; Nobuya Sato; Hiori Kino; Takashi Miyake; Koji Tsuda; Tamio Oguchi. *Physical Review Materials*. [Paper](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803)

**Method:** Bayesian selection of candidate relaxations. Random candidate pool → learned energy/acquisition score → priority DFT relaxation → update

**Inputs:** Formula, candidate pool and energy calculations

**Software:** [CrySPY / BO / LAQA](software.md#cryspy-bo-laqa)

**Groups:** [Yamashita–Tsuda / adaptive CSP collaboration](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803)

**Scope:** Candidate selection accelerates a supplied pool; no global-optimality certificate.

<a id="csp077"></a>
### 2018 — Fine-grained optimization method for crystal structure prediction

**CSP077 · Published journal article · Atomic / inorganic**

Kei Terayama; Tomoki Yamashita; Tamio Oguchi; Koji Tsuda. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-018-0090-y)

**Method:** LAQA: Look Ahead based on Quadratic Approximation. Random candidates → partial relaxations → energy/force estimate of final energy → allocate next step

**Inputs:** Formula and randomly generated starting structures

**Software:** [CrySPY / BO / LAQA](software.md#cryspy-bo-laqa)

**Groups:** [Yamashita–Tsuda / adaptive CSP collaboration](https://www.nature.com/articles/s41524-018-0090-y)

**Evidence:** Publisher abstract and LAQA scoring-method excerpt. [source 1](https://www.nature.com/articles/s41524-018-0090-y)

**Scope:** Adaptive relaxation allocation; LAQA is not itself a trained crystal generator.

<a id="csp094"></a>
### 2020 — CRYSPNet: Crystal structure predictions via neural networks

**CSP094 · Published journal article · Atomic / inorganic**

Haotong Liang; Valentin Stanev; A. Gilad Kusne; Ichiro Takeuchi. *Physical Review Materials*. [Paper](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802)

**Method:** Hierarchical neural prediction of crystallographic descriptors. Composition → Bravais lattice / space group / lattice-parameter predictors → candidate constraints

**Inputs:** Chemical composition

**Software:** [CRYSPNet](software.md#cryspnet)

**Groups:** [Takeuchi / Stanev / Kusne collaboration](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802)

**Scope:** Does not independently predict a full set of fractional atomic positions; use as a CSP prior rather than complete unconstrained CSP.

<a id="csp095"></a>
### 2020 — Efficient Global Structure Optimization with a Machine-Learned Surrogate Model

**CSP095 · Published journal article · Surfaces / clusters (adjacent)**

Malthe K. Bisbo; Bjørk Hammer. *Physical Review Letters*. [Paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102)

**Method:** GOFEE: GP surrogate and acquisition-based global optimization. Structural proposals → surrogate local optimization → uncertainty-aware acquisition → single-point DFT → retrain

**Inputs:** Atomic system, candidate population and expensive evaluator

**Software:** [AGOX / GOFEE](software.md#agox-gofee)

**Groups:** [Bjørk Hammer / AGOX collaboration](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102)

**Scope:** Original demonstrations concern surface reconstructions / graphene-on-Ir, rather than bulk formula-only CSP; transferable search architecture.

<a id="csp100"></a>
### 2021 — Accelerating materials discovery with Bayesian optimization and graph deep learning

**CSP100 · Published journal article · Atomic / inorganic**

Yunxing Zuo; Mingde Qin; Chi Chen; Weike Ye; Xiangguo Li; Jian Luo; Shyue Ping Ong. *Materials Today*. [Paper](https://www.sciencedirect.com/science/article/pii/S1369702121002984)

**Method:** BOWSR: Bayesian optimization with symmetry relaxation. Template / initial crystal → symmetry-preserving structural-variable BO with graph energy model → refined geometry

**Inputs:** Initial candidate crystal, fixed symmetry / Wyckoff configuration

**Software:** [BOWSR (maml)](software.md#bowsr-maml)

**Groups:** [Shyue Ping Ong / Materials Virtual Lab](https://www.sciencedirect.com/science/article/pii/S1369702121002984)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://www.sciencedirect.com/science/article/pii/S1369702121002984) · [source 2](https://arxiv.org/abs/2104.10242) · [source 3](https://materialsvirtuallab.org/pubs/10.1016_j.mattod.2021.08.012.pdf)

**Scope:** Local symmetry-constrained structural relaxation, rather than unrestricted search over all unknown symmetries.

<a id="csp102"></a>
### 2021 — CrySPY: a crystal structure prediction tool accelerated by machine learning

**CSP102 · Published journal article · Atomic / inorganic**

Tomoki Yamashita; Shinichi Kanehira; Nobuya Sato; Hiori Kino; Kei Terayama; Hikaru Sawahata; Takumi Sato; Futoshi Utsuno; Koji Tsuda; Takashi Miyake; Tamio Oguchi. *Science and Technology of Advanced Materials: Methods*. [Paper](https://www.tandfonline.com/doi/full/10.1080/27660400.2021.1943171)

**Method:** Modular random / evolutionary / BO / LAQA CSP. Generate candidates → select / relax / evaluate → track evolving candidate pool

**Inputs:** Formula, cell / symmetry bounds and external relaxation code

**Software:** [CrySPY / BO / LAQA](software.md#cryspy-bo-laqa)

**Groups:** [Yamashita–Tsuda / adaptive CSP collaboration](https://www.tandfonline.com/doi/full/10.1080/27660400.2021.1943171)

**Evidence:** Publisher-indexed abstract and author list; direct page fetch returned403. [source 1](https://www.tandfonline.com/doi/full/10.1080/27660400.2021.1943171)

**Scope:** Software orchestrates several algorithms; performance depends on evaluator and configured search.

<a id="csp106"></a>
### 2021 — MAISE: Construction of neural network interatomic models and evolutionary structure optimization

**CSP106 · Published journal article · Atomic / inorganic**

Samad Hajinazar; Aidan Thorn; Ernesto D. Sandoval; Saba Kharabadze; Aleksey N. Kolmogorov. *Computer Physics Communications*. [Paper](https://doi.org/10.1016/j.cpc.2020.107679)

**Method:** Construct neural-network potentials from evolutionary samples and use them in global crystal searches.. Construct neural-network potentials from evolutionary samples and use them in global crystal searches.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Software:** [MAISE](software.md#maise)

**Groups:** [Kolmogorov / MAISE team](https://arxiv.org/abs/2005.12131)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1016/j.cpc.2020.107679) · [source 2](https://arxiv.org/abs/2005.12131)

**Scope:** Potential quality depends on sampled chemistry and structural environments.

<a id="csp112"></a>
### 2022 — Atomistic global optimization X: A Python package for optimization of atomistic structures

**CSP112 · Published journal article · Surfaces / clusters (adjacent)**

Mads-Peter V. Christiansen; Nikolaj Rønne; Bjørk Hammer. *The Journal of Chemical Physics*. [Paper](https://arxiv.org/abs/2204.01451)

**Method:** AGOX modular atomistic global optimization framework. Assemble proposal / sampler / surrogate / acquisition / evaluator modules → iterative search

**Inputs:** Atomic system and chosen algorithm modules

**Software:** [AGOX / GOFEE](software.md#agox-gofee)

**Groups:** [Bjørk Hammer / AGOX collaboration](https://arxiv.org/abs/2204.01451)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://arxiv.org/abs/2204.01451)

**Scope:** Framework is broader than periodic bulk CSP; original challenging demonstration is a nitride cluster embedded in graphene.

<a id="csp114"></a>
### 2022 — Crystal structure prediction by combining graph network and optimization algorithm

**CSP114 · Published journal article · Atomic / inorganic**

Guanjian Cheng; Xin-Gao Gong; Wan-Jian Yin. *Nature Communications*. [Paper](https://www.nature.com/articles/s41467-022-29241-4)

**Method:** GN-OA: graph energy model plus RS / PSO / BO. Crystal proposals → graph-predicted formation energy → optimization algorithm selects new proposals

**Inputs:** Composition and structural parameter bounds

**Software:** [GN-OA](software.md#gn-oa)

**Groups:** [Soochow · Wan-Jian Yin / Guanjian Cheng](https://www.nature.com/articles/s41467-022-29241-4)

**Evidence:** Publisher abstract, discussion failure modes and author-affiliation section. [source 1](https://www.nature.com/articles/s41467-022-29241-4)

**Scope:** Relaxed-state formation-energy surrogate may misrank candidate geometries; source distinguishes energy-model failure from optimizer failure.

<a id="csp117"></a>
### 2022 — Hybrid algorithm of Bayesian optimization and evolutionary algorithm in crystal structure prediction

**CSP117 · Published journal article · Atomic / inorganic**

Tomoki Yamashita; Hiori Kino; Koji Tsuda; Takashi Miyake; Tamio Oguchi. *Science and Technology of Advanced Materials: Methods*. [Paper](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2055987)

**Method:** Bayesian optimization plus evolutionary candidate generation. Evolutionary structural proposals → BO candidate selection → relaxation → update

**Inputs:** Composition, population and evaluator

**Software:** [CrySPY / BO / LAQA](software.md#cryspy-bo-laqa)

**Groups:** [Yamashita–Tsuda / adaptive CSP collaboration](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2055987)

**Evidence:** Publisher-indexed abstract plus institutional author / publication list; direct publisher fetch returned403. [source 1](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2055987) · [source 2](https://mdcl.issp.u-tokyo.ac.jp/scc/wp/wp-content/uploads/2022/08/2021_04_publication.pdf)

**Scope:** Hybrid candidate proposal and selection; evaluation-specific efficiency is not a general convergence guarantee.

<a id="csp118"></a>
### 2022 — Improvement of look ahead based on quadratic approximation for crystal structure prediction

**CSP118 · Published journal article · Atomic / inorganic**

Tomoki Yamashita; Hirotaka Sekine. *Science and Technology of Advanced Materials: Methods*. [Paper](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2059335)

**Method:** Improved LAQA including stress term. Partly relaxed candidates → stress-aware priority score → next relaxation allocation

**Inputs:** Composition, candidate pool and stress / forces

**Software:** [CrySPY / BO / LAQA](software.md#cryspy-bo-laqa)

**Groups:** [Yamashita–Tsuda / adaptive CSP collaboration](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2059335)

**Evidence:** Publisher-indexed abstract and issue author list; direct article fetch returned403. [source 1](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2059335) · [source 2](https://www.tandfonline.com/toc/tstm20/2/1)

**Scope:** Improves relaxation allocation within the chosen pool; completeness is not claimed.

<a id="csp120"></a>
### 2022 — Rapid discovery of stable materials by coordinate-free coarse graining

**CSP120 · Published journal article · Atomic / inorganic**

Rhys E. A. Goodall; Abhijith S. Parackal; Felix A. Faber; Rickard Armiento; Alpha A. Lee. *Science Advances*. [Paper](https://www.science.org/doi/10.1126/sciadv.abn4117)

**Method:** Wren: coordinate-free Wyckoff-representation energy surrogate. Enumerate / construct chemical Wyckoff representations → predict energy → select DFT structure evaluation

**Inputs:** Composition plus Wyckoff / symmetry representation

**Software:** [Wren (aviary)](software.md#wren-aviary)

**Groups:** [Goodall / Armiento / Alpha Lee collaboration](https://www.science.org/doi/10.1126/sciadv.abn4117)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://www.science.org/doi/10.1126/sciadv.abn4117) · [source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9328671/) · [source 3](https://arxiv.org/abs/2106.11132)

**Scope:** Does not directly resolve every continuous coordinate; coarse representation needs a downstream full-structure stage.

<a id="csp121"></a>
### 2022 — Reliable crystal structure predictions from first principles

**CSP121 · Journal article · Molecular / organic**

Rahul Nikhar; Krzysztof Szalewicz. *Nature Communications*. [Paper](https://doi.org/10.1038/s41467-022-30692-y)

**Method:** SAPT-derived ab initio force field and hierarchical search. Fit dimer-based aiFF, generate extensive packing candidates, refine thousands with aiFF and rerank a small set by periodic DFT+D; optionally refit to candidate-derived dimers.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CSP(aiFF) / autoPES–UPACK workflow](software.md#csp-aiff)

**Groups:** [Szalewicz–Nikhar / CSP(aiFF)](https://www.nature.com/articles/s41467-022-30692-y)

**Evidence:** Primary full-text selected abstract/methods/limitations. [source 1](https://doi.org/10.1038/s41467-022-30692-y) · [source 2](https://www.nature.com/articles/s41467-022-30692-y)

**Scope:** Rigid-monomer, primarily two-body approximation and finite 15-molecule validation; thermal and many-body effects can matter.

<a id="csp124"></a>
### 2023 — A Continuous Action Space Tree search for INverse desiGn (CASTING) framework for materials discovery

**CSP124 · Published journal paper · Atomic / inorganic**

Suvo Banik; Troy Loefller; Sukriti Manna; Henry Chan; Srilok Srinivasan; Pierre Darancet; Alexander Hexemer; Subramanian K. R. S. Sankaranarayanan. *npj Computational Materials*. [Paper](https://doi.org/10.1038/s41524-023-01128-y)

**Method:** Continuous-action Monte Carlo tree search explores structure and design variables.. Define design space → tree selection / expansion → adaptive rollout → energy or objective evaluation

**Inputs:** Composition, geometry bounds and an objective

**Software:** [CASTING](software.md#casting)

**Groups:** [Sankaranarayanan–Banik–Manna / CASTING collaboration](https://doi.org/10.1038/s41524-023-01128-y)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1038/s41524-023-01128-y)

**Scope:** Crystal applications share a general optimization framework; performance depends on objective, representation and sampling bounds.

<a id="csp131"></a>
### 2023 — Deep Learning-Based Prediction of Contact Maps and Crystal Structures of Inorganic Materials

**CSP131 · Published journal article · Atomic / inorganic**

Jianjun Hu; Yong Zhao; Qin Li; Yuqi Song; Rongzhi Dong; Wenhui Yang; Edirisuriya M. D. Siriwardane. *ACS Omega*. [Paper](https://pubs.acs.org/doi/10.1021/acsomega.3c02115)

**Method:** AlphaCrystal: learned contact maps plus genetic reconstruction. Composition → contact map / symmetry / lattice predictions → GA coordinate reconstruction → DFT refinement

**Inputs:** Composition plus predicted or specified crystallographic constraints

**Software:** [AlphaCrystal](software.md#alphacrystal)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://pubs.acs.org/doi/10.1021/acsomega.3c02115)

**Evidence:** Primary full-text framework and benchmark / data excerpts. [source 1](https://pubs.acs.org/doi/10.1021/acsomega.3c02115) · [source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10373470/)

**Scope:** Contact-map fidelity alone does not uniquely determine structure. Small training-cell limit and dependence on symmetry / lattice priors must be considered.

<a id="csp137"></a>
### 2023 — Reinforcement learning in crystal structure prediction

**CSP137 · Published journal paper · Atomic / inorganic**

Elena Zamaraeva; Christopher M. Collins; Dmytro Antypov; Vladimir V. Gusev; Rahul Savani; Matthew S. Dyer; George R. Darling; Igor Potapov; Matthew J. Rosseinsky; Paul G. Spirakis. *Digital Discovery*. [Paper](https://doi.org/10.1039/d3dd00063j)

**Method:** A learned policy selects basin-hopping moves during the run.. FUSE / MC-EMMA → policy chooses moves → relaxation → reward and policy update

**Inputs:** Composition/phase field and an existing CSP move set

**Software:** [RL-CSP](software.md#rl-csp)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1039/d3dd00063j)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1039/d3dd00063j)

**Scope:** The reported tests cover selected compositions; adaptive move selection does not certify a global minimum.

<a id="csp139"></a>
### 2024 — AlphaCrystal-II: Distance matrix based crystal structure prediction using deep learning

**CSP139 · Preprint · Atomic / inorganic**

Yuqi Song; Rongzhi Dong; Lai Wei; Qin Li; Jianjun Hu. *arXiv*. [Paper](https://arxiv.org/abs/2404.04810)

**Method:** AlphaCrystal-II: learned distance matrices and coordinate reconstruction. Formula → interatomic distance prediction → reconstruct periodic crystal geometry

**Inputs:** Composition and structural reconstruction constraints

**Software:** [AlphaCrystal-II](software.md#alphacrystal-ii)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://arxiv.org/abs/2404.04810)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://arxiv.org/abs/2404.04810)

**Scope:** Reference reconstruction must be distinguished from an energy-ranked ground-state search.

<a id="csp147"></a>
### 2024 — Inferring energy–composition relationships with Bayesian optimization enhances exploration of inorganic materials

**CSP147 · Published journal paper · Atomic / inorganic**

Andrij Vasylenko; Benjamin M. Asher; Christopher M. Collins; Michael W. Gaultois; George R. Darling; Matthew S. Dyer; Matthew J. Rosseinsky. *The Journal of Chemical Physics*. [Paper](https://doi.org/10.1063/5.0180818)

**Method:** PhaseBO adaptively selects compositions for expensive structure/energy evaluation.. Composition domain → Bayesian proposal → structure search / energy → update composition model

**Inputs:** A bounded phase field and energy-evaluation workflow

**Software:** [PhaseBO](software.md#phasebo)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1063/5.0180818)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1063/5.0180818)

**Scope:** Composition-space optimization is an outer loop around CSP, not a replacement for inner structure prediction.

<a id="csp150"></a>
### 2024 — Machine-Learned Potentials by Active Learning from Organic Crystal Structure Prediction Landscapes

**CSP150 · Journal article · Molecular / organic**

Patrick W. V. Butler; Roohollah Hafizi; Graeme M. Day. *The Journal of Physical Chemistry A*. [Paper](https://doi.org/10.1021/acs.jpca.3c07129)

**Method:** Query-by-committee active learning and delta potentials. Select high-uncertainty configurations from predicted packing landscapes and Monte Carlo trajectories for target-DFT labels and iterative potential fitting.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CSP-AL (committee active / delta learning)](software.md#csp-al-molecular)

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://pubs.acs.org/doi/10.1021/acs.jpca.3c07129)

**Evidence:** Primary full-text selected workflow/discussion. [source 1](https://doi.org/10.1021/acs.jpca.3c07129) · [source 2](https://pubs.acs.org/doi/10.1021/acs.jpca.3c07129)

**Scope:** Initial landscape/conformation coverage matters; learned low-energy accuracy does not guarantee universal off-landscape stability.

<a id="csp153"></a>
### 2024 — Shotgun crystal structure prediction using machine-learned formation energies

**CSP153 · Published journal article · Atomic / inorganic**

Chang Liu; Hiromasa Tamaki; Tomoyasu Yokoyama; Kensuke Wakasugi; Satoshi Yotsuhashi; Minoru Kusaba; Artem R. Oganov; Ryo Yoshida. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-024-01471-8)

**Method:** ShotgunCSP: fine-tuned surrogate screening of generated libraries. Template substitution or Wyckoff generator → composition-specific pre-relaxed energy model → shortlist → DFT relax

**Inputs:** Formula, generated structure library and DFT single-point labels

**Software:** [ShotgunCSP](software.md#shotguncsp)

**Groups:** [Ryo Yoshida / Kusaba–Liu collaboration](https://www.nature.com/articles/s41524-024-01471-8)

**Evidence:** Publisher workflow, discussion and correction notice. [source 1](https://www.nature.com/articles/s41524-024-01471-8) · [source 2](https://doi.org/10.1038/s41524-025-01692-5)

**Scope:** Noniterative screening still requires query-specific labels and a sufficiently rich library. Journal benchmark differs from early preprint; correction published20June2025.

<a id="csp162"></a>
### 2025 — Accelerating crystal structure search through active learning with neural networks for rapid relaxations

**CSP162 · Published journal article · Atomic / inorganic**

Stefaan S. P. Hessmann; Kristof T. Schütt; Niklas W. A. Gebauer; Michael Gastegger; Tamio Oguchi; Tomoki Yamashita. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-025-01523-7)

**Method:** Active-learning force-field ensembles for candidate-pool relaxation. Random candidate pool → uncertainty-aware NNP relaxation → select DFT labels / validate minima → retrain

**Inputs:** Composition, candidate pool, DFT labels

**Software:** [active-csp](software.md#active-csp)

**Groups:** [Hessmann / Schütt / Yamashita collaboration](https://www.nature.com/articles/s41524-025-01523-7)

**Evidence:** Publisher abstract, candidate-generation and training-bias excerpts. [source 1](https://www.nature.com/articles/s41524-025-01523-7)

**Scope:** Small benchmark chemistries and larger-cell transfer studied; symmetry-biased training can harm relaxation accuracy.

<a id="csp168"></a>
### 2025 — Crystal structure prediction of organic molecules by machine learning-based lattice sampling and structure relaxation

**CSP168 · Journal article · Molecular / organic**

Takuya Taniguchi; Ryo Fukasawa. *Digital Discovery*. [Paper](https://doi.org/10.1039/D5DD00304K)

**Method:** Space-group/density-prior ML-guided lattice sampling. Predict space-group probabilities and density from molecular features, sample compatible lattices and relax with PFP neural potentials.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [SPaDe-CSP](software.md#spade-csp)

**Groups:** [Taniguchi–Fukasawa / SPaDe-CSP](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00304k)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1039/D5DD00304K) · [source 2](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00304k)

**Scope:** Training restricts to selected space groups and Z-prime 1; some controlled tests use reference-derived molecular geometries.

<a id="csp148"></a>
### 2025 — Integration of generative machine learning with the heuristic crystal structure prediction code FUSE

**CSP148 · Published journal paper · Atomic / inorganic**

Christopher M. Collins; Hasan M. Sayeed; George R. Darling; John B. Claridge; Taylor D. Sparks; Matthew J. Rosseinsky. *Faraday Discussions*. [Paper](https://doi.org/10.1039/d4fd00094c)

**Method:** FUSE2: graph-network energy-surrogate / Bayesian-optimization seeding followed by flexible-unit basin hopping. Specified composition and formula-unit counts → GN-OA/BO structural search → rank seeds → FUSE2 basin hopping → local relaxation and final ranking

**Inputs:** Composition, generative model and heuristic CSP settings

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility — [Mechanisms and limits](structural-priors.md)

**Software:** [FUSE / FUSE2](software.md#fuse)

**Groups:** [Rosseinsky–Dyer–Collins / Liverpool CSP collaboration](https://doi.org/10.1039/d4fd00094c)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1039/d4fd00094c) · [source 2](https://livrepository.liverpool.ac.uk/3184543/1/C_Collins_accepted.pdf)

**Scope:** Online publication 2024; journal issue 2025. Seeding improves tested searches but does not remove distribution or energy-model limits.

## Learned generation and conditional CSP

<a id="csp086"></a>
### 2019 — CrystalGAN: Learning to Discover Crystallographic Structures with Generative Adversarial Networks

**CSP086 · Published workshop paper, MAKE2019; preprint2018 · Atomic / inorganic**

Asma Nouira; Nataliya Sokolovska; Jean-Claude Crivello. *AAAI Spring Symposium MAKE2019, CEUR2350*. [Paper](https://ceur-ws.org/Vol-2350/paper18.pdf)

**Method:** CrystalGAN: cross-domain GAN from binary to ternary hydrides. Known binary hydride domains → cross-domain adversarial translation plus geometric constraints → ternary candidates

**Inputs:** Training binary domains / constrained chemical systems

**Software:** [CrystalGAN](software.md#crystalgan)

**Groups:** [Nouira / Sokolovska / Crivello collaboration](https://ceur-ws.org/Vol-2350/paper18.pdf)

**Evidence:** Workshop paper first page / abstract, arXiv metadata and author repository evaluation description. [source 1](https://ceur-ws.org/Vol-2350/paper18.pdf) · [source 2](https://arxiv.org/abs/1810.11203) · [source 3](https://github.com/asmanouira/CrystalGAN) · [source 4](https://github.com/asmanouira/CrystalGAN/blob/master/post_processing.py)

**Scope:** 2018 preprint,2019 workshop. Geometric plausibility and domain translation do not establish thermodynamic stability or general formula-only CSP.

<a id="csp087"></a>
### 2019 — Data-Driven Approach to Encoding and Decoding 3-D Crystal Structures

**CSP087 · Preprint · Atomic / inorganic**

Jordan Hoffmann; Louis Maestrati; Yoshihide Sawada; Jian Tang; Jean Michel Sellier; Yoshua Bengio. *arXiv*. [Paper](https://arxiv.org/abs/1909.00949)

**Method:** Density-grid VAE / encoder-decoder plus U-Net species segmentation. Crystal → smooth density grid → latent encoding → decoded grid → atom/type segmentation

**Inputs:** Encoded complete structure, latent sample or interpolation

**Software:** [DD3DCS / Encoding-Decoding 3D Crystals](software.md#dd3dcs-encoding-decoding-3d-crystals)

**Groups:** [Yoshua Bengio / Hoffmann collaboration](https://arxiv.org/abs/1909.00949)

**Evidence:** Primary abstract and author repository architecture description. [source 1](https://arxiv.org/abs/1909.00949) · [source 2](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals)

**Scope:** Often abbreviated DD3DCS in surveys. Author code describes a VAE and U-Net; avoid copying a survey GAN label without qualification. Reconstruction is not formula-only CSP.

<a id="csp088"></a>
### 2019 — Inverse Design of Solid-State Materials via a Continuous Representation

**CSP088 · Published, Matter 1, 1370–1384 · Atomic / inorganic**

Juhwan Noh; Jaehoon Kim; Helge S. Stein; Benjamin Sanchez-Lengeling; John M. Gregoire; Alan Aspuru-Guzik; Yousung Jung. *Matter*. [Paper](https://doi.org/10.1016/j.matt.2019.08.017)

**Method:** iMatGen: image-based hierarchical variational autoencoders. Crystal images → continuous latent space → generate/decode → relax and assess

**Inputs:** Training data / sampled latent variable

**Software:** [iMatGen](software.md#imatgen)

**Groups:** [Yousung Jung](https://doi.org/10.1016/j.matt.2019.08.017)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher summary/highlights and author-hosted accepted paper excerpts. [source 1](https://doi.org/10.1016/j.matt.2019.08.017) · [source 2](https://light.utoronto.ca/wp-content/uploads/2020/09/matter_inverse_design.pdf)

**Scope:** Learned candidate generation; not a generic formula-only CSP solver. Restricted V-O demonstration; generated metastability is not experimental synthesis.

<a id="csp092"></a>
### 2020 — 3‑D Inorganic Crystal Structure Generation and Property Prediction via Representation Learning

**CSP092 · Published journal article · Atomic / inorganic**

Callum
J. Court; Batuhan Yildirim; Apoorv Jain; Jacqueline M. Cole. *Journal of Chemical Information and Modeling*. [Paper](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464)

**Method:** ICSG3D: conditional feature-consistent VAE plus U-Net reconstruction. Energy-conditioned voxel VAE → decoded density field → U-Net atom segmentation → graph property prediction

**Inputs:** Latent sample, optional formation-energy condition

**Software:** [Cond-DFC-VAE / ICSG3D](software.md#cond-dfc-vae-icsg3d)

**Groups:** [Jacqueline Cole / Court collaboration](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464)

**Evidence:** Publisher scope / architecture and conclusions, author-hosted publication record. [source 1](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464) · [source 2](https://cjcourt.github.io/publication/jcim_2020) · [source 3](https://github.com/by256/icsg3d) · [source 4](https://github.com/by256/icsg3d/blob/master/generate.py)

**Scope:** Voxel-resolution and trained structure-family limits. Author paper specifies a conditional VAE, not a GAN; property-conditioned generation differs from fixed-formula CSP.

<a id="csp097"></a>
### 2020 — Generative Adversarial Networks for Crystal Structure Prediction

**CSP097 · Published journal article · Atomic / inorganic**

Sungwon Kim; Juhwan Noh; Geun Ho Gu; Alan Aspuru-Guzik; Yousung Jung. *ACS Central Science*. [Paper](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426)

**Method:** Composition-conditioned point-cloud crystal GAN. Formula condition → GAN lattice / fractional coordinates → HTVS → DFT assessment

**Inputs:** Composition within trained Mg–Mn–O chemistry

**Software:** [Composition-Conditioned Crystal GAN](software.md#composition-conditioned-crystal-gan)

**Groups:** [Yousung Jung / Aspuru-Guzik collaboration](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426)

**Evidence:** Publisher abstract / conclusions and primary arXiv author list. [source 1](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426) · [source 2](https://arxiv.org/abs/2004.01396) · [source 3](https://arxiv.org/pdf/2004.01396)

**Scope:** Limited demonstrated chemistry; generated candidates are proposed structures requiring independent energy ranking.

<a id="csp101"></a>
### 2021 — Constrained crystals deep convolutional generative adversarial network for the inverse design of crystal structures

**CSP101 · Published, npj Computational Materials 7, 66 · Atomic / inorganic**

Teng Long; Nuno M. Fortunato; Ingo Opahle; Yixuan Zhang; Ilias Samathrakis; Chen Shen; Oliver Gutfleisch; Hongbin Zhang. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-021-00526-4)

**Method:** CCDCGAN: GAN plus property feedback/backpropagation. GAN sample + post hoc energy filter OR energy feedback → latent/generator optimization → DFT relaxation

**Inputs:** Training crystals / desired properties

**Software:** [CCDCGAN](software.md#ccdcgan)

**Groups:** [Hongbin Zhang](https://www.nature.com/articles/s41524-021-00526-4)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher abstract, Introduction and author list. [source 1](https://www.nature.com/articles/s41524-021-00526-4) · [source 2](https://arxiv.org/abs/2007.11228) · [source 3](https://www.nature.com/articles/s41524-021-00526-4.pdf)

**Scope:** Constrained generative design; applicability beyond trained chemistry must be tested. Contrasts screening with integrated optimization; formation energy alone is not convex-hull stability.

<a id="csp105"></a>
### 2021 — High‐Throughput Discovery of Novel Cubic Crystal Materials Using Deep Generative Neural Networks

**CSP105 · Published, Advanced Science 8, 2100566 · Atomic / inorganic**

Yong Zhao; Mohammed Al‐Fahdi; Ming Hu; Edirisuriya M. D. Siriwardane; Yuqi Song; Alireza Nasiri; Jianjun Hu. *Advanced Science*. [Paper](https://doi.org/10.1002/advs.202100566)

**Method:** CubicGAN, element/space-group conditioned GAN. Element set + space group + noise → cubic structures → screening → DFT and phonons

**Inputs:** Element and cubic space-group conditions

**Software:** [CubicGAN](software.md#cubicgan)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://doi.org/10.1002/advs.202100566)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher methods/contribution excerpts; author institutional full citation. [source 1](https://doi.org/10.1002/advs.202100566) · [source 2](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202100566) · [source 3](https://www.nature.com/articles/s41524-022-00850-3)

**Scope:** Cubic symmetry constraint limits the explored polymorph space. Conditions constrain chemistry/symmetry rather than arbitrary functional-property targets; reported phonon validation applies selected candidates.

<a id="csp111"></a>
### 2022 — An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties

**CSP111 · Published, Matter 5, 314–335 · Atomic / inorganic**

Zekun Ren; Siyu Isaac Parker Tian; Juhwan Noh; Felipe Oviedo; Guangzong Xing; Jiali Li; Qiaohao Liang; Ruiming Zhu; Armin G. Aberle; Shijing Sun; Xiaonan Wang; Yi Liu; Qianxiao Li; Senthilnath Jayavelu; Kedar Hippalgaonkar; Yousung Jung; Tonio Buonassisi. *Matter*. [Paper](https://doi.org/10.1016/j.matt.2021.11.032)

**Method:** FTCP representation with property-structured VAE latent space. Target property → sample semantic latent space → decode composition/lattice/coordinates → validate

**Inputs:** Training crystals / property target

**Software:** [FTCP](software.md#ftcp)

**Groups:** [Yousung Jung](https://doi.org/10.1016/j.matt.2021.11.032)

**Evidence:** Reused source-qualified inverse-design catalogue: Author code README with complete citation and sampling workflow; institutional accepted-manuscript record. [source 1](https://doi.org/10.1016/j.matt.2021.11.032) · [source 2](https://arxiv.org/abs/2005.07609) · [source 3](https://github.com/PV-Lab/FTCP) · [source 4](https://arxiv.org/html/2005.07609v2)

**Scope:** Representation and generative inverse design; not a general proof of ground-state CSP. Institutional metadata points to 10.1016/j.matt.2022.01.022; author repository gives original article DOI 2021.11.032. Treat later DOI as a separate correction record to verify, not a second method.

<a id="csp113"></a>
### 2022 — Crystal Diffusion Variational Autoencoder for Periodic Material Generation

**CSP113 · Published, ICLR 2022; preprint 2021 · Atomic / inorganic**

Tian Xie; Xiang Fu; Octavian-Eugen Ganea; Regina Barzilay; Tommi Jaakkola. *Published, ICLR 2022; preprint 2021*. [Paper](https://arxiv.org/abs/2110.06197)

**Method:** CDVAE: equivariant VAE with score-based coordinate/type decoder. Sample or optimize latent → predict composition/lattice → denoise atoms → evaluate

**Inputs:** Latent sample, or complete structure to encode

**Software:** [CDVAE](software.md#cdvae)

**Groups:** [Tian Xie + collaborators](https://arxiv.org/abs/2110.06197) · [Regina Barzilay / Tommi Jaakkola](https://arxiv.org/abs/2110.06197)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary arXiv abstract; author repository and ICLR bibliographic record. [source 1](https://arxiv.org/abs/2110.06197) · [source 2](https://github.com/txie-93/cdvae/blob/f857f598d6f6cca5dc1ea0582d228f12dcc2c2ea/cdvae/pl_modules/model.py) · [source 3](https://arxiv.org/html/2309.04475)

**Scope:** Original reconstruction is structure-conditioned and is not equivalent to predicting from formula alone; later CSP baselines add composition priors. Base generation and latent property optimization are distinct tasks; dataset validity metrics do not establish DFT stability.

<a id="csp126"></a>
### 2023 — An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning

**CSP126 · Published, Nature Communications 14, 7027 · Atomic / inorganic**

Hang Xiao; Rong Li; Xiaoyang Shi; Yan Chen; Liangliang Zhu; Xi Chen; Lei Wang. *Nature Communications*. [Paper](https://www.nature.com/articles/s41467-023-42870-7)

**Method:** SLICES quotient-graph strings with unconditional/conditional RNNs. Generate composition+topology string → graph embedding → force-field geometry → MLIP refinement → property screening/DFT

**Inputs:** SLICES topology string; optional property conditioning

**Software:** [SLICES](software.md#slices)

**Groups:** [Hang Xiao](https://www.nature.com/articles/s41467-023-42870-7)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher abstract, Results benchmark, Discussion and reconstruction methods. [source 1](https://www.nature.com/articles/s41467-023-42870-7)

**Scope:** String reconstruction includes topology constraints and geometric optimization; it is not formula-only CSP. SLICES specifies topology as well as formula; reconstruction uses geometric optimization, not formula-only CSP.

<a id="csp128"></a>
### 2023 — Crystal Structure Prediction by Joint Equivariant Diffusion

**CSP128 · Published, NeurIPS 2023 · Atomic / inorganic**

Rui Jiao; Wenbing Huang; Peijia Lin; Jiaqi Han; Pin Chen; Yutong Lu; Yang Liu. *Published, NeurIPS 2023*. [Paper](https://arxiv.org/abs/2309.04475)

**Method:** DiffCSP, joint diffusion of lattice and fractional coordinates. Fixed composition → joint lattice/coordinate denoising → structure candidates; extended model also denoises atom types

**Inputs:** Atom types and counts / formula; optionally known atom count

**Software:** [DiffCSP](software.md#diffcsp)

**Groups:** [Rui Jiao / Wenbing Huang](https://arxiv.org/abs/2309.04475)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary arXiv abstract; NeurIPS paper first page and author implementation task documentation. [source 1](https://arxiv.org/abs/2309.04475) · [source 2](https://arxiv.org/html/2309.04475)

**Scope:** Reference-structure match under a finite sample budget is distinct from a global energy-minimum guarantee. Fixed-formula CSP is a structure-generation component, not by itself target functional-property inverse design.

<a id="csp130"></a>
### 2023 — Crystal-GFN: sampling crystals with desirable properties and constraints

**CSP130 · AI4Mat at NeurIPS 2023 workshop; arXiv preprint · Atomic / inorganic**

Mila AI4Science; Alex Hernandez-Garcia; Alexandre Duval; Alexandra Volokhova; Yoshua Bengio; Divya Sharma; Pierre Luc Carrier; Yasmine Benabed; Michał Koziarski; Victor Schmidt. *AI4Mat at NeurIPS 2023 workshop; arXiv preprint*. [Paper](https://arxiv.org/abs/2310.04925v2)

**Method:** GFlowNet reward-proportional constrained sequential sampling. Sample space group → composition → lattice parameters under hard constraints → proxy formation-energy reward

**Inputs:** Space-group / composition / lattice constraints and reward model

**Software:** [Crystal-GFN](software.md#crystal-gfn)

**Groups:** [Yoshua Bengio / Mila collaboration](https://arxiv.org/abs/2310.04925)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary 2023 abstract; author slides and official repository workshop citation. [source 1](https://arxiv.org/abs/2310.04925) · [source 2](https://arxiv.org/html/2310.04925v2)

**Scope:** Original Crystal-GFN does not independently generate all atomic coordinates; requires a downstream full-structure stage. Original abstract does not claim generation of independent full atomic coordinates; proxy low formation energy is not competing-phase stability. Author list here follows 2023 abstract; later arXiv version may expand authors.

<a id="csp134"></a>
### 2023 — Physics guided deep learning for generative design of crystal materials with symmetry constraints

**CSP134 · Published, npj Computational Materials 9, 38 · Atomic / inorganic**

Yong Zhao; Edirisuriya M. Dilanga Siriwardane; Zhenyao Wu; Nihang Fu; Mohammed Al-Fahdi; Ming Hu; Jianjun Hu. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-023-00987-9)

**Method:** PGCGM, symmetry-aware GAN with geometric physics losses. Elements + space group + noise → base sites/lattice → symmetry expansion → property/energy screening

**Inputs:** Composition / symmetry conditions

**Software:** [PGCGM](software.md#pgcgm)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://www.nature.com/articles/s41524-023-00987-9)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher model and loss methods excerpts plus arXiv abstract; correction publisher page. [source 1](https://www.nature.com/articles/s41524-023-00987-9) · [source 2](https://arxiv.org/abs/2203.14352) · [source 3](https://www.nature.com/articles/s41524-023-01059-8)

**Scope:** A symmetry-aware proposal generator; not an unrestricted formula-only CSP search. Geometric physics loss is not a first-principles stability guarantee. Author correction 10.1038/s41524-023-01059-8 exists.

<a id="csp138"></a>
### 2023 — Towards Symmetry-Aware Generation of Periodic Materials

**CSP138 · Published conference paper, NeurIPS2023 · Atomic / inorganic**

Youzhi Luo; Chengkai Liu; Shuiwang Ji. *Advances in Neural Information Processing Systems 36*. [Paper](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html)

**Method:** SyMat: symmetry-aware VAE plus score-based coordinate generation. VAE samples element sets and cell geometry → symmetry-aware score model samples periodic coordinates

**Inputs:** Stochastic latent sample; optional property optimization

**Software:** [SyMat (AIRS)](software.md#symat-airs)

**Groups:** [Shuiwang Ji / DIG collaboration](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html) · [source 2](https://arxiv.org/abs/2307.02707) · [source 3](https://papers.nips.cc/paper_files/paper/2023/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)

**Scope:** The reported primary tasks are random generation and property optimization, rather than unrestricted exact-formula energy-ranked CSP.

<a id="csp140"></a>
### 2024 — Crystal structure generation with autoregressive large language modeling

**CSP140 · Published, Nature Communications 15, 10570 · Atomic / inorganic**

Luis M. Antunes; Keith T. Butler; Ricardo Grau-Crespo. *Nature Communications*. [Paper](https://doi.org/10.1038/s41467-024-54639-7)

**Method:** CrystaLLM, autoregressive CIF language model with tree-search extensions. Formula and optional symmetry prompt → CIF token generation → validity checks/energy-assisted search

**Inputs:** CIF prefix including formula and optionally space group

**Software:** [CrystaLLM](software.md#crystallm)

**Groups:** [Ricardo Grau-Crespo / Keith Butler](https://doi.org/10.1038/s41467-024-54639-7)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher abstract and authors; author PDF CSP application excerpt. [source 1](https://doi.org/10.1038/s41467-024-54639-7) · [source 2](https://arxiv.org/abs/2307.04340) · [source 3](https://www.nature.com/articles/s41467-024-54639-7.pdf)

**Scope:** Valid CIF syntax and reference recovery do not establish thermodynamic stability. Generating a full CIF is structurally different from recommending a composition; valid CIF does not establish energy stability.

<a id="csp142"></a>
### 2024 — Deep learning generative model for crystal structure prediction

**CSP142 · Published, npj Computational Materials 2024 · Atomic / inorganic**

Xiaoshan Luo; Zhenyu Wang; Pengyue Gao; Jian Lv; Yanchao Wang; Changfeng Chen; Yanming Ma. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-024-01443-y)

**Method:** Cond-CDVAE, composition- and pressure-conditioned diffusion VAE. Formula + pressure → generated candidate structures → CSP assessment

**Inputs:** Composition, atom count and pressure

**Software:** [Cond-CDVAE](software.md#cond-cdvae)

**Groups:** [Yanming Ma–Yanchao Wang / CALYPSO collaboration](https://www.nature.com/articles/s41524-024-01443-y)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary arXiv abstract, publisher page identity. [source 1](https://www.nature.com/articles/s41524-024-01443-y)

**Scope:** Training-distribution and cell-size limits remain; pressure-specific recovery is not exhaustive phase-diagram prediction. Conditional CSP rather than generic functional-property conditioning; distinguish from Ye et al. Con-CDVAE.

<a id="csp143"></a>
### 2024 — Diffusion probabilistic models enhance variational autoencoder for crystal structure generative modeling

**CSP143 · Published journal article · Atomic / inorganic**

Teerachote Pakornchote; Natthaphon Choomphon-anomakhun; Sorrjit Arrerut; Chayanon Atthapak; Sakarn Khamkaeo; Thiparat Chotibut; Thiti Bovornratanaraks. *Scientific Reports*. [Paper](https://www.nature.com/articles/s41598-024-51400-4)

**Method:** DP-CDVAE: VAE with diffusion-probabilistic coordinate decoder. Encode latent crystal representation → decode lattice / counts → diffusion-denoise fractional positions

**Inputs:** Latent sample or complete input crystal for reconstruction

**Software:** [DP-CDVAE](software.md#dp-cdvae)

**Groups:** [Chotibut / Bovornratanaraks / Pakornchote collaboration](https://www.nature.com/articles/s41598-024-51400-4)

**Evidence:** Primary abstract and model / reconstruction excerpts. [source 1](https://www.nature.com/articles/s41598-024-51400-4) · [source 2](https://arxiv.org/abs/2308.02165)

**Scope:** Reconstruction has access to an encoded structure; proximity to a relaxed local minimum does not prove the global ground state.

<a id="csp144"></a>
### 2024 — Equivariant Diffusion for Crystal Structure Prediction

**CSP144 · Published conference paper, ICML2024 · Atomic / inorganic**

Peijia Lin; Pin Chen; Rui Jiao; Qing Mo; Jianhuan Cen; Wenbing Huang; Yang Liu; Dan Huang; Yutong Lu. *ICML 2024, PMLR235*. [Paper](https://proceedings.mlr.press/v235/lin24b.html)

**Method:** EquiCSP: lattice-permutation and periodic-translation equivariant diffusion. Formula → joint noising / equivariant denoising of crystal variables → structure candidates

**Inputs:** Atom types and cell atom count

**Software:** [EquiCSP](software.md#equicsp)

**Groups:** [EquiCSP · Lin / Huang / Lu collaboration](https://proceedings.mlr.press/v235/lin24b.html)

**Evidence:** Official PMLR abstract and author list; conference PDF first page. [source 1](https://proceedings.mlr.press/v235/lin24b.html) · [source 2](https://arxiv.org/abs/2512.07289) · [source 3](https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24b/lin24b.pdf)

**Scope:** Official conference2024 predates the December2025 arXiv upload; use proceedings year. Geometric recovery remains finite-sample / distribution-dependent.

<a id="csp145"></a>
### 2024 — FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions

**CSP145 · Published, NeurIPS 2024 · Atomic / inorganic**

Anuroop Sriram; Benjamin Kurt Miller; Ricky T. Q. Chen; Brandon M. Wood. *Published, NeurIPS 2024*. [Paper](https://arxiv.org/abs/2410.23405)

**Method:** Hybrid autoregressive LLM base distribution plus Riemannian flow. LLM → complete approximate crystal representation → graph conversion → flow refines lattice/positions with fixed atom types

**Inputs:** Autoregressive LLM-generated approximate complete crystal

**Software:** [FlowMM / FlowLLM](software.md#flowmm-flowllm)

**Groups:** [FlowMM / FlowLLM collaboration · Sriram–Miller–Wood](https://arxiv.org/abs/2410.23405)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary abstract and NeurIPS paper method/figure excerpts. [source 1](https://arxiv.org/abs/2410.23405) · [source 2](https://arxiv.org/html/2410.23405v1)

**Scope:** LLM proposes a complete approximate structure, rather than formula-only recommendation followed by an independent CSP search. This is LLM initial structure → geometric refinement, not LLM formula-only → CSP; promptability is not proof of arbitrary property control.

<a id="csp146"></a>
### 2024 — FlowMM: Generating Materials with Riemannian Flow Matching

**CSP146 · Published, ICML 2024 · Atomic / inorganic**

Benjamin Kurt Miller; Ricky T. Q. Chen; Anuroop Sriram; Brandon M. Wood. *Published, ICML 2024*. [Paper](https://proceedings.mlr.press/v235/miller24a.html)

**Method:** Riemannian flow matching on periodic crystal variables. Prior distributions → learned flow → composition-conditioned structures or de novo crystals → quantum-chemistry validation

**Inputs:** Atom types/counts for CSP; stochastic base sample

**Software:** [FlowMM / FlowLLM](software.md#flowmm-flowllm)

**Groups:** [FlowMM / FlowLLM collaboration · Sriram–Miller–Wood](https://proceedings.mlr.press/v235/miller24a.html)

**Evidence:** Reused source-qualified inverse-design catalogue: Official ICML proceedings abstract and author/citation metadata. [source 1](https://proceedings.mlr.press/v235/miller24a.html) · [source 2](https://arxiv.org/html/2406.04713) · [source 3](https://github.com/facebookresearch/flowmm)

**Scope:** Flow generation and benchmark recovery do not certify lowest Gibbs free energy. Conditional flow matching training terminology does not itself mean functional-property-conditioned inverse design.

<a id="csp149"></a>
### 2024 — Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation

**CSP149 · Published conference paper, NeurIPS2024 · Atomic / inorganic**

Keqiang Yan; Xiner Li; Hongyi Ling; Kenna Ashen; Carl Edwards; Raymundo Arróyave; Marinka Zitnik; Heng Ji; Xiaofeng Qian; Xiaoning Qian; Shuiwang Ji. *Advances in Neural Information Processing Systems 37*. [Paper](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html)

**Method:** Mat2Seq: canonical invariant sequence representation plus autoregressive LM. Canonical primitive lattice / atomic sequence → language model next-token sampling → crystal reconstruction

**Inputs:** Formula / token prefix or generation conditions

**Software:** [Mat2Seq (AIRS)](software.md#mat2seq-airs)

**Groups:** [Shuiwang Ji / DIG collaboration](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html)

**Evidence:** Official NeurIPS metadata / abstract and author-hosted PDF. [source 1](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html) · [source 2](https://arxiv.org/abs/2503.00152) · [source 3](https://blender.cs.illinois.edu/paper/mat2024.pdf) · [source 4](https://arxiv.org/html/2503.00152)

**Scope:** Use official NeurIPS2024 year despite February2025 arXiv upload. Canonical representation invariance does not imply physical validity or unbiased sampling.

<a id="csp151"></a>
### 2024 — Organic crystal structure prediction via coupled generative adversarial networks and graph convolutional networks

**CSP151 · Journal article · Molecular / organic**

Zhuyifan Ye; Nannan Wang; Jiantao Zhou; Defang Ouyang. *The Innovation*. [Paper](https://doi.org/10.1016/j.xinn.2023.100562)

**Method:** DeepCSP conditional GAN proposals and graph scoring. Condition GAN-generated trial structures on molecular features; use graph-based learned scoring to select plausible structures.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [DeepCSP (organic conditional GAN + GCN)](software.md#deepcsp-organic-gan)

**Groups:** [Ouyang–Ye / DeepCSP collaboration](https://www.the-innovation.org/data/article/innovation/preview/pdf/S2666-6758%2823%2900190-X.pdf)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1016/j.xinn.2023.100562) · [source 2](https://www.the-innovation.org/data/article/innovation/preview/pdf/S2666-6758%2823%2900190-X.pdf)

**Scope:** Dataset-derived plausibility/recovery does not establish quantum-accurate energy ordering or all polymorphs.

<a id="csp152"></a>
### 2024 — Scalable Diffusion for Materials Generation

**CSP152 · Published, ICLR 2024; preprint 2023 · Atomic / inorganic**

Sherry Yang; KwangHwan Cho; Amil Merchant; Pieter Abbeel; Dale Schuurmans; Igor Mordatch; Ekin Dogus Cubuk. *Published, ICLR 2024; preprint 2023*. [Paper](https://arxiv.org/abs/2311.09235)

**Method:** UniMat tensor representation plus diffusion. Encode crystals into unified tensor → train/sample diffusion, optionally composition-conditioned → DFT energy/hull assessment

**Inputs:** Formula / atom specification or unconditional latent noise

**Software:** [UniMat](software.md#unimat)

**Groups:** [Ekin D. Cubuk + collaborators](https://arxiv.org/abs/2311.09235)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary arXiv abstract; ICLR publication record. [source 1](https://arxiv.org/abs/2311.09235) · [source 2](https://arxiv.org/html/2311.09235v2)

**Scope:** Denoising a learned distribution needs independent relaxation and stability checks. Conditional composition generation addresses CSP; paper explicitly highlights mismatch between reconstruction metrics and stable discovery.

<a id="csp154"></a>
### 2024 — Space Group Constrained Crystal Generation

**CSP154 · Published, ICLR 2024 · Atomic / inorganic**

Rui Jiao; Wenbing Huang; Yu Liu; Deli Zhao; Yang Liu. *Published, ICLR 2024*. [Paper](https://arxiv.org/abs/2402.03992)

**Method:** DiffCSP++, symmetry-constrained joint diffusion. Composition/template symmetry + target space group → constrained denoising → crystal

**Inputs:** Composition and space-group / Wyckoff constraints

**Structural knowledge:** Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [DiffCSP++](software.md#diffcsp-plus-plus)

**Groups:** [Rui Jiao / Wenbing Huang](https://arxiv.org/abs/2402.03992)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary arXiv abstract and ICLR proceedings entry. [source 1](https://arxiv.org/abs/2402.03992) · [source 2](https://arxiv.org/html/2402.03992v1)

**Scope:** Symmetry constraint improves controlled generation but can exclude a correct unknown polymorph. Space-group control is a structural constraint; do not equate it with demonstrated arbitrary property targeting.

<a id="csp157"></a>
### 2024 — Vector Field Oriented Diffusion Model for Crystal Material Generation

**CSP157 · Published conference paper, AAAI2024 · Atomic / inorganic**

Astrid Klipfel; Yaël Fregier; Adlane Sayede; Zied Bouraoui. *Proceedings of the AAAI Conference on Artificial Intelligence*. [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/30224)

**Method:** GemsDiff: equivariant vector-field diffusion of lattice and positions. Composition / chemical system → joint geometrical diffusion → crystal candidates

**Inputs:** Formula or chemical-system constraints

**Software:** [GemsDiff](software.md#gemsdiff)

**Groups:** [Klipfel / Fregier / Sayede / Bouraoui collaboration](https://ojs.aaai.org/index.php/AAAI/article/view/30224)

**Evidence:** Official AAAI abstract / authors and author repository composition-conditioning / version note. [source 1](https://ojs.aaai.org/index.php/AAAI/article/view/30224) · [source 2](https://github.com/aklipf/gemsdiff) · [source 3](https://arxiv.org/abs/2401.05402) · [source 4](https://github.com/aklipf/gemsdiff/blob/5781f80eb072d313b3b3f1ac4bca34cb5feef1d7/sampling.py)

**Scope:** Official repository subsequently changes the released model to omit lattice diffusion; paper and latest code should be distinguished. Distribution metrics do not certify phase stability.

<a id="csp160"></a>
### 2025 — A Periodic Bayesian Flow for Material Generation

**CSP160 · Published, ICLR 2025 · Atomic / inorganic**

Hanlin Wu; Yuxuan Song; Jingjing Gong; Ziyao Cao; Yawen Ouyang; Jianbing Zhang; Hao Zhou; Wei-Ying Ma; Jingjing Liu. *Published, ICLR 2025*. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html)

**Method:** CrysBFN, periodic Bayesian Flow Network with entropy conditioning. Noisy observations → Bayesian updates in distribution-parameter space → periodic crystal structures

**Inputs:** Atom specification for CSP or stochastic distribution parameters

**Software:** [CrysBFN](software.md#crysbfn)

**Groups:** [CrysBFN collaboration · Hao Zhou / Jingjing Liu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html)

**Evidence:** Reused source-qualified inverse-design catalogue: Official ICLR 2025 abstract/author metadata and primary arXiv abstract. [source 1](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html) · [source 2](https://arxiv.org/abs/2502.02016) · [source 3](https://arxiv.org/html/2502.02016v1)

**Scope:** Bayesian flow networks differ from Bayesian optimization and from ODE flow matching. Bayesian Flow Network is a distinct generative family from ODE normalizing flow/flow matching; benchmark generation or CSP alone is not functional-property design.

<a id="csp159"></a>
### 2025 — A generative model for inorganic materials design

**CSP159 · Published, Nature 639, 624–632 · Atomic / inorganic**

Claudio Zeni; Robert Pinsler; Daniel Zügner; Andrew Fowler; Matthew Horton; Xiang Fu; Zilong Wang; Aliaksandra Shysheya; Jonathan Crabbé; Shoko Ueda; Roberto Sordillo; Lixin Sun; Jake Smith; Bichlien Nguyen; Hannes Schulz; Sarah Lewis; Chin-Wei Huang; Ziheng Lu; Yichi Zhou; Han Yang; Hongxia Hao; Jielan Li; Chunlei Yang; Wenjie Li; Ryota Tomioka; Tian Xie. *Nature*. [Paper](https://www.nature.com/articles/s41586-025-08628-5)

**Method:** MatterGen, joint atom/lattice/coordinate diffusion with property adapters. Unconditional pretraining → fine-tune adapters on target labels → conditional sampling → relaxation/validation

**Inputs:** Noise plus optional chemical-system / property conditions

**Software:** [MatterGen](software.md#mattergen)

**Groups:** [Tian Xie + collaborators](https://www.nature.com/articles/s41586-025-08628-5)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher abstract, fine-tuning description, author list, data/experimental record descriptions. [source 1](https://www.nature.com/articles/s41586-025-08628-5) · [source 2](https://arxiv.org/abs/2312.03687) · [source 3](https://github.com/microsoft/mattergen#crystal-structure-prediction)

**Scope:** Primarily de novo materials generation; property conditioning is not identical to exhaustive CSP for a prescribed exact formula. Experimental proof of concept is specific to demonstrated synthesized material; generated library is not generally experimentally validated.

<a id="csp163"></a>
### 2025 — All-atom Diffusion Transformers: Unified generative modelling of molecules and materials

**CSP163 · Published, ICML 2025, PMLR 267, 28393–28417 · Atomic / inorganic**

Chaitanya K. Joshi; Xiang Fu; Yi-Lun Liao; Vahe Gharakhanyan; Benjamin Kurt Miller; Anuroop Sriram; Zachary Ward Ulissi. *Published, ICML 2025, PMLR 267, 28393–28417*. [Paper](https://proceedings.mlr.press/v267/joshi25a.html)

**Method:** ADiT, transformer autoencoder plus latent diffusion. Unified periodic/nonperiodic all-atom representation → shared autoencoder latent → generative latent dynamics → decode crystals or molecules

**Inputs:** Shared all-atom latent-space sample

**Software:** [All-atom Diffusion Transformer (ADiT)](software.md#all-atom-diffusion-transformer-adit)

**Groups:** [Sriram / Miller collaboration](https://proceedings.mlr.press/v267/joshi25a.html)

**Evidence:** Reused source-qualified inverse-design catalogue: Official ICML proceedings abstract/citation; primary arXiv abstract. [source 1](https://proceedings.mlr.press/v267/joshi25a.html) · [source 2](https://arxiv.org/abs/2503.03965) · [source 3](https://arxiv.org/html/2503.03965v1)

**Scope:** Unified generation architecture; formula-only ground-state CSP requires a specifically evaluated conditional protocol. The primary abstract describes latent diffusion; do not classify as a plain direct-coordinate diffusion or assert functional-property control absent supporting experiments.

<a id="csp166"></a>
### 2025 — ContinuouSP: Generative Model for Crystal Structure Prediction with Invariance and Continuity

**CSP166 · Accepted AAAI AI2ASE2025 workshop; arXiv preprint · Atomic / inorganic**

Yuji Tone; Masatoshi Hanai; Mitsuaki Kawamura; Kenjiro Taura; Toyotaro Suzumura. *AAAI AI2ASE workshop / arXiv*. [Paper](https://arxiv.org/abs/2502.02026)

**Method:** ContinuouSP: symmetry- and continuity-aware energy-based generative model. Train invariant / continuous crystal energy-based model → sample composition-conditioned structures

**Inputs:** Composition and trained energy-based model

**Software:** [ContinuouSP](software.md#continuousp)

**Groups:** [Tone / Hanai / Kawamura / Suzumura collaboration](https://arxiv.org/abs/2502.02026)

**Evidence:** Primary arXiv abstract, workshop acceptance comment and author list. [source 1](https://arxiv.org/abs/2502.02026) · [source 2](https://arxiv.org/html/2502.02026v1)

**Scope:** Preliminary workshop evidence; mathematical invariance / continuity does not certify physical energy accuracy or complete polymorph sampling.

<a id="csp169"></a>
### 2025 — CrystalFlow: a flow-based generative model for crystalline materials

**CSP169 · Published, Nature Communications 16, 9267 · Atomic / inorganic**

Xiaoshan Luo; Zhenyu Wang; Qingchang Wang; Xuechen Shao; Jian Lv; Lei Wang; Yanchao Wang; Yanming Ma. *Nature Communications*. [Paper](https://www.nature.com/articles/s41467-025-64364-4)

**Method:** Equivariant continuous normalizing flow trained with conditional flow matching. Composition/pressure or other conditions + noise → flow on lattice/coordinates/types → relaxation

**Inputs:** Formula / atom types, noise and optional pressure or properties

**Software:** [CrystalFlow](software.md#crystalflow)

**Groups:** [Yanming Ma–Yanchao Wang / CALYPSO collaboration](https://www.nature.com/articles/s41467-025-64364-4)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher abstract and Results/model/DFT methodology sections. [source 1](https://www.nature.com/articles/s41467-025-64364-4) · [source 2](https://arxiv.org/abs/2412.11693)

**Scope:** Reported recovery and throughput depend on data split, sample count and solver steps. Sample efficiency/integration steps differs from total DFT discovery cost; local relaxation and hull assessment are separate.

<a id="crystalformercsp2025"></a>
### 2025 — CrystalFormer-CSP: Thinking Fast and Slow for Crystal Structure Prediction

**CrystalFormerCSP2025 · Preprint · Atomic / inorganic**

Zhendong Cao; Shigang Ou; Lei Wang. **. [Paper](https://arxiv.org/abs/2512.18251)

**Method:** CrystalFormer-CSP. Composition-given autoregressive prediction using space-group and Wyckoff representations.

**Inputs:** Composition; additional inference controls depend on version

**Structural knowledge:** Prototypes / substitution, Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [CrystalFormer](software.md#crystalformer)

**Groups:** [CrystalFormer collaboration](https://arxiv.org/abs/2512.18251)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://arxiv.org/abs/2512.18251)

**Scope:** Version-specific composition and cell-count controls; not runtime tested.

<a id="csp172"></a>
### 2025 — Kinetic Langevin Diffusion for Crystalline Materials Generation

**CSP172 · Published conference paper, ICML2025 · Atomic / inorganic**

François R J Cornet; Federico Bergamin; Arghya Bhowmik; Juan Maria Garcia-Lastra; Jes Frellsen; Mikkel N. Schmidt. *ICML2025, PMLR267*. [Paper](https://proceedings.mlr.press/v267/cornet25a.html)

**Method:** KLDM: auxiliary-velocity kinetic diffusion on periodic coordinates. Couple torus coordinates to Euclidean velocities → learn reverse diffusion → crystal candidates

**Inputs:** Composition for CSP; noise / species generation for de novo task

**Software:** [KLDM](software.md#kldm)

**Groups:** [Cornet / Frellsen / Schmidt collaboration](https://proceedings.mlr.press/v267/cornet25a.html)

**Evidence:** Official PMLR abstract and author metadata. [source 1](https://proceedings.mlr.press/v267/cornet25a.html) · [source 2](https://arxiv.org/abs/2507.03602) · [source 3](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cornet25a/cornet25a.pdf)

**Scope:** The chosen diffusion parameterization and sample budget affect recovery; published benchmark recovery is not a ground-state proof.

<a id="csp174"></a>
### 2025 — OXtal: An All-Atom Diffusion Model for Organic Crystal Structure Prediction

**CSP174 · Preprint · Molecular / organic**

Emily Jin; Andrei Cristian Nica; Mikhail Galkin; Jarrid Rector-Brooks; Kin Long Kelvin Lee; Santiago Miret; Frances H. Arnold; Michael Bronstein; Avishek Joey Bose; Alexander Tong; Cheng-Hao Liu. *arXiv*. [Paper](https://arxiv.org/abs/2512.06987)

**Method:** All-atom conditional diffusion. Generate molecular conformations and periodic packing jointly from chemical graphs with stochastic lattice-free shell representations.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [OXtal](software.md#oxtal)

**Groups:** [Jin–Nica / Bronstein–Tong–Liu OXtal collaboration](https://arxiv.org/abs/2512.06987)

**Evidence:** Primary arXiv abstract/version history. [source 1](https://arxiv.org/abs/2512.06987)

**Scope:** Preprint first posted December 2025, revised April 2026; dataset recovery/packing similarity does not prove free-energy ranking.

<a id="csp173"></a>
### 2025 — Open Materials Generation with Stochastic Interpolants

**CSP173 · Published, ICML 2025, PMLR 267, 23417–23450 · Atomic / inorganic**

Philipp Höllmer; Thomas Egg; Maya Martirossyan; Eric Fuemmeler; Zeren Shui; Amit Gupta; Pawan Prakash; Adrian Roitberg; Mingjie Liu; George Karypis; Mark Transtrum; Richard Hennig; Ellad B. Tadmor; Stefano Martiniani. *Published, ICML 2025, PMLR 267, 23417–23450*. [Paper](https://proceedings.mlr.press/v267/hollmer25a.html)

**Method:** OMatG, stochastic interpolants with periodic equivariant geometry and discrete species flow matching. Arbitrary base distributions → tunable stochastic/ODE interpolants for coordinates/lattice + discrete species updates → crystals

**Inputs:** Formula / atom count for CSP or stochastic base distribution

**Software:** [OMatG](software.md#omatg)

**Groups:** [Stefano Martiniani](https://proceedings.mlr.press/v267/hollmer25a.html) · [Richard Hennig / GASP and learned CSP](https://proceedings.mlr.press/v267/hollmer25a.html)

**Evidence:** Reused source-qualified inverse-design catalogue: Official ICML proceedings abstract/citation; author repository theoretical background and configuration excerpts. [source 1](https://proceedings.mlr.press/v267/hollmer25a.html) · [source 2](https://arxiv.org/abs/2502.02582) · [source 3](https://github.com/FERMat-ML/OMatG) · [source 4](https://arxiv.org/html/2502.02582v2)

**Scope:** Benchmark CSP and de novo stability results are different tasks; independent DFT checks remain necessary. Stochastic interpolants unify diffusion and flow matching as special cases; original model's CSP/DNG benchmarks should be distinguished from later reward-guided extensions.

<a id="csp177"></a>
### 2025 — Space group informed transformer for crystalline materials generation

**CSP177 · Published online 24 September 2025; Science Bulletin 70, 3522–3533 · Atomic / inorganic**

Zhendong Cao; Xiaoshan Luo; Jian Lv; Lei Wang. *Science Bulletin*. [Paper](https://doi.org/10.1016/j.scib.2025.09.035)

**Method:** CrystalFormer, autoregressive species/Wyckoff-coordinate transformer. Space group → inequivalent sites/species → symmetry expansion; property predictor can guide plug-and-play sampling

**Inputs:** Space group and autoregressive crystal-token prefix

**Structural knowledge:** Prototypes / substitution, Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [CrystalFormer](software.md#crystalformer)

**Groups:** [CrystalFormer collaboration · Zhendong Cao / Lei Wang](https://doi.org/10.1016/j.scib.2025.09.035)

**Evidence:** Reused source-qualified inverse-design catalogue: Publisher abstract/citation and author-hosted article Introduction; primary arXiv abstract. [source 1](https://doi.org/10.1016/j.scib.2025.09.035) · [source 2](https://arxiv.org/abs/2403.15734) · [source 3](https://arxiv.org/html/2403.15734) · [source 4](https://github.com/deepmodeling/CrystalFormer/blob/31bb734a3fd006af49a021921839061e6184cbf1/crystalformer/src/sample.py) · [source 5](https://github.com/deepmodeling/CrystalFormer/blob/31bb734a3fd006af49a021921839061e6184cbf1/scripts/awl2struct.py) · [source 6](https://github.com/deepmodeling/CrystalFormer/blob/31bb734a3fd006af49a021921839061e6184cbf1/README.md)

**Scope:** Wyckoff / symmetry priors restrict support; benchmark generation quality is not completeness. Disambiguate from property-prediction encoders also named Crystalformer; preprint 2024 but journal article 2025.

<a id="csp178"></a>
### 2025 — SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models

**CSP178 · Published, ICLR 2025 · Atomic / inorganic**

Daniel Levy; Siba Smarak Panigrahi; Sékou-Oumar Kaba; Qiang Zhu; Kin Long Kelvin Lee; Mikhail Galkin; Santiago Miret; Siamak Ravanbakhsh. *Published, ICLR 2025*. [Paper](https://arxiv.org/abs/2502.03638)

**Method:** Diffusion on asymmetric units and site symmetry transformations. Sample asymmetric unit + transformations → symmetry-expand full crystal → assess

**Inputs:** Asymmetric unit and site-symmetry generative variables

**Structural knowledge:** Symmetry-preserving exploration, Wyckoff / site assignments — [Mechanisms and limits](structural-priors.md)

**Software:** [SymmCD](software.md#symmcd)

**Groups:** [Qiang Zhu / crystal search and generation](https://arxiv.org/abs/2502.03638)

**Evidence:** Reused source-qualified inverse-design catalogue: Primary abstract and ICLR proceedings first-page/method positioning excerpts. [source 1](https://arxiv.org/abs/2502.03638) · [source 2](https://arxiv.org/html/2502.03638)

**Scope:** Generating plausible site symmetry is not proof of energy ranking or ground-state recovery. Realistic symmetry is a representation/generation advance, not automatically functional-property inverse design.

<a id="csp179"></a>
### 2025 — Uni-3DAR: Unified 3D Generation and Understanding via Autoregression on Compressed Spatial Tokens

**CSP179 · Preprint · Atomic / inorganic**

Shuqi Lu; Haowei Lin; Lin Yao; Zhifeng Gao; Xiaohong Ji; Weinan E; Linfeng Zhang; Guolin Ke. *arXiv*. [Paper](https://arxiv.org/abs/2503.16278v1)

**Method:** Uni-3DAR: octree-compressed spatial-token autoregression. Compress spatial hierarchy → autoregressive lattice vertices and atomic token generation → optional formula or PXRD constraints

**Inputs:** Formula / atom counts for CSP; PXRD optional in a separate task

**Software:** [Uni-3DAR](software.md#uni-3dar)

**Groups:** [Uni-3DAR · Gao / Zhang / Ke collaboration](https://arxiv.org/abs/2503.16278v1)

**Evidence:** Primary arXiv abstract / authors and author repository CSP / PXRD task instructions. [source 1](https://arxiv.org/abs/2503.16278v1) · [source 2](https://github.com/dptech-corp/Uni-3DAR) · [source 3](https://arxiv.org/html/2503.16278v1) · [source 4](https://github.com/dptech-corp/Uni-3DAR/blob/main/uni3dar/inference.py) · [source 5](https://github.com/dptech-corp/Uni-3DAR/blob/main/uni3dar/models/uni3dar_sampler.py)

**Scope:** CSP, de novo generation and diffraction-conditioned structure solution are different tasks. Later versions retitle the work; record follows initial arXiv version.

<a id="csp182"></a>
### 2026 — CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction

**CSP182 · Preprint · Atomic / inorganic**

Kaixiang Su; Hongfei Xue; Qiang Zhu. *arXiv*. [Paper](https://arxiv.org/abs/2608.06582)

**Method:** Recovery-aware reinforcement post-training of flow generators. Pretrained coordinate–lattice flow → stochastic policy → energy / recovery rewards → quality or coverage-aware policy updates

**Inputs:** Composition, pretrained generator and post-training reference targets

**Software:** [CrystalGRPO](software.md#crystalgrpo)

**Groups:** [Qiang Zhu / crystal search and generation](https://arxiv.org/abs/2608.06582)

**Evidence:** Primary arXiv abstract and author list. [source 1](https://arxiv.org/abs/2608.06582) · [source 2](https://arxiv.org/html/2608.06582v1)

**Scope:** Preprint benchmark evidence; recovery reward requires reference structures during post-training. Optimizing top-one recovery can reduce finite-budget coverage.

<a id="csp183"></a>
### 2026 — CrystalGRW: generative modeling of crystal structures with targeted crystallographic properties via geodesic random walks

**CSP183 · Published journal article · Atomic / inorganic**

Krit Tangsongcharoen; Teerachote Pakornchote; Chayanon Atthapak; Natthaphon Choomphon-anomakhun; Annop Ektarawong; Björn Alling; Christopher Sutton; Thiti Bovornratanaraks; Thiparat Chotibut. *Scientific Reports*. [Paper](https://www.nature.com/articles/s41598-026-62470-x)

**Method:** CrystalGRW: Riemannian score-based diffusion via geodesic random walks. Manifold-noise sample → equivariant score dynamics → coordinates / types / lattice → optional point-group guidance

**Inputs:** Noise plus optional crystallographic point group

**Software:** [CrystalGRW](software.md#crystalgrw)

**Groups:** [Chotibut / Bovornratanaraks / Pakornchote collaboration](https://www.nature.com/articles/s41598-026-62470-x)

**Evidence:** Publisher abstract and manifold / conditioning-method excerpts. [source 1](https://www.nature.com/articles/s41598-026-62470-x) · [source 2](https://arxiv.org/abs/2501.08998) · [source 3](https://github.com/trachote/crystalgrw/blob/main/src/crystalgrw/cli/evaluate.py) · [source 4](https://github.com/trachote/crystalgrw/blob/main/src/crystalgrw/samplers/sample.py)

**Scope:** Primarily de novo composition-plus-structure generation; point-group conditioning is not exact formula-only CSP. Local relaxation and hull thresholds are separate evidence.

<a id="csp184"></a>
### 2026 — Crystalite: A Lightweight Transformer for Efficient Crystal Modeling

**CSP184 · Preprint · Atomic / inorganic**

Tin Hadži Veljković; Joshua Rosenthal; Ivor Lončarić; Jan-Willem van de Meent. *arXiv*. [Paper](https://arxiv.org/abs/2604.02270)

**Method:** Crystalite: lightweight diffusion Transformer with subatomic tokens and geometric attention. Composition-conditioned noisy crystal variables → Transformer denoising with minimum-image geometry bias → candidates

**Inputs:** Composition for CSP; noise for de novo generation

**Software:** [Crystalite](software.md#crystalite)

**Groups:** [Crystalite · Veljković / Lončarić / van de Meent collaboration](https://arxiv.org/abs/2604.02270)

**Evidence:** Primary arXiv abstract / authors and author project explanation. [source 1](https://arxiv.org/abs/2604.02270) · [source 2](https://stases.github.io/blogposts/crystalite/) · [source 3](https://arxiv.org/html/2604.02270)

**Scope:** Preprint results depend on compared baselines / sample budget. Lightweight architecture and S.U.N. discovery performance do not establish unseen-prototype CSP.

<a id="csp187"></a>
### 2026 — Efficient symmetry-aware materials generation via hierarchical generative flow networks

**CSP187 · Published journal paper; DOI/title checked · Atomic / inorganic**

Tri Minh Nguyen; Sherif Abdulkader Tawfik; Truyen Tran; Sunil Gupta; Santu Rana; Svetha Venkatesh. *Digital Discovery*. [Paper](https://arxiv.org/abs/2411.04323)

**Method:** SHAFT hierarchical GFlowNet. Space-group hierarchy → lattice → symmetry-consistent atom placements → reward-based generation

**Inputs:** Space-group hierarchy and reward functions

**Software:** [SHAFT](software.md#shaft)

**Groups:** [SHAFT · Truyen Tran / Svetha Venkatesh, Deakin](https://arxiv.org/abs/2411.04323)

**Evidence:** Reused source-qualified inverse-design catalogue: Author arXiv abstract and publisher article/PDF excerpts. [source 1](https://arxiv.org/abs/2411.04323) · [source 2](https://arxiv.org/html/2411.04323v1)

**Scope:** Full-structure GFlowNet generation; reward-guided sampling is not a guarantee of global energy optimality. 2024 preprint; journal volume 5 (2026), pp. 686–697. Avoid confusing GFlowNet flow consistency with diffusion/continuous flow matching.

<a id="csp188"></a>
### 2026 — Molecular Crystal Structure Prediction from Conditional Flow on the Unit Cells

**CSP188 · Preprint · Molecular / organic**

Qiang Zhu; Yihan Weng. *arXiv*. [Paper](https://arxiv.org/abs/2610.04193)

**Method:** Conditional flow lattice proposals plus quasi-random packing. Learn lattice-invariant distributions conditioned on molecular graph, Hall setting and Z-prime; reconstruct cells and sample molecular packing.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CellNet (conditional unit-cell flow + packing)](software.md#cellnet-prototype)

**Groups:** [Qiang Zhu / crystal search and generation](https://arxiv.org/abs/2610.04193)

**Evidence:** Primary arXiv abstract. [source 1](https://arxiv.org/abs/2610.04193)

**Scope:** Preprint; tested with supplied Hall symmetry and Z-prime at most 1, so symmetry-blind molecular CSP is not demonstrated.

<a id="csp189"></a>
### 2026 — NextCrystal: a Symmetry-Driven Generative Framework for Crystal Structure Prediction

**CSP189 · Preprint; v1 February 2026, v4 July 2026; title changed across versions · Atomic / inorganic**

Jinming Mu; Lixin He; Xudong Zhu; Shi Yin. *arXiv:2602.17176v4*. [Paper](https://arxiv.org/abs/2602.17176v4)

**Method:** Language models propose space-group and Wyckoff patterns; constrained assignment steers a diffusion backbone.. Composition → learned symmetry pattern → multiplicity-consistent assignment → constrained diffusion → validation

**Inputs:** Composition and learned symmetry/diffusion models

**Software:** [NextCrystal](software.md#nextcrystal)

**Groups:** [Mu–He–Zhu–Yin / NextCrystal collaboration](https://arxiv.org/html/2602.17176v4)

**Evidence:** arXiv v4 abstract, author/affiliation block and selected introduction; version history checked. [source 1](https://arxiv.org/abs/2602.17176v4) · [source 2](https://arxiv.org/html/2602.17176v4)

**Scope:** Preprint; structural recovery and SUN claims do not imply a guaranteed ground state. v1 had a different title. The manuscript carries a placeholder journal DOI, which is not treated as a real DOI.

<a id="csp191"></a>
### 2026 — PackFlow: Generative Molecular Crystal Structure Prediction via Reinforcement Learning Alignment

**CSP191 · Preprint · Molecular / organic**

Akshay Subramanian; Elton Pan; Juno Nam; Maurice Weiler; Shuhui Qu; Cheol Woo Park; Tommi S. Jaakkola; Elsa Olivetti; Rafael Gomez-Bombarelli. *arXiv*. [Paper](https://arxiv.org/abs/2602.20140)

**Method:** Flow-matching crystal proposals with reinforcement-learning physics alignment. Generate heavy-atom positions and unit-cell parameters conditioned on a molecular graph; post-train by reinforcement learning using MLIP energies and forces; relax and rank candidate packings.

**Inputs:** Molecular chemical graph; heavy-atom crystal representation

**Software:** [PackFlow](software.md#packflow-molecular)

**Groups:** [Gómez-Bombarelli–Jaakkola–Olivetti / PackFlow collaboration](https://arxiv.org/abs/2602.20140)

**Evidence:** Primary arXiv abstract, author list and submission history. [source 1](https://arxiv.org/abs/2602.20140)

**Scope:** Preprint; MLIP energy/force rewards are stability proxies. Unseen-system proposal recovery and two blind-test case studies do not certify exhaustive polymorph sampling or accurate free-energy ranking.

<a id="csp192"></a>
### 2026 — Riemannian Flow Models with Reinforcement Learning for Molecular Crystal Structure Prediction

**CSP192 · Preprint · Molecular / organic**

Thomas Egg; Harry Winston Sullivan; Maya M. Martirossyan; Philipp Höllmer; Cheng Zeng; Adrian Roitberg; Mingjie Liu; Richard Hennig; Sapna Sarupria; Ellad B. Tadmor; Stefano Martiniani. *arXiv*. [Paper](https://arxiv.org/abs/2609.39773)

**Method:** CG-OMatG coarse-grained equivariant Riemannian flow with policy-gradient fine-tuning. Treat molecules as rigid bodies; generate centroids, orientations and lattice parameters conditioned on species/conformer geometry; apply policy-gradient reinforcement learning toward low-energy candidates and evaluate packing similarity.

**Inputs:** Chemical species and supplied conformer geometry; rigid-body molecular representation

**Software:** [CG-OMatG](software.md#cg-omatg)

**Groups:** [Martiniani–Tadmor–Sarupria–Hennig / CG-OMatG collaboration](https://arxiv.org/abs/2609.39773)

**Evidence:** Primary arXiv abstract, author list and submission history. [source 1](https://arxiv.org/abs/2609.39773)

**Scope:** Preprint posted September 30, 2026; conformer geometry is an input rather than freely predicted internal flexibility. COMPACK recovery does not certify thermodynamic ranking. arXiv DOI was marked pending registration at retrieval.

<a id="csp193"></a>
### 2026 — Siamese foundation models for crystal structure prediction

**CSP193 · Published journal article · Atomic / inorganic**

Liming Wu; Wenbing Huang; Rui Jiao; Jianxing Huang; Liwei Liu; Yipeng Zhou; Hao Sun; Yang Liu; Fuchun Sun; Yuxiang Ren; Ji-Rong Wen. *Nature Communications*. [Paper](https://www.nature.com/articles/s41467-026-72362-3)

**Method:** DAO-G / DAO-P: composition-conditioned generator and paired energy model. Stable / unstable crystal pretraining → learned relaxation of unstable training data → generator finetuning → energy-guided denoising

**Inputs:** Composition and pretrained generator / energy model

**Software:** [DAO](software.md#dao)

**Groups:** [DAO · Huang / Jiao / Wen collaboration](https://www.nature.com/articles/s41467-026-72362-3)

**Evidence:** Publisher abstract, training/inference workflow, dataset deduplication and author-list excerpts. [source 1](https://www.nature.com/articles/s41467-026-72362-3)

**Scope:** Source deduplicates matching compositions/structures, but this does not establish held-out prototype-family extrapolation; recovery and energy guidance are separate evidence.

<a id="csp195"></a>
### 2026 — uFlowCSP: Crystal Structure Prediction using Mean flow generative models

**CSP195 · Preprint · Atomic / inorganic**

Sourin Dey; Dipannoy Das Gupta; Lai Wei; Sadman Sadeed Omee; Jianjun Hu. *arXiv*. [Paper](https://arxiv.org/abs/2609.09799)

**Method:** MeanFlow average-velocity generative CSP. Formula → chemistry-aware Transformer predicts mean probability-flow velocity → one-to-five-step structure generation

**Inputs:** Composition / atom types; crystal-system auxiliary token only during training

**Software:** [uFlowCSP](software.md#uflowcsp)

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://arxiv.org/abs/2609.09799)

**Evidence:** Primary arXiv abstract and author list. [source 1](https://arxiv.org/abs/2609.09799) · [source 2](https://arxiv.org/html/2609.09799)

**Scope:** Preprint claims need independent reproduction; compare equal candidate / network-evaluation budgets and distinguish training-only auxiliary symmetry from inference input.

## Context, evaluators and evaluation

<a id="csp002"></a>
### 1996 — First Step Towards Planning of Syntheses in Solid‐State Chemistry: Determination of Promising Structure Candidates by Global Optimization

**CSP002 · Published journal article · Atomic / inorganic**

J. Christian Schön; Martin Jansen. *Angewandte Chemie International Edition in English*. [Paper](https://doi.org/10.1002/anie.199612861)

**Method:** Explore energy landscapes for low-energy solid candidates with global optimization.. Explore energy landscapes for low-energy solid candidates with global optimization.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Groups:** [Schön–Jansen landscape team](https://doi.org/10.1002/anie.199612861)

**Evidence:** Bibliographic metadata; abstract summary; publisher page inaccessible. [source 1](https://doi.org/10.1002/anie.199612861)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp003"></a>
### 1996 — Role of Electrostatic Interactions in Determining the Crystal Structures of Polar Organic Molecules. A Distributed Multipole Study

**CSP003 · Journal article · Molecular / organic**

David S. Coombes; Sarah L. Price; David J. Willock; Maurice Leslie. *The Journal of Physical Chemistry*. [Paper](https://doi.org/10.1021/jp960333b)

**Method:** Distributed-multipole electrostatic energy model. Compare realistic anisotropic electrostatics with simpler atom-based models for molecular-crystal energy minimization.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Price / molecular-crystal modelling collaboration](https://pubs.acs.org/doi/10.1021/jp960333b)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/jp960333b) · [source 2](https://pubs.acs.org/doi/10.1021/jp960333b)

**Scope:** Enabling intermolecular model; improved energy modeling alone is not a complete global search.

<a id="csp009"></a>
### 2000 — A test of crystal structure prediction of small organic molecules

**CSP009 · Journal article · Molecular / organic**

Jos P. M. Lommerse; W. D. Sam Motherwell; Herman L. Ammon; Jack D. Dunitz; Angelo Gavezzotti; Detlef W. M. Hofmann; Frank J. J. Leusen; Wijnand T. M. Mooij; Sarah L. Price; Bernd Schweizer; Martin U. Schmidt; Bouke P. van Eijck; Paul Verwer; Donald E. Williams. *Acta Crystallographica Section B Structural Science*. [Paper](https://doi.org/10.1107/S0108768100004584)

**Method:** CCDC blind-test cycle 1. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/paper?cnor=bk0070)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S0108768100004584) · [source 2](https://journals.iucr.org/paper?cnor=bk0070)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp012"></a>
### 2002 — A Concept for Synthesis Planning in Solid-State Chemistry

**CSP012 · Published journal article · Atomic / inorganic**

Martin Jansen. *Angewandte Chemie International Edition*. [Paper](https://doi.org/10.1002/1521-3773(20021018)41:20<3746::AID-ANIE3746>3.0.CO;2-2)

**Method:** Connect low-energy structure prediction and landscape accessibility to rational solid-state synthesis targets.. Connect low-energy structure prediction and landscape accessibility to rational solid-state synthesis targets.

**Inputs:** Chemical system and energy-landscape model

**Groups:** [Schön–Jansen landscape team](https://doi.org/10.1002/1521-3773(20021018)41:20%3C3746::AID-ANIE3746%3E3.0.CO;2-2)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1002/1521-3773(20021018)41:20<3746::AID-ANIE3746>3.0.CO;2-2) · [source 2](https://doi.org/10.1002/1521-3773(20021018)41:20%3C3746::AID-ANIE3746%3E3.0.CO;2-2)

**Scope:** Conceptual synthesis-planning framework; low energy alone does not guarantee realizability.

<a id="csp014"></a>
### 2002 — Crystal structure prediction of small organic molecules: a second blind test

**CSP014 · Journal article · Molecular / organic**

W. D. Sam Motherwell; Herman L. Ammon; Jack D. Dunitz; Alexander Dzyabchenko; Peter Erk; Angelo Gavezzotti; Detlef W. M. Hofmann; Frank J. J. Leusen; Jos P. M. Lommerse; Wijnand T. M. Mooij; Sarah L. Price; Harold Scheraga; Bernd Schweizer; Martin U. Schmidt; Bouke P. van Eijck; Paul Verwer; Donald E. Williams. *Acta Crystallographica Section B Structural Science*. [Paper](https://doi.org/10.1107/S0108768102005669)

**Method:** CCDC blind-test cycle 2. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/paper?cnor=bk0108)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S0108768102005669) · [source 2](https://journals.iucr.org/paper?cnor=bk0108)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp022"></a>
### 2005 — A third blind test of crystal structure prediction

**CSP022 · Journal article · Molecular / organic**

G. M. Day; W. D. S. Motherwell; H. L. Ammon; S. X. M. Boerrigter; R. G. Della Valle; E. Venuti; A. Dzyabchenko; J. D. Dunitz; B. Schweizer; B. P. van Eijck; P. Erk; J. C. Facelli; V. E. Bazterra; M. B. Ferraro; D. W. M. Hofmann; F. J. J. Leusen; C. Liang; C. C. Pantelides; P. G. Karamertzanis; S. L. Price; T. C. Lewis; H. Nowell; A. Torrisi; H. A. Scheraga; Y. A. Arnautova; M. U. Schmidt; P. Verwer. *Acta Crystallographica Section B Structural Science*. [Paper](https://doi.org/10.1107/S0108768105016563)

**Method:** CCDC blind-test cycle 3. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/b/issues/2005/05/00/de5014/)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S0108768105016563) · [source 2](https://journals.iucr.org/b/issues/2005/05/00/de5014/)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp036"></a>
### 2008 — Crystal structure prediction from first principles

**CSP036 · Published journal article · Atomic / inorganic**

Scott M. Woodley; Richard Catlow. *Nature Materials*. [Paper](https://doi.org/10.1038/nmat2321)

**Method:** Review landscape search, evolutionary algorithms and construction approaches for inorganic and molecular crystals.. Review landscape search, evolutionary algorithms and construction approaches for inorganic and molecular crystals.

**Inputs:** Review of CSP methodologies

**Groups:** [Woodley–Catlow–Gale–Battle team](https://www.nature.com/articles/nmat2321)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1038/nmat2321) · [source 2](https://www.nature.com/articles/nmat2321)

**Scope:** Historical review; method comparisons reflect the literature available in 2008.

<a id="csp038"></a>
### 2008 — Tailor-Made Force Fields for Crystal-Structure Prediction

**CSP038 · Journal article · Molecular / organic**

Marcus A. Neumann. *The Journal of Physical Chemistry B*. [Paper](https://doi.org/10.1021/jp710575h)

**Method:** Compound-specific fitted force field. Fit low-cost energy models to dispersion-corrected quantum calculations for extensive packing exploration.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GRACE (Generation Ranking and Characterization Engine)](software.md#grace-csp)

**Groups:** [Neumann / GRACE collaboration](https://pubmed.ncbi.nlm.nih.gov/18642947/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/jp710575h) · [source 2](https://pubmed.ncbi.nlm.nih.gov/18642947/)

**Scope:** Enabling evaluator fitted per compound; force-field accuracy must be checked against higher-level references.

<a id="csp040"></a>
### 2009 — Significant progress in predicting the crystal structures of small organic molecules – a report on the fourth blind test

**CSP040 · Journal article · Molecular / organic**

Graeme M. Day; Timothy G. Cooper; Aurora J. Cruz-Cabeza; Katarzyna E. Hejczyk; Herman L. Ammon; Stephan X. M. Boerrigter; Jeffrey S. Tan; Raffaele G. Della Valle; Elisabetta Venuti; Jovan Jose; Shridhar R. Gadre; Gautam R. Desiraju; Tejender S. Thakur; Bouke P. van Eijck; Julio C. Facelli; Victor E. Bazterra; Marta B. Ferraro; Detlef W. M. Hofmann; Marcus A. Neumann; Frank J. J. Leusen; John Kendrick; Sarah L. Price; Alston J. Misquitta; Panagiotis G. Karamertzanis; Gareth W. A. Welch; Harold A. Scheraga; Yelena A. Arnautova; Martin U. Schmidt; Jacco van de Streek; Alexandra K. Wolf; Bernd Schweizer. *Acta Crystallographica Section B Structural Science*. [Paper](https://doi.org/10.1107/S0108768109004066)

**Method:** CCDC blind-test cycle 4. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/b/issues/2009/02/00/bk5081/)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S0108768109004066) · [source 2](https://journals.iucr.org/b/issues/2009/02/00/bk5081/)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp041"></a>
### 2010 — Comparing efficiencies of genetic and minima hopping algorithms for crystal structure prediction

**CSP041 · Published journal article · Atomic / inorganic**

Min Ji; Cai-Zhuang Wang; Kai-Ming Ho. *Physical Chemistry Chemical Physics*. [Paper](https://doi.org/10.1039/C004096G)

**Method:** Evaluate genetic search and minima hopping across compositions, cell sizes and lattice-information constraints.. Run comparable searches on selected Al–Sc and boron systems → vary size and lattice information → compare search efficiency.

**Inputs:** Specified test compositions and cell-size/lattice-information choices

**Groups:** [Ji–Wang–Ho search-evaluation team](https://pubs.rsc.org/en/content/articlelanding/2010/cp/c004096g)

**Evidence:** Primary RSC article abstract and bibliographic metadata. [source 1](https://pubs.rsc.org/en/content/articlelanding/2010/cp/c004096g)

**Scope:** Performance depends strongly on composition, system size and whether lattice vectors are supplied; conclusions cannot be generalized to all CSP problems.

<a id="csp045"></a>
### 2011 — Ab initio random structure searching

**CSP045 · Published journal article · Atomic / inorganic**

Chris J Pickard; R J Needs. *Journal of Physics: Condensed Matter*. [Paper](https://doi.org/10.1088/0953-8984/23/5/053201)

**Method:** Sample chemically sensible random structures, exploit symmetry or motifs, and locally relax each candidate.. Sample chemically sensible random structures, exploit symmetry or motifs, and locally relax each candidate.

**Inputs:** Chemical composition; atom counts or cell-size bounds; pressure

**Structural knowledge:** Molecular units / chemical motifs, Chemical / geometric plausibility, Symmetric initialization — [Mechanisms and limits](structural-priors.md)

**Software:** [AIRSS / buildcell](software.md#airss)

**Groups:** [Pickard–Needs / AIRSS collaboration](https://arxiv.org/abs/1101.3987)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1088/0953-8984/23/5/053201) · [source 2](https://arxiv.org/abs/1101.3987)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp046"></a>
### 2011 — Appendix: First Blind Test of Inorganic Crystal Structure Prediction Methods

**CSP046 · Published book appendix; book first online November 2010, copyright 2011 · Atomic / inorganic**

Artem R. Oganov; J. Christian Schön; Martin Jansen; Scott M. Woodley; William W. Tipton; Richard G. Hennig. *Modern Methods of Crystal Structure Prediction*. [Paper](https://doi.org/10.1002/9783527632831.app1)

**Method:** Compare random search, simulated annealing and evolutionary crystal searches on shared empirical-energy test systems.. Define common compositions and energy models → independent search runs → compare attained energy and relaxation counts.

**Inputs:** Four prescribed inorganic model search problems; common empirical energy evaluator

**Groups:** [Oganov–Schön–Jansen–Woodley–Hennig benchmark collaboration](https://hennig.mse.ufl.edu/publications/)

**Evidence:** Primary Wiley book table of contents and exact appendix DOI; author-maintained bibliography; one-page appendix excerpt. [source 1](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527632831) · [source 2](https://onlinelibrary.wiley.com/doi/10.1002/9783527632831.app1) · [source 3](https://hennig.mse.ufl.edu/publications/) · [source 4](https://uspex-team.org/static/file/Book-Appendix.pdf)

**Scope:** Historical small benchmark, not a universal ranking of all CSP methods. Some targets are highly disordered and may not represent thermodynamically stable compounds. Print/copyright year 2011 differs from first-online 2010.

<a id="csp047"></a>
### 2011 — Current approaches to predicting molecular organic crystal structures

**CSP047 · Journal article · Molecular / organic**

Graeme M. Day. *Crystallography Reviews*. [Paper](https://doi.org/10.1080/0889311X.2010.517526)

**Method:** Review of molecular packing and ranking. Compare global lattice-energy methods and the role of molecular flexibility, electrostatics and polymorphism.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://www.tandfonline.com/doi/pdf/10.1080/0889311X.2010.517526)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1080/0889311X.2010.517526) · [source 2](https://www.tandfonline.com/doi/pdf/10.1080/0889311X.2010.517526)

**Scope:** Historical synthesis, not a new algorithm or current performance benchmark.

<a id="csp049"></a>
### 2011 — Efficient Handling of Molecular Flexibility in Lattice Energy Minimization of Organic Crystals

**CSP049 · Journal article · Molecular / organic**

A. V. Kazantsev; P. G. Karamertzanis; C. S. Adjiman; C. C. Pantelides. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/ct100597e)

**Method:** CrystalOptimizer local minimization. Use local approximate models and cached quantum calculations to minimize lattice energies with molecular flexibility.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CrystalOptimizer / CSO-FM](software.md#crystaloptimizer)

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://pubs.acs.org/doi/abs/10.1021/ct100597e)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/ct100597e) · [source 2](https://pubs.acs.org/doi/abs/10.1021/ct100597e)

**Scope:** Local refinement of supplied candidate structures; not a stand-alone global packing search.

<a id="csp050"></a>
### 2011 — How Evolutionary Crystal Structure Prediction Works—and Why

**CSP050 · Published journal article · Atomic / inorganic**

Artem R. Oganov; Andriy O. Lyakhov; Mario Valle. *Accounts of Chemical Research*. [Paper](https://doi.org/10.1021/ar1001318)

**Method:** Review evolutionary CSP using energy-landscape geometry, variation operators and applications.. Review evolutionary CSP using energy-landscape geometry, variation operators and applications.

**Inputs:** Review of methods; no single prediction input

**Groups:** [Oganov / USPEX collaboration](https://pubs.acs.org/doi/10.1021/ar1001318)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1021/ar1001318) · [source 2](https://pubs.acs.org/doi/10.1021/ar1001318)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp051"></a>
### 2011 — Towards crystal structure prediction of complex organic compounds – a report on the fifth blind test

**CSP051 · Journal article · Molecular / organic**

David A. Bardwell; Claire S. Adjiman; Yelena A. Arnautova; Ekaterina Bartashevich; Stephan X. M. Boerrigter; Doris E. Braun; Aurora J. Cruz-Cabeza; Graeme M. Day; Raffaele G. Della Valle; Gautam R. Desiraju; Bouke P. van Eijck; Julio C. Facelli; Marta B. Ferraro; Damian Grillo; Matthew Habgood; Detlef W. M. Hofmann; Fridolin Hofmann; K. V. Jovan Jose; Panagiotis G. Karamertzanis; Andrei V. Kazantsev; John Kendrick; Liudmila N. Kuleshova; Frank J. J. Leusen; Andrey V. Maleev; Alston J. Misquitta; Sharmarke Mohamed; Richard J. Needs; Marcus A. Neumann; Denis Nikylov; Anita M. Orendt; Rumpa Pal; Constantinos C. Pantelides; Chris J. Pickard; Louise S. Price; Sarah L. Price; Harold A. Scheraga; Jacco van de Streek; Tejender S. Thakur; Siddharth Tiwari; Elisabetta Venuti; Ilia K. Zhitkov. *Acta Crystallographica Section B Structural Science*. [Paper](https://doi.org/10.1107/S0108768111042868)

**Method:** CCDC blind-test cycle 5. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/b/issues/2011/06/00/bk5106/)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S0108768111042868) · [source 2](https://journals.iucr.org/b/issues/2011/06/00/bk5106/)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp061"></a>
### 2014 — Predicting crystal structures of organic compounds

**CSP061 · Journal article · Molecular / organic**

Sarah L. Price. *Chem. Soc. Rev.*. [Paper](https://doi.org/10.1039/C3CS60279F)

**Method:** Crystal-energy-landscape review. Interpret plausible low-energy structures in relation to observed polymorphs, disorder and crystallization.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Price / molecular-crystal modelling collaboration](https://pubs.rsc.org/en/content/articlelanding/2014/cs/c3cs60279f)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1039/C3CS60279F) · [source 2](https://pubs.rsc.org/en/content/articlelanding/2014/cs/c3cs60279f)

**Scope:** Low lattice energy alone does not predict whether a structure nucleates or can be isolated.

<a id="csp068"></a>
### 2016 — Report on the sixth blind test of organic crystal structure prediction methods

**CSP068 · Journal article · Molecular / organic**

Anthony M. Reilly; Richard I. Cooper; Claire S. Adjiman; Saswata Bhattacharya; A. Daniel Boese; Jan Gerit Brandenburg; Peter J. Bygrave; Rita Bylsma; Josh E. Campbell; Roberto Car; David H. Case; Renu Chadha; Jason C. Cole; Katherine Cosburn; Herma M. Cuppen; Farren Curtis; Graeme M. Day; Robert A. DiStasio Jr; Alexander Dzyabchenko; Bouke P. van Eijck; Dennis M. Elking; Joost A. van den Ende; Julio C. Facelli; Marta B. Ferraro; Laszlo Fusti-Molnar; Christina-Anna Gatsiou; Thomas S. Gee; René de Gelder; Luca M. Ghiringhelli; Hitoshi Goto; Stefan Grimme; Rui Guo; Detlef W. M. Hofmann; Johannes Hoja; Rebecca K. Hylton; Luca Iuzzolino; Wojciech Jankiewicz; Daniël T. de Jong; John Kendrick; Niek J. J. de Klerk; Hsin-Yu Ko; Liudmila N. Kuleshova; Xiayue Li; Sanjaya Lohani; Frank J. J. Leusen; Albert M. Lund; Jian Lv; Yanming Ma; Noa Marom; Artëm E. Masunov; Patrick McCabe; David P. McMahon; Hugo Meekes; Michael P. Metz; Alston J. Misquitta; Sharmarke Mohamed; Bartomeu Monserrat; Richard J. Needs; Marcus A. Neumann; Jonas Nyman; Shigeaki Obata; Harald Oberhofer; Artem R. Oganov; Anita M. Orendt; Gabriel I. Pagola; Constantinos C. Pantelides; Chris J. Pickard; Rafal Podeszwa; Louise S. Price; Sarah L. Price; Angeles Pulido; Murray G. Read; Karsten Reuter; Elia Schneider; Christoph Schober; Gregory P. Shields; Pawanpreet Singh; Isaac J. Sugden; Krzysztof Szalewicz; Christopher R. Taylor; Alexandre Tkatchenko; Mark E. Tuckerman; Francesca Vacarro; Manolis Vasileiadis; Alvaro Vazquez-Mayagoitia; Leslie Vogt; Yanchao Wang; Rona E. Watson; Gilles A. de Wijs; Jack Yang; Qiang Zhu; Colin R. Groom. *Acta Crystallographica Section B Structural Science, Crystal Engineering and Materials*. [Paper](https://doi.org/10.1107/S2052520616007447)

**Method:** CCDC blind-test cycle 6. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/b/issues/2016/04/00/gp5080/)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S2052520616007447) · [source 2](https://journals.iucr.org/b/issues/2016/04/00/gp5080/)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp081"></a>
### 2018 — Machine learning for the structure–energy–property landscapes of molecular crystals

**CSP081 · Journal article · Molecular / organic**

Félix Musil; Sandip De; Jack Yang; Joshua E. Campbell; Graeme M. Day; Michele Ceriotti. *Chemical Science*. [Paper](https://doi.org/10.1039/C7SC04665K)

**Method:** Kernel learning and landscape analysis. Use molecular-crystal descriptors, regression and dimensionality reduction to learn energies/properties of candidate polymorphs.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Ceriotti–Day / Musil–De collaboration](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc04665k)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1039/C7SC04665K) · [source 2](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc04665k)

**Scope:** Primarily accelerates evaluation/analysis of pre-generated landscapes rather than proving independent global search.

<a id="csp090"></a>
### 2019 — Structure prediction drives materials discovery

**CSP090 · Published journal article · Atomic / inorganic**

Artem R. Oganov; Chris J. Pickard; Qiang Zhu; Richard J. Needs. *Nature Reviews Materials*. [Paper](https://doi.org/10.1038/s41578-019-0101-8)

**Method:** Compare data-guided and global-search approaches across inorganic, organic and extreme-condition materials.. Compare data-guided and global-search approaches across inorganic, organic and extreme-condition materials.

**Inputs:** Review; no single prediction input

**Groups:** [Oganov–Pickard–Zhu–Needs review collaboration](https://www.nature.com/articles/s41578-019-0101-8)

**Evidence:** Primary abstract and bibliographic metadata. [source 1](https://doi.org/10.1038/s41578-019-0101-8) · [source 2](https://www.nature.com/articles/s41578-019-0101-8)

**Scope:** Finite search budgets and evaluator errors prevent a proof of the global ground state.

<a id="csp098"></a>
### 2020 — Multifidelity Statistical Machine Learning for Molecular Crystal Structure Prediction

**CSP098 · Journal article · Molecular / organic**

Olga Egorova; Roohollah Hafizi; David C. Woods; Graeme M. Day. *The Journal of Physical Chemistry A*. [Paper](https://doi.org/10.1021/acs.jpca.0c05006)

**Method:** Autoregressive Gaussian-process multifidelity ranking. Learn high-level hybrid-DFT energies using force-field and intermediate GGA-DFT calculations on candidate landscapes.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Day / GLEE–mol-CSPy collaboration](https://eprints.soton.ac.uk/443809/)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/acs.jpca.0c05006) · [source 2](https://eprints.soton.ac.uk/443809/)

**Scope:** Reranking pre-generated candidates; reported economy on three small hydrogen-bonding systems is not general search completeness.

<a id="csp099"></a>
### 2020 — Training machine-learning potentials for crystal structure prediction using disordered structures

**CSP099 · Published journal article · Atomic / inorganic**

Changho Hong; Jeong Min Choi; Wonseok Jeong; Sungwoo Kang; Suyeon Ju; Kyeongpung Lee; Jisu Jung; Yong Youn; Seungwu Han. *Physical Review B*. [Paper](https://arxiv.org/abs/2008.07786)

**Method:** Melt-quench training for CSP neural-network potentials. Composition → liquid/amorphous DFT trajectories → NNP training → evolutionary search / DFT comparisons

**Inputs:** Composition and melt-quench trajectories

**Software:** [Disordered-structure NNP training (Hong et al.)](software.md#disordered-structure-nnp-training-hong-et-al)

**Groups:** [Seungwu Han / SPINNER collaboration](https://arxiv.org/abs/2008.07786)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://arxiv.org/abs/2008.07786)

**Scope:** Disordered-phase training improves self-starting CSP but transfer to crystalline minima remains chemistry-dependent.

<a id="compositionsymmetry2021"></a>
### 2021 — Composition based crystal materials symmetry prediction using machine learning with enhanced descriptors

**CompositionSymmetry2021 · Journal article · Atomic / inorganic**

Li, Yuxin; Dong, Rongzhi; Yang, Wenhui; Hu, Jianjun. *Computational Materials Science*. [Paper](https://doi.org/10.1016/j.commatsci.2021.110686)

**Method:** Composition-based symmetry prediction. Random-forest crystal-system and space-group classification from enhanced composition descriptors.

**Inputs:** Formula / composition descriptors

**Software:** [Composition-based symmetry prediction](software.md#composition-symmetry)

**Groups:** [Jianjun Hu–Wenhui Yang collaboration](https://doi.org/10.1016/j.commatsci.2021.110686)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1016/j.commatsci.2021.110686)

**Scope:** Component accuracy is not complete CSP recovery.

<a id="csp103"></a>
### 2021 — Crystal Structure Prediction Methods for Organic Molecules: State of the Art

**CSP103 · Journal article · Molecular / organic**

David H. Bowskill; Isaac J. Sugden; Stefanos Konstantinopoulos; Claire S. Adjiman; Constantinos C. Pantelides. *Annual Review of Chemical and Biomolecular Engineering*. [Paper](https://doi.org/10.1146/annurev-chembioeng-060718-030256)

**Method:** Common-framework molecular CSP review. Compare packing generation, conformational treatment, energy models and refinement for organic CSP.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [Pantelides–Adjiman / CrystalPredictor–CrystalOptimizer](https://www.annualreviews.org/content/journals/10.1146/annurev-chembioeng-060718-030256)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1146/annurev-chembioeng-060718-030256) · [source 2](https://www.annualreviews.org/content/journals/10.1146/annurev-chembioeng-060718-030256)

**Scope:** Review snapshot; not a benchmark demonstrating equal accuracy across molecular classes.

<a id="mlatticeabc2021"></a>
### 2021 — MLatticeABC: Generic Lattice Constant Prediction of Crystal Materials Using Machine Learning

**MLatticeABC2021 · Journal article · Atomic / inorganic**

Li, Yuxin; Yang, Wenhui; Dong, Rongzhi; Hu, Jianjun. *ACS Omega*. [Paper](https://doi.org/10.1021/acsomega.1c00781)

**Method:** MLatticeABC. Random-forest lattice prediction from composition descriptors and atom-count features.

**Inputs:** Composition descriptors and atom-count information

**Software:** [MLatticeABC](software.md#mlatticeabc)

**Groups:** [Jianjun Hu–Wenhui Yang collaboration](https://doi.org/10.1021/acsomega.1c00781)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1021/acsomega.1c00781)

**Scope:** Component accuracy is not complete CSP recovery.

<a id="csp109"></a>
### 2022 — A universal graph deep learning interatomic potential for the periodic table

**CSP109 · Published journal article · Atomic / inorganic**

Chi Chen; Shyue Ping Ong. *Nature Computational Science*. [Paper](https://www.nature.com/articles/s43588-022-00349-3)

**Method:** M3GNet universal graph interatomic potential. Train on energy / force / stress relaxation trajectories → rapid candidate relaxation / scoring within a separately chosen search

**Inputs:** Complete candidate atomic structures

**Software:** [M3GNet](software.md#m3gnet)

**Groups:** [Shyue Ping Ong / Materials Virtual Lab](https://www.nature.com/articles/s43588-022-00349-3)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://www.nature.com/articles/s43588-022-00349-3) · [source 2](https://arxiv.org/abs/2202.02450)

**Scope:** An energy evaluator does not independently propose structures or guarantee global search coverage; novel configurations require validation.

<a id="csp122"></a>
### 2022 — Search methods for inorganic materials crystal structure prediction

**CSP122 · Published journal paper · Atomic / inorganic**

Xiangyu Yin; Chrysanthos E Gounaris. *Current Opinion in Chemical Engineering*. [Paper](https://doi.org/10.1016/j.coche.2021.100726)

**Method:** Review compares empirical, guided-sampling, data-driven and mathematical-optimization CSP searches.. Compare proposal/search approaches separately from stability evaluation

**Inputs:** Inorganic CSP methods

**Groups:** [Yin–Gounaris / mathematical optimization collaboration](https://doi.org/10.1016/j.coche.2021.100726)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1016/j.coche.2021.100726)

**Scope:** A review, not an independent common-budget performance ranking.

<a id="csp127"></a>
### 2023 — CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling

**CSP127 · Published journal article · Atomic / inorganic**

Bowen Deng; Peichen Zhong; KyuJung Jun; Janosh Riebesell; Kevin Han; Christopher J. Bartel; Gerbrand Ceder. *Nature Machine Intelligence*. [Paper](https://www.nature.com/articles/s42256-023-00716-3)

**Method:** CHGNet charge-informed universal graph interatomic potential. Train on energies / forces / stresses / magnetic moments → evaluate and relax candidates from outer CSP search

**Inputs:** Complete candidate atomic structures

**Software:** [CHGNet](software.md#chgnet)

**Groups:** [Gerbrand Ceder / data-driven crystal modeling](https://www.nature.com/articles/s42256-023-00716-3)

**Evidence:** Publisher abstract and author-hosted paper first-page metadata. [source 1](https://www.nature.com/articles/s42256-023-00716-3) · [source 2](https://ceder.berkeley.edu/publications/2023_Bowen_CHGNet.pdf)

**Scope:** A pretrained evaluator is not a proposal/search algorithm; charge/magnetic priors do not make all magnetic or OOD configurations reliable.

<a id="csp129"></a>
### 2023 — Crystal structure prediction: achievements and opportunities

**CSP129 · Published journal paper · Cross-domain**

C. Richard A. Catlow. *IUCrJ*. [Paper](https://doi.org/10.1107/s2052252523001835)

**Method:** Editorial distinguishes energy-minimized modeling from predictive structure search.. Assess historical progress and remaining prediction challenges

**Inputs:** Cross-domain CSP literature

**Groups:** [Catlow / atomistic structure modeling](https://doi.org/10.1107/s2052252523001835)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1107/s2052252523001835)

**Scope:** An editorial perspective, not a quantitative benchmark.

<a id="csp132"></a>
### 2023 — Geometric Deep Learning for Molecular Crystal Structure Prediction

**CSP132 · Journal article · Molecular / organic**

Michael Kilgour; Jutta Rogal; Mark Tuckerman. *Journal of Chemical Theory and Computation*. [Paper](https://doi.org/10.1021/acs.jctc.3c00031)

**Method:** MolXtalNet density and plausibility scoring. Predict density to constrain search and classify/score candidate crystal packings using geometric graph learning.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [MolXtalNet-D / MolXtalNet-S (MXtalTools)](software.md#molxtalnet-mxtaltools)

**Groups:** [Tuckerman–Rogal / Kilgour collaboration](https://arxiv.org/abs/2303.10140)

**Evidence:** Primary abstract and bibliographic record. [source 1](https://doi.org/10.1021/acs.jctc.3c00031) · [source 2](https://arxiv.org/abs/2303.10140)

**Scope:** Real-versus-synthetic discrimination is not an absolute energy or ground-state certificate.

<a id="csp135"></a>
### 2023 — Predicting crystal form stability under real-world conditions

**CSP135 · Journal article · Molecular / organic**

Dzmitry Firaha; Yifei Michelle Liu; Jacco van de Streek; Kiran Sasikumar; Hanno Dietrich; Julian Helfferich; Luc Aerts; Doris E. Braun; Anders Broo; Antonio G. DiPasquale; Alfred Y. Lee; Sarah Le Meur; Sten O. Nilsson Lill; Walter J. Lunsmann; Alessandra Mattei; Pierandrea Muglia; Okky Dwichandra Putra; Mohamed Raoui; Susan M. Reutzel-Edens; Sandrine Rome; Ahmad Y. Sheikh; Alexandre Tkatchenko; Grahame R. Woollam; Marcus A. Neumann. *Nature*. [Paper](https://doi.org/10.1038/s41586-023-06587-3)

**Method:** Temperature/humidity-dependent free-energy ranking. Combine accurate lattice energies with finite-temperature contributions and hydration chemical potentials; quantify free-energy prediction errors.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [GRACE (Generation Ranking and Characterization Engine)](software.md#grace-csp)

**Groups:** [Neumann / GRACE collaboration](https://www.nature.com/articles/s41586-023-06587-3)

**Evidence:** Primary abstract and selected benchmark/methods. [source 1](https://doi.org/10.1038/s41586-023-06587-3) · [source 2](https://www.nature.com/articles/s41586-023-06587-3)

**Scope:** Ranking and risk assessment require candidate polymorphs/hydrates; numerical uncertainty and missing forms limit guarantees.

<a id="csp155"></a>
### 2024 — The seventh blind test of crystal structure prediction: structure generation methods

**CSP155 · Journal article · Molecular / organic**

Lily M. Hunnisett; Jonas Nyman; Nicholas Francia; Nathan S. Abraham; Claire S. Adjiman; Srinivasulu Aitipamula; Tamador Alkhidir; Mubarak Almehairbi; Andrea Anelli; Dylan M. Anstine; John E. Anthony; Joseph E. Arnold; Faezeh Bahrami; Michael A. Bellucci; Rajni M. Bhardwaj; Imanuel Bier; Joanna A. Bis; A. Daniel Boese; David H. Bowskill; James Bramley; Jan Gerit Brandenburg; Doris E. Braun; Patrick W. V. Butler; Joseph Cadden; Stephen Carino; Eric J. Chan; Chao Chang; Bingqing Cheng; Sarah M. Clarke; Simon J. Coles; Richard I. Cooper; Ricky Couch; Ramon Cuadrado; Tom Darden; Graeme M. Day; Hanno Dietrich; Yiming Ding; Antonio DiPasquale; Bhausaheb Dhokale; Bouke P. van Eijck; Mark R. J. Elsegood; Dzmitry Firaha; Wenbo Fu; Kaori Fukuzawa; Joseph Glover; Hitoshi Goto; Chandler Greenwell; Rui Guo; Jürgen Harter; Julian Helfferich; Detlef W. M. Hofmann; Johannes Hoja; John Hone; Richard Hong; Geoffrey Hutchison; Yasuhiro Ikabata; Olexandr Isayev; Ommair Ishaque; Varsha Jain; Yingdi Jin; Aling Jing; Erin R. Johnson; Ian Jones; K. V. Jovan Jose; Elena A. Kabova; Adam Keates; Paul F. Kelly; Dmitry Khakimov; Stefanos Konstantinopoulos; Liudmila N. Kuleshova; He Li; Xiaolu Lin; Alexander List; Congcong Liu; Yifei Michelle Liu; Zenghui Liu; Zhi-Pan Liu; Joseph W. Lubach; Noa Marom; Alexander A. Maryewski; Hiroyuki Matsui; Alessandra Mattei; R. Alex Mayo; John W. Melkumov; Sharmarke Mohamed; Zahrasadat Momenzadeh Abardeh; Hari S. Muddana; Naofumi Nakayama; Kamal Singh Nayal; Marcus A. Neumann; Rahul Nikhar; Shigeaki Obata; Dana O'Connor; Artem R. Oganov; Koji Okuwaki; Alberto Otero-de-la-Roza; Constantinos C. Pantelides; Sean Parkin; Chris J. Pickard; Luca Pilia; Tatyana Pivina; Rafał Podeszwa; Alastair J. A. Price; Louise S. Price; Sarah L. Price; Michael R. Probert; Angeles Pulido; Gunjan Rajendra Ramteke; Atta Ur Rehman; Susan M. Reutzel-Edens; Jutta Rogal; Marta J. Ross; Adrian F. Rumson; Ghazala Sadiq; Zeinab M. Saeed; Alireza Salimi; Matteo Salvalaglio; Leticia Sanders de Almada; Kiran Sasikumar; Sivakumar Sekharan; Cheng Shang; Kenneth Shankland; Kotaro Shinohara; Baimei Shi; Xuekun Shi; A. Geoffrey Skillman; Hongxing Song; Nina Strasser; Jacco van de Streek; Isaac J. Sugden; Guangxu Sun; Krzysztof Szalewicz; Benjamin I. Tan; Lu Tan; Frank Tarczynski; Christopher R. Taylor; Alexandre Tkatchenko; Rithwik Tom; Mark E. Tuckerman; Yohei Utsumi; Leslie Vogt-Maranto; Jake Weatherston; Luke J. Wilkinson; Robert D. Willacy; Lukasz Wojtas; Grahame R. Woollam; Zhuocen Yang; Etsuo Yonemochi; Xin Yue; Qun Zeng; Yizu Zhang; Tian Zhou; Yunfei Zhou; Roman Zubatyuk; Jason C. Cole. *Acta Crystallographica Section B Structural Science, Crystal Engineering and Materials*. [Paper](https://doi.org/10.1107/S2052520624007492)

**Method:** CCDC blind-test cycle 7. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/b/issues/2024/06/00/aw5093/)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S2052520624007492) · [source 2](https://journals.iucr.org/b/issues/2024/06/00/aw5093/)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="csp156"></a>
### 2024 — The seventh blind test of crystal structure prediction: structure ranking methods

**CSP156 · Journal article · Molecular / organic**

Lily M. Hunnisett; Nicholas Francia; Jonas Nyman; Nathan S. Abraham; Srinivasulu Aitipamula; Tamador Alkhidir; Mubarak Almehairbi; Andrea Anelli; Dylan M. Anstine; John E. Anthony; Joseph E. Arnold; Faezeh Bahrami; Michael A. Bellucci; Gregory J. O. Beran; Rajni M. Bhardwaj; Raffaello Bianco; Joanna A. Bis; A. Daniel Boese; James Bramley; Doris E. Braun; Patrick W. V. Butler; Joseph Cadden; Stephen Carino; Ctirad Červinka; Eric J. Chan; Chao Chang; Sarah M. Clarke; Simon J. Coles; Cameron J. Cook; Richard I. Cooper; Tom Darden; Graeme M. Day; Wenda Deng; Hanno Dietrich; Antonio DiPasquale; Bhausaheb Dhokale; Bouke P. van Eijck; Mark R. J. Elsegood; Dzmitry Firaha; Wenbo Fu; Kaori Fukuzawa; Nikolaos Galanakis; Hitoshi Goto; Chandler Greenwell; Rui Guo; Jürgen Harter; Julian Helfferich; Johannes Hoja; John Hone; Richard Hong; Michal Hušák; Yasuhiro Ikabata; Olexandr Isayev; Ommair Ishaque; Varsha Jain; Yingdi Jin; Aling Jing; Erin R. Johnson; Ian Jones; K. V. Jovan Jose; Elena A. Kabova; Adam Keates; Paul F. Kelly; Jiří Klimeš; Veronika Kostková; He Li; Xiaolu Lin; Alexander List; Congcong Liu; Yifei Michelle Liu; Zenghui Liu; Ivor Lončarić; Joseph W. Lubach; Jan Ludík; Noa Marom; Hiroyuki Matsui; Alessandra Mattei; R. Alex Mayo; John W. Melkumov; Bruno Mladineo; Sharmarke Mohamed; Zahrasadat Momenzadeh Abardeh; Hari S. Muddana; Naofumi Nakayama; Kamal Singh Nayal; Marcus A. Neumann; Rahul Nikhar; Shigeaki Obata; Dana O'Connor; Artem R. Oganov; Koji Okuwaki; Alberto Otero-de-la-Roza; Sean Parkin; Antonio Parunov; Rafał Podeszwa; Alastair J. A. Price; Louise S. Price; Sarah L. Price; Michael R. Probert; Angeles Pulido; Gunjan Rajendra Ramteke; Atta Ur Rehman; Susan M. Reutzel-Edens; Jutta Rogal; Marta J. Ross; Adrian F. Rumson; Ghazala Sadiq; Zeinab M. Saeed; Alireza Salimi; Kiran Sasikumar; Sivakumar Sekharan; Kenneth Shankland; Baimei Shi; Xuekun Shi; Kotaro Shinohara; A. Geoffrey Skillman; Hongxing Song; Nina Strasser; Jacco van de Streek; Isaac J. Sugden; Guangxu Sun; Krzysztof Szalewicz; Lu Tan; Kehan Tang; Frank Tarczynski; Christopher R. Taylor; Alexandre Tkatchenko; Rithwik Tom; Petr Touš; Mark E. Tuckerman; Pablo A. Unzueta; Yohei Utsumi; Leslie Vogt-Maranto; Jake Weatherston; Luke J. Wilkinson; Robert D. Willacy; Lukasz Wojtas; Grahame R. Woollam; Yi Yang; Zhuocen Yang; Etsuo Yonemochi; Xin Yue; Qun Zeng; Tian Zhou; Yunfei Zhou; Roman Zubatyuk; Jason C. Cole. *Acta Crystallographica Section B Structural Science, Crystal Engineering and Materials*. [Paper](https://doi.org/10.1107/S2052520624008679)

**Method:** CCDC blind-test cycle 7 — ranking. Withhold experimental crystal structures; compare independent sampling and/or ranking submissions against experimental molecular crystals.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Groups:** [CCDC blind-test community collaboration](https://journals.iucr.org/b/issues/2024/06/00/aw5094/)

**Evidence:** Primary report abstract; selected methods/results of cycles 3, 4, 6 and 7. [source 1](https://doi.org/10.1107/S2052520624008679) · [source 2](https://journals.iucr.org/b/issues/2024/06/00/aw5094/)

**Scope:** Target difficulty and allowed prior information change between cycles; top-3/top-100 and generation/ranking metrics are not directly interchangeable. Publication year differs from test year.

<a id="cspmetrics2024"></a>
### 2024 — Towards quantitative evaluation of crystal structure prediction performance

**CSPMetrics2024 · Journal article · Atomic / inorganic**

Wei, Lai; Li, Qin; Omee, Sadman Sadeed; Hu, Jianjun. *Computational Materials Science*. [Paper](https://doi.org/10.1016/j.commatsci.2024.112802)

**Method:** CSPMetrics. Quantitative structure comparison using complementary geometry, graph, fingerprint and energy distances.

**Inputs:** Predicted and reference structures

**Software:** [CSPMetrics](software.md#cspmetrics)

**Groups:** [Jianjun Hu group](https://doi.org/10.1016/j.commatsci.2024.112802)

**Evidence:** Primary abstract and bibliographic record; author repository README when linked. [source 1](https://doi.org/10.1016/j.commatsci.2024.112802)

**Scope:** Component accuracy is not complete CSP recovery.

<a id="matbenchgenmetrics2024"></a>
### 2024 — matbench-genmetrics: A Python library for benchmarking crystal structure generative models using time-based splits of Materials Project structures

**MatbenchGenmetrics2024 · Journal article · Atomic / inorganic**

Sterling G. Baird; Hasan M. Sayeed; Joseph Montoya; Taylor D. Sparks. *Journal of Open Source Software*. [Paper](https://doi.org/10.21105/joss.05618)

**Method:** matbench-genmetrics / MPTS-52. Time-based Materials Project splits and crystal generation metrics.

**Inputs:** Crystal datasets and generated structures

**Groups:** [Baird–Sparks collaboration](https://joss.theoj.org/papers/10.21105/joss.05618)

**Evidence:** Primary JOSS record and original data repository README. [source 1](https://joss.theoj.org/papers/10.21105/joss.05618) · [source 2](https://github.com/sparks-baird/mp-time-split)

**Scope:** See primary source

<a id="csp180"></a>
### 2026 — Crystal Structure Prediction of Inorganic Materials: A Benchmark and Modern Evaluation

**CSP180 · Published journal paper · Atomic / inorganic**

Lai Wei; Sadman Sadeed Omee; Rongzhi Dong; Nihang Fu; Yuqi Song; Edirisuriya M. Dilanga Siriwardane; Meiling Xu; Ming Hu; Chris Wolverton; Jianjun Hu. *Advanced Intelligent Discovery*. [Paper](https://doi.org/10.1002/aidi.70162)

**Method:** CSP180 evaluates template, ML-potential and deep-learning approaches with multiple structure metrics.. 180 inorganic targets → specified algorithm implementations → structure/energy metrics; DFT subset compared separately

**Inputs:** Frozen benchmark structures and declared implementations

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://doi.org/10.1002/aidi.70162)

**Evidence:** Primary publisher/abstract and selected method descriptions; Crossref metadata where available. [source 1](https://doi.org/10.1002/aidi.70162)

**Scope:** The 23-structure DFT subset and 180-target DFT-free study have different denominators; implementation constraints and template availability affect comparisons.

<a id="csp181"></a>
### 2026 — Crystal structure prediction with nuclear quantum and finite-temperature effects via deep free energy learning

**CSP181 · Published journal article · Atomic / inorganic**

Xiaoyang Wang; Yinan Wang; Wenbo Zhao; Hanyu Liu; Hao Xie; Lei Wang; Han Wang. *Physical Review B*. [Paper](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7)

**Method:** Deep free-energy learning with two-level concurrent learning. SCHA free-energy labels → neural free-energy/force/stress model → finite-temperature / quantum-aware CSP

**Inputs:** Composition / pressure / temperature and quantum free-energy training labels

**Software:** [Deep free energy (DF) CSP](software.md#deep-free-energy-df-csp)

**Groups:** [Han Wang / Lei Wang / Hanyu Liu collaboration](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7)

**Evidence:** Publisher abstract and author list; published6October2026. [source 1](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7)

**Scope:** Enables finite-temperature and nuclear-quantum scoring; tested La–Sc–H domain is not a universal free-energy model or a new exhaustive structure proposer.

<a id="csp186"></a>
### 2026 — DFT Accuracy on Crystal Structure Prediction with Machine Learning Interatomic Potentials

**CSP186 · Preprint · Molecular / organic**

Laurence I. Midgley; Chen Lin; J. Harry Moore; Flaviano Della Pia; Javier Antorán; Sten O. Nilsson Lill; Emma S. E. Eriksson; Felix A. Faber; Lars Tornberg; Anders Broo; Gábor Csányi. *arXiv*. [Paper](https://arxiv.org/abs/2605.28905)

**Method:** Inter/intramolecular delta-learned molecular-crystal potential. Combine MACE-POLAR intramolecular modeling with long-range dispersion and a DFT-targeted intermolecular delta model.

**Inputs:** Molecular chemical graph or molecular geometry; space groups, Z/Z-prime and conformation assumptions as specified in the paper

**Software:** [CSP-MACE-Å](software.md#csp-mace-a)

**Groups:** [Csányi–AstraZeneca / CSP-MACE-Å collaboration](https://arxiv.org/abs/2605.28905)

**Evidence:** Primary arXiv abstract. [source 1](https://arxiv.org/abs/2605.28905)

**Scope:** Preprint evaluator validation; potential accuracy and structure ranking are separate from global-search completeness.

<a id="csp185"></a>
### 2026 — Deep Generative Crystal Structure Prediction: A Benchmark Study and a Controlled Test of Prototype Dependence

**CSP185 · Preprint · Atomic / inorganic**

Lai Wei; Rongzhi Dong; Ying Feng; Madeline Miklos; Jianjun Hu. *arXiv:2609.26502v1*. [Paper](https://arxiv.org/abs/2609.26502v1)

**Method:** Compares generative CSP with template retrieval and tests removal of prototype families during training.. Matched structural evaluation → template/generator comparison → retraining after family removal

**Inputs:** 180 reference structures and a leakage-controlled subset; training/removal protocol

**Groups:** [Jianjun Hu / USC crystal prediction collaboration](https://arxiv.org/abs/2609.26502v1)

**Evidence:** Primary abstract, author list and selected introduction; no independent reproduction. [source 1](https://arxiv.org/abs/2609.26502v1)

**Scope:** Preprint; findings concern the tested datasets, models and controlled family removals. Template overlap, recovery, novelty and phase stability are different quantities.

<a id="csp190"></a>
### 2026 — OpenCSP: a deep learning framework for crystal structure prediction from ambient to high pressure

**CSP190 · Published journal article · Atomic / inorganic**

Yinan Wang; Xiaoyang Wang; Zhenyu Wang; Jing Wu; Jian Lv; Weinan E; Han Wang. *npj Computational Materials*. [Paper](https://www.nature.com/articles/s41524-026-02180-0)

**Method:** OpenCSP: pressure-resolved concurrent learning and atomistic models. Randomized high-pressure sampling → uncertainty-guided DFT labels → pressure-resolved MLIP training → CSP enthalpy ranking

**Inputs:** Chemical systems, pressure and candidate structures

**Software:** [OpenCSP (crystal prediction)](software.md#opencsp-crystal-prediction)

**Groups:** [Han Wang / Jian Lv / Weinan E collaboration](https://www.nature.com/articles/s41524-026-02180-0)

**Evidence:** Primary publisher or author-submitted abstract and author metadata. [source 1](https://www.nature.com/articles/s41524-026-02180-0)

**Scope:** Enabling dataset/models rather than a unique proposal mechanism; non-spin-polarized DFT labels and pressure-domain coverage constrain transfer.
