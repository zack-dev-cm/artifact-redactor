# Overview

This repository packages Artifact Redactor as a small local-first skill and script bundle for safer sharing of text artifacts.

## Products

- `skill/artifact-redactor/SKILL.md`: public operator instructions for the redaction workflow.
- `skill/artifact-redactor/scripts/scan_sensitive_text.py`: scan supported text files for obvious sensitive patterns.
- `skill/artifact-redactor/scripts/redact_artifacts.py`: write a redacted copy of supported text files into a clean output directory.
- `skill/artifact-redactor/scripts/check_redaction_output.py`: re-scan the redacted output and surface `share-ready`, `manual-review-required`, or `fix-required`.
- `skill/artifact-redactor/scripts/render_redaction_report.py`: render a markdown report from the JSON outputs.

## Repo landmarks

- Skill bundle: `skill/artifact-redactor/`
- Smoke tests: `tests/`
- Public docs: `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, `docs/codex/`
- GitHub automation: `.github/workflows/`, `.github/pull_request_template.md`

## Standard checks

- Syntax: `python3 -m py_compile skill/artifact-redactor/scripts/*.py`
- Regression: `python3 -m unittest discover -s tests -q`
- End-to-end smoke when CLI behavior changes: `python3 -m unittest tests.test_smoke.ArtifactRedactorSmokeTest.test_end_to_end_redaction_flow -q`

## Non-goals

- This repo is not a hosted service.
- It does not claim binary, screenshot, PDF, or image redaction.
- It does not silently clear skipped files; manual review remains part of the deliverable.
