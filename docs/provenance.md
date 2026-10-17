# Provenance and coverage

This collection accompanies *Crystal Structure Prediction from Search to Learning: A 30-Year Expedition* (in preparation). Its initial 196-record literature map and 122-entry software directory were curated on 16 October 2026. The bibliography incorporates the survey's verified metadata corrections. Eight paper records were subsequently added from the manuscript (seven CSP/descriptor/evaluation papers and CrystalFormer-CSP), followed by the original matbench-genmetrics/MPTS-52 framework paper. Seven corresponding code entries were added from official author repositories.

The canonical JSON preserves the primary source URLs, evidence depth, task inputs, collaboration attribution, and dated availability observations. The exact formula audit covers 42 model/workflow records. Original input hashes and coverage counts are in [provenance.json](../data/provenance.json).

Benchmark links distinguish the historical CSPBench study from the later T180/T46 v3.1 release. Named test-cohort links are pinned to a commit. MPTS-52 is linked both to the original time-split framework and the DiffCSP dataset release.

The resources are source-qualified, not independently reproduced. Metadata verification does not imply full-text review of every paper; links to checkpoints and datasets do not imply that their payloads have been downloaded or executed. Existing availability findings retain their original dates rather than being presented as fresh runtime validation.

The repository publishes the curated catalogue and bibliographic/resource metadata. The in-progress manuscript and private research workspace are not part of this repository.

## Structural knowledge update (17 October 2026)

Three source-verified papers were added: constrained molecular USPEX (2012), the topology-based USPEX generator (2019), and the MAGUS framework (2023). Together with existing records, 21 profiles describe nine cross-cutting categories in [structural-priors.json](../data/structural_priors.json). The CALYPSO/SPAI paper is explicitly linked to its parent implementation. MAGUS v2.0.0 has a public Zenodo source archive with restricted academic terms; it is not labeled open source. Original records retain their IDs. The companion interactive map also incorporates the nine earlier manuscript/benchmark additions, bringing both paper catalogues to 208 records.

Profiles are backed by papers and developer documentation. Constraints, supplied information and release-specific availability are distinguished. Functional checks execute page JavaScript in a minimal DOM, validate cross-links, and exercise feature/license intersections; these do not establish browser rendering or algorithm runtime correctness.

## Survey count synchronization (17 October 2026)

The MaskGXT and TGDMat papers, previously included only in the survey, are now part of this repository, bringing its catalogue to **210 records**. Both include primary-paper attribution, BibTeX, and official source-code links. The software directory retains **129 implementation and component entries**; the original 122-entry directory describes the earlier import. The 42-record formula-conditioning audit is unchanged. The survey now reports this dated repository snapshot, while its Data availability statement remains count-free.
