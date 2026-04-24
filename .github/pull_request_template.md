## Summary

- what changed
- why it changed

## Validation

- [ ] `python3 -m py_compile skill/artifact-redactor/scripts/*.py`
- [ ] `python3 -m unittest discover -s tests -q`
- [ ] `python3 -m codex_harness audit . --strict --min-score 90` run locally when available, or the skip reason is explained
- [ ] Smallest relevant smoke path run if CLI behavior changed
- [ ] README/docs updated if the public surface changed
- [ ] Security, leak, and public-surface review completed
- [ ] No secret-like strings, private URLs, or absolute local paths were introduced
- [ ] Text-only scope remains truthful and manual-review behavior remains intact

## Notes

- false-positive or false-negative tradeoffs
- follow-up work, if any
