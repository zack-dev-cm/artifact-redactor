# AGENTS

- Keep the public promise narrow and truthful: this repo redacts text artifacts such as Markdown, JSON, logs, YAML, CSV, and similar files. It does not claim screenshot, PDF, or image redaction.
- Keep scripts standard-library-only unless there is a hard requirement otherwise.
- Preserve public context when safe: strip query strings from public URLs, redact private URLs and absolute paths, and replace secret-like strings and common PII with placeholders.
- Any README update should keep a short `## Proof` section above `## Quick Start`.
- Do not add real secrets, absolute local paths, or production identifiers to examples or tests.

