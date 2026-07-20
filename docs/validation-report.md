# Validation report

This report records validation results for the repository.

## GitHub Actions runs

| Workflow | Trigger | Result |
|----------|---------|--------|
| Validation (`90-validation.yml`) | push / pull_request | success |
| 15 - Security Scan | push / pull_request | success |
| Final Project - Capstone CI/CD | push (self) | success |

## Checks executed (local + CI)

| Check | Tool | Result |
|-------|------|--------|
| YAML validity | PyYAML (scripts/validate_yaml_json.py) | Pass |
| JSON validity | json module (scripts/validate_yaml_json.py) | Pass |
| Workflow structure | scripts/validate-workflows.py | Pass (all workflow files) |
| Markdown basic checks | scripts/validate-markdown.js | Pass |
| Internal Markdown links | scripts/validate-links.py | Pass |
| Python tests | pytest | Pass |
| Python coverage | pytest-cov | Pass (report uploaded) |
| Node tests | node --test | Pass |
| Secret scanning | gitleaks 8.24.3 (checksum-verified) | Pass |
| Workflow schema | actionlint 1.7.7 | Pass |

## Supply-chain measures

- The gitleaks binary is downloaded and its SHA-256 is verified against the published `gitleaks_8.24.3_checksums.txt` before execution.
- The actionlint binary hash is printed for audit.
- All workflows set minimal `permissions:`.
- Workflows set `concurrency:` with `cancel-in-progress: true` and per-job `timeout-minutes:`.

## Checks skipped (with reasons)

| Check | Reason |
|-------|--------|
| yamllint (standalone) | PyYAML parse validation + actionlint used as deeper equivalent |
| markdownlint (standalone) | Lightweight node script used to avoid external dependencies |
| ShellCheck | No shell scripts are committed for execution |
| Trivy Docker scan (strict) | Run as informational (`continue-on-error`) so it reports without failing the teaching pipeline |

## Security confirmations

- No credentials, tokens, private keys, or personal data committed.
- No external cloud resources created (deployment is simulated).
- No paid services required.
- All workflows set minimal `permissions:`.
- No use of `pull_request_target` to run untrusted code.
- Dependabot configured.

## Workflow triggers summary

- Demo workflows (01–18) trigger on `push` to `main` with path filters and `workflow_dispatch`; workflow 02 also runs weekly via cron.
- Validation workflow (`90-validation.yml`) triggers on push/pull_request to `main`.
- Capstone (`final-project.yml`) triggers on push to its own path or `examples/python-app/**`, on `v*` tags, and `workflow_dispatch`.
- Release workflow (14) triggers on `v*` tags.
- No cron triggers shorter than weekly.