# AGENTS.md

This repo ships one public Artifact Redactor skill plus standard-library Python scripts for text-only artifact redaction. Use this file as the index, not as the full manual.

## Operating rules

- Restate the user goal and name the verification step before editing files.
- Keep the public promise narrow and truthful: text artifacts only, not screenshots, PDFs, or image redaction.
- Keep scripts standard-library-only unless there is a hard requirement otherwise.
- Preserve public context when safe: strip query strings from public URLs, redact private URLs and absolute paths, and replace secret-like strings and common PII with placeholders.
- Any README update should keep a short `## Proof` section above `## Quick Start`.
- Do not add real secrets, absolute local paths, or production identifiers to examples or tests.

## Repo map

- [Overview](docs/codex/overview.md)
- [Architecture](docs/codex/architecture.md)
- [Workflow](docs/codex/workflow.md)
- [Evals](docs/codex/evals.md)
- [Cleanup](docs/codex/cleanup.md)

## Main code paths

- `skill/artifact-redactor/`: public skill bundle, agent metadata, and redaction scripts.
- `tests/`: smoke coverage for the end-to-end redaction flow and CLI argument validation.
- `docs/`: public release and maintenance docs.

## Default verification

1. Run `python3 -m py_compile skill/artifact-redactor/scripts/*.py`.
2. Run `python3 -m unittest discover -s tests -q`.
3. If CLI behavior changed, run the smallest relevant smoke path.

## Project-scoped custom agents

- `.codex/agents/architect.toml`
- `.codex/agents/implementer.toml`
- `.codex/agents/reviewer.toml`
- `.codex/agents/evolver.toml`
- `.codex/agents/cleanup.toml`
