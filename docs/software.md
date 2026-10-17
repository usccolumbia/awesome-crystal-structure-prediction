# Software, model and data profiles

Availability is recorded separately from license status and runtime validation. A missing release is marked unknown rather than inferred absent.

<a id="abinitio-landscape-sch-n"></a>
## Ab initio landscape exploration (Schön et al.)

**Energy-landscape exploration · Atomic / inorganic · Algorithm described in paper; source not verified**

[2007 CSP032](https://doi.org/10.1039/B709943F)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1039/B709943F)

<a id="active-csp"></a>
## active-csp

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2025 CSP162](https://www.nature.com/articles/s41524-025-01523-7)

**Source / access:** [Code](https://github.com/stefaanhessmann/active-csp) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/stefaanhessmann/active-csp/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [active-csp iterative DFT reference configurations](https://github.com/stefaanhessmann/active-csp) — Main model training. On-the-fly reference calculations and neural-network retraining; exact per-system release/split not verified

**Reference data:**
No separate item verified.

**Evaluation:**
- [Si16, Na8Cl8, Ga8As8, Al4O6; transfer to Si46/Al16O24](https://www.nature.com/articles/s41524-025-01523-7) — Active learning global-minimum search. Random/BO/LAQA baselines; original paper candidate pools and DFT validation; larger systems test transfer

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-025-01523-7) · [source 2](https://github.com/stefaanhessmann/active-csp) · [source 3](https://github.com/stefaanhessmann/active-csp/blob/main/LICENSE) · [source 4](https://github.com/stefaanhessmann/active-csp/blob/main/README.md)

<a id="aga"></a>
## Adaptive Genetic Algorithm (AGA; Wang–Ho collaboration)

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2014 CSP059](https://doi.org/10.1088/0953-8984/26/3/035402)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary method and official lab page identify AGA. Public source distribution was not verified. A historical author manual copied on cailiaoren describes author-request/EULA access, but an official current distribution endpoint was not established, so no current access claim is made.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/1309.4742) · [source 2](https://www.ameslab.gov/machine-learning-accelerated-materials-discovery-center/research) · [source 3](https://doi.org/10.1088/0953-8984/26/3/035402)

<a id="agox-gofee"></a>
## AGOX / GOFEE

**Adaptive and ML-guided search · Surfaces / clusters (adjacent) · Adjacent method**

[2020 CSP095](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102) · [2022 CSP112](https://arxiv.org/abs/2204.01451)

**Source / access:** [Code](https://gitlab.com/agox/agox) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://gitlab.com/agox/agox/-/blob/dev/README.md#license)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [GOFEE on-the-fly first-principles structure energies](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102) — Main model training. Gaussian-process surrogate fitted actively during search; no fixed offline corpus

**Reference data:**
No separate item verified.

**Evaluation:**
- [Surface reconstructions; graphene/Ir(111) edge oxidation and oxygen intercalation](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102) — Surrogate-assisted global optimization. Compare first-principles evolutionary search and GOFEE; original paper protocol, not all AGOX versions

AGOX includes a GOFEE implementation; this links the publicly documented later framework, not a claim that it is the original 2020 release. Multiple global optimization families are implemented.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.086102) · [source 2](https://arxiv.org/abs/2204.01451) · [source 3](https://gitlab.com/agox/agox) · [source 4](https://agox.gitlab.io/agox/) · [source 5](https://gitlab.com/agox/agox/-/blob/dev/README.md#license)

<a id="airss"></a>
## AIRSS / buildcell

**Random structure search · Atomic / inorganic · CSP search / proposal implementation**

[2006 CSP028](https://doi.org/10.1103/PhysRevLett.97.045504) · [2025 CSP165](https://doi.org/10.1039/D4FD00134F)

**Source / access:** [Code](https://www.mtg.msm.cam.ac.uk/Codes/AIRSS) — Source download

**License:** Open-source license verified [GPL-2.0](https://airss-docs.github.io/#licence-and-citation)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [High-pressure silane SiH4](https://doi.org/10.1103/PhysRevLett.97.045504) — Low-enthalpy structure discovery. Original 2006 paper random initial configurations; demonstrated cells up to at least 10 atoms. Later AIRSS uses not generalized to this protocol.

Developer university page explicitly provides full-source downloads and links historical versions. Hot random search and datum-derived structures are associated later workflows; the page source download does not by itself verify availability of every paper-specific component.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.mtg.msm.cam.ac.uk/Codes/AIRSS) · [source 2](https://airss-docs.github.io/) · [source 3](https://airss-docs.github.io/getting-started/installation/) · [source 4](https://arxiv.org/abs/1101.3987) · [source 5](https://airss-docs.github.io/#licence-and-citation) · [source 6](https://doi.org/10.1103/PhysRevLett.97.045504) · [source 7](https://doi.org/10.1039/D4FD00134F)

<a id="all-atom-diffusion-transformer-adit"></a>
## All-atom Diffusion Transformer (ADiT)

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2025 CSP163](https://proceedings.mlr.press/v267/joshi25a.html)

**Source / access:** [Code](https://github.com/facebookresearch/all-atom-diffusion-transformer) — Public source repository

**License:** Restrictive / noncommercial source license [CC-BY-NC-4.0](https://github.com/facebookresearch/all-atom-diffusion-transformer/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://huggingface.co/chaitjo/all-atom-diffusion-transformer) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP20 ADiT processed corpus](https://huggingface.co/datasets/chaitjo/MP20_ADiT) — Main model training. Repository train/eval pipelines support these corpora; released joint QM9+MP20 weights are independent reproduction, may differ from final paper models.
- [QM9 ADiT processed corpus](https://huggingface.co/datasets/chaitjo/QM9_ADiT) — Main model training. Repository train/eval pipelines support these corpora; released joint QM9+MP20 weights are independent reproduction, may differ from final paper models.
- [GEOM-DRUGS ADiT processed corpus](https://huggingface.co/datasets/chaitjo/GEOM-DRUGS_ADiT) — Main model training. Repository train/eval pipelines support these corpora; released joint QM9+MP20 weights are independent reproduction, may differ from final paper models.
- [QMOF150 ADiT processed corpus](https://huggingface.co/datasets/chaitjo/QMOF150_ADiT) — Main model training. Repository train/eval pipelines support these corpora; released joint QM9+MP20 weights are independent reproduction, may differ from final paper models.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP20 ADiT](https://huggingface.co/datasets/chaitjo/MP20_ADiT) — Autoencoder reconstruction and latent diffusion generation across molecules/materials. Author train scripts compute validation metrics; eval_autoencoder/eval_diffusion configs. Crystal/molecular metrics and exact-paper versus reproduced weights must remain distinct.
- [QM9 ADiT](https://huggingface.co/datasets/chaitjo/QM9_ADiT) — Autoencoder reconstruction and latent diffusion generation across molecules/materials. Author train scripts compute validation metrics; eval_autoencoder/eval_diffusion configs. Crystal/molecular metrics and exact-paper versus reproduced weights must remain distinct.
- [GEOM-DRUGS ADiT](https://huggingface.co/datasets/chaitjo/GEOM-DRUGS_ADiT) — Autoencoder reconstruction and latent diffusion generation across molecules/materials. Author train scripts compute validation metrics; eval_autoencoder/eval_diffusion configs. Crystal/molecular metrics and exact-paper versus reproduced weights must remain distinct.
- [QMOF150 ADiT](https://huggingface.co/datasets/chaitjo/QMOF150_ADiT) — Autoencoder reconstruction and latent diffusion generation across molecules/materials. Author train scripts compute validation metrics; eval_autoencoder/eval_diffusion configs. Crystal/molecular metrics and exact-paper versus reproduced weights must remain distinct.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://proceedings.mlr.press/v267/joshi25a.html) · [source 2](https://github.com/facebookresearch/all-atom-diffusion-transformer) · [source 3](https://github.com/facebookresearch/all-atom-diffusion-transformer/blob/main/README.md) · [source 4](https://github.com/facebookresearch/all-atom-diffusion-transformer/blob/main/LICENSE) · [source 5](https://huggingface.co/chaitjo/all-atom-diffusion-transformer)

<a id="alphacrystal"></a>
## AlphaCrystal

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2023 CSP131](https://pubs.acs.org/doi/10.1021/acsomega.3c02115)

**Source / access:** [Code](https://github.com/usccolumbia/AlphaCrystal) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/usccolumbia/AlphaCrystal/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [AlphaCrystal 12-atom contact-map model (.h5)](https://figshare.com/articles/software/Deep_learning_model_file_for_AlphaCrystal_For_structure_prediction_of_crystal_materials_with_12_atoms/23488214) — Main model / Public download

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author README explicitly cites the ACS Omega contact-map paper.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pubs.acs.org/doi/10.1021/acsomega.3c02115) · [source 2](https://github.com/usccolumbia/AlphaCrystal) · [source 3](https://github.com/usccolumbia/AlphaCrystal/blob/main/LICENSE) · [source 4](https://figshare.com/articles/software/Deep_learning_model_file_for_AlphaCrystal_For_structure_prediction_of_crystal_materials_with_12_atoms/23488214) · [source 5](https://github.com/usccolumbia/AlphaCrystal/blob/main/README.md)

<a id="alphacrystal-ii"></a>
## AlphaCrystal-II

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2024 CSP139](https://arxiv.org/abs/2404.04810)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary preprint was checked and targeted official-code searches found no verified paper-specific release. AlphaCrystal is a different earlier contact-map model and is not substituted for the distance-matrix method.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2404.04810)

<a id="bowsr-maml"></a>
## BOWSR (maml)

**Adaptive and ML-guided search · Atomic / inorganic · Adjacent method**

[2021 CSP100](https://www.sciencedirect.com/science/article/pii/S1369702121002984)

**Source / access:** [Code](https://github.com/materialyzeai/maml) — Public source repository

**License:** Open-source license verified [BSD-3-Clause](https://github.com/materialyzeai/maml/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Publisher code availability links the former materialsvirtuallab/maml repository; current project uses materialyzeai/maml. Symmetry-constrained structural relaxation is an enabling component, not a complete global CSP search.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.sciencedirect.com/science/article/pii/S1369702121002984) · [source 2](https://github.com/materialyzeai/maml) · [source 3](https://github.com/materialyzeai/maml/blob/main/LICENSE) · [source 4](https://github.com/materialyzeai/maml/blob/main/README.md)

<a id="calypso"></a>
## CALYPSO

**Swarm and differential evolution · Atomic / inorganic · CSP search / proposal implementation**

[2010 CSP043](https://doi.org/10.1103/PhysRevB.82.094116) · [2012 CSP054](https://doi.org/10.1016/j.cpc.2012.05.008)

**Source / access:** [Project](https://download.calypso.cn/home/) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Elemental, binary and ternary known crystal systems](https://doi.org/10.1103/PhysRevB.82.094116) — Particle-swarm structure recovery. Original CALYPSO paper reports recovery over metallic, ionic and covalent systems; exact named-system manifest not recovered from abstract

Official distribution and manual describe licensed registration/request access and binary releases. No public source-code repository was verified. CALYPSO-Python documentation is separate from evidence that the full CSP source is publicly downloadable.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://download.calypso.cn/home/) · [source 2](https://download.calypso.cn/releasenotes/) · [source 3](https://www.calypso.cn/static/web/documentation/CALYPSO_Manual_English.pdf) · [source 4](https://doi.org/10.1103/PhysRevB.82.094116) · [source 5](https://doi.org/10.1016/j.cpc.2012.05.008)

<a id="casting"></a>
## CASTING

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2023 CSP124](https://doi.org/10.1038/s41524-023-01128-y)

**Source / access:** [Code](https://github.com/sbanik2/CASTING) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/sbanik2/CASTING/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author implementation linked by the primary paper or repository; no software execution was performed.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1038/s41524-023-01128-y) · [source 2](https://github.com/sbanik2/CASTING) · [source 3](https://github.com/sbanik2/CASTING/blob/main/LICENSE) · [source 4](https://github.com/sbanik2/CASTING/blob/main/README.md)

<a id="ccdcgan"></a>
## CCDCGAN

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2021 CSP101](https://www.nature.com/articles/s41524-021-00526-4)

**Source / access:** [Code](https://github.com/TengLong1993/CCDCGAN-for-single-system) — Public source repository

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [DFT Bi-Se prototype-substitution corpus](https://github.com/TengLong1993/CCDCGAN-for-single-system) — Main model training. Paper: 10981 binary prototypes, <=20 atoms and maximum lattice constant <10 angstrom; 9810 converged Bi/Se substituted DFT structures form training database. MP known phases alone are not training corpus.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Bi-Se known-phase recovery and generated candidates](https://www.nature.com/articles/s41524-021-00526-4) — Restricted-system inverse crystal design. Paper Bi-Se energy-directed generation and DFT assessment; not standard MP-20.

Author README explicitly cites the 2021 paper and provides the Bi-Se single-system implementation.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-021-00526-4) · [source 2](https://github.com/TengLong1993/CCDCGAN-for-single-system) · [source 3](https://github.com/TengLong1993/CCDCGAN-for-single-system/blob/main/README.md)

<a id="cdvae"></a>
## CDVAE

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2022 CSP113](https://arxiv.org/abs/2110.06197)

**Source / access:** [Code](https://github.com/txie-93/cdvae) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/txie-93/cdvae/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Author implementation linked by the primary paper or repository; no software execution was performed.

CDVAE author repository releases train/validation/test CSVs for Perov-5, Carbon-24 and MP-20; reconstruction, generation and latent property optimization are separate experiments. Carbon source is AIRSS at 10 GPa; Perov-5 is a curated cubic-perovskite corpus.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2110.06197) · [source 2](https://github.com/txie-93/cdvae) · [source 3](https://github.com/txie-93/cdvae/blob/main/README.md) · [source 4](https://github.com/txie-93/cdvae/blob/main/LICENSE)

<a id="cellnet-prototype"></a>
## CellNet (conditional unit-cell flow + packing)

**Learned generation and conditional CSP · Molecular / organic · Method**

[2026 CSP188](https://arxiv.org/abs/2610.04193)

**Source / access:** [Code](https://github.com/qzhu2017/CellNet-prototype) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/qzhu2017/CellNet-prototype/main/LICENSE)

**Pretrained model:** Public pretrained download
- [CellNet best.pt checkpoint](https://github.com/qzhu2017/CellNet-prototype/tree/main/checkpoints/cellnet_flow) — Main model / Public download

**Training data:**
- [SPaDe-CSP-derived CellNet training tables](https://github.com/qzhu2017/CellNet-prototype/tree/main/datasets) — Main model training. spade_train.csv; rebuild script provided; experimental benchmark codes kept in benchmark directory

**Reference data:**
No separate item verified.

**Evaluation:**
- [Zhu & Hattori 84-system single-component molecular CSP test](https://github.com/qzhu2017/CellNet-prototype/tree/main/benchmark) — Molecular crystal packing recovery. 84 single-component systems with Z-prime <=1; per-code run scripts and results.csv; supplied author protocol

Paper Code availability explicitly names CellNet-prototype. Conditional lattice flow followed by cell reconstruction and quasi-random molecular packing; demonstrated with supplied Hall setting and Z-prime. Reference CSD structures remain license-controlled.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/html/2610.04193v1) · [source 2](https://github.com/qzhu2017/CellNet-prototype) · [source 3](https://arxiv.org/abs/2610.04193) · [source 4](https://raw.githubusercontent.com/qzhu2017/CellNet-prototype/main/README.md) · [source 5](https://raw.githubusercontent.com/qzhu2017/CellNet-prototype/main/LICENSE) · [source 6](https://github.com/qzhu2017/CellNet-prototype/tree/main/checkpoints/cellnet_flow)

<a id="cg-omatg"></a>
## CG-OMatG

**Learned generation and conditional CSP · Molecular / organic · Method**

[2026 CSP192](https://arxiv.org/abs/2609.39773)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Open Molecular Crystals OMC25 subset](https://arxiv.org/abs/2609.39773) — Main model training. CG-OMatG training subset; exact split not established from primary abstract
- [CSD molecular-crystal subset](https://www.ccdc.cam.ac.uk/solutions/software/csd/) — Main model training. CG-OMatG subset; reinforcement-learning low-energy fine-tuning separate

**Reference data:**
No separate item verified.

**Evaluation:**
- [CSP blind-test crystal structures](https://arxiv.org/abs/2609.39773) — Conditional molecular-crystal generation. COMPACK packing similarity to experimental crystals; exact blind-test cohort/split not established from abstract

Primary preprint verifies rigid-body Riemannian flow plus RL identity. Its HTML did not provide an authors’ implementation URL, and exact-model/GitHub searches did not verify a public repository. Generic flow-GRPO reference code is not CG-OMatG source.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/html/2609.39773v1) · [source 2](https://arxiv.org/abs/2609.39773)

<a id="chemdash"></a>
## ChemDASH

**Energy-landscape exploration · Atomic / inorganic · CSP search / proposal implementation**

[2020 CSP093](https://doi.org/10.1039/d0cp02206c) · [2022 CSP119](https://doi.org/10.1039/d2cp02180c)

**Source / access:** [Code](https://github.com/lrcfmd/ChemDASH) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/lrcfmd/ChemDASH/blob/master/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author repository cites the 2020 paper and explains chemistry-directed swaps. Variable-composition extension has its own author-group repository: https://github.com/lrcfmd/vc-ChemDASH.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/lrcfmd/ChemDASH) · [source 2](https://github.com/lrcfmd/vc-ChemDASH) · [source 3](https://github.com/lrcfmd) · [source 4](https://github.com/lrcfmd/ChemDASH/blob/master/LICENSE) · [source 5](https://github.com/lrcfmd/ChemDASH/blob/master/README.md) · [source 6](https://doi.org/10.1039/d0cp02206c) · [source 7](https://doi.org/10.1039/d2cp02180c)

<a id="chgnet"></a>
## CHGNet

**Context, evaluators and evaluation · Atomic / inorganic · Enabling evaluator**

[2023 CSP127](https://www.nature.com/articles/s42256-023-00716-3)

**Source / access:** [Code](https://github.com/CederGroupHub/chgnet) — Public source repository

**License:** Open-source license verified [BSD-3-Clause-LBNL](https://github.com/CederGroupHub/chgnet/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [CHGNet 0.3.0 packaged checkpoint](https://github.com/CederGroupHub/chgnet/blob/main/chgnet/pretrained/0.3.0/README.md) — Main model / Public download

**Training data:**
- [Materials Project trajectory (MPtrj)](https://figshare.com/articles/dataset/Materials_Project_Trjectory_MPtrj_Dataset/23713842) — Main model training. September 2022 MP GGA/GGA+U; default 0.3.0 versus original 0.2.0 checkpoints distinguished; exact paper split not verified

**Reference data:**
No separate item verified.

**Evaluation:**
- [Matbench Discovery](https://matbench-discovery.materialsproject.org) — Stability prediction from unrelaxed structures. README links benchmark; leaderboard model version and protocol must be checked before comparison

Enabling interatomic potential / relaxation evaluator, not a candidate-generation algorithm.

This canonical record is the learned CHGNet potential itself, so MPtrj is main-model training. When used by an outer search it is an evaluator component. r2SCAN transfer model and MatPES/MatGL successors are separate checkpoints, not assumed identical training.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s42256-023-00716-3) · [source 2](https://github.com/CederGroupHub/chgnet) · [source 3](https://github.com/CederGroupHub/chgnet/blob/main/LICENSE) · [source 4](https://github.com/CederGroupHub/chgnet/blob/main/chgnet/pretrained/0.3.0/README.md) · [source 5](https://github.com/CederGroupHub/chgnet/blob/main/README.md) · [source 6](https://github.com/spdx/license-list-data/blob/main/json/details/BSD-3-Clause-LBNL.json)

<a id="cmcrystal"></a>
## CMCrystal

**Evolutionary and genetic search · Atomic / inorganic · Method**

[2021 CMCrystal2021](https://doi.org/10.1039/d0ce01714k)

**Source / access:** [Code](https://github.com/usccolumbia/cmcrystal) — Public source repository

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/usccolumbia/cmcrystal/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

Contact-map reconstruction comparing global optimization algorithms. Reconstruction requires supplied structural constraints.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1039/d0ce01714k) · [source 2](https://github.com/usccolumbia/cmcrystal/blob/main/README.md)

<a id="cmcrystalhs"></a>
## CMCrystalHS

**Swarm and differential evolution · Atomic / inorganic · Method**

[2021 CMCrystalHS2021](https://doi.org/10.1088/1361-648x/ac1d6c)

**Source / access:** [Code](https://github.com/usccolumbia/DE-CSP-highsymmetry) — Public source repository

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/usccolumbia/DE-CSP-highsymmetry/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

PyXtal-compatible Wyckoff assignments followed by differential evolution of free coordinates. Reconstruction requires supplied structural constraints.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1088/1361-648x/ac1d6c) · [source 2](https://github.com/usccolumbia/DE-CSP-highsymmetry/blob/main/README.md)

<a id="cmcrystalmoo"></a>
## CMCrystalMOO / MOOCSP

**Evolutionary and genetic search · Atomic / inorganic · Method**

[2022 CMCrystalMOO2022](https://doi.org/10.1021/acs.jpca.1c07170)

**Source / access:** [Code](https://github.com/usccolumbia/MOOCSP) — Public source repository

**License:** Open-source license verified [Apache-2.0](https://github.com/usccolumbia/MOOCSP/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/usccolumbia/MOOCSP/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

Multiobjective reconstruction using contact agreement, coordination agreement and individual age. Reconstruction requires supplied structural constraints.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1021/acs.jpca.1c07170) · [source 2](https://github.com/usccolumbia/MOOCSP/blob/main/README.md)

<a id="composition-symmetry"></a>
## Composition-based symmetry prediction

**Context, evaluators and evaluation · Atomic / inorganic · Enabling predictor / evaluation**

[2021 CompositionSymmetry2021](https://doi.org/10.1016/j.commatsci.2021.110686)

**Source / access:** [Code](https://github.com/Yuxinya/SG_predict) — Public source repository

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Materials Project-derived descriptor dataset](https://figshare.com/s/9cfe81a3b087618353c8) — Main model training. See author README for feature files and split

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/Yuxinya/SG_predict/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

Random-forest crystal-system and space-group classification from enhanced composition descriptors. Component accuracy is not complete CSP recovery.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1016/j.commatsci.2021.110686) · [source 2](https://github.com/Yuxinya/SG_predict/blob/main/README.md)

<a id="composition-conditioned-crystal-gan"></a>
## Composition-Conditioned Crystal GAN

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2020 CSP097](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426)

**Source / access:** [Code](https://github.com/kaist-amsg/Composition-Conditioned-Crystal-GAN) — Public source repository

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Augmented Mg-Mn-O crystal corpus](https://figshare.com/s/0dce6bb830ae1e392206) — Main model training. Restricted Mg-Mn-O chemical system; author provides augmentation recipe and mgmno_2000.pickle (2000 examples per composition).

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official named author lab repository; restricted chemical-system implementation. Formula-conditioning capability is documented separately in the map audit.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426) · [source 2](https://github.com/kaist-amsg/Composition-Conditioned-Crystal-GAN) · [source 3](https://github.com/kaist-amsg/Composition-Conditioned-Crystal-GAN/blob/master/README.md)

<a id="cond-cdvae"></a>
## Cond-CDVAE

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP142](https://www.nature.com/articles/s41524-024-01443-y)

**Source / access:** [Code](https://github.com/ixsluo/cond-cdvae) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/ixsluo/cond-cdvae/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Cond-CDVAE-4M checkpoint release](https://github.com/ixsluo/cond-cdvae/releases/tag/v1.0.0) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP60-CALYPSO](https://github.com/ixsluo/cond-cdvae/tree/main/data) — Main model training. 4M and 86M model recipes use conf/data/caly-mp/230617/mp60-B-SiO2+calyhalf2.yaml; MP crystals and CALYPSO local minima; pressure conditioning.

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-024-01443-y) · [source 2](https://github.com/ixsluo/cond-cdvae) · [source 3](https://github.com/ixsluo/cond-cdvae/blob/main/README.md) · [source 4](https://github.com/ixsluo/cond-cdvae/blob/main/LICENSE) · [source 5](https://github.com/ixsluo/cond-cdvae/releases/tag/v1.0.0)

<a id="cond-dfc-vae-icsg3d"></a>
## Cond-DFC-VAE / ICSG3D

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2020 CSP092](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464)

**Source / access:** [Code](https://github.com/by256/icsg3d) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/by256/icsg3d/blob/master/LICENSE)

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://github.com/by256/icsg3d/tree/master/models) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP cubic-perovskite query corpus](https://github.com/by256/icsg3d/blob/master/query_matproj.py) — Main model training. Author Materials Project query restricted to cubic ABX3 example; exact paper snapshot/split not verified.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Cubic perovskite reconstruction example](https://github.com/by256/icsg3d) — Voxel reconstruction, atomic coordinate and lattice-parameter recovery. Author eval.py --name perovskites; not equivalent to later CDVAE benchmark reimplementation.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464) · [source 2](https://github.com/by256/icsg3d) · [source 3](https://cjcourt.github.io/publication/jcim_2020) · [source 4](https://github.com/by256/icsg3d/blob/master/README.md) · [source 5](https://github.com/by256/icsg3d/blob/master/LICENSE) · [source 6](https://github.com/by256/icsg3d/tree/master/models)

<a id="cfmc-crystal"></a>
## Conformation-family Monte Carlo (CFMC)

**Energy-landscape exploration · Molecular / organic · Method**

[2001 CSP010](https://doi.org/10.1073/pnas.231479298)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Named molecular-crystal sampling algorithm. No author-maintained public implementation verified in the primary-paper and title search.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC60057/) · [source 2](https://doi.org/10.1073/pnas.231479298)

<a id="continuousp"></a>
## ContinuouSP

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP166](https://arxiv.org/abs/2502.02026)

**Source / access:** [Code](https://github.com/tony998244353/ContinuouSP) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/tony998244353/ContinuouSP/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Composition-conditioned crystal structure prediction. Author train/test/eval commands and dataset-labelled checkpoints; evaluation example samples 20 structures per MP-20 target.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Composition-conditioned crystal structure prediction. Author train/test/eval commands and dataset-labelled checkpoints; evaluation example samples 20 structures per MP-20 target.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Composition-conditioned crystal structure prediction. Author train/test/eval commands and dataset-labelled checkpoints; evaluation example samples 20 structures per MP-20 target.

Author implementation linked by the primary paper or repository; no software execution was performed. Primary-paper packer-jp repository redirects to tony998244353/ContinuouSP.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2502.02026) · [source 2](https://github.com/packer-jp/ContinuouSP) · [source 3](https://github.com/tony998244353/ContinuouSP) · [source 4](https://github.com/tony998244353/ContinuouSP/blob/main/README.md) · [source 5](https://github.com/tony998244353/ContinuouSP/blob/main/LICENSE)

<a id="crysbfn"></a>
## CrysBFN

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP160](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html)

**Source / access:** [Code](https://github.com/wu-han-lin/CrysBFN) — Public source repository

**License:** No source license verified 

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://drive.google.com/drive/folders/1W5kGiZYFRJZiyKyTwCdcPk9lbjTsTCO-?usp=drive_link) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — CSP and de novo crystal generation. Separate csp_scripts and gen_scripts; MP-20 test structures and task-specific sampling/evaluation scripts. Other datasets not established by the bounded README check.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html) · [source 2](https://github.com/wu-han-lin/CrysBFN) · [source 3](https://arxiv.org/abs/2502.02016) · [source 4](https://github.com/wu-han-lin/CrysBFN/blob/main/README.md) · [source 5](https://drive.google.com/drive/folders/1W5kGiZYFRJZiyKyTwCdcPk9lbjTsTCO-?usp=drive_link)

<a id="crysim"></a>
## CRYSIM

**Construction, templates and discrete search · Atomic / inorganic · CSP search / proposal implementation**

[2025 CSP176](https://www.nature.com/articles/s42005-025-02380-y)

**Source / access:** [Code](https://github.com/tsudalab/CRYSIM) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/tsudalab/CRYSIM/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm
- [M3GNet pretrained energy evaluator](https://github.com/materialyzeai/m3gnet/tree/main/pretrained) — Optional evaluator / Hosted API

**Training data:**
- [CRYSIM generated structures and evaluator energies](https://github.com/tsudalab/CRYSIM) — Main model training. Random initial configurations, default 1000; factorization-machine regressor updated iteratively
- [M3GNet MPF.2021.2.8 evaluator data](https://figshare.com/articles/dataset/MPF_2021_2_8/19470599) — Required component training. Exact split/version not verified

**Reference data:**
No separate item verified.

**Evaluation:**
- [Ca4S4, Ca24Al16Si24O96 and Si96O192 examples](https://github.com/tsudalab/CRYSIM) — Symmetry-encoded crystal optimization. README supplies search dimensions, seeds, initialization sizes and iteration continuation examples

Tsuda-lab repository describes symmetry-encoded Ising CSP and source modules. Reproducing reported solver setup requires an external Amplify token; public code does not imply all external services are unrestricted.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/tsudalab/CRYSIM) · [source 2](https://www.nature.com/articles/s42005-025-02380-y) · [source 3](https://github.com/tsudalab/CRYSIM/blob/main/LICENSE) · [source 4](https://github.com/materialyzeai/m3gnet/tree/main/pretrained) · [source 5](https://github.com/tsudalab/CRYSIM/blob/main/README.md) · [source 6](https://github.com/materialyzeai/m3gnet/blob/main/README.md)

<a id="cryspai"></a>
## CrySPAI

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2025 CSP167](https://arxiv.org/abs/2501.15838)

**Source / access:** [Project](https://www.mdpi.com/2411-5134/10/2/26/html) — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [CrySPAI evolutionary-search DFT-labelled structures](https://arxiv.org/abs/2501.15838) — Main model training. DNN learns structure-energy relationship during workflow; exact release/split not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary preprint and published Inventions article identify software, but no public author source repository/download was verified in this search. Catalog preprint now has a journal version (10.3390/inventions10020026); metadata update is a separate task.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.mdpi.com/2411-5134/10/2/26/html) · [source 2](https://arxiv.org/abs/2501.15838)

<a id="cryspnet"></a>
## CRYSPNet

**Adaptive and ML-guided search · Atomic / inorganic · Adjacent method**

[2020 CSP094](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802)

**Source / access:** [Code](https://github.com/AuroraLHT/cryspnet) — Public source repository

**License:** No source license verified 

**Pretrained model:** Public pretrained download
- [CRYSPNet learner.zip (fastai v2)](https://drive.google.com/file/d/1rpbV2-mnNj3M16-4BKvhuo5pkeoIY96q/view?usp=sharing) — Main model / Public download

**Training data:**
- [ICSD inorganic structures](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802) — Main model training. More than 100,000 entries; original paper training/validation; current README retrained models distinguished

**Reference data:**
No separate item verified.

**Evaluation:**
- [CRYSPNet ICSD validation](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802) — Bravais lattice, space group and lattice parameter prediction. Paper-defined ICSD validation split; exact indices not verified

Predicts lattice type, space group and lattice parameters; it is an enabling predictor and does not itself supply a complete unconstrained CSP solution.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802) · [source 2](https://github.com/AuroraLHT/cryspnet) · [source 3](https://arxiv.org/abs/2003.14328) · [source 4](https://drive.google.com/file/d/1rpbV2-mnNj3M16-4BKvhuo5pkeoIY96q/view?usp=sharing) · [source 5](https://github.com/AuroraLHT/cryspnet/blob/master/README.md)

<a id="cryspy-bo-laqa"></a>
## CrySPY / BO / LAQA

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2018 CSP075](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803) · [2018 CSP077](https://www.nature.com/articles/s41524-018-0090-y) · [2021 CSP102](https://www.tandfonline.com/doi/full/10.1080/27660400.2021.1943171) · [2022 CSP117](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2055987) · [2022 CSP118](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2059335)

**Source / access:** [Code](https://github.com/Tomoki-YAMASHITA/CrySPY) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/Tomoki-YAMASHITA/CrySPY/blob/master/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [CrySPY BO evaluated candidate structures](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803) — Main model training. BO fits observed candidates during each search; no fixed pretrained corpus; LAQA and newer methods differ

**Reference data:**
No separate item verified.

**Evaluation:**
- [NaCl and Y2Co17](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803) — Bayesian optimization versus random search. Original 2018 selection-based BO recovery tests; not assumed to cover LAQA or later versions

One package implements random search, Bayesian optimization, LAQA, evolutionary search and their hybrids; version papers consolidated.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013803) · [source 2](https://www.nature.com/articles/s41524-018-0090-y) · [source 3](https://www.tandfonline.com/doi/full/10.1080/27660400.2021.1943171) · [source 4](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2055987) · [source 5](https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2059335) · [source 6](https://github.com/Tomoki-YAMASHITA/CrySPY) · [source 7](https://tomoki-yamashita.github.io/CrySPY_doc/) · [source 8](https://github.com/Tomoki-YAMASHITA/CrySPY/blob/master/LICENSE) · [source 9](https://github.com/Tomoki-YAMASHITA/CrySPY/blob/master/README.md)

<a id="crystal-gfn"></a>
## Crystal-GFN

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2023 CSP130](https://arxiv.org/abs/2310.04925v2)

**Source / access:** [Code](https://github.com/alexhernandezgarcia/gflownet) — Public source repository

**License:** Open-source license verified [Apache-2.0](https://github.com/alexhernandezgarcia/gflownet/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [MatBench / MP descriptor formation-energy proxy data](https://arxiv.org/abs/2310.04925) — Required component training. Paper trains descriptor MLP property proxy on MatBench MP snapshot. GFlowNet policy learns on-policy reward trajectories, not likelihood training on a crystal-structure corpus.
- [Self-sampled Crystal-GFN training trajectories](https://arxiv.org/abs/2310.04925) — Main model training. On-policy GFlowNet training with density/formation-energy reward; paper reports 500000 proxy queries. This is online candidate/trajectory data, not a fixed released offline crystal corpus.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Crystal-GFN formation-energy/density and constrained sampling](https://arxiv.org/abs/2310.04925) — Reward-proportional constrained descriptor sampling. Proxy-scored density/formation energy; binary Fe-O, ternary Li-Mn-O, atom-count and cubic constraints; not coordinate-resolved CSP or DFT stability.

Author repository explicitly lists the Crystal-GFN paper; samples structural descriptors, without generating a complete coordinate-resolved crystal.

Main policy is trained online from self-sampled reward trajectories; no fixed main offline structure corpus. Required property proxy trained on MatBench/MP. Samples high-level crystal descriptors without atomic coordinates.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2310.04925) · [source 2](https://github.com/alexhernandezgarcia/gflownet) · [source 3](https://github.com/alexhernandezgarcia/gflownet/blob/main/README.md) · [source 4](https://gflownet.readthedocs.io/en/latest/) · [source 5](https://github.com/alexhernandezgarcia/gflownet/blob/main/LICENSE) · [source 6](https://arxiv.org/html/2310.04925)

<a id="crystalflow"></a>
## CrystalFlow

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP169](https://www.nature.com/articles/s41467-025-64364-4)

**Source / access:** [Code](https://github.com/ixsluo/CrystalFlow) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/ixsluo/CrystalFlow/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://github.com/ixsluo/CrystalFlow/releases) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-CALYPSO-60](https://github.com/ixsluo/CrystalFlow) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Composition-conditioned CSP and de novo generation. Author CSP test.csv comparison; single and 20-sample commands; de novo MP-20 generation evaluated separately.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Composition-conditioned CSP and de novo generation. Author CSP test.csv comparison; single and 20-sample commands; de novo MP-20 generation evaluated separately.

Author implementation linked by the primary paper or repository; no software execution was performed.

Explicit pressure-conditioned training example uses MP-CALYPSO-60. MP-20 formation-energy-conditioned DNG example uses mp_20_chgnet. README acknowledgements alone are not taken as proof of training on all inherited datasets.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41467-025-64364-4) · [source 2](https://github.com/ixsluo/CrystalFlow) · [source 3](https://github.com/ixsluo/CrystalFlow/blob/main/README.md) · [source 4](https://github.com/ixsluo/CrystalFlow/blob/main/LICENSE) · [source 5](https://github.com/ixsluo/CrystalFlow/releases)

<a id="crystalformer"></a>
## CrystalFormer

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP177](https://doi.org/10.1016/j.scib.2025.09.035) · [2025 CrystalFormerCSP2025](https://arxiv.org/abs/2512.18251)

**Source / access:** [Code](https://github.com/deepmodeling/CrystalFormer) — Public source repository

**License:** Open-source license verified [Apache-2.0](https://github.com/deepmodeling/CrystalFormer/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Multitask and CSP-only Alex20s checkpoints](https://huggingface.co/zdcao/CrystalFormer) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [Alex-20s](https://huggingface.co/datasets/zdcao/alex-20s) — Main model training. Current MODEL_CARD: both multitask and CSP-only checkpoints trained on Alex-20s, differing cfg_drop_prob. This current release must not be silently conflated with original paper MP-20 experiments.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Alex-20s](https://huggingface.co/datasets/zdcao/alex-20s) — CSP and space-group-conditioned DNG. Current author evaluation expects train/test/generated structures in same specified space group; exact original-paper split not established.

Space-group-informed autoregressive generator. Unrelated omron-sinicx/crystalformer is a different property-prediction project.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1016/j.scib.2025.09.035) · [source 2](https://github.com/deepmodeling/CrystalFormer) · [source 3](https://github.com/deepmodeling/CrystalFormer/blob/main/README.md) · [source 4](https://github.com/deepmodeling/CrystalFormer/blob/main/LICENSE) · [source 5](https://huggingface.co/zdcao/CrystalFormer) · [source 6](https://github.com/deepmodeling/CrystalFormer/blob/main/MODEL_CARD.md)

<a id="crystalgan"></a>
## CrystalGAN

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2019 CSP086](https://ceur-ws.org/Vol-2350/paper18.pdf)

**Source / access:** [Code](https://github.com/asmanouira/CrystalGAN) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/asmanouira/CrystalGAN/blob/master/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Pd-H and Ni-H binary hydride POSCAR corpora](https://github.com/asmanouira/CrystalGAN) — Main model training. Binary Pd-H and Ni-H training domains; ternary Pd-H-Ni generated target domain, not a broad MP-20 model.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Pd-H-Ni generation case](https://github.com/asmanouira/CrystalGAN) — Generate ternary hydrides from binary training domains. Author Pd-H / Ni-H to Pd-H-Ni demonstration.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://ceur-ws.org/Vol-2350/paper18.pdf) · [source 2](https://github.com/asmanouira/CrystalGAN) · [source 3](https://github.com/asmanouira/CrystalGAN/blob/master/README.md) · [source 4](https://github.com/asmanouira/CrystalGAN/blob/master/LICENSE)

<a id="crystalgrpo"></a>
## CrystalGRPO

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2026 CSP182](https://arxiv.org/abs/2608.06582)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Paper composition-conditioned CSP post-training on pretrained flow backbones; exact post-training cohort details not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Paper composition-conditioned CSP post-training on pretrained flow backbones; exact post-training cohort details not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Composition-conditioned CSP; MP-20 PXRD-guided CSP. MR@1/MR@20 and RMSE@1/RMSE@20 reported separately; PXRD conditioning adds target-specific information.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Composition-conditioned CSP; MP-20 PXRD-guided CSP. MR@1/MR@20 and RMSE@1/RMSE@20 reported separately; PXRD conditioning adds target-specific information.

Primary preprint checked and targeted official-code searches found no verified release. Public OMatG and PXRDGen backbones do not establish release of the CrystalGRPO post-training implementation.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2608.06582) · [source 2](https://arxiv.org/html/2608.06582)

<a id="crystalgrw"></a>
## CrystalGRW

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2026 CSP183](https://www.nature.com/articles/s41598-026-62470-x)

**Source / access:** [Code](https://github.com/trachote/crystalgrw) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/trachote/crystalgrw/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [MP20 model checkpoints](https://zenodo.org/records/14948252) — Main model / Public download (official release instructions; no inference performed)
- [Alex-MP20 Git LFS checkpoints](https://github.com/trachote/crystalgrw/tree/main/checkpoints) — Main model / Public Git LFS

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. MP-20 example/checkpoints; separate 2025-04-15 ALEX-MP-20 and 2025-04-18 point-group-conditioned models.
- [ALEX-MP-20](https://github.com/trachote/crystalgrw) — Main model training. MP-20 example/checkpoints; separate 2025-04-15 ALEX-MP-20 and 2025-04-18 point-group-conditioned models.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — De novo and condition-guided crystal generation. Author compute_metrics.py example compares generated samples with MP-20 training reference; exact test protocol not independently verified.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41598-026-62470-x) · [source 2](https://github.com/trachote/crystalgrw) · [source 3](https://github.com/trachote/crystalgrw/blob/main/README.md) · [source 4](https://github.com/trachote/crystalgrw/blob/main/LICENSE) · [source 5](https://zenodo.org/records/14948252) · [source 6](https://github.com/trachote/crystalgrw/tree/main/checkpoints)

<a id="crystalite"></a>
## Crystalite

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2026 CSP184](https://arxiv.org/abs/2604.02270)

**Source / access:** [Code](https://github.com/joshrosie/crystalite) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/joshrosie/crystalite/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [DNG and CSP checkpoints](https://huggingface.co/datasets/joshrosie/crystalite-datasets/tree/main) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Released DNG MP20 checkpoint: subatomic_tokenizer_pca_16; CSP checkpoints: MP-20 and MPTS-52, atomic_number typing; training split IDs not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Released DNG MP20 checkpoint: subatomic_tokenizer_pca_16; CSP checkpoints: MP-20 and MPTS-52, atomic_number typing; training split IDs not independently compared.

**Reference data:**
- [MP phase-diagram reference 2023-02-07](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158?file=40344436) — Reference / search database. Optional stability hull reference, not generator training.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — CSP; MP-20 de novo generation and optional MLIP stability. CSP full test split uses StructureMatcher match rate/RMSD, aa_rho_lattice_values=4. DNG NequIP/other MLIP SUN/MSUN settings separately; no DFT inference.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — CSP; MP-20 de novo generation and optional MLIP stability. CSP full test split uses StructureMatcher match rate/RMSD, aa_rho_lattice_values=4. DNG NequIP/other MLIP SUN/MSUN settings separately; no DFT inference.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2604.02270) · [source 2](https://github.com/joshrosie/crystalite) · [source 3](https://stases.github.io/blogposts/crystalite/) · [source 4](https://github.com/joshrosie/crystalite/blob/main/README.md) · [source 5](https://github.com/joshrosie/crystalite/blob/main/LICENSE) · [source 6](https://huggingface.co/datasets/joshrosie/crystalite-datasets/tree/main)

<a id="crystallm"></a>
## CrystaLLM

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP140](https://doi.org/10.1038/s41467-024-54639-7)

**Source / access:** [Code](https://github.com/lantunes/CrystaLLM) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/lantunes/CrystaLLM/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released trained CrystaLLM models](https://zenodo.org/records/10642388) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [CrystaLLM CIF v1 corpus (MP/OQMD/NOMAD)](https://github.com/lantunes/CrystaLLM) — Main model training. cifs_v1_orig.tar.gz; deduplicate by cell composition plus space group choosing lowest volume per formula unit; preprocessing/augmentation and split commands supplied.

**Reference data:**
No separate item verified.

**Evaluation:**
- [CrystaLLM CIF v1 held-out test prompts](https://github.com/lantunes/CrystaLLM) — Autoregressive CIF completion and structural validity/recovery. make_prompts.py cifs_v1_test.pkl.gz and evaluate_cifs.py; paper-specific split, not CDVAE MP-20.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1038/s41467-024-54639-7) · [source 2](https://github.com/lantunes/CrystaLLM) · [source 3](https://github.com/lantunes/CrystaLLM/blob/main/README.md) · [source 4](https://github.com/lantunes/CrystaLLM/blob/main/LICENSE) · [source 5](https://zenodo.org/records/10642388)

<a id="crystaloptimizer"></a>
## CrystalOptimizer / CSO-FM

**Context, evaluators and evaluation · Molecular / organic · Enabling evaluator**

[2011 CSP049](https://doi.org/10.1021/ct100597e)

**Source / access:** [Project](https://sargentcentre.org/impact/spinouts-software/) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Flexible-molecule local lattice-energy minimizer, an enabling component rather than a stand-alone global search. Official Sargent Centre page calls CSO-FM formerly CrystalOptimizer and supplies a contact route; public source not verified. Avoid unrelated Minecraft repositories.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://sargentcentre.org/impact/spinouts-software/) · [source 2](https://www.chem.ucl.ac.uk/cposs/computational/crystaloptimizer.html) · [source 3](https://doi.org/10.1021/ct100597e)

<a id="crystalpredictor"></a>
## CrystalPredictor / CrystalPredictor II

**Random structure search · Molecular / organic · Method**

[2005 CSP023](https://doi.org/10.1002/jcc.20165) · [2007 CSP031](https://doi.org/10.1080/00268970601143317) · [2015 CSP063](https://doi.org/10.1021/ct500621v) · [2016 CSP065](https://doi.org/10.1107/S2052520616015122)

**Source / access:** [Project](https://sargentcentre.org/impact/spinouts-software/) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official Sargent Centre page identifies the CSP software suite and supplies a contact route. Source download and license terms were not publicly verified; the UCL manual describes distributed binaries. Consolidates rigid, flexible, local-approximation and adaptive-model papers.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://sargentcentre.org/impact/spinouts-software/) · [source 2](https://www.chem.ucl.ac.uk/cposs/computational/CrystalPredictor_v2.4.3_manual.pdf) · [source 3](https://doi.org/10.1002/jcc.20165) · [source 4](https://doi.org/10.1080/00268970601143317) · [source 5](https://doi.org/10.1021/ct500621v) · [source 6](https://doi.org/10.1107/S2052520616015122)

<a id="csp-aiff"></a>
## CSP(aiFF) / autoPES–UPACK workflow

**Random structure search · Molecular / organic · Method**

[2022 CSP121](https://doi.org/10.1038/s41467-022-30692-y)

**Source / access:** [Project](https://www.physics.udel.edu/~szalewic/SAPT/SAPT.html) — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Molecule-specific SAPT(DFT) dimer energies](https://doi.org/10.1038/s41467-022-30692-y) — Main model training. autoPES fitted ab initio force fields; not a cross-molecule pretrained corpus

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper molecular polymorph search validation](https://doi.org/10.1038/s41467-022-30692-y) — Crystal structure and energy-ranking recovery. Molecule-specific fitted potential search followed by periodic DFT+D ranking; paper supplementary CIFs

Primary paper’s Code availability identifies SAPT/autoPES, MOLPAK, UPACK and DFT components, an UPACK patch on the SAPT site, and fitted-potential FORTRAN in Supplementary Data. No single integrated repository is asserted. SAPT download portal failed to load during this check, so a working current complete source download was not verified.

Main training means fitted molecule-specific force-field targets in this record, not training of the UPACK packing search algorithm. SAPT dimer data and final DFT ranking are separate roles.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41467-022-30692-y) · [source 2](https://ampere.physics.udel.edu/~szalewic/SAPT/manual2020.pdf) · [source 3](https://doi.org/10.1038/s41467-022-30692-y)

<a id="csp-al-molecular"></a>
## CSP-AL (committee active / delta learning)

**Adaptive and ML-guided search · Molecular / organic · Enabling evaluator**

[2024 CSP150](https://doi.org/10.1021/acs.jpca.3c07129)

**Source / access:** [Code](https://github.com/pwvbutler/CSP-AL) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/pwvbutler/CSP-AL/main/LICENSE.md)

**Pretrained model:** No pretrained release verified

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Paper Data Availability explicitly links the authors’ Python active-learning code. Fits ML potentials to existing molecular-CSP landscapes and extends them with MC; it is an enabling training workflow, not a replacement for all generator/evaluator components.

Bounded check of author repository/paper sources; exact main-model training data and evaluation protocol not established in inspected source. Not verified is not a claim of absence.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10860135/) · [source 2](https://pubs.acs.org/doi/10.1021/acs.jpca.3c07129) · [source 3](https://doi.org/10.1021/acs.jpca.3c07129) · [source 4](https://raw.githubusercontent.com/pwvbutler/CSP-AL/main/README.md) · [source 5](https://raw.githubusercontent.com/pwvbutler/CSP-AL/main/LICENSE.md)

<a id="csp-mace-a"></a>
## CSP-MACE-Å

**Context, evaluators and evaluation · Molecular / organic · Enabling evaluator**

[2026 CSP186](https://arxiv.org/abs/2605.28905)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [B86bPBE-XDM molecular-crystal delta targets](https://arxiv.org/abs/2605.28905) — Main model training. 50,000 B86bPBE-XDM calculations; intermolecular residual targets

**Reference data:**
No separate item verified.

**Evaluation:**
- [AstraZeneca 19-compound cohort](https://arxiv.org/abs/2605.28905) — Molecular-crystal energy ranking. 19 compounds including a salt drawn from prior AstraZeneca CSP publications; DFT energy comparisons
- [Seven CSP blind-test 28-compound cohort](https://arxiv.org/abs/2605.28905) — Molecular-crystal energy ranking. 28 compounds including salts and cocrystals collated from seven blind tests

Primary preprint describes the intra/intermolecular delta-learned evaluator. No public authors’ repository, weights release or source download verified in the primary HTML and exact-name search. Generic ACEsuit/mace code is not automatically this trained model or workflow.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/html/2605.28905v1) · [source 2](https://arxiv.org/abs/2605.28905)

<a id="cspmetrics"></a>
## CSPMetrics

**Context, evaluators and evaluation · Atomic / inorganic · Enabling predictor / evaluation**

[2024 CSPMetrics2024](https://doi.org/10.1016/j.commatsci.2024.112802)

**Source / access:** [Code](https://github.com/usccolumbia/CSPBenchMetrics) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/usccolumbia/CSPBenchMetrics/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/usccolumbia/CSPBenchMetrics/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

Quantitative structure comparison using complementary geometry, graph, fingerprint and energy distances. Component accuracy is not complete CSP recovery.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1016/j.commatsci.2024.112802) · [source 2](https://github.com/usccolumbia/CSPBenchMetrics/blob/main/README.md)

<a id="cspml"></a>
## CSPML

**Construction, templates and discrete search · Atomic / inorganic · CSP search / proposal implementation**

[2022 CSP115](https://www.sciencedirect.com/science/article/pii/S0927025622002555)

**Source / access:** [Code](https://github.com/Minoru938/CSPML) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/Minoru938/CSPML/blob/master/LICENSE)

**Pretrained model:** Public pretrained download
- [CSPML embedded pretrained classifiers](https://github.com/Minoru938/CSPML#cspml-crystal-structure-prediction-with-machine-learning-based-element-substitution) — Main model / Public download

**Training data:**
- [CSPML stable Materials Project compounds](https://github.com/Minoru938/CSPML) — Main model training. 33,153 stable compounds; primary 2024 RL paper explicitly identifies CSPML pretrained ensemble training on these compounds; original/updated pair splits not verified

**Reference data:**
- [CSPML stable template compounds](https://github.com/Minoru938/CSPML) — Reference / search database. 33,153 stable MP compounds embedded; original versus 2024 updated classifier distinguished

**Evaluation:**
No separate item verified.

Repository calls itself original implementation and identifies 2022 paper and newer model version. Template selection and elemental substitution depend on database coverage.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/Minoru938/CSPML) · [source 2](https://github.com/Minoru938/CSPML/blob/master/LICENSE) · [source 3](https://github.com/Minoru938/CSPML#cspml-crystal-structure-prediction-with-machine-learning-based-element-substitution) · [source 4](https://github.com/Minoru938/CSPML/blob/master/README.md) · [source 5](https://www.sciencedirect.com/science/article/pii/S0927025622002555) · [source 6](https://www.nature.com/articles/s41524-024-01474-5)

<a id="cubicgan"></a>
## CubicGAN

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2021 CSP105](https://doi.org/10.1002/advs.202100566)

**Source / access:** [Code](https://github.com/MilesZhao/CubicGAN) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/MilesZhao/CubicGAN/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Ternary generator pretrained model](https://github.com/MilesZhao/CubicGAN/tree/main/pre-trained) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [OQMD cubic ternaries](https://github.com/MilesZhao/CubicGAN/blob/main/data/oqmd-dat.csv) — Main model training. Paper training material IDs in oqmd-dat.csv; symmetrized CIFs with atom-position multiplicative factor 0.25; 100 sample CIFs are a demo, not full training data.

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1002/advs.202100566) · [source 2](https://github.com/MilesZhao/CubicGAN) · [source 3](https://raw.githubusercontent.com/MilesZhao/CubicGAN/main/README.md) · [source 4](https://github.com/MilesZhao/CubicGAN/blob/main/LICENSE) · [source 5](https://github.com/MilesZhao/CubicGAN/tree/main/pre-trained)

<a id="dao"></a>
## DAO

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2026 CSP193](https://www.nature.com/articles/s41467-026-72362-3)

**Source / access:** [Code](https://github.com/GLAD-RUC/DAO) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/GLAD-RUC/DAO/blob/release/LICENSE)

**Pretrained model:** Public pretrained download
- [DAO pretrained / finetuned checkpoints](https://drive.google.com/drive/folders/1msp-D3uWD0fJrwE7qrbRXok1u-FoOAdc?usp=drive_link) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. DAO-G downstream fine-tuning commands and benchmark datasets; base pretraining corpus not established by this README check.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. DAO-G downstream fine-tuning commands and benchmark datasets; base pretraining corpus not established by this README check.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — CSP; property-prediction lane separate. Author DAO CSP generate and evaluation commands; SuperCon mentioned separately for downstream property tasks.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — CSP; property-prediction lane separate. Author DAO CSP generate and evaluation commands; SuperCon mentioned separately for downstream property tasks.

Publisher links ManlioWu/DAO; present official repository redirects/hosts under GLAD-RUC and explicitly names the paper.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41467-026-72362-3) · [source 2](https://github.com/GLAD-RUC/DAO) · [source 3](https://github.com/ManlioWu/DAO) · [source 4](https://raw.githubusercontent.com/GLAD-RUC/DAO/release/README.md) · [source 5](https://glad-ruc.github.io/DAO/) · [source 6](https://github.com/GLAD-RUC/DAO/blob/release/LICENSE) · [source 7](https://drive.google.com/drive/folders/1msp-D3uWD0fJrwE7qrbRXok1u-FoOAdc?usp=drive_link)

<a id="pymatgen-ionic-substitution"></a>
## Data-mined ionic substitution (pymatgen implementation)

**Construction, templates and discrete search · Atomic / inorganic · Template-substitution proposal component**

[2011 CSP048](https://doi.org/10.1021/ic102031h)

**Source / access:** [Code](https://github.com/materialsproject/pymatgen) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/materialsproject/pymatgen/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official API documentation explicitly attributes Substitutor algorithm to Hautier et al. (2011). This is a maintained-library implementation of the method, not an assertion of byte-for-byte identity with the original paper code.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pymatgen.org/pymatgen.core.structure_prediction.html) · [source 2](https://github.com/materialsproject/pymatgen) · [source 3](https://github.com/materialsproject/pymatgen/blob/main/LICENSE) · [source 4](https://github.com/materialsproject/pymatgen/blob/main/README.md) · [source 5](https://doi.org/10.1021/ic102031h)

<a id="data-mined-prototype-search"></a>
## Data-mined prototype search (Curtarolo / Fischer / Ceder)

**Construction, templates and discrete search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2003 CSP017](https://doi.org/10.1103/PhysRevLett.91.135503) · [2006 CSP029](https://doi.org/10.1038/nmat1691)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [Paper-specific ab initio materials library](https://doi.org/10.1103/PhysRevLett.91.135503) — Main model training. Heuristic rule extraction from calculated information; exact corpus release and split unverified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1103/PhysRevLett.91.135503) · [source 2](https://doi.org/10.1038/nmat1691)

<a id="dd3dcs-encoding-decoding-3d-crystals"></a>
## DD3DCS / Encoding-Decoding 3D Crystals

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2019 CSP087](https://arxiv.org/abs/1909.00949)

**Source / access:** [Code](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals/blob/master/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [46744 Materials Project CIF corpus](https://arxiv.org/abs/1909.00949) — Main model training. Paper Methods states 80% testing and 20% training (retain literal unusual wording); max cell side <10 angstrom; rotated single-cell and periodic-cube representations. Do not silently invert split.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Voxel reconstruction held-out crystals](https://arxiv.org/abs/1909.00949) — Encode/decode density, atom segmentation, interpolation. Paper-specific voxel reconstruction and atom recovery; QM9/ZINC are background examples, not this model training.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/1909.00949) · [source 2](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals) · [source 3](https://raw.githubusercontent.com/hoffmannjordan/Encoding-Decoding-3D-Crystals/master/README.md) · [source 4](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals/blob/master/LICENSE) · [source 5](https://arxiv.org/html/1909.00949)

<a id="deep-free-energy-df-csp"></a>
## Deep free energy (DF) CSP

**Context, evaluators and evaluation · Atomic / inorganic · Enabling evaluator**

[2026 CSP181](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [System-specific SCHA free-energy labels](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7) — Main model training. Two-level concurrent learning of free energies, forces and stresses; La–Sc–H at 200 GPa / 300 K; exact released split not verified

**Reference data:**
No separate item verified.

**Evaluation:**
- [La–Sc–H hydrides and LaH10 cost comparison](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7) — Finite-temperature and nuclear-quantum CSP. Recover LaH10/LaSc2H24 stability and assess LaScH8; compare with DFT-level SSCHA

Primary paper and author preprint checked; no paper-specific public source release verified. Distinguish deep free-energy evaluator from the outer CSP proposal/search mechanism.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://journals.aps.org/prb/abstract/10.1103/3qjr-mgv7) · [source 2](https://arxiv.org/abs/2604.20230)

<a id="deepcsp-organic-gan"></a>
## DeepCSP (organic conditional GAN + GCN)

**Learned generation and conditional CSP · Molecular / organic · Method**

[2024 CSP151](https://doi.org/10.1016/j.xinn.2023.100562)

**Source / access:** [Project](https://sites.google.com/view/yezhuyifan/) — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper verifies model identity and author contact pages; public code not verified in primary article and exact-title/model search. Distinguish this 2024 organic GAN system from unrelated EEG DeepCSP and inorganic diffusion models with similar names.

Bounded check of author repository/paper sources; exact main-model training data and evaluation protocol not established in inspected source. Not verified is not a claim of absence. Primary paper access attempted; response status 200 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10878116/) · [source 2](https://www.the-innovation.org/data/article/innovation/preview/pdf/S2666-6758%2823%2900190-X.pdf) · [source 3](https://doi.org/10.1016/j.xinn.2023.100562)

<a id="diffcsp"></a>
## DiffCSP

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2023 CSP128](https://arxiv.org/abs/2309.04475)

**Source / access:** [Code](https://github.com/jiaor17/DiffCSP) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/jiaor17/DiffCSP/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://drive.google.com/drive/folders/11WOc9lTZN4hkIY7SKLCIrbsTMGy9TsoW?usp=sharing) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Author implementation linked by the primary paper or repository; no software execution was performed.

Explicit author data/training instructions establish usage. MP-20 and MPTS-52 are distinct protocols; shared dataset names do not prove identical preprocessing or splits across implementations.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2309.04475) · [source 2](https://github.com/jiaor17/DiffCSP) · [source 3](https://raw.githubusercontent.com/jiaor17/DiffCSP/main/README.md) · [source 4](https://github.com/jiaor17/DiffCSP/blob/main/LICENSE) · [source 5](https://drive.google.com/drive/folders/11WOc9lTZN4hkIY7SKLCIrbsTMGy9TsoW?usp=sharing)

<a id="diffcsp-plus-plus"></a>
## DiffCSP++

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP154](https://arxiv.org/abs/2402.03992)

**Source / access:** [Code](https://github.com/jiaor17/DiffCSP-PP) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/jiaor17/DiffCSP-PP/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://drive.google.com/drive/folders/1FQ_b6CE09KtyGaU_r6uO8_I5JhrQmUFB?usp=sharing) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Author implementation linked by the primary paper or repository; no software execution was performed.

Author README supports Perov-5, Carbon-24, MP-20 and MPTS-52; its cited Alex-MP-20 extension is an optional extension, not proof of original training. CSP evaluation example uses ground-truth Wyckoff positions: disclose supplied symmetry information.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2402.03992) · [source 2](https://github.com/jiaor17/DiffCSP-PP) · [source 3](https://raw.githubusercontent.com/jiaor17/DiffCSP-PP/main/README.md) · [source 4](https://raw.githubusercontent.com/jiaor17/DiffCSP-PP/main/LICENSE) · [source 5](https://drive.google.com/drive/folders/1FQ_b6CE09KtyGaU_r6uO8_I5JhrQmUFB?usp=sharing)

<a id="deds-crystal"></a>
## Diffusion-equation / distance-scaling global optimization

**Energy-landscape exploration · Molecular / organic · Method**

[1998 CSP005](https://doi.org/10.1021/jp972424u)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Classical energy-landscape smoothing, unrelated to learned diffusion models. Primary method paper verified; no authors’ source distribution located by the limited paper/title search.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1021/jp972424u)

<a id="disordered-structure-nnp-training-hong-et-al"></a>
## Disordered-structure NNP training (Hong et al.)

**Context, evaluators and evaluation · Atomic / inorganic · Enabling evaluator**

[2020 CSP099](https://arxiv.org/abs/2008.07786)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Liquid and quenched-amorphous DFT trajectories](https://arxiv.org/abs/2008.07786) — Main model training. Composition-specific trajectories; exact counts/splits not verified

**Reference data:**
No separate item verified.

**Evaluation:**
- [Ba2AgSi3, Mg2SiO4, LiAlCl4 and InTe2O5F](https://arxiv.org/abs/2008.07786) — NNP energy ranking versus DFT. Experimental and theoretically generated low-energy structures; evolutionary-search comparison

Primary paper describes the training workflow; a paper-specific public code release was not verified. Related SPINNER/SIMPLE-NN software should not be substituted silently for this paper.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2008.07786)

<a id="dmcrystal"></a>
## DMCrystal

**Evolutionary and genetic search · Atomic / inorganic · Method**

[2020 DMCrystal2020](https://doi.org/10.1021/acs.jpca.0c08775)

**Source / access:** [Code](https://github.com/usccolumbia/dmcrystal) — Public source repository

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/usccolumbia/dmcrystal/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

Genetic reconstruction from pairwise distances, lattice, and space-group information. Reconstruction requires supplied structural constraints.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1021/acs.jpca.0c08775) · [source 2](https://github.com/usccolumbia/dmcrystal/blob/main/README.md)

<a id="dp-cdvae"></a>
## DP-CDVAE

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2024 CSP143](https://www.nature.com/articles/s41598-024-51400-4)

**Source / access:** [Code](https://github.com/trachote/dp-cdvae) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/trachote/dp-cdvae/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Paper crystal reconstruction/generation experiments; CDVAE benchmark corpus versions. Exact files/split comparison not performed.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Paper crystal reconstruction/generation experiments; CDVAE benchmark corpus versions. Exact files/split comparison not performed.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Paper crystal reconstruction/generation experiments; CDVAE benchmark corpus versions. Exact files/split comparison not performed.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction and de novo generation. Paper reconstruction and generation tasks with separate metrics; not composition-only CSP by default.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction and de novo generation. Paper reconstruction and generation tasks with separate metrics; not composition-only CSP by default.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction and de novo generation. Paper reconstruction and generation tasks with separate metrics; not composition-only CSP by default.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41598-024-51400-4) · [source 2](https://github.com/trachote/dp-cdvae) · [source 3](https://raw.githubusercontent.com/trachote/dp-cdvae/main/README.md) · [source 4](https://raw.githubusercontent.com/trachote/dp-cdvae/main/LICENSE) · [source 5](https://pmc.ncbi.nlm.nih.gov/articles/PMC10787843/)

<a id="enumlib"></a>
## enumlib

**Construction, templates and discrete search · Atomic / inorganic · Constructive enumeration component**

[2008 CSP035](https://doi.org/10.1103/PhysRevB.77.224115) · [2012 CSP056](https://doi.org/10.1016/j.commatsci.2012.02.015)

**Source / access:** [Code](https://github.com/msg-byu/enumlib) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/msg-byu/enumlib/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Developer repository cites the Hart–Forcade 2008 and fixed-concentration 2012 papers. Enumerates parent-lattice derivatives; requires subsequent physical evaluation.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/msg-byu/enumlib) · [source 2](https://github.com/msg-byu/enumlib/blob/main/LICENSE) · [source 3](https://github.com/msg-byu/enumlib/blob/main/README.md) · [source 4](https://doi.org/10.1103/PhysRevB.77.224115) · [source 5](https://doi.org/10.1016/j.commatsci.2012.02.015)

<a id="equicsp"></a>
## EquiCSP

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP144](https://proceedings.mlr.press/v235/lin24b.html)

**Source / access:** [Code](https://github.com/EmperorJia/EquiCSP) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/EmperorJia/EquiCSP/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released pretrained model / checkpoints](https://drive.google.com/drive/folders/1Dw945rCLCT3jbQ8FZsAxCCVMjeo-PByc?usp=drive_link) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Author implementation linked by the primary paper or repository; no software execution was performed.

Explicit author data/training instructions establish usage. MP-20 and MPTS-52 are distinct protocols; shared dataset names do not prove identical preprocessing or splits across implementations.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://proceedings.mlr.press/v235/lin24b.html) · [source 2](https://github.com/EmperorJia/EquiCSP) · [source 3](https://raw.githubusercontent.com/EmperorJia/EquiCSP/main/README.md) · [source 4](https://raw.githubusercontent.com/EmperorJia/EquiCSP/main/LICENSE) · [source 5](https://drive.google.com/drive/folders/1Dw945rCLCT3jbQ8FZsAxCCVMjeo-PByc?usp=drive_link)

<a id="norskov-alloy-search"></a>
## Evolutionary alloy-prototype search (Jóhannesson et al.)

**Evolutionary and genetic search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2002 CSP013](https://doi.org/10.1103/PhysRevLett.88.255506)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Four-component fcc/bcc alloys from 32 metals](https://doi.org/10.1103/PhysRevLett.88.255506) — Evolutionary alloy property optimization. Finite design pool of 192,016 possible alloys; DFT evaluation

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1103/PhysRevLett.88.255506)

<a id="flowmm-flowllm"></a>
## FlowMM / FlowLLM

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2024 CSP145](https://arxiv.org/abs/2410.23405) · [2024 CSP146](https://proceedings.mlr.press/v235/miller24a.html)

**Source / access:** [Code](https://github.com/facebookresearch/flowmm) — Public source repository

**License:** Restrictive / noncommercial source license [CC-BY-NC-4.0](https://raw.githubusercontent.com/facebookresearch/flowmm/main/LICENSE.md)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [FlowLLM MP-20 LLaMA-generated conditional pairs](https://github.com/facebookresearch/flowmm/tree/main/data/mp20_llama) — Main model training. FlowLLM successor: CrystalLLM/LLaMA fine-tuned on MP-20 supplies initial samples; paired data train conditional RFM, unlike FlowMM base Gaussian experiments.

**Reference data:**
- [MP convex-hull reference 2023-02-07](https://figshare.com/articles/dataset/Matbench_Discovery_v1_0_0/22715158) — Reference / search database. 2023-02-07 hull for optional stability evaluation; not FlowMM training data.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Official facebookresearch/flowmm README has a dedicated FlowLLM Model section, training command with data=mp20_llama and base_distribution_from_data=True, and citations for both papers. FlowLLM shares this implementation repository; its language-model base is the separate crystal-text-llm dependency linked below. No execution performed.

Explicit author data/training instructions establish usage. MP-20 and MPTS-52 are distinct protocols; shared dataset names do not prove identical preprocessing or splits across implementations.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2410.23405) · [source 2](https://proceedings.mlr.press/v235/miller24a.html) · [source 3](https://github.com/facebookresearch/flowmm) · [source 4](https://github.com/facebookresearch/crystal-text-llm) · [source 5](https://raw.githubusercontent.com/facebookresearch/flowmm/main/README.md) · [source 6](https://raw.githubusercontent.com/facebookresearch/flowmm/main/LICENSE.md)

<a id="ftcp"></a>
## FTCP

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2022 CSP111](https://doi.org/10.1016/j.matt.2021.11.032)

**Source / access:** [Code](https://github.com/PV-Lab/FTCP) — Public source repository

**License:** Open-source license verified [Apache-2.0](https://raw.githubusercontent.com/PV-Lab/FTCP/master/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [FTCP filtered Materials Project ternaries](https://github.com/PV-Lab/FTCP) — Main model training. Original paper case 1 dataset: ternary crystals <=20 sites, energy above hull <0.08 eV/atom; this is not necessarily CDVAE MP-20 split. Other design cases use separately filtered data.

**Reference data:**
No separate item verified.

**Evaluation:**
- [FTCP inverse-design DFT case studies](https://github.com/PV-Lab/FTCP) — Property-targeted inverse design. Paper selected generated structures undergo GGA(+U) relaxation/formation energy evaluation; thermoelectric power-factor case separate; no standard CSP benchmark implied.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1016/j.matt.2021.11.032) · [source 2](https://github.com/PV-Lab/FTCP) · [source 3](https://raw.githubusercontent.com/PV-Lab/FTCP/master/README.md) · [source 4](https://raw.githubusercontent.com/PV-Lab/FTCP/master/LICENSE) · [source 5](https://dspace.mit.edu/server/api/core/bitstreams/c07ccb4d-df07-41e2-a14f-8c6df86522d1/content)

<a id="fuse"></a>
## FUSE / FUSE2

**Energy-landscape exploration · Atomic / inorganic · CSP search / proposal implementation**

[2018 CSP083](https://doi.org/10.1039/c8fd00045j) · [2025 CSP148](https://doi.org/10.1039/d4fd00094c)

**Source / access:** [Code](https://github.com/lrcfmd/FUSE-stable) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/lrcfmd/FUSE-stable/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
- [ICSD known Y–Sr–Ti–O phases](https://doi.org/10.1039/c8fd00045j) — Reference / search database. Ten well-defined compounds supply validation reference structures

**Evaluation:**
- [42 Y–Sr–Ti–O compositions including Y2Ti2O7](https://doi.org/10.1039/c8fd00045j) — FUSE probe-structure composition prediction. Original 2018 FUSE: 3 searches per composition; known ICSD structures used for validation; not assumed FUSE2 protocol

Author-group repository identifies original 2018 paper and includes version folders. Later FUSE2 generative hybrid paper also explicitly points to this repository. FUSE2 generation-plus-basin-hopping implementation; paper specifies version 2.02. Merge with the classical FUSE software entry.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/lrcfmd/FUSE-stable) · [source 2](https://pubs.rsc.org/en/content/articlepdf/2025/fd/d4fd00094c) · [source 3](https://doi.org/10.1039/d4fd00094c) · [source 4](https://livrepository.liverpool.ac.uk/3184543/1/C_Collins_accepted.pdf) · [source 5](https://github.com/lrcfmd) · [source 6](https://github.com/lrcfmd/FUSE-stable/blob/main/LICENSE) · [source 7](https://doi.org/10.1039/c8fd00045j) · [source 8](https://pubs.rsc.org/en/content/articlehtml/2018/fd/c8fd00045j)

<a id="gasp-python"></a>
## GASP-Python

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2019 CSP080](https://doi.org/10.5281/zenodo.2554076)

**Source / access:** [Code](https://github.com/henniggroup/GASP-python) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/henniggroup/GASP-python/blob/master/LICENSE.md)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author-group repository supports bulk and lower-dimensional fixed/variable-composition searches. The older GASP implementation is separately available at https://github.com/henniggroup/gasp; Python and older code should not be conflated.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/henniggroup/GASP-python) · [source 2](https://github.com/henniggroup/GASP-python/blob/master/LICENSE.md) · [source 3](https://github.com/henniggroup/GASP-python/blob/master/README.rst) · [source 4](https://doi.org/10.5281/zenodo.2554076)

<a id="gator-molecular"></a>
## GAtor

**Evolutionary and genetic search · Molecular / organic · Method**

[2018 CSP076](https://doi.org/10.1039/C8FD00067K) · [2018 CSP078](https://doi.org/10.1021/acs.jctc.7b01152)

**Source / access:** [Code](https://www.noamarom.com/wp-content/uploads/2023/01/GAtor_Test.zip) — Source download

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Developer download page directly links the GAtor 1.2 source ZIP and cites both 2018 method papers; older source versions also available. Genetic search with energy/cluster fitness; external electronic-structure engines have their own access terms.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.noamarom.com/software/download/) · [source 2](https://doi.org/10.1039/C8FD00067K) · [source 3](https://doi.org/10.1021/acs.jctc.7b01152)

<a id="gemsdiff"></a>
## GemsDiff

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP157](https://ojs.aaai.org/index.php/AAAI/article/view/30224)

**Source / access:** [Code](https://github.com/aklipf/gemsdiff) — Public source repository

**License:** No source license verified 

**Pretrained model:** Public pretrained download
- [Released checkpoints without lattice diffusion](https://github.com/aklipf/gemsdiff/tree/main/runs/without_cell_diffusion) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [OQMD GemsDiff corpus](https://github.com/aklipf/gemsdiff) — Main model training. OQMD-labelled checkpoint and LiFeO2 sampling example; precise filtered corpus/split not verified.

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author implementation linked by the primary paper or repository; no software execution was performed.

Current author release explicitly removes lattice diffusion relative to the published model. Dataset/checkpoint behavior must be version qualified.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://ojs.aaai.org/index.php/AAAI/article/view/30224) · [source 2](https://github.com/aklipf/gemsdiff) · [source 3](https://raw.githubusercontent.com/aklipf/gemsdiff/main/README.md) · [source 4](https://github.com/aklipf/gemsdiff/tree/main/runs/without_cell_diffusion)

<a id="genarris"></a>
## Genarris (1.0–3.x; Rigid Press)

**Random structure search · Molecular / organic · Method**

[2018 CSP079](https://doi.org/10.1063/1.5014038) · [2020 CSP096](https://doi.org/10.1016/j.cpc.2020.107170) · [2025 CSP171](https://doi.org/10.1021/acs.jctc.5c01080)

**Source / access:** [Code](https://www.noamarom.com/wp-content/uploads/2026/06/gnrs-3.1.4.zip) — Source download

**License:** Open-source license verified [BSD-3-Clause](https://raw.githubusercontent.com/timcrose/Genarris/master/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official developer pages verify all three catalog papers and directly link the current source ZIP plus archived versions. Random packing, volume priors, Rigid Press and hierarchical screening; generator plus evaluator interfaces. Software version consolidation does not imply every feature existed in 2018.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.noamarom.com/software/download/) · [source 2](https://www.noamarom.com/software/genarris/) · [source 3](https://doi.org/10.1063/1.5014038) · [source 4](https://doi.org/10.1016/j.cpc.2020.107170) · [source 5](https://doi.org/10.1021/acs.jctc.5c01080) · [source 6](https://raw.githubusercontent.com/timcrose/Genarris/master/LICENSE)

<a id="glee"></a>
## GLEE (Global Lattice Energy Explorer)

**Random structure search · Molecular / organic · Method**

[2016 CSP066](https://doi.org/10.1021/acs.jctc.5b01112) · [2017 CSP071](https://doi.org/10.1038/nature21419)

**Source / access:** [Project](https://eprints.soton.ac.uk/385478) — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Legacy Day-group quasi-random molecular packing workflow. Original algorithm attribution verified; a public repository specifically distributed as GLEE was not located. See separate mol-CSPy entry for a currently public related Day-group implementation; equivalence to every historical GLEE version is not asserted.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://eprints.soton.ac.uk/385478) · [source 2](https://pubs.acs.org/doi/10.1021/acs.jpca.3c07129) · [source 3](https://doi.org/10.1021/acs.jctc.5b01112) · [source 4](https://doi.org/10.1038/nature21419)

<a id="gn-oa"></a>
## GN-OA

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2022 CSP114](https://www.nature.com/articles/s41467-022-29241-4)

**Source / access:** [Project](http://www.comates.group/links?software=gn_oa) — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [OQMD v1.3](https://www.nature.com/articles/s41467-022-29241-4) — Required component training. Train/validation/test 50/12.5/37.5%; 29 binary CSP compounds excluded from all splits
- [Matbench v0.1 formation energies](https://www.nature.com/articles/s41467-022-29241-4) — Required component training. Train/validation/test 50/12.5/37.5%; 29 binary CSP compounds excluded from all splits

**Reference data:**
No separate item verified.

**Evaluation:**
- [29 held-out binary compounds](https://www.nature.com/articles/s41467-022-29241-4) — Graph-network plus optimizer CSP. Separate from GN energy-regression test split; all 29 excluded from GN training/validation/testing

Publisher links the official comates.group portal; the linked endpoint returned HTTP 404 in this check, so a currently accessible official source release was not verified. Preserve the original source link for provenance; third-party copies are not labeled as author code.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41467-022-29241-4) · [source 2](http://www.comates.group/links?software=gn_oa)

<a id="grace-csp"></a>
## GRACE (Generation Ranking and Characterization Engine)

**Energy-landscape exploration · Molecular / organic · Method**

[2008 CSP034](https://doi.org/10.1002/anie.200704247) · [2008 CSP038](https://doi.org/10.1021/jp710575h) · [2019 CSP089](https://doi.org/10.1126/sciadv.aau3338) · [2023 CSP135](https://doi.org/10.1038/s41586-023-06587-3)

**Source / access:** [Project](https://www.avmatsim.eu/products) — Commercial implementation

**License:** Commercial / controlled source [Commercial license](https://www.avmatsim.eu/products)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

AMS commercial molecular-CSP workflow with tailor-made force fields and downstream ranking; the 2019 workflow combines GRACE sampling with FHI-aims ranking, so GRACE alone is not its entire implementation. The 2023 free-energy library is available from AMS upon request; it is not a public GRACE source release.

Bounded check of author repository/paper sources; exact main-model training data and evaluation protocol not established in inspected source. Not verified is not a claim of absence. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.avmatsim.eu/products) · [source 2](https://www.nature.com/articles/s41586-023-06587-3) · [source 3](https://fhi-aims-club.gitlab.io/tutorials/dispersion-corrected-hybrid-dft/CSP/) · [source 4](https://doi.org/10.1002/anie.200704247) · [source 5](https://doi.org/10.1021/jp710575h) · [source 6](https://doi.org/10.1126/sciadv.aau3338) · [source 7](https://doi.org/10.1038/s41586-023-06587-3)

<a id="grinsp"></a>
## GRINSP / GRINS

**Construction, templates and discrete search · Atomic / inorganic · CSP search / proposal implementation**

[2005 CSP024](https://doi.org/10.1107/S0021889805002384)

**Source / access:** [Code](https://www.cristal.org/grinsp/) — Source download

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author homepage describes Fortran source files inside ZIP packages and cites the 2005 paper. Geometric polyhedral construction and Monte Carlo refinement; not a general DFT-based global search.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.cristal.org/grinsp/) · [source 2](https://doi.org/10.1107/S0021889805002384)

<a id="gsgo"></a>
## GSGO (global space-group optimization)

**Evolutionary and genetic search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2007 CSP033](https://doi.org/10.1103/PhysRevB.75.104113)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Si, SiC, GaAs and Au8Pd4](https://doi.org/10.1103/PhysRevB.75.104113) — Global lattice/configuration recovery. Pseudopotential energy search from random cell/positions; AuPd close configurations unresolved

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1103/PhysRevB.75.104113)

<a id="htocsp"></a>
## HTOCSP (population / width-first sampling)

**Random structure search · Molecular / organic · Method**

[2025 CSP164](https://doi.org/10.1039/D4DD00264D)

**Source / access:** [Code](https://github.com/MaterSim/HTOCSP) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/MaterSim/HTOCSP/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm
- [UMA evaluator model card (separate access terms)](https://huggingface.co/facebook/UMA) — Optional evaluator / Gated / Hugging Face token required

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author repository cites Zhu–Hattori paper and documents PyXtal/pyocse/RDKit/AmberTools/CHARMM integration. Repository is public; CHARMM and optional UMA model access require separate steps. Population sampling is classified as a random/evolutionary hybrid, rather than treating all population methods as identical GAs.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/MaterSim/HTOCSP) · [source 2](https://pubs.rsc.org/en/content/articlehtml/2024/dd/d4dd00264d) · [source 3](https://doi.org/10.1039/D4DD00264D) · [source 4](https://raw.githubusercontent.com/MaterSim/HTOCSP/main/README.md) · [source 5](https://raw.githubusercontent.com/MaterSim/HTOCSP/main/LICENSE)

<a id="imatgen"></a>
## iMatGen

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2019 CSP088](https://doi.org/10.1016/j.matt.2019.08.017)

**Source / access:** [Code](https://github.com/kaist-amsg/imatgen) — Public source repository

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Image-based materials generator on the named author group repository; paper DOI and lab repository identify the work.

Bounded author README/source check did not establish exact main-model training data or evaluation split. Unknown is not evidence of absence. Primary-paper retrieval was unavailable or non-content (HTTP 200); exact data require a separate full-paper check.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1016/j.matt.2019.08.017) · [source 2](https://github.com/kaist-amsg/imatgen) · [source 3](https://raw.githubusercontent.com/kaist-amsg/imatgen/master/README.md)

<a id="im2ode"></a>
## IM²ODE

**Swarm and differential evolution · Atomic / inorganic · CSP search / proposal implementation**

[2015 CSP064](https://doi.org/10.1016/j.commatsci.2014.10.054)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper identifies the multi-objective differential-evolution package. Related author-coauthored DFSE repository includes an IM2ODE-derived component, but a standalone original IM²ODE source release was not established; DFSE is supporting evidence, not substituted as the original package URL.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://physics.ecust.edu.cn/_upload/article/files/59/56/bb36e249416cb10e1e3a83d6a0fb/ee775485-26ff-4956-84b0-49f22d50fee8.pdf) · [source 2](https://github.com/icen-tsui/DFSE) · [source 3](https://doi.org/10.1016/j.commatsci.2014.10.054)

<a id="woodley-ga"></a>
## Ionic-crystal genetic algorithm (Woodley et al.)

**Evolutionary and genetic search · Atomic / inorganic · Algorithm described in paper; source not verified**

[1999 CSP007](https://doi.org/10.1039/A901227C)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1039/A901227C)

<a id="ipcsp"></a>
## IPCSP (integer-programming CSP)

**Construction, templates and discrete search · Atomic / inorganic · CSP search / proposal implementation**

[2023 CSP133](https://doi.org/10.1038/s41586-023-06071-y)

**Source / access:** [Code](https://github.com/lrcfmd/ipcsp) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/lrcfmd/ipcsp/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Garnet Ca3Al2Si3O12 and spinel MgAl2O4](https://doi.org/10.1038/s41586-023-06071-y) — Integer-program allocation followed by local minimization. Primary paper Figure 2; energetic guarantees depend on stated lattice/potential assumptions

Primary Code availability explicitly links implementation of periodic lattice allocation and subsequent CSP. Optimality guarantees apply under the declared discretization and energy-model assumptions.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41586-023-06071-y) · [source 2](https://github.com/lrcfmd/ipcsp) · [source 3](https://github.com/lrcfmd/ipcsp/blob/main/LICENSE) · [source 4](https://github.com/lrcfmd/ipcsp/blob/main/README.md) · [source 5](https://doi.org/10.1038/s41586-023-06071-y)

<a id="kldm"></a>
## KLDM

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP172](https://proceedings.mlr.press/v267/cornet25a.html)

**Source / access:** [Code](https://github.com/frcnt/kldm) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/frcnt/kldm/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author train_csp_mp_20 preprocessing recipe, described as usual splits; no independent split comparison.

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://proceedings.mlr.press/v267/cornet25a.html) · [source 2](https://github.com/frcnt/kldm) · [source 3](https://raw.githubusercontent.com/frcnt/kldm/main/README.md) · [source 4](https://raw.githubusercontent.com/frcnt/kldm/main/LICENSE)

<a id="m3gnet"></a>
## M3GNet

**Context, evaluators and evaluation · Atomic / inorganic · Enabling evaluator**

[2022 CSP109](https://www.nature.com/articles/s43588-022-00349-3)

**Source / access:** [Code](https://github.com/materialyzeai/m3gnet) — Public source repository

**License:** Open-source license verified [BSD-3-Clause](https://github.com/materialyzeai/m3gnet/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Original TensorFlow M3GNet pretrained models](https://github.com/materialyzeai/m3gnet/tree/main/pretrained) — Main model / Public download

**Training data:**
- [Materials Project force dataset MPF.2021.2.8](https://figshare.com/articles/dataset/MPF_2021_2_8/19470599) — Main model training. MPF.2021.2.8; README example splits compounds 90/5/5 with seed 42; example not certified as exact original paper split

**Reference data:**
No separate item verified.

**Evaluation:**
- [Cubic crystal lattice/energy comparisons](https://github.com/materialyzeai/m3gnet/blob/main/examples/Cubic%20Crystal%20Test.ipynb) — Lattice constants and energies versus DFT/experimental references. Cubic crystals only; author notebook

Universal interatomic potential / relaxation evaluator; search candidates must come from a separate algorithm. Former materialsvirtuallab repository redirects to materialyzeai/m3gnet.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s43588-022-00349-3) · [source 2](https://github.com/materialsvirtuallab/m3gnet) · [source 3](https://github.com/materialyzeai/m3gnet) · [source 4](https://github.com/materialyzeai/m3gnet/blob/main/LICENSE) · [source 5](https://github.com/materialyzeai/m3gnet/tree/main/pretrained) · [source 6](https://github.com/materialyzeai/m3gnet/blob/main/README.md)

<a id="magus"></a>
## MAGUS

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2025 CSP170](https://doi.org/10.1038/s43588-025-00775-z)

**Source / access:** [Project](https://gitlab.com/bigd4/magus) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [MgAl2O4, gamma-boron, phosphorus allotropes and Si(111)-(7×7)](https://doi.org/10.1038/s43588-025-00775-z) — Symmetry-principle MAGUS optimization. 2025 method-specific tests; paper-defined benchmarks, not a standardized CSP corpus

Developer GitLab public README identifies Jian Sun group and the 2025 paper, but How to get access explicitly requires registration and invitation before full source can be seen. GitLab link is a project/access portal, not a verified public source repository. Registration endpoint: https://table.nju.edu.cn/dtable/forms/custom/magus/.

Core symmetry/group/graph-guided evolutionary generator is non-trained; optional learned potentials can be used but their datasets were not established for these reported tests.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://gitlab.com/bigd4/magus) · [source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10275355/) · [source 3](https://doi.org/10.1038/s43588-025-00775-z) · [source 4](https://www.nature.com/articles/s43588-025-00775-z)

<a id="maise"></a>
## MAISE

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2021 CSP106](https://doi.org/10.1016/j.cpc.2020.107679)

**Source / access:** [Code](https://github.com/maise-guide/maise) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/maise-guide/maise/blob/master/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm
- [MAISE system-specific pretrained NNs](https://github.com/maise-guide/maise/tree/master/models) — Optional evaluator / Hosted API

**Training data:**
- [MAISE system-specific DFT energies and forces](https://github.com/maise-guide/maise) — Main model training. Evolutionary sampling and stratified NN training; user/system-specific dataset, not a single fixed general corpus

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Developer repository identifies Kolmogorov, Hajinazar and Sandoval; combines neural interatomic modeling and evolutionary optimization. Source availability does not establish accuracy for an arbitrary new chemical system.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/maise-guide/maise) · [source 2](https://arxiv.org/abs/2005.12131) · [source 3](https://github.com/maise-guide/maise/blob/master/LICENSE) · [source 4](https://github.com/maise-guide/maise/tree/master/models) · [source 5](https://github.com/maise-guide/maise/blob/master/README.md) · [source 6](https://doi.org/10.1016/j.cpc.2020.107679)

<a id="mat2seq-airs"></a>
## Mat2Seq (AIRS)

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP149](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html)

**Source / access:** [Code](https://github.com/divelab/AIRS/tree/main/OpenMat/Mat2Seq) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://raw.githubusercontent.com/divelab/AIRS/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Mat2Seq pretrained model](https://figshare.com/ndownloader/files/58362571?private_link=6de7df4e6507e3fb6c53) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Official AIRS subproject, also linked by named author Keqiang Yan; keep distinct from SyMat despite shared monorepo.

Explicit author data/training instructions establish usage. MP-20 and MPTS-52 are distinct protocols; shared dataset names do not prove identical preprocessing or splits across implementations.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html) · [source 2](https://github.com/divelab/AIRS/tree/main/OpenMat/Mat2Seq) · [source 3](https://raw.githubusercontent.com/divelab/AIRS/main/OpenMat/Mat2Seq/README.md) · [source 4](https://raw.githubusercontent.com/divelab/AIRS/main/LICENSE) · [source 5](https://figshare.com/ndownloader/files/58362571?private_link=6de7df4e6507e3fb6c53)

<a id="mattergen"></a>
## MatterGen

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2025 CSP159](https://www.nature.com/articles/s41586-025-08628-5)

**Source / access:** [Code](https://github.com/microsoft/mattergen) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/microsoft/mattergen/main/LICENSE)

**Pretrained model:** Public pretrained download
- [MatterGen base and property-finetuned models](https://huggingface.co/microsoft/mattergen) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. mp_20_base trained MP-20; mattergen_base trained Alex-MP-20; keep base/condition-fine-tuned model data separate.
- [Alex-MP-20](https://github.com/microsoft/mattergen/tree/main/datasets) — Main model training. mp_20_base trained MP-20; mattergen_base trained Alex-MP-20; keep base/condition-fine-tuned model data separate.

**Reference data:**
- [MP2020 stability/novelty reference](https://github.com/microsoft/mattergen) — Reference / search database. Evaluation reference dataset; optional TRI2024 correction/reference workflow is distinct from base-model training.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — De novo generation, stable/unique/novel fractions, conditional property targeting. Author generation/evaluation scripts; relaxation/reference energy corrections must agree. Current MP2020 and TRI2024 evaluation schemes differ.
- [Alex-MP-20](https://github.com/microsoft/mattergen/tree/main/datasets) — De novo generation, stable/unique/novel fractions, conditional property targeting. Author generation/evaluation scripts; relaxation/reference energy corrections must agree. Current MP2020 and TRI2024 evaluation schemes differ.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41586-025-08628-5) · [source 2](https://github.com/microsoft/mattergen) · [source 3](https://raw.githubusercontent.com/microsoft/mattergen/main/README.md) · [source 4](https://raw.githubusercontent.com/microsoft/mattergen/main/LICENSE) · [source 5](https://huggingface.co/microsoft/mattergen)

<a id="mc-emma"></a>
## MC-EMMA

**Energy-landscape exploration · Atomic / inorganic · CSP search / proposal implementation**

[2017 CSP070](https://doi.org/10.1038/nature22374)

**Source / access:** [Code](https://github.com/lrcfmd/MC-EMMA-stable) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/lrcfmd/MC-EMMA-stable/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author research-group stable implementation is linked by the later RL-CSP paper and repository. It is a later public distribution of the MC-EMMA workflow, not necessarily the exact 2017 snapshot.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pubs.rsc.org/en/content/articlehtml/2023/dd/d3dd00063j) · [source 2](https://github.com/lrcfmd/rlcsp) · [source 3](https://github.com/lrcfmd/MC-EMMA-stable) · [source 4](https://github.com/lrcfmd) · [source 5](https://github.com/lrcfmd/MC-EMMA-stable/blob/main/LICENSE) · [source 6](https://doi.org/10.1038/nature22374)

<a id="minima-hopping"></a>
## Minima Hopping (Goedecker-group Python implementation)

**Energy-landscape exploration · Atomic / inorganic · CSP search / proposal implementation**

[2004 CSP020](https://doi.org/10.1063/1.1724816) · [2010 CSP042](https://doi.org/10.1063/1.3512900)

**Source / access:** [Code](https://gitlab.com/goedeckergroup/ase_mh) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://gitlab.com/goedeckergroup/ase_mh/-/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Lennard-Jones clusters and model silicon](https://edoc.unibas.ch/95451/1/20230811123429_64d60eb59705f.pdf) — Global minimum search. Original 2004 paper numerical tests; exact implementation equivalence with current Python wrapper not asserted

Developer-group implementation supports variable-cell bulk searches and cites original 2004 method. This is the later ASE-compatible implementation, not a claim that original 2004/2010 archived code is identical. Developer GitHub mirror is https://github.com/KrumaKruma/MinimaHopping.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://python-minima-hopping.readthedocs.io/en/stable/index.html) · [source 2](https://github.com/KrumaKruma/MinimaHopping) · [source 3](https://gitlab.com/goedeckergroup/ase_mh) · [source 4](https://python-minima-hopping.readthedocs.io/en/stable/) · [source 5](https://gitlab.com/goedeckergroup/ase_mh/-/blob/main/LICENSE) · [source 6](https://doi.org/10.1063/1.1724816) · [source 7](https://doi.org/10.1063/1.3512900) · [source 8](https://arxiv.org/abs/1007.2003) · [source 9](https://edoc.unibas.ch/95451/1/20230811123429_64d60eb59705f.pdf)

<a id="mlatticeabc"></a>
## MLatticeABC

**Context, evaluators and evaluation · Atomic / inorganic · Enabling predictor / evaluation**

[2021 MLatticeABC2021](https://doi.org/10.1021/acsomega.1c00781)

**Source / access:** [Code](https://github.com/usccolumbia/MLatticeABC) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/usccolumbia/MLatticeABC/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Materials Project-derived descriptor dataset](https://figshare.com/s/1411919c94be680136cd) — Main model training. See author README for feature files and split

**Reference data:**
No separate item verified.

**Evaluation:**
- [Paper evaluation and author examples](https://github.com/usccolumbia/MLatticeABC/blob/main/README.md) — Paper-defined evaluation. See paper and README; exact dataset payload not independently checked.

Random-forest lattice prediction from composition descriptors and atom-count features. Component accuracy is not complete CSP recovery.

Author README inspected; model and dataset payloads were not downloaded or executed.

**Checked:** 2026-10-17. **Evidence:** [source 1](https://doi.org/10.1021/acsomega.1c00781) · [source 2](https://github.com/usccolumbia/MLatticeABC/blob/main/README.md)

<a id="bazterra-modified-ga"></a>
## Modified genetic algorithm for molecular crystals (Bazterra–Ferraro–Facelli)

**Evolutionary and genetic search · Molecular / organic · Method**

[2002 CSP015](https://doi.org/10.1063/1.1458547) · [2003 CSP016](https://doi.org/10.1002/qua.10726)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Two method papers consolidated. No source repository or official software download verified; this does not assert that no implementation exists.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1063/1.1458547) · [source 2](https://doi.org/10.1002/qua.10726)

<a id="mol-cspy"></a>
## mol-CSPy: quasi-random sampling, QRBH and threshold MC

**Random structure search · Molecular / organic · Method**

[2016 CSP066](https://doi.org/10.1021/acs.jctc.5b01112) · [2021 CSP104](https://doi.org/10.1021/acs.jctc.0c01101) · [2022 CSP116](https://doi.org/10.1038/s42004-022-00705-4) · [2023 CSP136](https://doi.org/10.1073/pnas.2300516120)

**Source / access:** [Code](https://gitlab.com/mol-cspy/mol-cspy) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://mol-cspy.readthedocs.io/en/stable/license.html)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official Day-group repository and installation docs verified. Documentation cites the 2016 quasi-random paper and provides cspy-qrbh and cspy-threshold commands. Historical paper linkage identifies the implemented algorithm family; code identity with every paper-time internal version was not verified. Some external dependencies and CSD data require separate access.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://mol-cspy.readthedocs.io/en/stable/installation.html) · [source 2](https://mol-cspy.readthedocs.io/en/stable/bb_wikipages/Papers.html) · [source 3](https://mol-cspy.readthedocs.io/en/stable/commands/threshold.html) · [source 4](https://doi.org/10.1021/acs.jctc.5b01112) · [source 5](https://doi.org/10.1021/acs.jctc.0c01101) · [source 6](https://doi.org/10.1038/s42004-022-00705-4) · [source 7](https://doi.org/10.1073/pnas.2300516120) · [source 8](https://mol-cspy.readthedocs.io/en/stable/license.html)

<a id="molxtalnet-mxtaltools"></a>
## MolXtalNet-D / MolXtalNet-S (MXtalTools)

**Context, evaluators and evaluation · Molecular / organic · Enabling evaluator**

[2023 CSP132](https://doi.org/10.1021/acs.jctc.3c00031)

**Source / access:** [Code](https://github.com/InfluenceFunctional/MXtalTools) — Public source repository

**License:** Open-source license verified [BSD-3-Clause](https://raw.githubusercontent.com/InfluenceFunctional/MXtalTools/master/LICENSE)

**Pretrained model:** Public pretrained download
- [MXtalTools density/scoring/autoencoder checkpoints](https://github.com/InfluenceFunctional/MXtalTools/tree/master/checkpoints) — Main model / Public download

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author repository explicitly cites the 2023 paper and supplies molecular-crystal building, density, scoring and search tools. The paper’s MolXtalNet models are enabling density/plausibility predictors, not demonstrated complete global-CSP solvers. Rebuilding CSD datasets requires a CCDC license.

Bounded check of author repository/paper sources; exact main-model training data and evaluation protocol not established in inspected source. Not verified is not a claim of absence.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/InfluenceFunctional/MXtalTools) · [source 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10373482/) · [source 3](https://doi.org/10.1021/acs.jctc.3c00031) · [source 4](https://raw.githubusercontent.com/InfluenceFunctional/MXtalTools/master/README.md) · [source 5](https://raw.githubusercontent.com/InfluenceFunctional/MXtalTools/master/LICENSE) · [source 6](https://github.com/InfluenceFunctional/MXtalTools/tree/master/checkpoints)

<a id="muse"></a>
## MUSE

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2014 CSP060](https://doi.org/10.1016/j.cpc.2014.03.017)

**Source / access:** [Code](https://github.com/zhongliliu/muse) — Public source repository

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Author Zhong-Li Liu repository cites the MUSE paper and links its SourceForge distribution. Hybrid evolutionary, simulated-annealing and basin-hopping search.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/zhongliliu/muse) · [source 2](https://arxiv.org/abs/1303.2802) · [source 3](https://sourceforge.net/projects/pymuse/) · [source 4](https://doi.org/10.1016/j.cpc.2014.03.017)

<a id="nextcrystal"></a>
## NextCrystal

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2026 CSP189](https://arxiv.org/abs/2602.17176v4)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Paper explicitly uses same train/validation/test splits as DiffCSP++; v4 paper. No code/data release independently verified.
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Paper explicitly uses same train/validation/test splits as DiffCSP++; v4 paper. No code/data release independently verified.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Paper explicitly uses same train/validation/test splits as DiffCSP++; v4 paper. No code/data release independently verified.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Composition-conditioned CSP, Top-20 SUN and structure matching. Paper compares official DiffCSP++ reproduction with CSPML space-group retrieval; HfO2 first-principles application separate.
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Composition-conditioned CSP, Top-20 SUN and structure matching. Paper compares official DiffCSP++ reproduction with CSPML space-group retrieval; HfO2 first-principles application separate.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Composition-conditioned CSP, Top-20 SUN and structure matching. Paper compares official DiffCSP++ reproduction with CSPML space-group retrieval; HfO2 first-principles application separate.

Primary v4 preprint checked; no paper-specific author source release verified. Its cited DiffCSP++ backbone repository is not evidence that NextCrystal training and constrained-assignment code is released.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2602.17176v4) · [source 2](https://arxiv.org/html/2602.17176v4)

<a id="omatg"></a>
## OMatG

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP173](https://proceedings.mlr.press/v267/hollmer25a.html)

**Source / access:** [Code](https://github.com/FERMat-ML/OMatG) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/FERMat-ML/OMatG/main/LICENSE)

**Pretrained model:** Public pretrained download
- [OMatG checkpoint organization](https://huggingface.co/OMatG) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. OMatG published/config-supported corpora; Alex-MP-20 new split takes 10% training data for test; polymorph split groups same-composition structures. Exact per-paper experiment assignment in config.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. OMatG published/config-supported corpora; Alex-MP-20 new split takes 10% training data for test; polymorph split groups same-composition structures. Exact per-paper experiment assignment in config.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. OMatG published/config-supported corpora; Alex-MP-20 new split takes 10% training data for test; polymorph split groups same-composition structures. Exact per-paper experiment assignment in config.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. OMatG published/config-supported corpora; Alex-MP-20 new split takes 10% training data for test; polymorph split groups same-composition structures. Exact per-paper experiment assignment in config.
- [Alex-MP-20 OMatG split](https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter) — Main model training. OMatG published/config-supported corpora; Alex-MP-20 new split takes 10% training data for test; polymorph split groups same-composition structures. Exact per-paper experiment assignment in config.
- [Alex-MP-20 polymorph-aware split](https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter) — Main model training. OMatG published/config-supported corpora; Alex-MP-20 new split takes 10% training data for test; polymorph split groups same-composition structures. Exact per-paper experiment assignment in config.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — CSP/DNG; structure-matching and distribution benchmark robustness. CSP match rate/RMSD and optional match-everyone-to-reference; validation can filter denominator. 4,330 duplicate-pruned Carbon-24 structures with enantiomorphs and 160-structure chiral toy set are distinct variants.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — CSP/DNG; structure-matching and distribution benchmark robustness. CSP match rate/RMSD and optional match-everyone-to-reference; validation can filter denominator. 4,330 duplicate-pruned Carbon-24 structures with enantiomorphs and 160-structure chiral toy set are distinct variants.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — CSP/DNG; structure-matching and distribution benchmark robustness. CSP match rate/RMSD and optional match-everyone-to-reference; validation can filter denominator. 4,330 duplicate-pruned Carbon-24 structures with enantiomorphs and 160-structure chiral toy set are distinct variants.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — CSP/DNG; structure-matching and distribution benchmark robustness. CSP match rate/RMSD and optional match-everyone-to-reference; validation can filter denominator. 4,330 duplicate-pruned Carbon-24 structures with enantiomorphs and 160-structure chiral toy set are distinct variants.
- [Carbon-24-unique-with-enantiomorphs / Carbon-enantiomorphs](https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter) — CSP/DNG; structure-matching and distribution benchmark robustness. CSP match rate/RMSD and optional match-everyone-to-reference; validation can filter denominator. 4,330 duplicate-pruned Carbon-24 structures with enantiomorphs and 160-structure chiral toy set are distinct variants.
- [Alex-MP-20 polymorph-aware split](https://huggingface.co/collections/colabfit/datasets-all-that-structure-matches-does-not-glitter) — CSP/DNG; structure-matching and distribution benchmark robustness. CSP match rate/RMSD and optional match-everyone-to-reference; validation can filter denominator. 4,330 duplicate-pruned Carbon-24 structures with enantiomorphs and 160-structure chiral toy set are distinct variants.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://proceedings.mlr.press/v267/hollmer25a.html) · [source 2](https://github.com/FERMat-ML/OMatG) · [source 3](https://raw.githubusercontent.com/FERMat-ML/OMatG/main/README.md) · [source 4](https://raw.githubusercontent.com/FERMat-ML/OMatG/main/LICENSE) · [source 5](https://huggingface.co/OMatG)

<a id="opencsp-crystal-prediction"></a>
## OpenCSP (crystal prediction)

**Context, evaluators and evaluation · Atomic / inorganic · Enabling evaluator**

[2026 CSP190](https://www.nature.com/articles/s41524-026-02180-0)

**Source / access:** [Project](https://www.nature.com/articles/s41524-026-02180-0) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [OpenCSP-data](https://www.aissquare.com/datasets/detail?pageType=datasets&name=OpenCSP&id=369) — Main model training. 1,522,206 configurations; train/validation/test 8:1:1; test chemical compositions distinct from train/validation

**Reference data:**
No separate item verified.

**Evaluation:**
- [OpenCSP-data held-out split](https://www.nature.com/articles/s41524-026-02180-0) — Energy/force/virial error prediction. Composition-disjoint 10% test split; 8:1:1 train/validation/test
- [MPTrj-S and MPTrj-L](https://www.nature.com/articles/s41524-026-02180-0) — Cross-dataset generalization. 500 configurations each below/above 32 atoms; exclude shared compositions; ABACUS relabeling
- [Variable-pressure random-structure relaxation and CSP](https://www.nature.com/articles/s41524-026-02180-0) — Pressure control and on-hull recovery. Paper-defined FIRE/ExpCellFilter and LBFGS/UnitCellFilter protocols at 0–200 GPa

Publisher explicitly states the remaining workflow scripts are available from authors upon request. AIS Square links provide data/models, not a standalone full source release; Sandia OpenCSP is an unrelated concentrating-solar-power project.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-026-02180-0)

<a id="oxtal"></a>
## OXtal

**Learned generation and conditional CSP · Molecular / organic · Method**

[2025 CSP174](https://arxiv.org/abs/2512.06987)

**Source / access:** [Code](https://github.com/OXtal/OXtal) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/OXtal/OXtal/blob/main/LICENSE-SOURCE-CODE)

**Pretrained model:** Public pretrained download
- [OXtal model card and weights](https://huggingface.co/OXtal-CSP/OXtal) — Main model / Public download

**Training data:**
- [Cambridge Structural Database molecular-crystal data](https://www.ccdc.cam.ac.uk/solutions/software/csd/) — Main model training. Author CSD-derived model dataset; exact version/filter/split not established by README

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper and project link the author repository. All-atom diffusion accepts molecular graphs/SMILES or SDF and co-crystal component counts; unit cell is recovered downstream from generated shells. This is molecular-identity conditioning, not just an inorganic elemental formula.

CSD-derived training explicitly documented. Model weights and source code use different licenses; a public code repository does not make CSD training structures freely redistributable.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/html/2512.06987) · [source 2](https://github.com/OXtal/OXtal) · [source 3](https://www.futurehouse.org/research/oxtal) · [source 4](https://arxiv.org/abs/2512.06987) · [source 5](https://raw.githubusercontent.com/OXtal/OXtal/main/README.md) · [source 6](https://github.com/OXtal/OXtal/blob/main/LICENSE-SOURCE-CODE) · [source 7](https://huggingface.co/OXtal-CSP/OXtal) · [source 8](https://raw.githubusercontent.com/OXtal/OXtal/main/LICENSE-SOURCE-CODE) · [source 9](https://raw.githubusercontent.com/OXtal/OXtal/main/LICENSE-MODEL-WEIGHTS)

<a id="packflow-molecular"></a>
## PackFlow

**Learned generation and conditional CSP · Molecular / organic · Method**

[2026 CSP191](https://arxiv.org/abs/2602.20140)

**Source / access:** [Code](https://github.com/learningmatter-mit/packflow) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/learningmatter-mit/packflow/main/LICENSE)

**Pretrained model:** Public pretrained download
- [PackFlow model zoo checkpoints](https://huggingface.co/aksub99/packflow-checkpoints) — Main model / Public download

**Training data:**
- [Cambridge Structural Database molecular-crystal data](https://www.ccdc.cam.ac.uk/solutions/software/csd/) — Main model training. Author CSD-derived model dataset; exact version/filter/split not established by README

**Reference data:**
No separate item verified.

**Evaluation:**
- [PackFlow held-out CSD and blind-test refcodes](https://github.com/learningmatter-mit/packflow/tree/main/data/refcodes) — Molecular crystal packing generation. README ships train/validation/test and blind-test CSD refcodes; refcodes are not the full dataset

Paper Code availability and author README agree on repository. Molecular-graph-conditioned flow matching with optional RL physics alignment. Source and weights have different licenses according to README; CSD preprocessing and commercial weight use have additional access terms. Avoid unrelated Packflow packages.

CSD-derived training explicitly documented. Model weights and source code use different licenses; a public code repository does not make CSD training structures freely redistributable.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/html/2602.20140) · [source 2](https://github.com/learningmatter-mit/packflow) · [source 3](https://arxiv.org/abs/2602.20140) · [source 4](https://raw.githubusercontent.com/learningmatter-mit/packflow/main/README.md) · [source 5](https://raw.githubusercontent.com/learningmatter-mit/packflow/main/LICENSE) · [source 6](https://huggingface.co/aksub99/packflow-checkpoints) · [source 7](https://raw.githubusercontent.com/learningmatter-mit/packflow/main/packflow/checkpoints/README.md) · [source 8](https://raw.githubusercontent.com/learningmatter-mit/packflow/main/packflow/checkpoints/model_zoo.json)

<a id="paretocsp"></a>
## ParetoCSP

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2024 CSP141](https://www.oaepublish.com/articles/jmi.2023.33)

**Source / access:** [Code](https://github.com/sadmanomee/ParetoCSP) — Public source repository

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm
- [M3GNet pretrained energy evaluator](https://github.com/materialyzeai/m3gnet/tree/main/pretrained) — Optional evaluator / Hosted API

**Training data:**
- [M3GNet evaluator MPF.2021.2.8](https://figshare.com/articles/dataset/MPF_2021_2_8/19470599) — Required component training. Original ParetoCSP uses pretrained M3GNet; evaluator training only

**Reference data:**
No separate item verified.

**Evaluation:**
- [ParetoCSP 55-structure test set](https://www.oaepublish.com/articles/jmi.2023.33) — Crystal recovery and structural-error metrics. 55 diverse structures and seven metrics; exact author files/splits not verified

Primary paper explicitly identifies author source code; age-fitness Pareto evolutionary search with learned energy evaluation.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.oaepress.com/articles/jmi.2023.33) · [source 2](https://github.com/sadmanomee/ParetoCSP) · [source 3](https://github.com/materialyzeai/m3gnet/tree/main/pretrained) · [source 4](https://github.com/sadmanomee/ParetoCSP/blob/main/README.md) · [source 5](https://www.oaepublish.com/articles/jmi.2023.33) · [source 6](https://github.com/materialyzeai/m3gnet/blob/main/README.md)

<a id="paretocsp2"></a>
## ParetoCSP2

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2025 CSP175](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792)

**Source / access:** [Code](https://github.com/usccolumbia/ParetoCSP2) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/usccolumbia/ParetoCSP2/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [SrTiO3 README CSP and polymorphism example](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792) — Runnable author CSP/polymorph usage example; reported success not inferred. Author README commands specify population 100, 500 generations; usage demonstration, not assumed paper benchmark

Author repository is titled Polymorphism CSP and cites adaptive space-group diversity work. Separate code from original ParetoCSP.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/usccolumbia/ParetoCSP2) · [source 2](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202510792) · [source 3](https://github.com/usccolumbia/ParetoCSP2/blob/main/LICENSE) · [source 4](https://github.com/usccolumbia/ParetoCSP2/blob/main/README.md)

<a id="periodic-ga-abraham-probert"></a>
## Periodic real-space genetic algorithm (Abraham–Probert)

**Evolutionary and genetic search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2006 CSP026](https://doi.org/10.1103/PhysRevB.73.224104) · [2008 CSP037](https://doi.org/10.1103/PhysRevB.77.134117)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Lennard-Jones fcc/hcp-commensurate cells and carbon polymorphs](https://doi.org/10.1103/PhysRevB.73.224104) — Periodic real-space genetic optimization. Original abstract reports bulk convergence and carbon lonsdaleite/graphite-like structures; exact settings not verified

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1103/PhysRevB.73.224104) · [source 2](https://doi.org/10.1103/PhysRevB.77.134117)

<a id="tetrahedral-framework-enumeration"></a>
## Periodic tetrahedral-framework enumeration (Treacy et al.)

**Construction, templates and discrete search · Atomic / inorganic · Algorithm described in paper; source not verified**

[1997 CSP004](https://doi.org/10.1524/zkri.1997.212.11.768) · [2004 CSP019](https://doi.org/10.1016/j.micromeso.2004.06.013)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1524/zkri.1997.212.11.768) · [source 2](https://doi.org/10.1016/j.micromeso.2004.06.013)

<a id="pgcgm"></a>
## PGCGM

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2023 CSP134](https://www.nature.com/articles/s41524-023-00987-9)

**Source / access:** [Code](https://github.com/MilesZhao/PGCGM) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/MilesZhao/PGCGM/main/LICENSE)

**Pretrained model:** Public pretrained download
- [Released generator weights](https://github.com/MilesZhao/PGCGM/blob/main/models/frac12/generator_weights.pth) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP/ICSD/OQMD ternary PGCGM corpus](https://www.nature.com/articles/s41524-023-00987-9) — Main model training. Paper curates 42072 ternary materials covering 20 space groups / five crystal systems; OQMD v1.4. Exact author split not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [PGCGM generated-crystal DFT validation](https://www.nature.com/articles/s41524-023-00987-9) — Symmetry-constrained crystal generation. Paper selected generated crystals relaxed/validated with DFT; successful relaxation is distinct from thermodynamic stability.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-023-00987-9) · [source 2](https://github.com/MilesZhao/PGCGM) · [source 3](https://raw.githubusercontent.com/MilesZhao/PGCGM/main/README.md) · [source 4](https://raw.githubusercontent.com/MilesZhao/PGCGM/main/LICENSE) · [source 5](https://github.com/MilesZhao/PGCGM/blob/main/models/frac12/generator_weights.pth)

<a id="phasebo"></a>
## PhaseBO

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2024 CSP147](https://doi.org/10.1063/5.0180818)

**Source / access:** [Code](https://github.com/lrcfmd/PhaseBO) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/lrcfmd/PhaseBO/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [PhaseBO observed compositions and total energies](https://github.com/lrcfmd/PhaseBO) — Main model training. User-supplied CSV; BO updates from phase-field energy observations; example LiSnSCl_700eV.csv

**Reference data:**
No separate item verified.

**Evaluation:**
- [Li–Sn–S–Cl README example](https://doi.org/10.1063/5.0180818) — Bayesian phase-field composition search. Author default input_config.yaml and composition-energy CSV; example usage rather than independently validated outcome

Outer Bayesian search over composition; inner crystal search and its evaluator are supplied separately.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1063/5.0180818) · [source 2](https://github.com/lrcfmd/PhaseBO) · [source 3](https://www.liverpool.ac.uk/chemistry/research/rosseinsky-group/research/open-source-tools/) · [source 4](https://github.com/lrcfmd/PhaseBO/blob/main/LICENSE) · [source 5](https://github.com/lrcfmd/PhaseBO/blob/main/README.md)

<a id="pyxtal"></a>
## PyXtal

**Random structure search · Atomic / inorganic · Symmetry generation / analysis library**

[2021 CSP107](https://doi.org/10.1016/j.cpc.2020.107810)

**Source / access:** [Code](https://github.com/MaterSim/PyXtal) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/MaterSim/PyXtal/blob/master/LICENSE.txt)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Developer repository identifies Qiang Zhu and Scott Fredericks and cites the 2020 library paper. Current canonical repository redirects from older qzhu2017 namespace. Symmetry generation is a proposal/library component, although package also exposes optimization workflows.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://github.com/MaterSim/PyXtal) · [source 2](https://pyxtal.readthedocs.io/) · [source 3](https://github.com/MaterSim/PyXtal/blob/master/LICENSE.txt) · [source 4](https://github.com/MaterSim/PyXtal/blob/master/README.md) · [source 5](https://doi.org/10.1016/j.cpc.2020.107810)

<a id="randspg"></a>
## RandSpg

**Random structure search · Atomic / inorganic · Symmetry-constrained proposal component**

[2017 CSP072](https://doi.org/10.1016/j.cpc.2016.12.005)

**Source / access:** [Code](https://github.com/xtalopt/randSpg) — Public source repository

**License:** Open-source license verified [BSD-3-Clause](https://github.com/xtalopt/randSpg/blob/master/COPYING)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official XtalOpt resource page attributes RandSpg to Patrick Avery and links source. Composition- and symmetry-constrained initial structures; not a complete energy-ranking search alone.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://xtalopt.github.io/resources.html) · [source 2](https://github.com/xtalopt/randSpg) · [source 3](https://github.com/xtalopt/randSpg/blob/master/COPYING) · [source 4](https://doi.org/10.1016/j.cpc.2016.12.005)

<a id="rl-csp"></a>
## RL-CSP

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2023 CSP137](https://doi.org/10.1039/d3dd00063j)

**Source / access:** [Code](https://github.com/lrcfmd/rlcsp) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/lrcfmd/rlcsp/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [RL-CSP on-the-fly search trajectories](https://github.com/lrcfmd/rlcsp) — Main model training. REINFORCE policy learned during each search; no offline pretraining dataset

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Policy-learning module used with FUSE and MC-EMMA; official paper also links those integration repositories.

Author README explicitly says no pre-training; adaptive policy learns from search actions and rewards on the fly. It must not be assigned a generic Materials Project training corpus.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1039/d3dd00063j) · [source 2](https://github.com/lrcfmd/rlcsp) · [source 3](https://github.com/lrcfmd/rlcsp/blob/main/LICENSE) · [source 4](https://github.com/lrcfmd/rlcsp/blob/main/README.md)

<a id="schrodinger-csp"></a>
## Schrödinger Crystal Structure Prediction

**Random structure search · Molecular / organic · Method**

[2025 CSP161](https://doi.org/10.1038/s41467-025-57479-1)

**Source / access:** [Project](https://www.schrodinger.com/platform/products/ms-crystal-structure-prediction/) — Commercial implementation

**License:** Commercial / controlled source [Commercial license](https://www.schrodinger.com/platform/products/ms-crystal-structure-prediction/)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not verified

**Reference data:**
- [CSD experimental polymorph references](https://www.ccdc.cam.ac.uk/solutions/software/csd/) — Reference / search database. Experimental polymorph structures; preference neutron then low-temperature single-crystal XRD then room-temperature PXRD

**Evaluation:**
- [Retrospective 66-molecule crystal polymorph cohort](https://doi.org/10.1038/s41467-025-57479-1) — Molecular-crystal recovery and ranking. Paper comprehensive 66-molecule validation, with experimental structures mainly from CSD; energy ranking and RMSD cluster matching

Paper Code availability identifies Schrödinger suite 2025-1 and an evaluation license upon request. The bsantra/csp-validation-data repository supplies validation data, not the proprietary CSP solver; therefore it is not listed as source code.

Main-model training data remain unverified. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41467-025-57479-1) · [source 2](https://www.schrodinger.com/platform/products/ms-crystal-structure-prediction/) · [source 3](https://doi.org/10.1038/s41467-025-57479-1)

<a id="sgo"></a>
## SGO

**Swarm and differential evolution · Atomic / inorganic · CSP search / proposal implementation**

[2017 CSP073](https://doi.org/10.1016/j.cpc.2017.05.005)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary methods describe differential evolution plus GPU PWmat evaluation. A public author source repository or source download was not verified; image-download links and PWmat executables are not evidence of SGO source.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.sciencedirect.com/science/article/am/pii/S0010465517301352) · [source 2](https://arxiv.org/abs/1603.02732) · [source 3](https://doi.org/10.1016/j.cpc.2017.05.005)

<a id="shaft"></a>
## SHAFT

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2026 CSP187](https://arxiv.org/abs/2411.04323)

**Source / access:** [Code](https://github.com/ngminhtri0394/SHAFT) — Public source repository

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [MP_Battery](https://github.com/ngminhtri0394/SHAFT) — Required component training. README says MP_Battery trains CDVAE and DiffCSP comparison components; SHAFT policy/proxy exact offline training corpus not established.

**Reference data:**
No separate item verified.

**Evaluation:**
- [SHAFT sampled and DFT-optimized battery candidates](https://github.com/ngminhtri0394/SHAFT) — Battery material candidate discovery. Sampled_structure and DFT_optimized release corresponds to paper Section 5.1.7.

Paper code availability names SHAFT; the oganesson repository mentioned in preprint references is a different supporting package.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2411.04323) · [source 2](https://github.com/ngminhtri0394/SHAFT) · [source 3](https://pubs.rsc.org/en/content/articlehtml/2026/dd/d4dd00392f) · [source 4](https://raw.githubusercontent.com/ngminhtri0394/SHAFT/main/README.md) · [source 5](https://arxiv.org/html/2411.04323)

<a id="shotguncsp"></a>
## ShotgunCSP

**Adaptive and ML-guided search · Atomic / inorganic · Method**

[2024 CSP153](https://www.nature.com/articles/s41524-024-01471-8)

**Source / access:** [Code](https://github.com/TsumiNa/ShotgunCSP) — Public source repository

**License:** Open-source license verified [Apache-2.0](https://github.com/TsumiNa/ShotgunCSP/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Official repo provides template-selection ShotgunCSP-GT; README says symmetry/Wyckoff ShotgunCSP-GW release is anticipated for 2026, so do not infer both generators are released.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-024-01471-8) · [source 2](https://github.com/TsumiNa/ShotgunCSP) · [source 3](https://github.com/TsumiNa/ShotgunCSP/blob/main/LICENSE) · [source 4](https://github.com/TsumiNa/ShotgunCSP/blob/main/README.md)

<a id="cell-metadynamics"></a>
## Simulation-cell metadynamics (Martonak–Laio–Parrinello)

**Energy-landscape exploration · Atomic / inorganic · Algorithm described in paper; source not verified**

[2003 CSP018](https://doi.org/10.1103/PhysRevLett.90.075503) · [2005 CSP025](https://doi.org/10.1524/zkri.220.5.489.65078)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Silicon diamond to simple-hexagonal transition](https://doi.org/10.1103/PhysRevLett.90.075503) — Pressure-induced structural transformation. Simulation-cell edges as metadynamics collective variables; model-silicon validation

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1103/PhysRevLett.90.075503) · [source 2](https://doi.org/10.1524/zkri.220.5.489.65078)

<a id="slices"></a>
## SLICES

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2023 CSP126](https://www.nature.com/articles/s41467-023-42870-7)

**Source / access:** [Code](https://github.com/xiaohang007/SLICES) — Public source repository

**License:** Open-source license verified [LGPL-2.1](https://raw.githubusercontent.com/xiaohang007/SLICES/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [SLICES filtered MP-20](https://doi.org/10.6084/m9.figshare.22707472) — Main model training. Figshare v2: filtered MP-20 40330 crystals augmented to 2009115 strings for ucRNN/cRNN. Separate general 30085 and direct-gap transfer 364 crystals, augmented to 764546 and 11373 strings. These differ from original MP-20 split.
- [SLICES general/semiconductor transfer corpus](https://doi.org/10.6084/m9.figshare.22707472) — Main model training. Figshare v2: filtered MP-20 40330 crystals augmented to 2009115 strings for ucRNN/cRNN. Separate general 30085 and direct-gap transfer 364 crystals, augmented to 764546 and 11373 strings. These differ from original MP-20 split.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Filtered MP-20 reconstruction/generation/property optimization](https://doi.org/10.6084/m9.figshare.22707472) — Representation reconstruction, generative validity and conditional formation-energy optimization. Paper MP-21-40 filters yield 23560 crystals. Generation uses filtered MP-20; narrow-gap semiconductor DFT screening is a separate application.
- [Filtered MP-21-40 reconstruction](https://doi.org/10.6084/m9.figshare.22707472) — Representation reconstruction, generative validity and conditional formation-energy optimization. Paper MP-21-40 filters yield 23560 crystals. Generation uses filtered MP-20; narrow-gap semiconductor DFT screening is a separate application.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41467-023-42870-7) · [source 2](https://github.com/xiaohang007/SLICES) · [source 3](https://raw.githubusercontent.com/xiaohang007/SLICES/main/README.md) · [source 4](https://raw.githubusercontent.com/xiaohang007/SLICES/main/LICENSE)

<a id="spade-csp"></a>
## SPaDe-CSP

**Adaptive and ML-guided search · Molecular / organic · Method**

[2025 CSP168](https://doi.org/10.1039/D5DD00304K)

**Source / access:** [Code](https://github.com/takuyhaa/SPaDe-CSP) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/takuyhaa/SPaDe-CSP/main/LICENSE)

**Pretrained model:** Public pretrained download
- [SPaDe-CSP pretrained predictor weights (Git LFS)](https://github.com/takuyhaa/SPaDe-CSP#installation) — Main model / Public download

**Training data:**
- [SPaDe-CSP author molecular-crystal training dataset](https://raw.githubusercontent.com/takuyhaa/SPaDe-CSP/main/README.md) — Main model training. Repository datasets/ contains training and evaluation data; exact source filtering/split not established

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Paper availability statement links author repository and Zenodo archive 10.5281/zenodo.17214315. Learned space-group/packing-density priors guide lattice sampling and ML relaxation. Optional PFP/Matlantis evaluator requires a license; repository access alone does not supply that evaluator.

Model/component training-data usage is listed with role and split qualifications. Evaluation-set attribution remains unverified. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://pubs.rsc.org/en/content/articlepdf/2025/dd/d5dd00304k) · [source 2](https://github.com/takuyhaa/SPaDe-CSP) · [source 3](https://doi.org/10.1039/D5DD00304K) · [source 4](https://raw.githubusercontent.com/takuyhaa/SPaDe-CSP/main/README.md) · [source 5](https://raw.githubusercontent.com/takuyhaa/SPaDe-CSP/main/LICENSE) · [source 6](https://github.com/takuyhaa/SPaDe-CSP#installation)

<a id="spinner"></a>
## SPINNER

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2022 CSP110](https://www.nature.com/articles/s41524-022-00792-w)

**Source / access:** [Code](https://github.com/MDIL-SNU/SPINNER) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://github.com/MDIL-SNU/SPINNER/blob/main/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
- [SPINNER per-composition melt-quench-anneal DFT trajectories](https://www.nature.com/articles/s41524-022-00792-w) — Required component training. SIMPLE-NN potentials; iterative refinement adds DFT-relaxed low-energy structures; exact train/validation indices unverified

**Reference data:**
No separate item verified.

**Evaluation:**
- [SPINNER 60-ternary blind tests](https://www.nature.com/articles/s41524-022-00792-w) — Experimental or lower-energy phase recovery. Paper-specific 60 compositions; melt-quench NNP training per composition; exact downloadable test manifest unverified
- [TiO2, P3N5, NbPd3, Li10GeP2S12 and InGaZnO4](https://www.nature.com/articles/s41524-022-00792-w) — Beyond-ternary-system structure recovery. Original paper supplemental tests; ground-state searches around/within 5000 generations

Primary Code availability explicitly links core search code and separate SIMPLE-NN training package. Public core is not automatically a fully automated end-to-end pipeline.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41524-022-00792-w) · [source 2](https://github.com/MDIL-SNU/SPINNER) · [source 3](https://spinner-csp.readthedocs.io/) · [source 4](https://github.com/MDIL-SNU/SPINNER/blob/main/LICENSE) · [source 5](https://github.com/MDIL-SNU/SPINNER/blob/main/README.md)

<a id="ssw-lasp"></a>
## SSW / LASP

**Energy-landscape exploration · Atomic / inorganic · CSP search / proposal implementation**

[2013 CSP058](https://doi.org/10.1021/ct301010b) · [2014 CSP062](https://doi.org/10.1039/C4CP01485E)

**Source / access:** [Project](https://www.lasphub.com/) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Developer software article links SSW to LASP. Primary code-availability statement in later LASP work explicitly identifies an example binary and author-request route. Public LASP source was not verified; do not treat the binary tarball or NN potentials as source code.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.lasphub.com/publication/132.pdf) · [source 2](https://www.lasphub.com/publication/200.pdf) · [source 3](https://www.lasphub.com/) · [source 4](https://doi.org/10.1021/ct301010b) · [source 5](https://doi.org/10.1039/C4CP01485E)

<a id="symat-airs"></a>
## SyMat (AIRS)

**Learned generation and conditional CSP · Atomic / inorganic · Adjacent method**

[2023 CSP138](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html)

**Source / access:** [Code](https://github.com/divelab/AIRS/tree/main/OpenMat/SyMat) — Public source repository

**License:** Open-source license verified [GPL-3.0](https://raw.githubusercontent.com/divelab/AIRS/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Explicit train.py --dataset perov_5 example; other training corpora not assumed from framework.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — De novo crystal generation. Author generation example samples 10,000 structures; exact full paper test protocol requires separate verification.

Official AIRS repository subproject; repository root hosts multiple algorithms, so the direct subproject link is retained.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html) · [source 2](https://github.com/divelab/AIRS/tree/main/OpenMat/SyMat) · [source 3](https://raw.githubusercontent.com/divelab/AIRS/main/OpenMat/SyMat/README.md) · [source 4](https://raw.githubusercontent.com/divelab/AIRS/main/LICENSE)

<a id="symmcd"></a>
## SymmCD

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP178](https://arxiv.org/abs/2502.03638)

**Source / access:** [Code](https://github.com/sibasmarak/SymmCD) — Public source repository

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Author-provided training split; exact counts and split identity not independently compared.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Main model training. Author-provided training split; exact counts and split identity not independently compared.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.
- [MPTS-52](https://github.com/jiaor17/DiffCSP/tree/main/data/mpts_52) — Crystal reconstruction / composition-conditioned CSP and/or de novo generation; task-specific metrics apply.. Author commands compare held-out test.csv structures. CSP match rate/RMSD and de novo validity/coverage/distribution are distinct tasks; consult per-task configuration, not a pooled score.

Author implementation linked by the primary paper or repository; no software execution was performed.

Explicit author data/training instructions establish usage. MP-20 and MPTS-52 are distinct protocols; shared dataset names do not prove identical preprocessing or splits across implementations.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2502.03638) · [source 2](https://github.com/sibasmarak/SymmCD) · [source 3](https://raw.githubusercontent.com/sibasmarak/SymmCD/main/README.md)

<a id="symmetry-driven-random-search"></a>
## Symmetry-driven structure search (Domingos–Shaik–Militzer)

**Random structure search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2018 CSP082](https://doi.org/10.1103/PhysRevB.98.174107)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [(H2O)n–(NaCl)m and CnOm high-pressure compounds](https://doi.org/10.1103/PhysRevB.98.174107) — Symmetry-driven discovery. Paper reports Pnma water–salt and C2O candidate predictions

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1103/PhysRevB.98.174107)

<a id="symmetry-divide-conquer"></a>
## Symmetry-orientated divide-and-conquer CSP

**Construction, templates and discrete search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2022 CSP108](https://doi.org/10.1063/5.0074677)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1063/5.0074677)

<a id="systematic-network-enumeration"></a>
## Systematic crystalline-network enumeration (Delgado Friedrichs et al.)

**Construction, templates and discrete search · Atomic / inorganic · Algorithm described in paper; source not verified**

[1999 CSP006](https://doi.org/10.1038/23210)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1038/23210)

<a id="quotient-graph-search"></a>
## Systematic periodic-network search (Winkler–Pickard–Thimm)

**Construction, templates and discrete search · Atomic / inorganic · Algorithm described in paper; source not verified**

[2001 CSP011](https://doi.org/10.1016/S0009-2614(01)00126-9) · [2004 CSP021](https://doi.org/10.1103/PhysRevB.70.045101)

**Source / access:** No source or access link verified — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Primary paper defines the algorithm. An author-maintained public source repository or source download for this particular implementation was not verified; this label does not mean no code exists. The descriptive entry name is not a claimed software-package name.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://doi.org/10.1016/S0009-2614(01)00126-9) · [source 2](https://doi.org/10.1103/PhysRevB.70.045101)

<a id="tcsp"></a>
## TCSP / TCSP2.0

**Construction, templates and discrete search · Atomic / inorganic · CSP search / proposal implementation**

[2022 CSP123](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879) · [2026 CSP194](https://www.sciencedirect.com/science/article/pii/S0927025625006603)

**Source / access:** [Code](https://github.com/usccolumbia/TCSP) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/usccolumbia/TCSP/blob/main/LICENSE)

**Pretrained model:** Public pretrained download
- [BERTOS oxidation-state checkpoint](https://figshare.com/articles/journal_contribution/BERTOS/28379117) — Required component / Public download

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
- [TCSP2.0 template database](https://figshare.com/articles/dataset/TCSP2_0_database/28379060) — Reference / search database. TCSP2.0 combines MP, Materials Cloud 2D/3D, C2DB and GNoME; not silently assigned to original TCSP

**Evaluation:**
No separate item verified.

TCSP2.0 primary abstract explicitly links this source repository. Repository describes the later TCSP2.0 code and links TCSP1.0 paper; exact original-version snapshot not separately verified.

Template database is a reference/search corpus, not generator training. TCSP and TCSP2.0 consolidated here; current README describes successor database. Any learned embeddings or optional MLIP training provenance remains unverified.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.sciencedirect.com/science/article/abs/pii/S0927025625006603) · [source 2](https://github.com/usccolumbia/TCSP) · [source 3](https://github.com/usccolumbia/TCSP/blob/main/LICENSE) · [source 4](https://figshare.com/articles/journal_contribution/BERTOS/28379117) · [source 5](https://github.com/usccolumbia/TCSP/blob/main/README.md) · [source 6](https://pubs.acs.org/doi/10.1021/acs.inorgchem.1c03879) · [source 7](https://www.sciencedirect.com/science/article/pii/S0927025625006603)

<a id="uflowcsp"></a>
## uFlowCSP

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2026 CSP195](https://arxiv.org/abs/2609.09799)

**Source / access:** [Code](https://github.com/usccolumbia/uFlowCSP) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/usccolumbia/uFlowCSP/main/LICENSE)

**Pretrained model:** Public pretrained download
- [MP20 pretrained checkpoint](https://doi.org/10.6084/m9.figshare.33974422) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Canonical CDVAE/DiffCSP material-ID split 27136/9047/9046 explicitly documented; all.csv via Git LFS.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Composition-conditioned CSP. MP-20 full test and separate known-Z lane; 180-formula lane is separate, its required 180 reference corpus is not shipped and cannot be reconstructed from MP-20 alone.
- [180-formula CSPBench lane](https://github.com/usccolumbia/uFlowCSP/blob/main/180_primitive.csv) — Composition-conditioned CSP. MP-20 full test and separate known-Z lane; 180-formula lane is separate, its required 180 reference corpus is not shipped and cannot be reconstructed from MP-20 alone.

Author repository names the paper arXiv:2609.09799 and the USC authors; no inference was run.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item. Update 17 October 2026: a separate benchmark_deep_csp v3.1 release now provides T180/T46 references. This does not establish identity with the historical uFlowCSP evaluation cohort.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2609.09799) · [source 2](https://github.com/usccolumbia/uFlowCSP) · [source 3](https://raw.githubusercontent.com/usccolumbia/uFlowCSP/main/README.md) · [source 4](https://raw.githubusercontent.com/usccolumbia/uFlowCSP/main/LICENSE) · [source 5](https://doi.org/10.6084/m9.figshare.33974422)

<a id="uni-3dar"></a>
## Uni-3DAR

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2025 CSP179](https://arxiv.org/abs/2503.16278v1)

**Source / access:** [Code](https://github.com/dptech-corp/Uni-3DAR) — Public source repository

**License:** Open-source license verified [MIT](https://raw.githubusercontent.com/dptech-corp/Uni-3DAR/main/LICENSE)

**Pretrained model:** Public pretrained download
- [MP20 DNG / CSP / PXRD and molecular checkpoints](https://huggingface.co/dptech/Uni-3DAR/tree/main) — Main model / Public download (official release instructions; no inference performed)

**Training data:**
- [MP20 Uni-3DAR processed corpus](https://huggingface.co/dptech/Uni-3DAR/tree/main) — Main model training. Separate mp20_data, qm9_data and drug_data releases; DRUG upstream version not independently established in README.
- [QM9 Uni-3DAR processed corpus](https://huggingface.co/dptech/Uni-3DAR/tree/main) — Main model training. Separate mp20_data, qm9_data and drug_data releases; DRUG upstream version not independently established in README.
- [DRUG processed corpus (author label)](https://huggingface.co/dptech/Uni-3DAR/tree/main) — Main model training. Separate mp20_data, qm9_data and drug_data releases; DRUG upstream version not independently established in README.

**Reference data:**
No separate item verified.

**Evaluation:**
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — De novo generation, composition-conditioned CSP and PXRD-guided CSP. Distinct mp20.pt, mp20_csp.pt and mp20_pxrd.pt and test.csv inference scripts; molecular downstream scaffold-OOD tasks are not crystal CSP benchmarks.

Author implementation linked by the primary paper or repository; no software execution was performed.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2503.16278v1) · [source 2](https://github.com/dptech-corp/Uni-3DAR) · [source 3](https://raw.githubusercontent.com/dptech-corp/Uni-3DAR/main/README.md) · [source 4](https://raw.githubusercontent.com/dptech-corp/Uni-3DAR/main/LICENSE) · [source 5](https://huggingface.co/dptech/Uni-3DAR/tree/main)

<a id="unimat"></a>
## UniMat

**Learned generation and conditional CSP · Atomic / inorganic · Method**

[2024 CSP152](https://arxiv.org/abs/2311.09235)

**Source / access:** [Project](https://unified-materials.github.io/unimat/) — No public code verified

**License:** No source license verified 

**Pretrained model:** No pretrained release verified

**Training data:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — Main model training. Original paper standard benchmark comparison; larger-scale corpora not established in this bounded check.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — Main model training. Original paper standard benchmark comparison; larger-scale corpora not established in this bounded check.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — Main model training. Original paper standard benchmark comparison; larger-scale corpora not established in this bounded check.

**Reference data:**
No separate item verified.

**Evaluation:**
- [Perov-5](https://github.com/txie-93/cdvae/tree/main/data/perov_5) — De novo crystal generation. Original paper validity, coverage and property-distribution metrics; larger-scale stability results require their own training/data protocol.
- [Carbon-24](https://github.com/txie-93/cdvae/tree/main/data/carbon_24) — De novo crystal generation. Original paper validity, coverage and property-distribution metrics; larger-scale stability results require their own training/data protocol.
- [MP-20](https://github.com/txie-93/cdvae/tree/main/data/mp_20) — De novo crystal generation. Original paper validity, coverage and property-distribution metrics; larger-scale stability results require their own training/data protocol.

Official author project and primary paper verified; no author source-code release verified in this audit. A demo or project page is not treated as source code.

Model/component training-data usage is listed with role and split qualifications. Evaluation datasets and validation studies are listed with task/protocol qualifications. Parent database access does not establish that the exact author snapshot or split is downloadable; consult each item.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://arxiv.org/abs/2311.09235) · [source 2](https://unified-materials.github.io/unimat/materials/paper.pdf) · [source 3](https://unified-materials.github.io/unimat/) · [source 4](https://proceedings.iclr.cc/paper_files/paper/2024/file/cea5ebedc384c5f4b4ef6b6eb29c197f-Paper-Conference.pdf)

<a id="upack"></a>
## UPACK

**Random structure search · Molecular / organic · Method**

[1999 CSP008](https://doi.org/10.1002/(SICI)1096-987X(199906)20:8<799::AID-JCC6>3.0.CO;2-Z)

**Source / access:** [Project](http://www.crystal.chem.uu.nl/~vaneyck/upack.html) — No public code verified

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Original random molecular-packing package. Its historical author URL is corroborated by the 2019 review, but did not load during this check. The 2022 CSP(aiFF) paper reports UPACK code availability and a SAPT-site patch; a working current source download was not verified. Do not confuse with unrelated executable or .NET packers.

Classical lattice-energy search/minimization is not a pretrained generative model. Any fitted force field, local approximate quantum model, or optional learned evaluator requires separate provenance. Exact evaluated molecular cohort was not verified in the bounded source check. Primary paper access attempted; response status 403 prevented full-text dataset verification.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.nature.com/articles/s41578-019-0101-8) · [source 2](https://www.nature.com/articles/s41467-022-30692-y) · [source 3](https://doi.org/10.1002/(SICI)1096-987X(199906)20:8<799::AID-JCC6>3.0.CO;2-Z)

<a id="uspex"></a>
## USPEX

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2006 CSP027](https://doi.org/10.1063/1.2210932) · [2006 CSP030](https://doi.org/10.1016/j.cpc.2006.07.020) · [2010 CSP044](https://doi.org/10.1016/j.cpc.2010.06.007) · [2012 CSP055](https://doi.org/10.1039/C2CE06642D) · [2013 CSP057](https://doi.org/10.1016/j.cpc.2012.12.009) · [2019 CSP085](https://uspex-team.org/static/file/Podryabinkin-2019.pdf)

**Source / access:** [Project](https://uspex-team.org/documentation.html/uspex/downloads) — Registration or request required

**License:** No source license verified 

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Oxygen, sulphur, carbon, nitrogen and CaCO3 high-pressure phases](https://doi.org/10.1063/1.2210932) — Original USPEX crystal recovery/discovery. 2006 JCP abstract: tests with up to 40 atoms/cell, ionic/covalent/metallic/molecular systems; exact manifest not verified
- [USPEX 2006 CPC known-structure tests](https://uspex-team.org/static/file/CPC-USPEX-2006.pdf) — Stable-structure recovery. Tables 2–3: C, Xe, Si, N, Fe, TiO2, SiO2, Al2O3, MgSiO3, Si2N2O, SrSiN2, urea and Li at specified pressures/cells; separate CPC companion protocol

Official portal requires registration. Recent USPEX25 documentation describes a binary package; this link is a software-access portal, not a verified public source repository. Evolutionary metadynamics and active-learning MTP variants are linked as USPEX workflows, not separate independently verified public releases. Access and redistribution terms differ between historical versions.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://uspex-team.org/documentation.html/uspex/downloads) · [source 2](https://uspex-team.org/static/file/uspex_manual_english_v25.pdf) · [source 3](https://arxiv.org/abs/1105.1729) · [source 4](https://arxiv.org/abs/1211.0591) · [source 5](https://doi.org/10.1063/1.2210932) · [source 6](https://doi.org/10.1016/j.cpc.2006.07.020) · [source 7](https://doi.org/10.1016/j.cpc.2010.06.007) · [source 8](https://doi.org/10.1039/C2CE06642D) · [source 9](https://doi.org/10.1016/j.cpc.2012.12.009) · [source 10](https://uspex-team.org/static/file/Podryabinkin-2019.pdf) · [source 11](https://pubmed.ncbi.nlm.nih.gov/16821993/) · [source 12](https://uspex-team.org/static/file/CPC-USPEX-2006.pdf)

<a id="wren-aviary"></a>
## Wren (aviary)

**Adaptive and ML-guided search · Atomic / inorganic · Adjacent method**

[2022 CSP120](https://www.science.org/doi/10.1126/sciadv.abn4117)

**Source / access:** [Code](https://github.com/CompRhys/aviary) — Public source repository

**License:** Open-source license verified [MIT](https://github.com/CompRhys/aviary/blob/main/LICENSE)

**Pretrained model:** No pretrained release verified

**Training data:**
Not verified

**Reference data:**
No separate item verified.

**Evaluation:**
No separate item verified.

Coordinate-free energy/prototype-screening model; named author Zenodo record links the source repository.

Learned model/component or adaptive surrogate identified; exact training corpus and release-specific split not established in this bounded check. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://www.science.org/doi/10.1126/sciadv.abn4117) · [source 2](https://github.com/CompRhys/aviary) · [source 3](https://zenodo.org/records/6345276) · [source 4](https://github.com/CompRhys/aviary/blob/main/LICENSE) · [source 5](https://github.com/CompRhys/aviary/blob/main/README.md)

<a id="xtalopt"></a>
## XtalOpt (including r7–14)

**Evolutionary and genetic search · Atomic / inorganic · CSP search / proposal implementation**

[2011 CSP052](https://doi.org/10.1016/j.cpc.2011.06.003) · [2011 CSP053](https://doi.org/10.1016/j.cpc.2010.07.048) · [2016 CSP069](https://doi.org/10.1016/j.cpc.2015.09.018) · [2017 CSP074](https://doi.org/10.1016/j.cpc.2017.04.001) · [2018 CSP084](https://doi.org/10.1016/j.cpc.2017.09.011) · [2019 CSP091](https://doi.org/10.1016/j.cpc.2018.11.016) · [2024 CSP158](https://doi.org/10.1016/j.cpc.2024.109306) · [2026 CSP196](https://doi.org/10.1016/j.cpc.2025.109910)

**Source / access:** [Code](https://github.com/xtalopt/XtalOpt) — Public source repository

**License:** Open-source license verified [BSD-3-Clause](https://github.com/xtalopt/XtalOpt/blob/master/LICENSE)

**Pretrained model:** Not applicable — non-trained algorithm

**Training data:**
Not applicable — non-trained algorithm

**Reference data:**
No separate item verified.

**Evaluation:**
- [Original XtalOpt TiO2, SrTiO3 and NaH tests](https://xtalopt.github.io/pub.html) — Evolutionary operator parameterization and crystal recovery. Original 2011 implementation tests; r7 release-note DOI differs; later r7–14 protocols not presumed identical

Consolidates version papers; official download page links developer source repository and release assets. Newest repository contents need not reproduce historical releases.

Core search, enumeration, construction or DFT-screening algorithm does not require a fixed pretrained dataset. Optional evaluators and extensions must be qualified separately. Primary source links retained; named examples are not assumed to be standardized benchmarks.

**Checked:** 2026-10-16. **Evidence:** [source 1](https://xtalopt.github.io/download.html) · [source 2](https://github.com/xtalopt/XtalOpt) · [source 3](https://xtalopt.github.io/) · [source 4](https://github.com/xtalopt/XtalOpt/blob/master/LICENSE) · [source 5](https://github.com/xtalopt/XtalOpt/blob/master/README.md) · [source 6](https://doi.org/10.1016/j.cpc.2011.06.003) · [source 7](https://doi.org/10.1016/j.cpc.2010.07.048) · [source 8](https://doi.org/10.1016/j.cpc.2015.09.018) · [source 9](https://doi.org/10.1016/j.cpc.2017.04.001) · [source 10](https://doi.org/10.1016/j.cpc.2017.09.011) · [source 11](https://doi.org/10.1016/j.cpc.2018.11.016) · [source 12](https://doi.org/10.1016/j.cpc.2024.109306) · [source 13](https://doi.org/10.1016/j.cpc.2025.109910) · [source 14](https://arxiv.org/abs/2506.17246) · [source 15](https://xtalopt.github.io/pub.html)
