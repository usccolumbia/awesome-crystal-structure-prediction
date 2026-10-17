# Contributing

Additions and corrections are welcome through a pull request or resource issue.

1. Add or update the canonical entry in `data/papers.json`, `data/software.json`, or `data/benchmarks.json`. Use a stable unique ID and reuse an existing paper ID for related software releases.
2. Include a primary paper/DOI and the official code or project link. State the task inputs, algorithm category, and inorganic/molecular scope. Cite published versions where available and label preprints.
3. Record license, model, training-data, and benchmark evidence separately. Use “not verified” when the evidence is missing. A public repository alone does not establish an open-source license, nor does a formula prompt guarantee exact atom counts.
4. Add bibliographic metadata to `references.bib`. Avoid duplicate preprint/journal entries for the same work unless the version difference is material.
5. Preserve collaboration attribution and link the primary authorship source. Keep performance claims tied to their dataset, split, candidate budget, evaluator and matching protocol.
6. Run `python3 scripts/build.py` and `python3 scripts/validate.py`, then commit the data and regenerated pages together.

Do not add credentials, local filesystem paths, copied publisher PDFs, model binaries, or private datasets. Link to original resources and retain their terms. No algorithm installation is required to contribute a catalogue entry.
