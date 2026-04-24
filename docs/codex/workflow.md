# Workflow

## Default loop

1. Clarify the user request and the exact repository surface being changed.
2. Name the verification path before editing files.
3. Read the smallest relevant scripts, tests, and docs.
4. Implement the smallest durable change.
5. Review for correctness, regressions, secrets, private paths, and public-surface bleed.
6. Run the highest-signal local checks.
7. Update docs or templates when the change introduces a new durable rule.

## Open-source prep loop

1. Keep the public promise narrow: supported text artifacts only.
2. Verify that examples, docs, and templates contain no real secrets, private URLs, or absolute local paths.
3. Confirm that skipped files remain visible as manual-review-required items.
4. Keep contributor, security, and PR guidance aligned with the real CI path.
5. If README changes, preserve the short `## Proof` section above `## Quick Start`.

## When to use which agent

- `architect`: ambiguous scope, release-surface cuts, or boundary decisions.
- `implementer`: focused doc or code patches with minimal churn.
- `reviewer`: final correctness, leak, and public-surface review.
- `evolver`: measured tuning of regexes, heuristics, or report wording.
- `cleanup`: drift removal after repeated review comments or stale public artifacts.
