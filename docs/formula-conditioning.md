# Exact formula conditioning

An interface audit of 42 generative or hybrid workflows. These are source-qualified capabilities, not runtime tests. Exact cell counts are stronger than reduced-formula ratios or soft prompts.

## CrystalGAN

[CrystalGAN: Learning to Discover Crystallographic Structures with Generative Adversarial Networks](https://ceur-ws.org/Vol-2350/paper18.pdf)

**Needs adaptation** — Restricted binary-to-ternary hydride domain translation; no prescribed cell stoichiometry interface.

CrystalGAN transfers structures between two binary-hydride domains and combines them into a ternary domain; exported species counts are derived from generated arrays.

**Conditions:** Input binary chemical domains, Nearest-neighbor distance constraints

**Adaptation:** Add explicit desired counts and enforce occupancy/coordinate masks during generation and export; chemistry beyond the trained domains also requires new training.

Specified ternary element identities do not specify their multiplicities; no runtime validation performed.

- [Primary workshop full paper](https://ceur-ws.org/Vol-2350/paper18.pdf): Task Description: Exploring Novel Hydrides, p6 (PDF index5) — The experiments translate Pd-H/Ni-H and Mg-H/Ti-H datasets with padded coordinate matrices; no requested per-element count vector is provided.
- [Official source code](https://github.com/asmanouira/CrystalGAN/blob/master/post_processing.py): clean_data and write_POSCAR — Padding is removed by coordinate repetition checks; the POSCAR count line is computed from the lengths of the resulting generated H/M1/M2 arrays rather than a requested formula.

## DD3DCS

[Data-Driven Approach to Encoding and Decoding 3-D Crystal Structures](https://arxiv.org/abs/1909.00949)

**Needs adaptation** — Structure reconstruction/interpolation; formula-only inference not established

VAE density-field decoder and U-Net species segmentation reconstruct complete encoded structures.

**Conditions:** Encoded full crystal; interpolated structural latent

**Adaptation:** Add a formula-conditioned latent prior and count-constrained density-to-atom decoder; this is a proposed extension.

Accurate reconstruction of an input crystal does not establish formula-only CSP. No generation runtime was tested.

- [Official repository](https://github.com/hoffmannjordan/Encoding-Decoding-3D-Crystals): README: Article Description; Data Generation; Crystal-VAE — Describes encoding/decoding density fields and species segmentation; input data are CIFs and latent interpolation, rather than a prescribed formula sampler.

## iMatGen

[Inverse Design of Solid-State Materials via a Continuous Representation](https://doi.org/10.1016/j.matt.2019.08.017)

**Unconditional-only documented** — V–O domain; variable stoichiometry from latent sampling

Hierarchical autoencoders decode sampled or interpolated material latent vectors into density images; atom identities/counts are extracted afterward.

**Conditions:**

**Adaptation:** Add formula/count conditioning or constrained decoding, retrain/validate it; no such exact-formula interface established in this paper.

Sampling in stable latent regions is documented; this is not a user-prescribed formula condition. Unconditional-only describes the reviewed generation workflow, not impossibility of future extensions.

- [Author-hosted accepted manuscript](https://light.utoronto.ca/wp-content/uploads/2020/09/matter_inverse_design.pdf): Materials Generation, pp.6–8 — Gaussian latent sampling and interpolation generate V–O structures; invalid oxidation-state stoichiometries are discarded afterward.

## ICSG3D

[3‑D Inorganic Crystal Structure Generation and Property Prediction via Representation Learning](https://pubs.acs.org/doi/10.1021/acs.jcim.0c00464)

**Needs adaptation** — Property-conditioned voxel generation around an encoded existing base crystal; not formula-only CSP.

ICSG3D encodes the complete base compound density/coordinate grids, samples nearby latent vectors, and decodes new atom species via segmentation.

**Conditions:** Formation-energy interval, Encoded existing base crystal, Trained structural family

**Adaptation:** Provide formula-only inputs and constrain segmentation/occupancy to exact requested counts, with suitable conditional training or a separately validated count-constrained decoder.

A --base formula-looking argument is a lookup of a known full structure, not exact formula conditioning.

- [Official repository](https://github.com/by256/icsg3d): README: Generate new samples — The --base CeCrO3 example samples around a base compound rather than promising preservation of its stoichiometry.
- [Official source code](https://github.com/by256/icsg3d/blob/master/generate.py): M_base/C_base loading; vae.encoder.predict; watershed_clustering; structure.formula export — The formula argument resolves a dataset record and loads its full voxel structure. Decoded species and cluster counts determine the new formula; validity checks do not enforce the base counts.

## GANCSP

[Generative Adversarial Networks for Crystal Structure Prediction](https://pubs.acs.org/doi/10.1021/acscentsci.0c00426)

**Needs adaptation** — Demonstrated soft composition-conditioned GAN in Mg-Mn-O and V-O; exact hard count preservation is not established.

GANCSP receives a one-hot composition vector, trains a composition/occupancy classifier, and rejects outputs whose classifier-predicted composition disagrees with the target.

**Conditions:** Target composition class within trained chemical system

**Adaptation:** For hard guarantees, enforce the requested element occupancies in the coordinate blocks or verify actual decoded per-element counts with deterministic rejection, rather than relying only on a classifier label.

The paper legitimately reports composition-conditioned generation. This stricter audit distinguishes that claim from exact per-element count enforcement; restricted chemistry and atom caps also apply.

- [Primary full paper and SI](https://arxiv.org/pdf/2004.01396): Composition-conditioned Crystal GAN, pp8–10; SI S1.1 and S6.2, PDF pp21–22 and34–35 — Element-specific coordinate blocks contain learned zero padding. Target composition is a GAN input and classifier loss; SI accepts samples when the composition classifier agrees with the target. This is learned/classifier-based control, not a fixed external species list or a demonstrated exact decoded-atom-count check.

## CCDCGAN

[Constrained crystals deep convolutional generative adversarial network for the inverse design of crystal structures](https://www.nature.com/articles/s41524-021-00526-4)

**Needs adaptation** — Bi-Se chemical-system and formation-energy-guided generation; requested stoichiometry not enforced

CCDCGAN optimizes a formation-energy constraint over generated latent crystal graphs.

**Conditions:** Bi-Se training system, Formation energy objective

**Adaptation:** Add exact composition input and a species/count-preserving structural decoder or verified count constraint.

The word constrained refers to the property/energy objective. Code is available on request in the article, so no public implementation was executed.

- [Publisher paper](https://www.nature.com/articles/s41524-021-00526-4.pdf): Results: Construction and prediction of DCGAN; Training of CCDCGAN; Fig.3 — The constrained generator spans Bi-Se compositions; its extra feedback is formation energy, not an atom-count condition.

## CubicGAN

[High‐Throughput Discovery of Novel Cubic Crystal Materials Using Deep Generative Neural Networks](https://doi.org/10.1002/advs.202100566)

**Needs adaptation** — Ternary/quaternary cubic structures with selected space groups; element identity conditioning

GAN conditions on selected elements and cubic space group; generated asymmetric-site coordinates determine symmetry multiplicities and resulting stoichiometry.

**Conditions:** Selected elements, Space groups 216, 221, 225; quaternary demonstration mainly 216

**Adaptation:** Add requested per-element multiplicities/site assignments or exact-count acceptance constraints; element labels alone do not specify formula.

Cubic symmetry and one inequivalent site per element do not imply arbitrary exact formula support.

- [Primary publisher paper](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202100566): Model architecture and Dataset sections — Generator inputs include element and space-group embeddings; paper samples multiple anonymous formula prototypes.
- [Primary author follow-up](https://www.nature.com/articles/s41524-022-00850-3): Method: Generative adversarial network — Documents selected element combinations, selected cubic groups and special fractional-coordinate support.

## FTCP

[An invertible crystallographic representation for general inverse design of inorganic crystals with targeted properties](https://doi.org/10.1016/j.matt.2021.11.032)

**Needs adaptation** — Property-targeted variable-composition VAE inverse design.

FTCP decodes composition, lattice and coordinates jointly from a property-structured latent space; formulas are decoded outputs.

**Conditions:** Material-property targets via latent-space selection, Full-crystal reconstruction

**Adaptation:** Introduce an explicit formula/count condition and preserve element/occupancy channels during decoding; latent property steering alone is insufficient.

The cited early preprint is not identical to the final Matter text; the official published-paper repository confirms the same variable-composition sampling workflow.

- [Official repository](https://github.com/PV-Lab/FTCP): README: package overview, Sampling, Usage module table — The model trains a property-structured latent space and sampling.py derives chemical formulas from decoded representations.
- [Primary preprint full text](https://arxiv.org/html/2005.07609v2): Sections3.2,3.3,3.5 — Regression organizes the latent space by properties; inverse design samples those regions and permits chemical formulas to change.

## CDVAE

[Crystal Diffusion Variational Autoencoder for Periodic Material Generation](https://arxiv.org/abs/2110.06197)

**Exact formula supported** — LIMITED released low-level decoder hook; original paper standard generation is not a dedicated formula-only CSP model

langevin_dynamics accepts gt_num_atoms and gt_atom_types, initializes exactly that species list and bypasses type updates when supplied. Random coordinates do not require an input crystal.

**Conditions:** Latent z, Optional exact atom-count vector and species list, Full structure for reconstruction

**Adaptation:** No decoder change needed for exact counts. A wrapper must supply latent z, counts, and the species list; a composition-conditioned latent prior requires the separately documented adaptation.

This is code-level structural support, not a reported original-paper formula-conditioned benchmark or a pretrained formula-conditioned latent distribution. No runtime test or quality claim.

- [Official source code, pinned commit](https://github.com/txie-93/cdvae/blob/f857f598d6f6cca5dc1ea0582d228f12dcc2c2ea/cdvae/pl_modules/model.py): CDVAE.langevin_dynamics lines226–302; sample lines304–308 — Providing both optional arguments fixes N and all species throughout coordinate denoising; standard sample() supplies neither.
- [Primary paper describing adaptation](https://arxiv.org/html/2309.04475): Appendix B.2 and Fig.5 — DiffCSP adds a composition-conditioned prior encoder to CDVAE and fixes atom types for its CSP baseline.

## SLICES

[An invertible, invariant crystal representation for inverse design of solid-state materials using generative deep learning](https://www.nature.com/articles/s41467-023-42870-7)

**Needs adaptation** — SLICES reconstruction from a full topology/composition string and formation-energy-conditioned generation

The cRNN embeds a scalar target formation energy while sampling the SLICES atom and edge sequence. A full supplied SLICES string has more information than formula alone.

**Conditions:** Formation energy, Existing full SLICES string for reconstruction

**Adaptation:** Condition or constrain atom-prefix generation to prescribed species/counts while generating topology; validate stoichiometry after reconstruction.

Representation invertibility does not establish formula-only conditional generation in the 2023 paper.

- [Primary publisher paper](https://www.nature.com/articles/s41467-023-42870-7): Methods: ucRNN/cRNN Models for SLICES String Generation; Discussion — The conditional RNN uses desired formation energy; SLI2Cry reconstructs composition plus topology supplied by a SLICES string.

## DiffCSP

[Crystal Structure Prediction by Joint Equivariant Diffusion](https://arxiv.org/abs/2309.04475)

**Exact formula supported** — Fixed supplied unit-cell atom multiset across supported training chemistry/sizes

DiffCSP jointly denoises lattice and fractional coordinates conditional on a fixed list of atomic species.

**Conditions:** Exact per-atom species list and N

**Adaptation:** None for prescribed counts; reduced formulas still require selecting cell multiplicity.

Exact species/count preservation does not guarantee the thermodynamic ground state, unseen-size generalization, or correct cell multiplicity.

- [Primary paper](https://arxiv.org/html/2309.04475): Sec.3 Task definition; Sec.4.2; Appendix B.3 Algorithm2 — Sampling inputs include atom types A; only lattice and coordinate states are updated.

## Crystal-GFN

[Crystal-GFN: sampling crystals with desirable properties and constraints](https://arxiv.org/abs/2310.04925)

**Needs adaptation** — Partial crystal specification: space group, composition and lattice only; no atomic coordinates.

Crystal-GFN sequentially samples SG, per-element integer quantities and lattice parameters with action-space constraints.

**Conditions:** Reward model, Charge neutrality, Space-group/composition compatibility, Lattice-system constraints

**Adaptation:** Clamp or mask element-count actions for the requested formula and supply a downstream coordinate/occupancy generator consistent with the chosen symmetry.

Even exact count control over this partial output would not make the original model a complete CSP algorithm.

- [Primary full paper](https://arxiv.org/html/2310.04925v2): Introduction; Section4.2 Composition; Section6 Conclusions — The paper explicitly distinguishes its SG/composition/lattice output from generating atomic positions. Counts are sequentially sampled; the reported constraints are charge neutrality and Wyckoff compatibility, not a demonstrated fixed-formula full-structure CSP sampler.

## PGCGM

[Physics guided deep learning for generative design of crystal materials with symmetry constraints](https://www.nature.com/articles/s41524-023-00987-9)

**Needs adaptation** — Ternary elements and space-group-conditioned generation; arbitrary requested element counts not demonstrated

PGCGM generates one base atom site per element, applies symmetry operations, then clusters/merges equivalent or nearby atoms.

**Conditions:** Three element identities, Space group, Noise

**Adaptation:** Add stoichiometry-compatible Wyckoff allocation or a count-preserving decoder and enforce counts after merging.

The published study also has an author correction (10.1038/s41524-023-01059-8); element conditioning must not be labeled arbitrary exact-formula CSP.

- [Publisher paper](https://www.nature.com/articles/s41524-023-00987-9): Methods: Crystal symmetry based self-augmentation; Atom clustering and merging; Algorithm1; Materials representation — Full atom counts arise from symmetry expansion and clustering of generated base sites; the specified element set is not a specified per-element count vector.

## SyMat

[Towards Symmetry-Aware Generation of Periodic Materials](https://papers.nips.cc/paper_files/paper/2023/hash/a73474c359ed523e6cd3174ed29a4d56-Abstract-Conference.html)

**Needs adaptation** — Random generation, reconstruction and latent property optimization; coordinate submodel conditions on atom list AND lattice

SyMat first generates element counts and lattice from latent vectors, then samples coordinates with those generated variables fixed.

**Conditions:** Atom types/counts and lattice inside coordinate-generation submodel, Encoded full structure for reconstruction, Latent energy optimization

**Adaptation:** Replace/recondition the joint proposal stage so prescribed atom counts can drive compatible lattice generation; evaluate formula-only CSP.

The existence of p(coordinates | species, lattice) is not a demonstrated formula-only lattice-and-coordinate sampler.

- [Primary conference paper](https://papers.nips.cc/paper_files/paper/2023/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf): Sections3.2–3.4 and4.1; Algorithm1 — The first stage samples atom sets and lattice; its coordinate decoder conditions on both. Reported tasks are random generation, property optimization and reconstruction.

## CrystaLLM

[Crystal structure generation with autoregressive large language modeling](https://doi.org/10.1038/s41467-024-54639-7)

**Needs adaptation** — Exact cell-composition prompt supported; strict preservation is not enforced by the reported autoregressive sampler

A CIF data_ prefix supplies desired element counts, optionally augmented by symmetry/Z. Subsequent CIF tokens are sampled and outputs are validated.

**Conditions:** Cell-composition CIF prefix, Optional space group, Optional formula-unit count Z in web interface

**Adaptation:** Add constrained decoding/count accounting or explicit target-composition rejection and retry for guaranteed count-compliant outputs.

This label concerns strict count enforcement; formula-conditioned prompting and reported CSP experiments already exist and must not be described as absent.

- [Primary publisher paper](https://www.nature.com/articles/s41467-024-54639-7.pdf): Results: Generalizing to unseen structures; Fig.1; Methods: web application — Cell composition is supplied as a text prefix; model generates subsequent tokens and checks output validity afterward.

## Cond-CDVAE

[Deep learning generative model for crystal structure prediction](https://www.nature.com/articles/s41524-024-01443-y)

**Exact formula supported** — Composition-plus-pressure CSP within the trained element/size/pressure domain.

Cond-CDVAE supplies the atom-type list A as fixed input; generates lattice and coordinates while A does not participate in diffusion.

**Conditions:** Exact atom-species list/counts, External pressure

**Adaptation:** No count-conditioning adaptation needed; provide the desired expanded species list/number of formula units.

Formula-unit multiplicity must still be specified or searched. Support does not imply all chemical systems, cell sizes or pressures are validated.

- [Primary publisher full text](https://www.nature.com/articles/s41524-024-01443-y): Results: Architecture and workflow of Cond-CDVAE, following Fig1; reconstruction comparison — The model targets q(M|A,p); generation initializes (A,noisy positions,L) and denoises positions. The text explicitly states composition is predetermined and does not participate in diffusion.

## DP-CDVAE

[Diffusion probabilistic models enhance variational autoencoder for crystal structure generative modeling](https://www.nature.com/articles/s41598-024-51400-4)

**Unconditional-only documented** — Reported de novo generation predicts species/counts; full-input reconstruction is a separate task.

DP-CDVAE decodes lattice, predicted atom number and atomic-type distribution from a structure-encoded or sampled latent vector, then denoises coordinates and species.

**Conditions:** Full input structure for reconstruction, Dataset-specific training distribution

**Adaptation:** To obtain exact formula CSP, replace predicted counts/types with an externally specified species list and train/validate a conditional latent prior and coordinate/lattice decoder.

Reconstructing an encoded full crystal or training only on carbon does not demonstrate arbitrary requested cell stoichiometry. This label refers to the documented generation workflow, not architectural impossibility.

- [Primary publisher full text](https://www.nature.com/articles/s41598-024-51400-4): Figure1 caption; Results: Reconstruction performance, Generation performance; Methods — The architecture decodes the atom number and samples atomic types. The extra N_a encoder improves count prediction during reconstruction; no formula-only fixed-species generation interface is demonstrated.

## EquiCSP

[Equivariant Diffusion for Crystal Structure Prediction](https://proceedings.mlr.press/v235/lin24b.html)

**Exact formula supported** — Fixed supplied unit-cell species/counts

EquiCSP conditions on A and diffuses lattice parameters C and fractional positions F.

**Conditions:** Exact atom-type matrix A and N

**Adaptation:** None for prescribed counts; choose number of formula units separately.

Count support is established by the original published methods; no model was executed.

- [Published conference paper](https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24b/lin24b.pdf): Sec.3 Task definition; Sec.4.2; Algorithm2 Sampling Procedure of EquiCSP — Algorithm2 takes atom types A and returns only C0,F0; A is not generated.
- [Official conference record](https://proceedings.mlr.press/v235/lin24b.html): Paper metadata and download PDF — Identifies the published 2024 EquiCSP paper; later arXiv deposition is not the original publication date.

## FlowLLM

[FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions](https://arxiv.org/abs/2410.23405)

**Needs adaptation** — LLM formula prompts and fixed-species flow refinement documented; full end-to-end hard counts not guaranteed

LLM proposes a complete approximate crystal, then RFM updates only lattice and coordinates while keeping its proposed species.

**Conditions:** Optional formula prompt, LLM-generated complete initial structure

**Adaptation:** Enforce an exact formula in the LLM base sample with constrained decoding or a full-count acceptance check; retain fixed-type refinement.

A conditional refinement distribution given a complete crystal does not itself provide a formula-only initial-structure sampler. Natural-language promptability is documented but not a hard guarantee.

- [Primary paper](https://arxiv.org/html/2410.23405v1): Fig.1; Sec.4 Overview of sampling; Sec.4.1 Training; Algorithm1 step6 — Flow refinement freezes LLM-produced atom types. Formula prompts appear in training pair construction, but the LLM stage has no stated hard count enforcement; main sampling is unconditional.

## FlowMM

[FlowMM: Generating Materials with Riemannian Flow Matching](https://proceedings.mlr.press/v235/miller24a.html)

**Exact formula supported** — Native CSP mode across benchmark compositions, distinct from de novo generation

CSP keeps the full per-site species list fixed and flows only fractional coordinates/lattice; atom types act solely as conditions.

**Conditions:** Per-site atom identities and count

**Adaptation:** None for native CSP mode; use its compatible model/training configuration.

Support does not imply arbitrary cell-size extrapolation or a ground-state guarantee; no runtime validation here.

- [Primary author manuscript](https://arxiv.org/html/2406.04713): Sections2.1 Representing atomic types;2.4 Crystal Structure Prediction — CSP species are conditional information; model learns positions and lattice given the species tuple.
- [Official author repository](https://github.com/facebookresearch/flowmm): Experiments: Conditional Training; atom type manifold options — The null atom-type manifold is used for conditional generation, including model=null_params.

## FUSE2 hybrid workflow

[Integration of generative machine learning with the heuristic crystal structure prediction code FUSE](https://doi.org/10.1039/d4fd00094c)

**Exact formula supported** — Fixed-formula hybrid FUSE2 workflow with user-selected numbers of formula units; not a direct deep generative model.

A GN(MatB)-BO surrogate-guided structural search proposes fixed-composition starting structures, followed by FUSE basin hopping and local relaxation.

**Conditions:** Composition, Numbers of formula units, Space-group range, Optimizer settings

**Adaptation:** No formula-conditioning adaptation needed for this hybrid CSP workflow. Catalogue algorithm wording should identify surrogate/BO-seeded FUSE2 rather than direct deep generative sampling.

Searches can span multiple formula-unit counts; one exact cell count requires fixing that choice. GN-OA predicts energies while BO searches structures, an important taxonomy distinction.

- [Primary author accepted manuscript](https://livrepository.liverpool.ac.uk/3184543/1/C_Collins_accepted.pdf): Sections2.1 and2.2, pp2–4; Section3.1, p5 — Section2.1 identifies the structure proposer as GN-OA/MEGNet plus Bayesian optimization, not a latent deep generator. Section2.2 creates a user-selected number of structures for each requested formula-unit count; swaps and module moves preserve species, while cell extension changes formula-unit multiplicity.

## Mat2Seq

[Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation](https://papers.nips.cc/paper_files/paper/2024/hash/e23133d34964a0a09f6d076fc4b922a4-Abstract-Conference.html)

**Needs adaptation** — Formula-conditioned CSP is already reported, but strict cell-count enforcement is not established

Mat2Seq prepends desired compositional tokens before autoregressive structure tokens and evaluates formula consistency after generation.

**Conditions:** Formula/composition prefix, Property tokens including band gap

**Adaptation:** For a strict prescribed-cell contract, add count-aware token masking or an exact per-element-count acceptance check.

Needs adaptation refers specifically to hard prescribed cell counts, not lack of formula-conditioned CSP capability; the paper already reports composition-conditioned prediction.

- [Primary paper](https://arxiv.org/html/2503.00152): Sec.3.5 Conditional generation; Sec.4.2 Experimental setup — Composition prefix conditioning is explicit; generated formula consistency is part of post-generation validity. No count-preserving decoder is specified.

## UniMat

[Scalable Diffusion for Materials Generation](https://arxiv.org/abs/2311.09235)

**Needs adaptation** — Paper demonstrates exact-count/formula-conditioned inputs and per-composition CSP sampling; hard count preservation not verified

The denoiser concatenates a tensor condition giving the number of atoms per element, distinct from an element-presence condition.

**Conditions:** Exact element counts, e.g. Si4C4, Alternative allowed-element/type-only condition

**Adaptation:** No adaptation needed to supply exact-count conditions as reported; count-clamped extraction or explicit rejection may be needed if every returned sample must exactly preserve those counts.

This strict label concerns guaranteed counts only: the primary paper explicitly DOES support exact-count composition-conditioned inputs and reports per-composition sampling. The inspected conditioning tensor does not establish a hard occupancy/count guarantee or a released ready-to-use conditional checkpoint.

- [Primary author manuscript](https://arxiv.org/html/2311.09235v2): Section2.2 Conditioned Diffusion with UniMat; Section3.3 — Authors distinguish exact per-element counts from type-only conditioning and evaluate per-composition conditional generation.

## DiffCSP++

[Space Group Constrained Crystal Generation](https://arxiv.org/abs/2402.03992)

**Exact formula supported** — CSP mode with fixed species plus space-group/Wyckoff constraints, obtained from templates or supplied symmetry.

DiffCSP++ has a CSP configuration that keeps atom types fixed throughout training and generation while denoising symmetry-compatible lattice/coordinates.

**Conditions:** Exact species list/counts in CSP mode, Space group, Wyckoff assignments or CSPML template

**Adaptation:** No formula count adaptation in its CSP mode; provide or search compatible symmetry/Wyckoff/template conditions.

The unrestricted generation mode also diffuses species. Ground-truth symmetry-assisted scores and template-assisted practical CSP scores are distinct.

- [Primary full paper](https://arxiv.org/html/2402.03992v1): Section5.2 Crystal Structure Prediction; AppendixB.2 — The CSP section explicitly keeps atom types unchanged in both training and generation. It also requires SG/Wyckoff information and obtains it either from ground truth or a composition-matched CSPML template.

## GemsDiff

[Vector Field Oriented Diffusion Model for Crystal Material Generation](https://ojs.aaai.org/index.php/AAAI/article/view/30224)

**Exact formula supported** — Released composition-specific sampling; distinguish current no-lattice-diffusion revision from original paper

sampling.py parses formula to one atomic number per requested atom, supplies that list and N to sampling, and writes the same species list into the CIF.

**Conditions:** Exact formula string, Separate variable-composition chemical-system sampler

**Adaptation:** None for exact formula input in released sampler.

Latest official release differs from AAAI paper geometry process; fixed counts are code-inspected, not runtime-tested.

- [Official source code, pinned commit](https://github.com/aklipf/gemsdiff/blob/5781f80eb072d313b3b3f1ac4bca34cb5feef1d7/sampling.py): Formula parsing lines63–69 and model.sampling / make_cif lines90–98 — Per-element counts construct input_z and input_num_atoms; generated geometry is written with unchanged input_z.
- [Official repository](https://github.com/aklipf/gemsdiff): README: Sampling a specific composition; opening version note — Documents LiFeO2 CLI and warns released revision omits the original lattice diffusion.

## MatterGen

[A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)

**Exact formula supported** — Released CSP training/sampling mode; separate from paper’s chemical-system/property adapters

CSP mode excludes atom-type denoising and accepts target_compositions containing exact per-element atom numbers.

**Conditions:** Exact per-element cell counts in CSP mode, Chemical system in adapter mode, Symmetry and scalar properties in adapter modes

**Adaptation:** No architectural adaptation required for documented CSP mode, but training a CSP-mode model is explicitly required; a compatible pretrained CSP checkpoint was not established here.

Do not present the released base/property-adapter checkpoint as plug-and-play exact-formula CSP. Interface/code evidence only; not runtime-tested.

- [Official repository README](https://github.com/microsoft/mattergen#crystal-structure-prediction): Training > Crystal structure prediction — Documents --config-name=csp and --target_compositions with atom-number dictionaries and --sampling-config-name=csp; atomic identities are not denoised.
- [Primary publisher paper](https://www.nature.com/articles/s41586-025-08628-5): Chemistry-guided design; Fig.3 — Published chemistry-guided experiments explore chemical systems with variable stoichiometry, distinct from the repository CSP mode.

## CrysBFN

[A Periodic Bayesian Flow for Material Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f09e1ee5035a4c3fe38a5681cae5815-Abstract-Conference.html)

**Exact formula supported** — Native CSP mode on Perov-5, MP-20 and MPTS-52

CSP models p(lattice,fractional coordinates | atom types) with the full per-site species list embedded as fixed node conditions.

**Conditions:** Per-site atom identities and cell count

**Adaptation:** None for documented CSP mode.

Entropy conditioning concerns Bayesian-flow state uncertainty and is separate from composition conditioning; no runtime validation here.

- [Primary author manuscript](https://arxiv.org/html/2502.02016v1): Section5.2 Stable Structure Prediction; crystal notation — CSP fixes the atom-type vector and generates lattice and coordinates; distinct ab initio mode also generates species.

## ADiT

[All-atom Diffusion Transformers: Unified generative modelling of molecules and materials](https://proceedings.mlr.press/v267/joshi25a.html)

**Needs adaptation** — Unified model conditioned on periodic versus nonperiodic class; no exact formula control.

ADiT generates latent atomic systems with a DiT and decodes atom types, coordinates and lattice; the only implemented conditioning class distinguishes crystals from molecules.

**Conditions:** Periodic/nonperiodic class label

**Adaptation:** Add explicit species-count conditioning and a count-constrained species/occupancy decoder; additional training and fidelity evaluation are required.

The paper uses unconditional in the scientific-design sense despite a domain class label; its class conditioning is not chemical-formula conditioning.

- [Primary full paper](https://arxiv.org/html/2503.03965v1): Denoiser architecture; Algorithm3; Limitations paragraph — The denoiser uses a binary periodic/nonperiodic embedding. Additional property/geometric conditioning is future work; the limitations call current output generation unconditional.

## ContinuouSP

[ContinuouSP: Generative Model for Crystal Structure Prediction with Invariance and Continuity](https://arxiv.org/abs/2502.02026)

**Exact formula supported** — Composition-conditioned energy-based CSP; preliminary workshop evaluation.

ContinuouSP models p_theta(X,L|A) for a supplied species vector and samples coordinates and lattice with MCMC while A is held as the conditional variable.

**Conditions:** Exact species vector/counts

**Adaptation:** No count-conditioning adaptation needed; specify the full species vector/cell multiplicity.

Symmetry/re-description invariance can relate several choices of unit cell; that mathematical property does not make the specified sampling vector variable. Physical ground-state completeness is not established.

- [Primary full paper](https://arxiv.org/html/2502.02026v1): Definitions17–19, particularly Definition18 and Eq11; CSP sampling formulation — The normalized density integrates over X and L conditional on A, not over species; the species vector supplies the generation condition.

## CrystalFlow

[CrystalFlow: a flow-based generative model for crystalline materials](https://www.nature.com/articles/s41467-025-64364-4)

**Exact formula supported** — Fixed-composition CSP, optionally pressure-conditioned; separate de novo mode

CrystalFlow holds A0=A1 fixed and transports only lattice and fractional positions for CSP.

**Conditions:** Exact atomic species/counts, Optional pressure

**Adaptation:** None for exact composition; choose cell multiplicity and applicable pressure model.

Preserving counts is separate from recovering the lowest-enthalpy phase or DFT validation.

- [Publisher paper](https://www.nature.com/articles/s41467-025-64364-4): Fig.1 caption; Results model definition; Methods flow on chemical composition — The CSP condition is A,P; Fig.1 explicitly fixes A0=A1. Atom-type flow is introduced separately for de novo generation.

## KLDM

[Kinetic Langevin Diffusion for Crystalline Materials Generation](https://proceedings.mlr.press/v267/cornet25a.html)

**Exact formula supported** — Native CSP mode; separate species-diffusion extension for de novo generation

Uses the given K-entry atom identity vector a as the condition for p(f,l|a), so K and per-element counts remain supplied.

**Conditions:** Per-site species/counts in CSP

**Adaptation:** None for documented CSP mode.

Published CSP recovery and MLIP evaluation do not prove thermodynamic ground states; no runtime validation here.

- [Primary published conference PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cornet25a/cornet25a.pdf): Section2.1 Crystal Structure Prediction; Section5 CSP experiments — Defines composition as a K-entry atomic identity vector and CSP as sampling coordinates/lattice conditioned on it.

## OMatG

[Open Materials Generation with Stochastic Interpolants](https://proceedings.mlr.press/v267/hollmer25a.html)

**Exact formula supported** — Separate exact-composition CSP and variable-composition DNG configurations.

OMatG CSP fixes every atom species from t=0 and evolves only coordinates/lattice; DNG additionally learns species through discrete flow matching.

**Conditions:** Exact atom-species list/counts in CSP configuration

**Adaptation:** No formula-conditioning adaptation for the CSP checkpoint/configuration; select it rather than the joint DNG mode.

The paper evaluates compositions from benchmark datasets; exact count control does not certify performance outside trained sizes/chemistries.

- [Primary full paper](https://arxiv.org/html/2502.02582v2): SectionIII.3 Joint Generation; Figure2 caption; AppendixC.2 — The text fixes atom types for CSP, Figure2 fixes A at t=0, and the CSP objective omits the species-learning term. A separate formula-prediction model may feed the CSP model in a two-stage discovery workflow.

## CrystalFormer

[Space group informed transformer for crystalline materials generation](https://doi.org/10.1016/j.scib.2025.09.035)

**Needs adaptation** — Original space-group/element conditioning; current CrystalFormer-CSP extension already has formula-conditioned models and reduced-stoichiometry output filtering

Current sampler embeds formula and masks allowed species; it samples Wyckoff positions and species. Converter filters by reduced_formula, rather than exact full-cell atom counts.

**Conditions:** Space group, Allowed elements, Formula in later v0.5/v0.6 extension

**Adaptation:** For exact prescribed cell counts, use multiplicity-aware constrained decoding or compare full compositions and N after generation.

Do not say CrystalFormer lacks formula-conditioned CSP: the current extension supports it. The strict deficit is hard full-cell count enforcement and explicit formula-unit multiplicity control.

- [Primary paper](https://arxiv.org/html/2403.15734): Sec.II.1.3 Sampling — Original sampling supplies space group and possible elements; site count can fluctuate.
- [Official source code, pinned commit](https://github.com/deepmodeling/CrystalFormer/blob/31bb734a3fd006af49a021921839061e6184cbf1/crystalformer/src/sample.py): make_sample_crystal / sample_crystal lines72–105 — Formula affects model conditioning and a composition>0 element mask; no remaining-count budget enforces multiplicity totals.
- [Official source code, pinned commit](https://github.com/deepmodeling/CrystalFormer/blob/31bb734a3fd006af49a021921839061e6184cbf1/scripts/awl2struct.py): check_formula_match lines86–109; output filtering lines149–157 — Postprocessing compares reduced_formula, accepting matching stoichiometric ratios with potentially different cell multiplicities.
- [Official repository, pinned commit](https://github.com/deepmodeling/CrystalFormer/blob/31bb734a3fd006af49a021921839061e6184cbf1/README.md): Status; Crystal Structure Prediction; How to cite — Documents --formula Cu12Sb4S13 and later CrystalFormer-CSP arXiv2512.18251, distinct from original paper.

## SymmCD

[SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models](https://arxiv.org/abs/2502.03638)

**Needs adaptation** — Symmetry-conditioned discovery, not formula-given CSP

Samples space group and asymmetric-unit representatives, then diffuses representative types/site symmetries and expands symmetry orbits.

**Conditions:** Target space group, Number of asymmetric-unit representatives

**Adaptation:** Allocate symmetry-compatible orbits to requested species counts, keep species/counts fixed, and adapt conditional training/sampling.

Fixing the number of representatives is not fixing the full-cell atom multiset; orbit multiplicities vary.

- [Primary paper](https://arxiv.org/html/2502.03638): Sec.4.3; Algorithm2 inputs; Conclusion limitation — Algorithm2 supplies space group and representative count. The conclusion explicitly identifies composition-given CSP as challenging because composition is sampled after space group.

## Uni-3DAR

[Uni-3DAR: Unified 3D Generation and Understanding via Autoregression on Compressed Spatial Tokens](https://arxiv.org/abs/2503.16278v1)

**Exact formula supported** — Released MP-20 CSP checkpoint/interface with exact species inventory constraints; separate de novo and PXRD modes

CSP conditions on atom types/counts and sampler keeps a remaining inventory per element, masking exhausted species and decrementing budgets after atom sampling.

**Conditions:** Species and cell counts, PXRD plus composition in separate task

**Adaptation:** None for documented CSP workflow.

Constraint-code inspection is not runtime validation; model/data coverage and invalid structure handling still matter.

- [Primary author manuscript](https://arxiv.org/html/2503.16278v1): Section3.2 Tasks — Defines CSP inputs as atom types and counts.
- [Official repository README](https://github.com/dptech-corp/Uni-3DAR): Reproducing Results on MP20: Inference with Pretrained Model — Documents mp20_csp.pt and inference_mp20_csp.sh separately from de novo and PXRD checkpoints.
- [Official source code](https://github.com/dptech-corp/Uni-3DAR/blob/main/uni3dar/inference.py): lines149–157 — Extracts target atomic inventory and passes it to model.generate(atom_constraint=gt_atoms).
- [Official source code](https://github.com/dptech-corp/Uni-3DAR/blob/main/uni3dar/models/uni3dar_sampler.py): get_atom_predict_funcs, lines570–621; generation known_atoms initialization — Maintains element budgets, zeros probability for exhausted species, and decrements the selected inventory; total atomic count is supplied.

## CrystalGRPO

[CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction](https://arxiv.org/abs/2608.06582)

**Exact formula supported** — Fixed-composition flow CSP with RL post-training; optional additional PXRD condition.

CrystalGRPO post-trains coordinate/lattice flow policies with composition and atom number supplied, preserving the species list.

**Conditions:** Exact composition/atom types/count, Optional PXRD pattern

**Adaptation:** No formula-count adaptation needed for the CSP policy; PXRD conditioning is optional additional information.

Preprint evidence only; no runtime test. Reference recovery rewards during RL training differ from the information needed at inference.

- [Primary full paper](https://arxiv.org/html/2608.06582v1): Problem formulation; Section6.1; Appendix PXRD-conditioned CSP, Problem definition — The paper evaluates composition-conditioned MP-20/MPTS-52 and explicitly states that chemical composition, atom types and atom number are CSP inputs while fractional coordinates and lattice are predicted.

## CrystalGRW

[CrystalGRW: generative modeling of crystal structures with targeted crystallographic properties via geodesic random walks](https://www.nature.com/articles/s41598-026-62470-x)

**Exact formula supported** — Released fixed-atom-types sampling option; paper mainly evaluates de novo and point-group-controlled generation

--force_atom_types takes per-site identities and atom counts from the input batch, removes atom_types from the diffused manifolds, and samples coordinates/lattice.

**Conditions:** Fixed per-site species and cell counts via --force_atom_types, Point-group guidance in paper

**Adaptation:** No new sampling mechanism required for the released fixed-types option; build the input batch/dataset and select coordinate/lattice corruption appropriately.

Code-supported mechanism, not proof of exact-formula recovery accuracy; no runtime execution or checkpoint compatibility testing was performed. Formula-only use requires coordinate and lattice corruption and a score-only configuration without a structure encoder; encoder-based variants can depend on full input structure.

- [Official source code](https://github.com/trachote/crystalgrw/blob/main/src/crystalgrw/cli/evaluate.py): sample_properties lines28–48; reconstruction lines140–174; run_eval lines304–332 — Fixed-types flag copies batch atom types and counts and removes the atomic-type diffusion manifold.
- [Official source code](https://github.com/trachote/crystalgrw/blob/main/src/crystalgrw/samplers/sample.py): sample — Sampling passes the supplied atomic identities into the SDE and returns them with generated coordinates and lattice. The optional encoder branch consumes input_encoder when a configured encoder exists; choose a compatible score-only model for formula-only use.
- [Primary publisher paper](https://www.nature.com/articles/s41598-026-62470-x): Abstract; Condition guidance; Discussion — Paper demonstrates de novo generation and point-group controls rather than an exact-formula CSP benchmark.

## Crystalite

[Crystalite: A Lightweight Transformer for Efficient Crystal Modeling](https://arxiv.org/abs/2604.02270)

**Exact formula supported** — Dedicated CSP configuration with fixed supplied species/counts; separate de novo configuration

In CSP Crystalite holds atom-type features fixed and denoises coordinate and lattice channels only.

**Conditions:** Exact per-atom composition / N

**Adaptation:** None for counts in documented CSP configuration; select the CSP model/configuration.

The reported CSP configuration uses fixed atomic-number features; the de novo configuration uses PCA subatomic tokens. Do not assume a single unchanged checkpoint handles both.

- [Primary paper](https://arxiv.org/html/2604.02270): Sec.3.1 after Eq.4; Sec.3.2; Sec.4.1 task configurations; Appendix Table4 — CSP keeps atom-type features fixed and models p(F,L|A); task-specific CSP configurations differ from de novo generation.

## SHAFT

[Efficient symmetry-aware materials generation via hierarchical generative flow networks](https://arxiv.org/abs/2411.04323)

**Needs adaptation** — Element-set-restricted battery-material discovery and reward-guided complete-crystal generation.

SHAFT samples space groups, lattice, atom positions and species using a hierarchical GFlowNet; element choices are restricted for the battery task.

**Conditions:** Allowed element set, Physics-informed reward, Symmetry restrictions

**Adaptation:** Track remaining per-element count budgets and mask type/placement/stop actions, including symmetry multiplicities; validate fixed-formula sampling after adaptation.

The phrase specific formulas and elements in the motivation is not evidence that exact target atom counts are enforced.

- [Primary full paper](https://arxiv.org/html/2411.04323v1): Section4.1 and Algorithm1; Sections5 and5.1 — The policy samples atom types from a multinoulli distribution starting with an empty graph. Battery experiments restrict eligible elements, while per-element quantities remain generated. No explicit prescribed count vector appears in Algorithm1.

## NextCrystal

[NextCrystal: a Symmetry-Driven Generative Framework for Crystal Structure Prediction](https://arxiv.org/abs/2602.17176v4)

**Exact formula supported** — Preprint v4 formula-and-cell-count-conditioned symmetry proposal plus constrained diffusion

Expanded atom sequence encodes input counts; constrained beam search assigns Wyckoff multiplicities consistent with each element inventory before diffusion.

**Conditions:** Composition and atom counts, Inferred space group and count-consistent Wyckoff template

**Adaptation:** None in the documented method; implementation/runtime availability not established in this audit.

Preprint/method evidence only; algebraic count consistency does not establish ground-state discovery or universal scalability.

- [Primary author preprint](https://arxiv.org/html/2602.17176v4): Methods around Eqs1–3; Figure1; constrained assignment discussion — Input is expanded per-cell species sequence; assignment constraints enforce multiplicity totals compatible with requested stoichiometry.

## DAO

[Siamese foundation models for crystal structure prediction](https://www.nature.com/articles/s41467-026-72362-3)

**Exact formula supported** — Composition-conditioned DAO-G lattice/coordinate generation with optional DAO-P energy guidance.

DAO-G models p(L,F|A), using a fixed N-entry atom-type array A and denoising only lattice and fractional coordinates.

**Conditions:** Exact N-entry atom-species vector, Optional energy guidance

**Adaptation:** No formula-conditioning adaptation needed; supply the expanded species list/number of formula units.

Count support is separate from demonstrated compositional/prototype generalization and from thermodynamic validation.

- [Primary publisher full text](https://www.nature.com/articles/s41467-026-72362-3): Methods: Crystal representation; Equivariant diffusion models for crystal structure generation; Eqs1–4 — Chemical composition A is an N-entry species array. The generative distribution is explicitly p(L,F|A), and training/inference noise schedules cover lattice and coordinates, leaving species as input.

## uFlowCSP

[uFlowCSP: Crystal Structure Prediction using Mean flow generative models](https://arxiv.org/abs/2609.09799)

**Exact formula supported** — Primitive-cell atom multiset supplied to MP20 / CSPBench protocols

uFlowCSP transports continuous coordinates and lattice while atomic numbers remain fixed composition inputs.

**Conditions:** Primitive-cell per-atom atomic numbers / N, Formula embedding

**Adaptation:** None for supplied-cell count control; formula-unit multiplicity must be chosen externally.

Preprint support is methods-level; neither checkpoint execution nor independent recovery/energy validation was performed in this audit.

- [Primary preprint](https://arxiv.org/html/2609.09799): Sec.2.1 Problem Setting; Sec.2.2.1 Crystal Representation; Sec.2.3 inference conditions — Methods explicitly fix atomic numbers by the supplied composition; no space-group label is required at inference.
