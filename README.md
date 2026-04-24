# Artifact Redactor

**Redact private paths, secret-like strings, private URLs, and common PII from Markdown, JSON, logs, and other text artifacts before you share them.**

Artifact Redactor is a small public OpenClaw skill and local-first Python toolkit for making shareable
artifact bundles safer. It scans text files for obvious leak patterns, writes a redacted copy of the
artifacts into a clean output directory, checks the processed text output, surfaces skipped files as
manual-review items, and renders a concise markdown report.

Requires Python 3.9+.

Binary files are not rewritten. They are flagged for manual review so the tool stays honest about what
it can and cannot sanitize automatically.

## Proof

```md
# Artifact Redaction Report

- Recommendation: **Manual review before sharing**
- Original findings: **6**
- Output findings: **0**
- Processed text files: **2**
- Manual-review files: **1**
- Skipped files: **1**

## Output Check
- No obvious sensitive text patterns remain in processed text files.
- 1 skipped file still requires manual review before sharing the full bundle.
```

## Quick Start

```bash
mkdir -p artifact-redactor-demo

cat > artifact-redactor-demo/notes.md <<'EOF'
Contact person@example.com or +1 555 123 4567.
Public docs https://example.com/docs?page=2#proof can stay without the query string.
Token ghp_not_real should not be shared.
EOF

python3 skill/artifact-redactor/scripts/scan_sensitive_text.py \
  --root artifact-redactor-demo \
  --out artifact-redactor-scan.json

python3 skill/artifact-redactor/scripts/redact_artifacts.py \
  --root artifact-redactor-demo \
  --out-dir artifact-redactor-safe \
  --out artifact-redactor-redaction.json

python3 skill/artifact-redactor/scripts/check_redaction_output.py \
  --root artifact-redactor-safe \
  --redaction artifact-redactor-redaction.json \
  --out artifact-redactor-check.json

python3 skill/artifact-redactor/scripts/render_redaction_report.py \
  --scan artifact-redactor-scan.json \
  --redaction artifact-redactor-redaction.json \
  --check artifact-redactor-check.json \
  --out artifact-redactor-report.md
```

Use an empty output directory outside the source root for `--out-dir`; the tool now rejects overlapping or pre-populated output locations to avoid stale-file bleed.

## What It Covers

- scans text artifacts for private paths, private URLs, secret-like strings, email addresses, and phone numbers
- writes a redacted copy of supported files into a separate output directory
- marks skipped or unsupported files as manual-review-required instead of treating them as automatically cleared
- strips query strings and fragments from public URLs while keeping the public path when safe
- skips binary or unsupported files and calls them out for manual review
- renders a shareable report you can attach to a bug, release note, vendor handoff, or public issue

## Included

- `skill/artifact-redactor/SKILL.md`
- `skill/artifact-redactor/agents/openai.yaml`
- `skill/artifact-redactor/scripts/redaction_common.py`
- `skill/artifact-redactor/scripts/scan_sensitive_text.py`
- `skill/artifact-redactor/scripts/redact_artifacts.py`
- `skill/artifact-redactor/scripts/check_redaction_output.py`
- `skill/artifact-redactor/scripts/render_redaction_report.py`

## Use Cases

- sanitize browser QA bundles before sharing them outside the team
- clean logs, manifests, and markdown reports before filing a public GitHub issue
- strip secrets and local paths from AI experiment outputs before posting benchmarks
- prepare safer evidence packs for vendors, contractors, or release reviews

## Limits

- binary files, screenshots, and PDFs are not auto-redacted in `v1.0.3`
- the scanner uses conservative heuristics; some manual review is still required
- placeholder redaction is designed for sharing safety, not forensic reversibility

## Security

Report suspected leak or redaction failures privately through [SECURITY.md](SECURITY.md) instead of opening a public issue first.

## License

MIT No Attribution (MIT-0)
