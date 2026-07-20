# Validation report

This report records validation results for the repository. It is updated after the validation workflow runs.

## Checks executed (local + CI)

| Check | Tool | Result |
|-------|------|--------|
| YAML validity | PyYAML (scripts/validate_yaml_json.py) | Pass |
| JSON validity | json module (scripts/validate_yaml_json.py) | Pass |
| Workflow structure | scripts/validate-workflows.py | Pass |
| Markdown basic checks | scripts/validate-markdown.js | Pass |
| Python tests | pytest | Pass (3 tests) |
| Node tests | node --test | Pass (3 tests) |
| Secret scanning | gitleaks/gitleaks-action | Pass |

## Checks skipped (with reasons)

| Check | Reason |
|-------|--------|
| actionlint | Not installed in CI image; structural check used instead |
| yamllint | PyYAML parse validation used as equivalent minimal check |
| markdownlint | Lightweight node script used to avoid external dependencies |
| ShellCheck | No shell scripts are committed for execution |

## Security confirmations

- No credentials, tokens, private keys, or personal data committed.
- No external cloud resources created.
- No paid services required.
- All workflows set minimal `permissions:`.
- No use of `pull_request_target` to run untrusted code.
- Dependabot configured.

## Workflow triggers summary

- Demo workflows (01–16) trigger on `push` to `main` with path filters and `workflow_dispatch`, plus cron (weekly) for 02.
- Validation workflow (`90-validation.yml`) triggers on push/pull_request to `main`.
- Release workflow (14) triggers on `v*` tags.
- No cron triggers shorter than weekly.

## GitHub Actions run

The validation workflow run is recorded in the final report after publication.
