# Contributing

Artifact Redactor is intentionally narrow. It focuses on safer sharing of text artifacts without pretending to solve binary or image redaction.

## Local setup

Artifact Redactor targets Python 3.9+ and keeps the scripts standard-library-only.

```bash
python3 -m py_compile skill/artifact-redactor/scripts/*.py
python3 -m unittest discover -s tests -q
```

## Good contribution types

- tighten or clarify redaction heuristics for supported text files
- improve manual-review reporting for skipped files
- harden docs, examples, and release templates against leak or bleed issues
- improve report wording when it makes review decisions clearer

## Contribution guidelines

1. Keep the change small and legible.
2. Add or update tests when behavior changes.
3. Preserve the text-only public promise unless the implementation truly expands.
4. Prefer standard-library implementations unless there is a hard requirement otherwise.
5. Do not add real secrets, private URLs, production identifiers, or absolute local paths to examples, docs, or tests.
6. If README changes, keep `## Proof` above `## Quick Start`.

## Review notes

- False negatives matter because the tool is used as a pre-share safety pass.
- False positives matter because noisy output will be ignored.
- Manual-review-required is a valid outcome, not a failure of the product.
- Public docs and templates are part of the release surface and should be reviewed like code.
