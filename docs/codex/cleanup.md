# Cleanup

Codex can add drift quickly even in a small repo. This file defines the cleanup lane.

## Routine sweep

- Run a weekly cleanup cadence before release work or after repeated review drift.
- Remove stale reports, copied outputs, and misleading release notes.
- Refresh docs that drifted from the scripts, smoke tests, or CI workflow.
- Tighten repeated leak or bleed review comments into durable docs or templates.
- Re-check public examples for fake-only data and narrow scope claims.

## Promote a rule when

- The same leak pattern appears more than once in docs, examples, or fixtures.
- Review repeatedly asks for the same validation step or release warning.
- A public doc keeps implying broader coverage than the scripts actually provide.

## Do not do

- Large opportunistic rewrites under the label of cleanup.
- Broad abstraction work that hides the script-level workflow.
- New examples containing real tokens, workstation paths, or production identifiers.
