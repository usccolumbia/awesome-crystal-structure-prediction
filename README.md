<p align="center"><img src="assets/banner.svg" alt="Awesome Crystal Structure Prediction" width="100%"></p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

# Awesome Crystal Structure Prediction (CSP)

A curated directory of **algorithms, papers, source code, pretrained models, datasets, and evaluation benchmarks** for predicting periodic crystal structures. Covers inorganic and molecular crystals, classical search, learned generation, and the components that connect them.

Companion resources for *Crystal Structure Prediction from Search to Learning: A 30-Year Expedition* (survey in preparation). Related collection: [Awesome Crystal Prototype](https://github.com/usccolumbia/awesome-crystal-prototype).

**208 literature/software-paper records · 129 implementation and component entries · 42 formula-conditioning audits.** Literature window: 1996–16 October 2026. Resource checks: 16–17 October 2026. This is a curated collection, not an exhaustive census or a performance ranking. The 1996 start is a survey boundary; the founding USPEX journal papers appeared in 2006.

## Contents

- [Browse and download](#browse-and-download)
- [Algorithm categories](#algorithm-categories)
- [Symmetry, topology and domain knowledge](#symmetry-topology-and-domain-knowledge)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [How to interpret availability](#how-to-interpret-availability)
- [Contributing](CONTRIBUTING.md) · [Provenance](docs/provenance.md) · [BibTeX](references.bib)

## Browse and download

| Resource | What it contains |
|---|---|
| [Structural knowledge guide](docs/structural-priors.md) | Symmetry, Wyckoff sites, topology, motifs, prototypes and ordering; papers and code links |
| [All papers](docs/papers.md) | Category, year, publication status, method, input information, group attribution, and primary sources |
| [Software profiles](docs/software.md) | Paper/code links, license evidence, checkpoints, training data, evaluations, and limitations |
| [Benchmarks](docs/benchmarks.md) | MP-20, MPTS-52, CSPBench, T180, T46, CSPMetrics; dataset and protocol distinctions |
| [Dataset index](docs/datasets.md) | Training, reference, and evaluation resources linked to each implementation |
| [Formula-conditioning audit](docs/formula-conditioning.md) | Exact cell counts, adaptation requirements, and unconditional generation |
| [Research groups](docs/groups.md) | Paper attribution with verification sources; collaborations are retained |
| [Interactive explorer](docs/index.html) | Download/clone and open this self-contained HTML file in a browser; search and filter locally |
| [Machine-readable data](data/) | JSON and CSV catalogues; [BibTeX](references.bib) for citations |

To browse locally:

```bash
git clone https://github.com/usccolumbia/awesome-crystal-structure-prediction.git
cd awesome-crystal-structure-prediction
python3 -m http.server 8000
# Open http://localhost:8000/docs/
```

## Symmetry, topology and domain knowledge

Explore [21 documented method profiles](docs/structural-priors.md), including USPEX topology generation, constrained molecular USPEX, CALYPSO/SPAI divide-and-conquer, MAGUS, and symmetry-aware learned models. The [interactive explorer](docs/index.html) filters papers and software by nine structural-knowledge categories alongside algorithm family, group and release availability. Untagged entries have not been assessed in this focused pass.

## Algorithm categories

Categories describe candidate construction or search. Learned energy evaluators, symmetry predictors, and metric packages are listed as supporting components. Hybrids retain secondary categories in the data. Each table links to detailed release evidence.

### Construction, templates and discrete search

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **CRYSIM** | [2025 CSP176](https://www.nature.com/articles/s42005-025-02380-y) | [Source](https://github.com/tsudalab/CRYSIM) | [Profile](docs/software.md#crysim) |
| **CSPML** | [2022 CSP115](https://www.sciencedirect.com/science/article/pii/S0927025622002555) | [Source](https://github.com/Minoru938/CSPML) | [Profile](docs/software.md#cspml) |
| **Data-mined ionic substitution (pymatgen implementation)** | [2011 CSP048](https://doi.org/10.1021/ic102031h) | [Source](https://github.com/materialsproject/pymatgen) | [Profile](docs/software.md#pymatgen-ionic-substitution) |
| **Data-mined prototype search (Curtarolo / Fischer / Ceder)** | [2003 CSP017](https://doi.org/10.1103/PhysRevLett.91.135503) · [2006 CSP029](https://doi.org/10.1038/nmat1691) | Not verified | [Profile](docs/software.md#data-mined-prototype-search) |
| **enumlib** | [2008 CSP035](https://doi.org/10.1103/PhysRevB.77.224115) · [2012 CSP056](https://doi.org/10.1016/j.commatsci.2012.02.015) | [Source](https://github.com/msg-byu/enumlib) | [Profile](docs/software.md#enumlib) |
| **GRINSP / GRINS** | [2005 CSP024](https://doi.org/10.1107/S0021889805002384) | [Source](https://www.cristal.org/grinsp/) | [Profile](docs/software.md#grinsp) |
| **IPCSP (integer-programming CSP)** | [2023 CSP133](https://doi.org/10.1038/s41586-023-06071-y) | [Source](https://github.com/lrcfmd/ipcsp) | [Profile](docs/software.md#ipcsp) |
| **Periodic tetrahedral-framework enumeration (Treacy et al.)** | [1997 CSP004](https://doi.org/10.1524/zkri.1997.212.11.768) · [2004 CSP019](https://doi.org/10.1016/j.micromeso.2004.06.013) | Not verified | [Profile](docs/software.md#tetrahedral-framework-enumeration) |
| **SPAI / CALYPSO symmetry divide-and-conquer** | [2022 CSP108](https://doi.org/10.1063/5.0074677) | [Access portal](https://download.calypso.cn/home/) | [Profile](docs/software.md#symmetry-divide-conquer) |
| **Systematic crystalline-network enumeration (Delgado Friedrichs et al.)** | [1999 CSP006](https://doi.org/10.1038/23210) | Not verified | [Profile](docs/software.md#systematic-network-enumeration) |
| **Systematic periodic-network search (Winkler–Pickard–Thimm)** | [2001 CSP011](https://doi.org/10.1016/S0009-2614(01)00126-9) · [2004 CSP021](https://doi.org/10.1103/PhysRevB.70.045101) | Not verified | [Profile](docs/software.md#quotient-graph-search) |
| **TCSP / TCSP2.0** | [2022 CSP123](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879) · [2026 CSP194](https://www.sciencedirect.com/science/article/pii/S0927025625006603) | [Source](https://github.com/usccolumbia/TCSP) | [Profile](docs/software.md#tcsp) |

### Random structure search

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **AIRSS / buildcell** | [2006 CSP028](https://doi.org/10.1103/PhysRevLett.97.045504) · [2025 CSP165](https://doi.org/10.1039/D4FD00134F) · [2011 CSP045](https://doi.org/10.1088/0953-8984/23/5/053201) | [Source](https://www.mtg.msm.cam.ac.uk/Codes/AIRSS) | [Profile](docs/software.md#airss) |
| **CrystalPredictor / CrystalPredictor II** | [2005 CSP023](https://doi.org/10.1002/jcc.20165) · [2007 CSP031](https://doi.org/10.1080/00268970601143317) · [2015 CSP063](https://doi.org/10.1021/ct500621v) · [2016 CSP065](https://doi.org/10.1107/S2052520616015122) | [Access portal](https://sargentcentre.org/impact/spinouts-software/) | [Profile](docs/software.md#crystalpredictor) |
| **CSP(aiFF) / autoPES–UPACK workflow** | [2022 CSP121](https://doi.org/10.1038/s41467-022-30692-y) | [Access portal](https://www.physics.udel.edu/~szalewic/SAPT/SAPT.html) | [Profile](docs/software.md#csp-aiff) |
| **Genarris (1.0–3.x; Rigid Press)** | [2018 CSP079](https://doi.org/10.1063/1.5014038) · [2020 CSP096](https://doi.org/10.1016/j.cpc.2020.107170) · [2025 CSP171](https://doi.org/10.1021/acs.jctc.5c01080) | [Source](https://www.noamarom.com/wp-content/uploads/2026/06/gnrs-3.1.4.zip) | [Profile](docs/software.md#genarris) |
| **GLEE (Global Lattice Energy Explorer)** | [2016 CSP066](https://doi.org/10.1021/acs.jctc.5b01112) · [2017 CSP071](https://doi.org/10.1038/nature21419) | [Access portal](https://eprints.soton.ac.uk/385478) | [Profile](docs/software.md#glee) |
| **HTOCSP (population / width-first sampling)** | [2025 CSP164](https://doi.org/10.1039/D4DD00264D) | [Source](https://github.com/MaterSim/HTOCSP) | [Profile](docs/software.md#htocsp) |
| **mol-CSPy: quasi-random sampling, QRBH and threshold MC** | [2016 CSP066](https://doi.org/10.1021/acs.jctc.5b01112) · [2021 CSP104](https://doi.org/10.1021/acs.jctc.0c01101) · [2022 CSP116](https://doi.org/10.1038/s42004-022-00705-4) · [2023 CSP136](https://doi.org/10.1073/pnas.2300516120) | [Source](https://gitlab.com/mol-cspy/mol-cspy) | [Profile](docs/software.md#mol-cspy) |
| **PyXtal** | [2021 CSP107](https://doi.org/10.1016/j.cpc.2020.107810) | [Source](https://github.com/MaterSim/PyXtal) | [Profile](docs/software.md#pyxtal) |
| **RandSpg** | [2017 CSP072](https://doi.org/10.1016/j.cpc.2016.12.005) | [Source](https://github.com/xtalopt/randSpg) | [Profile](docs/software.md#randspg) |
| **Schrödinger Crystal Structure Prediction** | [2025 CSP161](https://doi.org/10.1038/s41467-025-57479-1) | [Access portal](https://www.schrodinger.com/platform/products/ms-crystal-structure-prediction/) | [Profile](docs/software.md#schrodinger-csp) |
| **Symmetry-driven structure search (Domingos–Shaik–Militzer)** | [2018 CSP082](https://doi.org/10.1103/PhysRevB.98.174107) | Not verified | [Profile](docs/software.md#symmetry-driven-random-search) |
| **UPACK** | [1999 CSP008](https://doi.org/10.1002/(SICI)1096-987X(199906)20:8<799::AID-JCC6>3.0.CO;2-Z) | [Access portal](http://www.crystal.chem.uu.nl/~vaneyck/upack.html) | [Profile](docs/software.md#upack) |

### Evolutionary and genetic search

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **Adaptive Genetic Algorithm (AGA; Wang–Ho collaboration)** | [2014 CSP059](https://doi.org/10.1088/0953-8984/26/3/035402) | Not verified | [Profile](docs/software.md#aga) |
| **CMCrystal** | [2021 CMCrystal2021](https://doi.org/10.1039/d0ce01714k) | [Source](https://github.com/usccolumbia/cmcrystal) | [Profile](docs/software.md#cmcrystal) |
| **CMCrystalMOO / MOOCSP** | [2022 CMCrystalMOO2022](https://doi.org/10.1021/acs.jpca.1c07170) | [Source](https://github.com/usccolumbia/MOOCSP) | [Profile](docs/software.md#cmcrystalmoo) |
| **CrySPAI** | [2025 CSP167](https://arxiv.org/abs/2501.15838) | [Access portal](https://www.mdpi.com/2411-5134/10/2/26/html) | [Profile](docs/software.md#cryspai) |
| **DMCrystal** | [2020 DMCrystal2020](https://doi.org/10.1021/acs.jpca.0c08775) | [Source](https://github.com/usccolumbia/dmcrystal) | [Profile](docs/software.md#dmcrystal) |
| **Evolutionary alloy-prototype search (Jóhannesson et al.)** | [2002 CSP013](https://doi.org/10.1103/PhysRevLett.88.255506) | Not verified | [Profile](docs/software.md#norskov-alloy-search) |
| **GASP-Python** | [2019 CSP080](https://doi.org/10.5281/zenodo.2554076) | [Source](https://github.com/henniggroup/GASP-python) | [Profile](docs/software.md#gasp-python) |
| **GAtor** | [2018 CSP076](https://doi.org/10.1039/C8FD00067K) · [2018 CSP078](https://doi.org/10.1021/acs.jctc.7b01152) | [Source](https://www.noamarom.com/wp-content/uploads/2023/01/GAtor_Test.zip) | [Profile](docs/software.md#gator-molecular) |
| **GSGO (global space-group optimization)** | [2007 CSP033](https://doi.org/10.1103/PhysRevB.75.104113) | Not verified | [Profile](docs/software.md#gsgo) |
| **Ionic-crystal genetic algorithm (Woodley et al.)** | [1999 CSP007](https://doi.org/10.1039/A901227C) | Not verified | [Profile](docs/software.md#woodley-ga) |
| **MAGUS** | [2025 CSP170](https://doi.org/10.1038/s43588-025-00775-z) · [2023 MAGUS2023](https://doi.org/10.1093/nsr/nwad128) | [Source](https://zenodo.org/records/14730874) | [Profile](docs/software.md#magus) |
| **MAISE** | [2021 CSP106](https://doi.org/10.1016/j.cpc.2020.107679) | [Source](https://github.com/maise-guide/maise) | [Profile](docs/software.md#maise) |
| **Modified genetic algorithm for molecular crystals (Bazterra–Ferraro–Facelli)** | [2002 CSP015](https://doi.org/10.1063/1.1458547) · [2003 CSP016](https://doi.org/10.1002/qua.10726) | Not verified | [Profile](docs/software.md#bazterra-modified-ga) |
| **MUSE** | [2014 CSP060](https://doi.org/10.1016/j.cpc.2014.03.017) | [Source](https://github.com/zhongliliu/muse) | [Profile](docs/software.md#muse) |
| **ParetoCSP** | [2024 CSP141](https://www.oaepublish.com/articles/jmi.2023.33) | [Source](https://github.com/sadmanomee/ParetoCSP) | [Profile](docs/software.md#paretocsp) |
| **ParetoCSP2** | [2025 CSP175](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792) | [Source](https://github.com/usccolumbia/ParetoCSP2) | [Profile](docs/software.md#paretocsp2) |
| **Periodic real-space genetic algorithm (Abraham–Probert)** | [2006 CSP026](https://doi.org/10.1103/PhysRevB.73.224104) · [2008 CSP037](https://doi.org/10.1103/PhysRevB.77.134117) | Not verified | [Profile](docs/software.md#periodic-ga-abraham-probert) |
| **SPINNER** | [2022 CSP110](https://www.nature.com/articles/s41524-022-00792-w) | [Source](https://github.com/MDIL-SNU/SPINNER) | [Profile](docs/software.md#spinner) |
| **USPEX** | [2006 CSP027](https://doi.org/10.1063/1.2210932) · [2006 CSP030](https://doi.org/10.1016/j.cpc.2006.07.020) · [2010 CSP044](https://doi.org/10.1016/j.cpc.2010.06.007) · [2012 CSP055](https://doi.org/10.1039/C2CE06642D) · [2013 CSP057](https://doi.org/10.1016/j.cpc.2012.12.009) · [2019 CSP085](https://uspex-team.org/static/file/Podryabinkin-2019.pdf) · [2019 USPEXTopology2019](https://doi.org/10.1016/j.cpc.2018.09.016) · [2012 MolecularUSPEX2012](https://doi.org/10.1107/S0108768112017466) | [Access portal](https://uspex-team.org/documentation.html/uspex/downloads) | [Profile](docs/software.md#uspex) |
| **XtalOpt (including r7–14)** | [2011 CSP052](https://doi.org/10.1016/j.cpc.2011.06.003) · [2011 CSP053](https://doi.org/10.1016/j.cpc.2010.07.048) · [2016 CSP069](https://doi.org/10.1016/j.cpc.2015.09.018) · [2017 CSP074](https://doi.org/10.1016/j.cpc.2017.04.001) · [2018 CSP084](https://doi.org/10.1016/j.cpc.2017.09.011) · [2019 CSP091](https://doi.org/10.1016/j.cpc.2018.11.016) · [2024 CSP158](https://doi.org/10.1016/j.cpc.2024.109306) · [2026 CSP196](https://doi.org/10.1016/j.cpc.2025.109910) | [Source](https://github.com/xtalopt/XtalOpt) | [Profile](docs/software.md#xtalopt) |

### Swarm and differential evolution

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **CALYPSO** | [2010 CSP043](https://doi.org/10.1103/PhysRevB.82.094116) · [2012 CSP054](https://doi.org/10.1016/j.cpc.2012.05.008) · [2022 CSP108](https://doi.org/10.1063/5.0074677) | [Access portal](https://download.calypso.cn/home/) | [Profile](docs/software.md#calypso) |
| **CMCrystalHS** | [2021 CMCrystalHS2021](https://doi.org/10.1088/1361-648x/ac1d6c) | [Source](https://github.com/usccolumbia/DE-CSP-highsymmetry) | [Profile](docs/software.md#cmcrystalhs) |
| **IM²ODE** | [2015 CSP064](https://doi.org/10.1016/j.commatsci.2014.10.054) | Not verified | [Profile](docs/software.md#im2ode) |
| **SGO** | [2017 CSP073](https://doi.org/10.1016/j.cpc.2017.05.005) | Not verified | [Profile](docs/software.md#sgo) |

### Energy-landscape exploration

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **Ab initio landscape exploration (Schön et al.)** | [2007 CSP032](https://doi.org/10.1039/B709943F) | Not verified | [Profile](docs/software.md#abinitio-landscape-sch-n) |
| **ChemDASH** | [2020 CSP093](https://doi.org/10.1039/d0cp02206c) · [2022 CSP119](https://doi.org/10.1039/d2cp02180c) | [Source](https://github.com/lrcfmd/ChemDASH) | [Profile](docs/software.md#chemdash) |
| **Conformation-family Monte Carlo (CFMC)** | [2001 CSP010](https://doi.org/10.1073/pnas.231479298) | Not verified | [Profile](docs/software.md#cfmc-crystal) |
| **Diffusion-equation / distance-scaling global optimization** | [1998 CSP005](https://doi.org/10.1021/jp972424u) | Not verified | [Profile](docs/software.md#deds-crystal) |
| **FUSE / FUSE2** | [2018 CSP083](https://doi.org/10.1039/c8fd00045j) · [2025 CSP148](https://doi.org/10.1039/d4fd00094c) | [Source](https://github.com/lrcfmd/FUSE-stable) | [Profile](docs/software.md#fuse) |
| **GRACE (Generation Ranking and Characterization Engine)** | [2008 CSP034](https://doi.org/10.1002/anie.200704247) · [2008 CSP038](https://doi.org/10.1021/jp710575h) · [2019 CSP089](https://doi.org/10.1126/sciadv.aau3338) · [2023 CSP135](https://doi.org/10.1038/s41586-023-06587-3) | [Access portal](https://www.avmatsim.eu/products) | [Profile](docs/software.md#grace-csp) |
| **MC-EMMA** | [2017 CSP070](https://doi.org/10.1038/nature22374) | [Source](https://github.com/lrcfmd/MC-EMMA-stable) | [Profile](docs/software.md#mc-emma) |
| **Minima Hopping (Goedecker-group Python implementation)** | [2004 CSP020](https://doi.org/10.1063/1.1724816) · [2010 CSP042](https://doi.org/10.1063/1.3512900) | [Source](https://gitlab.com/goedeckergroup/ase_mh) | [Profile](docs/software.md#minima-hopping) |
| **Simulation-cell metadynamics (Martonak–Laio–Parrinello)** | [2003 CSP018](https://doi.org/10.1103/PhysRevLett.90.075503) · [2005 CSP025](https://doi.org/10.1524/zkri.220.5.489.65078) | Not verified | [Profile](docs/software.md#cell-metadynamics) |
| **SSW / LASP** | [2013 CSP058](https://doi.org/10.1021/ct301010b) · [2014 CSP062](https://doi.org/10.1039/C4CP01485E) | [Access portal](https://www.lasphub.com/) | [Profile](docs/software.md#ssw-lasp) |

### Adaptive and ML-guided search

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **active-csp** | [2025 CSP162](https://www.nature.com/articles/s41524-025-01523-7) | [Source](https://github.com/stefaanhessmann/active-csp) | [Profile](docs/software.md#active-csp) |
| **AGOX / GOFEE** | [2020 CSP095](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102) · [2022 CSP112](https://arxiv.org/abs/2204.01451) | [Source](https://gitlab.com/agox/agox) | [Profile](docs/software.md#agox-gofee) |
| **AlphaCrystal** | [2023 CSP131](https://pubs.acs.org/doi/10.1021/acsomega.3c02115) | [Source](https://github.com/usccolumbia/AlphaCrystal) | [Profile](docs/software.md#alphacrystal) |
| **AlphaCrystal-II** | [2024 CSP139](https://arxiv.org/abs/2404.04810) | Not verified | [Profile](docs/software.md#alphacrystal-ii) |
| **BOWSR (maml)** | [2021 CSP100](https://www.sciencedirect.com/science/article/pii/S1369702121002984) | [Source](https://github.com/materialyzeai/maml) | [Profile](docs/software.md#bowsr-maml) |
| **CASTING** | [2023 CSP124](https://doi.org/10.1038/s41524-023-01128-y) | [Source](https://github.com/sbanik2/CASTING) | [Profile](docs/software.md#casting) |
| **CRYSPNet** | [2020 CSP094](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802) | [Source](https://github.com/AuroraLHT/cryspnet) | [Profile](docs/software.md#cryspnet) |
| **CrySPY / BO / LAQA** | [2018 CSP075](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803) · [2018 CSP077](https://www.nature.com/articles/s41524-018-0090-y) · [2021 CSP102](https://www.tandfonline.com/doi/full/10.1080/27660400.2021.1943171) · [2022 CSP117](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2055987) · [2022 CSP118](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2059335) | [Source](https://github.com/Tomoki-YAMASHITA/CrySPY) | [Profile](docs/software.md#cryspy-bo-laqa) |
| **CSP-AL (committee active / delta learning)** | [2024 CSP150](https://doi.org/10.1021/acs.jpca.3c07129) | [Source](https://github.com/pwvbutler/CSP-AL) | [Profile](docs/software.md#csp-al-molecular) |
| **GN-OA** | [2022 CSP114](https://www.nature.com/articles/s41467-022-29241-4) | [Access portal](http://www.comates.group/links?software=gn_oa) | [Profile](docs/software.md#gn-oa) |
| **PhaseBO** | [2024 CSP147](https://doi.org/10.1063/5.0180818) | [Source](https://github.com/lrcfmd/PhaseBO) | [Profile](docs/software.md#phasebo) |
| **RL-CSP** | [2023 CSP137](https://doi.org/10.1039/d3dd00063j) | [Source](https://github.com/lrcfmd/rlcsp) | [Profile](docs/software.md#rl-csp) |
| **ShotgunCSP** | [2024 CSP153](https://www.nature.com/articles/s41524-024-01471-8) | [Source](https://github.com/TsumiNa/ShotgunCSP) | [Profile](docs/software.md#shotguncsp) |
| **SPaDe-CSP** | [2025 CSP168](https://doi.org/10.1039/D5DD00304K) | [Source](https://github.com/takuyhaa/SPaDe-CSP) | [Profile](docs/software.md#spade-csp) |
| **Wren (aviary)** | [2022 CSP120](https://www.science.org/doi/10.1126/sciadv.abn4117) | [Source](https://github.com/CompRhys/aviary) | [Profile](docs/software.md#wren-aviary) |

### Learned generation and conditional CSP

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **All-atom Diffusion Transformer (ADiT)** | [2025 CSP163](https://proceedings.mlr.press/v267/joshi25a.html) | [Source](https://github.com/facebookresearch/all-atom-diffusion-transformer) | [Profile](docs/software.md#all-atom-diffusion-transformer-adit) |
| **CCDCGAN** | [2021 CSP101](https://www.nature.com/articles/s41524-021-00526-4) | [Source](https://github.com/TengLong1993/CCDCGAN-for-single-system) | [Profile](docs/software.md#ccdcgan) |
| **CDVAE** | [2022 CSP113](https://arxiv.org/abs/2110.06197) | [Source](https://github.com/txie-93/cdvae) | [Profile](docs/software.md#cdvae) |
| **CellNet (conditional unit-cell flow + packing)** | [2026 CSP188](https://arxiv.org/abs/2610.04193) | [Source](https://github.com/qzhu2017/CellNet-prototype) | [Profile](docs/software.md#cellnet-prototype) |
| **CG-OMatG** | [2026 CSP192](https://arxiv.org/abs/2609.39773) | Not verified | [Profile](docs/software.md#cg-omatg) |
| **Composition-Conditioned Crystal GAN** | [2020 CSP097](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426) | [Source](https://github.com/kaist-amsg/Composition-Conditioned-Crystal-GAN) | [Profile](docs/software.md#composition-conditioned-crystal-gan) |
| **Cond-CDVAE** | [2024 CSP142](https://www.nature.com/articles/s41524-024-01443-y) | [Source](https://github.com/ixsluo/cond-cdvae) | [Profile](docs/software.md#cond-cdvae) |
| **Cond-DFC-VAE / ICSG3D** | [2020 CSP092](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464) | [Source](https://github.com/by256/icsg3d) | [Profile](docs/software.md#cond-dfc-vae-icsg3d) |
| **ContinuouSP** | [2025 CSP166](https://arxiv.org/abs/2502.02026) | [Source](https://github.com/tony998244353/ContinuouSP) | [Profile](docs/software.md#continuousp) |
| **CrysBFN** | [2025 CSP160](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html) | [Source](https://github.com/wu-han-lin/CrysBFN) | [Profile](docs/software.md#crysbfn) |
| **Crystal-GFN** | [2023 CSP130](https://arxiv.org/abs/2310.04925v2) | [Source](https://github.com/alexhernandezgarcia/gflownet) | [Profile](docs/software.md#crystal-gfn) |
| **CrystalFlow** | [2025 CSP169](https://www.nature.com/articles/s41467-025-64364-4) | [Source](https://github.com/ixsluo/CrystalFlow) | [Profile](docs/software.md#crystalflow) |
| **CrystalFormer** | [2025 CSP177](https://doi.org/10.1016/j.scib.2025.09.035) · [2025 CrystalFormerCSP2025](https://arxiv.org/abs/2512.18251) | [Source](https://github.com/deepmodeling/CrystalFormer) | [Profile](docs/software.md#crystalformer) |
| **CrystalGAN** | [2019 CSP086](https://ceur-ws.org/Vol-2350/paper18.pdf) | [Source](https://github.com/asmanouira/CrystalGAN) | [Profile](docs/software.md#crystalgan) |
| **CrystalGRPO** | [2026 CSP182](https://arxiv.org/abs/2608.06582) | Not verified | [Profile](docs/software.md#crystalgrpo) |
| **CrystalGRW** | [2026 CSP183](https://www.nature.com/articles/s41598-026-62470-x) | [Source](https://github.com/trachote/crystalgrw) | [Profile](docs/software.md#crystalgrw) |
| **Crystalite** | [2026 CSP184](https://arxiv.org/abs/2604.02270) | [Source](https://github.com/joshrosie/crystalite) | [Profile](docs/software.md#crystalite) |
| **CrystaLLM** | [2024 CSP140](https://doi.org/10.1038/s41467-024-54639-7) | [Source](https://github.com/lantunes/CrystaLLM) | [Profile](docs/software.md#crystallm) |
| **CubicGAN** | [2021 CSP105](https://doi.org/10.1002/advs.202100566) | [Source](https://github.com/MilesZhao/CubicGAN) | [Profile](docs/software.md#cubicgan) |
| **DAO** | [2026 CSP193](https://www.nature.com/articles/s41467-026-72362-3) | [Source](https://github.com/GLAD-RUC/DAO) | [Profile](docs/software.md#dao) |
| **DD3DCS / Encoding-Decoding 3D Crystals** | [2019 CSP087](https://arxiv.org/abs/1909.00949) | [Source](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals) | [Profile](docs/software.md#dd3dcs-encoding-decoding-3d-crystals) |
| **DeepCSP (organic conditional GAN + GCN)** | [2024 CSP151](https://doi.org/10.1016/j.xinn.2023.100562) | [Access portal](https://sites.google.com/view/yezhuyifan/) | [Profile](docs/software.md#deepcsp-organic-gan) |
| **DiffCSP** | [2023 CSP128](https://arxiv.org/abs/2309.04475) | [Source](https://github.com/jiaor17/DiffCSP) | [Profile](docs/software.md#diffcsp) |
| **DiffCSP++** | [2024 CSP154](https://arxiv.org/abs/2402.03992) | [Source](https://github.com/jiaor17/DiffCSP-PP) | [Profile](docs/software.md#diffcsp-plus-plus) |
| **DP-CDVAE** | [2024 CSP143](https://www.nature.com/articles/s41598-024-51400-4) | [Source](https://github.com/trachote/dp-cdvae) | [Profile](docs/software.md#dp-cdvae) |
| **EquiCSP** | [2024 CSP144](https://proceedings.mlr.press/v235/lin24b.html) | [Source](https://github.com/EmperorJia/EquiCSP) | [Profile](docs/software.md#equicsp) |
| **FlowMM / FlowLLM** | [2024 CSP145](https://arxiv.org/abs/2410.23405) · [2024 CSP146](https://proceedings.mlr.press/v235/miller24a.html) | [Source](https://github.com/facebookresearch/flowmm) | [Profile](docs/software.md#flowmm-flowllm) |
| **FTCP** | [2022 CSP111](https://doi.org/10.1016/j.matt.2021.11.032) | [Source](https://github.com/PV-Lab/FTCP) | [Profile](docs/software.md#ftcp) |
| **GemsDiff** | [2024 CSP157](https://ojs.aaai.org/index.php/AAAI/article/view/30224) | [Source](https://github.com/aklipf/gemsdiff) | [Profile](docs/software.md#gemsdiff) |
| **iMatGen** | [2019 CSP088](https://doi.org/10.1016/j.matt.2019.08.017) | [Source](https://github.com/kaist-amsg/imatgen) | [Profile](docs/software.md#imatgen) |
| **KLDM** | [2025 CSP172](https://proceedings.mlr.press/v267/cornet25a.html) | [Source](https://github.com/frcnt/kldm) | [Profile](docs/software.md#kldm) |
| **Mat2Seq (AIRS)** | [2024 CSP149](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html) | [Source](https://github.com/divelab/AIRS/tree/main/OpenMat/Mat2Seq) | [Profile](docs/software.md#mat2seq-airs) |
| **MatterGen** | [2025 CSP159](https://www.nature.com/articles/s41586-025-08628-5) | [Source](https://github.com/microsoft/mattergen) | [Profile](docs/software.md#mattergen) |
| **NextCrystal** | [2026 CSP189](https://arxiv.org/abs/2602.17176v4) | Not verified | [Profile](docs/software.md#nextcrystal) |
| **OMatG** | [2025 CSP173](https://proceedings.mlr.press/v267/hollmer25a.html) | [Source](https://github.com/FERMat-ML/OMatG) | [Profile](docs/software.md#omatg) |
| **OXtal** | [2025 CSP174](https://arxiv.org/abs/2512.06987) | [Source](https://github.com/OXtal/OXtal) | [Profile](docs/software.md#oxtal) |
| **PackFlow** | [2026 CSP191](https://arxiv.org/abs/2602.20140) | [Source](https://github.com/learningmatter-mit/packflow) | [Profile](docs/software.md#packflow-molecular) |
| **PGCGM** | [2023 CSP134](https://www.nature.com/articles/s41524-023-00987-9) | [Source](https://github.com/MilesZhao/PGCGM) | [Profile](docs/software.md#pgcgm) |
| **SHAFT** | [2026 CSP187](https://arxiv.org/abs/2411.04323) | [Source](https://github.com/ngminhtri0394/SHAFT) | [Profile](docs/software.md#shaft) |
| **SLICES** | [2023 CSP126](https://www.nature.com/articles/s41467-023-42870-7) | [Source](https://github.com/xiaohang007/SLICES) | [Profile](docs/software.md#slices) |
| **SyMat (AIRS)** | [2023 CSP138](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html) | [Source](https://github.com/divelab/AIRS/tree/main/OpenMat/SyMat) | [Profile](docs/software.md#symat-airs) |
| **SymmCD** | [2025 CSP178](https://arxiv.org/abs/2502.03638) | [Source](https://github.com/sibasmarak/SymmCD) | [Profile](docs/software.md#symmcd) |
| **uFlowCSP** | [2026 CSP195](https://arxiv.org/abs/2609.09799) | [Source](https://github.com/usccolumbia/uFlowCSP) | [Profile](docs/software.md#uflowcsp) |
| **Uni-3DAR** | [2025 CSP179](https://arxiv.org/abs/2503.16278v1) | [Source](https://github.com/dptech-corp/Uni-3DAR) | [Profile](docs/software.md#uni-3dar) |
| **UniMat** | [2024 CSP152](https://arxiv.org/abs/2311.09235) | [Access portal](https://unified-materials.github.io/unimat/) | [Profile](docs/software.md#unimat) |

### Context, evaluators and evaluation

| Algorithm / component | Papers | Code or access | Details |
|---|---|---|---|
| **CHGNet** | [2023 CSP127](https://www.nature.com/articles/s42256-023-00716-3) | [Source](https://github.com/CederGroupHub/chgnet) | [Profile](docs/software.md#chgnet) |
| **Composition-based symmetry prediction** | [2021 CompositionSymmetry2021](https://doi.org/10.1016/j.commatsci.2021.110686) | [Source](https://github.com/Yuxinya/SG_predict) | [Profile](docs/software.md#composition-symmetry) |
| **CrystalOptimizer / CSO-FM** | [2011 CSP049](https://doi.org/10.1021/ct100597e) | [Access portal](https://sargentcentre.org/impact/spinouts-software/) | [Profile](docs/software.md#crystaloptimizer) |
| **CSP-MACE-Å** | [2026 CSP186](https://arxiv.org/abs/2605.28905) | Not verified | [Profile](docs/software.md#csp-mace-a) |
| **CSPMetrics** | [2024 CSPMetrics2024](https://doi.org/10.1016/j.commatsci.2024.112802) | [Source](https://github.com/usccolumbia/CSPBenchMetrics) | [Profile](docs/software.md#cspmetrics) |
| **Deep free energy (DF) CSP** | [2026 CSP181](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7) | Not verified | [Profile](docs/software.md#deep-free-energy-df-csp) |
| **Disordered-structure NNP training (Hong et al.)** | [2020 CSP099](https://arxiv.org/abs/2008.07786) | Not verified | [Profile](docs/software.md#disordered-structure-nnp-training-hong-et-al) |
| **M3GNet** | [2022 CSP109](https://www.nature.com/articles/s43588-022-00349-3) | [Source](https://github.com/materialyzeai/m3gnet) | [Profile](docs/software.md#m3gnet) |
| **MLatticeABC** | [2021 MLatticeABC2021](https://doi.org/10.1021/acsomega.1c00781) | [Source](https://github.com/usccolumbia/MLatticeABC) | [Profile](docs/software.md#mlatticeabc) |
| **MolXtalNet-D / MolXtalNet-S (MXtalTools)** | [2023 CSP132](https://doi.org/10.1021/acs.jctc.3c00031) | [Source](https://github.com/InfluenceFunctional/MXtalTools) | [Profile](docs/software.md#molxtalnet-mxtaltools) |
| **OpenCSP (crystal prediction)** | [2026 CSP190](https://www.nature.com/articles/s41524-026-02180-0) | [Access portal](https://www.nature.com/articles/s41524-026-02180-0) | [Profile](docs/software.md#opencsp-crystal-prediction) |

## Benchmarks and evaluation

| Resource | Role | Paper and release |
|---|---|---|
| **MP-20** | Training / validation / test dataset | [2022 CSP113](https://arxiv.org/abs/2110.06197) · [Release / code](https://github.com/txie-93/cdvae/tree/f857f598d6f6cca5dc1ea0582d228f12dcc2c2ea/data/mp_20) |
| **MPTS-52** | Chronological training / validation / test dataset | [2024 MatbenchGenmetrics2024](https://doi.org/10.21105/joss.05618) · [2023 CSP128](https://arxiv.org/abs/2309.04475) · [Release / code](https://github.com/jiaor17/DiffCSP/tree/7121d159826efa2ba9500bf299250d96da37f146/data/mpts_52) |
| **CSPBench** | Cross-method benchmark study | [2026 CSP180](https://doi.org/10.1002/aidi.70162) · [Release / code](https://github.com/usccolumbia/cspbenchmark/tree/6e2eee244f434e2010fa4f9d3a08e2c054242a47) |
| **T180** | Versioned test cohort | [2026 CSP185](https://arxiv.org/abs/2609.26502v1) · [Release / code](https://github.com/usccolumbia/benchmark_deep_csp/tree/320b7289e70b61f9d8d51d7fe7dae3e074f75522/data/testsets/v3.1/T180) |
| **T46** | Versioned test cohort | [2026 CSP185](https://arxiv.org/abs/2609.26502v1) · [Release / code](https://github.com/usccolumbia/benchmark_deep_csp/tree/320b7289e70b61f9d8d51d7fe7dae3e074f75522/data/testsets/v3.1/T46) |
| **CSPMetrics / CSPBenchMetrics** | Evaluation metric package | [2024 CSPMetrics2024](https://doi.org/10.1016/j.commatsci.2024.112802) · [Release / code](https://github.com/usccolumbia/CSPBenchMetrics) |

**MPTS-52** is the correct spelling (sometimes transposed as MPST-52); 52 is an atom-count limit. **T180** and **T46** are versioned test cohorts. **CSPMetrics/CSPBenchMetrics** is a metric toolkit. Historical CSPBench targets and later T180 releases must be compared by their manifests, not by the shared number 180. See [protocol notes](docs/benchmarks.md).

## How to interpret availability

- A public repository is not automatically open-source licensed; license evidence is a separate field.
- A checkpoint for a relaxation evaluator is different from a generator checkpoint. Classical algorithms can have no pretrained model by design.
- Formula prompting, reduced-formula matching, and exact per-element cell-count preservation are different capabilities.
- Paper-reported results, source inspection, and successful runtime reproduction are different evidence levels. This collection does not claim independent execution of the algorithms.
- Each entry retains dated sources. Upstream links and releases may change.

## Citation and license

Cite the original papers for the methods and datasets you use. This directory provides [BibTeX](references.bib) and a [repository citation](CITATION.cff); the companion survey is in preparation and has no assigned DOI here.

Repository-authored curation and tooling are under [MIT](LICENSE), matching the related prototype collection. Linked papers, software, models, and datasets retain their own licenses.
