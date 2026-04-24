# Architecture

## Boundaries

- `skill/artifact-redactor/SKILL.md`: public usage guidance and workflow framing.
- `skill/artifact-redactor/scripts/redaction_common.py`: shared heuristics for file discovery, text detection, URL sanitization, and placeholder replacement.
- `skill/artifact-redactor/scripts/scan_sensitive_text.py`: original-input scan that emits JSON findings.
- `skill/artifact-redactor/scripts/redact_artifacts.py`: redaction pass that writes supported text files into a separate output tree and records skipped files.
- `skill/artifact-redactor/scripts/check_redaction_output.py`: verification pass that re-scans output and carries skipped files forward as manual-review items.
- `skill/artifact-redactor/scripts/render_redaction_report.py`: markdown report renderer for the scan, redaction, and check JSON files.

## Shared design rules

- Keep the implementation standard-library-only unless a real requirement forces otherwise.
- Preserve surrounding context with stable placeholders instead of deleting whole lines.
- Keep public URLs when safe, but remove query strings and fragments.
- Treat binary or unsupported files as manual-review items, not automatically safe outputs.
- Write redacted artifacts into a separate output directory instead of mutating the source tree.

## Do-not-break list

- Public script entrypoints under `skill/artifact-redactor/scripts/`
- Status values: `share-ready`, `manual-review-required`, `fix-required`
- Placeholders such as `[redacted-secret]`, `[redacted-private-url]`, and `[redacted-private-path]`
- README proof section ordering and text-only scope claims
- Public docs in `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, and `.github/pull_request_template.md`
