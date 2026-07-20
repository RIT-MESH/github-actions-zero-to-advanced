# Validation report

This report records validation results for the repository.

## GitHub Actions runs

| Workflow | Run ID | Result |
|----------|--------|--------|
| Validation (90-validation.yml) | 29718680967 | success |
| 15 - Security Scan (15-security-scan.yml) | 29718680882 | success |

(Initial runs on the first push failed only because `gitleaks-action` could not resolve a base commit on the very first commit. Fixed by running gitleaks directly on the source tree with an example-placeholder allowlist. Both then passed.)

## Checks executed (local + CI)

| Check | Tool | Result |
|-------|------|--------|
| YAML validity | PyYAML (scripts/validate_yaml_json.py) | Pass |
| JSON validity | json module (scripts/validate_yaml_json.py) | Pass |
| Workflow structure | scripts/validate-workflows.py | Pass (17 workflow files) |
| Markdown basic checks | scripts/validate-markdown.js | Pass |
| Python tests | pytest | Pass (3 tests) |
| Node tests | node --test | Pass (3 tests) |
| Secret scanning | gitleaks 8.24.3 (source scan) | Pass |

## Checks skipped (with reasons)

| Check | Reason |
|-------|--------|
| actionlint | Not installed; an equivalent structural parse check is used |
| yamllint | PyYAML parse validation used as a minimal equivalent |
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

- Demo workflows (01–16) trigger on `push` to `main` with path filters and `workflow_dispatch`; workflow 02 also runs weekly via cron.
- Validation workflow (90-validation.yml) triggers on push/pull_request to `main`.
- Release workflow (14) triggers on `v*` tags.
- No cron triggers shorter than weekly.