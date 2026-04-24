# Evals

## Rules

- Every task should name the primary verification step before edits start.
- Public-surface changes need leak and bleed review, not just passing tests.
- Prefer deterministic local checks before broader release prep.
- If docs or examples change, review them like code for false claims and accidental disclosures.

## Required checks

- Syntax: `python3 -m py_compile skill/artifact-redactor/scripts/*.py`
- Regression: `python3 -m unittest discover -s tests -q`
- End-to-end smoke when workflow behavior changes: `python3 -m unittest tests.test_smoke.ArtifactRedactorSmokeTest.test_end_to_end_redaction_flow -q`

## Quality bar

- Any change that implies support for screenshots, PDFs, or other binary formats is a release blocker unless the implementation really changed.
- Secret-like strings, private URLs, absolute local paths, and production identifiers in examples or docs are release blockers.
- A skipped file must remain visible as a manual-review item rather than being treated as cleared.
- README, security docs, contributor docs, and the PR template are part of the product surface and must stay aligned with real behavior.
